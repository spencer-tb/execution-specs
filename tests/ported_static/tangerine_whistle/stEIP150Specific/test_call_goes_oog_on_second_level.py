"""
Verify an innermost-frame OOG (level two) reverts only that frame: both
callers observe the exact gas they were granted and complete normally.

Ported from:
state_tests/stEIP150Specific/CallGoesOOGOnSecondLevelFiller.json

@manually-enhanced: Do not overwrite. The gas_limit and the two stored
GAS observations are derived from the fork (intrinsic calculator and
`Op.GAS.gas_cost`) instead of hardcoded; fill-time asserts guard that
both CALL asks stay below the EIP-150 63/64 clamp so the callees
receive exactly the asked amounts on every fork.
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
DONE_SLOT = 0xC
# Both asks stay below the 63/64 clamp of the granting frame, so each
# callee receives exactly the asked amount and its entry GAS reading is
# a known constant.
FIRST_CALL_GAS = 0x927C0
SECOND_CALL_GAS = 0x493E0
# The top frame's budget after the intrinsic cost; the ported filler ran
# with 2_200_000 gas over a 21_000 intrinsic.
EXECUTION_BUDGET = 2_200_000 - 21_000
# SHA3 over a ~3 MiB memory segment: the expansion cost exceeds the
# innermost frame's grant, so it always goes OOG.
HUGE_SHA3_SIZE = 0x2FFFFF


@pytest.mark.ported_from(
    ["state_tests/stEIP150Specific/CallGoesOOGOnSecondLevelFiller.json"],
)
@pytest.mark.valid_from("Frontier")
def test_call_goes_oog_on_second_level(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """Verify only the OOG frame reverts and callers observe their grant."""
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
        code=entry_store
        + Op.POP(Op.SHA3(offset=0x0, size=HUGE_SHA3_SIZE))
        + Op.SSTORE(key=0x9, value=Op.GAS)
        + Op.SSTORE(key=0xA, value=Op.GAS)
        + Op.STOP,
    )
    call_second = Op.CALL(
        gas=SECOND_CALL_GAS, address=addr_2, address_warm=False
    )
    done_store = Op.SSTORE(
        key=DONE_SLOT,
        value=0x1,
        key_warm=False,
        original_value=0,
        new_value=1,
    )
    addr = pre.deploy_contract(
        code=entry_store
        + Op.SSTORE(key=RESULT_SLOT, value=call_second)
        + done_store
        + Op.STOP,
    )
    call_first = Op.CALL(gas=FIRST_CALL_GAS, address=addr, address_warm=False)
    result_store = Op.SSTORE(
        key=RESULT_SLOT,
        value=call_first,
        key_warm=False,
        original_value=0,
        new_value=1,
    )
    target = pre.deploy_contract(code=entry_store + result_store + Op.STOP)

    gas_limit = fork.transaction_intrinsic_cost_calculator()() + (
        EXECUTION_BUDGET
    )

    # Guard the constructed relationships. The composites price older
    # forks with the Berlin schedule (an overestimate there), so every
    # bound below is conservative on earlier forks.
    top_available = (
        EXECUTION_BUDGET
        - entry_store.gas_cost(fork)
        - call_first.gas_cost(fork)
    )
    assert FIRST_CALL_GAS <= top_available - top_available // 64, (
        "first ask must stay below the 63/64 clamp"
    )
    middle_available = (
        FIRST_CALL_GAS
        - entry_store.gas_cost(fork)
        - call_second.gas_cost(fork)
    )
    assert SECOND_CALL_GAS <= middle_available - middle_available // 64, (
        "second ask must stay below the 63/64 clamp"
    )
    # After the failed inner call, the middle frame must still afford
    # its completion store; the top frame likewise.
    assert middle_available - SECOND_CALL_GAS > done_store.gas_cost(fork)
    assert top_available - FIRST_CALL_GAS > result_store.gas_cost(fork)

    tx = Transaction(
        protected=fork.supports_protected_txs(),
        sender=sender,
        to=target,
        gas_limit=gas_limit,
    )

    # Only the innermost frame reverts (its SHA3 goes OOG); each caller
    # observes exactly the gas it was granted, minus the GAS opcode's
    # own charge, and completes.
    gas_op_cost = Op.GAS.gas_cost(fork)
    post = {
        addr_2: Account(storage={}),
        addr: Account(
            storage={
                ENTRY_SLOT: FIRST_CALL_GAS - gas_op_cost,
                DONE_SLOT: 1,
            },
        ),
        target: Account(
            storage={
                ENTRY_SLOT: EXECUTION_BUDGET - gas_op_cost,
                RESULT_SLOT: 1,
            },
        ),
    }

    state_test(pre=pre, post=post, tx=tx)
