"""
https://github.com/ethereum/tests/issues/652

Ported from:
tests/static/state_tests/stExtCodeHash/callToNonExistentFiller.json
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
    ["tests/static/state_tests/stExtCodeHash/callToNonExistentFiller.json"],
)
@pytest.mark.valid_from("Cancun")
@pytest.mark.parametrize(
    "tx_data_hex",
    [
        "0000000000000000000000001000000000000000000000000000000000001300",
        "0000000000000000000000001000000000000000000000000000000000001200",
        "0000000000000000000000001000000000000000000000000000000000001100",
        "0000000000000000000000001000000000000000000000000000000000001000",
    ],
    ids=['case0', 'case1', 'case2', 'case3'],
)
def test_call_to_non_existent(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
) -> None:
    """https://github.com/ethereum/tests/issues/652."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x1000000000000000000000000000000000001400")
    callee = Address("0x1000000000000000000000000000000000001000")
    callee_1 = Address("0x1000000000000000000000000000000000001100")
    callee_2 = Address("0x1000000000000000000000000000000000001200")
    callee_3 = Address("0x1000000000000000000000000000000000001300")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=3000000000,
    )

    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH20[0xdead000000000000000000000000000000000001] + Op.PUSH2[0x61a8]
        + Op.STATICCALL + Op.PUSH1[0x0] + Op.SSTORE
        + Op.PUSH20[0xdead000000000000000000000000000000000001] + Op.EXTCODEHASH
        + Op.PUSH1[0x1] + Op.SSTORE + Op.STOP
    ),
    )
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH20[0xdead000000000000000000000000000000000001] + Op.PUSH2[0x61a8]
        + Op.DELEGATECALL + Op.PUSH1[0x0] + Op.SSTORE
        + Op.PUSH20[0xdead000000000000000000000000000000000001] + Op.EXTCODEHASH
        + Op.PUSH1[0x1] + Op.SSTORE + Op.STOP
    ),
    )
    pre[callee_2] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH20[0xdead000000000000000000000000000000000001]
        + Op.PUSH2[0x61a8] + Op.CALLCODE + Op.PUSH1[0x0] + Op.SSTORE
        + Op.PUSH20[0xdead000000000000000000000000000000000001] + Op.EXTCODEHASH
        + Op.PUSH1[0x1] + Op.SSTORE + Op.STOP
    ),
    )
    pre[callee_3] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH20[0xdead000000000000000000000000000000000001]
        + Op.PUSH2[0x61a8] + Op.CALL + Op.PUSH1[0x0] + Op.SSTORE
        + Op.PUSH20[0xdead000000000000000000000000000000000001] + Op.EXTCODEHASH
        + Op.PUSH1[0x1] + Op.SSTORE + Op.STOP
    ),
    )
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH1[0x40] + Op.PUSH1[0x0] + Op.PUSH1[0x40] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.CALLDATALOAD + Op.GAS + Op.CALLCODE
        + Op.STOP
    ),
        storage={0x1: 0x1122},
    )
    pre[sender] = Account(balance=0xde0b6b3a7640000, nonce=0)

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=tx_data,
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = {}

    state_test(env=env, pre=pre, post=post, tx=tx)
