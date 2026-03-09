"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stSolidityTest/TestKeywordsFiller.json
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
    ["tests/static/state_tests/stSolidityTest/TestKeywordsFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_test_keywords(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x7f3f285918d9b5e764174551e10b7539b97bbb27")
    contract = Address("0xe7dcb339943a6db535ffe618ec32d1e4e5a50f37")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000,
    )

    pre[sender] = Account(balance=0x5F5E100, nonce=0)
    pre[contract] = Account(
        balance=0x186A0,
        nonce=0,
        code=bytes.fromhex(
            "7c0100000000000000000000000000000000000000000000000000000000600035046338"  # noqa: E501
            "0e439681146037578063c040622614604757005b603d6084565b8060005260206000f35b"  # noqa: E501
            "604d6057565b8060005260206000f35b6000605f6084565b600060006101000a81548160"  # noqa: E501
            "ff0219169083021790555060ff60016000540416905090565b6000808160011560cd575b"  # noqa: E501
            "600a82121560a157600190910190608f565b81600a1460ac5760c9565b50600a5b600081"  # noqa: E501
            "60ff16111560c85760019182900391900360b0565b5b60d5565b6000925060ed565b8160"  # noqa: E501
            "001460e05760e8565b6001925060ed565b600092505b50509056"
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xa2333eef5630066b928dea5fd85a239f511b5b067d1441ee7ac290d0122b917b"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex("c0406226"),
        gas_limit=350000,
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = {
        contract: Account(
            storage={0: 1},
            code=bytes.fromhex(
                "7c01000000000000000000000000000000000000000000000000000000006000350463380e439681146037578063c040622614604757005b603d6084565b8060005260206000f35b604d6057565b8060005260206000f35b6000605f6084565b600060006101000a81548160ff0219169083021790555060ff60016000540416905090565b6000808160011560cd575b600a82121560a157600190910190608f565b81600a1460ac5760c9565b50600a5b60008160ff16111560c85760019182900391900360b0565b5b60d5565b6000925060ed565b8160001460e05760e8565b6001925060ed565b600092505b50509056"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
