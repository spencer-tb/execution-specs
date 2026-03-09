"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRandom/randomStatetest275Filler.json
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
    ["tests/static/state_tests/stRandom/randomStatetest275Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_random_statetest275(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x4f3f701464972e74606d6ea82d4d3080599a0e79")
    sender = Address("0x2e3d0156d2b99a6eacba540c55f423c8f5a33143")
    contract = Address("0x69d3e12fb87d7effeb9ded3d46879ebe02925b4e")

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
            "437f000000000000000000000000000000000000000000000000000000000000c3507fff"  # noqa: E501
            "fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe7fffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f00000000000000"  # noqa: E501
            "00000000000000000000000000000000000000000000000000197fffffffffffffffffff"  # noqa: E501
            "fffffffffffffffffffffffffffffffffffffffffffffe09656756323c597455"
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xb1f4cbc3a50042184425a6f9e996d0910f7ba879457ce5dac5c71e498ad3c005"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex(
            "437f000000000000000000000000000000000000000000000000000000000000c3507fff"  # noqa: E501
            "fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe7fffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f00000000000000"  # noqa: E501
            "00000000000000000000000000000000000000000000000000197fffffffffffffffffff"  # noqa: E501
            "fffffffffffffffffffffffffffffffffffffffffffffe09656756323c5974"
        ),
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=4157391,
    )

    post = {
        coinbase: Account(
            code=bytes.fromhex("6000355415600957005b60203560003555"),
        ),
        contract: Account(
            code=bytes.fromhex(
                "437f000000000000000000000000000000000000000000000000000000000000c3507ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f0000000000000000000000000000000000000000000000000000000000000000197ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe09656756323c597455"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
