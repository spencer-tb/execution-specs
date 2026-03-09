"""
calldepth with subcall.

Ported from:
tests/static/state_tests/stCallCreateCallCodeTest/Call1024PreCallsFiller.json
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
        "tests/static/state_tests/stCallCreateCallCodeTest/Call1024PreCallsFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.valid_until("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit",
    [
        9214364837600034817,
        11837600034817,
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_call1024_pre_calls(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
) -> None:
    """Calldepth with subcall."""
    coinbase = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    sender = Address("0x3f13d7fc49b91cdc388f79f861c0f1a0e708dfbf")
    contract = Address("0x48c20cd83ddbd3908712f4d31c51b3cdaae287ce")
    callee = Address("0xd9b97c712ebce43f3c19179bbef44b550f9e8bc0")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[sender] = Account(balance=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF, nonce=0)
    pre[contract] = Account(
        balance=2024,
        nonce=0,
        code=bytes.fromhex(
            "6000600060006000600173d9b97c712ebce43f3c19179bbef44b550f9e8bc061fffff160"  # noqa: E501
            "02556000600060006000600173d9b97c712ebce43f3c19179bbef44b550f9e8bc061ffff"  # noqa: E501
            "f1600355600160005401600055600060006000600060007348c20cd83ddbd3908712f4d3"  # noqa: E501
            "1c51b3cdaae287ce650ffffffffffff160015500"
        ),
    )
    pre[callee] = Account(balance=7000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xcc381c83857b17ca629268ed418e2915a0287b84efe9cf2204c020302e83cda0"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=10,
    )

    post = {
        contract: Account(
            storage={0: 1025, 1: 1},
            code=bytes.fromhex(
                "6000600060006000600173d9b97c712ebce43f3c19179bbef44b550f9e8bc061fffff16002556000600060006000600173d9b97c712ebce43f3c19179bbef44b550f9e8bc061fffff1600355600160005401600055600060006000600060007348c20cd83ddbd3908712f4d31c51b3cdaae287ce650ffffffffffff160015500"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
