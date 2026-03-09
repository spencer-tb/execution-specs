"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stSolidityTest/TestOverflowFiller.json
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
    ["tests/static/state_tests/stSolidityTest/TestOverflowFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_test_overflow(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x73c241c3bc4fdf83b6ff3ae73735fddf7c9d711d")
    contract = Address("0x1a5a251a7e18ebc1a8ebfc47e3f36d9be03f1627")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[contract] = Account(
        balance=0x186A0,
        nonce=0,
        code=bytes.fromhex(
            "6000357c0100000000000000000000000000000000000000000000000000000000900480"  # noqa: E501
            "638040cac41461003a578063c04062261461004c57005b610042610099565b8060005260"  # noqa: E501
            "206000f35b61005461005e565b8060005260206000f35b6000610068610099565b600060"  # noqa: E501
            "006101000a81548160ff02191690830217905550600060009054906101000a900460ff16"  # noqa: E501
            "9050610096565b90565b60006000600060006001935083507fffffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffffffff925060006001840114156100db5761"  # noqa: E501
            "00e4565b6000935061013b565b63ffffffff915060006001830163ffffffff1614156101"  # noqa: E501
            "025761010b565b6000935061013b565b67ffffffffffffffff905060006001820167ffff"  # noqa: E501
            "ffffffffffff1614156101315761013a565b6000935061013b565b5b5050509056"  # noqa: E501
        ),
    )
    pre[sender] = Account(balance=0x12A05F200, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xa9ae12cb2700c0214f86b9796881bc03a1fd5605d0e76d2da2ca592e62d53e52"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex("c0406226"),
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            storage={0: 1},
            code=bytes.fromhex(
                "6000357c0100000000000000000000000000000000000000000000000000000000900480638040cac41461003a578063c04062261461004c57005b610042610099565b8060005260206000f35b61005461005e565b8060005260206000f35b6000610068610099565b600060006101000a81548160ff02191690830217905550600060009054906101000a900460ff169050610096565b90565b60006000600060006001935083507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff925060006001840114156100db576100e4565b6000935061013b565b63ffffffff915060006001830163ffffffff1614156101025761010b565b6000935061013b565b67ffffffffffffffff905060006001820167ffffffffffffffff1614156101315761013a565b6000935061013b565b5b5050509056"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
