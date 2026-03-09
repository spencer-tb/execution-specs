"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRandom/randomStatetest166Filler.json
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
    ["tests/static/state_tests/stRandom/randomStatetest166Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_random_statetest166(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x4f3f701464972e74606d6ea82d4d3080599a0e79")
    sender = Address("0x2e3d0156d2b99a6eacba540c55f423c8f5a33143")
    contract = Address("0x2f20efb4edc7dd07322d9c24d64c9ffdab363ccb")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "7f00000000000000000000000100000000000000000000000000000000000000007f0000"  # noqa: E501
            "00000000000000000000ffffffffffffffffffffffffffffffffffffffff817f00000000"  # noqa: E501
            "00000000000000010000000000000000000000000000000000000000417f000000000000"  # noqa: E501
            "00000000000000000000000000000000000000000000000000017f000000000000000000"  # noqa: E501
            "000000000000000000000000000000000000000000c350456f8eb7099d9f160532785143"  # noqa: E501
            "c5937e185560005155"
        ),
    )
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
            "7f00000000000000000000000100000000000000000000000000000000000000007f0000"  # noqa: E501
            "00000000000000000000ffffffffffffffffffffffffffffffffffffffff817f00000000"  # noqa: E501
            "00000000000000010000000000000000000000000000000000000000417f000000000000"  # noqa: E501
            "00000000000000000000000000000000000000000000000000017f000000000000000000"  # noqa: E501
            "000000000000000000000000000000000000000000c350456f8eb7099d9f160532785143"  # noqa: E501
            "c5937e18"
        ),
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=1614644579,
    )

    post = {
        contract: Account(
            storage={0: 0x8EB7099D9F160532785143C5937E1855},
            code=bytes.fromhex(
                "7f00000000000000000000000100000000000000000000000000000000000000007f000000000000000000000000ffffffffffffffffffffffffffffffffffffffff817f0000000000000000000000010000000000000000000000000000000000000000417f00000000000000000000000000000000000000000000000000000000000000017f000000000000000000000000000000000000000000000000000000000000c350456f8eb7099d9f160532785143c5937e185560005155"  # noqa: E501
            ),
        ),
        coinbase: Account(
            code=bytes.fromhex("6000355415600957005b60203560003555"),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
