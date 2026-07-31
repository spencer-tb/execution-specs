"""
Verify a zero-value STATICCALL to an absent account succeeds without
creating it, then a huge KECCAK256 memory expansion runs the frame out
of gas so every stored gas snapshot reverts.

Ported from:
state_tests/stStaticCall/static_ZeroValue_CALL_OOGRevertFiller.json

@manually-enhanced: Do not overwrite. Gas budget and the OOG guard are
derived from the fork (was a pinned 1350000); dynamic addresses.
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
# unused.
CALLEE_GAS_ASK = 0xEA60
# Hashing this window costs far more than the whole budget below.
KECCAK_SIZE = 0x2FFFFF


@pytest.mark.ported_from(
    ["state_tests/stStaticCall/static_ZeroValue_CALL_OOGRevertFiller.json"],
)
@pytest.mark.valid_from("Byzantium")
def test_static_zero_value_call_oog_revert(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """Revert stored gas snapshots when a KECCAK256 exhausts the frame."""
    callee = pre.nonexistent_account()
    call_code = Op.STATICCALL(gas=CALLEE_GAS_ASK, address=callee)
    keccak_code = Op.SHA3(
        offset=0x0,
        size=KECCAK_SIZE,
        data_size=KECCAK_SIZE,
        new_memory_size=KECCAK_SIZE,
    )
    contract = pre.deploy_contract(
        code=Op.SSTORE(key=0x0, value=Op.GAS)
        + Op.SSTORE(key=0x1, value=call_code)
        + Op.POP(keccak_code)
        + Op.SSTORE(key=0x64, value=Op.GAS)
        + Op.STOP,
    )

    # Budget covers the first SSTORE and the call (whose unused ask comes
    # back), but is far below the KECCAK256's cost, so the frame OOGs
    # there and both stored gas snapshots revert.
    sstore_cost = Op.SSTORE(
        key_warm=False, original_value=0, new_value=1
    ).gas_cost(fork)
    budget = 2 * sstore_cost + call_code.gas_cost(fork) + CALLEE_GAS_ASK
    assert budget < keccak_code.gas_cost(fork), "the KECCAK256 must OOG"
    gas_limit = fork.transaction_intrinsic_cost_calculator()() + budget

    tx = Transaction(
        sender=pre.fund_eoa(),
        to=contract,
        gas_limit=gas_limit,
    )

    post = {
        callee: Account.NONEXISTENT,
        contract: Account(storage={}),
    }

    state_test(pre=pre, post=post, tx=tx)
