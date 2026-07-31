"""
Verify a STATICCALL's additional gas costs (memory expansion plus the
callee's gas ask) fit the budget while the following SSTORE does not, so
the frame runs out of gas and every pending write reverts.

Ported from:
state_tests/stStaticCall/static_call_OOG_additionalGasCosts1Filler.json

@manually-enhanced: Do not overwrite. Gas budget derived from the fork
(was a pinned 30000); dynamic callee; post asserts the revert.
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

# The legacy ask: granted in full to the code-less callee and returned
# unused, so it is exactly the caller's gas left after the call.
CALLEE_GAS_ASK = 0x1770


@pytest.mark.ported_from(
    [
        "state_tests/stStaticCall/static_call_OOG_additionalGasCosts1Filler.json"  # noqa: E501
    ],
)
@pytest.mark.valid_from("Byzantium")
def test_static_call_oog_additional_gas_costs1(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """Run out of gas on the SSTORE right after a paid-for STATICCALL."""
    callee = pre.nonexistent_account()
    call_code = Op.STATICCALL(
        gas=CALLEE_GAS_ASK,
        address=callee,
        args_size=0x40,
        ret_size=0x40,
        new_memory_size=0x40,
    )
    target = pre.deploy_contract(
        code=Op.SSTORE(key=0x0, value=call_code)
        + Op.SSTORE(key=0x1, value=Op.GAS)
        + Op.STOP,
    )

    # Budget covers the call machinery and the callee's full ask; the ask
    # comes back unused, leaving ~CALLEE_GAS_ASK gas — less than any
    # fork's first-write SSTORE charge, so the first SSTORE OOGs.
    intrinsic = fork.transaction_intrinsic_cost_calculator()()
    gas_limit = intrinsic + call_code.gas_cost(fork) + CALLEE_GAS_ASK
    sstore_cost = Op.SSTORE(
        key_warm=False, original_value=0, new_value=1
    ).gas_cost(fork)
    assert CALLEE_GAS_ASK < sstore_cost, "ask must not fund the SSTORE"

    tx = Transaction(
        sender=pre.fund_eoa(),
        to=target,
        gas_limit=gas_limit,
    )

    post = {
        target: Account(storage={}),
        callee: Account.NONEXISTENT,
    }

    state_test(pre=pre, post=post, tx=tx)
