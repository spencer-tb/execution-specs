"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRandom2/randomStatetest564Filler.json
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
    ["tests/static/state_tests/stRandom2/randomStatetest564Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_random_statetest564(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x945304eb96065b2a98b57a48a06ae28d285a71b5")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x095e7baea6a6c7c4c2dfeb977efac326af552d87")

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
            "5b7f00000000000000000000000100000000000000000000000000000000000000007f00"  # noqa: E501
            "000000000000000000000100000000000000000000000000000000000000007f00000000"  # noqa: E501
            "0000000000000000ffffffffffffffffffffffffffffffffffffffff7f00000000000000"  # noqa: E501
            "0000000000945304eb96065b2a98b57a48a06ae28d285a71b57fffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffff"  # noqa: E501
            "fffffffffffffffffffffffffffffffffffffe7fffffffffffffffffffffffffffffffff"  # noqa: E501
            "fffffffffffffffffffffffffffffffe4550081655"
        ),
    )
    pre[coinbase] = Account(
        balance=46,
        nonce=0,
        code=bytes.fromhex("6000355415600957005b60203560003555"),
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex(
            "5b7f00000000000000000000000100000000000000000000000000000000000000007f00"  # noqa: E501
            "000000000000000000000100000000000000000000000000000000000000007f00000000"  # noqa: E501
            "0000000000000000ffffffffffffffffffffffffffffffffffffffff7f00000000000000"  # noqa: E501
            "0000000000945304eb96065b2a98b57a48a06ae28d285a71b57fffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffff"  # noqa: E501
            "fffffffffffffffffffffffffffffffffffffe7fffffffffffffffffffffffffffffffff"  # noqa: E501
            "fffffffffffffffffffffffffffffffe45500816"
        ),
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=286796184,
    )

    post = {
        contract: Account(
            storage={
                0x945304EB96065B2A98B57A48A06AE28D285A71B5: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
            },
            code=bytes.fromhex(
                "5b7f00000000000000000000000100000000000000000000000000000000000000007f00000000000000000000000100000000000000000000000000000000000000007f000000000000000000000000ffffffffffffffffffffffffffffffffffffffff7f000000000000000000000000945304eb96065b2a98b57a48a06ae28d285a71b57fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe7ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe4550081655"  # noqa: E501
            ),
        ),
        coinbase: Account(
            code=bytes.fromhex("6000355415600957005b60203560003555"),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
