"""
create fails because init code has stack size >1024.

Ported from:
tests/static/state_tests/stCallCreateCallCodeTest
createInitFailStackSizeLargerThan1024Filler.json
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
        "tests/static/state_tests/stCallCreateCallCodeTest/createInitFailStackSizeLargerThan1024Filler.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_create_init_fail_stack_size_larger_than1024(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Create fails because init code has stack size >1024."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0x0ee6db8c4a76cab3bb0584e06916cea75d307db0")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000000,
    )

    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "7f6103ff6000525b7f0102030405060708090a0102030405060708090a01020304600052"  # noqa: E501
            "7f05060708090a0102600160005103600052600051600657000000000000000000602052"  # noqa: E501
            "604060006001f0ff00"
        ),
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xe04d1ac7ddda0c98397d56a0b501e960d4cd325a39286919ac23c1a07009a869"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=2200000,
        gas_price=10,
        nonce=0,
        value=100000,
    )

    post = {
        contract: Account(
            code=bytes.fromhex(
                "7f6103ff6000525b7f0102030405060708090a0102030405060708090a010203046000527f05060708090a0102600160005103600052600051600657000000000000000000602052604060006001f0ff00"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
