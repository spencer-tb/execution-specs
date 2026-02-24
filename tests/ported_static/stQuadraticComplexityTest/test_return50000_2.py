"""
Ported from:
tests/static/state_tests/stQuadraticComplexityTest/Return50000_2Filler.json
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
    ["tests/static/state_tests/stQuadraticComplexityTest/Return50000_2Filler.json"],
)
@pytest.mark.valid_from("Cancun")
@pytest.mark.parametrize(
    "tx_gas_limit",
    [
        150000,
        16000000,
    ],
    ids=['case0', 'case1'],
)
def test_return50000_2(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x1000000000000000000000000000000000001100")
    callee = Address("0x1000000000000000000000000000000000001000")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=8825000000,
    )

    pre[callee] = Account(
        balance=0xfffffffffffff,
        nonce=0,
        code=(
        Op.PUSH2[0xc34f] + Op.CALLDATALOAD + Op.PUSH1[0x0] + Op.MSTORE
        + Op.PUSH1[0x1] + Op.PUSH1[0x0] + Op.MLOAD + Op.RETURN + Op.STOP
    ),
    )
    pre[contract] = Account(
        balance=0xfffffffffffff,
        nonce=0,
        code=(
        Op.JUMPDEST + Op.PUSH2[0xc350] + Op.PUSH1[0x80] + Op.MLOAD + Op.LT
        + Op.ISZERO + Op.PUSH1[0x3f] + Op.JUMPI + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH2[0xc350] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH20[0x1000000000000000000000000000000000001000] + Op.PUSH2[0x61c]
        + Op.CALL + Op.PUSH1[0x0] + Op.SSTORE + Op.PUSH1[0x1] + Op.PUSH1[0x80]
        + Op.MLOAD + Op.ADD + Op.PUSH1[0x80] + Op.MSTORE + Op.PUSH1[0x0] + Op.JUMP
        + Op.JUMPDEST + Op.PUSH1[0x80] + Op.MLOAD + Op.PUSH1[0x1] + Op.SSTORE
        + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0xffffffffffffffffffffffffffffffff, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=b"",
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=10,
    )

    post = {}

    state_test(env=env, pre=pre, post=post, tx=tx)
