"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stTransactionTest
SuicidesAndInternalCallSuicidesOOGFiller.json
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
        "tests/static/state_tests/stTransactionTest/SuicidesAndInternalCallSuicidesOOGFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_suicides_and_internal_call_suicides_oog(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    sender = Address("0x7f3f285918d9b5e764174551e10b7539b97bbb27")
    contract = Address("0x78f15ba0abc5cc1aaa5a0ac6add5d28dd9ab8e1e")
    callee = Address("0x5f0d8cd21c9026a32a4e8d15257b1801458989f3")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    pre[callee] = Account(balance=0, nonce=0, code=bytes.fromhex("6001ff00"))
    pre[contract] = Account(
        balance=10,
        nonce=0,
        code=bytes.fromhex(
            "60006000600060006001735f0d8cd21c9026a32a4e8d15257b1801458989f36155f0f150"  # noqa: E501
            "6000ff00"
        ),
    )
    pre[sender] = Account(balance=0x5F5E100, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xa2333eef5630066b928dea5fd85a239f511b5b067d1441ee7ac290d0122b917b"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=50000,
        gas_price=10,
        nonce=0,
        value=10,
    )

    post = {
        callee: Account(code=bytes.fromhex("6001ff00")),
        contract: Account(
            code=bytes.fromhex(
                "60006000600060006001735f0d8cd21c9026a32a4e8d15257b1801458989f36155f0f1506000ff00"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
