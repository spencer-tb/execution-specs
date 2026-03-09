"""
The first test case required here 
https://github.com/ethereum/tests/issues/431#issue-306081539

Implements: SUC007.0, SUC007.1, SUC007.2, SUC007.3,
            SUC008.0, SUC008.1, SUC008.2, SUC008.3


Ported from:
tests/static/state_tests/stSystemOperationsTest/doubleSelfdestructTestFiller.yml
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
    ["tests/static/state_tests/stSystemOperationsTest/doubleSelfdestructTestFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        ("f210011002", {Address("0x000000000000000000000000000000000000c0de"): Account(code=Op.JUMPI(pc=0x17, condition=Op.GT(Op.CALLDATASIZE, 0x2)) + Op.SHR(0xf0, Op.CALLDATALOAD(offset=0x0)) + Op.JUMPI(pc=0x15, condition=Op.EQ(0x2, Op.CALLDATASIZE)) + Op.STOP + Op.JUMPDEST + Op.SELFDESTRUCT + Op.JUMPDEST + Op.SHR(0xf8, Op.CALLDATALOAD(offset=0x0)) + Op.PUSH1[0xfa] + Op.AND(Op.SHR(0xe8, Op.CALLDATALOAD(offset=0x0)), 0xffff) + Op.SWAP2 + Op.PUSH1[0xff] + Op.AND(Op.SHR(0xd8, Op.CALLDATALOAD(offset=0x0)), 0xffff) + Op.MSTORE8(offset=0x0, value=Op.AND(Op.SHR(0x8, Op.DUP2), Op.DUP2)) + Op.MSTORE8(offset=0x1, value=Op.AND) + Op.JUMPI(pc=0x90, condition=Op.EQ(Op.DUP2, 0xf1)) + Op.JUMPDEST + Op.JUMPI(pc=0x7f, condition=Op.EQ(Op.DUP2, 0xf2)) + Op.JUMPDEST + Op.JUMPI(pc=0x6f, condition=Op.EQ(Op.DUP2, 0xf4)) + Op.JUMPDEST + Op.JUMPI(pc=0x61, condition=Op.EQ) + Op.SELFDESTRUCT + Op.JUMPDEST + Op.POP(Op.STATICCALL(gas=Op.GAS, address=0xc0de, args_offset=Op.DUP2, args_size=0x2, ret_offset=Op.DUP1, ret_size=0x0)) + Op.SELFDESTRUCT + Op.JUMPDEST + Op.POP(Op.DELEGATECALL(gas=Op.GAS, address=0xc0de, args_offset=Op.DUP2, args_size=0x2, ret_offset=Op.DUP1, ret_size=0x0)) + Op.JUMP(pc=0x5b) + Op.JUMPDEST + Op.POP(Op.CALLCODE(gas=Op.GAS, address=0xc0de, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x2, ret_offset=Op.DUP1, ret_size=0x0)) + Op.JUMP(pc=0x53) + Op.JUMPDEST + Op.POP(Op.CALL(gas=Op.GAS, address=0xc0de, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x2, ret_offset=Op.DUP1, ret_size=0x0)) + Op.JUMP(pc=0x4b))}),
        ("f410011002", {Address("0x000000000000000000000000000000000000c0de"): Account(code=Op.JUMPI(pc=0x17, condition=Op.GT(Op.CALLDATASIZE, 0x2)) + Op.SHR(0xf0, Op.CALLDATALOAD(offset=0x0)) + Op.JUMPI(pc=0x15, condition=Op.EQ(0x2, Op.CALLDATASIZE)) + Op.STOP + Op.JUMPDEST + Op.SELFDESTRUCT + Op.JUMPDEST + Op.SHR(0xf8, Op.CALLDATALOAD(offset=0x0)) + Op.PUSH1[0xfa] + Op.AND(Op.SHR(0xe8, Op.CALLDATALOAD(offset=0x0)), 0xffff) + Op.SWAP2 + Op.PUSH1[0xff] + Op.AND(Op.SHR(0xd8, Op.CALLDATALOAD(offset=0x0)), 0xffff) + Op.MSTORE8(offset=0x0, value=Op.AND(Op.SHR(0x8, Op.DUP2), Op.DUP2)) + Op.MSTORE8(offset=0x1, value=Op.AND) + Op.JUMPI(pc=0x90, condition=Op.EQ(Op.DUP2, 0xf1)) + Op.JUMPDEST + Op.JUMPI(pc=0x7f, condition=Op.EQ(Op.DUP2, 0xf2)) + Op.JUMPDEST + Op.JUMPI(pc=0x6f, condition=Op.EQ(Op.DUP2, 0xf4)) + Op.JUMPDEST + Op.JUMPI(pc=0x61, condition=Op.EQ) + Op.SELFDESTRUCT + Op.JUMPDEST + Op.POP(Op.STATICCALL(gas=Op.GAS, address=0xc0de, args_offset=Op.DUP2, args_size=0x2, ret_offset=Op.DUP1, ret_size=0x0)) + Op.SELFDESTRUCT + Op.JUMPDEST + Op.POP(Op.DELEGATECALL(gas=Op.GAS, address=0xc0de, args_offset=Op.DUP2, args_size=0x2, ret_offset=Op.DUP1, ret_size=0x0)) + Op.JUMP(pc=0x5b) + Op.JUMPDEST + Op.POP(Op.CALLCODE(gas=Op.GAS, address=0xc0de, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x2, ret_offset=Op.DUP1, ret_size=0x0)) + Op.JUMP(pc=0x53) + Op.JUMPDEST + Op.POP(Op.CALL(gas=Op.GAS, address=0xc0de, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x2, ret_offset=Op.DUP1, ret_size=0x0)) + Op.JUMP(pc=0x4b))}),
        ("f110011002", {Address("0x000000000000000000000000000000000000c0de"): Account(code=Op.JUMPI(pc=0x17, condition=Op.GT(Op.CALLDATASIZE, 0x2)) + Op.SHR(0xf0, Op.CALLDATALOAD(offset=0x0)) + Op.JUMPI(pc=0x15, condition=Op.EQ(0x2, Op.CALLDATASIZE)) + Op.STOP + Op.JUMPDEST + Op.SELFDESTRUCT + Op.JUMPDEST + Op.SHR(0xf8, Op.CALLDATALOAD(offset=0x0)) + Op.PUSH1[0xfa] + Op.AND(Op.SHR(0xe8, Op.CALLDATALOAD(offset=0x0)), 0xffff) + Op.SWAP2 + Op.PUSH1[0xff] + Op.AND(Op.SHR(0xd8, Op.CALLDATALOAD(offset=0x0)), 0xffff) + Op.MSTORE8(offset=0x0, value=Op.AND(Op.SHR(0x8, Op.DUP2), Op.DUP2)) + Op.MSTORE8(offset=0x1, value=Op.AND) + Op.JUMPI(pc=0x90, condition=Op.EQ(Op.DUP2, 0xf1)) + Op.JUMPDEST + Op.JUMPI(pc=0x7f, condition=Op.EQ(Op.DUP2, 0xf2)) + Op.JUMPDEST + Op.JUMPI(pc=0x6f, condition=Op.EQ(Op.DUP2, 0xf4)) + Op.JUMPDEST + Op.JUMPI(pc=0x61, condition=Op.EQ) + Op.SELFDESTRUCT + Op.JUMPDEST + Op.POP(Op.STATICCALL(gas=Op.GAS, address=0xc0de, args_offset=Op.DUP2, args_size=0x2, ret_offset=Op.DUP1, ret_size=0x0)) + Op.SELFDESTRUCT + Op.JUMPDEST + Op.POP(Op.DELEGATECALL(gas=Op.GAS, address=0xc0de, args_offset=Op.DUP2, args_size=0x2, ret_offset=Op.DUP1, ret_size=0x0)) + Op.JUMP(pc=0x5b) + Op.JUMPDEST + Op.POP(Op.CALLCODE(gas=Op.GAS, address=0xc0de, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x2, ret_offset=Op.DUP1, ret_size=0x0)) + Op.JUMP(pc=0x53) + Op.JUMPDEST + Op.POP(Op.CALL(gas=Op.GAS, address=0xc0de, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x2, ret_offset=Op.DUP1, ret_size=0x0)) + Op.JUMP(pc=0x4b))}),
        ("fa1001c0de", {Address("0x000000000000000000000000000000000000c0de"): Account(code=Op.JUMPI(pc=0x17, condition=Op.GT(Op.CALLDATASIZE, 0x2)) + Op.SHR(0xf0, Op.CALLDATALOAD(offset=0x0)) + Op.JUMPI(pc=0x15, condition=Op.EQ(0x2, Op.CALLDATASIZE)) + Op.STOP + Op.JUMPDEST + Op.SELFDESTRUCT + Op.JUMPDEST + Op.SHR(0xf8, Op.CALLDATALOAD(offset=0x0)) + Op.PUSH1[0xfa] + Op.AND(Op.SHR(0xe8, Op.CALLDATALOAD(offset=0x0)), 0xffff) + Op.SWAP2 + Op.PUSH1[0xff] + Op.AND(Op.SHR(0xd8, Op.CALLDATALOAD(offset=0x0)), 0xffff) + Op.MSTORE8(offset=0x0, value=Op.AND(Op.SHR(0x8, Op.DUP2), Op.DUP2)) + Op.MSTORE8(offset=0x1, value=Op.AND) + Op.JUMPI(pc=0x90, condition=Op.EQ(Op.DUP2, 0xf1)) + Op.JUMPDEST + Op.JUMPI(pc=0x7f, condition=Op.EQ(Op.DUP2, 0xf2)) + Op.JUMPDEST + Op.JUMPI(pc=0x6f, condition=Op.EQ(Op.DUP2, 0xf4)) + Op.JUMPDEST + Op.JUMPI(pc=0x61, condition=Op.EQ) + Op.SELFDESTRUCT + Op.JUMPDEST + Op.POP(Op.STATICCALL(gas=Op.GAS, address=0xc0de, args_offset=Op.DUP2, args_size=0x2, ret_offset=Op.DUP1, ret_size=0x0)) + Op.SELFDESTRUCT + Op.JUMPDEST + Op.POP(Op.DELEGATECALL(gas=Op.GAS, address=0xc0de, args_offset=Op.DUP2, args_size=0x2, ret_offset=Op.DUP1, ret_size=0x0)) + Op.JUMP(pc=0x5b) + Op.JUMPDEST + Op.POP(Op.CALLCODE(gas=Op.GAS, address=0xc0de, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x2, ret_offset=Op.DUP1, ret_size=0x0)) + Op.JUMP(pc=0x53) + Op.JUMPDEST + Op.POP(Op.CALL(gas=Op.GAS, address=0xc0de, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x2, ret_offset=Op.DUP1, ret_size=0x0)) + Op.JUMP(pc=0x4b))}),
        ("fa10011002", {Address("0x000000000000000000000000000000000000c0de"): Account(code=Op.JUMPI(pc=0x17, condition=Op.GT(Op.CALLDATASIZE, 0x2)) + Op.SHR(0xf0, Op.CALLDATALOAD(offset=0x0)) + Op.JUMPI(pc=0x15, condition=Op.EQ(0x2, Op.CALLDATASIZE)) + Op.STOP + Op.JUMPDEST + Op.SELFDESTRUCT + Op.JUMPDEST + Op.SHR(0xf8, Op.CALLDATALOAD(offset=0x0)) + Op.PUSH1[0xfa] + Op.AND(Op.SHR(0xe8, Op.CALLDATALOAD(offset=0x0)), 0xffff) + Op.SWAP2 + Op.PUSH1[0xff] + Op.AND(Op.SHR(0xd8, Op.CALLDATALOAD(offset=0x0)), 0xffff) + Op.MSTORE8(offset=0x0, value=Op.AND(Op.SHR(0x8, Op.DUP2), Op.DUP2)) + Op.MSTORE8(offset=0x1, value=Op.AND) + Op.JUMPI(pc=0x90, condition=Op.EQ(Op.DUP2, 0xf1)) + Op.JUMPDEST + Op.JUMPI(pc=0x7f, condition=Op.EQ(Op.DUP2, 0xf2)) + Op.JUMPDEST + Op.JUMPI(pc=0x6f, condition=Op.EQ(Op.DUP2, 0xf4)) + Op.JUMPDEST + Op.JUMPI(pc=0x61, condition=Op.EQ) + Op.SELFDESTRUCT + Op.JUMPDEST + Op.POP(Op.STATICCALL(gas=Op.GAS, address=0xc0de, args_offset=Op.DUP2, args_size=0x2, ret_offset=Op.DUP1, ret_size=0x0)) + Op.SELFDESTRUCT + Op.JUMPDEST + Op.POP(Op.DELEGATECALL(gas=Op.GAS, address=0xc0de, args_offset=Op.DUP2, args_size=0x2, ret_offset=Op.DUP1, ret_size=0x0)) + Op.JUMP(pc=0x5b) + Op.JUMPDEST + Op.POP(Op.CALLCODE(gas=Op.GAS, address=0xc0de, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x2, ret_offset=Op.DUP1, ret_size=0x0)) + Op.JUMP(pc=0x53) + Op.JUMPDEST + Op.POP(Op.CALL(gas=Op.GAS, address=0xc0de, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x2, ret_offset=Op.DUP1, ret_size=0x0)) + Op.JUMP(pc=0x4b))}),
        ("f21001c0de", {Address("0x000000000000000000000000000000000000c0de"): Account(code=Op.JUMPI(pc=0x17, condition=Op.GT(Op.CALLDATASIZE, 0x2)) + Op.SHR(0xf0, Op.CALLDATALOAD(offset=0x0)) + Op.JUMPI(pc=0x15, condition=Op.EQ(0x2, Op.CALLDATASIZE)) + Op.STOP + Op.JUMPDEST + Op.SELFDESTRUCT + Op.JUMPDEST + Op.SHR(0xf8, Op.CALLDATALOAD(offset=0x0)) + Op.PUSH1[0xfa] + Op.AND(Op.SHR(0xe8, Op.CALLDATALOAD(offset=0x0)), 0xffff) + Op.SWAP2 + Op.PUSH1[0xff] + Op.AND(Op.SHR(0xd8, Op.CALLDATALOAD(offset=0x0)), 0xffff) + Op.MSTORE8(offset=0x0, value=Op.AND(Op.SHR(0x8, Op.DUP2), Op.DUP2)) + Op.MSTORE8(offset=0x1, value=Op.AND) + Op.JUMPI(pc=0x90, condition=Op.EQ(Op.DUP2, 0xf1)) + Op.JUMPDEST + Op.JUMPI(pc=0x7f, condition=Op.EQ(Op.DUP2, 0xf2)) + Op.JUMPDEST + Op.JUMPI(pc=0x6f, condition=Op.EQ(Op.DUP2, 0xf4)) + Op.JUMPDEST + Op.JUMPI(pc=0x61, condition=Op.EQ) + Op.SELFDESTRUCT + Op.JUMPDEST + Op.POP(Op.STATICCALL(gas=Op.GAS, address=0xc0de, args_offset=Op.DUP2, args_size=0x2, ret_offset=Op.DUP1, ret_size=0x0)) + Op.SELFDESTRUCT + Op.JUMPDEST + Op.POP(Op.DELEGATECALL(gas=Op.GAS, address=0xc0de, args_offset=Op.DUP2, args_size=0x2, ret_offset=Op.DUP1, ret_size=0x0)) + Op.JUMP(pc=0x5b) + Op.JUMPDEST + Op.POP(Op.CALLCODE(gas=Op.GAS, address=0xc0de, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x2, ret_offset=Op.DUP1, ret_size=0x0)) + Op.JUMP(pc=0x53) + Op.JUMPDEST + Op.POP(Op.CALL(gas=Op.GAS, address=0xc0de, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x2, ret_offset=Op.DUP1, ret_size=0x0)) + Op.JUMP(pc=0x4b))}),
        ("f41001c0de", {Address("0x000000000000000000000000000000000000c0de"): Account(code=Op.JUMPI(pc=0x17, condition=Op.GT(Op.CALLDATASIZE, 0x2)) + Op.SHR(0xf0, Op.CALLDATALOAD(offset=0x0)) + Op.JUMPI(pc=0x15, condition=Op.EQ(0x2, Op.CALLDATASIZE)) + Op.STOP + Op.JUMPDEST + Op.SELFDESTRUCT + Op.JUMPDEST + Op.SHR(0xf8, Op.CALLDATALOAD(offset=0x0)) + Op.PUSH1[0xfa] + Op.AND(Op.SHR(0xe8, Op.CALLDATALOAD(offset=0x0)), 0xffff) + Op.SWAP2 + Op.PUSH1[0xff] + Op.AND(Op.SHR(0xd8, Op.CALLDATALOAD(offset=0x0)), 0xffff) + Op.MSTORE8(offset=0x0, value=Op.AND(Op.SHR(0x8, Op.DUP2), Op.DUP2)) + Op.MSTORE8(offset=0x1, value=Op.AND) + Op.JUMPI(pc=0x90, condition=Op.EQ(Op.DUP2, 0xf1)) + Op.JUMPDEST + Op.JUMPI(pc=0x7f, condition=Op.EQ(Op.DUP2, 0xf2)) + Op.JUMPDEST + Op.JUMPI(pc=0x6f, condition=Op.EQ(Op.DUP2, 0xf4)) + Op.JUMPDEST + Op.JUMPI(pc=0x61, condition=Op.EQ) + Op.SELFDESTRUCT + Op.JUMPDEST + Op.POP(Op.STATICCALL(gas=Op.GAS, address=0xc0de, args_offset=Op.DUP2, args_size=0x2, ret_offset=Op.DUP1, ret_size=0x0)) + Op.SELFDESTRUCT + Op.JUMPDEST + Op.POP(Op.DELEGATECALL(gas=Op.GAS, address=0xc0de, args_offset=Op.DUP2, args_size=0x2, ret_offset=Op.DUP1, ret_size=0x0)) + Op.JUMP(pc=0x5b) + Op.JUMPDEST + Op.POP(Op.CALLCODE(gas=Op.GAS, address=0xc0de, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x2, ret_offset=Op.DUP1, ret_size=0x0)) + Op.JUMP(pc=0x53) + Op.JUMPDEST + Op.POP(Op.CALL(gas=Op.GAS, address=0xc0de, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x2, ret_offset=Op.DUP1, ret_size=0x0)) + Op.JUMP(pc=0x4b))}),
        ("f11001c0de", {Address("0x000000000000000000000000000000000000c0de"): Account(code=Op.JUMPI(pc=0x17, condition=Op.GT(Op.CALLDATASIZE, 0x2)) + Op.SHR(0xf0, Op.CALLDATALOAD(offset=0x0)) + Op.JUMPI(pc=0x15, condition=Op.EQ(0x2, Op.CALLDATASIZE)) + Op.STOP + Op.JUMPDEST + Op.SELFDESTRUCT + Op.JUMPDEST + Op.SHR(0xf8, Op.CALLDATALOAD(offset=0x0)) + Op.PUSH1[0xfa] + Op.AND(Op.SHR(0xe8, Op.CALLDATALOAD(offset=0x0)), 0xffff) + Op.SWAP2 + Op.PUSH1[0xff] + Op.AND(Op.SHR(0xd8, Op.CALLDATALOAD(offset=0x0)), 0xffff) + Op.MSTORE8(offset=0x0, value=Op.AND(Op.SHR(0x8, Op.DUP2), Op.DUP2)) + Op.MSTORE8(offset=0x1, value=Op.AND) + Op.JUMPI(pc=0x90, condition=Op.EQ(Op.DUP2, 0xf1)) + Op.JUMPDEST + Op.JUMPI(pc=0x7f, condition=Op.EQ(Op.DUP2, 0xf2)) + Op.JUMPDEST + Op.JUMPI(pc=0x6f, condition=Op.EQ(Op.DUP2, 0xf4)) + Op.JUMPDEST + Op.JUMPI(pc=0x61, condition=Op.EQ) + Op.SELFDESTRUCT + Op.JUMPDEST + Op.POP(Op.STATICCALL(gas=Op.GAS, address=0xc0de, args_offset=Op.DUP2, args_size=0x2, ret_offset=Op.DUP1, ret_size=0x0)) + Op.SELFDESTRUCT + Op.JUMPDEST + Op.POP(Op.DELEGATECALL(gas=Op.GAS, address=0xc0de, args_offset=Op.DUP2, args_size=0x2, ret_offset=Op.DUP1, ret_size=0x0)) + Op.JUMP(pc=0x5b) + Op.JUMPDEST + Op.POP(Op.CALLCODE(gas=Op.GAS, address=0xc0de, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x2, ret_offset=Op.DUP1, ret_size=0x0)) + Op.JUMP(pc=0x53) + Op.JUMPDEST + Op.POP(Op.CALL(gas=Op.GAS, address=0xc0de, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x2, ret_offset=Op.DUP1, ret_size=0x0)) + Op.JUMP(pc=0x4b))}),
    ],
    ids=['case0', 'case1', 'case2', 'case3', 'case4', 'case5', 'case6', 'case7'],
)
@pytest.mark.pre_alloc_mutable
def test_double_selfdestruct_test(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """The first test case required here 
https://github.com/ethereum/tests/issues/431#issue-306081539

