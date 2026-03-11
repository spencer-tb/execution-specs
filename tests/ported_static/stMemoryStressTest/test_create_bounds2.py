"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stMemoryStressTest/CREATE_Bounds2Filler.json
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
    ["tests/static/state_tests/stMemoryStressTest/CREATE_Bounds2Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit, expected_post",
    [
        (
            150000,
            {
                Address("0x1000000000000000000000000000000000000000"): Account(
                    code=Op.MSTORE(
                        offset=0x0,
                        value=0x6001600155601080600C6000396000F3006000355415600957005B6020356000,  # noqa: E501
                    )
                    + Op.MSTORE8(offset=0x20, value=0x35)
                    + Op.MSTORE8(offset=0x21, value=0x55)
                    + Op.CREATE(value=0x1, offset=0x0, size=0xFFFFFFFF)
                    + Op.STOP
                )
            },
        ),
        (
            16777216,
            {
                Address("0x1000000000000000000000000000000000000000"): Account(
                    code=Op.MSTORE(
                        offset=0x0,
                        value=0x6001600155601080600C6000396000F3006000355415600957005B6020356000,  # noqa: E501
                    )
                    + Op.MSTORE8(offset=0x20, value=0x35)
                    + Op.MSTORE8(offset=0x21, value=0x55)
                    + Op.CREATE(value=0x1, offset=0x0, size=0xFFFFFFFF)
                    + Op.STOP
                )
            },
        ),
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_create_bounds2(
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

    # Source: LLL
    # {  (MSTORE 0 0x6001600155601080600c6000396000f3006000355415600957005b6020356000 )  (MSTORE8 32 0x35) (MSTORE8 33 0x55) (CREATE 1 0 0xffffffff) }  # noqa: E501
    pre[contract] = Account(
        balance=100,
        nonce=0,
        code=(
            Op.MSTORE(
                offset=0x0,
                value=0x6001600155601080600C6000396000F3006000355415600957005B6020356000,  # noqa: E501
            )
            + Op.MSTORE8(offset=0x20, value=0x35)
            + Op.MSTORE8(offset=0x21, value=0x55)
            + Op.CREATE(value=0x1, offset=0x0, size=0xFFFFFFFF)
            + Op.STOP
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
