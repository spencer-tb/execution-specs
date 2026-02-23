"""Automatic gas limit resolver for auto_gas-annotated transactions."""

from __future__ import annotations

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from execution_testing.forks.base_fork import BaseFork
    from execution_testing.test_types.block_types import Environment
    from execution_testing.test_types.transaction_types import Transaction


class AutoGasBudgetError(Exception):
    """Raised when auto_gas cannot assign a valid gas limit."""

    pass


def resolve_auto_gas(
    fork: type[BaseFork],
    env: Environment,
    txs: List[Transaction],
) -> None:
    """
    Resolve auto_gas metadata to concrete gas limits before signing.

    Mutates txs[i].gas_limit in-place for transactions with auto_gas set.
    """
    auto_indices = [i for i, tx in enumerate(txs) if tx.auto_gas is not None]

    if not auto_indices:
        return

    # Block context for transition-fork-aware lookups
    bn, ts = env.number, env.timestamp

    # --- Guards ---

    for i in auto_indices:
        tx = txs[i]
        if tx.secret_key is None:
            raise AutoGasBudgetError(
                "auto_gas requires a re-signable tx (secret_key must be set). "
                "Pre-signed txs need explicit gas_limit."
            )
        if tx.error is not None:
            raise AutoGasBudgetError(
                f"auto_gas cannot be used with tx.error={tx.error}. "
                "Intentional failure tests need explicit gas_limit."
            )
        if tx.expected_receipt and tx.expected_receipt.gas_used is not None:
            raise AutoGasBudgetError(
                "auto_gas cannot be used with expected_receipt.gas_used. "
                "Gas-exact tests need explicit gas_limit."
            )
        if (
            tx.expected_receipt
            and tx.expected_receipt.cumulative_gas_used is not None
        ):
            raise AutoGasBudgetError(
                "auto_gas cannot be used with "
                "expected_receipt.cumulative_gas_used. "
                "Gas-exact tests need explicit gas_limit."
            )

    cap_mode = fork.tx_gas_cap_mode(block_number=bn, timestamp=ts)
    cap_value = fork.tx_gas_cap_value(block_number=bn, timestamp=ts)
    explicit_sum = sum(
        txs[i].gas_limit for i in range(len(txs)) if i not in auto_indices
    )

    # --- Pre-loop sanity checks ---

    if explicit_sum > env.gas_limit:
        raise AutoGasBudgetError(
            f"Explicit tx gas ({explicit_sum}) already exceeds "
            f"block gas limit ({env.gas_limit})."
        )

    if cap_mode == "hard_total":
        for i in auto_indices:
            if txs[i].auto_gas.min_reservoir:
                raise AutoGasBudgetError(
                    f"min_reservoir={txs[i].auto_gas.min_reservoir} requested "
                    f"but fork {fork} has a hard tx gas cap. "
                    "Use explicit gas_limit."
                )

    # --- Pass 1: compute per-tx minimum gas ---

    minimums: dict[int, int] = {}
    for i in auto_indices:
        tx = txs[i]
        intrinsic = fork.transaction_intrinsic_cost_calculator(
            block_gas_limit=env.gas_limit,
            block_number=bn,
            timestamp=ts,
        )(
            calldata=tx.data,
            contract_creation=tx.to is None,
            access_list=tx.access_list,
            authorization_list_or_count=tx.authorization_list,
        )
        intrinsic_state = fork.transaction_intrinsic_state_gas(
            block_gas_limit=env.gas_limit,
            contract_creation=tx.to is None,
            authorization_count=len(tx.authorization_list or []),
        )
        intrinsic_total = intrinsic + intrinsic_state

        if cap_mode == "regular_only" and tx.auto_gas.min_reservoir:
            required_exec_for_res = max(0, cap_value - intrinsic) + tx.auto_gas.min_reservoir
            floor = intrinsic_total + required_exec_for_res
        else:
            floor = intrinsic_total

        minimums[i] = floor

    reserved = sum(minimums.values())
    remaining = env.gas_limit - explicit_sum

    if reserved > remaining:
        raise AutoGasBudgetError(
            f"Minimum gas for auto txs ({reserved}) exceeds available "
            f"budget ({remaining}). Use explicit gas_limit."
        )

    # --- Pass 2: distribute remaining budget above minimums ---

    surplus = remaining - reserved
    n = len(auto_indices)
    plan: dict[int, int] = {}

    for j, i in enumerate(auto_indices):
        if j == n - 1:
            bonus = surplus
        else:
            bonus = surplus // (n - j)
            surplus -= bonus

        share = minimums[i] + bonus

        if cap_mode == "hard_total":
            share = min(share, cap_value)

        plan[i] = share

    # --- Apply atomically ---

    for i, gas_limit in plan.items():
        txs[i].gas_limit = gas_limit
