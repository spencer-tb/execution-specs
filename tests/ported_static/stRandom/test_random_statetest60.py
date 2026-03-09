"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRandom/randomStatetest60Filler.json
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
    ["tests/static/state_tests/stRandom/randomStatetest60Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_random_statetest60(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x4f3f701464972e74606d6ea82d4d3080599a0e79")
    sender = Address("0x2e3d0156d2b99a6eacba540c55f423c8f5a33143")
    contract = Address("0x97d4db1514b37df70e337f6511ef8cd55950821a")

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
            "427f0000000000000000000000000000000000000000000000000000000000000000427f"  # noqa: E501
            "000000000000000000000000ffffffffffffffffffffffffffffffffffffffff437f0000"  # noqa: E501
            "00000000000000000000000000000000000000000000000000000000c3507fffffffffff"  # noqa: E501
            "fffffffffffffffffffffffffffffffffffffffffffffffffffffe6f969001091aa15b8b"  # noqa: E501
            "9b75459d015a045560005155"
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xb1f4cbc3a50042184425a6f9e996d0910f7ba879457ce5dac5c71e498ad3c005"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex(
            "427f0000000000000000000000000000000000000000000000000000000000000000427f"  # noqa: E501
            "000000000000000000000000ffffffffffffffffffffffffffffffffffffffff437f0000"  # noqa: E501
            "00000000000000000000000000000000000000000000000000000000c3507fffffffffff"  # noqa: E501
            "fffffffffffffffffffffffffffffffffffffffffffffffffffffe6f969001091aa15b8b"  # noqa: E501
            "9b75459d015a04"
        ),
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=1423842991,
    )

    post = {
        coinbase: Account(
            code=bytes.fromhex("6000355415600957005b60203560003555"),
        ),
        contract: Account(
            storage={0: 0x969001091AA15B8B9B75459D015A0455},
            code=bytes.fromhex(
                "427f0000000000000000000000000000000000000000000000000000000000000000427f000000000000000000000000ffffffffffffffffffffffffffffffffffffffff437f000000000000000000000000000000000000000000000000000000000000c3507ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe6f969001091aa15b8b9b75459d015a045560005155"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
