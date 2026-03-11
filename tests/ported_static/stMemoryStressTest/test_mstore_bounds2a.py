"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stMemoryStressTest/MSTORE_Bounds2aFiller.json
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
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


@pytest.mark.ported_from(
    ["tests/static/state_tests/stMemoryStressTest/MSTORE_Bounds2aFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.valid_until("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit, expected_post",
    [
        (
            150000,
            {
                Address("0x10da52cbd00939aebe8218a1dd2eda0bffe93f30"): Account(
                    code=Op.MSTORE(offset=0x3FFFFF, value=0x1) + Op.STOP
                )
            },
        ),
        (
            250000000,
            {
                Address("0x10da52cbd00939aebe8218a1dd2eda0bffe93f30"): Account(
                    code=Op.MSTORE(offset=0x3FFFFF, value=0x1) + Op.STOP
                )
            },
        ),
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_mstore_bounds2a(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa99635038e8d9ab237a31179dd5c9087713f723a")
    contract = Address("0x10da52cbd00939aebe8218a1dd2eda0bffe93f30")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    # Source: LLL
    # {  (MSTORE 0x3fffff 1)}
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=Op.MSTORE(offset=0x3FFFFF, value=0x1) + Op.STOP,
    )
    pre[sender] = Account(
        balance=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
        nonce=0,
    )

    tx = Transaction(
        secret_key=Hash(
            "0x50eadfb1030587ab3a993a6ecc073041fc3b45e119daa31a13d78c7e209631a5"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
