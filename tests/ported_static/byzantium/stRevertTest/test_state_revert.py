"""
Verify every kind of frame failure — revert, out-of-gas, huge-size
out-of-gas, undefined opcode, bad jump, stack underflow and stack
overflow — rolls back the failing delegate frame's storage write while
the calling frame keeps its own state and observes the failure.

Ported from:
state_tests/stRevertTest/stateRevertFiller.yml

@manually-enhanced: Do not overwrite. The ported dispatch computed
0x1000+d addresses that no contract occupied, so the failure modes
never executed; the target now delegate-calls the failing contract
directly and stores the observed failure (the ported never-dispatched
guard slot is superseded by this flag). The pinned 2^24 gas limit is
dropped for the maxed default.
"""

import pytest
from execution_testing import (
    Account,
    Alloc,
    Bytecode,
    Fork,
    Hash,
    StateTestFiller,
    Transaction,
)
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"

# Sentinel the target writes before the failing delegate call.
SENTINEL = 0x60A7
# Marker the failing frame writes first; it must never persist.
MARKER = 0x1001
# Gas kept back from the throwaway delegate call to the dead address,
# left for the failure op itself.
DEAD_CALL_RESERVE = 0x7530
# Empty address the failing frame delegate-calls before failing.
DEAD_ADDRESS = 0xDEAD

FAILURE_MODES = [
    "revert",
    "out_of_gas",
    "xtreme_oog",
    "bad_opcode",
    "jump_badly",
    "stack_underflow",
    "stack_overflow",
]


@pytest.mark.ported_from(
    ["state_tests/stRevertTest/stateRevertFiller.yml"],
)
@pytest.mark.valid_from("TangerineWhistle")
@pytest.mark.parametrize("failure_mode", FAILURE_MODES)
def test_state_revert(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    failure_mode: str,
) -> None:
    """Roll back a failing delegate frame and observe the failure."""
    # Common prologue: record a marker (must revert), then make a
    # throwaway delegate call to an empty address, keeping enough gas
    # for the failure op.
    prologue = Op.SSTORE(key=0x1, value=MARKER) + Op.POP(
        Op.DELEGATECALL(
            gas=Op.SUB(Op.GAS, DEAD_CALL_RESERVE), address=DEAD_ADDRESS
        )
    )
    failing_code: Bytecode | bytes
    if failure_mode == "revert":
        failing_code = prologue + Op.REVERT(offset=0x0, size=0x10) + Op.STOP
    elif failure_mode == "out_of_gas":
        # Hashing a 16 MiB window costs more than any legal budget.
        failing_code = prologue + Op.SHA3(offset=0x0, size=0x1000000)
    elif failure_mode == "xtreme_oog":
        # A 2**256-1 hash size overflows any gas accounting.
        failing_code = prologue + Op.SHA3(offset=0x0, size=Op.SUB(0x0, 0x1))
    elif failure_mode == "bad_opcode":
        # 0xBA is undefined on every fork.
        failing_code = bytes(prologue) + b"\xba"
    elif failure_mode == "jump_badly":
        # Position zero is a PUSH, not a JUMPDEST.
        failing_code = prologue + Op.JUMP(pc=0x0)
    elif failure_mode == "stack_underflow":
        # The stack is empty after the prologue's POP.
        failing_code = prologue + Op.ADD + Op.ADD + Op.ADD
    else:
        # Each loop iteration leaves one PC value behind until the
        # stack overflows.
        failing_code = (
            prologue + Op.JUMPDEST + Op.PC + Op.JUMP(pc=Op.SUB(Op.PC, 0x4))
        )
    failing = pre.deploy_contract(code=failing_code)

    # The target writes its sentinel, delegate-calls the failing
    # contract, and stores 1 if (and only if) that frame failed.
    target = pre.deploy_contract(
        code=Op.SSTORE(key=0x0, value=SENTINEL)
        + Op.SSTORE(
            key=0x2,
            value=Op.ISZERO(
                Op.DELEGATECALL(address=Op.CALLDATALOAD(offset=0x0))
            ),
        )
        + Op.STOP,
    )

    tx = Transaction(
        protected=fork.supports_protected_txs(),
        sender=pre.fund_eoa(),
        to=target,
        data=Hash(failing, left_padding=True),
    )

    # The sentinel survives, the failing frame's marker does not, and
    # the observed failure flag is set.
    post = {
        target: Account(storage={0: SENTINEL, 1: 0, 2: 1}),
        failing: Account(storage={}),
    }

    state_test(pre=pre, post=post, tx=tx)
