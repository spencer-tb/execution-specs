"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRefundTest/refund_changeNonZeroStorageFiller.json
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
    [
        "tests/static/state_tests/stRefundTest/refund_changeNonZeroStorageFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_refund_change_non_zero_storage(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0xeb201d2887816e041f6e807e804f64f3a7a226fe")
    sender = Address("0x720cdc678c4361866ff59a4307a6ece59bae06df")
    contract = Address("0x904261b07d3a5f213bbd6fb9f3bb66f4fb65c7eb")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    pre[sender] = Account(balance=0x3C336080, nonce=0)
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=Op.SSTORE(key=0x1, value=0x17) + Op.STOP,
        storage={0x1: 0x1},
    )
    pre[coinbase] = Account(balance=0, nonce=1)

    tx = Transaction(
        secret_key=Hash(
            "0x4d9fc6fdf95098986741ee78843ac52beed77c8c801dc87bd3f04cd6bbf1a3eb"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=228500,
        gas_price=10,
        nonce=0,
        value=10,
    )

    post = {
        contract: Account(
            storage={1: 23},
            code=Op.SSTORE(key=0x1, value=0x17) + Op.STOP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
