"""
calldepth with balance too low.

Ported from:
tests/static/state_tests/stCallCreateCallCodeTest
Call1024BalanceTooLowFiller.json
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
        "tests/static/state_tests/stCallCreateCallCodeTest/Call1024BalanceTooLowFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.valid_until("Prague")
@pytest.mark.pre_alloc_mutable
def test_call1024_balance_too_low(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Calldepth with balance too low."""
    coinbase = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    sender = Address("0x4768b5e50b0ebe91ae38d84a47e3179e615f9c40")
    contract = Address("0x2aaa3ab47a59b4ad0ba3f72ad0b5bc35388333b4")
    callee = Address("0xd9b97c712ebce43f3c19179bbef44b550f9e8bc0")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[contract] = Account(
        balance=1024,
        nonce=0,
        code=bytes.fromhex(
            "6001600054016000556000600060006000600054732aaa3ab47a59b4ad0ba3f72ad0b5bc"  # noqa: E501
            "35388333b4650ffffffffffff160015500"
        ),
    )
    pre[sender] = Account(balance=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF, nonce=0)
    pre[callee] = Account(balance=7000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xe7c72b378297589acee4e0ba3272841bcfc5e220f86de253f890274cfee9e474"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=17592186099592,
        gas_price=10,
        nonce=0,
        value=10,
    )

    post = {
        contract: Account(
            storage={0: 1025, 1: 1},
            code=bytes.fromhex(
                "6001600054016000556000600060006000600054732aaa3ab47a59b4ad0ba3f72ad0b5bc35388333b4650ffffffffffff160015500"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
