"""
Readable source of the candidate `RECENT_ROOT_CODE`.

The EIP leaves `RECENT_ROOT_CODE` as `TBD`. This module assembles a
candidate runtime code implementing the specified semantics with the
bytecode DSL, so reviewers can read the algorithm instead of the hex; a
test pins the assembled bytes to the constant the spec and the testing
framework install.

Memory layout while hashing (offsets in bytes):

* `0..32`: the entry or storage domain
* `32..64`: the source identifier
* `64..72`: the slot or ring buffer index as an eight-byte big-endian word
* `72..104`: the root (entry preimage only)
* `128..160`: the validation loop's calldata offset
* `160..192`: the tuple's slot
"""

from execution_testing import Bytecode, Conditional, Op, While

from .spec import Spec

OFFSET_PTR = 128
"""Memory word holding the validation loop's calldata offset."""

SLOT_PTR = 160
"""Memory word holding the slot of the tuple being checked."""

MAX_VALIDATION_BYTES = (
    Spec.MAX_RECENT_ROOT_REFERENCES * Spec.RECENT_ROOT_TUPLE_BYTES
)
"""Longest valid validation calldata: sixteen tuples."""

REVERT = Op.REVERT(0, 0)


def _entry_hash(slot: Bytecode | Op, root: Bytecode | Op) -> Bytecode:
    """
    Push the entry hash of the source identifier at memory `32..64`, the
    given slot and root.
    """
    return (
        Op.MSTORE(0, int.from_bytes(Spec.RECENT_ROOT_ENTRY_DOMAIN, "big"))
        + Op.MSTORE(64, Op.SHL(192, slot))
        + Op.MSTORE(72, root)
        + Op.SHA3(0, 104)
    )


def _storage_key(slot: Bytecode | Op) -> Bytecode:
    """
    Push the storage key of the source identifier at memory `32..64` for
    the ring buffer index of the given slot.
    """
    return (
        Op.MSTORE(0, int.from_bytes(Spec.RECENT_ROOT_STORAGE_DOMAIN, "big"))
        + Op.MSTORE(64, Op.SHL(192, Op.MOD(slot, Spec.RECENT_ROOT_LENGTH)))
        + Op.SHA3(0, 72)
    )


def write_operation() -> Bytecode:
    """
    Store `entry_hash(source_id, S, root)` under the storage key of the
    caller's source for the current slot `S`, where the source identifier
    hashes the caller with the salt in calldata `0..32` and the root is
    calldata `32..64`.
    """
    return (
        Op.MSTORE(0, Op.SHL(96, Op.CALLER))
        + Op.MSTORE(20, Op.CALLDATALOAD(0))
        + Op.MSTORE(32, Op.SHA3(0, 52))
        + _entry_hash(Op.SLOTNUM, Op.CALLDATALOAD(32))
        + _storage_key(Op.SLOTNUM)
        + Op.SSTORE
        + Op.STOP
    )


def _check_tuple() -> Bytecode:
    """
    Check the tuple at the calldata offset in `OFFSET_PTR`, reverting
    unless its slot is strictly before the current slot, within the usable
    window, and its entry hash is stored under its storage key.
    """
    offset = Op.MLOAD(OFFSET_PTR)
    slot = Op.MLOAD(SLOT_PTR)
    return (
        Op.MSTORE(32, Op.CALLDATALOAD(offset))
        + Op.MSTORE(SLOT_PTR, Op.SHR(192, Op.CALLDATALOAD(Op.ADD(offset, 32))))
        + Conditional(
            condition=Op.ISZERO(Op.LT(slot, Op.SLOTNUM)),
            if_true=REVERT,
        )
        + Conditional(
            condition=Op.GT(
                Op.SUB(Op.SLOTNUM, slot), Spec.RECENT_ROOT_USABLE_WINDOW
            ),
            if_true=REVERT,
        )
        + Conditional(
            condition=Op.ISZERO(
                Op.EQ(
                    Op.SLOAD(_storage_key(slot)),
                    _entry_hash(slot, Op.CALLDATALOAD(Op.ADD(offset, 40))),
                )
            ),
            if_true=REVERT,
        )
    )


def validation_operation() -> Bytecode:
    """
    Check every 72-byte tuple in calldata, reverting for an empty, a
    misaligned or an oversized calldata and for any failing tuple.
    """
    size = Op.CALLDATASIZE
    return (
        Conditional(
            condition=Op.OR(
                Op.ISZERO(size),
                Op.OR(
                    Op.MOD(size, Spec.RECENT_ROOT_TUPLE_BYTES),
                    Op.GT(size, MAX_VALIDATION_BYTES),
                ),
            ),
            if_true=REVERT,
        )
        + Op.MSTORE(OFFSET_PTR, 0)
        + While(
            body=_check_tuple()
            + Op.MSTORE(
                OFFSET_PTR,
                Op.ADD(Op.MLOAD(OFFSET_PTR), Spec.RECENT_ROOT_TUPLE_BYTES),
            ),
            condition=Op.LT(Op.MLOAD(OFFSET_PTR), size),
        )
        + Op.STOP
    )


def recent_root_code() -> Bytecode:
    """
    Assemble the candidate recent root contract: revert on value, then
    dispatch by calldata length to the write or the validation operation.
    """
    return Conditional(condition=Op.CALLVALUE, if_true=REVERT) + Conditional(
        condition=Op.EQ(Op.CALLDATASIZE, Spec.RECENT_ROOT_WRITE_BYTES),
        if_true=write_operation(),
        if_false=validation_operation(),
    )
