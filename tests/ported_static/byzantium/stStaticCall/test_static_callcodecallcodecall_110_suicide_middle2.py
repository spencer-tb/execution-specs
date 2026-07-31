"""
Verify a SELFDESTRUCT to self in the middle of a CALLCODE-CALLCODE
chain halts its frame immediately — the static call after it never
runs — while under EIP-6780 the pre-existing account is not deleted
and the enclosing frames complete normally.

Ported from:
state_tests/stStaticCall/static_callcodecallcodecall_110_SuicideMiddle2Filler.json

@manually-enhanced: Do not overwrite. Self-beneficiary expressed as
ADDRESS; the chain's result and a completion canary are stored and
asserted (the ported post checked only the balance).
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
    [
        "state_tests/stStaticCall/static_callcodecallcodecall_110_SuicideMiddle2Filler.json"  # noqa: E501
    ],
)
@pytest.mark.valid_from("Cancun")
def test_static_callcodecallcodecall_110_suicide_middle2(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Halt a frame at SELFDESTRUCT to self and keep the account."""
    # Never reached: the SELFDESTRUCT before the static call halts the
    # frame first.
    leaf = pre.deploy_contract(code=Op.MSTORE(offset=0x3, value=0x1) + Op.STOP)
    # Runs in the target's context two CALLCODEs deep: self-destructs
    # with itself as the beneficiary, which ends the frame before the
    # static call.
    inner = pre.deploy_contract(
        code=Op.SELFDESTRUCT(address=Op.ADDRESS)
        + Op.STATICCALL(address=leaf, args_size=0x40, ret_size=0x40)
        + Op.STOP,
    )
    outer = pre.deploy_contract(
        code=Op.CALLCODE(
            address=inner,
            value=Op.CALLVALUE,
            args_size=0x40,
            ret_size=0x40,
        )
        + Op.STOP,
    )
    target = pre.deploy_contract(
        code=Op.SSTORE(
            key=0x0,
            value=Op.CALLCODE(
                address=outer,
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
    )

    # SELFDESTRUCT halts its frame successfully, so the chain reports
    # success; EIP-6780 keeps the pre-existing target, whose balance
    # only moved to itself.
    post = {
        leaf: Account(storage={}),
        target: Account(
            balance=TARGET_BALANCE,
            storage={0: 1, 1: CANARY},
        ),
    }

    state_test(pre=pre, post=post, tx=tx)
