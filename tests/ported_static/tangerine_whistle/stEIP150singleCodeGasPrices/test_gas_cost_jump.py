"""
Measure the gas cost of JUMP, JUMPI (taken and not taken), and JUMPDEST
(by Ori Pomerantz qbzzt1@gmail.com).

Ported from:
state_tests/stEIP150singleCodeGasPrices/gasCostJumpFiller.yml

@manually-enhanced: Do not overwrite. The legacy raw GAS-delta windows
(action-minus-baseline differences) are reframed as one CodeGasMeasure
per case over a CALL to the jump-variant callee, asserting the
fork-derived `call cost + callee body cost` for each.
"""

import pytest
from execution_testing import (
    Account,
    Alloc,
    Bytecode,
    CodeGasMeasure,
    Fork,
    StateTestFiller,
    Transaction,
)
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"

GAS_SLOT = 0x0


@pytest.mark.ported_from(
    ["state_tests/stEIP150singleCodeGasPrices/gasCostJumpFiller.yml"],
)
@pytest.mark.valid_from("Berlin")
@pytest.mark.parametrize(
    "case",
    ["jumpdest", "jump", "jumpi_taken", "jumpi_not_taken"],
)
def test_gas_cost_jump(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    case: str,
) -> None:
    """Measure the gas a CALL to each jump-variant callee consumes."""
    # Every callee executes exactly the opcodes its composite lists: the
    # jump target (pc=0x5) is the JUMPDEST after the pushes, and a
    # not-taken JUMPI falls through to that same JUMPDEST.
    body: Bytecode
    if case == "jumpdest":
        # The legacy baseline: two pushes and two JUMPDESTs.
        body = Op.PUSH1[0x0] * 2 + Op.JUMPDEST * 2 + Op.STOP
    elif case == "jump":
        body = Op.PUSH1[0x0] + Op.JUMP(pc=0x5) + Op.JUMPDEST + Op.STOP
    elif case == "jumpi_taken":
        body = Op.JUMPI(pc=0x5, condition=0x1) + Op.JUMPDEST + Op.STOP
    else:
        body = Op.JUMPI(pc=0x5, condition=0x0) + Op.JUMPDEST + Op.STOP
    callee = pre.deploy_contract(code=body)

    call_code = Op.CALL(address=callee, address_warm=False)
    contract = pre.deploy_contract(
        code=CodeGasMeasure(
            code=call_code,
            extra_stack_items=1,
            sstore_key=GAS_SLOT,
        ),
    )

    tx = Transaction(sender=pre.fund_eoa(), to=contract)

    # The measured window covers the CALL plus what the callee consumed.
    post = {
        contract: Account(
            storage={
                GAS_SLOT: call_code.gas_cost(fork) + body.gas_cost(fork),
            },
        ),
    }

    state_test(pre=pre, post=post, tx=tx)
