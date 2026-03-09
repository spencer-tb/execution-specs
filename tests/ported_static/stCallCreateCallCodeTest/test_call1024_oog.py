"""
calldepth with oog

Ported from:
tests/static/state_tests/stCallCreateCallCodeTest/Call1024OOGFiller.json
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
    ["tests/static/state_tests/stCallCreateCallCodeTest/Call1024OOGFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit, expected_post",
    [
        (13120826, {Address("0x0878bc1c3d660907b056e31c854a309f7ef1b4c4"): Account(storage={0: 134, 1: 1, 2: 0x20b71}, code=Op.SSTORE(key=0x0, value=Op.ADD(Op.SLOAD(key=0x0), 0x1)) + Op.SSTORE(key=0x1, value=Op.CALL(gas=Op.MUL(Op.SUB(Op.GAS, 0x2710), Op.SUB(0x1, Op.DIV(Op.SLOAD(key=0x0), 0x401))), address=0x878bc1c3d660907b056e31c854a309f7ef1b4c4, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x2, value=Op.ADD(0x1, Op.MUL(Op.SLOAD(key=0x0), 0x3e8))) + Op.STOP)}),
        (9320826, {Address("0x0878bc1c3d660907b056e31c854a309f7ef1b4c4"): Account(storage={0: 113, 1: 1, 2: 0x1b969}, code=Op.SSTORE(key=0x0, value=Op.ADD(Op.SLOAD(key=0x0), 0x1)) + Op.SSTORE(key=0x1, value=Op.CALL(gas=Op.MUL(Op.SUB(Op.GAS, 0x2710), Op.SUB(0x1, Op.DIV(Op.SLOAD(key=0x0), 0x401))), address=0x878bc1c3d660907b056e31c854a309f7ef1b4c4, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x2, value=Op.ADD(0x1, Op.MUL(Op.SLOAD(key=0x0), 0x3e8))) + Op.STOP)}),
        (15720826, {Address("0x0878bc1c3d660907b056e31c854a309f7ef1b4c4"): Account(storage={0: 146, 1: 1, 2: 0x23a51}, code=Op.SSTORE(key=0x0, value=Op.ADD(Op.SLOAD(key=0x0), 0x1)) + Op.SSTORE(key=0x1, value=Op.CALL(gas=Op.MUL(Op.SUB(Op.GAS, 0x2710), Op.SUB(0x1, Op.DIV(Op.SLOAD(key=0x0), 0x401))), address=0x878bc1c3d660907b056e31c854a309f7ef1b4c4, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x2, value=Op.ADD(0x1, Op.MUL(Op.SLOAD(key=0x0), 0x3e8))) + Op.STOP)}),
        (11220826, {Address("0x0878bc1c3d660907b056e31c854a309f7ef1b4c4"): Account(storage={0: 124, 1: 1, 2: 0x1e461}, code=Op.SSTORE(key=0x0, value=Op.ADD(Op.SLOAD(key=0x0), 0x1)) + Op.SSTORE(key=0x1, value=Op.CALL(gas=Op.MUL(Op.SUB(Op.GAS, 0x2710), Op.SUB(0x1, Op.DIV(Op.SLOAD(key=0x0), 0x401))), address=0x878bc1c3d660907b056e31c854a309f7ef1b4c4, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x2, value=Op.ADD(0x1, Op.MUL(Op.SLOAD(key=0x0), 0x3e8))) + Op.STOP)}),
    ],
    ids=['case0', 'case1', 'case2', 'case3'],
)
@pytest.mark.pre_alloc_mutable
def test_call1024_oog(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
    expected_post: dict,
) -> None:
    """calldepth with oog."""
    coinbase = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    sender = Address("0x4768b5e50b0ebe91ae38d84a47e3179e615f9c40")
    contract = Address("0x0878bc1c3d660907b056e31c854a309f7ef1b4c4")
    callee = Address("0xd9b97c712ebce43f3c19179bbef44b550f9e8bc0")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[contract] = Account(
        balance=1024,
        nonce=0,
        code=(
        Op.SSTORE(key=0x0, value=Op.ADD(Op.SLOAD(key=0x0), 0x1))
        + Op.SSTORE(key=0x1, value=Op.CALL(gas=Op.MUL(Op.SUB(Op.GAS, 0x2710), Op.SUB(0x1, Op.DIV(Op.SLOAD(key=0x0), 0x401))), address=0x878bc1c3d660907b056e31c854a309f7ef1b4c4, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.SSTORE(key=0x2, value=Op.ADD(0x1, Op.MUL(Op.SLOAD(key=0x0), 0x3e8)))
        + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0xffffffffffffffffffffffffffffffff, nonce=0)
    pre[callee] = Account(balance=7000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xe7c72b378297589acee4e0ba3272841bcfc5e220f86de253f890274cfee9e474"
        ),
        to=contract,
        data=b"",
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=10,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
