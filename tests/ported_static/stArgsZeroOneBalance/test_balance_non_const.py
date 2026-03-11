"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stArgsZeroOneBalance/balanceNonConstFiller.yml
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
    [
        "tests/static/state_tests/stArgsZeroOneBalance/balanceNonConstFiller.yml",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_value, expected_post",
    [
        (
            0,
            {
                Address("0xee6a324b2ece5eacdf881abfdcc62b5361d0fb50"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BALANCE(
                            address=Op.BALANCE(
                                address=0xEE6A324B2ECE5EACDF881ABFDCC62B5361D0FB50  # noqa: E501
                            )
                        ),
                    )
                    + Op.STOP
                )
            },
        ),
        (
            1,
            {
                Address("0xee6a324b2ece5eacdf881abfdcc62b5361d0fb50"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BALANCE(
                            address=Op.BALANCE(
                                address=0xEE6A324B2ECE5EACDF881ABFDCC62B5361D0FB50  # noqa: E501
                            )
                        ),
                    )
                    + Op.STOP
                )
            },
        ),
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_balance_non_const(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_value: int,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x2e3d0156d2b99a6eacba540c55f423c8f5a33143")
    contract = Address("0xee6a324b2ece5eacdf881abfdcc62b5361d0fb50")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)
    # Source: LLL
    # { [[ 0 ]](BALANCE (BALANCE <contract:target:0x095e7baea6a6c7c4c2dfeb977efac326af552d87>)) }  # noqa: E501
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(
                key=0x0,
                value=Op.BALANCE(
                    address=Op.BALANCE(
                        address=0xEE6A324B2ECE5EACDF881ABFDCC62B5361D0FB50,
                    ),
                ),
            )
            + Op.STOP
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xb1f4cbc3a50042184425a6f9e996d0910f7ba879457ce5dac5c71e498ad3c005"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=400000,
        gas_price=10,
        nonce=0,
        value=tx_value,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
