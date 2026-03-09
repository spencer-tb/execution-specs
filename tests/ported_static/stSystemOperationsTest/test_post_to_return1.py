"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stSystemOperationsTest/PostToReturn1Filler.json
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
    [
        "tests/static/state_tests/stSystemOperationsTest/PostToReturn1Filler.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_post_to_return1(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0x3ae2f90d9f77554f1e03d5a4868ca5f0c4e14039")
    callee = Address("0x1ec76f80449bf4d3edf503813e06c0d4373fdf3d")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[callee] = Account(
        balance=23,
        nonce=0,
        code=bytes.fromhex("603760005360026000f2"),
    )
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff600052"  # noqa: E501
            "7faaffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffaa602052"  # noqa: E501
            "60006000604060006017731ec76f80449bf4d3edf503813e06c0d4373fdf3d617530f160"  # noqa: E501
            "0155600160025500"
        ),
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xe04d1ac7ddda0c98397d56a0b501e960d4cd325a39286919ac23c1a07009a869"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=300000,
        gas_price=10,
        nonce=0,
        value=100000,
    )

    post = {
        callee: Account(code=bytes.fromhex("603760005360026000f2")),
        contract: Account(
            storage={2: 1},
            code=bytes.fromhex(
                "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff6000527faaffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffaa60205260006000604060006017731ec76f80449bf4d3edf503813e06c0d4373fdf3d617530f1600155600160025500"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
