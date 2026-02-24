"""
Ported from:
tests/static/state_tests/stEIP150Specific/NewGasPriceForCodesFiller.json
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
    ["tests/static/state_tests/stEIP150Specific/NewGasPriceForCodesFiller.json"],
)
@pytest.mark.valid_from("Cancun")
def test_new_gas_price_for_codes(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x1000000000000000000000000000000000001200")
    callee = Address("0x1000000000000000000000000000000000001000")
    callee_1 = Address("0x1000000000000000000000000000000000001100")

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
        code=Op.PUSH1[0x11] + Op.PUSH1[0x64] + Op.SSTORE + Op.STOP,
    )
    pre[callee_1] = Account(
        balance=111,
        nonce=0,
        code=bytes.fromhex("1122334455667788991011121314151617181920212223242526272829303132"),
    )
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.GAS + Op.PUSH2[0x3e7] + Op.MSTORE
        + Op.PUSH20[0x1000000000000000000000000000000000001100] + Op.EXTCODESIZE
        + Op.PUSH1[0x1] + Op.SSTORE + Op.PUSH1[0x14] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH20[0x1000000000000000000000000000000000001100] + Op.EXTCODECOPY
        + Op.PUSH1[0x0] + Op.MLOAD + Op.PUSH1[0x2] + Op.SSTORE + Op.PUSH1[0x0]
        + Op.SLOAD + Op.PUSH1[0x4] + Op.SSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x1]
        + Op.PUSH20[0x1000000000000000000000000000000000001000] + Op.PUSH2[0x7530]
        + Op.CALL + Op.PUSH1[0x5] + Op.SSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x1]
        + Op.PUSH20[0x1000000000000000000000000000000000001000] + Op.PUSH2[0x7530]
        + Op.CALLCODE + Op.PUSH1[0x6] + Op.SSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH20[0x1000000000000000000000000000000000001000] + Op.PUSH2[0x7530]
        + Op.DELEGATECALL + Op.PUSH1[0x7] + Op.SSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH20[0x1000000000000000000000000000000000000013] + Op.PUSH2[0x7530]
        + Op.CALL + Op.PUSH1[0x8] + Op.SSTORE
        + Op.PUSH20[0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b] + Op.BALANCE
        + Op.PUSH1[0x3] + Op.SSTORE + Op.GAS + Op.PUSH2[0x3e7] + Op.MLOAD + Op.SUB
        + Op.PUSH1[0xa] + Op.SSTORE + Op.STOP
    ),
        storage={0x0: 0x12},
    )
    pre[sender] = Account(balance=0xe8d4a51000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=b"",
        gas_limit=600000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {}

    state_test(env=env, pre=pre, post=post, tx=tx)
