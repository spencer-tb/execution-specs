"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stSolidityTest/TestStoreGasPricesFiller.json
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
    ["tests/static/state_tests/stSolidityTest/TestStoreGasPricesFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.valid_until("Prague")
@pytest.mark.pre_alloc_mutable
def test_test_store_gas_prices(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x4a609d84854dbf90b31517f914f50ad91f02a9ae")
    contract = Address("0xfe58f48415dcf9d527f770e3148b769a76ef83f1")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[sender] = Account(balance=0x746A528800, nonce=0)
    pre[contract] = Account(
        balance=0x186A0,
        nonce=0,
        code=bytes.fromhex(
            "7c01000000000000000000000000000000000000000000000000000000006000350463c0"  # noqa: E501
            "4062268114602d57005b6033603d565b8060005260206000f35b600060005a6001602055"  # noqa: E501
            "90505a81036000555a600260205590505a81036001555a600260205590505a8103600255"  # noqa: E501
            "5a65168aa8d53fe660205590505a81036003555a600260205590505a81036004555a6000"  # noqa: E501
            "60205590505a81036005555a5060019291505056"
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0x185fbea9f643c40e33475353b07fa51d0695ca94789492166b67d60fdb6ef7fb"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex("c0406226"),
        gas_limit=35000000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            storage={0: 22113, 1: 113, 2: 113, 3: 113, 4: 113, 5: 113},
            code=bytes.fromhex(
                "7c01000000000000000000000000000000000000000000000000000000006000350463c04062268114602d57005b6033603d565b8060005260206000f35b600060005a600160205590505a81036000555a600260205590505a81036001555a600260205590505a81036002555a65168aa8d53fe660205590505a81036003555a600260205590505a81036004555a600060205590505a81036005555a5060019291505056"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
