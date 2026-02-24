"""
create fails because init code has stack size >1024

Ported from:
tests/static/state_tests/stCallCreateCallCodeTest/createInitFailStackSizeLargerThan1024Filler.json
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
    ["tests/static/state_tests/stCallCreateCallCodeTest/createInitFailStackSizeLargerThan1024Filler.json"],
)
@pytest.mark.valid_from("Cancun")
def test_create_init_fail_stack_size_larger_than1024(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """create fails because init code has stack size >1024."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x1000000000000000000000000000000000001000")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000000,
    )

    pre[contract] = Account(
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=(
        Op.PUSH32[0x6103ff6000525b7f0102030405060708090a0102030405060708090a01020304]
        + Op.PUSH1[0x0] + Op.MSTORE
        + Op.PUSH32[0x5060708090a0102600160005103600052600051600657000000000000000000]
        + Op.PUSH1[0x20] + Op.MSTORE + Op.PUSH1[0x40] + Op.PUSH1[0x0] + Op.PUSH1[0x1]
        + Op.CREATE + Op.SELFDESTRUCT + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0xde0b6b3a7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=b"",
        gas_limit=2200000,
        gas_price=10,
        nonce=0,
        value=100000,
    )

    post = {}

    state_test(env=env, pre=pre, post=post, tx=tx)
