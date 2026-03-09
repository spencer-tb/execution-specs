"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stSystemOperationsTest/ABAcalls1Filler.json
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
    ["tests/static/state_tests/stSystemOperationsTest/ABAcalls1Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.valid_until("Prague")
@pytest.mark.pre_alloc_mutable
def test_ab_acalls1(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0x572a88ed686beb6c9b71dc491ba1e120b327a85f")
    callee = Address("0x6236ea4ea8f3e5263acb65a97abe8683ab54d03a")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000000,
    )

    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "60006000600060006018736236ea4ea8f3e5263acb65a97abe8683ab54d03a620186a05a"  # noqa: E501
            "03f1585500"
        ),
    )
    pre[callee] = Account(
        balance=23,
        nonce=0,
        code=bytes.fromhex(
            "6000600060006000601773572a88ed686beb6c9b71dc491ba1e120b327a85f620186a05a"  # noqa: E501
            "03f1600101585500"
        ),
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xe04d1ac7ddda0c98397d56a0b501e960d4cd325a39286919ac23c1a07009a869"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=1000000000,
        gas_price=10,
        nonce=0,
        value=100000,
    )

    post = {
        contract: Account(
            storage={38: 1},
            code=bytes.fromhex(
                "60006000600060006018736236ea4ea8f3e5263acb65a97abe8683ab54d03a620186a05a03f1585500"  # noqa: E501
            ),
        ),
        callee: Account(
            storage={41: 2},
            code=bytes.fromhex(
                "6000600060006000601773572a88ed686beb6c9b71dc491ba1e120b327a85f620186a05a03f1600101585500"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
