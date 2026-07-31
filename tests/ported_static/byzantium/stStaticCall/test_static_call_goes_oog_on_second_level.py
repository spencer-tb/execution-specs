"""
Verify a huge KECCAK256 at call depth three exhausts nearly the whole
transaction budget: the intermediate static frame still completes, but
the top frame's 1/64 retentions cannot fund its SSTORE, so it runs out
of gas and every write reverts.

Ported from:
state_tests/stStaticCall/static_CallGoesOOGOnSecondLevelFiller.json

@manually-enhanced: Do not overwrite. Gas budget guarded by fork-derived
asserts (was a pinned 220000); sub-calls forward all gas.
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

# Post-intrinsic execution budget. Small enough that the top frame's
# 1/64 retentions cannot fund an SSTORE (guarded below), large enough to
# reach the depth-three KECCAK256.
GAS_BUDGET = 199_000
# Hashing this window costs far more than the whole budget.
KECCAK_SIZE = 0x2FFFFF


@pytest.mark.ported_from(
    ["state_tests/stStaticCall/static_CallGoesOOGOnSecondLevelFiller.json"],
)
@pytest.mark.valid_from("Byzantium")
def test_static_call_goes_oog_on_second_level(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """Run the top frame out of gas after a nested static call OOGs."""
    keccak_code = Op.SHA3(
        offset=0x0,
        size=KECCAK_SIZE,
        data_size=KECCAK_SIZE,
        new_memory_size=KECCAK_SIZE,
    )
    addr_2 = pre.deploy_contract(code=keccak_code + Op.STOP)
    addr = pre.deploy_contract(
        code=Op.MSTORE(offset=0x8, value=Op.GAS)
        + Op.MSTORE(offset=0x9, value=Op.STATICCALL(address=addr_2))
        + Op.STOP,
    )
    target = pre.deploy_contract(
        code=Op.SSTORE(key=0x9, value=Op.STATICCALL(address=addr))
        + Op.SSTORE(key=0xA, value=Op.GAS)
        + Op.STOP,
    )

    # The depth-three frame burns its whole grant on the KECCAK256; the
    # top frame keeps only its own 1/64 plus the intermediate frame's
    # returned 1/64, which must not fund the first SSTORE.
    sstore_cost = Op.SSTORE(
        key_warm=False, original_value=0, new_value=1
    ).gas_cost(fork)
    assert GAS_BUDGET < keccak_code.gas_cost(fork), "the KECCAK256 must OOG"
    assert GAS_BUDGET // 32 + 100 < sstore_cost, (
        "retained gas must not fund the top frame's SSTORE"
    )
    gas_limit = fork.transaction_intrinsic_cost_calculator()() + GAS_BUDGET

    tx = Transaction(
        sender=pre.fund_eoa(),
        to=target,
        gas_limit=gas_limit,
    )

    post = {
        addr: Account(storage={}),
        addr_2: Account(storage={}),
        target: Account(storage={}),
    }

    state_test(pre=pre, post=post, tx=tx)
