"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stCallDelegateCodesHomestead
callcallcodecall_010_SuicideEndFiller.json
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
        "tests/static/state_tests/stCallDelegateCodesHomestead/callcallcodecall_010_SuicideEndFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_callcallcodecall_010_suicide_end(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0x4353e77718be108d4c149d88b34caceda42c5c66")
    callee = Address("0x2cac1d43f00e8b40b63426ab460c7e8717ee6455")
    callee_1 = Address("0x73b954ebc05bb0ff4a0f6a13a054d50ad1584099")
    callee_2 = Address("0xd957e143ad2c011bc6a2b142795f1a9ba70d0680")

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
        code=bytes.fromhex(
            "604060006040600073d957e143ad2c011bc6a2b142795f1a9ba70d0680620186a0f46001"  # noqa: E501
            "5500"
        ),
    )
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "60406000604060006000732cac1d43f00e8b40b63426ab460c7e8717ee6455620249f0f1"  # noqa: E501
            "60005500"
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
            "604060006040600060007373b954ebc05bb0ff4a0f6a13a054d50ad158409961c350f160"  # noqa: E501
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
        callee: Account(
            storage={1: 1, 2: 1},
            code=bytes.fromhex(
                "604060006040600073d957e143ad2c011bc6a2b142795f1a9ba70d0680620186a0f460015500"  # noqa: E501
            ),
        ),
        contract: Account(
            storage={0: 1},
            code=bytes.fromhex(
                "60406000604060006000732cac1d43f00e8b40b63426ab460c7e8717ee6455620249f0f160005500"  # noqa: E501
            ),
        ),
        callee_1: Account(storage={3: 1}, code=bytes.fromhex("600160035500")),
        callee_2: Account(
            code=bytes.fromhex(
                "604060006040600060007373b954ebc05bb0ff4a0f6a13a054d50ad158409961c350f1600255732cac1d43f00e8b40b63426ab460c7e8717ee6455ff00"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
