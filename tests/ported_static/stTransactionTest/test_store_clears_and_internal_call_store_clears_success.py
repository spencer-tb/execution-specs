"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stTransactionTest
StoreClearsAndInternalCallStoreClearsSuccessFiller.json
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
        "tests/static/state_tests/stTransactionTest/StoreClearsAndInternalCallStoreClearsSuccessFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_store_clears_and_internal_call_store_clears_success(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    sender = Address("0x01a87dcc756f6a6bd9e586598a5c1a44a1c6d945")
    contract = Address("0x8989e867016031a6730f2b84d5e47e1f0f83bdd9")
    callee = Address("0xd61e0564fab2b0da5136f75db579b663bd9f2bd8")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[sender] = Account(balance=0x1DCD6500, nonce=0)
    pre[contract] = Account(
        balance=10,
        nonce=0,
        code=bytes.fromhex(
            "60006000556000600155600060025560006003556000600060006000600173d61e0564fa"  # noqa: E501
            "b2b0da5136f75db579b663bd9f2bd861c350f100"
        ),
        storage={0x0: 0xC, 0x1: 0xC, 0x2: 0xC, 0x3: 0xC, 0x4: 0xC},
    )
    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "600060005560006001556000600255600060035560006004556000600555600060065560"  # noqa: E501
            "006007556000600855600060095500"
        ),
        storage={
            0x0: 0xC,
            0x1: 0xC,
            0x2: 0xC,
            0x3: 0xC,
            0x4: 0xC,
            0x5: 0xC,
            0x6: 0xC,
            0x7: 0xC,
            0x8: 0xC,
            0x9: 0xC,
        },
    )

    tx = Transaction(
        secret_key=Hash(
            "0x96c07046493ec8728482079ab999d2994420d9cf4d3491dfd06871b106d9d87b"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=200000,
        gas_price=10,
        nonce=0,
        value=10,
    )

    post = {
        contract: Account(
            storage={4: 12},
            code=bytes.fromhex(
                "60006000556000600155600060025560006003556000600060006000600173d61e0564fab2b0da5136f75db579b663bd9f2bd861c350f100"  # noqa: E501
            ),
        ),
        callee: Account(
            code=bytes.fromhex(
                "600060005560006001556000600255600060035560006004556000600555600060065560006007556000600855600060095500"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
