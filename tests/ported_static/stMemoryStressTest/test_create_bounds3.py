"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stMemoryStressTest/CREATE_Bounds3Filler.json
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
    ["tests/static/state_tests/stMemoryStressTest/CREATE_Bounds3Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit, expected_post",
    [
        (
            150000,
            {
                Address("0x1000000000000000000000000000000000000000"): Account(
                    code=bytes.fromhex(
                        "7f6001600155601080600c6000396000f3006000355415600957005b60203560006000526035602053605560215367ffffffffffffffff60006001f0506fffffffffffffffffffffffffffffffff60006001f0507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff60006001f0506000630fffffff6001f050600063ffffffff6001f050600067ffffffffffffffff6001f05060006fffffffffffffffffffffffffffffffff6001f05060007fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff6001f050630fffffff630fffffff6001f05063ffffffff63ffffffff6001f05067ffffffffffffffff67ffffffffffffffff6001f0506fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6001f0507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff6001f000"  # noqa: E501
                    )
                )
            },
        ),
        (
            1000000,
            {
                Address("0x1000000000000000000000000000000000000000"): Account(
                    code=bytes.fromhex(
                        "7f6001600155601080600c6000396000f3006000355415600957005b60203560006000526035602053605560215367ffffffffffffffff60006001f0506fffffffffffffffffffffffffffffffff60006001f0507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff60006001f0506000630fffffff6001f050600063ffffffff6001f050600067ffffffffffffffff6001f05060006fffffffffffffffffffffffffffffffff6001f05060007fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff6001f050630fffffff630fffffff6001f05063ffffffff63ffffffff6001f05067ffffffffffffffff67ffffffffffffffff6001f0506fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6001f0507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff6001f000"  # noqa: E501
                    )
                )
            },
        ),
        (
            16777216,
            {
                Address("0x1000000000000000000000000000000000000000"): Account(
                    code=bytes.fromhex(
                        "7f6001600155601080600c6000396000f3006000355415600957005b60203560006000526035602053605560215367ffffffffffffffff60006001f0506fffffffffffffffffffffffffffffffff60006001f0507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff60006001f0506000630fffffff6001f050600063ffffffff6001f050600067ffffffffffffffff6001f05060006fffffffffffffffffffffffffffffffff6001f05060007fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff6001f050630fffffff630fffffff6001f05063ffffffff63ffffffff6001f05067ffffffffffffffff67ffffffffffffffff6001f0506fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6001f0507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff6001f000"  # noqa: E501
                    )
                )
            },
        ),
    ],
    ids=["case0", "case1", "case2"],
)
@pytest.mark.pre_alloc_mutable
def test_create_bounds3(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x1000000000000000000000000000000000000000")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[contract] = Account(
        balance=100,
        nonce=0,
        code=bytes.fromhex(
            "7f6001600155601080600c6000396000f3006000355415600957005b6020356000600052"  # noqa: E501
            "6035602053605560215367ffffffffffffffff60006001f0506fffffffffffffffffffff"  # noqa: E501
            "ffffffffffff60006001f0507fffffffffffffffffffffffffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffff60006001f0506000630fffffff6001f050600063ffffffff6001f0"  # noqa: E501
            "50600067ffffffffffffffff6001f05060006fffffffffffffffffffffffffffffffff60"  # noqa: E501
            "01f05060007fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"  # noqa: E501
            "ffff6001f050630fffffff630fffffff6001f05063ffffffff63ffffffff6001f05067ff"  # noqa: E501
            "ffffffffffffff67ffffffffffffffff6001f0506fffffffffffffffffffffffffffffff"  # noqa: E501
            "ff6fffffffffffffffffffffffffffffffff6001f0507fffffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffff6001f000"
        ),
    )
    pre[sender] = Account(
        balance=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
        nonce=0,
    )

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
