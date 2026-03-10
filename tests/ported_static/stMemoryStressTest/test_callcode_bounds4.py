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
from execution_testing.vm import Op

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
                    code=Op.SSTORE(
                        key=0x0, value=Op.ADD(0x1, Op.SLOAD(key=0x0))
                    )
                    + Op.STOP
                ),
                Address("0xc0479fbac15cb575e66ded014fd60ceb98749b04"): Account(
                    code=Op.POP(
                        Op.CALLCODE(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x849F53126ADE5F72469029537296F2B6644D4D41,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0xFFFFFFFFFFFFFFFF,
                            ret_offset=0x0,
                            ret_size=0xFFFFFFFFFFFFFFFF,
                        )
                    )
                    + Op.POP(
                        Op.CALLCODE(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x849F53126ADE5F72469029537296F2B6644D4D41,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                            ret_offset=0x0,
                            ret_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                        )
                    )
                    + Op.POP(
                        Op.CALLCODE(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x849F53126ADE5F72469029537296F2B6644D4D41,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            ret_offset=0x0,
                            ret_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                        )
                    )
                    + Op.POP(
                        Op.CALLCODE(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x849F53126ADE5F72469029537296F2B6644D4D41,
                            value=0x0,
                            args_offset=0xFFFFFFFFFFFFFFFF,
                            args_size=0xFFFFFFFFFFFFFFFF,
                            ret_offset=0xFFFFFFFFFFFFFFFF,
                            ret_size=0xFFFFFFFFFFFFFFFF,
                        )
                    )
                    + Op.POP(
                        Op.CALLCODE(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x849F53126ADE5F72469029537296F2B6644D4D41,
                            value=0x0,
                            args_offset=0xFFFFFFFFFFFFFFFF,
                            args_size=0xFFFFFFFFFFFFFFFF,
                            ret_offset=0xFFFFFFFFFFFFFFFF,
                            ret_size=0xFFFFFFFFFFFFFFFF,
                        )
                    )
                    + Op.POP(
                        Op.CALLCODE(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x849F53126ADE5F72469029537296F2B6644D4D41,
                            value=0x0,
                            args_offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            args_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            ret_offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            ret_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                        )
                    )
                    + Op.CALLCODE(
                        gas=0x7FFFFFFFFFFFFFF,
                        address=0x849F53126ADE5F72469029537296F2B6644D4D41,
                        value=0x0,
                        args_offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                        args_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                        ret_offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                        ret_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                    )
                    + Op.STOP
                ),
            },
        ),
        (
            1000000,
            {
                Address("0x849f53126ade5f72469029537296f2b6644d4d41"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.ADD(0x1, Op.SLOAD(key=0x0))
                    )
                    + Op.STOP
                ),
                Address("0xc0479fbac15cb575e66ded014fd60ceb98749b04"): Account(
                    code=Op.POP(
                        Op.CALLCODE(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x849F53126ADE5F72469029537296F2B6644D4D41,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0xFFFFFFFFFFFFFFFF,
                            ret_offset=0x0,
                            ret_size=0xFFFFFFFFFFFFFFFF,
                        )
                    )
                    + Op.POP(
                        Op.CALLCODE(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x849F53126ADE5F72469029537296F2B6644D4D41,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                            ret_offset=0x0,
                            ret_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                        )
                    )
                    + Op.POP(
                        Op.CALLCODE(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x849F53126ADE5F72469029537296F2B6644D4D41,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            ret_offset=0x0,
                            ret_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                        )
                    )
                    + Op.POP(
                        Op.CALLCODE(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x849F53126ADE5F72469029537296F2B6644D4D41,
                            value=0x0,
                            args_offset=0xFFFFFFFFFFFFFFFF,
                            args_size=0xFFFFFFFFFFFFFFFF,
                            ret_offset=0xFFFFFFFFFFFFFFFF,
                            ret_size=0xFFFFFFFFFFFFFFFF,
                        )
                    )
                    + Op.POP(
                        Op.CALLCODE(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x849F53126ADE5F72469029537296F2B6644D4D41,
                            value=0x0,
                            args_offset=0xFFFFFFFFFFFFFFFF,
                            args_size=0xFFFFFFFFFFFFFFFF,
                            ret_offset=0xFFFFFFFFFFFFFFFF,
                            ret_size=0xFFFFFFFFFFFFFFFF,
                        )
                    )
                    + Op.POP(
                        Op.CALLCODE(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x849F53126ADE5F72469029537296F2B6644D4D41,
                            value=0x0,
                            args_offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            args_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            ret_offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            ret_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                        )
                    )
                    + Op.CALLCODE(
                        gas=0x7FFFFFFFFFFFFFF,
                        address=0x849F53126ADE5F72469029537296F2B6644D4D41,
                        value=0x0,
                        args_offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                        args_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                        ret_offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                        ret_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                    )
                    + Op.STOP
                ),
            },
        ),
        (
            16777216,
            {
                Address("0x849f53126ade5f72469029537296f2b6644d4d41"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.ADD(0x1, Op.SLOAD(key=0x0))
                    )
                    + Op.STOP
                ),
                Address("0xc0479fbac15cb575e66ded014fd60ceb98749b04"): Account(
                    code=Op.POP(
                        Op.CALLCODE(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x849F53126ADE5F72469029537296F2B6644D4D41,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0xFFFFFFFFFFFFFFFF,
                            ret_offset=0x0,
                            ret_size=0xFFFFFFFFFFFFFFFF,
                        )
                    )
                    + Op.POP(
                        Op.CALLCODE(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x849F53126ADE5F72469029537296F2B6644D4D41,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                            ret_offset=0x0,
                            ret_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                        )
                    )
                    + Op.POP(
                        Op.CALLCODE(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x849F53126ADE5F72469029537296F2B6644D4D41,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            ret_offset=0x0,
                            ret_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                        )
                    )
                    + Op.POP(
                        Op.CALLCODE(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x849F53126ADE5F72469029537296F2B6644D4D41,
                            value=0x0,
                            args_offset=0xFFFFFFFFFFFFFFFF,
                            args_size=0xFFFFFFFFFFFFFFFF,
                            ret_offset=0xFFFFFFFFFFFFFFFF,
                            ret_size=0xFFFFFFFFFFFFFFFF,
                        )
                    )
                    + Op.POP(
                        Op.CALLCODE(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x849F53126ADE5F72469029537296F2B6644D4D41,
                            value=0x0,
                            args_offset=0xFFFFFFFFFFFFFFFF,
                            args_size=0xFFFFFFFFFFFFFFFF,
                            ret_offset=0xFFFFFFFFFFFFFFFF,
                            ret_size=0xFFFFFFFFFFFFFFFF,
                        )
                    )
                    + Op.POP(
                        Op.CALLCODE(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x849F53126ADE5F72469029537296F2B6644D4D41,
                            value=0x0,
                            args_offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            args_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            ret_offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            ret_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                        )
                    )
                    + Op.CALLCODE(
                        gas=0x7FFFFFFFFFFFFFF,
                        address=0x849F53126ADE5F72469029537296F2B6644D4D41,
                        value=0x0,
                        args_offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                        args_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                        ret_offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                        ret_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                    )
                    + Op.STOP
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
        code=(
            Op.SSTORE(key=0x0, value=Op.ADD(0x1, Op.SLOAD(key=0x0))) + Op.STOP
        ),
    )
    pre[sender] = Account(
        balance=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
        nonce=0,
    )
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.POP(
                Op.CALLCODE(
                    gas=0x7FFFFFFFFFFFFFF,
                    address=0x849F53126ADE5F72469029537296F2B6644D4D41,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0xFFFFFFFFFFFFFFFF,
                    ret_offset=0x0,
                    ret_size=0xFFFFFFFFFFFFFFFF,
                ),
            )
            + Op.POP(
                Op.CALLCODE(
                    gas=0x7FFFFFFFFFFFFFF,
                    address=0x849F53126ADE5F72469029537296F2B6644D4D41,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                    ret_offset=0x0,
                    ret_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                ),
            )
            + Op.POP(
                Op.CALLCODE(
                    gas=0x7FFFFFFFFFFFFFF,
                    address=0x849F53126ADE5F72469029537296F2B6644D4D41,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                    ret_offset=0x0,
                    ret_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                ),
            )
            + Op.POP(
                Op.CALLCODE(
                    gas=0x7FFFFFFFFFFFFFF,
                    address=0x849F53126ADE5F72469029537296F2B6644D4D41,
                    value=0x0,
                    args_offset=0xFFFFFFFFFFFFFFFF,
                    args_size=0xFFFFFFFFFFFFFFFF,
                    ret_offset=0xFFFFFFFFFFFFFFFF,
                    ret_size=0xFFFFFFFFFFFFFFFF,
                ),
            )
            + Op.POP(
                Op.CALLCODE(
                    gas=0x7FFFFFFFFFFFFFF,
                    address=0x849F53126ADE5F72469029537296F2B6644D4D41,
                    value=0x0,
                    args_offset=0xFFFFFFFFFFFFFFFF,
                    args_size=0xFFFFFFFFFFFFFFFF,
                    ret_offset=0xFFFFFFFFFFFFFFFF,
                    ret_size=0xFFFFFFFFFFFFFFFF,
                ),
            )
            + Op.POP(
                Op.CALLCODE(
                    gas=0x7FFFFFFFFFFFFFF,
                    address=0x849F53126ADE5F72469029537296F2B6644D4D41,
                    value=0x0,
                    args_offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                    args_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                    ret_offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                    ret_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                ),
            )
            + Op.CALLCODE(
                gas=0x7FFFFFFFFFFFFFF,
                address=0x849F53126ADE5F72469029537296F2B6644D4D41,
                value=0x0,
                args_offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                args_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                ret_offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                ret_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
            )
            + Op.STOP
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
