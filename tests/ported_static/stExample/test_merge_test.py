"""
Example of PoS merge state test.

Ported from:
tests/static/state_tests/stExample/mergeTestFiller.yml
"""

import pytest
from execution_testing import (
    AccessList,
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
    ["tests/static/state_tests/stExample/mergeTestFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_merge_test(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Example of PoS merge state test."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x8dab845a8398167a1c204f0e79540d619be8b473")
    contract = Address("0x49a0fe79e28d1d65e16cdf53acafeae7baccac0e")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x1500000000000000000000000000000000000000000000000000000000000000,  # noqa: E501
        base_fee_per_gas=1000,
        gas_limit=16777216,
    )

    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=1,
        code=bytes.fromhex("3a600055486001554460025500"),
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=1)

    tx = Transaction(
        secret_key=Hash(
            "0xde0c95357363da5c1c5a73bd7c2781ca5c9fecc1014103b5e1d1e990ae8208ec"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex("00"),
        gas_limit=4000000,
        max_fee_per_gas=2000,
        max_priority_fee_per_gas=10,
        nonce=1,
        value=0,
        access_list=[
            AccessList(
                address=Address("0x49a0fe79e28d1d65e16cdf53acafeae7baccac0e"),
                storage_keys=[
                    Hash(
                        "0x0000000000000000000000000000000000000000000000000000000000000000"  # noqa: E501
                    ),
                    Hash(
                        "0x0000000000000000000000000000000000000000000000000000000000000001"  # noqa: E501
                    ),
                ],
            ),
        ],
    )

    post = {
        contract: Account(
            storage={
                0: 1010,
                1: 1000,
                2: 0x1500000000000000000000000000000000000000000000000000000000000000,  # noqa: E501
            },
            code=bytes.fromhex("3a600055486001554460025500"),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
