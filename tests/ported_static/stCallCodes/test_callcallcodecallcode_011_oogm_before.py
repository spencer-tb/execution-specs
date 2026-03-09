"""
call -> callcode -> oog callcode -> code.

Ported from:
tests/static/state_tests/stCallCodes
callcallcodecallcode_011_OOGMBeforeFiller.json
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
        "tests/static/state_tests/stCallCodes/callcallcodecallcode_011_OOGMBeforeFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_callcallcodecallcode_011_oogm_before(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Call -> callcode -> oog callcode -> code."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0x335b558774699d81f685543cfbcde5c4e5407686")
    callee = Address("0x8e6e134402f2eeca8e910e8ec62b45b36ee31f30")
    callee_1 = Address("0xb126c622075b1189fb6c45e851641cfaddf65b36")
    callee_2 = Address("0xdbb53599a5d13e0c465e1cc4ff24d7f00d780df4")

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
            "60406000604060006000738e6e134402f2eeca8e910e8ec62b45b36ee31f30620c3500f1"  # noqa: E501
            "60005500"
        ),
    )
    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "6040600060406000600073dbb53599a5d13e0c465e1cc4ff24d7f00d780df4620927c0f2"  # noqa: E501
            "6001556001600b5500"
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
            "622fffff600020506040600060406000600073b126c622075b1189fb6c45e851641cfadd"  # noqa: E501
            "f65b3662061a80f260025500"
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
            storage={0: 1},
            code=bytes.fromhex(
                "60406000604060006000738e6e134402f2eeca8e910e8ec62b45b36ee31f30620c3500f160005500"  # noqa: E501
            ),
        ),
        callee: Account(
            storage={11: 1},
            code=bytes.fromhex(
                "6040600060406000600073dbb53599a5d13e0c465e1cc4ff24d7f00d780df4620927c0f26001556001600b5500"  # noqa: E501
            ),
        ),
        callee_1: Account(code=bytes.fromhex("600160035500")),
        callee_2: Account(
            code=bytes.fromhex(
                "622fffff600020506040600060406000600073b126c622075b1189fb6c45e851641cfaddf65b3662061a80f260025500"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
