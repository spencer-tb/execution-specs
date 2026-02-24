"""
Ported from:
tests/static/state_tests/stStaticCall/static_callcodecallcallcode_ABCB_RECURSIVE2Filler.json
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
    ["tests/static/state_tests/stStaticCall/static_callcodecallcallcode_ABCB_RECURSIVE2Filler.json"],
)
@pytest.mark.valid_from("Cancun")
@pytest.mark.parametrize(
    "tx_data_hex, tx_value",
    [
        ("0000000000000000000000001000000000000000000000000000000000001100", 0),
        ("0000000000000000000000001000000000000000000000000000000000001100", 1),
        ("0000000000000000000000001000000000000000000000000000000000001300", 0),
        ("0000000000000000000000001000000000000000000000000000000000001300", 1),
    ],
    ids=['case0', 'case1', 'case2', 'case3'],
)
def test_static_callcodecallcallcode_abcb_recursive2(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    tx_value: int,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x1000000000000000000000000000000000001000")
    callee = Address("0x1000000000000000000000000000000000001100")
    callee_1 = Address("0x1000000000000000000000000000000000001200")
    callee_2 = Address("0x1000000000000000000000000000000000001300")
    callee_3 = Address("0x1000000000000000000000000000000000001400")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=3000000000,
    )

    pre[contract] = Account(
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=(
        Op.PUSH1[0x40] + Op.PUSH1[0x0] + Op.PUSH1[0x40] + Op.PUSH1[0x0]
        + Op.CALLVALUE + Op.PUSH1[0x0] + Op.CALLDATALOAD + Op.PUSH4[0x17d7840]
        + Op.CALLCODE + Op.PUSH1[0x0] + Op.SSTORE + Op.PUSH1[0x1] + Op.PUSH1[0x1]
        + Op.SSTORE + Op.STOP
    ),
    )
    pre[callee] = Account(
        balance=0x2540be400,
        nonce=0,
        code=(
        Op.PUSH1[0x40] + Op.PUSH1[0x0] + Op.PUSH1[0x40] + Op.PUSH1[0x0]
        + Op.PUSH20[0x1000000000000000000000000000000000001200] + Op.PUSH3[0xf4240]
        + Op.STATICCALL + Op.STOP
    ),
    )
    pre[callee_1] = Account(
        balance=0x2540be400,
        nonce=0,
        code=(
        Op.PUSH1[0x40] + Op.PUSH1[0x0] + Op.PUSH1[0x40] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH20[0x1000000000000000000000000000000000001100]
        + Op.PUSH3[0x7a120] + Op.CALLCODE + Op.STOP
    ),
    )
    pre[callee_2] = Account(
        balance=0x2540be400,
        nonce=0,
        code=(
        Op.PUSH1[0x40] + Op.PUSH1[0x0] + Op.PUSH1[0x40] + Op.PUSH1[0x0]
        + Op.PUSH20[0x1000000000000000000000000000000000001400] + Op.PUSH3[0xf4240]
        + Op.STATICCALL + Op.STOP
    ),
    )
    pre[callee_3] = Account(
        balance=0x2540be400,
        nonce=0,
        code=(
        Op.PUSH1[0x40] + Op.PUSH1[0x0] + Op.PUSH1[0x40] + Op.PUSH1[0x0]
        + Op.PUSH1[0x1] + Op.PUSH20[0x1000000000000000000000000000000000001300]
        + Op.PUSH3[0x7a120] + Op.CALLCODE + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0xde0b6b3a7640000, nonce=0)

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=tx_data,
        gas_limit=600000,
        gas_price=10,
        nonce=0,
        value=tx_value,
    )

    post = {}

    state_test(env=env, pre=pre, post=post, tx=tx)
