"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stSystemOperationsTest
CallToReturn1ForDynamicJump1Filler.json
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
        "tests/static/state_tests/stSystemOperationsTest/CallToReturn1ForDynamicJump1Filler.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_call_to_return1_for_dynamic_jump1(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0x7bc307ec814ce37f4553993ac5612b763f18165d")
    callee = Address("0xd43411a40a68e9cba15440e3c34a74a4dc5f79dd")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "6001601f60006000601773d43411a40a68e9cba15440e3c34a74a4dc5f79dd6103e8f160"  # noqa: E501
            "005560005156605b6023602355"
        ),
    )
    pre[callee] = Account(
        balance=23,
        nonce=0,
        code=bytes.fromhex("6001600155602b601f536001601ff3"),
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xe04d1ac7ddda0c98397d56a0b501e960d4cd325a39286919ac23c1a07009a869"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=300000,
        gas_price=10,
        nonce=0,
        value=100000,
    )

    post = {
        contract: Account(
            code=bytes.fromhex(
                "6001601f60006000601773d43411a40a68e9cba15440e3c34a74a4dc5f79dd6103e8f160005560005156605b6023602355"  # noqa: E501
            ),
        ),
        callee: Account(code=bytes.fromhex("6001600155602b601f536001601ff3")),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
