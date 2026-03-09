"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRandom/randomStatetest155Filler.json
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
    ["tests/static/state_tests/stRandom/randomStatetest155Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_random_statetest155(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x4f3f701464972e74606d6ea82d4d3080599a0e79")
    sender = Address("0x2e3d0156d2b99a6eacba540c55f423c8f5a33143")
    contract = Address("0xa8b18ae8f1784b75923dbc884c39419340a580ef")

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
            "457f00000000000000000000000000000000000000000000000000000000000000007fff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f00000000"  # noqa: E501
            "0000000000000000ffffffffffffffffffffffffffffffffffffffff7f00000000000000"  # noqa: E501
            "0000000000ffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffff"  # noqa: E501
            "fffffffffffffffffffffffffffffffffffffffffffe7f0000000000000000000000004f"  # noqa: E501
            "3f701464972e74606d6ea82d4d3080599a0e797f00000000000000000000000000000000"  # noqa: E501
            "000000000000000000000000000000006f3494f39b6ca29473a199580308910155600051"  # noqa: E501
            "55"
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xb1f4cbc3a50042184425a6f9e996d0910f7ba879457ce5dac5c71e498ad3c005"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex(
            "457f00000000000000000000000000000000000000000000000000000000000000007fff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f00000000"  # noqa: E501
            "0000000000000000ffffffffffffffffffffffffffffffffffffffff7f00000000000000"  # noqa: E501
            "0000000000ffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffff"  # noqa: E501
            "fffffffffffffffffffffffffffffffffffffffffffe7f0000000000000000000000004f"  # noqa: E501
            "3f701464972e74606d6ea82d4d3080599a0e797f00000000000000000000000000000000"  # noqa: E501
            "000000000000000000000000000000006f3494f39b6ca29473a1995803089101"
        ),
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=579536172,
    )

    post = {
        coinbase: Account(
            code=bytes.fromhex("6000355415600957005b60203560003555"),
        ),
        contract: Account(
            storage={0: 0x3494F39B6CA29473A199580308910155},
            code=bytes.fromhex(
                "457f00000000000000000000000000000000000000000000000000000000000000007fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f000000000000000000000000ffffffffffffffffffffffffffffffffffffffff7f000000000000000000000000ffffffffffffffffffffffffffffffffffffffff7ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe7f0000000000000000000000004f3f701464972e74606d6ea82d4d3080599a0e797f00000000000000000000000000000000000000000000000000000000000000006f3494f39b6ca29473a19958030891015560005155"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
