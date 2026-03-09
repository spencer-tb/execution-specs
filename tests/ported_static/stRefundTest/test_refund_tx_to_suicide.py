"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRefundTest/refund_TxToSuicideFiller.json
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
    ["tests/static/state_tests/stRefundTest/refund_TxToSuicideFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_refund_tx_to_suicide(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0xeb201d2887816e041f6e807e804f64f3a7a226fe")
    sender = Address("0x7f3f285918d9b5e764174551e10b7539b97bbb27")
    contract = Address("0x2bc33a472f0fba1e30bf2317d07910367908c7f6")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex("73095e7baea6a6c7c4c2dfeb977efac326af552d87ff00"),
        storage={0x1: 0x1},
    )
    pre[sender] = Account(balance=0x5F5E100, nonce=0)
    pre[coinbase] = Account(balance=0, nonce=1)

    tx = Transaction(
        secret_key=Hash(
            "0xa2333eef5630066b928dea5fd85a239f511b5b067d1441ee7ac290d0122b917b"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=61003,
        gas_price=10,
        nonce=0,
        value=10,
    )

    post = {
        contract: Account(
            storage={1: 1},
            code=bytes.fromhex(
                "73095e7baea6a6c7c4c2dfeb977efac326af552d87ff00"
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
