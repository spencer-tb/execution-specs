"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stCreate2/CREATE2_Bounds3Filler.json
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
    ["tests/static/state_tests/stCreate2/CREATE2_Bounds3Filler.json"],
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
                        "7f6001600155601080600c6000396000f3006000355415600957005b602035600060005260356020536055602153600067ffffffffffffffff60006001f55060006fffffffffffffffffffffffffffffffff60006001f55060007fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff60006001f55060006000630fffffff6001f5506000600063ffffffff6001f5506000600067ffffffffffffffff6001f550600060006fffffffffffffffffffffffffffffffff6001f550600060007fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff6001f5506000630fffffff630fffffff6001f550600063ffffffff63ffffffff6001f550600067ffffffffffffffff67ffffffffffffffff6001f55060006fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6001f55060007fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff6001f500"  # noqa: E501
                    )
                )
            },
        ),
        (
            1000000,
            {
                Address("0x1000000000000000000000000000000000000000"): Account(
                    code=bytes.fromhex(
                        "7f6001600155601080600c6000396000f3006000355415600957005b602035600060005260356020536055602153600067ffffffffffffffff60006001f55060006fffffffffffffffffffffffffffffffff60006001f55060007fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff60006001f55060006000630fffffff6001f5506000600063ffffffff6001f5506000600067ffffffffffffffff6001f550600060006fffffffffffffffffffffffffffffffff6001f550600060007fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff6001f5506000630fffffff630fffffff6001f550600063ffffffff63ffffffff6001f550600067ffffffffffffffff67ffffffffffffffff6001f55060006fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6001f55060007fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff6001f500"  # noqa: E501
                    )
                )
            },
        ),
        (
            16777216,
            {
                Address("0x1000000000000000000000000000000000000000"): Account(
                    code=bytes.fromhex(
                        "7f6001600155601080600c6000396000f3006000355415600957005b602035600060005260356020536055602153600067ffffffffffffffff60006001f55060006fffffffffffffffffffffffffffffffff60006001f55060007fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff60006001f55060006000630fffffff6001f5506000600063ffffffff6001f5506000600067ffffffffffffffff6001f550600060006fffffffffffffffffffffffffffffffff6001f550600060007fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff6001f5506000630fffffff630fffffff6001f550600063ffffffff63ffffffff6001f550600067ffffffffffffffff67ffffffffffffffff6001f55060006fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6001f55060007fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff6001f500"  # noqa: E501
                    )
                )
            },
        ),
    ],
    ids=["case0", "case1", "case2"],
)
@pytest.mark.pre_alloc_mutable
def test_create2_bounds3(
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
            "60356020536055602153600067ffffffffffffffff60006001f55060006fffffffffffff"  # noqa: E501
            "ffffffffffffffffffff60006001f55060007fffffffffffffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffff60006001f55060006000630fffffff6001f5506000"  # noqa: E501
            "600063ffffffff6001f5506000600067ffffffffffffffff6001f550600060006fffffff"  # noqa: E501
            "ffffffffffffffffffffffffff6001f550600060007fffffffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffff6001f5506000630fffffff630fffffff6001"  # noqa: E501
            "f550600063ffffffff63ffffffff6001f550600067ffffffffffffffff67ffffffffffff"  # noqa: E501
            "ffff6001f55060006fffffffffffffffffffffffffffffffff6fffffffffffffffffffff"  # noqa: E501
            "ffffffffffff6001f55060007fffffffffffffffffffffffffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffff6001f500"
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
