"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stSpecialTest/makeMoneyFiller.json
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
    ["tests/static/state_tests/stSpecialTest/makeMoneyFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_make_money(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xc4a2ca1058df329e5da4755f9921ddaf05cbaa06")
    contract = Address("0x56f6da36928bffd1fdb9eade8a5b8baffde0dea4")
    callee = Address("0x802edccf6cde9162a05fd89cdfcd8dc4a230b978")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "7b601080600c6000396000f2006000355415600957006020356000355560005260006000"  # noqa: E501
            "60006000601773802edccf6cde9162a05fd89cdfcd8dc4a230b9787fffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffffffffffffecf100"
        ),
    )
    pre[callee] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex("600160015532600255"),
    )
    pre[sender] = Account(balance=0x3B9ACA00, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xf79127a3004abde26a4cbd80c428cb10f829fa11b54d36e7b326f4f4a5927acf"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=228500,
        gas_price=10,
        nonce=0,
        value=10,
    )

    post = {
        contract: Account(
            code=bytes.fromhex(
                "7b601080600c6000396000f200600035541560095700602035600035556000526000600060006000601773802edccf6cde9162a05fd89cdfcd8dc4a230b9787fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffecf100"  # noqa: E501
            ),
        ),
        callee: Account(
            storage={
                1: 1,
                2: 0xC4A2CA1058DF329E5DA4755F9921DDAF05CBAA06,
            },
            code=bytes.fromhex("600160015532600255"),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
