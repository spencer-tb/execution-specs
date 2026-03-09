"""
An example test for using simple yul contracts in the test.

Ported from:
tests/static/state_tests/stExample/yulExampleFiller.yml
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
    ["tests/static/state_tests/stExample/yulExampleFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_yul_example(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """An example test for using simple yul contracts in the test."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x56724d001b4f2a2888a81971a64aad37cd43f881")
    contract = Address("0xf30c160326a04ecb32e7651c0a8f373468bea269")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000,
    )

    pre[sender] = Account(balance=0xBA1A9CE0BA1A9CE, nonce=0)
    pre[contract] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("600360005560206000f3"),
    )

    tx = Transaction(
        secret_key=Hash(
            "0x40ac0fc28c27e961ee46ec43355a094de205856edbd4654cf2577c2608d4ec1e"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=16777216,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            storage={0: 3},
            code=bytes.fromhex("600360005560206000f3"),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
