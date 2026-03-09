"""
call -> call -> code oog.

Ported from:
tests/static/state_tests/stCallCodes/callcall_00_OOGEFiller.json
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
    ["tests/static/state_tests/stCallCodes/callcall_00_OOGEFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_callcall_00_ooge(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Call -> call -> code oog."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0x4353e77718be108d4c149d88b34caceda42c5c66")
    callee = Address("0x766b2cf0691f51029181fc511395b7ab71353a88")
    callee_1 = Address("0x9196f97bca1b117e521275693c79420479d9cc90")

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
            "60406000604060006000739196f97bca1b117e521275693c79420479d9cc90620249f0f1"  # noqa: E501
            "60005500"
        ),
    )
    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("6001600255622fffff60002000"),
    )
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "6040600060406000600073766b2cf0691f51029181fc511395b7ab71353a88614e34f160"  # noqa: E501
            "01556001600b5500"
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
                "60406000604060006000739196f97bca1b117e521275693c79420479d9cc90620249f0f160005500"  # noqa: E501
            ),
        ),
        callee: Account(code=bytes.fromhex("6001600255622fffff60002000")),
        callee_1: Account(
            storage={11: 1},
            code=bytes.fromhex(
                "6040600060406000600073766b2cf0691f51029181fc511395b7ab71353a88614e34f16001556001600b5500"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
