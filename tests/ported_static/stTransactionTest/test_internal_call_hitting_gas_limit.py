"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stTransactionTest
InternalCallHittingGasLimitFiller.json
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
        "tests/static/state_tests/stTransactionTest/InternalCallHittingGasLimitFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_internal_call_hitting_gas_limit(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adf5374fce5edbc8e2a8697c15331677e6ebf0b")
    sender = Address("0xc4a2ca1058df329e5da4755f9921ddaf05cbaa06")
    contract = Address("0xb208128346fe6a0c4efa386c0c411a56e4557e2a")
    callee = Address("0x9f499a40cbc961c5230197401ce369d5c53ed896")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000,
    )

    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("603760015500"),
    )
    pre[contract] = Account(
        balance=0xF4240,
        nonce=0,
        code=bytes.fromhex(
            "60006000600060006001739f499a40cbc961c5230197401ce369d5c53ed896611388f100"  # noqa: E501
        ),
    )
    pre[sender] = Account(balance=0x3B9ACA00, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xf79127a3004abde26a4cbd80c428cb10f829fa11b54d36e7b326f4f4a5927acf"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=21100,
        gas_price=10,
        nonce=0,
        value=10,
    )

    post = {
        callee: Account(code=bytes.fromhex("603760015500")),
        contract: Account(
            code=bytes.fromhex(
                "60006000600060006001739f499a40cbc961c5230197401ce369d5c53ed896611388f100"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
