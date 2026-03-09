"""
call with value. call takes more gas then tx has, and more value than...

Ported from:
tests/static/state_tests/stCallCreateCallCodeTest
callWithHighValueAndGasOOGFiller.json
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
        "tests/static/state_tests/stCallCreateCallCodeTest/callWithHighValueAndGasOOGFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_value, expected_post",
    [
        (
            100000,
            {
                Address("0x0896f13e800125c0ccec44f3c434335f0a97bc1b"): Account(
                    code=bytes.fromhex("6001600155603760005360026000f3")
                ),
                Address("0xdfad372452688759edd82c422bf3976eafc89c2b"): Account(
                    storage={
                        1: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF  # noqa: E501
                    },
                    code=bytes.fromhex(
                        "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff6000527faaffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffaa602052600260006040600068056bc75e2d63100000730896f13e800125c0ccec44f3c434335f0a97bc1b6bfffffffffffffffffffffffff160005560005160015500"  # noqa: E501
                    ),
                ),
            },
        ),
        (
            100000000000000000000,
            {
                Address("0x0896f13e800125c0ccec44f3c434335f0a97bc1b"): Account(
                    storage={1: 1},
                    code=bytes.fromhex("6001600155603760005360026000f3"),
                ),
                Address("0xdfad372452688759edd82c422bf3976eafc89c2b"): Account(
                    storage={
                        0: 1,
                        1: 0x3700FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                    },
                    code=bytes.fromhex(
                        "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff6000527faaffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffaa602052600260006040600068056bc75e2d63100000730896f13e800125c0ccec44f3c434335f0a97bc1b6bfffffffffffffffffffffffff160005560005160015500"  # noqa: E501
                    ),
                ),
            },
        ),
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_call_with_high_value_and_gas_oog(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_value: int,
    expected_post: dict,
) -> None:
    """Call with value. call takes more gas then tx has, and more value..."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xd187b36e8532efd7f15218fb1781d79330c0cda2")
    contract = Address("0xdfad372452688759edd82c422bf3976eafc89c2b")
    callee = Address("0x0896f13e800125c0ccec44f3c434335f0a97bc1b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=30000000,
    )

    pre[callee] = Account(
        balance=23,
        nonce=0,
        code=bytes.fromhex("6001600155603760005360026000f3"),
    )
    pre[sender] = Account(balance=0x3635C9ADC5DEA00000, nonce=0)
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff600052"  # noqa: E501
            "7faaffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffaa602052"  # noqa: E501
            "600260006040600068056bc75e2d63100000730896f13e800125c0ccec44f3c434335f0a"  # noqa: E501
            "97bc1b6bfffffffffffffffffffffffff160005560005160015500"
        ),
        storage={0x0: 0x5},
    )

    tx = Transaction(
        secret_key=Hash(
            "0x897b12d02d588d8a4fe16ff831cbd4459c6f62f8c845b0ccdd31caf068c84a26"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=6000000,
        gas_price=10,
        nonce=0,
        value=tx_value,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
