"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRandom2/randomStatetest480Filler.json
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
    ["tests/static/state_tests/stRandom2/randomStatetest480Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_random_statetest480(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x4f3f701464972e74606d6ea82d4d3080599a0e79")
    sender = Address("0x2e3d0156d2b99a6eacba540c55f423c8f5a33143")
    contract = Address("0x0085349f22c7c8692fcee4f900382152fc914ffd")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "7ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe7fffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f0000000000"  # noqa: E501
            "00000000000000ffffffffffffffffffffffffffffffffffffffff037f00000000000000"  # noqa: E501
            "00000000000000000000000000000000000000000000000000427fffffffffffffffffff"  # noqa: E501
            "fffffffffffffffffffffffffffffffffffffffffffffe6f5af3a474ff64f3a37d51f36a"  # noqa: E501
            "6a607f5560005155"
        ),
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)
    pre[coinbase] = Account(
        balance=46,
        nonce=0,
        code=bytes.fromhex("6000355415600957005b60203560003555"),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xb1f4cbc3a50042184425a6f9e996d0910f7ba879457ce5dac5c71e498ad3c005"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex(
            "7ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe7fffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f0000000000"  # noqa: E501
            "00000000000000ffffffffffffffffffffffffffffffffffffffff037f00000000000000"  # noqa: E501
            "00000000000000000000000000000000000000000000000000427fffffffffffffffffff"  # noqa: E501
            "fffffffffffffffffffffffffffffffffffffffffffffe6f5af3a474ff64f3a37d51f36a"  # noqa: E501
            "6a607f"
        ),
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=745095931,
    )

    post = {
        contract: Account(
            storage={0: 0x5AF3A474FF64F3A37D51F36A6A607F55},
            code=bytes.fromhex(
                "7ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f000000000000000000000000ffffffffffffffffffffffffffffffffffffffff037f0000000000000000000000000000000000000000000000000000000000000000427ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe6f5af3a474ff64f3a37d51f36a6a607f5560005155"  # noqa: E501
            ),
        ),
        coinbase: Account(
            code=bytes.fromhex("6000355415600957005b60203560003555"),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
