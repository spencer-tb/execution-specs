"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stSystemOperationsTest/ABAcalls0Filler.json
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
    ["tests/static/state_tests/stSystemOperationsTest/ABAcalls0Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_ab_acalls0(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0xd6cd6ec9adca299f2bbfd754ff8bcf6a4b9aae40")
    callee = Address("0x44eb1162303b6a60f2f8882d43d661787b3011e6")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[callee] = Account(
        balance=23,
        nonce=0,
        code=bytes.fromhex(
            "6000600060006000601773d6cd6ec9adca299f2bbfd754ff8bcf6a4b9aae4061c350f160"  # noqa: E501
            "0101585500"
        ),
    )
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "600060006000600060187344eb1162303b6a60f2f8882d43d661787b3011e6620186a0f1"  # noqa: E501
            "585500"
        ),
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xe04d1ac7ddda0c98397d56a0b501e960d4cd325a39286919ac23c1a07009a869"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=1000000,
        gas_price=10,
        nonce=0,
        value=100000,
    )

    post = {
        callee: Account(
            storage={38: 1},
            code=bytes.fromhex(
                "6000600060006000601773d6cd6ec9adca299f2bbfd754ff8bcf6a4b9aae4061c350f1600101585500"  # noqa: E501
            ),
        ),
        contract: Account(
            storage={36: 1},
            code=bytes.fromhex(
                "600060006000600060187344eb1162303b6a60f2f8882d43d661787b3011e6620186a0f1585500"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
