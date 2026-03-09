"""
call -> (call -> call -> code) oog.

Ported from:
tests/static/state_tests/stCallCodes/callcallcall_000_OOGMAfterFiller.json
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
        "tests/static/state_tests/stCallCodes/callcallcall_000_OOGMAfterFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_callcallcall_000_oogm_after(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Call -> (call -> call -> code) oog."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0x1f4cb3e7976ba5835015b9c3b0075aea78aaa482")
    callee = Address("0x8d7270785422b63a97d83bada6aac80bebc3a99d")
    callee_1 = Address("0xb126c622075b1189fb6c45e851641cfaddf65b36")
    callee_2 = Address("0xb5d1a486869d27225126c47727513f57d329a01a")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=30000000,
    )

    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "6040600060406000600073b5d1a486869d27225126c47727513f57d329a01a620c3500f1"  # noqa: E501
            "6000556001600b5500"
        ),
    )
    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "6040600060406000600073b126c622075b1189fb6c45e851641cfaddf65b3662061a80f1"  # noqa: E501
            "60025500"
        ),
    )
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("600160035500"),
    )
    pre[callee_2] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "60406000604060006000738d7270785422b63a97d83bada6aac80bebc3a99d620927c0f1"  # noqa: E501
            "600155622fffff60002000"
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
        value=0,
    )

    post = {
        contract: Account(
            storage={11: 1},
            code=bytes.fromhex(
                "6040600060406000600073b5d1a486869d27225126c47727513f57d329a01a620c3500f16000556001600b5500"  # noqa: E501
            ),
        ),
        callee: Account(
            code=bytes.fromhex(
                "6040600060406000600073b126c622075b1189fb6c45e851641cfaddf65b3662061a80f160025500"  # noqa: E501
            ),
        ),
        callee_1: Account(code=bytes.fromhex("600160035500")),
        callee_2: Account(
            code=bytes.fromhex(
                "60406000604060006000738d7270785422b63a97d83bada6aac80bebc3a99d620927c0f1600155622fffff60002000"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
