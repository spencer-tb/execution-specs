"""
transaction calls A (CALL B(CALL C(RETURN) OOG) 'check buffers').

Ported from:
tests/static/state_tests/stReturnDataTest
returndatasize_after_oog_after_deeperFiller.json
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
        "tests/static/state_tests/stReturnDataTest/returndatasize_after_oog_after_deeperFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_returndatasize_after_oog_after_deeper(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Transaction calls A (CALL B(CALL C(RETURN) OOG) 'check buffers')."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x73470b0c32d3f7811258f2bf112aa71e17b115c6")
    contract = Address("0x58eaa3041ad52c24e38e485222953f1cc19c7484")
    callee = Address("0x8e0c75135225713d8c9acbb889abba5a5f598920")
    callee_1 = Address("0xbda572e15071b6ab42cfec01423f1fbb1de68703")
    callee_2 = Address("0xcb33b9a773995316746a40201081d054635d02da")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=111669149696,
    )

    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(
                key=0x2,
                value=Op.CALL(
                    gas=0x186A0,
                    address=0xCB33B9A773995316746A40201081D054635D02DA,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x20,
                ),
            )
            + Op.SSTORE(key=0x0, value=Op.RETURNDATASIZE)
            + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
            + Op.STOP
        ),
        storage={
            0x0: 0xFFFFFFFF,
            0x1: 0xFFFFFFFF,
            0x2: 0xFFFFFFFF,
        },
    )
    pre[sender] = Account(balance=0x100000000000, nonce=0)
    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.MSTORE(offset=0x0, value=0xFF)
            + Op.RETURN(offset=0x0, size=0x20)
            + Op.STOP
        ),
    )
    pre[callee_1] = Account(balance=0x1000000000, nonce=0)
    pre[callee_2] = Account(
        balance=0x6400000000,
        nonce=0,
        code=(
            Op.POP(
                Op.CALL(
                    gas=0x186A0,
                    address=0x8E0C75135225713D8C9ACBB889ABBA5A5F598920,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.JUMPDEST
            + Op.JUMPI(pc=0x34, condition=Op.ISZERO(0x1))
            + Op.SSTORE(key=0x0, value=0x1)
            + Op.JUMP(pc=0x25)
            + Op.JUMPDEST
            + Op.STOP
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0x987c63506890b18862bd2304513f21b726a7e35961c9214954326694141fdb46"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=200000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            code=(
                Op.SSTORE(
                    key=0x2,
                    value=Op.CALL(
                        gas=0x186A0,
                        address=0xCB33B9A773995316746A40201081D054635D02DA,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    ),
                )
                + Op.SSTORE(key=0x0, value=Op.RETURNDATASIZE)
                + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                + Op.STOP
            ),
        ),
        callee: Account(
            code=(
                Op.MSTORE(offset=0x0, value=0xFF)
                + Op.RETURN(offset=0x0, size=0x20)
                + Op.STOP
            ),
        ),
        callee_2: Account(
            code=(
                Op.POP(
                    Op.CALL(
                        gas=0x186A0,
                        address=0x8E0C75135225713D8C9ACBB889ABBA5A5F598920,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    ),
                )
                + Op.JUMPDEST
                + Op.JUMPI(pc=0x34, condition=Op.ISZERO(0x1))
                + Op.SSTORE(key=0x0, value=0x1)
                + Op.JUMP(pc=0x25)
                + Op.JUMPDEST
                + Op.STOP
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
