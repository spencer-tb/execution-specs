"""
Ported from:
tests/static/state_tests/stCreateTest/TransactionCollisionToEmpty2Filler.json
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
    ["tests/static/state_tests/stCreateTest/TransactionCollisionToEmpty2Filler.json"],
)
@pytest.mark.valid_from("Cancun")
@pytest.mark.parametrize(
    "tx_gas_limit, tx_value, expected_post",
    [
    pytest.param(
        600000, 0,
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(storage={1: 1}, nonce=1, balance=10), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case0",
    ),
    pytest.param(
        600000, 1,
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(storage={1: 1}, nonce=1, balance=11), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case1",
    ),
    pytest.param(
        54000, 0,
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(storage={}, nonce=0, balance=10), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case2",
    ),
    pytest.param(
        54000, 1,
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(storage={}, nonce=0, balance=10), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case3",
    ),
    ],
)
@pytest.mark.pre_alloc_mutable
def test_transaction_collision_to_empty2(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
    tx_value: int,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[contract] = Account(balance=10, nonce=0)
    pre[sender] = Account(balance=0xe8d4a51000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=None,
        data=bytes.fromhex("6001600155"),
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=tx_value,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
