"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stMemoryStressTest/CALL_Bounds3Filler.json
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
    ["tests/static/state_tests/stMemoryStressTest/CALL_Bounds3Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit, expected_post",
    [
        (
            150000,
            {
                Address("0x82475c10fea2425b322d1f97fcef265c5dc7c8c9"): Account(
                    code=bytes.fromhex(
                        "67ffffffffffffffff600067ffffffffffffffff6000600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff1506fffffffffffffffffffffffffffffffff60006fffffffffffffffffffffffffffffffff6000600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff1507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff60007fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff6000600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff15063ffffffff63ffffffff63ffffffff63ffffffff600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff15067ffffffffffffffff67ffffffffffffffff67ffffffffffffffff67ffffffffffffffff600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff1506fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff1507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff100"  # noqa: E501
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
                Address("0x82475c10fea2425b322d1f97fcef265c5dc7c8c9"): Account(
                    code=bytes.fromhex(
                        "67ffffffffffffffff600067ffffffffffffffff6000600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff1506fffffffffffffffffffffffffffffffff60006fffffffffffffffffffffffffffffffff6000600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff1507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff60007fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff6000600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff15063ffffffff63ffffffff63ffffffff63ffffffff600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff15067ffffffffffffffff67ffffffffffffffff67ffffffffffffffff67ffffffffffffffff600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff1506fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff1507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff100"  # noqa: E501
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
                Address("0x82475c10fea2425b322d1f97fcef265c5dc7c8c9"): Account(
                    code=bytes.fromhex(
                        "67ffffffffffffffff600067ffffffffffffffff6000600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff1506fffffffffffffffffffffffffffffffff60006fffffffffffffffffffffffffffffffff6000600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff1507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff60007fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff6000600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff15063ffffffff63ffffffff63ffffffff63ffffffff600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff15067ffffffffffffffff67ffffffffffffffff67ffffffffffffffff67ffffffffffffffff600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff1506fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff1507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff100"  # noqa: E501
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
def test_call_bounds3(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x4d2e21bbf9a40a8303787a066285648f8013129a")
    contract = Address("0x82475c10fea2425b322d1f97fcef265c5dc7c8c9")
    callee = Address("0x849f53126ade5f72469029537296f2b6644d4d41")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[sender] = Account(
        balance=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
        nonce=0,
    )
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "67ffffffffffffffff600067ffffffffffffffff6000600073849f53126ade5f72469029"  # noqa: E501
            "537296f2b6644d4d416707fffffffffffffff1506fffffffffffffffffffffffffffffff"  # noqa: E501
            "ff60006fffffffffffffffffffffffffffffffff6000600073849f53126ade5f72469029"  # noqa: E501
            "537296f2b6644d4d416707fffffffffffffff1507fffffffffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffff60007fffffffffffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffff6000600073849f53126ade5f72469029537296f2"  # noqa: E501
            "b6644d4d416707fffffffffffffff15063ffffffff63ffffffff63ffffffff63ffffffff"  # noqa: E501
            "600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff15067ff"  # noqa: E501
            "ffffffffffffff67ffffffffffffffff67ffffffffffffffff67ffffffffffffffff6000"  # noqa: E501
            "73849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff1506fffffff"  # noqa: E501
            "ffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffff"  # noqa: E501
            "ffffffffffffffffffffff6fffffffffffffffffffffffffffffffff600073849f53126a"  # noqa: E501
            "de5f72469029537296f2b6644d4d416707fffffffffffffff1507fffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffff600073849f53126ade5f72469029537296f2b6644d4d"  # noqa: E501
            "416707fffffffffffffff100"
        ),
    )
    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("60005460010160005500"),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xef111bbdab3a1622936afdfc9bbec4b5bc05b4fa4b1ef0ce2a55cef552f7650e"  # noqa: E501
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
