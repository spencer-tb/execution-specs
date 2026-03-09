"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRandom2/randomStatetest630Filler.json
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
    ["tests/static/state_tests/stRandom2/randomStatetest630Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_random_statetest630(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x4f3f701464972e74606d6ea82d4d3080599a0e79")
    sender = Address("0x2e3d0156d2b99a6eacba540c55f423c8f5a33143")
    contract = Address("0x9d1ae3f0ce71afc95b61a0f1071af3d10ad1f7cd")

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
            "7f00000000000000000000000000000000000000000000000000000000000000017fffff"  # noqa: E501
            "fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe7f0000000000"  # noqa: E501
            "000000000000000000000000000000000000000000000000000001427f00000000000000"  # noqa: E501
            "000000000100000000000000000000000000000000000000007f00000000000000000000"  # noqa: E501
            "000100000000000000000000000000000000000000007fffffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffff6f9461a46e61507a1206917b17137e7e55600051"  # noqa: E501
            "55"
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xb1f4cbc3a50042184425a6f9e996d0910f7ba879457ce5dac5c71e498ad3c005"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex(
            "7f00000000000000000000000000000000000000000000000000000000000000017fffff"  # noqa: E501
            "fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe7f0000000000"  # noqa: E501
            "000000000000000000000000000000000000000000000000000001427f00000000000000"  # noqa: E501
            "000000000100000000000000000000000000000000000000007f00000000000000000000"  # noqa: E501
            "000100000000000000000000000000000000000000007fffffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffff6f9461a46e61507a1206917b17137e7e"
        ),
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=411786818,
    )

    post = {
        coinbase: Account(
            code=bytes.fromhex("6000355415600957005b60203560003555"),
        ),
        contract: Account(
            storage={0: 0x9461A46E61507A1206917B17137E7E55},
            code=bytes.fromhex(
                "7f00000000000000000000000000000000000000000000000000000000000000017ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe7f0000000000000000000000000000000000000000000000000000000000000001427f00000000000000000000000100000000000000000000000000000000000000007f00000000000000000000000100000000000000000000000000000000000000007fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff6f9461a46e61507a1206917b17137e7e5560005155"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
