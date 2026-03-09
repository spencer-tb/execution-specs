"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stMemoryStressTest/DELEGATECALL_Bounds3Filler.json
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
        "tests/static/state_tests/stMemoryStressTest/DELEGATECALL_Bounds3Filler.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit, expected_post",
    [
        (
            150000,
            {
                Address("0x5a6cc254b318bb5f7539fcc10cfb01c517154c5c"): Account(
                    code=bytes.fromhex(
                        "67ffffffffffffffff600067ffffffffffffffff600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff4506fffffffffffffffffffffffffffffffff60006fffffffffffffffffffffffffffffffff600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff4507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff60007fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff45067ffffffffffffffff67ffffffffffffffff67ffffffffffffffff67ffffffffffffffff73849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff4506fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff73849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff4507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff73849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff400"  # noqa: E501
                    )
                ),
                Address("0x849f53126ade5f72469029537296f2b6644d4d41"): Account(
                    code=bytes.fromhex("60005460010160005500")
                ),
            },
        ),
        (
            1000000,
            {
                Address("0x5a6cc254b318bb5f7539fcc10cfb01c517154c5c"): Account(
                    code=bytes.fromhex(
                        "67ffffffffffffffff600067ffffffffffffffff600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff4506fffffffffffffffffffffffffffffffff60006fffffffffffffffffffffffffffffffff600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff4507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff60007fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff45067ffffffffffffffff67ffffffffffffffff67ffffffffffffffff67ffffffffffffffff73849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff4506fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff73849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff4507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff73849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff400"  # noqa: E501
                    )
                ),
                Address("0x849f53126ade5f72469029537296f2b6644d4d41"): Account(
                    code=bytes.fromhex("60005460010160005500")
                ),
            },
        ),
        (
            16777216,
            {
                Address("0x5a6cc254b318bb5f7539fcc10cfb01c517154c5c"): Account(
                    code=bytes.fromhex(
                        "67ffffffffffffffff600067ffffffffffffffff600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff4506fffffffffffffffffffffffffffffffff60006fffffffffffffffffffffffffffffffff600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff4507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff60007fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff45067ffffffffffffffff67ffffffffffffffff67ffffffffffffffff67ffffffffffffffff73849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff4506fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff73849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff4507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff73849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff400"  # noqa: E501
                    )
                ),
                Address("0x849f53126ade5f72469029537296f2b6644d4d41"): Account(
                    code=bytes.fromhex("60005460010160005500")
                ),
            },
        ),
    ],
    ids=["case0", "case1", "case2"],
)
@pytest.mark.pre_alloc_mutable
def test_delegatecall_bounds3(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa99635038e8d9ab237a31179dd5c9087713f723a")
    contract = Address("0x5a6cc254b318bb5f7539fcc10cfb01c517154c5c")
    callee = Address("0x849f53126ade5f72469029537296f2b6644d4d41")

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
            "67ffffffffffffffff600067ffffffffffffffff600073849f53126ade5f724690295372"  # noqa: E501
            "96f2b6644d4d416707fffffffffffffff4506fffffffffffffffffffffffffffffffff60"  # noqa: E501
            "006fffffffffffffffffffffffffffffffff600073849f53126ade5f72469029537296f2"  # noqa: E501
            "b6644d4d416707fffffffffffffff4507fffffffffffffffffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffff60007fffffffffffffffffffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffff600073849f53126ade5f72469029537296f2b6644d4d4167"  # noqa: E501
            "07fffffffffffffff45067ffffffffffffffff67ffffffffffffffff67ffffffffffffff"  # noqa: E501
            "ff67ffffffffffffffff73849f53126ade5f72469029537296f2b6644d4d416707ffffff"  # noqa: E501
            "fffffffff4506fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffff"  # noqa: E501
            "ffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffff"  # noqa: E501
            "ffff73849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff4507fff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffffffffff73849f53126ade5f724690295372"  # noqa: E501
            "96f2b6644d4d416707fffffffffffffff400"
        ),
    )
    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("60005460010160005500"),
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
