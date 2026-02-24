"""
Ported from:
tests/static/state_tests/stZeroCallsRevert/ZeroValue_CALL_ToNonZeroBalance_OOGRevertFiller.json
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
    ["tests/static/state_tests/stZeroCallsRevert/ZeroValue_CALL_ToNonZeroBalance_OOGRevertFiller.json"],
)
@pytest.mark.valid_from("Cancun")
def test_zero_value_call_to_non_zero_balance_oog_revert(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x8a0a19589531694250d570040a0c4b74576919b8")
    contract = Address("0x1000000000000000000000000000000000001000")
    callee = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.GAS + Op.PUSH1[0x0] + Op.SSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH20[0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b] + Op.PUSH2[0xea60]
        + Op.CALL + Op.PUSH1[0x1] + Op.SSTORE + Op.PUSH1[0xc] + Op.PUSH1[0x2]
        + Op.SSTORE + Op.PUSH1[0xc] + Op.PUSH1[0x3] + Op.SSTORE + Op.PUSH1[0xc]
        + Op.PUSH1[0x4] + Op.SSTORE + Op.GAS + Op.PUSH1[0x64] + Op.SSTORE + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0xe8d4a51000, nonce=0)
    pre[callee] = Account(balance=100, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x9e7645d0cfd9c3a04eb7a9db59a4eb7d359f2e75c9164a9d6b9a7d54e1b6a36f"
        ),
        to=contract,
        data=b"",
        gas_limit=135000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {}

    state_test(env=env, pre=pre, post=post, tx=tx)
