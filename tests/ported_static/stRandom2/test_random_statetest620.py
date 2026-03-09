"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRandom2/randomStatetest620Filler.json
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
    ["tests/static/state_tests/stRandom2/randomStatetest620Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_random_statetest620(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x4f3f701464972e74606d6ea82d4d3080599a0e79")
    sender = Address("0x2e3d0156d2b99a6eacba540c55f423c8f5a33143")
    contract = Address("0x388b9f8645907d4c06dee4ebab70d61e76fa253c")

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
            "7f000000000000000000000000ffffffffffffffffffffffffffffffffffffffff427f00"  # noqa: E501
            "00000000000000000000010000000000000000000000000000000000000000457fffffff"  # noqa: E501
            "fffffffffffffffffffffffffffffffffffffffffffffffffffffffffe7f000000000000"  # noqa: E501
            "000000000000000000000000000000000000000000000000c3507f000000000000000000"  # noqa: E501
            "00000000000000000000000000000000000000000000007fffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffffff6f6c54a420327d73727d9d1a667bf389"  # noqa: E501
            "5560005155"
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
            "7f000000000000000000000000ffffffffffffffffffffffffffffffffffffffff427f00"  # noqa: E501
            "00000000000000000000010000000000000000000000000000000000000000457fffffff"  # noqa: E501
            "fffffffffffffffffffffffffffffffffffffffffffffffffffffffffe7f000000000000"  # noqa: E501
            "000000000000000000000000000000000000000000000000c3507f000000000000000000"  # noqa: E501
            "00000000000000000000000000000000000000000000007fffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffffff6f6c54a420327d73727d9d1a667bf389"  # noqa: E501
        ),
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=1643601446,
    )

    post = {
        contract: Account(
            storage={0: 0x6C54A420327D73727D9D1A667BF38955},
            code=bytes.fromhex(
                "7f000000000000000000000000ffffffffffffffffffffffffffffffffffffffff427f0000000000000000000000010000000000000000000000000000000000000000457ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe7f000000000000000000000000000000000000000000000000000000000000c3507f00000000000000000000000000000000000000000000000000000000000000007fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff6f6c54a420327d73727d9d1a667bf3895560005155"  # noqa: E501
            ),
        ),
        coinbase: Account(
            code=bytes.fromhex("6000355415600957005b60203560003555"),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
