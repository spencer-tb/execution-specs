"""
Verify a two-level call chain where the innermost frame goes out of gas
and every caller's retained gas is too small to finish, so no storage
write survives at any level.

Ported from:
state_tests/stEIP150Specific/CallGoesOOGOnSecondLevel2Filler.json

@manually-enhanced: Do not overwrite. The gas budget is derived from the
fork (intrinsic, SSTORE composite, CALL composite) so every level still
reaches its entry store and the cascade still fails on EIP-8037 forks,
where the entry stores' state gas comes from an explicit reservoir.
"""

import pytest
from execution_testing import (
    Account,
    Alloc,
    Fork,
    StateTestFiller,
    Transaction,
)
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"

ENTRY_SLOT = 0x8
RESULT_SLOT = 0x9
# Both CALLs ask for more gas than is ever available, so each callee
# receives all-but-one-64th of the caller's remaining gas (EIP-150).
OVERSIZED_GAS_ASK = 0x927C0
# SHA3 over a ~3 MiB memory segment: the expansion cost exceeds any
# budget this test grants, so the innermost frame always goes OOG.
HUGE_SHA3_SIZE = 0x2FFFFF
# The framework prices every fork with the Berlin schedule, so actual
# pre-Berlin frames run a few thousand gas cheaper than the composite
# estimates and would retain more than intended. Aim the retention this
# far below the halt threshold to absorb that drift.
PRE_BERLIN_DRIFT_HEADROOM = 800


@pytest.mark.ported_from(
    ["state_tests/stEIP150Specific/CallGoesOOGOnSecondLevel2Filler.json"],
)
@pytest.mark.valid_from("Frontier")
def test_call_goes_oog_on_second_level2(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """Verify an innermost-frame OOG starves and reverts every level."""
    gas_costs = fork.gas_costs()
    sender = pre.fund_eoa()

    # Every level starts by storing its remaining gas to a fresh slot.
    entry_store = Op.SSTORE(
        key=ENTRY_SLOT,
        value=Op.GAS,
        key_warm=False,
        original_value=0,
        new_value=1,
    )
    addr_2 = pre.deploy_contract(
        code=entry_store + Op.SHA3(offset=0x0, size=HUGE_SHA3_SIZE) + Op.STOP,
    )
    call_second = Op.CALL(
        gas=OVERSIZED_GAS_ASK, address=addr_2, address_warm=False
    )
    addr = pre.deploy_contract(
        code=entry_store
        + Op.SSTORE(key=RESULT_SLOT, value=call_second)
        + Op.STOP,
    )
    call_first = Op.CALL(
        gas=OVERSIZED_GAS_ASK, address=addr, address_warm=False
    )
    target = pre.deploy_contract(
        code=entry_store
        + Op.SSTORE(key=RESULT_SLOT, value=call_first)
        + Op.STOP,
    )

    # Size the top frame so that, at its CALL, just under
    # CALL_STIPEND * 64 gas remains: the retained 1/64 then cannot cover
    # the post-call SSTORE on any fork (EIP-2200 demands more than the
    # stipend; earlier forks charge 5000), so the frame goes OOG. On
    # EIP-8037 forks the entry stores' state gas is drawn from the
    # reservoir, so the frame arithmetic below holds on every fork.
    entry_exec = entry_store.execution_cost(fork)
    state_gas_reservoir = 3 * entry_store.state_cost(fork)
    top_available = (gas_costs.CALL_STIPEND - PRE_BERLIN_DRIFT_HEADROOM) * 64
    gas_limit = (
        fork.transaction_intrinsic_cost_calculator()()
        + entry_exec
        + call_first.gas_cost(fork)
        + top_available
    )

    # The middle frame must reach its entry store and its own CALL, yet
    # retain too little to finish; the innermost frame must afford its
    # entry store before the SHA3 goes OOG.
    forwarded_first = top_available - top_available // 64
    middle_available = (
        forwarded_first - entry_exec - call_second.gas_cost(fork)
    )
    assert middle_available // 64 <= gas_costs.CALL_STIPEND, (
        "middle frame retention must not cover its post-call SSTORE"
    )
    forwarded_second = middle_available - middle_available // 64
    assert forwarded_second > entry_exec, (
        "innermost frame must afford its entry store"
    )

    tx = Transaction(
        protected=fork.supports_protected_txs(),
        sender=sender,
        to=target,
        gas_limit=gas_limit,
        state_gas_reservoir=state_gas_reservoir,
    )

    # The innermost OOG cascades: every frame fails, so every store is
    # reverted at every level.
    post = {
        addr: Account(storage={}),
        addr_2: Account(storage={}),
        target: Account(storage={}),
    }

    state_test(pre=pre, post=post, tx=tx)
