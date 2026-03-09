"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRandom/randomStatetest73Filler.json
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
    ["tests/static/state_tests/stRandom/randomStatetest73Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_random_statetest73(
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
            "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f0000"  # noqa: E501
            "0000000000000000000000000000000000000000000000000000000000007f0000000000"  # noqa: E501
            "00000000000000000000000000000000000000000000000000c3507f0000000000000000"  # noqa: E501
            "0000000000000000000000000000000000000000000000017f0000000000000000000000"  # noqa: E501
            "00945304eb96065b2a98b57a48a06ae28d285a71b57e7f00000000000000000000000094"  # noqa: E501
            "5304eb96065b2a98b57a48a06ae28d285a71b5b573198d729b711671056e0a0555346138"  # noqa: E501
            "55"
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
            "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f0000"  # noqa: E501
            "0000000000000000000000000000000000000000000000000000000000007f0000000000"  # noqa: E501
            "00000000000000000000000000000000000000000000000000c3507f0000000000000000"  # noqa: E501
            "0000000000000000000000000000000000000000000000017f0000000000000000000000"  # noqa: E501
            "00945304eb96065b2a98b57a48a06ae28d285a71b57e7f00000000000000000000000094"  # noqa: E501
            "5304eb96065b2a98b57a48a06ae28d285a71b5b573198d729b711671056e0a0555346138"  # noqa: E501
        ),
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=84268071,
    )

    post = {
        contract: Account(
            storage={
                0xB5B573198D729B711671056E0A0555346138: 0x7F000000000000000000000000945304EB96065B2A98B57A48A06AE28D285A,  # noqa: E501
            },
            code=bytes.fromhex(
                "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f00000000000000000000000000000000000000000000000000000000000000007f000000000000000000000000000000000000000000000000000000000000c3507f00000000000000000000000000000000000000000000000000000000000000017f000000000000000000000000945304eb96065b2a98b57a48a06ae28d285a71b57e7f000000000000000000000000945304eb96065b2a98b57a48a06ae28d285a71b5b573198d729b711671056e0a055534613855"  # noqa: E501
            ),
        ),
        coinbase: Account(
            code=bytes.fromhex("6000355415600957005b60203560003555"),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
