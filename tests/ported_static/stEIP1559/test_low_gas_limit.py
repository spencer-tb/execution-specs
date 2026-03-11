"""
Ori Pomerantz qbzzt1@gmail.com.

Ported from:
tests/static/state_tests/stEIP1559/lowGasLimitFiller.yml
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
    TransactionException,
)
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


@pytest.mark.ported_from(
    ["tests/static/state_tests/stEIP1559/lowGasLimitFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit, tx_error, expected_post",
    [
        pytest.param(
            90000,
            TransactionException.GAS_ALLOWANCE_EXCEEDED,
            {
                Address("0xef0454d0376d1921b9a83868282725853c293ab5"): Account(
                    storage={0: 24743},
                    code=Op.SSTORE(key=0x0, value=0x2) + Op.STOP,
                )
            },
            id="case0",
            marks=pytest.mark.exception_test,
        ),
        pytest.param(
            50000,
            None,
            {
                Address("0xef0454d0376d1921b9a83868282725853c293ab5"): Account(
                    storage={0: 2},
                    code=Op.SSTORE(key=0x0, value=0x2) + Op.STOP,
                )
            },
            id="case1",
        ),
        pytest.param(
            25000,
            None,
            {
                Address("0xef0454d0376d1921b9a83868282725853c293ab5"): Account(
                    storage={0: 24743},
                    code=Op.SSTORE(key=0x0, value=0x2) + Op.STOP,
                )
            },
            id="case2",
        ),
        pytest.param(
            20000,
            TransactionException.INTRINSIC_GAS_TOO_LOW,
            {
                Address("0xef0454d0376d1921b9a83868282725853c293ab5"): Account(
                    storage={0: 24743},
                    code=Op.SSTORE(key=0x0, value=0x2) + Op.STOP,
                )
            },
            id="case3",
            marks=pytest.mark.exception_test,
        ),
    ],
)
@pytest.mark.pre_alloc_mutable
def test_low_gas_limit(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
    tx_error: object,
    expected_post: dict,
) -> None:
    """Ori Pomerantz qbzzt1@gmail.com."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x8dab845a8398167a1c204f0e79540d619be8b473")
    contract = Address("0xef0454d0376d1921b9a83868282725853c293ab5")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=1000,
        gas_limit=80000,
    )

    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=1)
    # Source: Yul
    # {
    #     sstore(0, add(1,1))
    # }
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=Op.SSTORE(key=0x0, value=0x2) + Op.STOP,
        storage={0x0: 0x60A7},
    )

    tx = Transaction(
        secret_key=Hash(
            "0xde0c95357363da5c1c5a73bd7c2781ca5c9fecc1014103b5e1d1e990ae8208ec"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex("00"),
        gas_limit=tx_gas_limit,
        max_fee_per_gas=1000,
        max_priority_fee_per_gas=1000,
        nonce=1,
        value=0,
        access_list=[],
        error=tx_error,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
