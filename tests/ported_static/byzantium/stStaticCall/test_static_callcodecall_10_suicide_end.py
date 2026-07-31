"""
Verify a SELFDESTRUCT to self at the end of a delegated frame under
EIP-6780: the pre-existing account is not deleted, keeps its balance
and storage, and a static call made just before it only fails when its
callee writes storage.

Ported from:
state_tests/stStaticCall/static_callcodecall_10_SuicideEndFiller.json

@manually-enhanced: Do not overwrite. Self-beneficiary expressed as
ADDRESS; the static call's result and a completion canary are stored
and asserted (the ported post checked only the balance).
"""

import pytest
from execution_testing import (
    Account,
    Alloc,
    Hash,
    StateTestFiller,
    Transaction,
)
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"

TARGET_BALANCE = 10**18
CANARY = 0xC0DE


@pytest.mark.ported_from(
    ["state_tests/stStaticCall/static_callcodecall_10_SuicideEndFiller.json"],
)
@pytest.mark.valid_from("Cancun")
@pytest.mark.parametrize("leaf_behavior", ["mstore", "static_violation"])
def test_static_callcodecall_10_suicide_end(
    state_test: StateTestFiller,
    pre: Alloc,
    leaf_behavior: str,
) -> None:
    """Keep a pre-existing account after SELFDESTRUCT to itself."""
    if leaf_behavior == "mstore":
        # Memory-only callee: the static call succeeds.
        leaf = pre.deploy_contract(
            code=Op.MSTORE(offset=0x2, value=0x1) + Op.STOP
        )
    else:
        # Storage write inside the static context: the callee halts and
        # the static call reports failure.
        leaf = pre.deploy_contract(
            code=Op.SSTORE(key=0x2, value=0x1) + Op.STOP
        )
    # Runs in the target's context via DELEGATECALL: records the static
    # call's result (+1 so failure stores a non-zero 1), then
    # self-destructs with itself as the beneficiary.
    delegate = pre.deploy_contract(
        code=Op.SSTORE(
            key=0x2,
            value=Op.ADD(
                0x1,
                Op.STATICCALL(
                    address=Op.CALLDATALOAD(offset=0x0),
                    args_size=0x40,
                    ret_size=0x40,
                ),
            ),
        )
        + Op.SELFDESTRUCT(address=Op.ADDRESS)
        + Op.STOP,
    )
    target = pre.deploy_contract(
        code=Op.MSTORE(offset=0x0, value=Op.CALLDATALOAD(offset=0x0))
        + Op.SSTORE(
            key=0x0,
            value=Op.DELEGATECALL(
                address=delegate, args_size=0x40, ret_size=0x40
            ),
        )
        + Op.SSTORE(key=0x1, value=CANARY)
        + Op.STOP,
        balance=TARGET_BALANCE,
    )

    tx = Transaction(
        sender=pre.fund_eoa(),
        to=target,
        data=Hash(leaf, left_padding=True),
    )

    # EIP-6780: the target pre-existed, so its self-destruct only moves
    # its balance — to itself. Everything survives, and the writes made
    # after the SELFDESTRUCT was registered persist.
    static_call_result = 2 if leaf_behavior == "mstore" else 1
    post = {
        leaf: Account(storage={}),
        target: Account(
            balance=TARGET_BALANCE,
            storage={0: 1, 1: CANARY, 2: static_call_result},
        ),
    }

    state_test(pre=pre, post=post, tx=tx)
