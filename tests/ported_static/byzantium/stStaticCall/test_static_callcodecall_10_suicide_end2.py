"""
Verify a SELFDESTRUCT to self at the end of a CALLCODE frame under
EIP-6780: the pre-existing account is not deleted and keeps its whole
balance, including any value the transaction sent it.

Ported from:
state_tests/stStaticCall/static_callcodecall_10_SuicideEnd2Filler.json

@manually-enhanced: Do not overwrite. Self-beneficiary expressed as
ADDRESS; the static call's result and a completion canary are stored
and asserted (the ported post checked only the balance).
"""

import pytest
from execution_testing import (
    Account,
    Alloc,
    StateTestFiller,
    Transaction,
)
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"

TARGET_BALANCE = 10**18
CANARY = 0xC0DE


@pytest.mark.ported_from(
    ["state_tests/stStaticCall/static_callcodecall_10_SuicideEnd2Filler.json"],
)
@pytest.mark.valid_from("Cancun")
@pytest.mark.parametrize("tx_value", [0, 1])
def test_static_callcodecall_10_suicide_end2(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_value: int,
) -> None:
    """Keep a pre-existing account after SELFDESTRUCT to itself."""
    # Memory-only callee: the static call succeeds.
    leaf = pre.deploy_contract(code=Op.MSTORE(offset=0x2, value=0x1) + Op.STOP)
    # Runs in the target's context via CALLCODE: records the static
    # call's result (+1 to distinguish it from a never-written slot),
    # then self-destructs with itself as the beneficiary.
    delegate = pre.deploy_contract(
        code=Op.SSTORE(
            key=0x2,
            value=Op.ADD(
                0x1,
                Op.STATICCALL(address=leaf, args_size=0x40, ret_size=0x40),
            ),
        )
        + Op.SELFDESTRUCT(address=Op.ADDRESS)
        + Op.STOP,
    )
    target = pre.deploy_contract(
        code=Op.SSTORE(
            key=0x0,
            value=Op.CALLCODE(
                address=delegate,
                value=Op.CALLVALUE,
                args_size=0x40,
                ret_size=0x40,
            ),
        )
        + Op.SSTORE(key=0x1, value=CANARY)
        + Op.STOP,
        balance=TARGET_BALANCE,
    )

    tx = Transaction(
        sender=pre.fund_eoa(),
        to=target,
        value=tx_value,
    )

    # EIP-6780: the target pre-existed, so its self-destruct only moves
    # its balance — to itself. The transferred value stays, and the
    # writes made after the SELFDESTRUCT was registered persist.
    post = {
        leaf: Account(storage={}),
        target: Account(
            balance=TARGET_BALANCE + tx_value,
            storage={0: 1, 1: CANARY, 2: 2},
        ),
    }

    state_test(pre=pre, post=post, tx=tx)
