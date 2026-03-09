"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stTransactionTest/SuicidesStopAfterSuicideFiller.json
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
        "tests/static/state_tests/stTransactionTest/SuicidesStopAfterSuicideFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_suicides_stop_after_suicide(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xc94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    callee = Address("0x0000000000000000000000000000000000000000")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000,
    )

    pre[callee] = Account(
        balance=1110,
        nonce=0,
        code=bytes.fromhex("6001ff00"),
    )
    pre[sender] = Account(balance=0x7459280, nonce=0)
    pre[contract] = Account(
        balance=0x2710,
        nonce=0,
        code=bytes.fromhex("6000ff600060006000600060006000617530f100"),
    )

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=83700,
        gas_price=10,
        nonce=0,
        value=10,
    )

    post = {
        callee: Account(code=bytes.fromhex("6001ff00")),
        contract: Account(
            code=bytes.fromhex("6000ff600060006000600060006000617530f100"),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
