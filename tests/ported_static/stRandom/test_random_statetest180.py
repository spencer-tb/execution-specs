"""
Ported from:
tests/static/state_tests/stRandom/randomStatetest180Filler.json
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
    ["tests/static/state_tests/stRandom/randomStatetest180Filler.json"],
)
@pytest.mark.valid_from("Cancun")
def test_random_statetest180(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x1000000000000000000000000000000000001000")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x1000000000000000000000000000000000001100")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[coinbase] = Account(
        balance=46,
        nonce=0,
        code=(
        Op.PUSH1[0x0] + Op.CALLDATALOAD + Op.SLOAD + Op.ISZERO + Op.PUSH1[0x9]
        + Op.JUMPI + Op.STOP + Op.JUMPDEST + Op.PUSH1[0x20] + Op.CALLDATALOAD
        + Op.PUSH1[0x0] + Op.CALLDATALOAD + Op.SSTORE
    ),
    )
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH32[0x10000000000000000000000000000000000000000] + Op.PUSH32[0x1]
        + Op.PREVRANDAO + Op.PUSH32[0xc350] + Op.PUSH32[0x0]
        + Op.PUSH32[0x10000000000000000000000000000000000000000]
        + Op.PUSH32[0x1000000000000000000000000000000000001000]
        + Op.PUSH16[0x11576b693c128a9e0820609c050a219d] + Op.PUSH1[0x0] + Op.MLOAD
        + Op.SSTORE
    ),
    )
    pre[sender] = Account(balance=0xde0b6b3a7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=bytes.fromhex(
            "7f00000000000000000000000100000000000000000000000000000000000000007f0000"
            "000000000000000000000000000000000000000000000000000000000001447f00000000"
            "0000000000000000000000000000000000000000000000000000c3507f00000000000000"
            "000000000000000000000000000000000000000000000000007f00000000000000000000"
            "000100000000000000000000000000000000000000007f00000000000000000000000010"
            "000000000000000000000000000000000010006f11576b693c128a9e0820609c050a219d"
        ),
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=566466109,
    )

    post = {}

    state_test(env=env, pre=pre, post=post, tx=tx)
