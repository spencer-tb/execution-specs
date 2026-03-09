"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRandom/randomStatetest28Filler.json
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
    ["tests/static/state_tests/stRandom/randomStatetest28Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_random_statetest28(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x4f3f701464972e74606d6ea82d4d3080599a0e79")
    sender = Address("0x2e3d0156d2b99a6eacba540c55f423c8f5a33143")
    contract = Address("0xdf2d980d762338e0da723885b33558d435309a78")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)
    pre[coinbase] = Account(
        balance=46,
        nonce=0,
        code=bytes.fromhex("6000355415600957005b60203560003555"),
    )
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "7ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe7fffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffffffffffffffffffff417f00000000000000"  # noqa: E501
            "000000000100000000000000000000000000000000000000007f00000000000000000000"  # noqa: E501
            "00004f3f701464972e74606d6ea82d4d3080599a0e796f38129d68939a19a2697172926f"  # noqa: E501
            "6a67363055"
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xb1f4cbc3a50042184425a6f9e996d0910f7ba879457ce5dac5c71e498ad3c005"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex(
            "7ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe7fffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffffffffffffffffffff417f00000000000000"  # noqa: E501
            "000000000100000000000000000000000000000000000000007f00000000000000000000"  # noqa: E501
            "00004f3f701464972e74606d6ea82d4d3080599a0e796f38129d68939a19a2697172926f"  # noqa: E501
            "6a673630"
        ),
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=1370440167,
    )

    post = {
        coinbase: Account(
            code=bytes.fromhex("6000355415600957005b60203560003555"),
        ),
        contract: Account(
            storage={
                0xDF2D980D762338E0DA723885B33558D435309A78: 0x38129D68939A19A2697172926F6A6736,  # noqa: E501
            },
            code=bytes.fromhex(
                "7ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff417f00000000000000000000000100000000000000000000000000000000000000007f0000000000000000000000004f3f701464972e74606d6ea82d4d3080599a0e796f38129d68939a19a2697172926f6a67363055"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
