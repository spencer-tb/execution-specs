"""
Measure the gas cost of EXP as the exponent byte length grows
(by Ori Pomerantz qbzzt1@gmail.com).

Ported from:
state_tests/stEIP150singleCodeGasPrices/gasCostExpFiller.yml

@manually-enhanced: Do not overwrite. The legacy raw GAS-delta window is
reframed as a CodeGasMeasure over the EXP opcode, asserting the
fork-derived `exp_code.gas_cost(fork)` (base plus a per-byte charge on
the exponent's minimal byte length).
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

GAS_SLOT = 0x0

# Exponents straddling each byte-length boundary (0, 1, 2, 3, and 4
# bytes), so the per-byte charge is exercised on both sides of each step.
EXPONENTS = [
    0x0,
    0x1,
    0xFF,
    0x100,
    0xFFFF,
    0x10000,
    0xFFFFFF,
    0x1000000,
    0xFFFFFFFF,
]


@pytest.mark.ported_from(
    ["state_tests/stEIP150singleCodeGasPrices/gasCostExpFiller.yml"],
)
@pytest.mark.valid_from("SpuriousDragon")
@pytest.mark.parametrize(
    "exponent", EXPONENTS, ids=lambda e: f"exponent_{e:#x}"
)
def test_gas_cost_exp(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    exponent: int,
) -> None:
    """Measure the gas EXP consumes for each exponent byte length."""
    exp_code = Op.EXP(2, exponent, exponent=exponent)
    contract = pre.deploy_contract(
        code=CodeGasMeasure(
            code=exp_code,
            extra_stack_items=1,
            sstore_key=GAS_SLOT,
        ),
    )

    tx = Transaction(
        protected=fork.supports_protected_txs(),
        sender=pre.fund_eoa(),
        to=contract,
    )

    post = {contract: Account(storage={GAS_SLOT: exp_code.gas_cost(fork)})}

    state_test(pre=pre, post=post, tx=tx)
