"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stSolidityTest/TestContractSuicideFiller.json
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
    ["tests/static/state_tests/stSolidityTest/TestContractSuicideFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_test_contract_suicide(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x7f3f285918d9b5e764174551e10b7539b97bbb27")
    contract = Address("0xfe34831df57f026afbfffd7e7b51b4adbfe135e1")

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
            "7c01000000000000000000000000000000000000000000000000000000006000350463a6"  # noqa: E501
            "0eedda8114610039578063c04062261461004b57005b61004161005d565b806000526020"  # noqa: E501
            "6000f35b61005361015a565b8060005260206000f35b60006000608161018a6000396081"  # noqa: E501
            "60006000f0905073ffffffffffffffffffffffffffffffffffffffff811662f55d9d6000"  # noqa: E501
            "807ef55d9d00000000000000000000000000000000000000000000000000000000825260"  # noqa: E501
            "044173ffffffffffffffffffffffffffffffffffffffff16815260200160006000866032"  # noqa: E501
            "5a03f16100e057005b505073ffffffffffffffffffffffffffffffffffffffff811663b9"  # noqa: E501
            "c3d0a5602060007fb9c3d0a5000000000000000000000000000000000000000000000000"  # noqa: E501
            "0000000081526004600060008660325a03f161013757005b505060005160e11461014857"  # noqa: E501
            "610151565b60019150610156565b600091505b5090565b600061016461005d565b600060"  # noqa: E501
            "006101000a81548160ff0219169083021790555060ff6001600054041690509056006075"  # noqa: E501
            "80600c6000396000f3007c01000000000000000000000000000000000000000000000000"  # noqa: E501
            "000000006000350462f55d9d81146036578063b9c3d0a514604557005b603f600435605a"  # noqa: E501
            "565b60006000f35b604b6055565b8060005260206000f35b60e190565b8073ffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffff16ff5056"
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
                "7c01000000000000000000000000000000000000000000000000000000006000350463a60eedda8114610039578063c04062261461004b57005b61004161005d565b8060005260206000f35b61005361015a565b8060005260206000f35b60006000608161018a600039608160006000f0905073ffffffffffffffffffffffffffffffffffffffff811662f55d9d6000807ef55d9d00000000000000000000000000000000000000000000000000000000825260044173ffffffffffffffffffffffffffffffffffffffff168152602001600060008660325a03f16100e057005b505073ffffffffffffffffffffffffffffffffffffffff811663b9c3d0a5602060007fb9c3d0a50000000000000000000000000000000000000000000000000000000081526004600060008660325a03f161013757005b505060005160e11461014857610151565b60019150610156565b600091505b5090565b600061016461005d565b600060006101000a81548160ff0219169083021790555060ff600160005404169050905600607580600c6000396000f3007c01000000000000000000000000000000000000000000000000000000006000350462f55d9d81146036578063b9c3d0a514604557005b603f600435605a565b60006000f35b604b6055565b8060005260206000f35b60e190565b8073ffffffffffffffffffffffffffffffffffffffff16ff5056"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
