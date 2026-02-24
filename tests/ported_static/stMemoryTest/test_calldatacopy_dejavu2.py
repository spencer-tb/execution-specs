"""
Ported from:
tests/static/state_tests/stMemoryTest/calldatacopy_dejavu2Filler.json
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
    ["tests/static/state_tests/stMemoryTest/calldatacopy_dejavu2Filler.json"],
)
@pytest.mark.valid_from("Cancun")
def test_calldatacopy_dejavu2(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x1000000000000000000000000000000000001000")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=52949672960,
    )

    pre[contract] = Account(
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=(
        Op.PUSH1[0x42] + Op.PUSH1[0x1f] + Op.MSTORE8 + Op.PUSH2[0x103]
        + Op.PUSH1[0x0] + Op.PUSH1[0x1f] + Op.CALLDATACOPY + Op.PUSH1[0x60]
        + Op.PUSH1[0x0] + Op.MLOAD + Op.EQ + Op.PUSH1[0x1f] + Op.JUMPI
        + Op.PUSH5[0xbadc0ffee] + Op.PUSH1[0xff] + Op.SSTORE + Op.JUMPDEST + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0x271000000000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=b"",
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=10,
    )

    post = {}

    state_test(env=env, pre=pre, post=post, tx=tx)