Implements: SUC007.0, SUC007.1, SUC007.2, SUC007.3,
            SUC008.0, SUC008.1, SUC008.2, SUC008.3
."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x000000000000000000000000000000000000c0de")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000000,
    )

    pre[contract] = Account(
        balance=0xf4240,
        nonce=1,
        code=(
        Op.JUMPI(pc=0x17, condition=Op.GT(Op.CALLDATASIZE, 0x2))
        + Op.SHR(0xf0, Op.CALLDATALOAD(offset=0x0))
        + Op.JUMPI(pc=0x15, condition=Op.EQ(0x2, Op.CALLDATASIZE)) + Op.STOP
        + Op.JUMPDEST + Op.SELFDESTRUCT + Op.JUMPDEST
        + Op.SHR(0xf8, Op.CALLDATALOAD(offset=0x0)) + Op.PUSH1[0xfa]
        + Op.AND(Op.SHR(0xe8, Op.CALLDATALOAD(offset=0x0)), 0xffff) + Op.SWAP2
        + Op.PUSH1[0xff] + Op.AND(Op.SHR(0xd8, Op.CALLDATALOAD(offset=0x0)), 0xffff)
        + Op.MSTORE8(offset=0x0, value=Op.AND(Op.SHR(0x8, Op.DUP2), Op.DUP2))
        + Op.MSTORE8(offset=0x1, value=Op.AND)
        + Op.JUMPI(pc=0x90, condition=Op.EQ(Op.DUP2, 0xf1)) + Op.JUMPDEST
        + Op.JUMPI(pc=0x7f, condition=Op.EQ(Op.DUP2, 0xf2)) + Op.JUMPDEST
        + Op.JUMPI(pc=0x6f, condition=Op.EQ(Op.DUP2, 0xf4)) + Op.JUMPDEST
        + Op.JUMPI(pc=0x61, condition=Op.EQ) + Op.SELFDESTRUCT + Op.JUMPDEST
        + Op.POP(Op.STATICCALL(gas=Op.GAS, address=0xc0de, args_offset=Op.DUP2, args_size=0x2, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.SELFDESTRUCT + Op.JUMPDEST
        + Op.POP(Op.DELEGATECALL(gas=Op.GAS, address=0xc0de, args_offset=Op.DUP2, args_size=0x2, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.JUMP(pc=0x5b) + Op.JUMPDEST
        + Op.POP(Op.CALLCODE(gas=Op.GAS, address=0xc0de, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x2, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.JUMP(pc=0x53) + Op.JUMPDEST
        + Op.POP(Op.CALL(gas=Op.GAS, address=0xc0de, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x2, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.JUMP(pc=0x4b)
    ),
    )
    pre[sender] = Account(balance=0xde0b6b3a7640000, nonce=1)

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=tx_data,
        gas_limit=16777216,
        gas_price=10,
        nonce=1,
        value=1,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
