"""
Test if calldata is empty in initcode context.

Ported from:
tests/static/state_tests/stCreateTest/CREATE2_CallDataFiller.yml
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
    ["tests/static/state_tests/stCreateTest/CREATE2_CallDataFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_create2_call_data(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test if calldata is empty in initcode context."""
    coinbase = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x000000000000000000000000000000000c5ea705")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "6000601080601183398180f560005500fe600035600055604060008037596000f3"  # noqa: E501
        ),
    )
    pre[sender] = Account(balance=0x5AF3107A4000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            storage={0: 0x7F8330AD7BC2AFE0DFFB2FDC76BBAD8BC326296A},
            code=bytes.fromhex(
                "6000601080601183398180f560005500fe600035600055604060008037596000f3"  # noqa: E501
            ),
        ),
        Address("0x7f8330ad7bc2afe0dffb2fdc76bbad8bc326296a"): Account(
            code=bytes.fromhex(
                "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
