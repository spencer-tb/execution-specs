"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stInitCodeTest/ReturnTest2Filler.json
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
    ["tests/static/state_tests/stInitCodeTest/ReturnTest2Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_return_test2(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x194f5374fce5edbc8e2a8697c15331677e6ebf0b")
    callee = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000000,
    )

    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "60156000526020602060206000600073b94f5374fce5edbc8e2a8697c15331677e6ebf0b"  # noqa: E501
            "611b58f15060005160005560205160015560406000f300"
        ),
    )
    pre[sender] = Account(balance=0x989680, nonce=0)
    pre[callee] = Account(
        balance=0x186A0,
        nonce=0,
        code=bytes.fromhex("60003560030260005260206000f300"),
    )

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=250000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            storage={0: 21, 1: 63},
            code=bytes.fromhex(
                "60156000526020602060206000600073b94f5374fce5edbc8e2a8697c15331677e6ebf0b611b58f15060005160005560205160015560406000f300"  # noqa: E501
            ),
        ),
        callee: Account(code=bytes.fromhex("60003560030260005260206000f300")),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
