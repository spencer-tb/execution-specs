"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stMemoryTest/codecopy_dejavu2Filler.json
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

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


@pytest.mark.ported_from(
    ["tests/static/state_tests/stMemoryTest/codecopy_dejavu2Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_codecopy_dejavu2(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x894d19064bdc4e212b2e634e18a2b765d52e9b54")
    contract = Address("0xc165257d26f9435cbd00d8e2825ff173393d3b31")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=52949672960,
    )

    pre[sender] = Account(balance=0x271000000000, nonce=0)
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex("600a68010000000000000001601f3900"),
    )

    tx = Transaction(
        secret_key=Hash(
            "0x7dd1d0ec78fe936b0e88f8c21226f51f048579915c7baff1c5d7fd84b2139bf1"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=10,
    )

    post = {
        contract: Account(
            code=bytes.fromhex("600a68010000000000000001601f3900"),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
