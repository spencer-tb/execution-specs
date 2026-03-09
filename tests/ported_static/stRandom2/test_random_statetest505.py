"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRandom2/randomStatetest505Filler.json
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
    ["tests/static/state_tests/stRandom2/randomStatetest505Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_random_statetest505(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x4f3f701464972e74606d6ea82d4d3080599a0e79")
    sender = Address("0x2e3d0156d2b99a6eacba540c55f423c8f5a33143")
    contract = Address("0x7aa0fc7f8aa86925083a8fe4388167a152409e49")

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
            "7ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe427f00"  # noqa: E501
            "000000000000000000000000000000000000000000000000000000000000017f00000000"  # noqa: E501
            "000000000000000000000000000000000000000000000000000000007fffffffffffffff"  # noqa: E501
            "fffffffffffffffffffffffffffffffffffffffffffffffffe457f000000000000000000"  # noqa: E501
            "00000000000000000000000000000000000000000000007f000000000000000000000001"  # noqa: E501
            "00000000000000000000000000000000000000006f44a06f550371317376738c53998437"  # noqa: E501
            "5560005155"
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xb1f4cbc3a50042184425a6f9e996d0910f7ba879457ce5dac5c71e498ad3c005"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex(
            "7ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe427f00"  # noqa: E501
            "000000000000000000000000000000000000000000000000000000000000017f00000000"  # noqa: E501
            "000000000000000000000000000000000000000000000000000000007fffffffffffffff"  # noqa: E501
            "fffffffffffffffffffffffffffffffffffffffffffffffffe457f000000000000000000"  # noqa: E501
            "00000000000000000000000000000000000000000000007f000000000000000000000001"  # noqa: E501
            "00000000000000000000000000000000000000006f44a06f550371317376738c53998437"  # noqa: E501
        ),
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=1075033443,
    )

    post = {
        coinbase: Account(
            code=bytes.fromhex("6000355415600957005b60203560003555"),
        ),
        contract: Account(
            storage={0: 0x44A06F550371317376738C5399843755},
            code=bytes.fromhex(
                "7ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe427f00000000000000000000000000000000000000000000000000000000000000017f00000000000000000000000000000000000000000000000000000000000000007ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe457f00000000000000000000000000000000000000000000000000000000000000007f00000000000000000000000100000000000000000000000000000000000000006f44a06f550371317376738c539984375560005155"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
