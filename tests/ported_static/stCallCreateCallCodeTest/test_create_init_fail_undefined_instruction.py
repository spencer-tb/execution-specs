"""
create fails because init code has undefined opcode, trying to suicide to it.

Ported from:
tests/static/state_tests/stCallCreateCallCodeTest
createInitFailUndefinedInstructionFiller.json
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
        "tests/static/state_tests/stCallCreateCallCodeTest/createInitFailUndefinedInstructionFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_create_init_fail_undefined_instruction(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Create fails because init code has undefined opcode, trying to..."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0x73e58ff0ab0c422709d507efb9d4889740040144")
    callee = Address("0x0183feb7335d767d4d6ae41bbdea7afb27227860")
    callee_1 = Address("0x552f200b75457440ee6df9159d6b188e9d18c222")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000000,
    )

    pre[callee] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex("60f96000536000600160006001f5ff00"),
    )
    pre[callee_1] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex("60f9600053600160006001f0ff00"),
    )
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "6000600060006000600073552f200b75457440ee6df9159d6b188e9d18c22262061a80f1"  # noqa: E501
            "60005560006000600060006000730183feb7335d767d4d6ae41bbdea7afb272278606206"  # noqa: E501
            "1a80f1600155600160025500"
        ),
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xe04d1ac7ddda0c98397d56a0b501e960d4cd325a39286919ac23c1a07009a869"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=900000,
        gas_price=10,
        nonce=0,
        value=100000,
    )

    post = {
        callee: Account(
            code=bytes.fromhex("60f96000536000600160006001f5ff00"),
        ),
        callee_1: Account(code=bytes.fromhex("60f9600053600160006001f0ff00")),
        contract: Account(
            storage={2: 1},
            code=bytes.fromhex(
                "6000600060006000600073552f200b75457440ee6df9159d6b188e9d18c22262061a80f160005560006000600060006000730183feb7335d767d4d6ae41bbdea7afb2722786062061a80f1600155600160025500"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
