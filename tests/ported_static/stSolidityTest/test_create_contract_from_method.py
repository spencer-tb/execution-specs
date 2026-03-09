"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stSolidityTest/CreateContractFromMethodFiller.json
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
        "tests/static/state_tests/stSolidityTest/CreateContractFromMethodFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_create_contract_from_method(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x095e7baea6a6c7c4c2dfeb977efac326af552d87")

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
            "60003560e060020a900480637ee17e1214601f578063c040622614602b57005b60256047"  # noqa: E501
            "565b60006000f35b6031603b565b8060005260206000f35b600060436047565b5090565b"  # noqa: E501
            "60006060605d600039606060006000f09050905600605480600c6000396000f300600035"  # noqa: E501
            "60e060020a90048062f55d9d14601e578063b9c3d0a514602d57005b6027600435604656"  # noqa: E501
            "5b60006000f35b6033603d565b8060005260206000f35b600060e1905090565b80600160"  # noqa: E501
            "a060020a0316ff5056"
        ),
    )
    pre[sender] = Account(balance=0x5F5E100, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
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
            code=bytes.fromhex(
                "60003560e060020a900480637ee17e1214601f578063c040622614602b57005b60256047565b60006000f35b6031603b565b8060005260206000f35b600060436047565b5090565b60006060605d600039606060006000f09050905600605480600c6000396000f30060003560e060020a90048062f55d9d14601e578063b9c3d0a514602d57005b60276004356046565b60006000f35b6033603d565b8060005260206000f35b600060e1905090565b80600160a060020a0316ff5056"  # noqa: E501
            ),
        ),
        Address("0xd2571607e241ecf590ed94b12d87c94babe36db6"): Account(
            code=bytes.fromhex(
                "60003560e060020a90048062f55d9d14601e578063b9c3d0a514602d57005b60276004356046565b60006000f35b6033603d565b8060005260206000f35b600060e1905090565b80600160a060020a0316ff5056"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
