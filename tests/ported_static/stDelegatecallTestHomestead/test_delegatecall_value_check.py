"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stDelegatecallTestHomestead
delegatecallValueCheckFiller.json
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
        "tests/static/state_tests/stDelegatecallTestHomestead/delegatecallValueCheckFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_delegatecall_value_check(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0x55bb8a8658b848ebbbb73cbf6ac9d59d715aec58")
    callee = Address("0x5d25ad2a26f849e9400d6b65244f26f4eea11adf")

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
            "6002600060406000735d25ad2a26f849e9400d6b65244f26f4eea11adf6207a120f46000"  # noqa: E501
            "5500"
        ),
    )
    pre[callee] = Account(
        balance=23,
        nonce=0,
        code=bytes.fromhex("3460015500"),
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
        value=23,
    )

    post = {
        contract: Account(
            storage={0: 1, 1: 23},
            code=bytes.fromhex(
                "6002600060406000735d25ad2a26f849e9400d6b65244f26f4eea11adf6207a120f460005500"  # noqa: E501
            ),
        ),
        callee: Account(code=bytes.fromhex("3460015500")),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
