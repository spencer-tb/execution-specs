"""
Test combination of gas refund and EF-prefixed CREATE2 failure.

Ported from:
tests/static/state_tests/stCreateTest/CREATE2_RefundEFFiller.yml
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
    ["tests/static/state_tests/stCreateTest/CREATE2_RefundEFFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_create2_refund_ef(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test combination of gas refund and EF-prefixed CREATE2 failure."""
    coinbase = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x000000000000000000000000000000000c5ea705")
    callee = Address("0x00000000000000000000000000000000005ef94d")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("6000805500"),
        storage={0x0: 0x1},
    )
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "6000601980601183398180f560005500fe600080808080625ef94d61c350f15060ef6000"  # noqa: E501
            "5360016000f3"
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
        callee: Account(storage={0: 1}, code=bytes.fromhex("6000805500")),
        contract: Account(
            code=bytes.fromhex(
                "6000601980601183398180f560005500fe600080808080625ef94d61c350f15060ef60005360016000f3"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
