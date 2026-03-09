"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stEIP150Specific/CreateAndGasInsideCreateFiller.json
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
        "tests/static/state_tests/stEIP150Specific/CreateAndGasInsideCreateFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_create_and_gas_inside_create(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[sender] = Account(balance=0xE8D4A51000, nonce=0)
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "5a606452635a60fd556000526004601c6000f0600b555a6064510360095500"
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=600000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            storage={
                9: 0x129DB,
                11: 0xF1ECF98489FA9ED60A664FC4998DB699CFA39D40,
            },
            code=bytes.fromhex(
                "5a606452635a60fd556000526004601c6000f0600b555a6064510360095500"  # noqa: E501
            ),
        ),
        Address("0xf1ecf98489fa9ed60a664fc4998db699cfa39d40"): Account(
            storage={253: 0x83729},
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
