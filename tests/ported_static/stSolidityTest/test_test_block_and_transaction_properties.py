"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stSolidityTest
TestBlockAndTransactionPropertiesFiller.json
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
        "tests/static/state_tests/stSolidityTest/TestBlockAndTransactionPropertiesFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_test_block_and_transaction_properties(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x7f3f285918d9b5e764174551e10b7539b97bbb27")
    contract = Address("0xad24d212286ab785efe98ab6f5a3ecde73054ee5")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[sender] = Account(balance=0x5F5E100, nonce=0)
    pre[contract] = Account(
        balance=0x186A0,
        nonce=0,
        code=bytes.fromhex(
            "60606040526000357c010000000000000000000000000000000000000000000000000000"  # noqa: E501
            "000090048063c040622614610044578063e97384dc1461006957610042565b005b610051"  # noqa: E501
            "600480505061008e565b60405180821515815260200191505060405180910390f35b6100"  # noqa: E501
            "7660048050506100c9565b60405180821515815260200191505060405180910390f35b60"  # noqa: E501
            "006100986100c9565b600060006101000a81548160ff0219169083021790555060006000"  # noqa: E501
            "9054906101000a900460ff1690506100c6565b90565b6000600190508050732adc256650"  # noqa: E501
            "18aa1fe0e6bc666dac8fc2697ff9ba4173ffffffffffffffffffffffffffffffffffffff"  # noqa: E501
            "ff1614151561010d57600090506101f7565b6302b8feb044141515610123576000905061"  # noqa: E501
            "01f7565b677fffffffffffffff4514151561013d57600090506101f7565b607843141515"  # noqa: E501
            "61015057600090506101f7565b6078405042505a50737f3f285918d9b5e764174551e10b"  # noqa: E501
            "7539b97bbb273373ffffffffffffffffffffffffffffffffffffffff1614151561019457"  # noqa: E501
            "600090506101f7565b6064341415156101a757600090506101f7565b60013a1415156101"  # noqa: E501
            "ba57600090506101f7565b737f3f285918d9b5e764174551e10b7539b97bbb273273ffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffff161415156101f657600090506101f7565b5b"  # noqa: E501
            "9056"
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
        value=100,
    )

    post = {
        contract: Account(
            code=bytes.fromhex(
                "60606040526000357c010000000000000000000000000000000000000000000000000000000090048063c040622614610044578063e97384dc1461006957610042565b005b610051600480505061008e565b60405180821515815260200191505060405180910390f35b61007660048050506100c9565b60405180821515815260200191505060405180910390f35b60006100986100c9565b600060006101000a81548160ff02191690830217905550600060009054906101000a900460ff1690506100c6565b90565b6000600190508050732adc25665018aa1fe0e6bc666dac8fc2697ff9ba4173ffffffffffffffffffffffffffffffffffffffff1614151561010d57600090506101f7565b6302b8feb04414151561012357600090506101f7565b677fffffffffffffff4514151561013d57600090506101f7565b60784314151561015057600090506101f7565b6078405042505a50737f3f285918d9b5e764174551e10b7539b97bbb273373ffffffffffffffffffffffffffffffffffffffff1614151561019457600090506101f7565b6064341415156101a757600090506101f7565b60013a1415156101ba57600090506101f7565b737f3f285918d9b5e764174551e10b7539b97bbb273273ffffffffffffffffffffffffffffffffffffffff161415156101f657600090506101f7565b5b9056"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
