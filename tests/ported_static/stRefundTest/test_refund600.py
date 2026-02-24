"""
Ported from:
tests/static/state_tests/stRefundTest/refund600Filler.json
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
    ["tests/static/state_tests/stRefundTest/refund600Filler.json"],
)
@pytest.mark.valid_from("Cancun")
def test_refund600(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x8a0a19589531694250d570040a0c4b74576919b8")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x1000000000000000000000000000000000001000")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    pre[contract] = Account(
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=(
        Op.PUSH1[0x1] + Op.SLOAD + Op.POP + Op.PUSH1[0x2] + Op.SLOAD + Op.POP
        + Op.PUSH2[0xffff] + Op.PUSH1[0x2] + Op.EXP + Op.PUSH1[0xa] + Op.SSTORE
        + Op.ADDRESS + Op.BALANCE + Op.PUSH1[0xb] + Op.SSTORE + Op.PUSH1[0x0]
        + Op.PUSH1[0x1] + Op.SSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x2] + Op.SSTORE
        + Op.PUSH1[0x0] + Op.PUSH1[0x3] + Op.SSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x4]
        + Op.SSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x5] + Op.SSTORE + Op.PUSH1[0x0]
        + Op.PUSH1[0x6] + Op.SSTORE + Op.STOP
    ),
        storage={0x1: 0x1, 0x2: 0x1, 0x3: 0x1, 0x4: 0x1, 0x5: 0x1, 0x6: 0x1},
    )
    pre[coinbase] = Account(balance=0, nonce=1)
    pre[sender] = Account(balance=0x989680, nonce=0)

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
