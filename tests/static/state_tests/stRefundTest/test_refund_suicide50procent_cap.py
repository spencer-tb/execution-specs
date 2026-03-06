"""
Ported from:
tests/static/state_tests/stRefundTest/refundSuicide50procentCapFiller.json

callee code:
    push20 0xa6cc2ca5611255d50118601aa8ece6f124fc4c45
    selfdestruct
    stop

contract code:
    gas
    push1 0x16
    mstore
    push1 0x01
    push1 0x0a
    sstore
    push1 0x00
    push1 0x00
    push1 0x00
    push1 0x00
    push1 0x00
    push20 0x4ff65047ce9c85f968689e4369c10003026a41a9
    push1 0x00
    calldataload
    call
    push1 0x0b
    sstore
    push1 0x00
    push1 0x01
    sstore
    ... (28 more instructions)
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
    "tx_data_hex, expected_post",
    [
    pytest.param(
        "00000000000000000000000000000000000000000000000000000000000001f4",
        {Address("0x095e7baea6a6c7c4c2dfeb977efac326af552d87"): Account(storage={10: 1, 11: 0, 23: 0x107a7}, balance=0xde0b6b3a7640000), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case0",
    ),
    pytest.param(
        "0000000000000000000000000000000000000000000000000000000000010000",
        {Address("0x095e7baea6a6c7c4c2dfeb977efac326af552d87"): Account(storage={10: 1, 11: 1, 23: 0x166fa}, balance=0x1bc16d674ec80000), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case1",
    ),
    ],
)
@pytest.mark.pre_alloc_mutable
def test_refund_suicide50procent_cap(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0xeb201d2887816e041f6e807e804f64f3a7a226fe")
    sender = Address("0xc4a2ca1058df329e5da4755f9921ddaf05cbaa06")
    contract = Address("0xa6cc2ca5611255d50118601aa8ece6f124fc4c45")
    callee = Address("0x4ff65047ce9c85f968689e4369c10003026a41a9")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000,
    )

    pre[callee] = Account(
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=(
        Op.PUSH20[0xa6cc2ca5611255d50118601aa8ece6f124fc4c45] + Op.SELFDESTRUCT
        + Op.STOP
    ),
    )
    pre[contract] = Account(
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=(
        Op.GAS + Op.PUSH1[0x16] + Op.MSTORE + Op.PUSH1[0x1] + Op.PUSH1[0xa]
        + Op.SSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH20[0x4ff65047ce9c85f968689e4369c10003026a41a9]
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
    pre[sender] = Account(balance=0x3b9aca00, nonce=0)
    pre[coinbase] = Account(balance=0, nonce=1)

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0xf79127a3004abde26a4cbd80c428cb10f829fa11b54d36e7b326f4f4a5927acf"
        ),
        to=contract,
        data=tx_data,
        gas_limit=10000000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
