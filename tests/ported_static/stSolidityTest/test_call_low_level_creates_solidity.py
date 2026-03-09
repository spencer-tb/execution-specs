"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stSolidityTest/CallLowLevelCreatesSolidityFiller.json
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
        "tests/static/state_tests/stSolidityTest/CallLowLevelCreatesSolidityFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_call_low_level_creates_solidity(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x7f3f285918d9b5e764174551e10b7539b97bbb27")
    contract = Address("0x5da6fbe439a0c3ab33f813671a4e7767ee0a263b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000,
    )

    pre[contract] = Account(
        balance=0x186A0,
        nonce=0,
        code=bytes.fromhex(
            "60003560e060020a9004806330debb4214610021578063c04062261461003257005b6100"  # noqa: E501
            "2c6004356100c7565b60006000f35b61003a610044565b8060005260206000f35b600060"  # noqa: E501
            "006001600081905550735da6fbe439a0c3ab33f813671a4e7767ee0a263b600181905550"  # noqa: E501
            "606a6100d2600039606a60006000f0905080600160a060020a03166319ab453c60006000"  # noqa: E501
            "8260e060020a026000526004600154600160a060020a0316815260200160006000866032"  # noqa: E501
            "5a03f16100bc57005b505060005491505090565b80600081905550505600605e80600c60"  # noqa: E501
            "00396000f30060003560e060020a9004806319ab453c14601557005b601e600435602456"  # noqa: E501
            "5b60006000f35b80600160a060020a03166330debb42600060008260e060020a02600052"  # noqa: E501
            "600460e18152602001600060008660325a03f1605957005b50505056"
        ),
    )
    pre[sender] = Account(balance=0x5F5E100, nonce=0)

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
            storage={
                0: 225,
                1: 0x5DA6FBE439A0C3AB33F813671A4E7767EE0A263B,
            },
            code=bytes.fromhex(
                "60003560e060020a9004806330debb4214610021578063c04062261461003257005b61002c6004356100c7565b60006000f35b61003a610044565b8060005260206000f35b600060006001600081905550735da6fbe439a0c3ab33f813671a4e7767ee0a263b600181905550606a6100d2600039606a60006000f0905080600160a060020a03166319ab453c600060008260e060020a026000526004600154600160a060020a03168152602001600060008660325a03f16100bc57005b505060005491505090565b80600081905550505600605e80600c6000396000f30060003560e060020a9004806319ab453c14601557005b601e6004356024565b60006000f35b80600160a060020a03166330debb42600060008260e060020a02600052600460e18152602001600060008660325a03f1605957005b50505056"  # noqa: E501
            ),
        ),
        Address("0xdb95dad3113b9a7b8d67924d5878f2be23c3cedf"): Account(
            code=bytes.fromhex(
                "60003560e060020a9004806319ab453c14601557005b601e6004356024565b60006000f35b80600160a060020a03166330debb42600060008260e060020a02600052600460e18152602001600060008660325a03f1605957005b50505056"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
