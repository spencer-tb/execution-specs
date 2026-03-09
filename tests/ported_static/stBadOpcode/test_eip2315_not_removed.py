"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stBadOpcode/eip2315NotRemovedFiller.json
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
    ["tests/static/state_tests/stBadOpcode/eip2315NotRemovedFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_eip2315_not_removed(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xf2f6c03017e58b15115443223a6a0f8a4363b5c1")
    contract = Address("0x147943601b1281618e4d824d11073025cd2ac623")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex("60045e005c60016000555d"),
    )
    pre[sender] = Account(balance=0x7FFFFFFFFFFFFFFF, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x31b5af02b012484ae954b3a43943242ede546a2e76fc0a6acc17435107c385eb"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=400000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(code=bytes.fromhex("60045e005c60016000555d")),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
