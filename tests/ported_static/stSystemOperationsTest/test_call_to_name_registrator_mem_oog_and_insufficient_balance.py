"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stSystemOperationsTest
CallToNameRegistratorMemOOGAndInsufficientBalanceFiller.json
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
        "tests/static/state_tests/stSystemOperationsTest/CallToNameRegistratorMemOOGAndInsufficientBalanceFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_call_to_name_registrator_mem_oog_and_insufficient_balance(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0x74859a27dc2f1ee153cf9b4e4bac1133f3b01b17")
    callee = Address("0x15eb18969e0925c8e4a76fd7cbce36a2b056b27e")

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
        code=bytes.fromhex("6000355415600957005b60203560003555"),
    )
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff600052"  # noqa: E501
            "7faaffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffaa602052"  # noqa: E501
            "6000604065ffffffffffff600060177315eb18969e0925c8e4a76fd7cbce36a2b056b27e"  # noqa: E501
            "64fffffffffff160005500"
        ),
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
        callee: Account(
            code=bytes.fromhex("6000355415600957005b60203560003555"),
        ),
        contract: Account(
            code=bytes.fromhex(
                "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff6000527faaffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffaa6020526000604065ffffffffffff600060177315eb18969e0925c8e4a76fd7cbce36a2b056b27e64fffffffffff160005500"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
