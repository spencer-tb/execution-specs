"""Resolve transaction gas limits from the block gas budget."""

from typing import List

from execution_testing.base_types import HexNumber
from execution_testing.forks import Fork
from execution_testing.test_types import Transaction


def needs_gas_resolution(tx: Transaction) -> bool:
    """Return True if gas_limit was not explicitly set."""
    return "gas_limit" not in tx.model_fields_set


def resolve_gas_limits(
    txs: List[Transaction],
    block_gas_limit: int,
    fork: Fork,
) -> List[Transaction]:
    """
    Assign gas_limit from the block budget to transactions that need it.

    Transactions with an explicit gas_limit are unchanged.  The
    remaining block gas is split evenly across unresolved transactions.
    """
    auto_indices = [
        i for i, tx in enumerate(txs) if needs_gas_resolution(tx)
    ]

    if not auto_indices:
        return txs

    explicit_total = sum(
        int(txs[i].gas_limit)
        for i in range(len(txs))
        if i not in auto_indices
    )

    available = block_gas_limit - explicit_total
    auto_count = len(auto_indices)
    per_tx = available // auto_count
    remainder = available - (per_tx * auto_count)

    tx_gas_cap = fork.transaction_gas_limit_cap()

    resolved: List[Transaction] = list(txs)
    for idx, i in enumerate(auto_indices):
        share = per_tx + (remainder if idx == auto_count - 1 else 0)
        if tx_gas_cap is not None:
            share = min(share, tx_gas_cap)
        resolved[i] = txs[i].model_copy(
            update={"gas_limit": HexNumber(share)}
        )

    return resolved
