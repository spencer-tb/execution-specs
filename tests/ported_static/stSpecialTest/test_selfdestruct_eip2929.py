"""
Martin: @tkstanczak requested a state-test regarding selfdestructs in...

Ported from:
tests/static/state_tests/stSpecialTest/selfdestructEIP2929Filler.json
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
    ["tests/static/state_tests/stSpecialTest/selfdestructEIP2929Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_selfdestruct_eip2929(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Martin: @tkstanczak requested a state-test regarding..."""
    coinbase = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    sender = Address("0x2e3d0156d2b99a6eacba540c55f423c8f5a33143")
    contract = Address("0xb686be1a7a0f441fae9583884043ac034fe82089")
    callee = Address("0x7704d8a022a1ba8f3539fc82c7d7fb065abc0df3")
    callee_1 = Address("0x9ecbdbdbd8448cdd955755cdd81d6918e436f68a")
    callee_2 = Address("0xd2e5c26a2f035a63d0859e255621ed1e57148085")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10944489199640098,
    )

    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)
    pre[callee] = Account(balance=0, nonce=1)
    pre[callee_1] = Account(balance=0, nonce=1)
    # Source: raw bytecode
    pre[contract] = Account(
        balance=1,
        nonce=1,
        code=(
            Op.POP(
                Op.CALL(
                    gas=0x0,
                    address=0xCC,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.POP(
                Op.CALL(
                    gas=0x0,
                    address=0xDD,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.POP(
                Op.CALL(
                    gas=0x0,
                    address=0x3,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.MSTORE(offset=0x0, value=0xAA)
            + Op.POP(
                Op.CALL(
                    gas=Op.GAS,
                    address=0xDEAD,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x20,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.MSTORE(offset=0x0, value=0xAA)
            + Op.POP(
                Op.CALL(
                    gas=Op.GAS,
                    address=0xDEAD,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x20,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.MSTORE(offset=0x0, value=0xBB)
            + Op.POP(
                Op.CALL(
                    gas=Op.GAS,
                    address=0xDEAD,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x20,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.MSTORE(offset=0x0, value=0xBB)
            + Op.POP(
                Op.CALL(
                    gas=Op.GAS,
                    address=0xDEAD,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x20,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.MSTORE(offset=0x0, value=0xCC)
            + Op.POP(
                Op.CALL(
                    gas=Op.GAS,
                    address=0xDEAD,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x20,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.MSTORE(offset=0x0, value=0xCC)
            + Op.POP(
                Op.CALL(
                    gas=Op.GAS,
                    address=0xDEAD,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x20,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.MSTORE(offset=0x0, value=0xDD)
            + Op.POP(
                Op.CALL(
                    gas=Op.GAS,
                    address=0xDEAD,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x20,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.MSTORE(offset=0x0, value=0xDD)
            + Op.POP(
                Op.CALL(
                    gas=Op.GAS,
                    address=0xDEAD,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x20,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.MSTORE(offset=0x0, value=0x1)
            + Op.POP(
                Op.CALL(
                    gas=Op.GAS,
                    address=0xDEAD,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x20,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.MSTORE(offset=0x0, value=0x1)
            + Op.POP(
                Op.CALL(
                    gas=Op.GAS,
                    address=0xDEAD,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x20,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.MSTORE(offset=0x0, value=0x2)
            + Op.POP(
                Op.CALL(
                    gas=Op.GAS,
                    address=0xDEAD,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x20,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.MSTORE(offset=0x0, value=0x2)
            + Op.POP(
                Op.CALL(
                    gas=Op.GAS,
                    address=0xDEAD,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x20,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.MSTORE(offset=0x0, value=0x3)
            + Op.POP(
                Op.CALL(
                    gas=Op.GAS,
                    address=0xDEAD,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x20,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.SSTORE(key=0x1, value=0x1)
        ),
    )
    # Source: raw bytecode
    pre[callee_2] = Account(
        balance=1,
        nonce=1,
        code=(
            Op.SELFDESTRUCT(
                address=Op.AND(
                    0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                    Op.CALLDATALOAD(offset=0x0),
                ),
            )
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xb1f4cbc3a50042184425a6f9e996d0910f7ba879457ce5dac5c71e498ad3c005"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=8000000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            storage={1: 1},
            code=(
                Op.POP(
                    Op.CALL(
                        gas=0x0,
                        address=0xCC,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    ),
                )
                + Op.POP(
                    Op.CALL(
                        gas=0x0,
                        address=0xDD,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    ),
                )
                + Op.POP(
                    Op.CALL(
                        gas=0x0,
                        address=0x3,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    ),
                )
                + Op.MSTORE(offset=0x0, value=0xAA)
                + Op.POP(
                    Op.CALL(
                        gas=Op.GAS,
                        address=0xDEAD,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x20,
                        ret_offset=0x0,
                        ret_size=0x0,
                    ),
                )
                + Op.MSTORE(offset=0x0, value=0xAA)
                + Op.POP(
                    Op.CALL(
                        gas=Op.GAS,
                        address=0xDEAD,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x20,
                        ret_offset=0x0,
                        ret_size=0x0,
                    ),
                )
                + Op.MSTORE(offset=0x0, value=0xBB)
                + Op.POP(
                    Op.CALL(
                        gas=Op.GAS,
                        address=0xDEAD,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x20,
                        ret_offset=0x0,
                        ret_size=0x0,
                    ),
                )
                + Op.MSTORE(offset=0x0, value=0xBB)
                + Op.POP(
                    Op.CALL(
                        gas=Op.GAS,
                        address=0xDEAD,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x20,
                        ret_offset=0x0,
                        ret_size=0x0,
                    ),
                )
                + Op.MSTORE(offset=0x0, value=0xCC)
                + Op.POP(
                    Op.CALL(
                        gas=Op.GAS,
                        address=0xDEAD,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x20,
                        ret_offset=0x0,
                        ret_size=0x0,
                    ),
                )
                + Op.MSTORE(offset=0x0, value=0xCC)
                + Op.POP(
                    Op.CALL(
                        gas=Op.GAS,
                        address=0xDEAD,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x20,
                        ret_offset=0x0,
                        ret_size=0x0,
                    ),
                )
                + Op.MSTORE(offset=0x0, value=0xDD)
                + Op.POP(
                    Op.CALL(
                        gas=Op.GAS,
                        address=0xDEAD,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x20,
                        ret_offset=0x0,
                        ret_size=0x0,
                    ),
                )
                + Op.MSTORE(offset=0x0, value=0xDD)
                + Op.POP(
                    Op.CALL(
                        gas=Op.GAS,
                        address=0xDEAD,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x20,
                        ret_offset=0x0,
                        ret_size=0x0,
                    ),
                )
                + Op.MSTORE(offset=0x0, value=0x1)
                + Op.POP(
                    Op.CALL(
                        gas=Op.GAS,
                        address=0xDEAD,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x20,
                        ret_offset=0x0,
                        ret_size=0x0,
                    ),
                )
                + Op.MSTORE(offset=0x0, value=0x1)
                + Op.POP(
                    Op.CALL(
                        gas=Op.GAS,
                        address=0xDEAD,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x20,
                        ret_offset=0x0,
                        ret_size=0x0,
                    ),
                )
                + Op.MSTORE(offset=0x0, value=0x2)
                + Op.POP(
                    Op.CALL(
                        gas=Op.GAS,
                        address=0xDEAD,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x20,
                        ret_offset=0x0,
                        ret_size=0x0,
                    ),
                )
                + Op.MSTORE(offset=0x0, value=0x2)
                + Op.POP(
                    Op.CALL(
                        gas=Op.GAS,
                        address=0xDEAD,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x20,
                        ret_offset=0x0,
                        ret_size=0x0,
                    ),
                )
                + Op.MSTORE(offset=0x0, value=0x3)
                + Op.POP(
                    Op.CALL(
                        gas=Op.GAS,
                        address=0xDEAD,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x20,
                        ret_offset=0x0,
                        ret_size=0x0,
                    ),
                )
                + Op.SSTORE(key=0x1, value=0x1)
            ),
        ),
        callee_2: Account(
            code=(
                Op.SELFDESTRUCT(
                    address=Op.AND(
                        0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                        Op.CALLDATALOAD(offset=0x0),
                    ),
                )
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
