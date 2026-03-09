"""
CALLCODE -> CALLCODE -> DELEGATE -> CODE OOG.

Ported from:
tests/static/state_tests/stCallDelegateCodesCallCodeHomestead
callcallcallcode_001_OOGEFiller.json
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
        "tests/static/state_tests/stCallDelegateCodesCallCodeHomestead/callcallcallcode_001_OOGEFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_callcallcallcode_001_ooge(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """CALLCODE -> CALLCODE -> DELEGATE -> CODE OOG."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0x9e57433afaff8a546fbc43cf0330afb6561dc550")
    callee = Address("0x1dd747f92062bb53bb8e867ec2902792435f1748")
    callee_1 = Address("0x3e423a7b1fba04d0c3f9423a3ae2a180d2878d5b")
    callee_2 = Address("0x913cf7a18f61bab7bccf5607dfa9b730c5976000")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=30000000,
    )

    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("6001600355622fffff60002000"),
    )
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "6040600060406000731dd747f92062bb53bb8e867ec2902792435f174862061a80f46002"  # noqa: E501
            "556001600b5500"
        ),
    )
    pre[callee_2] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "60406000604060006000733e423a7b1fba04d0c3f9423a3ae2a180d2878d5b620927c0f2"  # noqa: E501
            "60015500"
        ),
    )
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "6040600060406000600073913cf7a18f61bab7bccf5607dfa9b730c5976000620c3500f2"  # noqa: E501
            "60005500"
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
        callee: Account(code=bytes.fromhex("6001600355622fffff60002000")),
        callee_1: Account(
            code=bytes.fromhex(
                "6040600060406000731dd747f92062bb53bb8e867ec2902792435f174862061a80f46002556001600b5500"  # noqa: E501
            ),
        ),
        callee_2: Account(
            code=bytes.fromhex(
                "60406000604060006000733e423a7b1fba04d0c3f9423a3ae2a180d2878d5b620927c0f260015500"  # noqa: E501
            ),
        ),
        contract: Account(
            storage={0: 1, 1: 1, 11: 1},
            code=bytes.fromhex(
                "6040600060406000600073913cf7a18f61bab7bccf5607dfa9b730c5976000620c3500f260005500"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
