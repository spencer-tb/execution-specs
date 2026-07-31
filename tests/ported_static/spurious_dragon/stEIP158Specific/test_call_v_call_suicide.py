"""
Measure the gas cost of a CALL to a cold contract that SELFDESTRUCTs to
an alive beneficiary, across value-transfer and beneficiary variants.

Ported from:
state_tests/stEIP158Specific/CALL_ZeroVCallSuicideFiller.json
state_tests/stEIP158Specific/CALL_OneVCallSuicideFiller.json
state_tests/stEIP158Specific/CALL_OneVCallSuicide2Filler.json

@manually-enhanced: Do not overwrite. Three CALL_*VCallSuicide fillers
folded into one CodeGasMeasure parametrize; the expectation is the
fork-derived CALL + SELFDESTRUCT composite (minus the returned stipend
on value calls), and the caller-beneficiary is `Op.CALLER` instead of a
hardcoded self-referential address.
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
from execution_testing.forks import Cancun
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"

GAS_SLOT = 0x64
TARGET_BALANCE = 100
# Non-zero so the beneficiary EOA is alive (EIP-158) and stays cold.
BENEFICIARY_BALANCE = 1


@pytest.mark.ported_from(
    [
        "state_tests/stEIP158Specific/CALL_ZeroVCallSuicideFiller.json",
        "state_tests/stEIP158Specific/CALL_OneVCallSuicideFiller.json",
        "state_tests/stEIP158Specific/CALL_OneVCallSuicide2Filler.json",
    ],
)
@pytest.mark.valid_from("Berlin")
@pytest.mark.parametrize(
    "call_value, cold_beneficiary",
    [
        pytest.param(0, False, id="call_zero_v_call_suicide"),
        pytest.param(1, False, id="call_one_v_call_suicide"),
        pytest.param(1, True, id="call_one_v_call_suicide2"),
    ],
)
def test_call_v_call_suicide(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    call_value: int,
    cold_beneficiary: bool,
) -> None:
    """Measure a CALL whose callee SELFDESTRUCTs to an alive account."""
    gas_costs = fork.gas_costs()

    # The beneficiary is either the (warm, alive) caller — read at
    # runtime via CALLER instead of a hardcoded self-address — or a
    # cold, alive EOA; neither triggers a new-account write.
    if cold_beneficiary:
        beneficiary = pre.fund_eoa(amount=BENEFICIARY_BALANCE)
        sd_body = (
            Op.SELFDESTRUCT(
                address=beneficiary, address_warm=False, account_new=False
            )
            + Op.STOP
        )
    else:
        sd_body = (
            Op.SELFDESTRUCT(
                address=Op.CALLER, address_warm=True, account_new=False
            )
            + Op.STOP
        )
    callee = pre.deploy_contract(code=sd_body)

    call_code = Op.CALL(
        address=callee,
        value=call_value,
        address_warm=False,
        value_transfer=call_value > 0,
    )
    target = pre.deploy_contract(
        code=CodeGasMeasure(
            code=call_code,
            extra_stack_items=1,
            sstore_key=GAS_SLOT,
        ),
        balance=TARGET_BALANCE,
    )

    tx = Transaction(
        sender=pre.fund_eoa(),
        to=target,
        state_gas_reservoir=0,
    )

    # The measured window covers the CALL plus the callee's
    # SELFDESTRUCT; a value-bearing CALL hands the callee the stipend,
    # which comes back unused.
    stipend_returned = gas_costs.CALL_STIPEND if call_value > 0 else 0
    measured_gas = (
        call_code.gas_cost(fork) + sd_body.gas_cost(fork) - stipend_returned
    )

    # The callee forwards its whole balance (the transferred value) to
    # the beneficiary; before EIP-6780 (Cancun) it is also destroyed.
    callee_post = Account(balance=0) if fork >= Cancun else Account.NONEXISTENT
    post = {
        callee: callee_post,
        target: Account(
            storage={GAS_SLOT: measured_gas},
            # A caller-beneficiary gets the transferred value back.
            balance=TARGET_BALANCE - (call_value if cold_beneficiary else 0),
        ),
    }
    if cold_beneficiary:
        post[beneficiary] = Account(balance=BENEFICIARY_BALANCE + call_value)

    state_test(pre=pre, post=post, tx=tx)
