"""
CALLCODE -> CALLCODE -> (CALLCODE -> code) suicide.

Ported from:
tests/static/state_tests/stCallCodes
callcodecallcodecallcode_111_SuicideEndFiller.json
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
        "tests/static/state_tests/stCallCodes/callcodecallcodecallcode_111_SuicideEndFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_callcodecallcodecallcode_111_suicide_end(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """CALLCODE -> CALLCODE -> (CALLCODE -> code) suicide."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0xa74ca10b765dcda3b60687f73f2881e2a56eda64")
    callee = Address("0x73b954ebc05bb0ff4a0f6a13a054d50ad1584099")
    callee_1 = Address("0x94c8f980aeecbb6575b12ae614a249fc3e836f21")
    callee_2 = Address("0xeaf8c2ae0d01a880cea4e1aa88def5edd153d57b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=30000000,
    )

    pre[callee] = Account(
        balance=0x2540BE400,
        nonce=0,
        code=bytes.fromhex("600160035500"),
    )
    pre[callee_1] = Account(
        balance=0x2540BE400,
        nonce=0,
        code=bytes.fromhex(
            "604060006040600060007373b954ebc05bb0ff4a0f6a13a054d50ad158409961c350f260"  # noqa: E501
            "025573eaf8c2ae0d01a880cea4e1aa88def5edd153d57bff00"
        ),
    )
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "6040600060406000600073eaf8c2ae0d01a880cea4e1aa88def5edd153d57b620249f0f2"  # noqa: E501
            "60005500"
        ),
    )
    pre[callee_2] = Account(
        balance=0x2540BE400,
        nonce=0,
        code=bytes.fromhex(
            "604060006040600060007394c8f980aeecbb6575b12ae614a249fc3e836f21620186a0f2"  # noqa: E501
            "60015500"
        ),
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xe04d1ac7ddda0c98397d56a0b501e960d4cd325a39286919ac23c1a07009a869"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=3000000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        callee: Account(code=bytes.fromhex("600160035500")),
        callee_1: Account(
            code=bytes.fromhex(
                "604060006040600060007373b954ebc05bb0ff4a0f6a13a054d50ad158409961c350f260025573eaf8c2ae0d01a880cea4e1aa88def5edd153d57bff00"  # noqa: E501
            ),
        ),
        contract: Account(
            storage={0: 1, 1: 1, 2: 1, 3: 1},
            code=bytes.fromhex(
                "6040600060406000600073eaf8c2ae0d01a880cea4e1aa88def5edd153d57b620249f0f260005500"  # noqa: E501
            ),
        ),
        callee_2: Account(
            code=bytes.fromhex(
                "604060006040600060007394c8f980aeecbb6575b12ae614a249fc3e836f21620186a0f260015500"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
