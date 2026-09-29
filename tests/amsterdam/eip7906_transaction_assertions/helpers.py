"""Helpers for EIP-7906 transaction assertion tests."""

from typing import Any, Dict, List

from execution_testing import (
    EOA,
    Address,
    Bytecode,
    Conditional,
    Frame,
    FrameReceipt,
    Op,
    Transaction,
    TransactionReceipt,
)

from tests.amsterdam.eip8141_frame_transactions.helpers import verify_frame
from tests.amsterdam.eip8141_frame_transactions.spec import Spec as Spec8141

from .spec import Spec

BODY_FRAME_GAS = 500_000
"""
Execution gas budget of the execution-body frames: ample for the
storage writes, contract creations and logs the bodies perform. State
charges draw from each frame's separate state gas budget.
"""

ASSERTION_FRAME_GAS = 500_000
"""
Execution gas budget of the `POST_TX` frames: ample for an assertion
enumerating every table of a small diff.
"""

SLOT_MARKER = 0x01
"""Storage slot a probe writes before a read that is expected to halt."""

MARKER = 0xFF
"""The value a probe writes into `SLOT_MARKER`."""


def as_int(address: Address | EOA) -> int:
    """Return an address as the integer the opcodes push it as."""
    return int.from_bytes(address, "big")


def post_tx_frame(**overrides: Any) -> Frame:
    """
    Return a `POST_TX` frame, the trailing assertion frame.

    Keyword arguments override the corresponding frame fields, for
    variants that differ from the canonical frame in a single field.
    """
    kwargs: Dict[str, Any] = dict(
        mode=Spec.MODE_POST_TX,
        gas_limit=ASSERTION_FRAME_GAS,
    )
    kwargs.update(overrides)
    return Frame(**kwargs)


def body_frame(**overrides: Any) -> Frame:
    """
    Return a `SENDER` frame of the execution body with the body gas
    budget.

    Keyword arguments override the corresponding frame fields.
    """
    kwargs: Dict[str, Any] = dict(
        mode=Spec8141.MODE_SENDER,
        gas_limit=BODY_FRAME_GAS,
    )
    kwargs.update(overrides)
    return Frame(**kwargs)


def expect_eq(value: Bytecode | Op, expected: Any) -> Bytecode:
    """
    Return bytecode that reverts unless `value` evaluates to `expected`.

    An assertion contract is a sequence of these checks followed by
    `STOP`: the `POST_TX` frame succeeds only when every check holds,
    which the body's committed effects and the frame's receipt status
    then make observable.
    """
    return Conditional(
        condition=Op.EQ(value, expected),
        if_false=Op.REVERT(0, 0),
    )


def measured_gas(
    probe: Bytecode | Op, *, pushes_result: bool = True
) -> Bytecode:
    """
    Return bytecode that leaves the execution gas consumed by `probe`
    on the stack, including the probe's own operand pushes.

    The measurement brackets the probe with `GAS` reads: the first read
    is taken after its own charge and the second after its own, so the
    difference is the probe's operand pushes, the probe, the `POP` of
    its result when it pushes one, and the second `GAS`. Callers add
    that overhead with `probe_overhead`.
    """
    code = Op.GAS + probe
    if pushes_result:
        code += Op.POP
    return code + Op.GAS + Op.SWAP1 + Op.SUB


def probe_overhead(
    gas_costs: Any, operand_pushes: int, *, pushes_result: bool = True
) -> int:
    """
    Return the gas `measured_gas` adds around a probe: the operand
    pushes, the `POP` of a pushed result, and the closing `GAS`.
    """
    overhead = operand_pushes * gas_costs.VERY_LOW + gas_costs.BASE
    if pushes_result:
        overhead += gas_costs.BASE
    return overhead


def assertion_transaction(
    sender: EOA,
    body: List[Frame],
    assertion: Address | List[Address],
    frame_receipts: List[FrameReceipt] | None = None,
    **overrides: Any,
) -> Transaction:
    """
    Return a frame transaction whose validation prefix is the sender's
    default-code `VERIFY` frame, followed by the body frames and one
    `POST_TX` frame per assertion contract, a single one usually.
    """
    assertions = assertion if isinstance(assertion, list) else [assertion]
    kwargs: Dict[str, Any] = dict(
        sender=sender,
        frames=[
            verify_frame(),
            *body,
            *[post_tx_frame(target=target) for target in assertions],
        ],
    )
    if frame_receipts is not None:
        kwargs["expected_receipt"] = TransactionReceipt(
            payer=sender, frame_receipts=frame_receipts
        )
    kwargs.update(overrides)
    return Transaction(**kwargs)


def success_receipts(count: int) -> List[FrameReceipt]:
    """Return `count` frame receipts expecting success."""
    return [FrameReceipt(status=Spec8141.STATUS_SUCCESS) for _ in range(count)]


def reverted_body_receipts(body_count: int) -> List[FrameReceipt]:
    """
    Return the receipts of a transaction whose single `POST_TX` frame
    failed: the `VERIFY` frame succeeded, the body frames keep their
    success status with their logs emptied, and the assertion frame
    failed.
    """
    return [
        FrameReceipt(status=Spec8141.STATUS_SUCCESS),
        *[
            FrameReceipt(status=Spec8141.STATUS_SUCCESS, logs=[])
            for _ in range(body_count)
        ],
        FrameReceipt(status=Spec8141.STATUS_FAILURE),
    ]
