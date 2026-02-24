"""
Ported from:
tests/static/state_tests/stSystemOperationsTest/Call10Filler.json
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
    ["tests/static/state_tests/stSystemOperationsTest/Call10Filler.json"],
)
@pytest.mark.valid_from("Cancun")
def test_call10(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    sender = Address("0x8a0a19589531694250d570040a0c4b74576919b8")
    contract = Address("0x1000000000000000000000000000000000001000")
    callee = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[contract] = Account(
        balance=1000,
        nonce=0,
        code=(
        Op.JUMPDEST + Op.PUSH1[0xa] + Op.PUSH1[0x80] + Op.MLOAD + Op.LT + Op.ISZERO
        + Op.PUSH1[0x42] + Op.JUMPI + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH2[0xc350]
        + Op.PUSH1[0x0] + Op.PUSH1[0x1]
        + Op.PUSH20[0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b]
        + Op.PUSH6[0xfffffffffff] + Op.CALL + Op.PUSH1[0x0] + Op.SSTORE
        + Op.PUSH1[0x1] + Op.PUSH1[0x80] + Op.MLOAD + Op.ADD + Op.PUSH1[0x80]
        + Op.MSTORE + Op.PUSH1[0x0] + Op.JUMP + Op.JUMPDEST + Op.PUSH1[0x80]
        + Op.MLOAD + Op.PUSH1[0x1] + Op.SSTORE + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0xffffffffffffffffffffffffffffffff, nonce=0)
    pre[callee] = Account(balance=7000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x9e7645d0cfd9c3a04eb7a9db59a4eb7d359f2e75c9164a9d6b9a7d54e1b6a36f"
        ),
        to=contract,
        data=b"",
        gas_limit=200000,
        gas_price=10,
        nonce=0,
        value=10,
    )

    post = {}

    state_test(env=env, pre=pre, post=post, tx=tx)
