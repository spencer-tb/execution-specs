"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stCallDelegateCodesCallCodeHomestead
callcodecallcode_11_SuicideEndFiller.json
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
        "tests/static/state_tests/stCallDelegateCodesCallCodeHomestead/callcodecallcode_11_SuicideEndFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_callcodecallcode_11_suicide_end(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0x2b30b637f37e3f5b8ca4ab846331d0779a3f4671")
    callee = Address("0x1cca6e93108ec94304ae5eb121d323e6c317fe7a")
    callee_1 = Address("0x703b936fd4d674f0ff5d6957f61097152f8781b8")

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
            "604060006040600073703b936fd4d674f0ff5d6957f61097152f8781b861c350f4600155"  # noqa: E501
            "732b30b637f37e3f5b8ca4ab846331d0779a3f4671ff00"
        ),
    )
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "6040600060406000731cca6e93108ec94304ae5eb121d323e6c317fe7a620249f0f46000"  # noqa: E501
            "5500"
        ),
    )
    pre[callee_1] = Account(
        balance=0x2540BE400,
        nonce=0,
        code=bytes.fromhex("600160025500"),
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
            code=bytes.fromhex(
                "604060006040600073703b936fd4d674f0ff5d6957f61097152f8781b861c350f4600155732b30b637f37e3f5b8ca4ab846331d0779a3f4671ff00"  # noqa: E501
            ),
        ),
        contract: Account(
            storage={0: 1, 1: 1, 2: 1},
            code=bytes.fromhex(
                "6040600060406000731cca6e93108ec94304ae5eb121d323e6c317fe7a620249f0f460005500"  # noqa: E501
            ),
        ),
        callee_1: Account(code=bytes.fromhex("600160025500")),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
