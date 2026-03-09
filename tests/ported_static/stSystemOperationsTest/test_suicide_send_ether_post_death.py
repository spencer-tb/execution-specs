"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stSystemOperationsTest
suicideSendEtherPostDeathFiller.json
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
        "tests/static/state_tests/stSystemOperationsTest/suicideSendEtherPostDeathFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_suicide_send_ether_post_death(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x2e3d0156d2b99a6eacba540c55f423c8f5a33143")
    contract = Address("0xa997455dca526734f5607f7c452de0cfb9af19f4")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "60606040526000357c010000000000000000000000000000000000000000000000000000"  # noqa: E501
            "00009004806335f46994146100445780634d536fe31461005157610042565b005b61004f"  # noqa: E501
            "600450610072565b005b61005c60045061008d565b604051808281526020019150506040"  # noqa: E501
            "5180910390f35b3073ffffffffffffffffffffffffffffffffffffffff16ff5b565b6000"  # noqa: E501
            "60003073ffffffffffffffffffffffffffffffffffffffff166335f46994604051817c01"  # noqa: E501
            "000000000000000000000000000000000000000000000000000000000281526004018090"  # noqa: E501
            "506000604051808303816000876161da5a03f115610002575050503073ffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffff163190503373ffffffffffffffffffffffffffffffffff"  # noqa: E501
            "ffffff16600082604051809050600060405180830381858888f193505050505080915061"  # noqa: E501
            "0147565b509056"
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xb1f4cbc3a50042184425a6f9e996d0910f7ba879457ce5dac5c71e498ad3c005"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex("4d536fe3"),
        gas_limit=3000000,
        gas_price=10,
        nonce=0,
        value=100000,
    )

    post = {
        contract: Account(
            code=bytes.fromhex(
                "60606040526000357c01000000000000000000000000000000000000000000000000000000009004806335f46994146100445780634d536fe31461005157610042565b005b61004f600450610072565b005b61005c60045061008d565b6040518082815260200191505060405180910390f35b3073ffffffffffffffffffffffffffffffffffffffff16ff5b565b600060003073ffffffffffffffffffffffffffffffffffffffff166335f46994604051817c01000000000000000000000000000000000000000000000000000000000281526004018090506000604051808303816000876161da5a03f115610002575050503073ffffffffffffffffffffffffffffffffffffffff163190503373ffffffffffffffffffffffffffffffffffffffff16600082604051809050600060405180830381858888f1935050505050809150610147565b509056"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
