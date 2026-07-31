"""
Measure what a failing callee costs its caller for every call kind and
failure kind: a reverting callee charges only the gas it actually used
before reverting, while out-of-gas, undefined-opcode, bad-jump and
stack failures consume the callee's whole grant.

Ported from:
state_tests/stRevertTest/costRevertFiller.yml

@manually-enhanced: Do not overwrite. The hand-rolled GAS-delta
dispatcher (pinned 2609 delta, 0x2A/0x27 overheads, 80M gas limit that
capped validity at Prague) became a CodeGasMeasure per call kind; the
grant-consumed cases collapse to a sentinel via an in-EVM threshold,
and the revert case asserts the fork-derived cost.
"""

import pytest
from execution_testing import (
    Account,
    Alloc,
    Bytecode,
    CodeGasMeasure,
    Conditional,
    Fork,
    StateTestFiller,
    Transaction,
)
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"

GAS_SLOT = 0x0
# Stored instead of the raw delta when the callee consumed its whole
# grant (the grant depends on the transaction budget, the delta of a
# cheap failure does not).
SENTINEL = 0xFFFFFF
# Any measured delta above this means the callee consumed its grant:
# far above every cheap-failure delta, far below any grant here.
CONSUMED_ALL_THRESHOLD = 0x100000
# Slack the measurer keeps beyond its result SSTORE for the threshold
# collapse logic after the measured call.
COLLAPSE_HEADROOM = 2_000

FAILURE_MODES = [
    "revert",
    "out_of_gas",
    "xtreme_oog",
    "bad_opcode",
    "jump_badly",
    "stack_underflow",
    "stack_overflow",
]
CALL_KINDS = [Op.CALL, Op.DELEGATECALL, Op.STATICCALL, Op.CALLCODE]


@pytest.mark.ported_from(
    ["state_tests/stRevertTest/costRevertFiller.yml"],
)
@pytest.mark.valid_from("Berlin")
@pytest.mark.parametrize("call_kind", CALL_KINDS, ids=lambda op: op._name_)
@pytest.mark.parametrize("failure_mode", FAILURE_MODES)
def test_cost_revert(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    call_kind: Op,
    failure_mode: str,
) -> None:
    """Measure a failing callee's cost to its caller per call kind."""
    revert_code = Op.REVERT(offset=0x0, size=0x10, new_memory_size=0x10)
    callee_code: Bytecode | bytes
    if failure_mode == "revert":
        callee_code = revert_code + Op.STOP
    elif failure_mode == "out_of_gas":
        # Hashing a 16 MiB window costs more than any legal budget.
        callee_code = Op.SHA3(offset=0x0, size=0x1000000) + Op.STOP
    elif failure_mode == "xtreme_oog":
        # A 2**256-1 hash size overflows any gas accounting.
        callee_code = Op.SHA3(offset=0x0, size=Op.SUB(0x0, 0x1)) + Op.STOP
    elif failure_mode == "bad_opcode":
        # 0xBA is undefined on every fork.
        callee_code = b"\xba"
    elif failure_mode == "jump_badly":
        # Position zero is a PUSH, not a JUMPDEST.
        callee_code = Op.JUMP(pc=0x0)
    elif failure_mode == "stack_underflow":
        # LT on an empty stack.
        callee_code = Op.LT + Op.STOP
    else:
        # Each loop iteration leaves one PC value behind until the
        # stack overflows.
        callee_code = Op.JUMPDEST + Op.PC + Op.JUMP(pc=Op.SUB(Op.PC, 0x4))
    callee = pre.deploy_contract(code=callee_code)

    # Ask for everything except what the result SSTORE and the collapse
    # need after the call.
    reserve = (
        Op.SSTORE(key_warm=False, original_value=0, new_value=1).gas_cost(fork)
        + COLLAPSE_HEADROOM
    )
    call_args = {
        "gas": Op.SUB(Op.GAS, reserve),
        "address": callee,
    }
    if call_kind in (Op.CALL, Op.CALLCODE):
        call_args["value"] = 0x0
    call_op = call_kind(**call_args)  # type: ignore[arg-type]
    measurer = pre.deploy_contract(
        code=CodeGasMeasure(
            code=call_op,
            extra_stack_items=1,
            sstore_key=GAS_SLOT,
        )
        + Conditional(
            condition=Op.GT(Op.SLOAD(key=GAS_SLOT), CONSUMED_ALL_THRESHOLD),
            if_true=Op.SSTORE(key=GAS_SLOT, value=SENTINEL),
        )
        + Op.STOP,
    )

    tx = Transaction(
        sender=pre.fund_eoa(),
        to=measurer,
        state_gas_reservoir=0,
    )

    if failure_mode == "revert":
        # A reverting callee refunds all but what it actually used, so
        # the caller pays the call machinery plus the revert's own gas.
        expected = call_op.gas_cost(fork) + revert_code.gas_cost(fork)
        assert expected < CONSUMED_ALL_THRESHOLD, (
            "the cheap-failure delta must stay below the threshold"
        )
    else:
        # Every other failure forfeits the callee's whole grant, which
        # dwarfs the threshold and collapses to the sentinel.
        expected = SENTINEL

    post = {
        measurer: Account(storage={GAS_SLOT: expected}),
        callee: Account(storage={}),
    }

    state_test(pre=pre, post=post, tx=tx)
