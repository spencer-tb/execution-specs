"""
Ported from:
tests/static/state_tests/stRefundTest/refundSuicide50procentCapFiller.json
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
    ["tests/static/state_tests/stRefundTest/refundSuicide50procentCapFiller.json"],
)
@pytest.mark.valid_from("Cancun")
@pytest.mark.parametrize(
    "tx_data_hex",
    [
        "00000000000000000000000000000000000000000000000000000000000001f4",
        "0000000000000000000000000000000000000000000000000000000000010000",
    ],
    ids=['case0', 'case1'],
)
def test_refund_suicide50procent_cap(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x8a0a19589531694250d570040a0c4b74576919b8")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x1000000000000000000000000000000000001000")
    callee = Address("0x1000000000000000000000000000000000001100")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000,
    )

    pre[contract] = Account(
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=(
        Op.GAS + Op.PUSH1[0x16] + Op.MSTORE + Op.PUSH1[0x1] + Op.PUSH1[0xa]
        + Op.SSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH20[0x1000000000000000000000000000000000001100]
        + Op.PUSH1[0x0] + Op.CALLDATALOAD + Op.CALL + Op.PUSH1[0xb] + Op.SSTORE
        + Op.PUSH1[0x0] + Op.PUSH1[0x1] + Op.SSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x2]
        + Op.SSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x3] + Op.SSTORE + Op.PUSH1[0x0]
        + Op.PUSH1[0x4] + Op.SSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x5] + Op.SSTORE
        + Op.PUSH1[0x0] + Op.PUSH1[0x6] + Op.SSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x7]
        + Op.SSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x8] + Op.SSTORE + Op.GAS
        + Op.PUSH1[0x16] + Op.MLOAD + Op.SUB + Op.PUSH1[0x17] + Op.SSTORE + Op.STOP
    ),
        storage={0x1: 0x1, 0x2: 0x1, 0x3: 0x1, 0x4: 0x1, 0x5: 0x1, 0x6: 0x1, 0x7: 0x1, 0x8: 0x1},
    )
    pre[callee] = Account(
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=(
        Op.PUSH20[0x1000000000000000000000000000000000001000] + Op.SELFDESTRUCT
        + Op.STOP
    ),
    )
    pre[coinbase] = Account(balance=0, nonce=1)
    pre[sender] = Account(balance=0x3b9aca00, nonce=0)

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=tx_data,
        gas_limit=10000000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {}

    state_test(env=env, pre=pre, post=post, tx=tx)
