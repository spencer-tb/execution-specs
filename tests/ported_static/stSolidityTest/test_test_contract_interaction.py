"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stSolidityTest/TestContractInteractionFiller.json
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
        "tests/static/state_tests/stSolidityTest/TestContractInteractionFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_test_contract_interaction(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x7f3f285918d9b5e764174551e10b7539b97bbb27")
    contract = Address("0x087dfec56d6da95fd3a1bcf8ccf995ee51645950")

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
            "7c01000000000000000000000000000000000000000000000000000000006000350463c0"  # noqa: E501
            "4062268114610039578063ed973fe91461004b57005b6100416100ea565b806000526020"  # noqa: E501
            "6000f35b61005361005d565b8060005260206000f35b60006000608161011a6000396081"  # noqa: E501
            "60006000f0905073ffffffffffffffffffffffffffffffffffffffff811663b9c3d0a560"  # noqa: E501
            "2060007fb9c3d0a500000000000000000000000000000000000000000000000000000000"  # noqa: E501
            "81526004600060008660325a03f16100c757005b505060005160e1146100d8576100e156"  # noqa: E501
            "5b600191506100e6565b600091505b5090565b60006100f461005d565b60006000610100"  # noqa: E501
            "0a81548160ff0219169083021790555060ff600160005404169050905600607580600c60"  # noqa: E501
            "00396000f3007c0100000000000000000000000000000000000000000000000000000000"  # noqa: E501
            "6000350462f55d9d81146036578063b9c3d0a514604557005b603f6004356055565b6000"  # noqa: E501
            "6000f35b604b6070565b8060005260206000f35b8073ffffffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffff16ff50565b60e19056"
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
            storage={0: 1},
            code=bytes.fromhex(
                "7c01000000000000000000000000000000000000000000000000000000006000350463c04062268114610039578063ed973fe91461004b57005b6100416100ea565b8060005260206000f35b61005361005d565b8060005260206000f35b60006000608161011a600039608160006000f0905073ffffffffffffffffffffffffffffffffffffffff811663b9c3d0a5602060007fb9c3d0a50000000000000000000000000000000000000000000000000000000081526004600060008660325a03f16100c757005b505060005160e1146100d8576100e1565b600191506100e6565b600091505b5090565b60006100f461005d565b600060006101000a81548160ff0219169083021790555060ff600160005404169050905600607580600c6000396000f3007c01000000000000000000000000000000000000000000000000000000006000350462f55d9d81146036578063b9c3d0a514604557005b603f6004356055565b60006000f35b604b6070565b8060005260206000f35b8073ffffffffffffffffffffffffffffffffffffffff16ff50565b60e19056"  # noqa: E501
            ),
        ),
        Address("0xd0a4f234edb751a767cc39613d2204399d6cc464"): Account(
            code=bytes.fromhex(
                "7c01000000000000000000000000000000000000000000000000000000006000350462f55d9d81146036578063b9c3d0a514604557005b603f6004356055565b60006000f35b604b6070565b8060005260206000f35b8073ffffffffffffffffffffffffffffffffffffffff16ff50565b60e19056"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
