"""
Implements: SUC000, SUC001, SUC002, SUC003, SUC004, SUC005


Ported from:
tests/static/state_tests/stSystemOperationsTest/multiSelfdestructFiller.yml
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
    ["tests/static/state_tests/stSystemOperationsTest/multiSelfdestructFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        ("01", {Address("0x000000000000000000000000000000000000dead"): Account(code=Op.SHR(0xf8, Op.CALLDATALOAD(offset=0x0)) + Op.AND(Op.SHR(0xe8, Op.CALLDATALOAD(offset=0x0)), 0xffff) + Op.JUMPI(pc=0x34, condition=Op.EQ(Op.DUP3, 0x0)) + Op.JUMPI(pc=0x32, condition=Op.EQ(Op.DUP3, 0xff)) + Op.PUSH1[0x0] + Op.DUP1 + Op.DUP1 + Op.DUP1 + Op.SWAP5 + Op.DUP2 + Op.SWAP5 + Op.JUMPI(pc=0x2d, condition=Op.EQ(Op.CALL, Op.GAS)) + Op.STOP + Op.JUMPDEST + Op.REVERT(offset=Op.DUP1, size=0x0) + Op.JUMPDEST + Op.SELFDESTRUCT + Op.JUMPDEST + Op.STOP), Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(storage={0: 1, 1: 3, 16: 1, 17: 3, 18: 2}, code=Op.MSTORE8(offset=0x0, value=0xff) + Op.MSTORE8(offset=0x1, value=0x10) + Op.MSTORE8(offset=0x2, value=0x0) + Op.SSTORE(key=0x0, value=Op.CALL(gas=Op.GAS, address=0xdead, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x3, ret_offset=Op.DUP1, ret_size=0x0)) + Op.SSTORE(key=0x1, value=Op.BALANCE(address=0x1000)) + Op.SSTORE(key=0x2, value=Op.BALANCE(address=0xdead)) + Op.SHR(0xf8, Op.CALLDATALOAD(offset=0x0)) + Op.JUMPI(pc=0xce, condition=Op.EQ(0x1, Op.DUP1)) + Op.JUMPI(pc=0xbc, condition=Op.EQ(0x2, Op.DUP1)) + Op.JUMPI(pc=0xa5, condition=Op.EQ(0x3, Op.DUP1)) + Op.JUMPI(pc=0x8a, condition=Op.EQ(0x4, Op.DUP1)) + Op.PUSH1[0x5] + Op.JUMPI(pc=0x58, condition=Op.EQ) + Op.REVERT(offset=Op.DUP1, size=0x0) + Op.JUMPDEST + Op.MSTORE8(offset=0x0, value=0x1) + Op.MSTORE8(offset=0x2, value=0x1) + Op.CALL(gas=Op.GAS, address=0xdead, value=0x2, args_offset=Op.DUP2, args_size=0x3, ret_offset=Op.DUP1, ret_size=0x0) + Op.JUMPDEST + Op.PUSH1[0x10] + Op.SSTORE + Op.SSTORE(key=0x11, value=Op.BALANCE(address=0x1000)) + Op.SSTORE(key=0x12, value=Op.BALANCE(address=0xdead)) + Op.SSTORE(key=0x13, value=Op.BALANCE(address=0x1001)) + Op.STOP + Op.JUMPDEST + Op.POP + Op.MSTORE8(offset=0x0, value=0x1) + Op.MSTORE8(offset=0x2, value=0x1) + Op.CALL(gas=Op.GAS, address=0xdead, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x3, ret_offset=Op.DUP1, ret_size=0x0) + Op.JUMP(pc=0x70) + Op.JUMPDEST + Op.POP + Op.MSTORE8(offset=0x2, value=0x1) + Op.CALL(gas=Op.GAS, address=0xdead, value=0x2, args_offset=Op.DUP2, args_size=0x3, ret_offset=Op.DUP1, ret_size=0x0) + Op.JUMP(pc=0x70) + Op.JUMPDEST + Op.POP + Op.CALL(gas=Op.GAS, address=0xdead, value=0x2, args_offset=Op.DUP2, args_size=0x3, ret_offset=Op.DUP1, ret_size=0x0) + Op.JUMP(pc=0x70) + Op.JUMPDEST + Op.POP + Op.CALL(gas=Op.GAS, address=0xdead, value=0x2, args_offset=Op.DUP1, args_size=0x3, ret_offset=Op.DUP1, ret_size=0x0) + Op.JUMP(pc=0x70))}),
        ("02", {Address("0x000000000000000000000000000000000000dead"): Account(code=Op.SHR(0xf8, Op.CALLDATALOAD(offset=0x0)) + Op.AND(Op.SHR(0xe8, Op.CALLDATALOAD(offset=0x0)), 0xffff) + Op.JUMPI(pc=0x34, condition=Op.EQ(Op.DUP3, 0x0)) + Op.JUMPI(pc=0x32, condition=Op.EQ(Op.DUP3, 0xff)) + Op.PUSH1[0x0] + Op.DUP1 + Op.DUP1 + Op.DUP1 + Op.SWAP5 + Op.DUP2 + Op.SWAP5 + Op.JUMPI(pc=0x2d, condition=Op.EQ(Op.CALL, Op.GAS)) + Op.STOP + Op.JUMPDEST + Op.REVERT(offset=Op.DUP1, size=0x0) + Op.JUMPDEST + Op.SELFDESTRUCT + Op.JUMPDEST + Op.STOP), Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(storage={0: 1, 1: 3, 16: 1, 17: 5}, code=Op.MSTORE8(offset=0x0, value=0xff) + Op.MSTORE8(offset=0x1, value=0x10) + Op.MSTORE8(offset=0x2, value=0x0) + Op.SSTORE(key=0x0, value=Op.CALL(gas=Op.GAS, address=0xdead, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x3, ret_offset=Op.DUP1, ret_size=0x0)) + Op.SSTORE(key=0x1, value=Op.BALANCE(address=0x1000)) + Op.SSTORE(key=0x2, value=Op.BALANCE(address=0xdead)) + Op.SHR(0xf8, Op.CALLDATALOAD(offset=0x0)) + Op.JUMPI(pc=0xce, condition=Op.EQ(0x1, Op.DUP1)) + Op.JUMPI(pc=0xbc, condition=Op.EQ(0x2, Op.DUP1)) + Op.JUMPI(pc=0xa5, condition=Op.EQ(0x3, Op.DUP1)) + Op.JUMPI(pc=0x8a, condition=Op.EQ(0x4, Op.DUP1)) + Op.PUSH1[0x5] + Op.JUMPI(pc=0x58, condition=Op.EQ) + Op.REVERT(offset=Op.DUP1, size=0x0) + Op.JUMPDEST + Op.MSTORE8(offset=0x0, value=0x1) + Op.MSTORE8(offset=0x2, value=0x1) + Op.CALL(gas=Op.GAS, address=0xdead, value=0x2, args_offset=Op.DUP2, args_size=0x3, ret_offset=Op.DUP1, ret_size=0x0) + Op.JUMPDEST + Op.PUSH1[0x10] + Op.SSTORE + Op.SSTORE(key=0x11, value=Op.BALANCE(address=0x1000)) + Op.SSTORE(key=0x12, value=Op.BALANCE(address=0xdead)) + Op.SSTORE(key=0x13, value=Op.BALANCE(address=0x1001)) + Op.STOP + Op.JUMPDEST + Op.POP + Op.MSTORE8(offset=0x0, value=0x1) + Op.MSTORE8(offset=0x2, value=0x1) + Op.CALL(gas=Op.GAS, address=0xdead, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x3, ret_offset=Op.DUP1, ret_size=0x0) + Op.JUMP(pc=0x70) + Op.JUMPDEST + Op.POP + Op.MSTORE8(offset=0x2, value=0x1) + Op.CALL(gas=Op.GAS, address=0xdead, value=0x2, args_offset=Op.DUP2, args_size=0x3, ret_offset=Op.DUP1, ret_size=0x0) + Op.JUMP(pc=0x70) + Op.JUMPDEST + Op.POP + Op.CALL(gas=Op.GAS, address=0xdead, value=0x2, args_offset=Op.DUP2, args_size=0x3, ret_offset=Op.DUP1, ret_size=0x0) + Op.JUMP(pc=0x70) + Op.JUMPDEST + Op.POP + Op.CALL(gas=Op.GAS, address=0xdead, value=0x2, args_offset=Op.DUP1, args_size=0x3, ret_offset=Op.DUP1, ret_size=0x0) + Op.JUMP(pc=0x70))}),
        ("03", {Address("0x000000000000000000000000000000000000dead"): Account(code=Op.SHR(0xf8, Op.CALLDATALOAD(offset=0x0)) + Op.AND(Op.SHR(0xe8, Op.CALLDATALOAD(offset=0x0)), 0xffff) + Op.JUMPI(pc=0x34, condition=Op.EQ(Op.DUP3, 0x0)) + Op.JUMPI(pc=0x32, condition=Op.EQ(Op.DUP3, 0xff)) + Op.PUSH1[0x0] + Op.DUP1 + Op.DUP1 + Op.DUP1 + Op.SWAP5 + Op.DUP2 + Op.SWAP5 + Op.JUMPI(pc=0x2d, condition=Op.EQ(Op.CALL, Op.GAS)) + Op.STOP + Op.JUMPDEST + Op.REVERT(offset=Op.DUP1, size=0x0) + Op.JUMPDEST + Op.SELFDESTRUCT + Op.JUMPDEST + Op.STOP), Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(storage={0: 1, 1: 3, 16: 1, 17: 3, 19: 2}, code=Op.MSTORE8(offset=0x0, value=0xff) + Op.MSTORE8(offset=0x1, value=0x10) + Op.MSTORE8(offset=0x2, value=0x0) + Op.SSTORE(key=0x0, value=Op.CALL(gas=Op.GAS, address=0xdead, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x3, ret_offset=Op.DUP1, ret_size=0x0)) + Op.SSTORE(key=0x1, value=Op.BALANCE(address=0x1000)) + Op.SSTORE(key=0x2, value=Op.BALANCE(address=0xdead)) + Op.SHR(0xf8, Op.CALLDATALOAD(offset=0x0)) + Op.JUMPI(pc=0xce, condition=Op.EQ(0x1, Op.DUP1)) + Op.JUMPI(pc=0xbc, condition=Op.EQ(0x2, Op.DUP1)) + Op.JUMPI(pc=0xa5, condition=Op.EQ(0x3, Op.DUP1)) + Op.JUMPI(pc=0x8a, condition=Op.EQ(0x4, Op.DUP1)) + Op.PUSH1[0x5] + Op.JUMPI(pc=0x58, condition=Op.EQ) + Op.REVERT(offset=Op.DUP1, size=0x0) + Op.JUMPDEST + Op.MSTORE8(offset=0x0, value=0x1) + Op.MSTORE8(offset=0x2, value=0x1) + Op.CALL(gas=Op.GAS, address=0xdead, value=0x2, args_offset=Op.DUP2, args_size=0x3, ret_offset=Op.DUP1, ret_size=0x0) + Op.JUMPDEST + Op.PUSH1[0x10] + Op.SSTORE + Op.SSTORE(key=0x11, value=Op.BALANCE(address=0x1000)) + Op.SSTORE(key=0x12, value=Op.BALANCE(address=0xdead)) + Op.SSTORE(key=0x13, value=Op.BALANCE(address=0x1001)) + Op.STOP + Op.JUMPDEST + Op.POP + Op.MSTORE8(offset=0x0, value=0x1) + Op.MSTORE8(offset=0x2, value=0x1) + Op.CALL(gas=Op.GAS, address=0xdead, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x3, ret_offset=Op.DUP1, ret_size=0x0) + Op.JUMP(pc=0x70) + Op.JUMPDEST + Op.POP + Op.MSTORE8(offset=0x2, value=0x1) + Op.CALL(gas=Op.GAS, address=0xdead, value=0x2, args_offset=Op.DUP2, args_size=0x3, ret_offset=Op.DUP1, ret_size=0x0) + Op.JUMP(pc=0x70) + Op.JUMPDEST + Op.POP + Op.CALL(gas=Op.GAS, address=0xdead, value=0x2, args_offset=Op.DUP2, args_size=0x3, ret_offset=Op.DUP1, ret_size=0x0) + Op.JUMP(pc=0x70) + Op.JUMPDEST + Op.POP + Op.CALL(gas=Op.GAS, address=0xdead, value=0x2, args_offset=Op.DUP1, args_size=0x3, ret_offset=Op.DUP1, ret_size=0x0) + Op.JUMP(pc=0x70))}),
        ("04", {Address("0x000000000000000000000000000000000000dead"): Account(code=Op.SHR(0xf8, Op.CALLDATALOAD(offset=0x0)) + Op.AND(Op.SHR(0xe8, Op.CALLDATALOAD(offset=0x0)), 0xffff) + Op.JUMPI(pc=0x34, condition=Op.EQ(Op.DUP3, 0x0)) + Op.JUMPI(pc=0x32, condition=Op.EQ(Op.DUP3, 0xff)) + Op.PUSH1[0x0] + Op.DUP1 + Op.DUP1 + Op.DUP1 + Op.SWAP5 + Op.DUP2 + Op.SWAP5 + Op.JUMPI(pc=0x2d, condition=Op.EQ(Op.CALL, Op.GAS)) + Op.STOP + Op.JUMPDEST + Op.REVERT(offset=Op.DUP1, size=0x0) + Op.JUMPDEST + Op.SELFDESTRUCT + Op.JUMPDEST + Op.STOP), Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(storage={0: 1, 1: 3, 17: 3}, code=Op.MSTORE8(offset=0x0, value=0xff) + Op.MSTORE8(offset=0x1, value=0x10) + Op.MSTORE8(offset=0x2, value=0x0) + Op.SSTORE(key=0x0, value=Op.CALL(gas=Op.GAS, address=0xdead, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x3, ret_offset=Op.DUP1, ret_size=0x0)) + Op.SSTORE(key=0x1, value=Op.BALANCE(address=0x1000)) + Op.SSTORE(key=0x2, value=Op.BALANCE(address=0xdead)) + Op.SHR(0xf8, Op.CALLDATALOAD(offset=0x0)) + Op.JUMPI(pc=0xce, condition=Op.EQ(0x1, Op.DUP1)) + Op.JUMPI(pc=0xbc, condition=Op.EQ(0x2, Op.DUP1)) + Op.JUMPI(pc=0xa5, condition=Op.EQ(0x3, Op.DUP1)) + Op.JUMPI(pc=0x8a, condition=Op.EQ(0x4, Op.DUP1)) + Op.PUSH1[0x5] + Op.JUMPI(pc=0x58, condition=Op.EQ) + Op.REVERT(offset=Op.DUP1, size=0x0) + Op.JUMPDEST + Op.MSTORE8(offset=0x0, value=0x1) + Op.MSTORE8(offset=0x2, value=0x1) + Op.CALL(gas=Op.GAS, address=0xdead, value=0x2, args_offset=Op.DUP2, args_size=0x3, ret_offset=Op.DUP1, ret_size=0x0) + Op.JUMPDEST + Op.PUSH1[0x10] + Op.SSTORE + Op.SSTORE(key=0x11, value=Op.BALANCE(address=0x1000)) + Op.SSTORE(key=0x12, value=Op.BALANCE(address=0xdead)) + Op.SSTORE(key=0x13, value=Op.BALANCE(address=0x1001)) + Op.STOP + Op.JUMPDEST + Op.POP + Op.MSTORE8(offset=0x0, value=0x1) + Op.MSTORE8(offset=0x2, value=0x1) + Op.CALL(gas=Op.GAS, address=0xdead, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x3, ret_offset=Op.DUP1, ret_size=0x0) + Op.JUMP(pc=0x70) + Op.JUMPDEST + Op.POP + Op.MSTORE8(offset=0x2, value=0x1) + Op.CALL(gas=Op.GAS, address=0xdead, value=0x2, args_offset=Op.DUP2, args_size=0x3, ret_offset=Op.DUP1, ret_size=0x0) + Op.JUMP(pc=0x70) + Op.JUMPDEST + Op.POP + Op.CALL(gas=Op.GAS, address=0xdead, value=0x2, args_offset=Op.DUP2, args_size=0x3, ret_offset=Op.DUP1, ret_size=0x0) + Op.JUMP(pc=0x70) + Op.JUMPDEST + Op.POP + Op.CALL(gas=Op.GAS, address=0xdead, value=0x2, args_offset=Op.DUP1, args_size=0x3, ret_offset=Op.DUP1, ret_size=0x0) + Op.JUMP(pc=0x70))}),
        ("05", {Address("0x000000000000000000000000000000000000dead"): Account(code=Op.SHR(0xf8, Op.CALLDATALOAD(offset=0x0)) + Op.AND(Op.SHR(0xe8, Op.CALLDATALOAD(offset=0x0)), 0xffff) + Op.JUMPI(pc=0x34, condition=Op.EQ(Op.DUP3, 0x0)) + Op.JUMPI(pc=0x32, condition=Op.EQ(Op.DUP3, 0xff)) + Op.PUSH1[0x0] + Op.DUP1 + Op.DUP1 + Op.DUP1 + Op.SWAP5 + Op.DUP2 + Op.SWAP5 + Op.JUMPI(pc=0x2d, condition=Op.EQ(Op.CALL, Op.GAS)) + Op.STOP + Op.JUMPDEST + Op.REVERT(offset=Op.DUP1, size=0x0) + Op.JUMPDEST + Op.SELFDESTRUCT + Op.JUMPDEST + Op.STOP), Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(storage={0: 1, 1: 3, 16: 1, 17: 3, 18: 1, 19: 1}, code=Op.MSTORE8(offset=0x0, value=0xff) + Op.MSTORE8(offset=0x1, value=0x10) + Op.MSTORE8(offset=0x2, value=0x0) + Op.SSTORE(key=0x0, value=Op.CALL(gas=Op.GAS, address=0xdead, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x3, ret_offset=Op.DUP1, ret_size=0x0)) + Op.SSTORE(key=0x1, value=Op.BALANCE(address=0x1000)) + Op.SSTORE(key=0x2, value=Op.BALANCE(address=0xdead)) + Op.SHR(0xf8, Op.CALLDATALOAD(offset=0x0)) + Op.JUMPI(pc=0xce, condition=Op.EQ(0x1, Op.DUP1)) + Op.JUMPI(pc=0xbc, condition=Op.EQ(0x2, Op.DUP1)) + Op.JUMPI(pc=0xa5, condition=Op.EQ(0x3, Op.DUP1)) + Op.JUMPI(pc=0x8a, condition=Op.EQ(0x4, Op.DUP1)) + Op.PUSH1[0x5] + Op.JUMPI(pc=0x58, condition=Op.EQ) + Op.REVERT(offset=Op.DUP1, size=0x0) + Op.JUMPDEST + Op.MSTORE8(offset=0x0, value=0x1) + Op.MSTORE8(offset=0x2, value=0x1) + Op.CALL(gas=Op.GAS, address=0xdead, value=0x2, args_offset=Op.DUP2, args_size=0x3, ret_offset=Op.DUP1, ret_size=0x0) + Op.JUMPDEST + Op.PUSH1[0x10] + Op.SSTORE + Op.SSTORE(key=0x11, value=Op.BALANCE(address=0x1000)) + Op.SSTORE(key=0x12, value=Op.BALANCE(address=0xdead)) + Op.SSTORE(key=0x13, value=Op.BALANCE(address=0x1001)) + Op.STOP + Op.JUMPDEST + Op.POP + Op.MSTORE8(offset=0x0, value=0x1) + Op.MSTORE8(offset=0x2, value=0x1) + Op.CALL(gas=Op.GAS, address=0xdead, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x3, ret_offset=Op.DUP1, ret_size=0x0) + Op.JUMP(pc=0x70) + Op.JUMPDEST + Op.POP + Op.MSTORE8(offset=0x2, value=0x1) + Op.CALL(gas=Op.GAS, address=0xdead, value=0x2, args_offset=Op.DUP2, args_size=0x3, ret_offset=Op.DUP1, ret_size=0x0) + Op.JUMP(pc=0x70) + Op.JUMPDEST + Op.POP + Op.CALL(gas=Op.GAS, address=0xdead, value=0x2, args_offset=Op.DUP2, args_size=0x3, ret_offset=Op.DUP1, ret_size=0x0) + Op.JUMP(pc=0x70) + Op.JUMPDEST + Op.POP + Op.CALL(gas=Op.GAS, address=0xdead, value=0x2, args_offset=Op.DUP1, args_size=0x3, ret_offset=Op.DUP1, ret_size=0x0) + Op.JUMP(pc=0x70))}),
    ],
    ids=['case0', 'case1', 'case2', 'case3', 'case4'],
)
@pytest.mark.pre_alloc_mutable
def test_multi_selfdestruct(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Implements: SUC000, SUC001, SUC002, SUC003, SUC004, SUC005
."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xcccccccccccccccccccccccccccccccccccccccc")
    callee = Address("0x000000000000000000000000000000000000dead")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=1000,
        gas_limit=71794957647893862,
    )

    pre[callee] = Account(
        balance=3,
        nonce=1,
        code=(
        Op.SHR(0xf8, Op.CALLDATALOAD(offset=0x0))
        + Op.AND(Op.SHR(0xe8, Op.CALLDATALOAD(offset=0x0)), 0xffff)
        + Op.JUMPI(pc=0x34, condition=Op.EQ(Op.DUP3, 0x0))
        + Op.JUMPI(pc=0x32, condition=Op.EQ(Op.DUP3, 0xff)) + Op.PUSH1[0x0] + Op.DUP1
        + Op.DUP1 + Op.DUP1 + Op.SWAP5 + Op.DUP2 + Op.SWAP5
        + Op.JUMPI(pc=0x2d, condition=Op.EQ(Op.CALL, Op.GAS)) + Op.STOP + Op.JUMPDEST
        + Op.REVERT(offset=Op.DUP1, size=0x0) + Op.JUMPDEST + Op.SELFDESTRUCT
        + Op.JUMPDEST + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0xde0b6b3a7640000, nonce=1)
    pre[contract] = Account(
        balance=0x5f5e100,
        nonce=1,
        code=(
        Op.MSTORE8(offset=0x0, value=0xff) + Op.MSTORE8(offset=0x1, value=0x10)
        + Op.MSTORE8(offset=0x2, value=0x0)
        + Op.SSTORE(key=0x0, value=Op.CALL(gas=Op.GAS, address=0xdead, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x3, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.SSTORE(key=0x1, value=Op.BALANCE(address=0x1000))
        + Op.SSTORE(key=0x2, value=Op.BALANCE(address=0xdead))
        + Op.SHR(0xf8, Op.CALLDATALOAD(offset=0x0))
        + Op.JUMPI(pc=0xce, condition=Op.EQ(0x1, Op.DUP1))
        + Op.JUMPI(pc=0xbc, condition=Op.EQ(0x2, Op.DUP1))
        + Op.JUMPI(pc=0xa5, condition=Op.EQ(0x3, Op.DUP1))
        + Op.JUMPI(pc=0x8a, condition=Op.EQ(0x4, Op.DUP1)) + Op.PUSH1[0x5]
        + Op.JUMPI(pc=0x58, condition=Op.EQ) + Op.REVERT(offset=Op.DUP1, size=0x0)
        + Op.JUMPDEST + Op.MSTORE8(offset=0x0, value=0x1)
        + Op.MSTORE8(offset=0x2, value=0x1)
        + Op.CALL(gas=Op.GAS, address=0xdead, value=0x2, args_offset=Op.DUP2, args_size=0x3, ret_offset=Op.DUP1, ret_size=0x0)
        + Op.JUMPDEST + Op.PUSH1[0x10] + Op.SSTORE
        + Op.SSTORE(key=0x11, value=Op.BALANCE(address=0x1000))
        + Op.SSTORE(key=0x12, value=Op.BALANCE(address=0xdead))
        + Op.SSTORE(key=0x13, value=Op.BALANCE(address=0x1001)) + Op.STOP
        + Op.JUMPDEST + Op.POP + Op.MSTORE8(offset=0x0, value=0x1)
        + Op.MSTORE8(offset=0x2, value=0x1)
        + Op.CALL(gas=Op.GAS, address=0xdead, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x3, ret_offset=Op.DUP1, ret_size=0x0)
        + Op.JUMP(pc=0x70) + Op.JUMPDEST + Op.POP + Op.MSTORE8(offset=0x2, value=0x1)
        + Op.CALL(gas=Op.GAS, address=0xdead, value=0x2, args_offset=Op.DUP2, args_size=0x3, ret_offset=Op.DUP1, ret_size=0x0)
        + Op.JUMP(pc=0x70) + Op.JUMPDEST + Op.POP
        + Op.CALL(gas=Op.GAS, address=0xdead, value=0x2, args_offset=Op.DUP2, args_size=0x3, ret_offset=Op.DUP1, ret_size=0x0)
        + Op.JUMP(pc=0x70) + Op.JUMPDEST + Op.POP
        + Op.CALL(gas=Op.GAS, address=0xdead, value=0x2, args_offset=Op.DUP1, args_size=0x3, ret_offset=Op.DUP1, ret_size=0x0)
        + Op.JUMP(pc=0x70)
    ),
        storage={0x0: 0x60a7, 0x1: 0x60a7, 0x10: 0x60a7, 0x11: 0x60a7, 0x12: 0x60a7, 0x13: 0x60a7},
    )

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=tx_data,
        gas_limit=10000000,
        gas_price=1000,
        nonce=1,
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
