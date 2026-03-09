"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stSolidityTest/AmbiguousMethodFiller.json
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
    ["tests/static/state_tests/stSolidityTest/AmbiguousMethodFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_ambiguous_method(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x73c241c3bc4fdf83b6ff3ae73735fddf7c9d711d")
    contract = Address("0x235c9320b0f4d30204334c1ddb008dfe1d75b1b9")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000,
    )

    pre[contract] = Account(
        balance=0x186A0,
        nonce=0,
        code=bytes.fromhex(
            "60003560e060020a90048063c040622614601557005b601b6021565b60006000f35b6101"  # noqa: E501
            "4f60008190555056"
        ),
    )
    pre[sender] = Account(balance=0x12A05F200, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xa9ae12cb2700c0214f86b9796881bc03a1fd5605d0e76d2da2ca592e62d53e52"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex("c0406226"),
        gas_limit=300000,
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = {
        contract: Account(
            storage={0: 335},
            code=bytes.fromhex(
                "60003560e060020a90048063c040622614601557005b601b6021565b60006000f35b61014f60008190555056"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
