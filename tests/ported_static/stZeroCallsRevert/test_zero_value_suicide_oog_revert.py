"""
Ported from:
tests/static/state_tests/stZeroCallsRevert/ZeroValue_SUICIDE_OOGRevertFiller.json
"""

import pytest
from execution_testing import (
    Account,
    Address,
    Alloc,
    Environment,
    Hash,
    StateTestFiller,
    Transaction,
)
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


@pytest.mark.ported_from(
    ["tests/static/state_tests/stZeroCallsRevert/ZeroValue_SUICIDE_OOGRevertFiller.json"],
)
@pytest.mark.valid_from("Cancun")
def test_zero_value_suicide_oog_revert(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x1000000000000000000000000000000000001100")
    callee = Address("0x1000000000000000000000000000000000001000")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH20[0x1000000000000000000000000000000000001000] + Op.SELFDESTRUCT
        + Op.STOP
    ),
    )
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH20[0x1000000000000000000000000000000000001000]
        + Op.PUSH2[0x9c40] + Op.CALL + Op.POP + Op.PUSH1[0xc] + Op.PUSH1[0x2]
        + Op.SSTORE + Op.PUSH1[0xc] + Op.PUSH1[0x3] + Op.SSTORE + Op.PUSH1[0xc]
        + Op.PUSH1[0x4] + Op.SSTORE + Op.GAS + Op.PUSH1[0x64] + Op.SSTORE + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0xe8d4a51000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=b"",
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {}

    state_test(env=env, pre=pre, post=post, tx=tx)
