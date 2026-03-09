"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stCallDelegateCodesHomestead
callcodecallcallcode_101_SuicideMiddleFiller.json
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
        "tests/static/state_tests/stCallDelegateCodesHomestead/callcodecallcallcode_101_SuicideMiddleFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_callcodecallcallcode_101_suicide_middle(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x1000000000000000000000000000000000000000")
    callee = Address("0x1000000000000000000000000000000000000001")
    callee_1 = Address("0x1000000000000000000000000000000000000002")
    callee_2 = Address("0x1000000000000000000000000000000000000003")

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
            "6040600060406000731000000000000000000000000000000000000001620249f0f46000"  # noqa: E501
            "5500"
        ),
    )
    pre[callee] = Account(
        balance=0x2540BE400,
        nonce=0,
        code=bytes.fromhex(
            "60406000604060006000731000000000000000000000000000000000000002620186a0f1"  # noqa: E501
            "60015500"
        ),
    )
    pre[callee_1] = Account(
        balance=0x2540BE400,
        nonce=0,
        code=bytes.fromhex(
            "731000000000000000000000000000000000000000ff6040600060406000731000000000"  # noqa: E501
            "00000000000000000000000000000361c350f460025500"
        ),
    )
    pre[callee_2] = Account(
        balance=0x2540BE400,
        nonce=0,
        code=bytes.fromhex("600160035500"),
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
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
            storage={0: 1, 1: 1},
            code=bytes.fromhex(
                "6040600060406000731000000000000000000000000000000000000001620249f0f460005500"  # noqa: E501
            ),
        ),
        callee: Account(
            code=bytes.fromhex(
                "60406000604060006000731000000000000000000000000000000000000002620186a0f160015500"  # noqa: E501
            ),
        ),
        callee_1: Account(
            code=bytes.fromhex(
                "731000000000000000000000000000000000000000ff604060006040600073100000000000000000000000000000000000000361c350f460025500"  # noqa: E501
            ),
        ),
        callee_2: Account(code=bytes.fromhex("600160035500")),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
