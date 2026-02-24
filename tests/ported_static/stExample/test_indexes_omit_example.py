"""
expect section set -indexes field by default equal to -1

Ported from:
tests/static/state_tests/stExample/indexesOmitExampleFiller.yml
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
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


@pytest.mark.ported_from(
    ["tests/static/state_tests/stExample/indexesOmitExampleFiller.yml"],
)
@pytest.mark.valid_from("Cancun")
def test_indexes_omit_example(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """expect section set -indexes field by default equal to -1."""
    coinbase = Address("0x8a0a19589531694250d570040a0c4b74576919b8")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x1000000000000000000000000000000000001000")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=71794957647893862,
    )

    pre[contract] = Account(
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=Op.PUSH1[0x1] + Op.PUSH1[0x1] + Op.ADD + Op.PUSH1[0x0] + Op.SSTORE + Op.STOP,
    )
    pre[coinbase] = Account(balance=0, nonce=1)
    pre[sender] = Account(balance=0xde0b6b3a7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=b"",
        gas_limit=400000,
        gas_price=10,
        nonce=0,
        value=100000,
    )

    post = {}

    state_test(env=env, pre=pre, post=post, tx=tx)
