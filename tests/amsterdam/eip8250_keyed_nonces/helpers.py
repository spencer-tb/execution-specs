"""Helpers for EIP-8250 keyed nonce tests."""

from typing import Sequence

from execution_testing import Account, Alloc, Fork, Transaction

from ..eip8141_frame_transactions.helpers import default_code_frame_gas
from .spec import Spec, keyed_nonce_slot

NONCE_KEY = 0xBEEF
"""A non-zero nonce key selecting a keyed domain."""

OTHER_KEY = 0xCAFE
"""A second non-zero nonce key, disjoint from `NONCE_KEY`."""


def nonce_fields(tx: Transaction) -> tuple[Sequence[int], int]:
    """
    Return the transaction's nonce keys and sequence as integers, for
    the fork gas calculators.
    """
    return (
        [int(key) for key in tx.rlp_nonce_keys],
        int(tx.rlp_nonce_seq),
    )


def verify_only_tx_gas_used(
    fork: Fork, tx: Transaction, first_uses: int
) -> int:
    """
    Return the gas a transaction made of default-code `VERIFY` frames
    resolving to its sender settles at.

    Each frame's only execution charge is the sender's warm access at
    frame entry, so the execution dimension is the intrinsic cost plus
    one warm access per frame, held to the calldata floor — which binds
    for these signature-heavy, execution-light transactions. The nonce
    transition's state gas, one storage set per keyed domain used for
    the first time, is paid on top of the floor.
    """
    tx.sign()
    assert tx.frames is not None and tx.signatures is not None
    nonce_keys, nonce_seq = nonce_fields(tx)
    intrinsic = fork.frame_transaction_intrinsic_cost_calculator()(
        frames=tx.frames,
        signatures=tx.signatures,
        sender=tx.sender,
        nonce_keys=nonce_keys,
        nonce_seq=nonce_seq,
        return_cost_deducted_prior_execution=True,
    )
    floor = fork.frame_transaction_data_floor_cost_calculator()(
        frames=tx.frames,
        signatures=tx.signatures,
        sender=tx.sender,
        nonce_keys=nonce_keys,
        nonce_seq=nonce_seq,
    )
    execution_used = intrinsic + len(tx.frames) * default_code_frame_gas(
        fork, target_warm=True
    )
    state_used = first_uses * fork.gas_costs().KEYED_NONCE_FIRST_USE
    return max(execution_used, floor) + state_used


def nonce_manager_with_slots(pre: Alloc, slots: dict[int, int]) -> None:
    """
    Seed the nonce manager's storage in the pre-state, keeping its
    activation code and nonce; the test must be `pre_alloc_mutable`.
    """
    pre[Spec.NONCE_MANAGER] = Account(
        nonce=Spec.NONCE_MANAGER_NONCE,
        code=Spec.NONCE_MANAGER_CODE,
        storage=slots,
    )


def used_key_slots(
    sender: Account | bytes, keys_to_seq: dict[int, int]
) -> dict[int, int]:
    """
    Return the nonce manager slots holding the given current sequences
    of `sender`'s keys, keyed by slot.
    """
    return {
        keyed_nonce_slot(sender, key): seq  # type: ignore[arg-type]
        for key, seq in keys_to_seq.items()
    }
