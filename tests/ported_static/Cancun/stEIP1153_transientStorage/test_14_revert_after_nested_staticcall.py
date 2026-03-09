"""
Transient storage can't be manipulated from nested staticcall.

Ported from:
tests/static/state_tests/Cancun/stEIP1153_transientStorage
14_revertAfterNestedStaticcallFiller.yml
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
    [
        "tests/static/state_tests/Cancun/stEIP1153_transientStorage/14_revertAfterNestedStaticcallFiller.yml",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_14_revert_after_nested_staticcall(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Transient storage can't be manipulated from nested staticcall."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xcef5f3b33e31360216fab2c61046840df9bd788e")
    contract = Address("0x1150baff55fdcea5fd92b0995358ec0c416debe3")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=4503599627370496,
    )

    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "5f3560e01c8063f5f4059014602f578063f8dfc2d014602b576362fdb9be14602357005b"  # noqa: E501
            "60296077565b005b605d565b506029600a5f5d5f5c5f55630f8dfc2d60e41b5f5260205f"  # noqa: E501
            "81813061fffffa5f516001556002555f5c600355565b63317edcdf60e11b5f525f806020"  # noqa: E501
            "8180305af15f5260205ff35b600b5f5d56"
        ),
        storage={0x1: 0xFFFF},
    )
    pre[sender] = Account(balance=0x3635C9ADC5DEA00000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xbe0e7d5fea1604bf57e004b0b414df8de04816dbb1c8f8719b725d0d6619b531"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex("f5f40590"),
        gas_limit=400000,
        max_fee_per_gas=2000,
        max_priority_fee_per_gas=0,
        nonce=0,
        value=0,
        access_list=[],
    )

    post = {
        contract: Account(
            storage={0: 10, 2: 1, 3: 10},
            code=bytes.fromhex(
                "5f3560e01c8063f5f4059014602f578063f8dfc2d014602b576362fdb9be14602357005b60296077565b005b605d565b506029600a5f5d5f5c5f55630f8dfc2d60e41b5f5260205f81813061fffffa5f516001556002555f5c600355565b63317edcdf60e11b5f525f8060208180305af15f5260205ff35b600b5f5d56"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
