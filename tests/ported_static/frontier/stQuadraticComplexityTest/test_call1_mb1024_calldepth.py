"""
Verify a self-call recursion that copies 1MB of call arguments per level:
the quadratic memory cost starves the recursion long before the 1024
depth limit, and only the deepest frame's work reverts.

Ported from:
state_tests/stQuadraticComplexityTest/Call1MB1024CalldepthFiller.json

@manually-enhanced: Do not overwrite. The 250M/882500M gas limits are
impossible under the EIP-7825 cap; the budget is a fixed named constant
and the reached depth is pinned per gas-schedule era (the ported absolute
depth 69 was a function of the old 250M budget). The self-call address is
resolved at runtime instead of a hardcoded self-reference.
"""

import pytest
from execution_testing import (
    Account,
    Alloc,
    Conditional,
    Fork,
    StateTestFiller,
    Transaction,
)
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"

COUNTER_SLOT = 0x0
RESULT_SLOT = 0x1
DEPTH_LIMIT_SLOT = 0x2
# 1MB of call arguments copied per recursion level.
ARGS_SIZE = 0xF4240
DEPTH_LIMIT = 0x400
# Gas withheld by each level before recursing (ported reserve).
GAS_RESERVE = 0xF55C8
# The recursion depth is a function of this budget via the per-level
# memory expansion cost; changing it changes the pinned frame counts.
GAS_BUDGET = 10_000_000
# Too little for even one level's 1MB memory expansion.
STARVED_GAS_BUDGET = 150_000


@pytest.mark.ported_from(
    ["state_tests/stQuadraticComplexityTest/Call1MB1024CalldepthFiller.json"],
)
@pytest.mark.valid_from("Berlin")
@pytest.mark.parametrize("starved", [True, False], ids=["starved", "funded"])
def test_call1_mb1024_calldepth(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    starved: bool,
) -> None:
    """Recurse with 1MB call arguments until the gas budget starves it."""
    # Source: lll
    # { (def 'i 0x80) [[ 0 ]] (+ @@0 1)
    #   (if (LT @@0 1024)
    #       [[ 1 ]] (CALL (- (GAS) 1005000) <self> 0 0 1000000 0 0)
    #       [[ 2 ]] 1 ) }
    target = pre.deploy_contract(
        code=Op.SSTORE(
            key=COUNTER_SLOT, value=Op.ADD(Op.SLOAD(key=COUNTER_SLOT), 0x1)
        )
        + Conditional(
            condition=Op.LT(Op.SLOAD(key=COUNTER_SLOT), DEPTH_LIMIT),
            if_true=Op.SSTORE(
                key=RESULT_SLOT,
                value=Op.CALL(
                    gas=Op.SUB(Op.GAS, GAS_RESERVE),
                    address=Op.ADDRESS,
                    args_size=ARGS_SIZE,
                ),
            ),
            if_false=Op.SSTORE(key=DEPTH_LIMIT_SLOT, value=0x1),
        )
        + Op.STOP,
    )

    # The starved budget cannot pay for the first level's memory expansion,
    # so the whole first frame reverts.
    memory_cost = fork.memory_expansion_gas_calculator()(new_bytes=ARGS_SIZE)
    assert STARVED_GAS_BUDGET < memory_cost, "starved budget must OOG"

    tx = Transaction(
        protected=fork.supports_protected_txs(),
        sender=pre.fund_eoa(),
        to=target,
        gas_limit=STARVED_GAS_BUDGET if starved else GAS_BUDGET,
    )

    if starved:
        post = {target: Account(storage={})}
    else:
        # Completed frames under GAS_BUDGET, pinned per gas-schedule era.
        # EIP-8037 (reservoir 0): the unwind's one zero-to-non-zero store
        # of a call result (~111k with its state spill) exceeds the 63/64
        # retention of the ancestor paying it, reverting two more frames.
        depth = 2 if fork.is_eip_enabled(8037) else 4
        post = {
            target: Account(
                storage={COUNTER_SLOT: depth, RESULT_SLOT: 1},
            ),
        }

    state_test(pre=pre, post=post, tx=tx)
