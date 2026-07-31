"""
Measure the gas cost of a BALANCE read of the warm transaction sender.

Ported from:
state_tests/stEIP150singleCodeGasPrices/RawBalanceGasFiller.json

@manually-enhanced: Do not overwrite. The legacy raw GAS-delta window is
reframed as a CodeGasMeasure over the BALANCE opcode, asserting the
fork-derived `balance_code.gas_cost(fork)` (warm: the sender is
pre-warmed as the transaction origin).
"""

import pytest
from execution_testing import (
    Account,
    Alloc,
    CodeGasMeasure,
    Fork,
    StateTestFiller,
    Transaction,
)
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"

GAS_SLOT = 0x1


@pytest.mark.ported_from(
    ["state_tests/stEIP150singleCodeGasPrices/RawBalanceGasFiller.json"],
)
@pytest.mark.valid_from("Berlin")
def test_raw_balance_gas(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """Measure the gas a BALANCE of the warm transaction sender consumes."""
    sender = pre.fund_eoa()
    # The sender is the transaction origin, so its address is warm.
    balance_code = Op.BALANCE(address=sender, address_warm=True)
    target = pre.deploy_contract(
        code=CodeGasMeasure(
            code=balance_code,
            extra_stack_items=1,
            sstore_key=GAS_SLOT,
        ),
    )

    tx = Transaction(sender=sender, to=target)

    post = {target: Account(storage={GAS_SLOT: balance_code.gas_cost(fork)})}

    state_test(pre=pre, post=post, tx=tx)
