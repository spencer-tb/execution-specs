"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stTransactionTest/StoreGasOnCreateFiller.json
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
    ["tests/static/state_tests/stTransactionTest/StoreGasOnCreateFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_store_gas_on_create(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    pre[sender] = Account(balance=0x17D78400, nonce=0)
    pre[coinbase] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("635a60fd556000526004601c6000f000"),
    )

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=coinbase,
        data=b"",
        gas_limit=131882,
        gas_price=10,
        nonce=0,
        value=100,
    )

    post = {
        coinbase: Account(
            code=bytes.fromhex("635a60fd556000526004601c6000f000"),
        ),
        Address("0xf1ecf98489fa9ed60a664fc4998db699cfa39d40"): Account(
            storage={253: 0x12F39},
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
