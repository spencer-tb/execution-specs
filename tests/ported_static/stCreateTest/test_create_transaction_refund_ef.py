"""
Test combination of gas refund and EF-prefixed create transaction failure.

Ported from:
tests/static/state_tests/stCreateTest/CreateTransactionRefundEFFiller.yml
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
        "tests/static/state_tests/stCreateTest/CreateTransactionRefundEFFiller.yml",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_create_transaction_refund_ef(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test combination of gas refund and EF-prefixed create transaction..."""
    coinbase = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x00000000000000000000000000000000005ef94d")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    # Source: Yul
    # {
    #   sstore(0,0)
    # }
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=Op.SSTORE(key=Op.DUP1, value=0x0) + Op.STOP,
        storage={0x0: 0x1},
    )
    pre[sender] = Account(balance=0x5AF3107A4000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=None,
        data=bytes.fromhex(
            "600080808080625ef94d61c350f15060ef60005360016000f3"
        ),
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            storage={0: 1},
            code=Op.SSTORE(key=Op.DUP1, value=0x0) + Op.STOP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
