"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stMemoryStressTest/CALL_Bounds2aFiller.json
"""

import pytest
from execution_testing import (
    Account,
    Address,
    Alloc,
    EOA,
    Environment,
    Hash,
    StateTestFiller,
    Transaction,
)
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


@pytest.mark.ported_from(
    ["tests/static/state_tests/stMemoryStressTest/CALL_Bounds2aFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit, expected_post",
    [
        (
            150000,
            {
                Address("0x6c184e7e792470e474b189a511b48f06f0643d4b"): Account(
                    code=Op.CALL(
                        gas=0x7FFFFFFFFFFFFFF,
                        address=0x849F53126ADE5F72469029537296F2B6644D4D41,
                        value=0x0,
                        args_offset=0xFFFFFFFF,
                        args_size=0xFFFFFFFF,
                        ret_offset=0xFFFFFFFF,
                        ret_size=0xFFFFFFFF,
                    )
                    + Op.STOP
                ),
                Address("0x849f53126ade5f72469029537296f2b6644d4d41"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.ADD(0x1, Op.SLOAD(key=0x0))
                    )
                    + Op.STOP
                ),
            },
        ),
        (
            16777216,
            {
                Address("0x6c184e7e792470e474b189a511b48f06f0643d4b"): Account(
                    code=Op.CALL(
                        gas=0x7FFFFFFFFFFFFFF,
                        address=0x849F53126ADE5F72469029537296F2B6644D4D41,
                        value=0x0,
                        args_offset=0xFFFFFFFF,
                        args_size=0xFFFFFFFF,
                        ret_offset=0xFFFFFFFF,
                        ret_size=0xFFFFFFFF,
                    )
                    + Op.STOP
                ),
                Address("0x849f53126ade5f72469029537296f2b6644d4d41"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.ADD(0x1, Op.SLOAD(key=0x0))
                    )
                    + Op.STOP
                ),
            },
        ),
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_call_bounds2a(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = EOA(
        key=0xEF111BBDAB3A1622936AFDFC9BBEC4B5BC05B4FA4B1EF0CE2A55CEF552F7650E
    )
    contract = Address("0x6c184e7e792470e474b189a511b48f06f0643d4b")
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
    # Source: LLL
    # {   (CALL 0x7ffffffffffffff <contract:0x1000000000000000000000000000000000000001> 0 0xffffffff 0xffffffff 0xffffffff 0xffffffff)  }  # noqa: E501
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.CALL(
                gas=0x7FFFFFFFFFFFFFF,
                address=0x849F53126ADE5F72469029537296F2B6644D4D41,
                value=0x0,
                args_offset=0xFFFFFFFF,
                args_size=0xFFFFFFFF,
                ret_offset=0xFFFFFFFF,
                ret_size=0xFFFFFFFF,
            )
            + Op.STOP
        ),
    )
    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=Op.ADD(0x1, Op.SLOAD(key=0x0))) + Op.STOP
        ),
    )

    tx = Transaction(
        sender=sender,
        to=contract,
        data=b"",
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
