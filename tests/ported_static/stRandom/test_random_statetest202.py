"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRandom/randomStatetest202Filler.json
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
    ["tests/static/state_tests/stRandom/randomStatetest202Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_random_statetest202(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x4f3f701464972e74606d6ea82d4d3080599a0e79")
    sender = Address("0x2e3d0156d2b99a6eacba540c55f423c8f5a33143")
    contract = Address("0x1099229c5d84d6bc6a189e2189357e91c30c6f6a")

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
            "7f00000000000000000000000000000000000000000000000000000000000000007f0000"  # noqa: E501
            "00000000000000000000000000000000000000000000000000000000c3507f0000000000"  # noqa: E501
            "000000000000000000000000000000000000000000000000000000557f00000000000000"  # noqa: E501
            "000000000000000000000000000000000000000000000000007f00000000000000000000"  # noqa: E501
            "000000000000000000000000000000000000000000007f00000000000000000000000000"  # noqa: E501
            "0000000000000000000000000000000000c3507f000000000000000000000000ffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffff6750a3190486f0"
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
            "7f00000000000000000000000000000000000000000000000000000000000000007f0000"  # noqa: E501
            "00000000000000000000000000000000000000000000000000000000c3507f0000000000"  # noqa: E501
            "000000000000000000000000000000000000000000000000000000557f00000000000000"  # noqa: E501
            "000000000000000000000000000000000000000000000000007f00000000000000000000"  # noqa: E501
            "000000000000000000000000000000000000000000007f00000000000000000000000000"  # noqa: E501
            "0000000000000000000000000000000000c3507f000000000000000000000000ffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffff6750a3190486f0"
        ),
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=827910093,
    )

    post = {
        contract: Account(
            storage={0: 50000},
            code=bytes.fromhex(
                "7f00000000000000000000000000000000000000000000000000000000000000007f000000000000000000000000000000000000000000000000000000000000c3507f0000000000000000000000000000000000000000000000000000000000000000557f00000000000000000000000000000000000000000000000000000000000000007f00000000000000000000000000000000000000000000000000000000000000007f000000000000000000000000000000000000000000000000000000000000c3507f000000000000000000000000ffffffffffffffffffffffffffffffffffffffff6750a3190486f0"  # noqa: E501
            ),
        ),
        coinbase: Account(
            code=bytes.fromhex("6000355415600957005b60203560003555"),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
