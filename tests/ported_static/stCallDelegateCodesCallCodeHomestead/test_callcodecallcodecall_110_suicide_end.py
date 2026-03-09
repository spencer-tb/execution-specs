"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stCallDelegateCodesCallCodeHomestead
callcodecallcodecall_110_SuicideEndFiller.json
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
        "tests/static/state_tests/stCallDelegateCodesCallCodeHomestead/callcodecallcodecall_110_SuicideEndFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_callcodecallcodecall_110_suicide_end(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0x2b30b637f37e3f5b8ca4ab846331d0779a3f4671")
    callee = Address("0x2cac1d43f00e8b40b63426ab460c7e8717ee6455")
    callee_1 = Address("0x73b954ebc05bb0ff4a0f6a13a054d50ad1584099")
    callee_2 = Address("0x94c8f980aeecbb6575b12ae614a249fc3e836f21")

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
            "6040600060406000732cac1d43f00e8b40b63426ab460c7e8717ee6455620249f0f46000"  # noqa: E501
            "5500"
        ),
    )
    pre[callee] = Account(
        balance=0x2540BE400,
        nonce=0,
        code=bytes.fromhex(
            "60406000604060007394c8f980aeecbb6575b12ae614a249fc3e836f21620186a0f46001"  # noqa: E501
            "5500"
        ),
    )
    pre[callee_1] = Account(
        balance=0x2540BE400,
        nonce=0,
        code=bytes.fromhex("600160035500"),
    )
    pre[callee_2] = Account(
        balance=0x2540BE400,
        nonce=0,
        code=bytes.fromhex(
            "604060006040600060007373b954ebc05bb0ff4a0f6a13a054d50ad158409961c350f260"  # noqa: E501
            "0255732cac1d43f00e8b40b63426ab460c7e8717ee6455ff00"
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
        contract: Account(
            storage={0: 1, 1: 1, 2: 1, 3: 1},
            code=bytes.fromhex(
                "6040600060406000732cac1d43f00e8b40b63426ab460c7e8717ee6455620249f0f460005500"  # noqa: E501
            ),
        ),
        callee: Account(
            code=bytes.fromhex(
                "60406000604060007394c8f980aeecbb6575b12ae614a249fc3e836f21620186a0f460015500"  # noqa: E501
            ),
        ),
        callee_1: Account(code=bytes.fromhex("600160035500")),
        callee_2: Account(
            code=bytes.fromhex(
                "604060006040600060007373b954ebc05bb0ff4a0f6a13a054d50ad158409961c350f2600255732cac1d43f00e8b40b63426ab460c7e8717ee6455ff00"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
