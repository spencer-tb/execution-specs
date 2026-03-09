"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stMemoryStressTest/CALLCODE_Bounds4Filler.json
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
        "tests/static/state_tests/stMemoryStressTest/CALLCODE_Bounds4Filler.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit, expected_post",
    [
        (
            150000,
            {
                Address("0x849f53126ade5f72469029537296f2b6644d4d41"): Account(
                    code=bytes.fromhex("60005460010160005500")
                ),
                Address("0xc0479fbac15cb575e66ded014fd60ceb98749b04"): Account(
                    code=bytes.fromhex(
                        "67ffffffffffffffff600067ffffffffffffffff6000600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff2506fffffffffffffffffffffffffffffffff60006fffffffffffffffffffffffffffffffff6000600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff2507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff60007fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff6000600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff25067ffffffffffffffff67ffffffffffffffff67ffffffffffffffff67ffffffffffffffff600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff25067ffffffffffffffff67ffffffffffffffff67ffffffffffffffff67ffffffffffffffff600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff2507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff2506fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff200"  # noqa: E501
                    )
                ),
            },
        ),
        (
            1000000,
            {
                Address("0x849f53126ade5f72469029537296f2b6644d4d41"): Account(
                    code=bytes.fromhex("60005460010160005500")
                ),
                Address("0xc0479fbac15cb575e66ded014fd60ceb98749b04"): Account(
                    code=bytes.fromhex(
                        "67ffffffffffffffff600067ffffffffffffffff6000600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff2506fffffffffffffffffffffffffffffffff60006fffffffffffffffffffffffffffffffff6000600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff2507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff60007fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff6000600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff25067ffffffffffffffff67ffffffffffffffff67ffffffffffffffff67ffffffffffffffff600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff25067ffffffffffffffff67ffffffffffffffff67ffffffffffffffff67ffffffffffffffff600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff2507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff2506fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff200"  # noqa: E501
                    )
                ),
            },
        ),
        (
            16777216,
            {
                Address("0x849f53126ade5f72469029537296f2b6644d4d41"): Account(
                    code=bytes.fromhex("60005460010160005500")
                ),
                Address("0xc0479fbac15cb575e66ded014fd60ceb98749b04"): Account(
                    code=bytes.fromhex(
                        "67ffffffffffffffff600067ffffffffffffffff6000600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff2506fffffffffffffffffffffffffffffffff60006fffffffffffffffffffffffffffffffff6000600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff2507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff60007fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff6000600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff25067ffffffffffffffff67ffffffffffffffff67ffffffffffffffff67ffffffffffffffff600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff25067ffffffffffffffff67ffffffffffffffff67ffffffffffffffff67ffffffffffffffff600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff2507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff2506fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff200"  # noqa: E501
                    )
                ),
            },
        ),
    ],
    ids=["case0", "case1", "case2"],
)
@pytest.mark.pre_alloc_mutable
def test_callcode_bounds4(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa99635038e8d9ab237a31179dd5c9087713f723a")
    contract = Address("0xc0479fbac15cb575e66ded014fd60ceb98749b04")
    callee = Address("0x849f53126ade5f72469029537296f2b6644d4d41")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
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
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "67ffffffffffffffff600067ffffffffffffffff6000600073849f53126ade5f72469029"  # noqa: E501
            "537296f2b6644d4d416707fffffffffffffff2506fffffffffffffffffffffffffffffff"  # noqa: E501
            "ff60006fffffffffffffffffffffffffffffffff6000600073849f53126ade5f72469029"  # noqa: E501
            "537296f2b6644d4d416707fffffffffffffff2507fffffffffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffff60007fffffffffffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffff6000600073849f53126ade5f72469029537296f2"  # noqa: E501
            "b6644d4d416707fffffffffffffff25067ffffffffffffffff67ffffffffffffffff67ff"  # noqa: E501
            "ffffffffffffff67ffffffffffffffff600073849f53126ade5f72469029537296f2b664"  # noqa: E501
            "4d4d416707fffffffffffffff25067ffffffffffffffff67ffffffffffffffff67ffffff"  # noqa: E501
            "ffffffffff67ffffffffffffffff600073849f53126ade5f72469029537296f2b6644d4d"  # noqa: E501
            "416707fffffffffffffff2507fffffffffffffffffffffffffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"  # noqa: E501
            "ffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"  # noqa: E501
            "600073849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff2506fff"  # noqa: E501
            "ffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffff"  # noqa: E501
            "ffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff600073849f53"  # noqa: E501
            "126ade5f72469029537296f2b6644d4d416707fffffffffffffff200"
        ),
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
