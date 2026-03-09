"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stSystemOperationsTest
CallRecursiveBombLog2Filler.json
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
        "tests/static/state_tests/stSystemOperationsTest/CallRecursiveBombLog2Filler.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.valid_until("Prague")
@pytest.mark.pre_alloc_mutable
def test_call_recursive_bomb_log2(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0xd2e8fbe36bd16b24a1d34e4c06ec0741bd71c452")
    callee = Address("0x4f046f9952c30de8430278a978358e998784a4ca")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=11000000000,
    )

    pre[callee] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "5a60005260206000a060016000540160005560006000600060006000306161a85a03f160"  # noqa: E501
            "015500"
        ),
    )
    pre[contract] = Account(
        balance=0x1312D00,
        nonce=0,
        code=bytes.fromhex(
            "60006000600060006017734f046f9952c30de8430278a978358e998784a4ca6305f5e100"  # noqa: E501
            "f100"
        ),
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xe04d1ac7ddda0c98397d56a0b501e960d4cd325a39286919ac23c1a07009a869"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=10000000000,
        gas_price=10,
        nonce=0,
        value=100000,
    )

    post = {
        callee: Account(
            storage={0: 322, 1: 1},
            code=bytes.fromhex(
                "5a60005260206000a060016000540160005560006000600060006000306161a85a03f160015500"  # noqa: E501
            ),
        ),
        contract: Account(
            code=bytes.fromhex(
                "60006000600060006017734f046f9952c30de8430278a978358e998784a4ca6305f5e100f100"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
