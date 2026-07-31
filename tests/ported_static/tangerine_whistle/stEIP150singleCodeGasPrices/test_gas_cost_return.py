"""
Measure that terminating a callee via RETURN costs the same as STOP
(by Ori Pomerantz qbzzt1@gmail.com).

Ported from:
state_tests/stEIP150singleCodeGasPrices/gasCostReturnFiller.yml

@manually-enhanced: Do not overwrite. The legacy raw GAS-delta windows
(whose stored difference was asserted to be zero) are reframed as two
CodeGasMeasure windows over each CALL, asserting the same fork-derived
`call_code.gas_cost(fork)` for both, with the callee addresses threaded
dynamically instead of hardcoded.
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

GAS_SLOT_STOP = 0x0
GAS_SLOT_RETURN = 0x1


@pytest.mark.ported_from(
    ["state_tests/stEIP150singleCodeGasPrices/gasCostReturnFiller.yml"],
)
@pytest.mark.valid_from("Berlin")
def test_gas_cost_return(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """Measure that a callee ending in RETURN costs the same as STOP."""
    # Identical callee bodies except the terminal opcode. RETURN pops the
    # two pushed words as (offset=0xFF, size=0x0); a zero-size RETURN
    # expands no memory, so both callees consume exactly the same gas.
    stop_body = Op.PUSH1[0x0] + Op.PUSH1[0xFF] + Op.STOP
    return_body = Op.PUSH1[0x0] + Op.PUSH1[0xFF] + Op.RETURN
    stop_target = pre.deploy_contract(code=stop_body)
    return_target = pre.deploy_contract(code=return_body)

    call_stop = Op.CALL(address=stop_target, address_warm=False)
    call_return = Op.CALL(address=return_target, address_warm=False)
    contract = pre.deploy_contract(
        code=CodeGasMeasure(
            code=call_stop,
            extra_stack_items=1,
            sstore_key=GAS_SLOT_STOP,
        )
        + CodeGasMeasure(
            code=call_return,
            extra_stack_items=1,
            sstore_key=GAS_SLOT_RETURN,
        ),
    )

    tx = Transaction(sender=pre.fund_eoa(), to=contract)

    # Each measured window covers the CALL plus what its callee consumed;
    # the two expectations are equal by construction (STOP and a
    # zero-size RETURN both cost nothing).
    post = {
        contract: Account(
            storage={
                GAS_SLOT_STOP: call_stop.gas_cost(fork)
                + stop_body.gas_cost(fork),
                GAS_SLOT_RETURN: call_return.gas_cost(fork)
                + return_body.gas_cost(fork),
            },
        ),
    }

    state_test(pre=pre, post=post, tx=tx)
