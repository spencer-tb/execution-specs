"""
Ported from:
tests/static/state_tests/stSpecialTest/block504980Filler.json
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
    ["tests/static/state_tests/stSpecialTest/block504980Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_block504980(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x1cdc8315bdb1362de8b7b2fa9ee75dc873037179")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xb03f030056db7d467d778326658bac0d1b35d8f7")
    callee = Address("0x0000000000000000000000000000000000000000")
    callee_1 = Address("0x0000000000000000000000000000000000000001")
    callee_2 = Address("0x0000000000000000000000000000000000000002")
    callee_3 = Address("0x0000000000000000000000000000000000000003")
    callee_4 = Address("0x0000000000000000000000000000000000000004")
    callee_5 = Address("0x0ea65418d7bf32680f55572c943a94b590804998")
    callee_6 = Address("0x142a6927cf0060133187ba8a8e74d641438f0c1c")
    callee_7 = Address("0x9761fecf88590592cf05ce545504d376d1693ab3")
    callee_8 = Address("0xc9ae5868651bf7b7db6e360217db49ce4e69c07e")
    callee_9 = Address("0xe509e3a93beb1eba72f8cb8d25f93a85e2d54afb")
    callee_10 = Address("0xf1562e1c0d0baa3ea746442bb7f11153fcf5cfda")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=3141592,
    )

    pre[callee] = Account(balance=1, nonce=0)
    pre[callee_1] = Account(balance=1, nonce=0)
    pre[callee_2] = Account(balance=1, nonce=0)
    pre[callee_3] = Account(balance=1, nonce=0)
    pre[callee_4] = Account(balance=1, nonce=0)
    pre[callee_5] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.MSTORE8(offset=0x289f, value=0x0)
        + Op.DIV(Op.CALLDATALOAD(offset=0x0), 0x100000000000000000000000000000000000000000000000000000000)
        + Op.MSTORE(offset=0x20, value=0xc9ae5868651bf7b7db6e360217db49ce4e69c07e)
        + Op.JUMPI(pc=0x127, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xc4982a85)))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0x80]
        + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MSTORE(offset=0xa0, value=Op.SLOAD(key=Op.SHA3))
        + Op.MLOAD(offset=0xa0) + Op.ADD(0x20, Op.MUL(0x20, Op.DUP1)) + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1
        + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0xe0] + Op.MSTORE
        + Op.MSTORE(offset=0x140, value=0x0) + Op.JUMPDEST
        + Op.JUMPI(pc=0x10b, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x140), Op.MLOAD(offset=0xa0))))
        + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x1)
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=Op.MLOAD(offset=0x140))
        + Op.DUP1 + Op.SWAP1 + Op.POP
        + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0xe0), Op.MUL(0x20, Op.MLOAD(offset=0x140))), value=Op.SLOAD(key=Op.SHA3))
        + Op.MSTORE(offset=0x140, value=Op.ADD(Op.MLOAD(offset=0x140), 0x1))
        + Op.JUMP(pc=Op.PUSH2[0xad]) + Op.JUMPDEST + Op.MLOAD(offset=0xe0)
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20)
        + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20)))
        + Op.POP + Op.JUMPDEST
        + Op.JUMPI(pc=0x176, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xcc1c944e)))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0x80]
        + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MSTORE(offset=0x1a0, value=Op.SLOAD(key=Op.SHA3))
        + Op.RETURN(offset=0x1a0, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x1d5, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x95a405b9)))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0x1e0, value=Op.CALLDATALOAD(offset=0x44)) + Op.PUSH1[0xa0]
        + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x1)
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=Op.MLOAD(offset=0x1e0))
        + Op.DUP1 + Op.SWAP1 + Op.POP
        + Op.MSTORE(offset=0x200, value=Op.SLOAD(key=Op.SHA3))
        + Op.RETURN(offset=0x200, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x224, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x71ebb662)))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0x80]
        + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x2) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MSTORE(offset=0x240, value=Op.SLOAD(key=Op.SHA3))
        + Op.RETURN(offset=0x240, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x325, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x7a57a3db)))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0x280, value=Op.CALLDATALOAD(offset=0x44)) + Op.PUSH1[0xc0]
        + Op.PUSH1[0xc0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x3)
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=Op.MLOAD(offset=0x280))
        + Op.MSTORE(offset=Op.ADD(0xa0, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1
        + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MUL(0x20, Op.SLOAD(key=Op.SHA3)) + Op.DUP1
        + Op.ADD(0x20, Op.DUP1) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1
        + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x2e9, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DIV(Op.DUP4, 0x20))))
        + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.SLOAD(key=Op.ADD(Op.DUP5, Op.DUP1)))
        + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x2c8) + Op.JUMPDEST
        + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.AND(Op.SLOAD(key=Op.ADD(Op.DUP6, Op.DUP2)), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20))))))
        + Op.DUP2 + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP
        + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20)
        + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20)))
        + Op.POP + Op.JUMPDEST
        + Op.JUMPI(pc=0x394, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xf73dc690)))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0x3c0, value=Op.CALLDATALOAD(offset=0x44))
        + Op.MSTORE(offset=0x3e0, value=Op.CALLDATALOAD(offset=0x64)) + Op.PUSH1[0xc0]
        + Op.PUSH1[0xc0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x3)
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=Op.MLOAD(offset=0x3c0))
        + Op.MSTORE(offset=Op.ADD(0xa0, Op.DUP2), value=Op.MLOAD(offset=0x3e0))
        + Op.DUP1 + Op.SWAP1 + Op.POP
        + Op.MSTORE(offset=0x400, value=Op.SLOAD(key=Op.SHA3))
        + Op.RETURN(offset=0x400, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x3f3, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x54cc6109)))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0x3c0, value=Op.CALLDATALOAD(offset=0x44)) + Op.PUSH1[0xa0]
        + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x4)
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=Op.MLOAD(offset=0x3c0))
        + Op.DUP1 + Op.SWAP1 + Op.POP
        + Op.MSTORE(offset=0x440, value=Op.SLOAD(key=Op.SHA3))
        + Op.RETURN(offset=0x440, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x442, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xc63ef546)))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0x80]
        + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x5) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MSTORE(offset=0x480, value=Op.SLOAD(key=Op.SHA3))
        + Op.RETURN(offset=0x480, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x533, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x9381779b)))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0xa0]
        + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x6)
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1
        + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x5) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MUL(0x20, Op.SLOAD(key=Op.SHA3)) + Op.DUP1
        + Op.ADD(0x20, Op.DUP1) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1
        + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x4f7, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DIV(Op.DUP4, 0x20))))
        + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.SLOAD(key=Op.ADD(Op.DUP5, Op.DUP1)))
        + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x4d6) + Op.JUMPDEST
        + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.AND(Op.SLOAD(key=Op.ADD(Op.DUP6, Op.DUP2)), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20))))))
        + Op.DUP2 + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP
        + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20)
        + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20)))
        + Op.POP + Op.JUMPDEST
        + Op.JUMPI(pc=0x624, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x4f9c6eeb)))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0xa0]
        + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x7)
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1
        + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x5) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MUL(0x20, Op.SLOAD(key=Op.SHA3)) + Op.DUP1
        + Op.ADD(0x20, Op.DUP1) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1
        + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x5e8, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DIV(Op.DUP4, 0x20))))
        + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.SLOAD(key=Op.ADD(Op.DUP5, Op.DUP1)))
        + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x5c7) + Op.JUMPDEST
        + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.AND(Op.SLOAD(key=Op.ADD(Op.DUP6, Op.DUP2)), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20))))))
        + Op.DUP2 + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP
        + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20)
        + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20)))
        + Op.POP + Op.JUMPDEST
        + Op.JUMPI(pc=0x715, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x7dc12195)))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0xa0]
        + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x8)
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1
        + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x5) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MUL(0x20, Op.SLOAD(key=Op.SHA3)) + Op.DUP1
        + Op.ADD(0x20, Op.DUP1) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1
        + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x6d9, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DIV(Op.DUP4, 0x20))))
        + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.SLOAD(key=Op.ADD(Op.DUP5, Op.DUP1)))
        + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x6b8) + Op.JUMPDEST
        + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.AND(Op.SLOAD(key=Op.ADD(Op.DUP6, Op.DUP2)), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20))))))
        + Op.DUP2 + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP
        + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20)
        + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20)))
        + Op.POP + Op.JUMPDEST
        + Op.JUMPI(pc=0x806, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xfa9832d1)))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0xa0]
        + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x9)
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1
        + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MUL(0x20, Op.SLOAD(key=Op.SHA3)) + Op.DUP1
        + Op.ADD(0x20, Op.DUP1) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1
        + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x7ca, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DIV(Op.DUP4, 0x20))))
        + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.SLOAD(key=Op.ADD(Op.DUP5, Op.DUP1)))
        + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x7a9) + Op.JUMPDEST
        + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.AND(Op.SLOAD(key=Op.ADD(Op.DUP6, Op.DUP2)), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20))))))
        + Op.DUP2 + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP
        + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20)
        + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20)))
        + Op.POP + Op.JUMPDEST
        + Op.JUMPI(pc=0x8f7, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x2c5a40d5)))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0xa0]
        + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0xa)
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1
        + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x5) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MUL(0x20, Op.SLOAD(key=Op.SHA3)) + Op.DUP1
        + Op.ADD(0x20, Op.DUP1) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1
        + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x8bb, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DIV(Op.DUP4, 0x20))))
        + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.SLOAD(key=Op.ADD(Op.DUP5, Op.DUP1)))
        + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x89a) + Op.JUMPDEST
        + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.AND(Op.SLOAD(key=Op.ADD(Op.DUP6, Op.DUP2)), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20))))))
        + Op.DUP2 + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP
        + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20)
        + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20)))
        + Op.POP + Op.JUMPDEST
        + Op.JUMPI(pc=0x9eb, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xe05dcb56)))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0xa0]
        + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0xb)
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.PUSH1[0x2] + Op.PUSH1[0x80] + Op.PUSH1[0x80]
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MUL(0x20, Op.SLOAD(key=Op.SHA3)) + Op.ADD + Op.DUP1
        + Op.ADD(0x20, Op.DUP1) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1
        + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x9af, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DIV(Op.DUP4, 0x20))))
        + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.SLOAD(key=Op.ADD(Op.DUP5, Op.DUP1)))
        + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x98e) + Op.JUMPDEST
        + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.AND(Op.SLOAD(key=Op.ADD(Op.DUP6, Op.DUP2)), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20))))))
        + Op.DUP2 + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP
        + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20)
        + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20)))
        + Op.POP + Op.JUMPDEST
        + Op.JUMPI(pc=0xa3a, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x586b5be0)))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0x80]
        + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0xc) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MSTORE(offset=0xb80, value=Op.SLOAD(key=Op.SHA3))
        + Op.RETURN(offset=0xb80, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0xb58, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xeb8af5aa)))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0xa0]
        + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0xd)
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1
        + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x5) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.MUL(0x20, Op.SDIV) + Op.DUP1
        + Op.ADD(0x20, Op.DUP1) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1
        + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0xb1c, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DIV(Op.DUP4, 0x20))))
        + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.SLOAD(key=Op.ADD(Op.DUP5, Op.DUP1)))
        + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0xafb) + Op.JUMPDEST
        + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.AND(Op.SLOAD(key=Op.ADD(Op.DUP6, Op.DUP2)), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20))))))
        + Op.DUP2 + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP
        + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20)
        + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20)))
        + Op.POP + Op.JUMPDEST
        + Op.JUMPI(pc=0xc76, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x7ab6ea8a)))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0xa0]
        + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0xe)
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1
        + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x5) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.MUL(0x20, Op.SDIV) + Op.DUP1
        + Op.ADD(0x20, Op.DUP1) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1
        + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0xc3a, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DIV(Op.DUP4, 0x20))))
        + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.SLOAD(key=Op.ADD(Op.DUP5, Op.DUP1)))
        + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0xc19) + Op.JUMPDEST
        + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.AND(Op.SLOAD(key=Op.ADD(Op.DUP6, Op.DUP2)), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20))))))
        + Op.DUP2 + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP
        + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20)
        + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20)))
        + Op.POP + Op.JUMPDEST
        + Op.JUMPI(pc=0xd94, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x2b810cb9)))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0xa0]
        + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0xf)
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1
        + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x5) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.MUL(0x20, Op.SDIV) + Op.DUP1
        + Op.ADD(0x20, Op.DUP1) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1
        + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0xd58, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DIV(Op.DUP4, 0x20))))
        + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.SLOAD(key=Op.ADD(Op.DUP5, Op.DUP1)))
        + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0xd37) + Op.JUMPDEST
        + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.AND(Op.SLOAD(key=Op.ADD(Op.DUP6, Op.DUP2)), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20))))))
        + Op.DUP2 + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP
        + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20)
        + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20)))
        + Op.POP + Op.JUMPDEST
        + Op.JUMPI(pc=0xe85, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x7fb42e46)))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0xa0]
        + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x10)
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1
        + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MUL(0x20, Op.SLOAD(key=Op.SHA3)) + Op.DUP1
        + Op.ADD(0x20, Op.DUP1) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1
        + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0xe49, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DIV(Op.DUP4, 0x20))))
        + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.SLOAD(key=Op.ADD(Op.DUP5, Op.DUP1)))
        + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0xe28) + Op.JUMPDEST
        + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.AND(Op.SLOAD(key=Op.ADD(Op.DUP6, Op.DUP2)), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20))))))
        + Op.DUP2 + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP
        + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20)
        + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20)))
        + Op.POP + Op.JUMPDEST
        + Op.JUMPI(pc=0xf76, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x734fa727)))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0xa0]
        + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x11)
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1
        + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MUL(0x20, Op.SLOAD(key=Op.SHA3)) + Op.DUP1
        + Op.ADD(0x20, Op.DUP1) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1
        + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0xf3a, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DIV(Op.DUP4, 0x20))))
        + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.SLOAD(key=Op.ADD(Op.DUP5, Op.DUP1)))
        + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0xf19) + Op.JUMPDEST
        + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.AND(Op.SLOAD(key=Op.ADD(Op.DUP6, Op.DUP2)), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20))))))
        + Op.DUP2 + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP
        + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20)
        + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20)))
        + Op.POP + Op.JUMPDEST
        + Op.JUMPI(pc=0x1067, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xc67fa857)))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0xa0]
        + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x12)
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1
        + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MUL(0x20, Op.SLOAD(key=Op.SHA3)) + Op.DUP1
        + Op.ADD(0x20, Op.DUP1) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1
        + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x102b, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DIV(Op.DUP4, 0x20))))
        + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.SLOAD(key=Op.ADD(Op.DUP5, Op.DUP1)))
        + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x100a) + Op.JUMPDEST
        + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.AND(Op.SLOAD(key=Op.ADD(Op.DUP6, Op.DUP2)), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20))))))
        + Op.DUP2 + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP
        + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20)
        + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20)))
        + Op.POP + Op.JUMPDEST
        + Op.JUMPI(pc=0x1185, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x5ed853e4)))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0xa0]
        + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x13)
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1
        + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x5) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.MUL(0x20, Op.SDIV) + Op.DUP1
        + Op.ADD(0x20, Op.DUP1) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1
        + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x1149, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DIV(Op.DUP4, 0x20))))
        + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.SLOAD(key=Op.ADD(Op.DUP5, Op.DUP1)))
        + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x1128) + Op.JUMPDEST
        + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.AND(Op.SLOAD(key=Op.ADD(Op.DUP6, Op.DUP2)), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20))))))
        + Op.DUP2 + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP
        + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20)
        + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20)))
        + Op.POP + Op.JUMPDEST
        + Op.JUMPI(pc=0x12a3, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xb86f5125)))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0xa0]
        + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x14)
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1
        + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x5) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.MUL(0x20, Op.SDIV) + Op.DUP1
        + Op.ADD(0x20, Op.DUP1) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1
        + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x1267, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DIV(Op.DUP4, 0x20))))
        + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.SLOAD(key=Op.ADD(Op.DUP5, Op.DUP1)))
        + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x1246) + Op.JUMPDEST
        + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.AND(Op.SLOAD(key=Op.ADD(Op.DUP6, Op.DUP2)), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20))))))
        + Op.DUP2 + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP
        + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20)
        + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20)))
        + Op.POP + Op.JUMPDEST
        + Op.JUMPI(pc=0x1394, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xbc3d7d85)))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0xa0]
        + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x15)
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1
        + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MUL(0x20, Op.SLOAD(key=Op.SHA3)) + Op.DUP1
        + Op.ADD(0x20, Op.DUP1) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1
        + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x1358, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DIV(Op.DUP4, 0x20))))
        + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.SLOAD(key=Op.ADD(Op.DUP5, Op.DUP1)))
        + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x1337) + Op.JUMPDEST
        + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.AND(Op.SLOAD(key=Op.ADD(Op.DUP6, Op.DUP2)), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20))))))
        + Op.DUP2 + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP
        + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20)
        + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20)))
        + Op.POP + Op.JUMPDEST
        + Op.JUMPI(pc=0x1481, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xa2302f2f)))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x1680, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0x16a0, value=Op.CALLDATALOAD(offset=0x44))
        + Op.MLOAD(offset=0x16a0) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x1680))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x1) + Op.PUSH1[0x80]
        + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x1680))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=Op.SLOAD(key=Op.SHA3))
        + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.PUSH1[0x1]
        + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x1680))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.ADD + Op.PUSH1[0x80] + Op.PUSH1[0x80]
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x1680))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.MSTORE(offset=0x1740, value=0x1)
        + Op.RETURN(offset=0x1740, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x14dd, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x58ca2bc)))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0x1760, value=Op.CALLDATALOAD(offset=0x44))
        + Op.MLOAD(offset=0x1760) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x2) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.MSTORE(offset=0x17a0, value=0x1)
        + Op.RETURN(offset=0x17a0, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x1617, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x5d3b965b)))
        + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE
        + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE)
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0x280, value=Op.CALLDATALOAD(offset=0x44))
        + Op.MSTORE(offset=0x17e0, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x64)))
        + Op.MSTORE(offset=0x1800, value=Op.CALLDATALOAD(offset=0x84)) + Op.POP
        + Op.PUSH1[0xc0] + Op.PUSH1[0xc0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x3)
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=Op.MLOAD(offset=0x280))
        + Op.MSTORE(offset=Op.ADD(0xa0, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3
        + Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x17e0), 0x20)))
        + Op.DIV(Op.DUP2, 0x20) + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x158c, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DUP2)))
        + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x17e0), Op.MUL(0x20, Op.DUP1))))
        + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x156b) + Op.JUMPDEST
        + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.AND(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x17e0), Op.MUL(0x20, Op.DUP2))), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20))))))
        + Op.POP + Op.POP + Op.POP + Op.POP + Op.MLOAD(offset=0x1800) + Op.PUSH1[0x80]
        + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x2) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.ADD + Op.PUSH1[0x80] + Op.PUSH1[0x80]
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x2) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.MSTORE(offset=0x1900, value=0x1)
        + Op.RETURN(offset=0x1900, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x1673, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xb0e14f0f)))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0x1920, value=Op.CALLDATALOAD(offset=0x44))
        + Op.MLOAD(offset=0x1920) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x5) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.MSTORE(offset=0x1960, value=0x1)
        + Op.RETURN(offset=0x1960, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x1739, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x6acccdbc)))
        + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE
        + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE)
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0x1980, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x44)))
        + Op.POP + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE
        + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x6)
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3
        + Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x1980), 0x20)))
        + Op.DIV(Op.DUP2, 0x20) + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x170b, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DUP2)))
        + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x1980), Op.MUL(0x20, Op.DUP1))))
        + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x16ea) + Op.JUMPDEST
        + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.AND(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x1980), Op.MUL(0x20, Op.DUP2))), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20))))))
        + Op.POP + Op.POP + Op.POP + Op.POP + Op.MSTORE(offset=0x1a40, value=0x1)
        + Op.RETURN(offset=0x1a40, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x17ff, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xa1fa51f9)))
        + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE
        + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE)
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0x1a60, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x44)))
        + Op.POP + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE
        + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x7)
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3
        + Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x1a60), 0x20)))
        + Op.DIV(Op.DUP2, 0x20) + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x17d1, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DUP2)))
        + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x1a60), Op.MUL(0x20, Op.DUP1))))
        + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x17b0) + Op.JUMPDEST
        + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.AND(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x1a60), Op.MUL(0x20, Op.DUP2))), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20))))))
        + Op.POP + Op.POP + Op.POP + Op.POP + Op.MSTORE(offset=0x1b20, value=0x1)
        + Op.RETURN(offset=0x1b20, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x18c5, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xcd87f43a)))
        + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE
        + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE)
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0x1b40, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x44)))
        + Op.POP + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE
        + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x8)
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3
        + Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x1b40), 0x20)))
        + Op.DIV(Op.DUP2, 0x20) + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x1897, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DUP2)))
        + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x1b40), Op.MUL(0x20, Op.DUP1))))
        + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x1876) + Op.JUMPDEST
        + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.AND(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x1b40), Op.MUL(0x20, Op.DUP2))), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20))))))
        + Op.POP + Op.POP + Op.POP + Op.POP + Op.MSTORE(offset=0x1c00, value=0x1)
        + Op.RETURN(offset=0x1c00, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x198b, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x222a8663)))
        + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE
        + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE)
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0x1c20, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x44)))
        + Op.POP + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE
        + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x9)
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3
        + Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x1c20), 0x20)))
        + Op.DIV(Op.DUP2, 0x20) + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x195d, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DUP2)))
        + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x1c20), Op.MUL(0x20, Op.DUP1))))
        + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x193c) + Op.JUMPDEST
        + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.AND(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x1c20), Op.MUL(0x20, Op.DUP2))), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20))))))
        + Op.POP + Op.POP + Op.POP + Op.POP + Op.MSTORE(offset=0x1ce0, value=0x1)
        + Op.RETURN(offset=0x1ce0, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x1a51, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xb39e1faa)))
        + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE
        + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE)
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0x1d00, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x44)))
        + Op.POP + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE
        + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0xa)
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3
        + Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x1d00), 0x20)))
        + Op.DIV(Op.DUP2, 0x20) + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x1a23, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DUP2)))
        + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x1d00), Op.MUL(0x20, Op.DUP1))))
        + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x1a02) + Op.JUMPDEST
        + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.AND(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x1d00), Op.MUL(0x20, Op.DUP2))), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20))))))
        + Op.POP + Op.POP + Op.POP + Op.POP + Op.MSTORE(offset=0x1dc0, value=0x1)
        + Op.RETURN(offset=0x1dc0, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x1b17, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xe365736b)))
        + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE
        + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE)
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0x1de0, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x44)))
        + Op.POP + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE
        + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0xb)
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3
        + Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x1de0), 0x20)))
        + Op.DIV(Op.DUP2, 0x20) + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x1ae9, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DUP2)))
        + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x1de0), Op.MUL(0x20, Op.DUP1))))
        + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x1ac8) + Op.JUMPDEST
        + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.AND(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x1de0), Op.MUL(0x20, Op.DUP2))), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20))))))
        + Op.POP + Op.POP + Op.POP + Op.POP + Op.MSTORE(offset=0x1ea0, value=0x1)
        + Op.RETURN(offset=0x1ea0, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x1b73, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xaad7d6e3)))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0x1ec0, value=Op.CALLDATALOAD(offset=0x44))
        + Op.MLOAD(offset=0x1ec0) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0xc) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.MSTORE(offset=0x1f00, value=0x1)
        + Op.RETURN(offset=0x1f00, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x1c39, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x1112b27)))
        + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE
        + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE)
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0x1f20, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x44)))
        + Op.POP + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE
        + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0xd)
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3
        + Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x1f20), 0x20)))
        + Op.DIV(Op.DUP2, 0x20) + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x1c0b, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DUP2)))
        + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x1f20), Op.MUL(0x20, Op.DUP1))))
        + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x1bea) + Op.JUMPDEST
        + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.AND(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x1f20), Op.MUL(0x20, Op.DUP2))), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20))))))
        + Op.POP + Op.POP + Op.POP + Op.POP + Op.MSTORE(offset=0x1fe0, value=0x1)
        + Op.RETURN(offset=0x1fe0, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x1cff, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xbdbb239b)))
        + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE
        + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE)
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0x2000, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x44)))
        + Op.POP + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE
        + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0xe)
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3
        + Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x2000), 0x20)))
        + Op.DIV(Op.DUP2, 0x20) + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x1cd1, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DUP2)))
        + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x2000), Op.MUL(0x20, Op.DUP1))))
        + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x1cb0) + Op.JUMPDEST
        + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.AND(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x2000), Op.MUL(0x20, Op.DUP2))), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20))))))
        + Op.POP + Op.POP + Op.POP + Op.POP + Op.MSTORE(offset=0x20c0, value=0x1)
        + Op.RETURN(offset=0x20c0, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x1dc5, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x5a0cd48)))
        + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE
        + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE)
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0x20e0, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x44)))
        + Op.POP + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE
        + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0xf)
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3
        + Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x20e0), 0x20)))
        + Op.DIV(Op.DUP2, 0x20) + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x1d97, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DUP2)))
        + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x20e0), Op.MUL(0x20, Op.DUP1))))
        + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x1d76) + Op.JUMPDEST
        + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.AND(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x20e0), Op.MUL(0x20, Op.DUP2))), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20))))))
        + Op.POP + Op.POP + Op.POP + Op.POP + Op.MSTORE(offset=0x21a0, value=0x1)
        + Op.RETURN(offset=0x21a0, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x1e8b, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xaaa1fe35)))
        + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE
        + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE)
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0x21c0, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x44)))
        + Op.POP + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE
        + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x10)
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3
        + Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x21c0), 0x20)))
        + Op.DIV(Op.DUP2, 0x20) + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x1e5d, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DUP2)))
        + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x21c0), Op.MUL(0x20, Op.DUP1))))
        + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x1e3c) + Op.JUMPDEST
        + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.AND(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x21c0), Op.MUL(0x20, Op.DUP2))), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20))))))
        + Op.POP + Op.POP + Op.POP + Op.POP + Op.MSTORE(offset=0x2280, value=0x1)
        + Op.RETURN(offset=0x2280, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x1f51, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x2be4935d)))
        + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE
        + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE)
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0x22a0, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x44)))
        + Op.POP + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE
        + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x11)
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3
        + Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x22a0), 0x20)))
        + Op.DIV(Op.DUP2, 0x20) + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x1f23, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DUP2)))
        + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x22a0), Op.MUL(0x20, Op.DUP1))))
        + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x1f02) + Op.JUMPDEST
        + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.AND(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x22a0), Op.MUL(0x20, Op.DUP2))), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20))))))
        + Op.POP + Op.POP + Op.POP + Op.POP + Op.MSTORE(offset=0x2360, value=0x1)
        + Op.RETURN(offset=0x2360, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x2017, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x13a8350d)))
        + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE
        + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE)
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0x2380, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x44)))
        + Op.POP + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE
        + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x12)
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3
        + Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x2380), 0x20)))
        + Op.DIV(Op.DUP2, 0x20) + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x1fe9, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DUP2)))
        + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x2380), Op.MUL(0x20, Op.DUP1))))
        + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x1fc8) + Op.JUMPDEST
        + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.AND(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x2380), Op.MUL(0x20, Op.DUP2))), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20))))))
        + Op.POP + Op.POP + Op.POP + Op.POP + Op.MSTORE(offset=0x2440, value=0x1)
        + Op.RETURN(offset=0x2440, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x20dd, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xcb540b45)))
        + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE
        + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE)
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0x2460, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x44)))
        + Op.POP + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE
        + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x13)
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3
        + Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x2460), 0x20)))
        + Op.DIV(Op.DUP2, 0x20) + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x20af, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DUP2)))
        + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x2460), Op.MUL(0x20, Op.DUP1))))
        + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x208e) + Op.JUMPDEST
        + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.AND(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x2460), Op.MUL(0x20, Op.DUP2))), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20))))))
        + Op.POP + Op.POP + Op.POP + Op.POP + Op.MSTORE(offset=0x2520, value=0x1)
        + Op.RETURN(offset=0x2520, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x21a3, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xbe030627)))
        + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE
        + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE)
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0x2540, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x44)))
        + Op.POP + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE
        + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x14)
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3
        + Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x2540), 0x20)))
        + Op.DIV(Op.DUP2, 0x20) + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x2175, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DUP2)))
        + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x2540), Op.MUL(0x20, Op.DUP1))))
        + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x2154) + Op.JUMPDEST
        + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.AND(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x2540), Op.MUL(0x20, Op.DUP2))), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20))))))
        + Op.POP + Op.POP + Op.POP + Op.POP + Op.MSTORE(offset=0x2600, value=0x1)
        + Op.RETURN(offset=0x2600, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x2269, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x83fd77f0)))
        + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE
        + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE)
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0x2620, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x44)))
        + Op.POP + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE
        + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x15)
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3
        + Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x2620), 0x20)))
        + Op.DIV(Op.DUP2, 0x20) + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x223b, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DUP2)))
        + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x2620), Op.MUL(0x20, Op.DUP1))))
        + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x221a) + Op.JUMPDEST
        + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.AND(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x2620), Op.MUL(0x20, Op.DUP2))), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20))))))
        + Op.POP + Op.POP + Op.POP + Op.POP + Op.MSTORE(offset=0x26e0, value=0x1)
        + Op.RETURN(offset=0x26e0, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x22d5, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x59462205)))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0x3c0, value=Op.CALLDATALOAD(offset=0x44))
        + Op.MSTORE(offset=0x2700, value=Op.CALLDATALOAD(offset=0x64))
        + Op.MLOAD(offset=0x2700) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x4)
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=Op.MLOAD(offset=0x3c0))
        + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE
        + Op.MSTORE(offset=0x2740, value=0x1) + Op.RETURN(offset=0x2740, size=0x20)
        + Op.JUMPDEST
        + Op.JUMPI(pc=0x2448, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xbb8e4196)))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x2760, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0x2780, value=Op.CALLDATALOAD(offset=0x44))
        + Op.MSTORE(offset=0x27a0, value=0x0) + Op.JUMPDEST + Op.PUSH1[0x80]
        + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.SUB(Op.MLOAD(offset=0x2760), 0x1))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP
        + Op.JUMPI(pc=0x243b, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x27a0), Op.SLOAD(key=Op.SHA3))))
        + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.SUB(Op.MLOAD(offset=0x2760), 0x1))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x1)
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=Op.MLOAD(offset=0x27a0))
        + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.PUSH1[0xa0]
        + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x2780))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x1) + Op.PUSH1[0x80]
        + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x2780))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=Op.SLOAD(key=Op.SHA3))
        + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.PUSH1[0x1]
        + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x2780))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.ADD + Op.PUSH1[0x80] + Op.PUSH1[0x80]
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x2780))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE
        + Op.MSTORE(offset=0x27a0, value=Op.ADD(Op.MLOAD(offset=0x27a0), 0x1))
        + Op.JUMP(pc=0x22fc) + Op.JUMPDEST + Op.MSTORE(offset=0x2880, value=0x1)
        + Op.RETURN(offset=0x2880, size=0x20) + Op.JUMPDEST + Op.POP
    ),
        storage={0x65d5efdfcc0fba693dc9e467f633097ffdc97401901463ad0e28855486d1edf: 0xb9d69098a6acfe0c6411bcaaf430f78d363a9adc32b78bc2e15ccd6e883e9784, 0x12643ff300762717d27efb567b82c65560d7b43249d908504e5510863ab82aac: 0x154cf60e137c594516a065149610b6a3989396a42581d5fd8919e711c55da225, 0x1489023d18c5d10427c4aa8dc726e840eb5ae7f604a8e9243c61634fb009e4d7: 0x5, 0x1489023d18c5d10427c4aa8dc726e840eb5ae7f604a8e9243c61634fb009e4d8: 0x1, 0x19efb13d6576359514ace5211988a8d51379fa88ccd2b886b409f842b13d7932: 0xc849cc595b452d11c206d2eb8cdfa06de211e3ff19ee0e0276dc857c05d4fe, 0x1b37e91bf8580c7c6bcf8cdff25c7ed78180124a94af6f30c40d476a3d079ad6: 0xaba4cd295118a482a0a62579e35e4ba5bdd76146cc9e4d96172fce8be8977ab4, 0x2bf9fd8facdd6fd9c84657f5ad7381a5aecf670cda68cb3c5829b6532c865506: 0x53098a1d111586dbcc0d051846284f5803c63c313e7f7e6d84430435d11d4c50, 0x3111bfd25728c0adfad0f8c1ad79cb1b91167267deca98de88f156ed25caeedc: 0xad393086f30b49511b08fdd27ac78810b084c7cd7de6ac354f614c18ea9e7df4, 0x3379e7ae125c5c5d623d1d993c1459b61d6723b1c30d1aa026c48f6a6155b8ea: 0x8c4183732567a99a8a718e363391e102532f9a640e42968cf2354d9acc908bb0, 0x34cabe0c7e64a2caa93fd8d6a0defc07acb9d44b13430fa3ae9282fffd40dee2: 0x1, 0x34cabe0c7e64a2caa93fd8d6a0defc07acb9d44b13430fa3ae9282fffd40dee3: 0x1, 0x34cabe0c7e64a2caa93fd8d6a0defc07acb9d44b13430fa3ae9282fffd40dee4: 0x1, 0x34cabe0c7e64a2caa93fd8d6a0defc07acb9d44b13430fa3ae9282fffd40dee5: 0x1, 0x39050607fe892059a6344ab0f594f382fb0b345cab373497246dbe86fe7e14e7: 0x2b3bca833e482737e7e47b1568e6f890f8e1666490d38fe130abd6f0ccb109cf, 0x417be8bc6791807372e0222a350bb8a5d67bbc8d7595c301d8a5a8372cfdcef1: 0xabd4971b4605a7155802f70e08298b1ceb0e4e4eaccccd348f77a77227f73a7f, 0x41e9a54b3ee0c276aa076babb161de12b0f8916b47f8f6fb85cc387cf34696dd: 0x22f2f444ebda9d2913ffef5059b039ec9b5876aa71821991c2515bf79f64935e, 0x45ceb8da6fb8936592d3bce4883f1a6a34d636f559e0a1070a5802a65ac39bd5: 0x57a5122ff3bf737b0de0f9f08011a8648c19e43ff071fb7086234723c9383f1f, 0x4aa6b934608a45c8f53a945c05ddee1814a3b9f63a048fc7ad3d47e67156f024: 0xd03862becedada67b4825a0238f3e67495ccb595cd7d08f1bd5d3160644b9299, 0x4b8b58f0b0e326a5907d1a810e5ff31e05b4cab45125b776db8577e7dbc46bce: 0x2f0000000000000000, 0x4c33460347337bfc7df08bf182988301b7b426a27a67f1c6c634f637c60e87ac: 0xbab4ab2ad4eafe7c84ef6a8cd69157d9ce6b843793a2cd0877b8e91f63cb2d4d, 0x58da0c0c256bba101ce36fad8bf838717a57e6ab850a191dc9c09da9ce56bf1b: 0x5, 0x5cb38b16db1d632086d4af695de7f5f242a6e40947067f96edd566fe2ac438ef: 0x6d0be832b2007ea28cda705b73922cbf9794c5a25b89bd2f28b7347ed2b96c86, 0x64a9621cc4ba92bf738c55010c609dfaa3972a1138c30b5adcef1ba2363b360e: 0xd7953bfe8cb591f129fd0862a9e9c421151e2b5831560ff5215d23f751364b35, 0x696664a5f0ab5acd9304a377fb684f2d3fe6bb60b8a95cb2bdbb57db767e7a84: 0x154cf60e137c594516a065149610b6a3989396a42581d5fd8919e711c55da225, 0x69ad1d19e617936abdf05133bf268dc8ced6b518f22b249b5860967d07006487: 0x8c803b48b383ddabd1b3afe858efb48c203229b7317dd76149dddab4253b858a, 0x70b3bf53996fac325eb67608a4eeb0cd0b55def6255d7ed42ad28ec07238b5d6: 0x45e9723e9232b37207ecac1c97b8647d053625a578d450f7456280b2ff8efc27, 0x7a9dcee62e3e02cc8e020f372df2efdeb835f091c1ef1dbe221072d1095aabd2: 0x2f0000000000000000, 0x7e4d8c0f6d8abb4ce1ae45b254046aceedabfa9548851b8b5d3e2c0637c985fd: 0xb, 0x7e95f3cc3315d289c52253baaba29b1b00c86816e6b788d50795279a8baa00db: 0x45e9723e9232b37207ecac1c97b8647d053625a578d450f7456280b2ff8efc27, 0x8da187157087529ee4e9c381f8e3149c56acf3bdfda29b8b9b4532f24b83f5fe: 0x8c4183732567a99a8a718e363391e102532f9a640e42968cf2354d9acc908bb0, 0x9001f91ddaef87bc067886e874c0749998c9b58b2ec8472ca014ca8b55f88578: 0xfb76974eefca01f33fb38646c2d3c1536f1a763d7aff53ab7f877d4c5ea7fd0, 0x9ed0cedd2a9a78d949f40019f53d10031aef6ed342c97e01fc03b481ee56b3cb: 0x4, 0x9fddf1db29caa5c1239edd86e9e0835cdfe41f7253ec78f62d3da8558d6f3cd7: 0x104eef8fa35bf39f677d81855bc0b9f42317f32792e98e95e4df441deb634211, 0xa0953566119395c11186b334805fc1a16175ecac0ecc93ae0322264f0dc2e40d: 0x10c5a00466ab7c0adae1e93537cc275ea8cf23ff509d5466a1fd6f56b0a61d1b, 0xaa0dbf8241ef3ae07c254e6869e84895ba2be0779a7f261c8308a3114be1c54a: 0x4, 0xaffe808b495d13a14391ce5f27c211c36da12826969cd7841ee0d81e5b900e2d: 0x1, 0xaffe808b495d13a14391ce5f27c211c36da12826969cd7841ee0d81e5b900e2e: 0x1, 0xb4a2b68c48ef78aeb641ee538fad51781022fd23ed9d93d211017db6a02376ce: 0xfbc06642245cf2fed7ed46ea0a18a7185830b6f2c4e0a4ca55246041e8bfa72, 0xba8d79990898383919e437f2458b93b340072c89d963808d9e04f51858e3c5ec: 0x41d2cac534d90a0dbd199117481a63e32cc11411dab2eaa36c91c0eec62823cf, 0xbb3bc1a2015123750df57d4ceff7e28cb847910b79b34841de905b59a8bb177c: 0x734417eb19e1873427257f1ea1594748c16cfa866a7b7cf896e281f2ec774a40, 0xbf30cdcb83ab2bd5f5eee691ffa4107b58b75ba6a5c2e6754d4c5c0437f2876c: 0x5, 0xc2a26b80067fc36b8268b0d5b31afff953fa91cebea39f191e2763d6e71259b9: 0x2a43c547fe8de2400d2a141016550e8bae058d41164247c099e787ddd40e789, 0xc98339d275eef16e0562ca8521212cef61aa0f39b12e2a27502aaa97a9e5e70f: 0x5a3de2a5c268cdb75f4b01507aa80c4e4a1bc67bcb0df265bbb00060774e5978, 0xcbd6ae6bd61bc9270ec836f1919b3268113abe076c7febfdb8cf573b199ce9a9: 0xf402b17773c1f7534034ee58dc0d2a3421470a7a67daf4fa790dc3b420eef790, 0xd2c8cbb562fccd0c9a3d0d491b7f65cc6a89856498f933427d9d21b745b9d50e: 0x3625a26fdb7b747501f1ee2500f98c49d9cd290383a21254587c3c49d2805321, 0xd66f52a4e24585238ccc03443b2fdb8b2b100259bc7260f39097c7c339211ffe: 0x1641851904381915c86b60df7e288896fb5f8ebad65d594829fb9f2b59cd1da6, 0xd8f720c05a5526dd621d1831ae122abddd3dfecd8b63b0ba4c92fa7b2ade44ff: 0xad393086f30b49511b08fdd27ac78810b084c7cd7de6ac354f614c18ea9e7df4, 0xdc22d3171b82817c910bbeac1f8b50c8de99f8c524f172aef3491981bd5ed4fb: 0x94b8cba4ea090d1c392fbc94b82fb9ef9f468a15bbc537f4d051776f4d422b1d, 0xdce8adbdefa929dbe60245f359446db4174c62824b42e5d4d9e7b834b4d61deb: 0x2c9069845b2e74c577ff1cd18df6bc452805f527a9ee91fd4a059e0408b5dea6, 0xdd9493073db9e42fd955e834c89a74089f99196186ee0b2688124989be00d196: 0x1, 0xdd9493073db9e42fd955e834c89a74089f99196186ee0b2688124989be00d197: 0x1, 0xdd9493073db9e42fd955e834c89a74089f99196186ee0b2688124989be00d198: 0x1, 0xdd9493073db9e42fd955e834c89a74089f99196186ee0b2688124989be00d199: 0x1, 0xdd9493073db9e42fd955e834c89a74089f99196186ee0b2688124989be00d19a: 0x1, 0xe54f074c81bfa60b5bf413934c108086298b77291560edfeead8aa1232e95236: 0xf40aaa24323c9e6983ccffafeebe4b426509b901e8c98b8a40d881804804e6b, 0xe66c0f55f66c752edf73027d45b7b1ae729ae15e1c67c362dbc6f25edf8d76ff: 0x1, 0xe983d899f807bbcb5881f2ddf875b2ebb5cb8a7a4e77a8c98a40aaae6a468735: 0x6d0be832b2007ea28cda705b73922cbf9794c5a25b89bd2f28b7347ed2b96c86, 0xed7d6e2d40fbd5046412ffad1c45b63d87c6197182d6dbc66bb1e5c6e4ded5c7: 0xaba4cd295118a482a0a62579e35e4ba5bdd76146cc9e4d96172fce8be8977ab4, 0xf043b5a1952847579f233706a8f130889a484d2da3e574fdd5859f05aaf52111: 0x2, 0xf40f4cfdacb62dd799f36b580349fac1f4a4caf8dd3383cc387c35adb6574e21: 0x2f0000000000000000, 0xf60fa6e25e9028a6dc6b26bbc1eadae3da157df0d1d6f6628bc33cad68a7e455: 0x2d7d00618c059ebe40593b9497c633e1ac6e161dadbd5bb734c2663cd3e8a8e1, 0xfd280ac5182d5b2366122f38acfa6dc471240ffde9d5feb985ce7a2325c960e7: 0x3},
    )
    pre[callee_6] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.MSTORE8(offset=0x31f, value=0x0)
        + Op.DIV(Op.CALLDATALOAD(offset=0x0), 0x100000000000000000000000000000000000000000000000000000000)
        + Op.MSTORE(offset=0x20, value=0xc9ae5868651bf7b7db6e360217db49ce4e69c07e)
        + Op.MSTORE(offset=0x40, value=0xea65418d7bf32680f55572c943a94b590804998)
        + Op.JUMPI(pc=0x38d, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x27138bfb)))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x4)) + Op.PUSH1[0x1c]
        + Op.PUSH1[0x44] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x7a66d7ca)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x80))
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP4, args_size=0x24, ret_offset=0xe0, ret_size=0x20))
        + Op.MLOAD(offset=0xe0) + Op.SWAP1 + Op.POP + Op.PUSH1[0xa0] + Op.MSTORE
        + Op.PUSH1[0x1c] + Op.PUSH1[0x44] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xc60409c6)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x80))
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP4, args_size=0x24, ret_offset=0x120, ret_size=0x20))
        + Op.MLOAD(offset=0x120) + Op.SWAP1 + Op.POP + Op.NUMBER
        + Op.MSTORE(offset=0x100, value=Op.SDIV) + Op.MSTORE(offset=0x140, value=0x0)
        + Op.MSTORE(offset=0x160, value=0x0) + Op.MSTORE(offset=0x180, value=0x0)
        + Op.JUMPI(pc=0x10a, condition=Op.ISZERO(Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x100), Op.ADD(Op.MLOAD(offset=0xa0), 0x2)))))
        + Op.MSTORE(offset=0x140, value=0x1) + Op.JUMPDEST
        + Op.MSTORE(offset=0x1a0, value=0x0)
        + Op.MSTORE(offset=0x1c0, value=Op.MLOAD(offset=0x100)) + Op.JUMPDEST
        + Op.JUMPI(pc=0x184, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x1c0), Op.ADD(Op.MLOAD(offset=0x100), 0x64))))
        + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xcc1c944e)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0x1c0))
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x40), value=0x0, args_offset=Op.DUP4, args_size=0x44, ret_offset=0x1e0, ret_size=0x20))
        + Op.MLOAD(offset=0x1e0) + Op.SWAP1 + Op.POP + Op.MLOAD(offset=0x1a0)
        + Op.MSTORE(offset=0x1a0, value=Op.ADD)
        + Op.MSTORE(offset=0x1c0, value=Op.ADD(Op.MLOAD(offset=0x1c0), 0x1))
        + Op.JUMP(pc=0x119) + Op.JUMPDEST + Op.PUSH1[0x5] + Op.PUSH1[0x1c]
        + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xcc1c944e)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0xa0))
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x40), value=0x0, args_offset=Op.DUP4, args_size=0x44, ret_offset=0x200, ret_size=0x20))
        + Op.MLOAD(offset=0x200) + Op.SWAP1 + Op.POP + Op.SLT
        + Op.JUMPI(pc=0x1d3, condition=Op.ISZERO(Op.DUP1)) + Op.DUP1
        + Op.JUMP(pc=0x1db) + Op.JUMPDEST + Op.SLT(Op.MLOAD(offset=0x1a0), 0xa)
        + Op.JUMPDEST + Op.SWAP1 + Op.POP + Op.JUMPI(pc=0x1eb, condition=Op.ISZERO)
        + Op.MLOAD(offset=0x140) + Op.JUMP(pc=0x1ee) + Op.JUMPDEST + Op.PUSH1[0x0]
        + Op.JUMPDEST + Op.JUMPI(pc=0x336, condition=Op.ISZERO) + Op.PUSH1[0x1c]
        + Op.PUSH1[0x44] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xc5476efe)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x80))
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP4, args_size=0x24, ret_offset=0x240, ret_size=0x20))
        + Op.MLOAD(offset=0x240) + Op.SWAP1 + Op.POP + Op.POP + Op.PUSH1[0x1c]
        + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x7265802d)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=0x0)
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP4, args_size=0x44, ret_offset=0x260, ret_size=0x20))
        + Op.MLOAD(offset=0x260) + Op.SWAP1 + Op.POP + Op.POP + Op.PUSH1[0x1c]
        + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xc286273a)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=0x0)
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP4, args_size=0x44, ret_offset=0x280, ret_size=0x20))
        + Op.MLOAD(offset=0x280) + Op.SWAP1 + Op.POP + Op.POP + Op.PUSH1[0x1c]
        + Op.PUSH1[0x44] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x7a66d7ca)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x80))
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP4, args_size=0x24, ret_offset=0x2a0, ret_size=0x20))
        + Op.MLOAD(offset=0x2a0) + Op.SWAP1 + Op.POP + Op.PUSH1[0xa0] + Op.MSTORE
        + Op.PUSH1[0x1c] + Op.PUSH1[0x84] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xbb8e4196)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0xa0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=Op.MLOAD(offset=0x100))
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x40), value=0x0, args_offset=Op.DUP4, args_size=0x64, ret_offset=0x2c0, ret_size=0x20))
        + Op.MLOAD(offset=0x2c0) + Op.SWAP1 + Op.POP + Op.POP + Op.JUMP(pc=0x343)
        + Op.JUMPDEST + Op.MSTORE(offset=0x160, value=0x1)
        + Op.MSTORE(offset=0x180, value=0x1) + Op.JUMPDEST
        + Op.JUMPI(pc=0x355, condition=Op.ISZERO(Op.MLOAD(offset=0x140)))
        + Op.MLOAD(offset=0x160) + Op.JUMP(pc=0x358) + Op.JUMPDEST + Op.PUSH1[0x0]
        + Op.JUMPDEST + Op.JUMPI(pc=0x366, condition=Op.ISZERO)
        + Op.MLOAD(offset=0x180) + Op.JUMP(pc=0x369) + Op.JUMPDEST + Op.PUSH1[0x0]
        + Op.JUMPDEST + Op.JUMPI(pc=0x37f, condition=Op.ISZERO)
        + Op.MSTORE(offset=0x2e0, value=0x1) + Op.RETURN(offset=0x2e0, size=0x20)
        + Op.JUMP(pc=0x38c) + Op.JUMPDEST + Op.MSTORE(offset=0x300, value=0x0)
        + Op.RETURN(offset=0x300, size=0x20) + Op.JUMPDEST + Op.JUMPDEST + Op.POP
    ),
    )
    pre[coinbase] = Account(balance=1, nonce=0)
    pre[callee_7] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.MSTORE8(offset=0x5df, value=0x0)
        + Op.DIV(Op.CALLDATALOAD(offset=0x0), 0x100000000000000000000000000000000000000000000000000000000)
        + Op.MSTORE(offset=0x20, value=0xea65418d7bf32680f55572c943a94b590804998)
        + Op.MSTORE(offset=0x40, value=0xe509e3a93beb1eba72f8cb8d25f93a85e2d54afb)
        + Op.MSTORE(offset=0x60, value=0xc9ae5868651bf7b7db6e360217db49ce4e69c07e)
        + Op.MSTORE(offset=0x80, value=0xf1562e1c0d0baa3ea746442bb7f11153fcf5cfda)
        + Op.JUMPI(pc=0x38d, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x546fdeb3)))
        + Op.MSTORE(offset=0xc0, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0xe0, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0x100, value=Op.CALLDATALOAD(offset=0x44))
        + Op.MSTORE(offset=0x120, value=Op.CALLDATALOAD(offset=0x64))
        + Op.MSTORE(offset=0x140, value=Op.CALLDATALOAD(offset=0x84))
        + Op.ADD(Op.MLOAD(offset=0x100), 0x2) + Op.PUSH1[0x1c] + Op.PUSH1[0x64]
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xe05dcb56)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0xc0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0xe0))
        + Op.ADD(Op.MLOAD(offset=0x100), 0x2) + Op.ADD(Op.MUL(0x20, Op.DUP2), 0x40)
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP6, args_size=0x44, ret_offset=Op.DUP2, ret_size=Op.ADD(0x40, Op.MUL(0x20, Op.DUP2))))
        + Op.ADD(Op.DUP2, 0x40) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1
        + Op.POP
        + Op.JUMPI(pc=0x250, condition=Op.ISZERO(Op.EQ(Op.MLOAD(offset=Op.ADD(Op.DUP3, Op.MUL(0x20, Op.ADD(Op.MLOAD(offset=0x100), 0x1)))), 0x0)))
        + Op.PUSH1[0x60] + Op.PUSH1[0x1c] + Op.PUSH2[0x14c] + Op.MSIZE + Op.SWAP1
        + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xe365736b)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0xc0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0xe0))
        + Op.PUSH1[0x1c] + Op.PUSH1[0x84] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x2f300bee)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=0x2)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=0x5)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=Op.MLOAD(offset=0x100))
        + Op.DUP5 + Op.ADD(Op.MUL(0x20, Op.DUP2), 0x40) + Op.MSIZE + Op.SWAP1
        + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x80), value=0x0, args_offset=Op.DUP6, args_size=0x64, ret_offset=Op.DUP2, ret_size=Op.ADD(0x40, Op.MUL(0x20, Op.DUP2))))
        + Op.ADD(Op.DUP2, 0x40) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1
        + Op.POP + Op.ADD(0x20, Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.DUP2, 0x20))))
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x44), value=Op.DUP4)
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0xa4), value=Op.SUB(Op.DUP3, 0x20))
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x108), value=Op.DUP1)
        + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.POP
        + Op.ADD(0x4, Op.DUP2) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.JUMPI(pc=0x1fc, condition=Op.CALL(gas=0x1c, address=0x4, value=0x0, args_offset=Op.DUP5, args_size=0x64, ret_offset=Op.DUP2, ret_size=0x64))
        + Op.INVALID + Op.JUMPDEST + Op.ADD(Op.DUP2, 0x64) + Op.SWAP3 + Op.POP
        + Op.MLOAD(offset=Op.ADD(Op.DUP3, 0x108)) + Op.DUP1
        + Op.JUMPI(pc=0x223, condition=Op.CALL(gas=Op.ADD(0x12, Op.SDIV(Op.DUP8, 0xa)), address=0x4, value=0x0, args_offset=Op.MLOAD(offset=Op.ADD(Op.DUP8, 0xa4)), args_size=Op.DUP3, ret_offset=Op.DUP6, ret_size=Op.DUP1))
        + Op.INVALID + Op.JUMPDEST + Op.POP + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4
        + Op.POP + Op.POP + Op.SUB(Op.DUP4, Op.DUP1)
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP5, args_size=Op.DUP3, ret_offset=0x280, ret_size=0x20))
        + Op.MLOAD(offset=0x280) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1
        + Op.POP + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x37d) + Op.JUMPDEST
        + Op.PUSH1[0x60] + Op.PUSH1[0x1c] + Op.PUSH2[0x14c] + Op.MSIZE + Op.SWAP1
        + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xe365736b)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0xc0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0xe0))
        + Op.PUSH1[0x1c] + Op.PUSH1[0x84] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x2f300bee)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.SUB(Op.MLOAD(offset=Op.ADD(Op.DUP6, Op.MUL(0x20, Op.ADD(Op.MLOAD(offset=0x100), 0x1)))), 0x1))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=0x5)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=Op.MLOAD(offset=0x100))
        + Op.DUP5 + Op.ADD(Op.MUL(0x20, Op.DUP2), 0x40) + Op.MSIZE + Op.SWAP1
        + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x80), value=0x0, args_offset=Op.DUP6, args_size=0x64, ret_offset=Op.DUP2, ret_size=Op.ADD(0x40, Op.MUL(0x20, Op.DUP2))))
        + Op.ADD(Op.DUP2, 0x40) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1
        + Op.POP + Op.ADD(0x20, Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.DUP2, 0x20))))
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x44), value=Op.DUP4)
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0xa4), value=Op.SUB(Op.DUP3, 0x20))
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x108), value=Op.DUP1)
        + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.POP
        + Op.ADD(0x4, Op.DUP2) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.JUMPI(pc=0x32d, condition=Op.CALL(gas=0x1c, address=0x4, value=0x0, args_offset=Op.DUP5, args_size=0x64, ret_offset=Op.DUP2, ret_size=0x64))
        + Op.INVALID + Op.JUMPDEST + Op.ADD(Op.DUP2, 0x64) + Op.SWAP3 + Op.POP
        + Op.MLOAD(offset=Op.ADD(Op.DUP3, 0x108)) + Op.DUP1
        + Op.JUMPI(pc=0x354, condition=Op.CALL(gas=Op.ADD(0x12, Op.SDIV(Op.DUP8, 0xa)), address=0x4, value=0x0, args_offset=Op.MLOAD(offset=Op.ADD(Op.DUP8, 0xa4)), args_size=Op.DUP3, ret_offset=Op.DUP6, ret_size=Op.DUP1))
        + Op.INVALID + Op.JUMPDEST + Op.POP + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4
        + Op.POP + Op.POP + Op.SUB(Op.DUP4, Op.DUP1)
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP5, args_size=Op.DUP3, ret_offset=0x2c0, ret_size=0x20))
        + Op.MLOAD(offset=0x2c0) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1
        + Op.POP + Op.SWAP1 + Op.POP + Op.JUMPDEST + Op.POP
        + Op.MSTORE(offset=0x2e0, value=0x1) + Op.RETURN(offset=0x2e0, size=0x20)
        + Op.POP + Op.POP + Op.JUMPDEST
        + Op.JUMPI(pc=0x764, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xde9080c8)))
        + Op.MSTORE(offset=0xc0, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0xe0, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0x100, value=Op.CALLDATALOAD(offset=0x44))
        + Op.MSTORE(offset=0x120, value=Op.CALLDATALOAD(offset=0x64))
        + Op.MSTORE(offset=0x140, value=Op.CALLDATALOAD(offset=0x84))
        + Op.ADD(Op.MLOAD(offset=0x100), 0x2) + Op.PUSH1[0x1c] + Op.PUSH1[0x64]
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xe05dcb56)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0xc0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0xe0))
        + Op.DUP2 + Op.ADD(Op.MUL(0x20, Op.DUP2), 0x40) + Op.MSIZE + Op.SWAP1
        + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP6, args_size=0x44, ret_offset=Op.DUP2, ret_size=Op.ADD(0x40, Op.MUL(0x20, Op.DUP2))))
        + Op.ADD(Op.DUP2, 0x40) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1
        + Op.POP + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE
        + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x2c5a40d5)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0xc0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0xe0))
        + Op.MLOAD(offset=0x140) + Op.ADD(Op.MUL(0x20, Op.DUP2), 0x40) + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP6, args_size=0x44, ret_offset=Op.DUP2, ret_size=Op.ADD(0x40, Op.MUL(0x20, Op.DUP2))))
        + Op.ADD(Op.DUP2, 0x40) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1
        + Op.POP + Op.MLOAD(offset=0x120) + Op.ADD(0x20, Op.MUL(0x20, Op.DUP1))
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20)
        + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x4ee, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.MLOAD(offset=0x120))))
        + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x28c8b315)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0xc0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.DUP2)
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x40), value=0x0, args_offset=Op.DUP4, args_size=0x44, ret_offset=0x360, ret_size=0x20))
        + Op.MLOAD(offset=0x360) + Op.SWAP1 + Op.POP
        + Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)) + Op.MSTORE + Op.ADD(Op.DUP2, 0x1)
        + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x493) + Op.JUMPDEST + Op.POP
        + Op.PUSH1[0xa0] + Op.PUSH1[0x1c] + Op.PUSH2[0x20c] + Op.MSIZE + Op.SWAP1
        + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xa647a5b9) + Op.DUP5
        + Op.ADD(0x20, Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.DUP2, 0x20))))
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x4), value=Op.DUP4)
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0xa4), value=Op.SUB(Op.DUP3, 0x20))
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x148), value=Op.DUP1)
        + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.POP + Op.DUP4
        + Op.ADD(0x20, Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.DUP2, 0x20))))
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x24), value=Op.DUP4)
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0xc4), value=Op.SUB(Op.DUP3, 0x20))
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x168), value=Op.DUP1)
        + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.POP + Op.DUP3
        + Op.ADD(0x20, Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.DUP2, 0x20))))
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x44), value=Op.DUP4)
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0xe4), value=Op.SUB(Op.DUP3, 0x20))
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x188), value=Op.DUP1)
        + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.POP
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x64), value=Op.MLOAD(offset=0x120))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x84), value=Op.MLOAD(offset=0x100))
        + Op.ADD(0x4, Op.DUP2) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.JUMPI(pc=0x5b5, condition=Op.CALL(gas=0x22, address=0x4, value=0x0, args_offset=Op.DUP5, args_size=0xa4, ret_offset=Op.DUP2, ret_size=0xa4))
        + Op.INVALID + Op.JUMPDEST + Op.ADD(Op.DUP2, 0xa4) + Op.SWAP3 + Op.POP
        + Op.MLOAD(offset=Op.ADD(Op.DUP3, 0x148)) + Op.DUP1
        + Op.JUMPI(pc=0x5dc, condition=Op.CALL(gas=Op.ADD(0x12, Op.SDIV(Op.DUP8, 0xa)), address=0x4, value=0x0, args_offset=Op.MLOAD(offset=Op.ADD(Op.DUP8, 0xa4)), args_size=Op.DUP3, ret_offset=Op.DUP6, ret_size=Op.DUP1))
        + Op.INVALID + Op.JUMPDEST + Op.POP + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4
        + Op.POP + Op.POP + Op.MLOAD(offset=Op.ADD(Op.DUP3, 0x168)) + Op.DUP1
        + Op.JUMPI(pc=0x604, condition=Op.CALL(gas=Op.ADD(0x12, Op.SDIV(Op.DUP8, 0xa)), address=0x4, value=0x0, args_offset=Op.MLOAD(offset=Op.ADD(Op.DUP8, 0xc4)), args_size=Op.DUP3, ret_offset=Op.DUP6, ret_size=Op.DUP1))
        + Op.INVALID + Op.JUMPDEST + Op.POP + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4
        + Op.POP + Op.POP + Op.MLOAD(offset=Op.ADD(Op.DUP3, 0x188)) + Op.DUP1
        + Op.JUMPI(pc=0x62c, condition=Op.CALL(gas=Op.ADD(0x12, Op.SDIV(Op.DUP8, 0xa)), address=0x4, value=0x0, args_offset=Op.MLOAD(offset=Op.ADD(Op.DUP8, 0xe4)), args_size=Op.DUP3, ret_offset=Op.DUP6, ret_size=Op.DUP1))
        + Op.INVALID + Op.JUMPDEST + Op.POP + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4
        + Op.POP + Op.POP + Op.SUB(Op.DUP4, Op.DUP1) + Op.DUP8
        + Op.ADD(Op.MUL(0x20, Op.DUP2), 0x40) + Op.MSIZE + Op.SWAP1 + Op.MSIZE
        + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x80), value=0x0, args_offset=Op.DUP7, args_size=Op.DUP5, ret_offset=Op.DUP2, ret_size=Op.ADD(0x40, Op.MUL(0x20, Op.DUP2))))
        + Op.ADD(Op.DUP2, 0x40) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1
        + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP
        + Op.SWAP3 + Op.POP + Op.PUSH1[0x60] + Op.PUSH1[0x1c] + Op.PUSH2[0x14c]
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xe365736b)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0xc0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0xe0))
        + Op.DUP5 + Op.ADD(0x20, Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.DUP2, 0x20))))
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x44), value=Op.DUP4)
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0xa4), value=Op.SUB(Op.DUP3, 0x20))
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x108), value=Op.DUP1)
        + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.POP
        + Op.ADD(0x4, Op.DUP2) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.JUMPI(pc=0x6df, condition=Op.CALL(gas=0x1c, address=0x4, value=0x0, args_offset=Op.DUP5, args_size=0x64, ret_offset=Op.DUP2, ret_size=0x64))
        + Op.INVALID + Op.JUMPDEST + Op.ADD(Op.DUP2, 0x64) + Op.SWAP3 + Op.POP
        + Op.MLOAD(offset=Op.ADD(Op.DUP3, 0x108)) + Op.DUP1
        + Op.JUMPI(pc=0x706, condition=Op.CALL(gas=Op.ADD(0x12, Op.SDIV(Op.DUP8, 0xa)), address=0x4, value=0x0, args_offset=Op.MLOAD(offset=Op.ADD(Op.DUP8, 0xa4)), args_size=Op.DUP3, ret_offset=Op.DUP6, ret_size=Op.DUP1))
        + Op.INVALID + Op.JUMPDEST + Op.POP + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4
        + Op.POP + Op.POP + Op.SUB(Op.DUP4, Op.DUP1)
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP5, args_size=Op.DUP3, ret_offset=0x3c0, ret_size=0x20))
        + Op.MLOAD(offset=0x3c0) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1
        + Op.POP + Op.SWAP1 + Op.POP + Op.POP
        + Op.JUMPI(pc=0x752, condition=Op.ISZERO(Op.EQ(Op.MLOAD(offset=Op.ADD(Op.DUP5, Op.MUL(0x20, Op.MLOAD(offset=0x100)))), 0x0)))
        + Op.MSTORE(offset=0x3e0, value=0x0) + Op.RETURN(offset=0x3e0, size=0x20)
        + Op.JUMP(pc=0x75f) + Op.JUMPDEST + Op.MSTORE(offset=0x400, value=0x1)
        + Op.RETURN(offset=0x400, size=0x20) + Op.JUMPDEST + Op.POP + Op.POP + Op.POP
        + Op.POP + Op.JUMPDEST
        + Op.JUMPI(pc=0xa66, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x384ca8dd)))
        + Op.MSTORE(offset=0xc0, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0xe0, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0x100, value=Op.CALLDATALOAD(offset=0x44))
        + Op.MSTORE(offset=0x120, value=Op.CALLDATALOAD(offset=0x64))
        + Op.MSTORE(offset=0x140, value=Op.CALLDATALOAD(offset=0x84)) + Op.PUSH1[0x1c]
        + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xe05dcb56)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0xc0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0xe0))
        + Op.ADD(Op.MLOAD(offset=0x100), 0x2) + Op.ADD(Op.MUL(0x20, Op.DUP2), 0x40)
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP6, args_size=0x44, ret_offset=Op.DUP2, ret_size=Op.ADD(0x40, Op.MUL(0x20, Op.DUP2))))
        + Op.ADD(Op.DUP2, 0x40) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1
        + Op.POP + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE
        + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xfa9832d1)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0xc0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0xe0))
        + Op.MLOAD(offset=0x100) + Op.ADD(Op.MUL(0x20, Op.DUP2), 0x40) + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP6, args_size=0x44, ret_offset=Op.DUP2, ret_size=Op.ADD(0x40, Op.MUL(0x20, Op.DUP2))))
        + Op.ADD(Op.DUP2, 0x40) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1
        + Op.POP + Op.PUSH1[0x1c] + Op.PUSH1[0x84] + Op.MSIZE + Op.SWAP1 + Op.MSIZE
        + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xaad7d6e3)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0xc0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0xe0))
        + Op.PUSH1[0x60] + Op.PUSH1[0x1c] + Op.PUSH2[0x14c] + Op.MSIZE + Op.SWAP1
        + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x5b180229) + Op.DUP4
        + Op.ADD(0x20, Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.DUP2, 0x20))))
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x4), value=Op.DUP4)
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x64), value=Op.SUB(Op.DUP3, 0x20))
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0xc8), value=Op.DUP1)
        + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.POP + Op.DUP5
        + Op.ADD(0x20, Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.DUP2, 0x20))))
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x24), value=Op.DUP4)
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x84), value=Op.SUB(Op.DUP3, 0x20))
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0xe8), value=Op.DUP1)
        + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.POP
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=Op.MLOAD(offset=0x100))
        + Op.ADD(0x4, Op.DUP2) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.JUMPI(pc=0x901, condition=Op.CALL(gas=0x1c, address=0x4, value=0x0, args_offset=Op.DUP5, args_size=0x64, ret_offset=Op.DUP2, ret_size=0x64))
        + Op.INVALID + Op.JUMPDEST + Op.ADD(Op.DUP2, 0x64) + Op.SWAP3 + Op.POP
        + Op.MLOAD(offset=Op.ADD(Op.DUP3, 0xc8)) + Op.DUP1
        + Op.JUMPI(pc=0x927, condition=Op.CALL(gas=Op.ADD(0x12, Op.SDIV(Op.DUP8, 0xa)), address=0x4, value=0x0, args_offset=Op.MLOAD(offset=Op.ADD(Op.DUP8, 0x64)), args_size=Op.DUP3, ret_offset=Op.DUP6, ret_size=Op.DUP1))
        + Op.INVALID + Op.JUMPDEST + Op.POP + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4
        + Op.POP + Op.POP + Op.MLOAD(offset=Op.ADD(Op.DUP3, 0xe8)) + Op.DUP1
        + Op.JUMPI(pc=0x94e, condition=Op.CALL(gas=Op.ADD(0x12, Op.SDIV(Op.DUP8, 0xa)), address=0x4, value=0x0, args_offset=Op.MLOAD(offset=Op.ADD(Op.DUP8, 0x84)), args_size=Op.DUP3, ret_offset=Op.DUP6, ret_size=Op.DUP1))
        + Op.INVALID + Op.JUMPDEST + Op.POP + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4
        + Op.POP + Op.POP + Op.SUB(Op.DUP4, Op.DUP1)
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x80), value=0x0, args_offset=Op.DUP5, args_size=Op.DUP3, ret_offset=0x440, ret_size=0x20))
        + Op.MLOAD(offset=0x440) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1
        + Op.POP + Op.SWAP1 + Op.POP + Op.ADD(Op.DUP3, 0x44) + Op.MSTORE
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP4, args_size=0x64, ret_offset=0x460, ret_size=0x20))
        + Op.MLOAD(offset=0x460) + Op.SWAP1 + Op.POP + Op.POP + Op.PUSH1[0x60]
        + Op.PUSH1[0x1c] + Op.PUSH2[0x14c] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x222a8663)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0xc0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0xe0))
        + Op.DUP3 + Op.ADD(0x20, Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.DUP2, 0x20))))
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x44), value=Op.DUP4)
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0xa4), value=Op.SUB(Op.DUP3, 0x20))
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x108), value=Op.DUP1)
        + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.POP
        + Op.ADD(0x4, Op.DUP2) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.JUMPI(pc=0xa07, condition=Op.CALL(gas=0x1c, address=0x4, value=0x0, args_offset=Op.DUP5, args_size=0x64, ret_offset=Op.DUP2, ret_size=0x64))
        + Op.INVALID + Op.JUMPDEST + Op.ADD(Op.DUP2, 0x64) + Op.SWAP3 + Op.POP
        + Op.MLOAD(offset=Op.ADD(Op.DUP3, 0x108)) + Op.DUP1
        + Op.JUMPI(pc=0xa2e, condition=Op.CALL(gas=Op.ADD(0x12, Op.SDIV(Op.DUP8, 0xa)), address=0x4, value=0x0, args_offset=Op.MLOAD(offset=Op.ADD(Op.DUP8, 0xa4)), args_size=Op.DUP3, ret_offset=Op.DUP6, ret_size=Op.DUP1))
        + Op.INVALID + Op.JUMPDEST + Op.POP + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4
        + Op.POP + Op.POP + Op.SUB(Op.DUP4, Op.DUP1)
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP5, args_size=Op.DUP3, ret_offset=0x480, ret_size=0x20))
        + Op.MLOAD(offset=0x480) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1
        + Op.POP + Op.SWAP1 + Op.POP + Op.POP + Op.MSTORE(offset=0x4a0, value=0x1)
        + Op.RETURN(offset=0x4a0, size=0x20) + Op.POP + Op.POP + Op.JUMPDEST
        + Op.JUMPI(pc=0xd4b, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xd5dc5af1)))
        + Op.MSTORE(offset=0xc0, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0xe0, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0x100, value=Op.CALLDATALOAD(offset=0x44))
        + Op.MSTORE(offset=0x120, value=Op.CALLDATALOAD(offset=0x64))
        + Op.MSTORE(offset=0x140, value=Op.CALLDATALOAD(offset=0x84)) + Op.PUSH1[0x1c]
        + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xe05dcb56)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0xc0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0xe0))
        + Op.ADD(Op.MLOAD(offset=0x100), 0x2) + Op.ADD(Op.MUL(0x20, Op.DUP2), 0x40)
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP6, args_size=0x44, ret_offset=Op.DUP2, ret_size=Op.ADD(0x40, Op.MUL(0x20, Op.DUP2))))
        + Op.ADD(Op.DUP2, 0x40) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1
        + Op.POP + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE
        + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x2c5a40d5)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0xc0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0xe0))
        + Op.MLOAD(offset=0x140) + Op.ADD(Op.MUL(0x20, Op.DUP2), 0x40) + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP6, args_size=0x44, ret_offset=Op.DUP2, ret_size=Op.ADD(0x40, Op.MUL(0x20, Op.DUP2))))
        + Op.ADD(Op.DUP2, 0x40) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1
        + Op.POP + Op.PUSH1[0x80] + Op.PUSH1[0x1c] + Op.PUSH2[0x1ac] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xf4ca7dc4) + Op.DUP4
        + Op.ADD(0x20, Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.DUP2, 0x20))))
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x4), value=Op.DUP4)
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x84), value=Op.SUB(Op.DUP3, 0x20))
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x108), value=Op.DUP1)
        + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.POP + Op.DUP3
        + Op.ADD(0x20, Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.DUP2, 0x20))))
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x24), value=Op.DUP4)
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0xa4), value=Op.SUB(Op.DUP3, 0x20))
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x128), value=Op.DUP1)
        + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.POP
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=Op.MLOAD(offset=0x120))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x64), value=Op.MLOAD(offset=0x100))
        + Op.ADD(0x4, Op.DUP2) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.JUMPI(pc=0xbe7, condition=Op.CALL(gas=0x1f, address=0x4, value=0x0, args_offset=Op.DUP5, args_size=0x84, ret_offset=Op.DUP2, ret_size=0x84))
        + Op.INVALID + Op.JUMPDEST + Op.ADD(Op.DUP2, 0x84) + Op.SWAP3 + Op.POP
        + Op.MLOAD(offset=Op.ADD(Op.DUP3, 0x108)) + Op.DUP1
        + Op.JUMPI(pc=0xc0e, condition=Op.CALL(gas=Op.ADD(0x12, Op.SDIV(Op.DUP8, 0xa)), address=0x4, value=0x0, args_offset=Op.MLOAD(offset=Op.ADD(Op.DUP8, 0x84)), args_size=Op.DUP3, ret_offset=Op.DUP6, ret_size=Op.DUP1))
        + Op.INVALID + Op.JUMPDEST + Op.POP + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4
        + Op.POP + Op.POP + Op.MLOAD(offset=Op.ADD(Op.DUP3, 0x128)) + Op.DUP1
        + Op.JUMPI(pc=0xc36, condition=Op.CALL(gas=Op.ADD(0x12, Op.SDIV(Op.DUP8, 0xa)), address=0x4, value=0x0, args_offset=Op.MLOAD(offset=Op.ADD(Op.DUP8, 0xa4)), args_size=Op.DUP3, ret_offset=Op.DUP6, ret_size=Op.DUP1))
        + Op.INVALID + Op.JUMPDEST + Op.POP + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4
        + Op.POP + Op.POP + Op.SUB(Op.DUP4, Op.DUP1) + Op.MLOAD(offset=0x140)
        + Op.ADD(Op.MUL(0x20, Op.DUP2), 0x40) + Op.MSIZE + Op.SWAP1 + Op.MSIZE
        + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x80), value=0x0, args_offset=Op.DUP7, args_size=Op.DUP5, ret_offset=Op.DUP2, ret_size=Op.ADD(0x40, Op.MUL(0x20, Op.DUP2))))
        + Op.ADD(Op.DUP2, 0x40) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1
        + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP
        + Op.SWAP1 + Op.POP + Op.PUSH1[0x60] + Op.PUSH1[0x1c] + Op.PUSH2[0x14c]
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xb39e1faa)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0xc0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0xe0))
        + Op.DUP3 + Op.ADD(0x20, Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.DUP2, 0x20))))
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x44), value=Op.DUP4)
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0xa4), value=Op.SUB(Op.DUP3, 0x20))
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x108), value=Op.DUP1)
        + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.POP
        + Op.ADD(0x4, Op.DUP2) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.JUMPI(pc=0xcec, condition=Op.CALL(gas=0x1c, address=0x4, value=0x0, args_offset=Op.DUP5, args_size=0x64, ret_offset=Op.DUP2, ret_size=0x64))
        + Op.INVALID + Op.JUMPDEST + Op.ADD(Op.DUP2, 0x64) + Op.SWAP3 + Op.POP
        + Op.MLOAD(offset=Op.ADD(Op.DUP3, 0x108)) + Op.DUP1
        + Op.JUMPI(pc=0xd13, condition=Op.CALL(gas=Op.ADD(0x12, Op.SDIV(Op.DUP8, 0xa)), address=0x4, value=0x0, args_offset=Op.MLOAD(offset=Op.ADD(Op.DUP8, 0xa4)), args_size=Op.DUP3, ret_offset=Op.DUP6, ret_size=Op.DUP1))
        + Op.INVALID + Op.JUMPDEST + Op.POP + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4
        + Op.POP + Op.POP + Op.SUB(Op.DUP4, Op.DUP1)
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP5, args_size=Op.DUP3, ret_offset=0x4c0, ret_size=0x20))
        + Op.MLOAD(offset=0x4c0) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1
        + Op.POP + Op.SWAP1 + Op.POP + Op.POP + Op.MSTORE(offset=0x4e0, value=0x1)
        + Op.RETURN(offset=0x4e0, size=0x20) + Op.POP + Op.POP + Op.JUMPDEST
        + Op.JUMPI(pc=0x114c, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x939aa8c)))
        + Op.MSTORE(offset=0xc0, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0xe0, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0x100, value=Op.CALLDATALOAD(offset=0x44))
        + Op.MSTORE(offset=0x120, value=Op.CALLDATALOAD(offset=0x64))
        + Op.MSTORE(offset=0x140, value=Op.CALLDATALOAD(offset=0x84)) + Op.PUSH1[0x1c]
        + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xe05dcb56)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0xc0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0xe0))
        + Op.ADD(Op.MLOAD(offset=0x100), 0x2) + Op.ADD(Op.MUL(0x20, Op.DUP2), 0x40)
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP6, args_size=0x44, ret_offset=Op.DUP2, ret_size=Op.ADD(0x40, Op.MUL(0x20, Op.DUP2))))
        + Op.ADD(Op.DUP2, 0x40) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1
        + Op.POP + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE
        + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x7dc12195)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0xc0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0xe0))
        + Op.MLOAD(offset=0x140) + Op.ADD(Op.MUL(0x20, Op.DUP2), 0x40) + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP6, args_size=0x44, ret_offset=Op.DUP2, ret_size=Op.ADD(0x40, Op.MUL(0x20, Op.DUP2))))
        + Op.ADD(Op.DUP2, 0x40) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1
        + Op.POP + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE
        + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x586b5be0)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0xc0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0xe0))
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP4, args_size=0x44, ret_offset=0x500, ret_size=0x20))
        + Op.MLOAD(offset=0x500) + Op.SWAP1 + Op.POP + Op.PUSH1[0x1c] + Op.PUSH1[0x64]
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xeb8af5aa)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0xc0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0xe0))
        + Op.MLOAD(offset=0x120) + Op.ADD(Op.MUL(0x20, Op.DUP2), 0x40) + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP6, args_size=0x44, ret_offset=Op.DUP2, ret_size=Op.ADD(0x40, Op.MUL(0x20, Op.DUP2))))
        + Op.ADD(Op.DUP2, 0x40) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1
        + Op.POP + Op.PUSH1[0xc0] + Op.PUSH1[0x1c] + Op.PUSH2[0x26c] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x232b2734) + Op.DUP3
        + Op.ADD(0x20, Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.DUP2, 0x20))))
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x4), value=Op.DUP4)
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0xc4), value=Op.SUB(Op.DUP3, 0x20))
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x188), value=Op.DUP1)
        + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.POP + Op.DUP6
        + Op.ADD(0x20, Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.DUP2, 0x20))))
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x24), value=Op.DUP4)
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0xe4), value=Op.SUB(Op.DUP3, 0x20))
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x1a8), value=Op.DUP1)
        + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.POP + Op.DUP5
        + Op.ADD(0x20, Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.DUP2, 0x20))))
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x44), value=Op.DUP4)
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x104), value=Op.SUB(Op.DUP3, 0x20))
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x1c8), value=Op.DUP1)
        + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.POP
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x64), value=Op.DUP4)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x84), value=Op.MLOAD(offset=0x120))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0xa4), value=Op.MLOAD(offset=0x100))
        + Op.ADD(0x4, Op.DUP2) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.JUMPI(pc=0xf96, condition=Op.CALL(gas=0x25, address=0x4, value=0x0, args_offset=Op.DUP5, args_size=0xc4, ret_offset=Op.DUP2, ret_size=0xc4))
        + Op.INVALID + Op.JUMPDEST + Op.ADD(Op.DUP2, 0xc4) + Op.SWAP3 + Op.POP
        + Op.MLOAD(offset=Op.ADD(Op.DUP3, 0x188)) + Op.DUP1
        + Op.JUMPI(pc=0xfbd, condition=Op.CALL(gas=Op.ADD(0x12, Op.SDIV(Op.DUP8, 0xa)), address=0x4, value=0x0, args_offset=Op.MLOAD(offset=Op.ADD(Op.DUP8, 0xc4)), args_size=Op.DUP3, ret_offset=Op.DUP6, ret_size=Op.DUP1))
        + Op.INVALID + Op.JUMPDEST + Op.POP + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4
        + Op.POP + Op.POP + Op.MLOAD(offset=Op.ADD(Op.DUP3, 0x1a8)) + Op.DUP1
        + Op.JUMPI(pc=0xfe5, condition=Op.CALL(gas=Op.ADD(0x12, Op.SDIV(Op.DUP8, 0xa)), address=0x4, value=0x0, args_offset=Op.MLOAD(offset=Op.ADD(Op.DUP8, 0xe4)), args_size=Op.DUP3, ret_offset=Op.DUP6, ret_size=Op.DUP1))
        + Op.INVALID + Op.JUMPDEST + Op.POP + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4
        + Op.POP + Op.POP + Op.MLOAD(offset=Op.ADD(Op.DUP3, 0x1c8)) + Op.DUP1
        + Op.JUMPI(pc=0x100e, condition=Op.CALL(gas=Op.ADD(0x12, Op.SDIV(Op.DUP8, 0xa)), address=0x4, value=0x0, args_offset=Op.MLOAD(offset=Op.ADD(Op.DUP8, 0x104)), args_size=Op.DUP3, ret_offset=Op.DUP6, ret_size=Op.DUP1))
        + Op.INVALID + Op.JUMPDEST + Op.POP + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4
        + Op.POP + Op.POP + Op.SUB(Op.DUP4, Op.DUP1) + Op.MLOAD(offset=0x120)
        + Op.ADD(Op.MUL(0x20, Op.DUP2), 0x40) + Op.MSIZE + Op.SWAP1 + Op.MSIZE
        + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x80), value=0x0, args_offset=Op.DUP7, args_size=Op.DUP5, ret_offset=Op.DUP2, ret_size=Op.ADD(0x40, Op.MUL(0x20, Op.DUP2))))
        + Op.ADD(Op.DUP2, 0x40) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1
        + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP
        + Op.SWAP1 + Op.POP + Op.PUSH1[0x60] + Op.PUSH1[0x1c] + Op.PUSH2[0x14c]
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x1112b27)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0xc0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0xe0))
        + Op.DUP3 + Op.ADD(0x20, Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.DUP2, 0x20))))
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x44), value=Op.DUP4)
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0xa4), value=Op.SUB(Op.DUP3, 0x20))
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x108), value=Op.DUP1)
        + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.POP
        + Op.ADD(0x4, Op.DUP2) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.JUMPI(pc=0x10c4, condition=Op.CALL(gas=0x1c, address=0x4, value=0x0, args_offset=Op.DUP5, args_size=0x64, ret_offset=Op.DUP2, ret_size=0x64))
        + Op.INVALID + Op.JUMPDEST + Op.ADD(Op.DUP2, 0x64) + Op.SWAP3 + Op.POP
        + Op.MLOAD(offset=Op.ADD(Op.DUP3, 0x108)) + Op.DUP1
        + Op.JUMPI(pc=0x10eb, condition=Op.CALL(gas=Op.ADD(0x12, Op.SDIV(Op.DUP8, 0xa)), address=0x4, value=0x0, args_offset=Op.MLOAD(offset=Op.ADD(Op.DUP8, 0xa4)), args_size=Op.DUP3, ret_offset=Op.DUP6, ret_size=Op.DUP1))
        + Op.INVALID + Op.JUMPDEST + Op.POP + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4
        + Op.POP + Op.POP + Op.SUB(Op.DUP4, Op.DUP1)
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP5, args_size=Op.DUP3, ret_offset=0x580, ret_size=0x20))
        + Op.MLOAD(offset=0x580) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1
        + Op.POP + Op.SWAP1 + Op.POP + Op.POP
        + Op.JUMPI(pc=0x113a, condition=Op.ISZERO(Op.EQ(Op.MLOAD(offset=Op.ADD(Op.DUP6, Op.MUL(0x20, Op.ADD(Op.MLOAD(offset=0x100), 0x1)))), 0x0)))
        + Op.MSTORE(offset=0x5a0, value=0x0) + Op.RETURN(offset=0x5a0, size=0x20)
        + Op.JUMP(pc=0x1147) + Op.JUMPDEST + Op.MSTORE(offset=0x5c0, value=0x1)
        + Op.RETURN(offset=0x5c0, size=0x20) + Op.JUMPDEST + Op.POP + Op.POP + Op.POP
        + Op.POP + Op.JUMPDEST + Op.POP
    ),
    )
    pre[sender] = Account(balance=0xd8d726b7177a800000, nonce=0)
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.MSTORE8(offset=0x75f, value=0x0)
        + Op.DIV(Op.CALLDATALOAD(offset=0x0), 0x100000000000000000000000000000000000000000000000000000000)
        + Op.MSTORE(offset=0x20, value=0x1e147037f0a63df228fe6e7aef730f1ea31c8ce3)
        + Op.MSTORE(offset=0x40, value=0xea65418d7bf32680f55572c943a94b590804998)
        + Op.MSTORE(offset=0x60, value=0xe509e3a93beb1eba72f8cb8d25f93a85e2d54afb)
        + Op.MSTORE(offset=0x80, value=0xc9ae5868651bf7b7db6e360217db49ce4e69c07e)
        + Op.MSTORE(offset=0xa0, value=0x142a6927cf0060133187ba8a8e74d641438f0c1c)
        + Op.MSTORE(offset=0xc0, value=0xb163e767e4c1ba5ae88b2ee7594f3a3fec2bb096)
        + Op.MSTORE(offset=0xe0, value=0xba7b277319128ef4c22635534d0f61dffdaa13ab)
        + Op.MSTORE(offset=0x100, value=0x9761fecf88590592cf05ce545504d376d1693ab3)
        + Op.MSTORE(offset=0x120, value=0xf70bbc50f1468cecae0761ef09386a87c1c696ea)
        + Op.MSTORE(offset=0x140, value=0xa89d22f049aaa5bbfb5f1a1939fff3ae7a26ae74)
        + Op.MSTORE(offset=0x160, value=0x174827f7e53e8ce13b047adcac0eb3f2cb0c3285)
        + Op.JUMPI(pc=0xa88, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x36a560bd)))
        + Op.MSTORE(offset=0x1a0, value=Op.CALLDATALOAD(offset=0x4)) + Op.PUSH1[0x1c]
        + Op.PUSH1[0x44] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x27138bfb)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0))
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0xa0), value=0x0, args_offset=Op.DUP4, args_size=0x24, ret_offset=0x1e0, ret_size=0x20))
        + Op.MLOAD(offset=0x1e0) + Op.SWAP1 + Op.POP
        + Op.JUMPI(pc=0x195, condition=Op.ISZERO(Op.ISZERO))
        + Op.MSTORE(offset=0x200, value=Op.SUB(0x0, 0x1))
        + Op.RETURN(offset=0x200, size=0x20) + Op.JUMPDEST + Op.PUSH1[0x1c]
        + Op.PUSH1[0x44] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x7a66d7ca)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0))
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x80), value=0x0, args_offset=Op.DUP4, args_size=0x24, ret_offset=0x220, ret_size=0x20))
        + Op.MLOAD(offset=0x220) + Op.SWAP1 + Op.POP + Op.PUSH1[0x1c] + Op.PUSH1[0x64]
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xcc1c944e)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.DUP2)
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x280), value=0x0, args_offset=Op.DUP4, args_size=0x44, ret_offset=0x260, ret_size=0x20))
        + Op.MLOAD(offset=0x260) + Op.SWAP1 + Op.POP + Op.PUSH1[0x1c] + Op.PUSH1[0x44]
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x80b5e7bd)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0))
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x60), value=0x0, args_offset=Op.DUP4, args_size=0x24, ret_offset=0x2a0, ret_size=0x20))
        + Op.MLOAD(offset=0x2a0) + Op.SWAP1 + Op.POP + Op.MUL(Op.DUP3, Op.DUP1)
        + Op.PUSH1[0x1c] + Op.PUSH1[0x44] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x18633576)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0))
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x80), value=0x0, args_offset=Op.DUP4, args_size=0x24, ret_offset=0x300, ret_size=0x20))
        + Op.MLOAD(offset=0x300) + Op.SWAP1 + Op.POP
        + Op.JUMPI(pc=0x36d, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x9)))
        + Op.PUSH1[0x1c] + Op.PUSH1[0xc4] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xac44d71e)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.DUP6)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=Op.DUP5)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x64), value=Op.DUP4)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x84), value=Op.DUP3)
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x160), value=0x0, args_offset=Op.DUP4, args_size=0xa4, ret_offset=0x360, ret_size=0x20))
        + Op.MLOAD(offset=0x360) + Op.SWAP1 + Op.POP + Op.POP + Op.PUSH1[0x1c]
        + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x7265802d)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=0x0)
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x80), value=0x0, args_offset=Op.DUP4, args_size=0x44, ret_offset=0x380, ret_size=0x20))
        + Op.MLOAD(offset=0x380) + Op.SWAP1 + Op.POP + Op.POP + Op.PUSH1[0x1c]
        + Op.PUSH1[0x44] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xc5476efe)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0))
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x80), value=0x0, args_offset=Op.DUP4, args_size=0x24, ret_offset=0x3a0, ret_size=0x20))
        + Op.MLOAD(offset=0x3a0) + Op.SWAP1 + Op.POP + Op.POP
        + Op.MSTORE(offset=0x3c0, value=Op.ADD(Op.DUP6, 0x1))
        + Op.RETURN(offset=0x3c0, size=0x20) + Op.JUMP(pc=0xa3a) + Op.JUMPDEST
        + Op.JUMPI(pc=0x3cd, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x0)))
        + Op.PUSH1[0x1c] + Op.PUSH1[0xc4] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xef72638a)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.DUP6)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=Op.DUP5)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x64), value=Op.DUP4)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x84), value=Op.DUP3)
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0xc0), value=0x0, args_offset=Op.DUP4, args_size=0xa4, ret_offset=0x3e0, ret_size=0x20))
        + Op.MLOAD(offset=0x3e0) + Op.SWAP1 + Op.POP + Op.POP + Op.JUMP(pc=0xa39)
        + Op.JUMPDEST + Op.JUMPI(pc=0x42d, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x1)))
        + Op.PUSH1[0x1c] + Op.PUSH1[0xc4] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xa63e976c)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.DUP6)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=Op.DUP5)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x64), value=Op.DUP4)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x84), value=Op.DUP3)
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0xe0), value=0x0, args_offset=Op.DUP4, args_size=0xa4, ret_offset=0x400, ret_size=0x20))
        + Op.MLOAD(offset=0x400) + Op.SWAP1 + Op.POP + Op.POP + Op.JUMP(pc=0xa38)
        + Op.JUMPDEST + Op.JUMPI(pc=0x48d, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x2)))
        + Op.PUSH1[0x1c] + Op.PUSH1[0xc4] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x533ea0ed)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.DUP6)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=Op.DUP5)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x64), value=Op.DUP4)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x84), value=Op.DUP3)
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0xe0), value=0x0, args_offset=Op.DUP4, args_size=0xa4, ret_offset=0x420, ret_size=0x20))
        + Op.MLOAD(offset=0x420) + Op.SWAP1 + Op.POP + Op.POP + Op.JUMP(pc=0xa37)
        + Op.JUMPDEST + Op.JUMPI(pc=0x850, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x3)))
        + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xe05dcb56)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.DUP6)
        + Op.ADD(Op.DUP6, 0x2) + Op.ADD(Op.MUL(0x20, Op.DUP2), 0x40) + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x280), value=0x0, args_offset=Op.DUP6, args_size=0x44, ret_offset=Op.DUP2, ret_size=Op.ADD(0x40, Op.MUL(0x20, Op.DUP2))))
        + Op.ADD(Op.DUP2, 0x40) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1
        + Op.POP + Op.PUSH1[0x1c] + Op.PUSH1[0x44] + Op.MSIZE + Op.SWAP1 + Op.MSIZE
        + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x3d905045)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0))
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x80), value=0x0, args_offset=Op.DUP4, args_size=0x24, ret_offset=0x480, ret_size=0x20))
        + Op.MLOAD(offset=0x480) + Op.SWAP1 + Op.POP
        + Op.JUMPI(pc=0x633, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x4)))
        + Op.PUSH1[0x1c] + Op.PUSH1[0xc4] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x939aa8c)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.DUP8)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=Op.DUP7)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x64), value=Op.DUP6)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x84), value=Op.DUP5)
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x100), value=0x0, args_offset=Op.DUP4, args_size=0xa4, ret_offset=0x4e0, ret_size=0x20))
        + Op.MLOAD(offset=0x4e0) + Op.SWAP1 + Op.POP + Op.PUSH2[0x4c0] + Op.MSTORE
        + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xc286273a)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=0x0)
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x80), value=0x0, args_offset=Op.DUP4, args_size=0x44, ret_offset=0x500, ret_size=0x20))
        + Op.MLOAD(offset=0x500) + Op.SWAP1 + Op.POP + Op.POP
        + Op.JUMPI(pc=0x5e5, condition=Op.ISZERO(Op.EQ(Op.MLOAD(offset=0x4c0), 0x1)))
        + Op.MSTORE(offset=0x520, value=Op.DUP3) + Op.RETURN(offset=0x520, size=0x20)
        + Op.JUMP(pc=0x62e) + Op.JUMPDEST + Op.PUSH1[0x1c] + Op.PUSH1[0x44] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xaac2ffb5)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0))
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x80), value=0x0, args_offset=Op.DUP4, args_size=0x24, ret_offset=0x540, ret_size=0x20))
        + Op.MLOAD(offset=0x540) + Op.SWAP1 + Op.POP + Op.POP
        + Op.MSTORE(offset=0x560, value=Op.ADD(Op.DUP4, 0x1))
        + Op.RETURN(offset=0x560, size=0x20) + Op.JUMPDEST + Op.JUMP(pc=0x804)
        + Op.JUMPDEST + Op.JUMPI(pc=0x694, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x0)))
        + Op.PUSH1[0x1c] + Op.PUSH1[0xc4] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x546fdeb3)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.DUP8)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=Op.DUP7)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x64), value=Op.DUP6)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x84), value=Op.DUP5)
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x100), value=0x0, args_offset=Op.DUP4, args_size=0xa4, ret_offset=0x580, ret_size=0x20))
        + Op.MLOAD(offset=0x580) + Op.SWAP1 + Op.POP + Op.POP + Op.JUMP(pc=0x803)
        + Op.JUMPDEST + Op.JUMPI(pc=0x742, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x1)))
        + Op.PUSH1[0x0] + Op.PUSH1[0x1c] + Op.PUSH1[0xc4] + Op.MSIZE + Op.SWAP1
        + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xde9080c8)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.DUP9)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=Op.DUP8)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x64), value=Op.DUP7)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x84), value=Op.DUP6)
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x100), value=0x0, args_offset=Op.DUP4, args_size=0xa4, ret_offset=0x5a0, ret_size=0x20))
        + Op.MLOAD(offset=0x5a0) + Op.SWAP1 + Op.POP
        + Op.JUMPI(pc=0x732, condition=Op.ISZERO(Op.EQ)) + Op.PUSH1[0x1c]
        + Op.PUSH1[0x44] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x1cda01ef)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0))
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x80), value=0x0, args_offset=Op.DUP4, args_size=0x24, ret_offset=0x5c0, ret_size=0x20))
        + Op.MLOAD(offset=0x5c0) + Op.SWAP1 + Op.POP + Op.POP + Op.JUMPDEST
        + Op.MSTORE(offset=0x5e0, value=Op.DUP3) + Op.RETURN(offset=0x5e0, size=0x20)
        + Op.JUMP(pc=0x802) + Op.JUMPDEST
        + Op.JUMPI(pc=0x7a3, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x2)))
        + Op.PUSH1[0x1c] + Op.PUSH1[0xc4] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x384ca8dd)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.DUP8)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=Op.DUP7)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x64), value=Op.DUP6)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x84), value=Op.DUP5)
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x100), value=0x0, args_offset=Op.DUP4, args_size=0xa4, ret_offset=0x600, ret_size=0x20))
        + Op.MLOAD(offset=0x600) + Op.SWAP1 + Op.POP + Op.POP + Op.JUMP(pc=0x801)
        + Op.JUMPDEST + Op.JUMPI(pc=0x800, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x3)))
        + Op.PUSH1[0x1c] + Op.PUSH1[0xc4] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xd5dc5af1)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.DUP8)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=Op.DUP7)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x64), value=Op.DUP6)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x84), value=Op.DUP5)
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x100), value=0x0, args_offset=Op.DUP4, args_size=0xa4, ret_offset=0x620, ret_size=0x20))
        + Op.MLOAD(offset=0x620) + Op.SWAP1 + Op.POP + Op.POP + Op.JUMPDEST
        + Op.JUMPDEST + Op.JUMPDEST + Op.JUMPDEST + Op.JUMPDEST + Op.PUSH1[0x1c]
        + Op.PUSH1[0x44] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x1cda01ef)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0))
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x80), value=0x0, args_offset=Op.DUP4, args_size=0x24, ret_offset=0x640, ret_size=0x20))
        + Op.MLOAD(offset=0x640) + Op.SWAP1 + Op.POP + Op.POP
        + Op.MSTORE(offset=0x660, value=Op.DUP3) + Op.RETURN(offset=0x660, size=0x20)
        + Op.POP + Op.POP + Op.JUMP(pc=0xa36) + Op.JUMPDEST
        + Op.JUMPI(pc=0x8b1, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x4)))
        + Op.PUSH1[0x1c] + Op.PUSH1[0xc4] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xf6559853)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.DUP6)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=Op.DUP5)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x64), value=Op.DUP4)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x84), value=Op.DUP3)
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x120), value=0x0, args_offset=Op.DUP4, args_size=0xa4, ret_offset=0x680, ret_size=0x20))
        + Op.MLOAD(offset=0x680) + Op.SWAP1 + Op.POP + Op.POP + Op.JUMP(pc=0xa35)
        + Op.JUMPDEST + Op.JUMPI(pc=0x912, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x5)))
        + Op.PUSH1[0x1c] + Op.PUSH1[0xc4] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xd8e5473d)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.DUP6)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=Op.DUP5)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x64), value=Op.DUP4)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x84), value=Op.DUP3)
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x120), value=0x0, args_offset=Op.DUP4, args_size=0xa4, ret_offset=0x6a0, ret_size=0x20))
        + Op.MLOAD(offset=0x6a0) + Op.SWAP1 + Op.POP + Op.POP + Op.JUMP(pc=0xa34)
        + Op.JUMPDEST + Op.JUMPI(pc=0x973, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x6)))
        + Op.PUSH1[0x1c] + Op.PUSH1[0xc4] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x90507ea)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.DUP6)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=Op.DUP5)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x64), value=Op.DUP4)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x84), value=Op.DUP3)
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x120), value=0x0, args_offset=Op.DUP4, args_size=0xa4, ret_offset=0x6c0, ret_size=0x20))
        + Op.MLOAD(offset=0x6c0) + Op.SWAP1 + Op.POP + Op.POP + Op.JUMP(pc=0xa33)
        + Op.JUMPDEST + Op.JUMPI(pc=0x9d4, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x7)))
        + Op.PUSH1[0x1c] + Op.PUSH1[0xc4] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x5b911842)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.DUP6)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=Op.DUP5)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x64), value=Op.DUP4)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x84), value=Op.DUP3)
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x140), value=0x0, args_offset=Op.DUP4, args_size=0xa4, ret_offset=0x6e0, ret_size=0x20))
        + Op.MLOAD(offset=0x6e0) + Op.SWAP1 + Op.POP + Op.POP + Op.JUMP(pc=0xa32)
        + Op.JUMPDEST + Op.JUMPI(pc=0xa31, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x8)))
        + Op.PUSH1[0x1c] + Op.PUSH1[0xc4] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xabe22b84)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.DUP6)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=Op.DUP5)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x64), value=Op.DUP4)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x84), value=Op.DUP3)
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x140), value=0x0, args_offset=Op.DUP4, args_size=0xa4, ret_offset=0x700, ret_size=0x20))
        + Op.MLOAD(offset=0x700) + Op.SWAP1 + Op.POP + Op.POP + Op.JUMPDEST
        + Op.JUMPDEST + Op.JUMPDEST + Op.JUMPDEST + Op.JUMPDEST + Op.JUMPDEST
        + Op.JUMPDEST + Op.JUMPDEST + Op.JUMPDEST + Op.JUMPDEST + Op.PUSH1[0x1c]
        + Op.PUSH1[0x44] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xaac2ffb5)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0))
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x80), value=0x0, args_offset=Op.DUP4, args_size=0x24, ret_offset=0x720, ret_size=0x20))
        + Op.MLOAD(offset=0x720) + Op.SWAP1 + Op.POP + Op.POP
        + Op.MSTORE(offset=0x740, value=Op.ADD(Op.DUP2, 0x1))
        + Op.RETURN(offset=0x740, size=0x20) + Op.POP + Op.POP + Op.POP + Op.POP
        + Op.POP + Op.JUMPDEST + Op.POP
    ),
    )
    pre[callee_8] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.MSTORE8(offset=0x83f, value=0x0)
        + Op.DIV(Op.CALLDATALOAD(offset=0x0), 0x100000000000000000000000000000000000000000000000000000000)
        + Op.JUMPI(pc=Op.PUSH2[0x66], condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x7a66d7ca)))
        + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x4)) + Op.PUSH1[0x60]
        + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MSTORE(offset=0x60, value=Op.SLOAD(key=Op.SHA3))
        + Op.RETURN(offset=0x60, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=Op.PUSH2[0xa5], condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xc60409c6)))
        + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x4)) + Op.PUSH1[0x60]
        + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MSTORE(offset=0xa0, value=Op.SLOAD(key=Op.SHA3))
        + Op.RETURN(offset=0xa0, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=Op.PUSH2[0xe4], condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x18633576)))
        + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x4)) + Op.PUSH1[0x60]
        + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x2) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MSTORE(offset=0xe0, value=Op.SLOAD(key=Op.SHA3))
        + Op.RETURN(offset=0xe0, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x1bc, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xb3903c8a)))
        + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x4)) + Op.PUSH1[0x60]
        + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x5) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MSTORE(offset=0x120, value=Op.SLOAD(key=Op.SHA3))
        + Op.MLOAD(offset=0x120) + Op.ADD(0x20, Op.MUL(0x20, Op.DUP1)) + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1
        + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH2[0x160] + Op.MSTORE
        + Op.MSTORE(offset=0x1c0, value=0x0) + Op.JUMPDEST
        + Op.JUMPI(pc=0x19f, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x1c0), Op.MLOAD(offset=0x120))))
        + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x4)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0))
        + Op.DUP1 + Op.SWAP1 + Op.POP
        + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x160), Op.MUL(0x20, Op.MLOAD(offset=0x1c0))), value=Op.SLOAD(key=Op.SHA3))
        + Op.MSTORE(offset=0x1c0, value=Op.ADD(Op.MLOAD(offset=0x1c0), 0x1))
        + Op.JUMP(pc=0x147) + Op.JUMPDEST + Op.MLOAD(offset=0x160)
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20)
        + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20)))
        + Op.POP + Op.JUMPDEST
        + Op.JUMPI(pc=0x1fd, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x6824e0fb)))
        + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x4)) + Op.PUSH1[0x60]
        + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x5) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MSTORE(offset=0x220, value=Op.SLOAD(key=Op.SHA3))
        + Op.RETURN(offset=0x220, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x23e, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x3db16be3)))
        + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x4)) + Op.PUSH1[0x60]
        + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x6) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MSTORE(offset=0x260, value=Op.SLOAD(key=Op.SHA3))
        + Op.RETURN(offset=0x260, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x2e0, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xc3387858)))
        + Op.MSTORE(offset=0x2a0, value=0x0)
        + Op.MSTORE(offset=0x2c0, value=Op.SLOAD(key=0x0)) + Op.MLOAD(offset=0x2c0)
        + Op.ADD(0x20, Op.MUL(0x20, Op.DUP1)) + Op.MSIZE + Op.SWAP1 + Op.MSIZE
        + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1
        + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH2[0x2e0] + Op.MSTORE + Op.JUMPDEST
        + Op.JUMPI(pc=0x2c3, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x2a0), Op.MLOAD(offset=0x2c0))))
        + Op.PUSH1[0x40] + Op.PUSH1[0x40] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x1)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x2a0))
        + Op.DUP1 + Op.SWAP1 + Op.POP
        + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x2e0), Op.MUL(0x20, Op.MLOAD(offset=0x2a0))), value=Op.SLOAD(key=Op.SHA3))
        + Op.MSTORE(offset=0x2a0, value=Op.ADD(Op.MLOAD(offset=0x2a0), 0x1))
        + Op.JUMP(pc=0x27a) + Op.JUMPDEST + Op.MLOAD(offset=0x2e0)
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20)
        + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20)))
        + Op.POP + Op.JUMPDEST
        + Op.JUMPI(pc=0x2fa, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x175c6322)))
        + Op.MSTORE(offset=0x380, value=Op.SLOAD(key=0x0))
        + Op.RETURN(offset=0x380, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x336, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xd861f2b4)))
        + Op.MSTORE(offset=0x3a0, value=Op.CALLDATALOAD(offset=0x4)) + Op.PUSH1[0x40]
        + Op.PUSH1[0x40] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x1)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x3a0))
        + Op.DUP1 + Op.SWAP1 + Op.POP
        + Op.MSTORE(offset=0x3c0, value=Op.SLOAD(key=Op.SHA3))
        + Op.RETURN(offset=0x3c0, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x44f, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xb0dab01f)))
        + Op.MSTORE(offset=0x400, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x420, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0x440, value=Op.CALLDATALOAD(offset=0x44))
        + Op.MSTORE(offset=0x460, value=Op.CALLDATALOAD(offset=0x64)) + Op.PUSH1[0x0]
        + Op.PUSH1[0x60] + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x400))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SLOAD(key=Op.SHA3)
        + Op.JUMPI(pc=0x441, condition=Op.ISZERO(Op.EQ)) + Op.MLOAD(offset=0x420)
        + Op.PUSH1[0x60] + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x400))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.MLOAD(offset=0x440) + Op.PUSH1[0x60]
        + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x400))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.MLOAD(offset=0x460) + Op.PUSH1[0x60]
        + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x400))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x6) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.MLOAD(offset=0x400) + Op.PUSH1[0x40]
        + Op.PUSH1[0x40] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x1)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.SLOAD(key=0x0)) + Op.DUP1
        + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE
        + Op.SSTORE(key=0x0, value=Op.ADD(Op.SLOAD(key=0x0), 0x1))
        + Op.MSTORE(offset=0x520, value=0x1) + Op.RETURN(offset=0x520, size=0x20)
        + Op.JUMP(pc=0x44e) + Op.JUMPDEST + Op.MSTORE(offset=0x540, value=0x0)
        + Op.RETURN(offset=0x540, size=0x20) + Op.JUMPDEST + Op.JUMPDEST
        + Op.JUMPI(pc=0x4b9, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xaac2ffb5)))
        + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x4)) + Op.PUSH1[0x1]
        + Op.PUSH1[0x60] + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x2) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.ADD + Op.PUSH1[0x60] + Op.PUSH1[0x60]
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x2) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.MSTORE(offset=0x5a0, value=0x1)
        + Op.RETURN(offset=0x5a0, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x507, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x7265802d)))
        + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x5c0, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MLOAD(offset=0x5c0) + Op.PUSH1[0x60] + Op.PUSH1[0x60] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x2) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.MSTORE(offset=0x600, value=0x1)
        + Op.RETURN(offset=0x600, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x571, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xc5476efe)))
        + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x4)) + Op.PUSH1[0x1]
        + Op.PUSH1[0x60] + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.ADD + Op.PUSH1[0x60] + Op.PUSH1[0x60]
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.MSTORE(offset=0x660, value=0x1)
        + Op.RETURN(offset=0x660, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x63b, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xc551e31e)))
        + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x680, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0x60]
        + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x5) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MSTORE(offset=0x120, value=Op.SLOAD(key=Op.SHA3))
        + Op.MLOAD(offset=0x680) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x4)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x120))
        + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.PUSH1[0x1]
        + Op.PUSH1[0x60] + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x5) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.ADD + Op.PUSH1[0x60] + Op.PUSH1[0x60]
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x5) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.MSTORE(offset=0x720, value=0x1)
        + Op.RETURN(offset=0x720, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x67c, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x3d905045)))
        + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x4)) + Op.PUSH1[0x60]
        + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x3) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MSTORE(offset=0x740, value=Op.SLOAD(key=Op.SHA3))
        + Op.RETURN(offset=0x740, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x6e6, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x1cda01ef)))
        + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x4)) + Op.PUSH1[0x1]
        + Op.PUSH1[0x60] + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x3) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.ADD + Op.PUSH1[0x60] + Op.PUSH1[0x60]
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x3) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.MSTORE(offset=0x7c0, value=0x1)
        + Op.RETURN(offset=0x7c0, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x734, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xc286273a)))
        + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x7e0, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MLOAD(offset=0x7e0) + Op.PUSH1[0x60] + Op.PUSH1[0x60] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x3) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.MSTORE(offset=0x820, value=0x1)
        + Op.RETURN(offset=0x820, size=0x20) + Op.JUMPDEST + Op.POP
    ),
        storage={0x0: 0x1, 0xa4470e9d0419df71f6257fcdfd2c0a3bad96a23f5ab414bc10aaf1a31a536a7: 0xb4876148229c22bd2291f1a4f5468c8c789b23639370c4d447f270ba341dbbec, 0x16ef4193a274568d283ff919c299729e07696d9ada48187b81d68e12e7b962de: 0xa103c04e7ecb9b3395f77c7b0cad28e62c85f042de4767ccc6c005e6f47f8d4, 0x1f1866e966f321b84535705846689749d34d5dc02994613e2931973c605d9e93: 0xc723d0aa4a60529fe42277c8094aa19263aff36650136efc5edfd0785d457634, 0x252a4ec7133643fddcdb22a86c415f78b2dd251f18d1efcd6a44acf590c4ae72: 0x9caf94b82715869e71d3cee986094ea612f0258570b7e5ef47b5d09e9515322b, 0x41b451e8d86d28add758cbd3f48a18fd04b11a80288c1dc434a5bf2d8fb1ca64: 0xb602498f12a8b4af3a1fca357cea6b19bcd163dfec1d845364ce1395f7c21fa7, 0x491d10658c1ec762152d8ad2d890ad59111b1ee7b4bc25736046923d3534d9a5: 0x629e, 0x5b0e8552efd72a845e47318abbbef9dc9fcdfe0d1a06cda44494401301581511: 0xfbc98f4017ae5c20459daadaa6bee519b6de871d3dbaa9ab3f34340fef4cb643, 0x5b672a107ba6fab01cbddf079042e9f6176a8e6f154584fc4df4b15674c9456e: 0x1603da41d610854d85536b37d000e5eb7ca09786c43f50e7441c0afbff1de0a9, 0x605b934bd26c9ecdf7029a7dc062d3a6b87338511cff96e0c5f13de9eea3462e: 0xf0d24f3d0eda573fc5d43e3d0680993c51293752cd6de205040d3197f412f475, 0x618355e25491dfe86175f9d9b3147e4d680aa561d98384e3621dc6a3088b0846: 0x6b2e6d2d5deb27dffec973f23af4caf111e66d1397f467dbbedf5ab2192fb6b6, 0x65112936bec0f1e84fda6623fb54e12baadc8a4a208c8c4eb3ed5e79cbd7e85f: 0xa59ac24e3e0663413d0f87516ba8fb44c6c3e14da8eaabbde80f8ee285f65934, 0x687cb2122de7bacf42b9cd380b04ff2a2ce92a0b63706a9a78263b3ce86f3313: 0x200000000000000, 0x72a539b064c98d29a514ee55694225e05fb41fe63e5fe710e4536bd9ba3591b4: 0x338ecfe6c523ed1184918b19584d97dd1095ecaadc49c7ba9da62b8b513026e0, 0x7aeb0a0ce8882a12d853078382a2bc72f7a94af6109f167de37b36c0a7deb828: 0x4c428400ea8a7bd7c46ba9895b508770efa4551f0d793e1beb1207da01d9962f, 0x7c8f4a98e086f64e28c75f54712b5d44bec3c29b5c70519e8880d3046a5618dc: 0xaafc1f2601752b114d722070f75539bfec7faf49f0d48a48d27862f0c3b09903, 0x809c325f50acf5787776e960985e72443b4330ad1e2f466557fffee16ba51d44: 0xb940a56e64b5b661d87919b8ef03640ec077a6d72dd0b524adedaa7ddc91ff7a, 0x84e4a80d33c5d2abd2b0a5aec0fdc5eaeed90ab31db556e404a81718ea286e39: 0x1c, 0x877305412fa2486f563c457b744e5c8b1e4d0eca73371de5e771f2abc263f4dc: 0x7088a36f67276d475aa62127cfde9790cc802fdf3a54df49461a25eb8bf15707, 0x922a8f2fc1cbe67c8acc6a8a720983c366d71d3e2e78e3048949ebc913ea611a: 0x50fb9f913ca102534bb0a8eb8ebf19c68dfd16ffe5e207bcc580084cd4ecd8b4, 0x987cb9ecfd8ce499d9d0e9e6b7da29617aa02774a34f4a8ea54442f44a1e1936: 0x5179f98f555f1e9f1d4a335d16f41154579a53e361e9859269b6fa74ea9c7d21, 0xada5013122d395ba3c54772283fb069b10426056ef8ca54750cb9bb552a59e7d: 0xf69b5, 0xb16b117660f31197087f4d6fe50d3d4579152244956f753f9653ccf85f4b35c4: 0x830272e3bb35226b047244cbdc46f1b6b864a280461e7a592f70e0863f4f1d33, 0xb1f1aaedfb83c7755a2bffc9e2557f1723f9abe5642397963e76248c9209af57: 0xe9be955c5fbfcd846d7425eaea05ce897786aefad99665342cbf30761b352526, 0xb7bd50fdf7b043411c9ac33f0af2cebc69c393eb0b91f4976946f9c7b15ad0da: 0xfccca0e7832bae9afe799a6d6177dc3869fa6c5b5105f8df6f365de5723820ec, 0xbc96058eb03504ee6f5c0a9582f8720d99a6e9738b171499507facff0b2c0b5b: 0x9db6a4f2766b51013b8d2f9038131d1bb4af725d019d111d7e26ff96c023b23f, 0xc186c4f377b7f13892ade9656acd1522aa1f8ac151ac4f62457b5073241d79fc: 0x7289738fef00f1770eeb098db9bd486c01ac12398d79cdf935514a128c585c51, 0xcae57ae3017972d63effd8eae44f5054402c3e890d154b905ed6b5b533327fa9: 0xd2e4bf465e61993d13089b940a7c55017a5117d8e43e4115550a139e1d4b3e3a, 0xcf569ee7bf3accc0f893dffd04f1a757f373efe80893eff504fb3678f688ec1d: 0x3, 0xd69b7284545a9f5275df64ce94848dc954fcb8a8b525e7ac801517c12a75af84: 0x4202995350abae303b43e564aa79121a30b5f1aea31f69cd25e07dd3fa64dce7, 0xd8f6f90f51e657690ee28d1cc80d81bc1b89290065891fdd853d09caaaf756aa: 0x1, 0xde72f8eed43cc2a5a3eaa51483d14b17dc92bb26c154ae184cee4b4895011edc: 0x47ce2b6fdb72c3fabb9c74f82c1e3e522bcd42e614fd85c208ac3c4c840cea72, 0xe0e687ddf317f3d2b209ae3884148eff0f636e16827f82eded14ada8fc603009: 0xfa7c8939f9b033162cf8d75ea69671bb8a27041bd4cdc76594e61e99333cb041, 0xe8cda339d72a1a350b62f1e3fa52e254c395cc9fdd9f60adb21c7633fbdab531: 0x128c4fdf4801a30eae99dd58f0f3ff5ca65f71b66a9ac0f38dd450fb24b4aaaa, 0xec5e7f54fa5e516e616b04f9d5a0ee433a80e09ed47d7e5269afd76c05ff251e: 0x14, 0xf9a3bf5f2ccb903ee1a7644113b794db0260de404fb8f11203e75a7fff151618: 0xbd94773c0d85c68240ae8dfd53d9d33cd137509bfc5d3433381299df768c8377},
    )
    pre[callee_9] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.MSTORE8(offset=0xb7f, value=0x0)
        + Op.DIV(Op.CALLDATALOAD(offset=0x0), 0x100000000000000000000000000000000000000000000000000000000)
        + Op.MSTORE(offset=0x20, value=0xc9ae5868651bf7b7db6e360217db49ce4e69c07e)
        + Op.JUMPI(pc=0x245, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x8d3d587)))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.PUSH1[0x60]
        + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MSTORE(offset=0x80, value=Op.SLOAD(key=Op.SHA3)) + Op.PUSH1[0x0]
        + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x2)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.ORIGIN) + Op.DUP1
        + Op.SWAP1 + Op.POP + Op.SLOAD(key=Op.SHA3)
        + Op.JUMPI(pc=0x14e, condition=Op.ISZERO(Op.ISZERO(Op.EQ))) + Op.PUSH1[0x80]
        + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x2)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.ORIGIN) + Op.DUP1
        + Op.SWAP1 + Op.POP + Op.MSTORE(offset=0x80, value=Op.SLOAD(key=Op.SHA3))
        + Op.PUSH9[0x2f0000000000000000] + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.ORIGIN + Op.PUSH1[0xa0] + Op.PUSH1[0xa0]
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.JUMP(pc=0x238) + Op.JUMPDEST
        + Op.MLOAD(offset=0x80) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x2)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.ORIGIN) + Op.DUP1
        + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.PUSH9[0x2f0000000000000000]
        + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.ORIGIN + Op.PUSH1[0xa0] + Op.PUSH1[0xa0]
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.PUSH1[0x1] + Op.PUSH1[0x60]
        + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.ADD + Op.PUSH1[0x60] + Op.PUSH1[0x60]
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.JUMPDEST
        + Op.MSTORE(offset=0x1e0, value=0x1) + Op.RETURN(offset=0x1e0, size=0x20)
        + Op.JUMPDEST
        + Op.JUMPI(pc=0x29d, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x28c8b315)))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x200, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0xa0]
        + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x200))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MSTORE(offset=0x220, value=Op.SLOAD(key=Op.SHA3))
        + Op.RETURN(offset=0x220, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x386, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x74af23ec)))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x260, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0x80]
        + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x2)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x260))
        + Op.DUP1 + Op.SWAP1 + Op.POP
        + Op.MSTORE(offset=0x200, value=Op.SLOAD(key=Op.SHA3))
        + Op.JUMPI(pc=0x332, condition=Op.ISZERO(Op.EQ(Op.MLOAD(offset=0x200), 0x0)))
        + Op.MLOAD(offset=0x260) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x200))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.ISZERO(Op.EQ) + Op.JUMP(pc=0x335)
        + Op.JUMPDEST + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x347, condition=Op.ISZERO) + Op.MSTORE(offset=0x2c0, value=0x0)
        + Op.RETURN(offset=0x2c0, size=0x20) + Op.JUMPDEST + Op.PUSH1[0xa0]
        + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x200))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MSTORE(offset=0x2e0, value=Op.SLOAD(key=Op.SHA3))
        + Op.RETURN(offset=0x2e0, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x3dc, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x84d646ee)))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0xa0]
        + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MSTORE(offset=0x320, value=Op.SLOAD(key=Op.SHA3))
        + Op.RETURN(offset=0x320, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x6f4, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xf4229427)))
        + Op.MSTORE(offset=0x260, value=Op.CALLDATALOAD(offset=0x4)) + Op.PUSH1[0x1c]
        + Op.PUSH1[0x24] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x175c6322)
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP4, args_size=0x4, ret_offset=0x3a0, ret_size=0x20))
        + Op.MLOAD(offset=0x3a0) + Op.SWAP1 + Op.POP + Op.PUSH2[0x360] + Op.MSTORE
        + Op.JUMPI(pc=0x581, condition=Op.ISZERO(Op.MLOAD(offset=0x260)))
        + Op.MUL(0x2, Op.MLOAD(offset=0x360)) + Op.ADD(0x20, Op.MUL(0x20, Op.DUP1))
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20)
        + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH2[0x3c0] + Op.MSTORE
        + Op.MLOAD(offset=0x360) + Op.ADD(0x20, Op.MUL(0x20, Op.DUP1)) + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1
        + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH2[0x420] + Op.MSTORE + Op.PUSH1[0x1c]
        + Op.PUSH1[0x24] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xc3387858)
        + Op.MLOAD(offset=0x360) + Op.ADD(Op.MUL(0x20, Op.DUP2), 0x40) + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP6, args_size=0x4, ret_offset=Op.DUP2, ret_size=Op.ADD(0x40, Op.MUL(0x20, Op.DUP2))))
        + Op.ADD(Op.DUP2, 0x40) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1
        + Op.POP + Op.PUSH2[0x420] + Op.MSTORE + Op.MSTORE(offset=0x4c0, value=0x0)
        + Op.MSTORE(offset=0x4e0, value=0x0) + Op.JUMPDEST
        + Op.JUMPI(pc=0x57c, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x4c0), Op.MLOAD(offset=0x360))))
        + Op.MSTORE(offset=0x60, value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x420), Op.MUL(0x20, Op.MLOAD(offset=0x4c0)))))
        + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x74af23ec)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0x260))
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.ADDRESS, value=0x0, args_offset=Op.DUP4, args_size=0x44, ret_offset=0x520, ret_size=0x20))
        + Op.MLOAD(offset=0x520) + Op.SWAP1 + Op.POP + Op.PUSH2[0x500] + Op.MSTORE
        + Op.JUMPI(pc=0x56c, condition=Op.ISZERO(Op.ISZERO(Op.EQ(Op.MLOAD(offset=0x500), 0x0))))
        + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x3c0), Op.MUL(0x20, Op.MLOAD(offset=0x4e0))), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x3c0), Op.MUL(0x20, Op.ADD(Op.MLOAD(offset=0x4e0), 0x1))), value=Op.MLOAD(offset=0x500))
        + Op.MSTORE(offset=0x4e0, value=Op.ADD(Op.MLOAD(offset=0x4e0), 0x2))
        + Op.JUMPDEST
        + Op.MSTORE(offset=0x4c0, value=Op.ADD(Op.MLOAD(offset=0x4c0), 0x1))
        + Op.JUMP(pc=0x4ce) + Op.JUMPDEST + Op.JUMP(pc=0x6d7) + Op.JUMPDEST
        + Op.MSTORE(offset=0x260, value=Op.ORIGIN)
        + Op.MUL(0x2, Op.MLOAD(offset=0x360)) + Op.ADD(0x20, Op.MUL(0x20, Op.DUP1))
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20)
        + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH2[0x3c0] + Op.MSTORE
        + Op.MLOAD(offset=0x360) + Op.ADD(0x20, Op.MUL(0x20, Op.DUP1)) + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1
        + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH2[0x420] + Op.MSTORE + Op.PUSH1[0x1c]
        + Op.PUSH1[0x24] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xc3387858)
        + Op.MLOAD(offset=0x360) + Op.ADD(Op.MUL(0x20, Op.DUP2), 0x40) + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP6, args_size=0x4, ret_offset=Op.DUP2, ret_size=Op.ADD(0x40, Op.MUL(0x20, Op.DUP2))))
        + Op.ADD(Op.DUP2, 0x40) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1
        + Op.POP + Op.PUSH2[0x420] + Op.MSTORE + Op.MSTORE(offset=0x4c0, value=0x0)
        + Op.MSTORE(offset=0x4e0, value=0x0) + Op.JUMPDEST
        + Op.JUMPI(pc=0x6d6, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x4c0), Op.MLOAD(offset=0x360))))
        + Op.MSTORE(offset=0x60, value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x420), Op.MUL(0x20, Op.MLOAD(offset=0x4c0)))))
        + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x74af23ec)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0x260))
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.ADDRESS, value=0x0, args_offset=Op.DUP4, args_size=0x44, ret_offset=0x5c0, ret_size=0x20))
        + Op.MLOAD(offset=0x5c0) + Op.SWAP1 + Op.POP + Op.PUSH2[0x500] + Op.MSTORE
        + Op.JUMPI(pc=0x6c6, condition=Op.ISZERO(Op.ISZERO(Op.EQ(Op.MLOAD(offset=0x500), 0x0))))
        + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x3c0), Op.MUL(0x20, Op.MLOAD(offset=0x4e0))), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x3c0), Op.MUL(0x20, Op.ADD(Op.MLOAD(offset=0x4e0), 0x1))), value=Op.MLOAD(offset=0x500))
        + Op.MSTORE(offset=0x4e0, value=Op.ADD(Op.MLOAD(offset=0x4e0), 0x2))
        + Op.JUMPDEST
        + Op.MSTORE(offset=0x4c0, value=Op.ADD(Op.MLOAD(offset=0x4c0), 0x1))
        + Op.JUMP(pc=0x628) + Op.JUMPDEST + Op.JUMPDEST + Op.MLOAD(offset=0x3c0)
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20)
        + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20)))
        + Op.POP + Op.JUMPDEST
        + Op.JUMPI(pc=0x735, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x80b5e7bd)))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.PUSH1[0x60]
        + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MSTORE(offset=0x600, value=Op.SLOAD(key=Op.SHA3))
        + Op.RETURN(offset=0x600, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x786, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x156f1c32)))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x640, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0x80]
        + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x2)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x640))
        + Op.DUP1 + Op.SWAP1 + Op.POP
        + Op.MSTORE(offset=0x660, value=Op.SLOAD(key=Op.SHA3))
        + Op.RETURN(offset=0x660, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x878, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xb3a24fc0)))
        + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE
        + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE)
        + Op.MSTORE(offset=0x6c0, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x4)))
        + Op.MSTORE(offset=0x6e0, value=Op.CALLDATALOAD(offset=0x24)) + Op.POP
        + Op.ADD(Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x6c0), 0x20)), 0x2)
        + Op.ADD(0x20, Op.MUL(0x20, Op.DUP1)) + Op.MSIZE + Op.SWAP1 + Op.MSIZE
        + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1
        + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH2[0x700] + Op.MSTORE
        + Op.MSTORE(offset=Op.MLOAD(offset=0x700), value=Op.ORIGIN)
        + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x700), 0x20), value=Op.MLOAD(offset=0x6e0))
        + Op.MSTORE(offset=0x4c0, value=0x2) + Op.JUMPDEST
        + Op.JUMPI(pc=0x838, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x4c0), Op.ADD(Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x6c0), 0x20)), 0x2))))
        + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x700), Op.MUL(0x20, Op.MLOAD(offset=0x4c0))), value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x6c0), Op.MUL(0x20, Op.SUB(Op.MLOAD(offset=0x4c0), 0x2)))))
        + Op.MSTORE(offset=0x4c0, value=Op.ADD(Op.MLOAD(offset=0x4c0), 0x1))
        + Op.JUMP(pc=0x7f6) + Op.JUMPDEST
        + Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x700), 0x20)))
        + Op.PUSH1[0x20] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE
        + Op.POP(Op.CALL(gas=Op.ADD(0x48, Op.DUP8), address=0x2, value=0x0, args_offset=Op.MLOAD(offset=0x700), args_size=Op.DUP4, ret_offset=Op.DUP2, ret_size=0x20))
        + Op.MLOAD(offset=Op.DUP1) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP
        + Op.PUSH2[0x760] + Op.MSTORE
        + Op.MSTORE(offset=0x7c0, value=Op.MLOAD(offset=0x760))
        + Op.RETURN(offset=0x7c0, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0xa1c, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xe346f5fc)))
        + Op.MSTORE(offset=0x7e0, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x800, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0x4c0, value=0x0) + Op.JUMPDEST + Op.PUSH1[0x60]
        + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x7e0))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP
        + Op.JUMPI(pc=0x9e6, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x4c0), Op.SLOAD(key=Op.SHA3))))
        + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x7e0))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x4c0))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MSTORE(offset=0x840, value=Op.SLOAD(key=Op.SHA3))
        + Op.MLOAD(offset=0x840) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x800))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x4c0))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x7e0))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x4c0))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x800))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x4c0))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.MLOAD(offset=0x4c0) + Op.PUSH1[0x80]
        + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x800))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x2)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x840))
        + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE
        + Op.MSTORE(offset=0x4c0, value=Op.ADD(Op.MLOAD(offset=0x4c0), 0x1))
        + Op.JUMP(pc=0x899) + Op.JUMPDEST + Op.MLOAD(offset=0x4c0) + Op.PUSH1[0x60]
        + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x800))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.MSTORE(offset=0x920, value=0x1)
        + Op.RETURN(offset=0x920, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0xb54, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x3fb57036)))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x940, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0x60]
        + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MSTORE(offset=0x960, value=Op.SLOAD(key=Op.SHA3))
        + Op.MLOAD(offset=0x960) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x2)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x940))
        + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.PUSH1[0x0]
        + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x960))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.MLOAD(offset=0x940) + Op.PUSH1[0xa0]
        + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x960))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.PUSH1[0x1] + Op.PUSH1[0x60]
        + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.ADD + Op.PUSH1[0x60] + Op.PUSH1[0x60]
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.MSTORE(offset=0xa40, value=0x1)
        + Op.RETURN(offset=0xa40, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0xbeb, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x12709a33)))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0xa60, value=Op.CALLDATALOAD(offset=0x44))
        + Op.MLOAD(offset=0xa60) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.ADD + Op.PUSH1[0xa0] + Op.PUSH1[0xa0]
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.MSTORE(offset=0xac0, value=0x1)
        + Op.RETURN(offset=0xac0, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0xc82, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x3229cf6e)))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0xa60, value=Op.CALLDATALOAD(offset=0x44))
        + Op.MLOAD(offset=0xa60) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.SUB + Op.PUSH1[0xa0] + Op.PUSH1[0xa0]
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.MSTORE(offset=0xb20, value=0x1)
        + Op.RETURN(offset=0xb20, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0xce5, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xa75f5c6a)))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0xa60, value=Op.CALLDATALOAD(offset=0x44))
        + Op.MLOAD(offset=0xa60) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.MSTORE(offset=0xb60, value=0x1)
        + Op.RETURN(offset=0xb60, size=0x20) + Op.JUMPDEST + Op.POP
    ),
        storage={0xf299dbbe3a7a5d949fe794e9a47b3106699c8110ff986eb84921c183e69e7f0: 0x2f0000000000000000, 0x1edcd36f61cae5dc6414157dfbadf9f11ca013ac763e27f8af55feaa8a239c89: 0x1, 0x689082d076ec3c02cbe4b99f6d9833e3c4a161072fd42fb7649eee5189a67ccc: 0x63524e3fe4791aefce1e932bbfb3fdf375bfad89, 0xaf1d6676be3ab502a59d91f6f5c49baffc15b2cfc65a41c4d96857c0f535adba: 0x1d60000000000000000, 0xdf1a770f69d93d1719292f384fdb4da22c0e88aef2ba462bff16674bc7848730: 0x1c11aa45c792e202e9ffdc2f12f99d0d209bef70, 0xec5e7f54fa5e516e616b04f9d5a0ee433a80e09ed47d7e5269afd76c05ff251e: 0x2},
    )
    pre[callee_10] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.MSTORE8(offset=0x67f, value=0x0)
        + Op.DIV(Op.CALLDATALOAD(offset=0x0), 0x100000000000000000000000000000000000000000000000000000000)
        + Op.JUMPI(pc=Op.PUSH2[0xac], condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x2f300bee)))
        + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x44))
        + Op.ADD(Op.MLOAD(offset=0x80), 0x2) + Op.DUP1
        + Op.ADD(0x20, Op.MUL(0x20, Op.DUP1)) + Op.MSIZE + Op.SWAP1 + Op.MSIZE
        + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1
        + Op.POP + Op.SWAP1 + Op.POP
        + Op.MSTORE(offset=Op.DUP2, value=0x10000000000000000)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, Op.MUL(0x20, Op.MLOAD(offset=0x80))), value=Op.MLOAD(offset=0x60))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, Op.MUL(0x20, Op.ADD(Op.MLOAD(offset=0x80), 0x1))), value=Op.SUB(Op.MLOAD(offset=0x40), 0x1))
        + Op.DUP1 + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20)
        + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20)))
        + Op.POP + Op.POP + Op.POP + Op.JUMPDEST
        + Op.JUMPI(pc=0x2c8, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xa647a5b9)))
        + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE
        + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE)
        + Op.MSTORE(offset=0x100, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x4)))
        + Op.MSTORE(offset=0x160, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x24)))
        + Op.MSTORE(offset=0x180, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x44)))
        + Op.MSTORE(offset=0x1a0, value=Op.CALLDATALOAD(offset=0x64))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x84)) + Op.POP
        + Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x100), 0x20)) + Op.DUP1
        + Op.ADD(0x20, Op.MUL(0x20, Op.DUP1)) + Op.MSIZE + Op.SWAP1 + Op.MSIZE
        + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1
        + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x1d5, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.MLOAD(offset=0x1a0))))
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x162, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.MLOAD(offset=0x80))))
        + Op.ADD(Op.DUP3, Op.MUL(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x160), Op.MUL(0x20, Op.ADD(Op.MUL(Op.DUP6, Op.MLOAD(offset=0x80)), Op.DUP2)))), Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x100), Op.MUL(0x20, Op.DUP1)))))
        + Op.SWAP2 + Op.POP + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP
        + Op.JUMP(pc=0x12e) + Op.JUMPDEST + Op.POP
        + Op.SDIV(Op.DUP2, 0x10000000000000000) + Op.SWAP1 + Op.POP + Op.PUSH1[0x0]
        + Op.JUMPDEST
        + Op.JUMPI(pc=0x1c8, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.MLOAD(offset=0x80))))
        + Op.MSTORE(offset=Op.ADD(Op.DUP6, Op.MUL(0x20, Op.DUP2)), value=Op.SUB(Op.MLOAD(offset=Op.ADD(Op.DUP6, Op.MUL(0x20, Op.DUP2))), Op.SDIV(Op.MUL(Op.MUL(Op.DUP5, Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x160), Op.MUL(0x20, Op.ADD(Op.MUL(Op.DUP7, Op.MLOAD(offset=0x80)), Op.DUP3))))), Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x180), Op.MUL(0x20, Op.DUP4)))), 0x100000000000000000000000000000000)))
        + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x174) + Op.JUMPDEST
        + Op.POP + Op.POP + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP
        + Op.JUMP(pc=0x11e) + Op.JUMPDEST + Op.POP + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.JUMPDEST
        + Op.JUMPI(pc=0x203, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.MLOAD(offset=0x80))))
        + Op.ADD(Op.DUP3, Op.MUL(Op.MLOAD(offset=Op.ADD(Op.DUP5, Op.MUL(0x20, Op.DUP2))), Op.MLOAD(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP1)))))
        + Op.SWAP2 + Op.POP + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP
        + Op.JUMP(pc=0x1db) + Op.JUMPDEST + Op.POP
        + Op.SDIV(Op.DUP2, 0x10000000000000000) + Op.SWAP1 + Op.POP
        + Op.SDIV(Op.DUP2, 0x2) + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x242, condition=Op.ISZERO(Op.SLT(Op.DUP2, 0xb)))
        + Op.SDIV(Op.ADD(Op.DUP4, Op.SDIV(Op.MUL(Op.DUP6, 0x10000000000000000), Op.DUP3)), 0x2)
        + Op.SWAP2 + Op.POP + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP
        + Op.JUMP(pc=0x219) + Op.JUMPDEST + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x276, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.MLOAD(offset=0x80))))
        + Op.MSTORE(offset=Op.ADD(Op.DUP6, Op.MUL(0x20, Op.DUP2)), value=Op.SDIV(Op.MUL(Op.MLOAD(offset=Op.ADD(Op.DUP7, Op.MUL(0x20, Op.DUP3))), 0x10000000000000000), Op.DUP2))
        + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x246) + Op.JUMPDEST
        + Op.POP + Op.POP + Op.POP
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, Op.MUL(0x20, Op.MLOAD(offset=0x80))), value=Op.SUB(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x100), Op.MUL(0x20, Op.MLOAD(offset=0x80)))), 0x1))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, Op.MUL(0x20, Op.ADD(Op.MLOAD(offset=0x80), 0x1))), value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x100), Op.MUL(0x20, Op.ADD(Op.MLOAD(offset=0x80), 0x1)))))
        + Op.DUP1 + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20)
        + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20)))
        + Op.POP + Op.POP + Op.POP + Op.JUMPDEST
        + Op.JUMPI(pc=0x379, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x5b180229)))
        + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE
        + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE)
        + Op.MSTORE(offset=0x300, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x4)))
        + Op.MSTORE(offset=0x320, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x24)))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x44)) + Op.POP
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x33f, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.MLOAD(offset=0x80))))
        + Op.ADD(Op.DUP3, Op.SDIV(Op.MUL(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x300), Op.MUL(0x20, Op.DUP3))), Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x320), Op.MUL(0x20, Op.DUP2)))), 0x10000000000000000))
        + Op.SWAP2 + Op.POP + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP
        + Op.JUMP(pc=0x306) + Op.JUMPDEST
        + Op.JUMPI(pc=0x366, condition=Op.ISZERO(Op.ISZERO(Op.EQ(Op.MLOAD(offset=Op.MLOAD(offset=0x320)), 0x0))))
        + Op.SDIV(Op.MUL(Op.DUP4, 0x10000000000000000), Op.MLOAD(offset=Op.MLOAD(offset=0x320)))
        + Op.SWAP2 + Op.POP + Op.JUMP(pc=0x36b) + Op.JUMPDEST + Op.PUSH1[0x0]
        + Op.SWAP2 + Op.POP + Op.JUMPDEST + Op.MSTORE(offset=0x380, value=Op.DUP2)
        + Op.RETURN(offset=0x380, size=0x20) + Op.POP + Op.POP + Op.JUMPDEST
        + Op.JUMPI(pc=0x571, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xf4ca7dc4)))
        + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE
        + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE)
        + Op.MSTORE(offset=0x3a0, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x4)))
        + Op.MSTORE(offset=0x3c0, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x24)))
        + Op.MSTORE(offset=0x1a0, value=Op.CALLDATALOAD(offset=0x44))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x64)) + Op.POP
        + Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x3c0), 0x20))
        + Op.EXP(Op.MLOAD(offset=0x80), 0x2) + Op.ADD(0x20, Op.MUL(0x20, Op.DUP1))
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20)
        + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x44d, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.MLOAD(offset=0x80))))
        + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x441, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.MLOAD(offset=0x80))))
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, Op.MUL(0x20, Op.ADD(Op.MUL(Op.DUP5, Op.MLOAD(offset=0x80)), Op.DUP2))), value=Op.ADD(Op.MLOAD(offset=Op.ADD(Op.DUP5, Op.MUL(0x20, Op.ADD(Op.MUL(Op.DUP5, Op.MLOAD(offset=0x80)), Op.DUP2)))), Op.SDIV(Op.MUL(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x3a0), Op.MUL(0x20, Op.DUP4))), Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x3a0), Op.MUL(0x20, Op.DUP2)))), 0x10000000000000000)))
        + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x3f1) + Op.JUMPDEST
        + Op.POP + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x3e4)
        + Op.JUMPDEST + Op.DUP2 + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.DUP2
        + Op.ADD(0x20, Op.MUL(0x20, Op.DUP1)) + Op.MSIZE + Op.SWAP1 + Op.MSIZE
        + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1
        + Op.POP + Op.SWAP1 + Op.POP
        + Op.MUL(Op.MLOAD(offset=0x1a0), Op.MLOAD(offset=0x80))
        + Op.ADD(0x20, Op.MUL(0x20, Op.DUP1)) + Op.MSIZE + Op.SWAP1 + Op.MSIZE
        + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1
        + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x51e, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.MLOAD(offset=0x1a0))))
        + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x512, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.MLOAD(offset=0x80))))
        + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x506, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.MLOAD(offset=0x80))))
        + Op.MSTORE(offset=Op.ADD(Op.DUP6, Op.MUL(0x20, Op.ADD(Op.MUL(Op.DUP6, Op.MLOAD(offset=0x80)), Op.DUP3))), value=Op.ADD(Op.MLOAD(offset=Op.ADD(Op.DUP6, Op.MUL(0x20, Op.ADD(Op.MUL(Op.DUP6, Op.MLOAD(offset=0x80)), Op.DUP3)))), Op.SDIV(Op.MUL(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x3c0), Op.MUL(0x20, Op.ADD(Op.MUL(Op.DUP7, Op.MLOAD(offset=0x80)), Op.DUP3)))), Op.MLOAD(offset=Op.ADD(Op.DUP8, Op.MUL(0x20, Op.ADD(Op.MUL(Op.DUP4, Op.MLOAD(offset=0x80)), Op.DUP3))))), 0x10000000000000000)))
        + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x4ad) + Op.JUMPDEST
        + Op.POP + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x4a0)
        + Op.JUMPDEST + Op.POP + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP
        + Op.JUMP(pc=0x492) + Op.JUMPDEST + Op.DUP2 + Op.SWAP1 + Op.POP + Op.SWAP1
        + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x552, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DUP5)))
        + Op.MSTORE(offset=Op.ADD(Op.DUP5, Op.MUL(0x20, Op.DUP2)), value=Op.SUB(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x3c0), Op.MUL(0x20, Op.DUP2))), Op.MLOAD(offset=Op.ADD(Op.DUP3, Op.MUL(0x20, Op.DUP1)))))
        + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x526) + Op.JUMPDEST
        + Op.POP + Op.DUP2 + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20)
        + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20)))
        + Op.POP + Op.POP + Op.POP + Op.POP + Op.POP + Op.JUMPDEST
        + Op.JUMPI(pc=0x69d, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x232b2734)))
        + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE
        + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE)
        + Op.MSTORE(offset=0x620, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x4)))
        + Op.MSTORE(offset=0x280, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x24)))
        + Op.MSTORE(offset=0x3c0, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x44)))
        + Op.MSTORE(offset=0x640, value=Op.CALLDATALOAD(offset=0x64))
        + Op.MSTORE(offset=0x1a0, value=Op.CALLDATALOAD(offset=0x84))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0xa4)) + Op.POP
        + Op.JUMPI(pc=0x602, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=Op.MLOAD(offset=0x280)), 0x0)))
        + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x600, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.MLOAD(offset=0x80))))
        + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x280), Op.MUL(0x20, Op.DUP2)), value=Op.SUB(0x0, Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x280), Op.MUL(0x20, Op.DUP1)))))
        + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x5d4) + Op.JUMPDEST
        + Op.POP + Op.JUMPDEST + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x67f, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.MLOAD(offset=0x1a0))))
        + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x673, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.MLOAD(offset=0x80))))
        + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x620), Op.MUL(0x20, Op.DUP3)), value=Op.ADD(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x620), Op.MUL(0x20, Op.DUP3))), Op.SDIV(Op.MUL(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x3c0), Op.MUL(0x20, Op.ADD(Op.MUL(Op.DUP6, Op.MLOAD(offset=0x80)), Op.DUP3)))), Op.SDIV(Op.MUL(Op.MLOAD(offset=0x640), Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x280), Op.MUL(0x20, Op.DUP3)))), 0x10000000000000000)), 0x10000000000000000)))
        + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x613) + Op.JUMPDEST
        + Op.POP + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x605)
        + Op.JUMPDEST + Op.MLOAD(offset=0x620)
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20)
        + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20)))
        + Op.POP + Op.POP + Op.JUMPDEST + Op.POP
    ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=bytes.fromhex("36a560bd00000000000000000000000000000000000000000000000000000000000f69b5"),
        gas_limit=3000000,
        gas_price=10000000000000,
        nonce=0,
        value=0,
    )

    post = {
        callee_5: Account(
            storage={0x65d5efdfcc0fba693dc9e467f633097ffdc97401901463ad0e28855486d1edf: 0xb9d69098a6acfe0c6411bcaaf430f78d363a9adc32b78bc2e15ccd6e883e9784, 0x12643ff300762717d27efb567b82c65560d7b43249d908504e5510863ab82aac: 0x154cf60e137c594516a065149610b6a3989396a42581d5fd8919e711c55da225, 0x1489023d18c5d10427c4aa8dc726e840eb5ae7f604a8e9243c61634fb009e4d7: 5, 0x1489023d18c5d10427c4aa8dc726e840eb5ae7f604a8e9243c61634fb009e4d8: 1, 0x19efb13d6576359514ace5211988a8d51379fa88ccd2b886b409f842b13d7932: 0xc849cc595b452d11c206d2eb8cdfa06de211e3ff19ee0e0276dc857c05d4fe, 0x1b37e91bf8580c7c6bcf8cdff25c7ed78180124a94af6f30c40d476a3d079ad6: 0xaba4cd295118a482a0a62579e35e4ba5bdd76146cc9e4d96172fce8be8977ab4, 0x2bf9fd8facdd6fd9c84657f5ad7381a5aecf670cda68cb3c5829b6532c865506: 0x53098a1d111586dbcc0d051846284f5803c63c313e7f7e6d84430435d11d4c50, 0x3111bfd25728c0adfad0f8c1ad79cb1b91167267deca98de88f156ed25caeedc: 0xad393086f30b49511b08fdd27ac78810b084c7cd7de6ac354f614c18ea9e7df4, 0x3379e7ae125c5c5d623d1d993c1459b61d6723b1c30d1aa026c48f6a6155b8ea: 0x8c4183732567a99a8a718e363391e102532f9a640e42968cf2354d9acc908bb0, 0x34cabe0c7e64a2caa93fd8d6a0defc07acb9d44b13430fa3ae9282fffd40dee2: 1, 0x34cabe0c7e64a2caa93fd8d6a0defc07acb9d44b13430fa3ae9282fffd40dee3: 1, 0x34cabe0c7e64a2caa93fd8d6a0defc07acb9d44b13430fa3ae9282fffd40dee4: 1, 0x34cabe0c7e64a2caa93fd8d6a0defc07acb9d44b13430fa3ae9282fffd40dee5: 1, 0x39050607fe892059a6344ab0f594f382fb0b345cab373497246dbe86fe7e14e7: 0x2b3bca833e482737e7e47b1568e6f890f8e1666490d38fe130abd6f0ccb109cf, 0x417be8bc6791807372e0222a350bb8a5d67bbc8d7595c301d8a5a8372cfdcef1: 0xabd4971b4605a7155802f70e08298b1ceb0e4e4eaccccd348f77a77227f73a7f, 0x41e9a54b3ee0c276aa076babb161de12b0f8916b47f8f6fb85cc387cf34696dd: 0x22f2f444ebda9d2913ffef5059b039ec9b5876aa71821991c2515bf79f64935e, 0x45ceb8da6fb8936592d3bce4883f1a6a34d636f559e0a1070a5802a65ac39bd5: 0x57a5122ff3bf737b0de0f9f08011a8648c19e43ff071fb7086234723c9383f1f, 0x4aa6b934608a45c8f53a945c05ddee1814a3b9f63a048fc7ad3d47e67156f024: 0xd03862becedada67b4825a0238f3e67495ccb595cd7d08f1bd5d3160644b9299, 0x4b8b58f0b0e326a5907d1a810e5ff31e05b4cab45125b776db8577e7dbc46bce: 0x2f0000000000000000, 0x4c33460347337bfc7df08bf182988301b7b426a27a67f1c6c634f637c60e87ac: 0xbab4ab2ad4eafe7c84ef6a8cd69157d9ce6b843793a2cd0877b8e91f63cb2d4d, 0x58da0c0c256bba101ce36fad8bf838717a57e6ab850a191dc9c09da9ce56bf1b: 5, 0x5cb38b16db1d632086d4af695de7f5f242a6e40947067f96edd566fe2ac438ef: 0x6d0be832b2007ea28cda705b73922cbf9794c5a25b89bd2f28b7347ed2b96c86, 0x64a9621cc4ba92bf738c55010c609dfaa3972a1138c30b5adcef1ba2363b360e: 0xd7953bfe8cb591f129fd0862a9e9c421151e2b5831560ff5215d23f751364b35, 0x696664a5f0ab5acd9304a377fb684f2d3fe6bb60b8a95cb2bdbb57db767e7a84: 0x154cf60e137c594516a065149610b6a3989396a42581d5fd8919e711c55da225, 0x69ad1d19e617936abdf05133bf268dc8ced6b518f22b249b5860967d07006487: 0x8c803b48b383ddabd1b3afe858efb48c203229b7317dd76149dddab4253b858a, 0x70b3bf53996fac325eb67608a4eeb0cd0b55def6255d7ed42ad28ec07238b5d6: 0x45e9723e9232b37207ecac1c97b8647d053625a578d450f7456280b2ff8efc27, 0x7a9dcee62e3e02cc8e020f372df2efdeb835f091c1ef1dbe221072d1095aabd2: 0x2f0000000000000000, 0x7e4d8c0f6d8abb4ce1ae45b254046aceedabfa9548851b8b5d3e2c0637c985fd: 11, 0x7e95f3cc3315d289c52253baaba29b1b00c86816e6b788d50795279a8baa00db: 0x45e9723e9232b37207ecac1c97b8647d053625a578d450f7456280b2ff8efc27, 0x8da187157087529ee4e9c381f8e3149c56acf3bdfda29b8b9b4532f24b83f5fe: 0x8c4183732567a99a8a718e363391e102532f9a640e42968cf2354d9acc908bb0, 0x9001f91ddaef87bc067886e874c0749998c9b58b2ec8472ca014ca8b55f88578: 0xfb76974eefca01f33fb38646c2d3c1536f1a763d7aff53ab7f877d4c5ea7fd0, 0x9ed0cedd2a9a78d949f40019f53d10031aef6ed342c97e01fc03b481ee56b3cb: 4, 0x9fddf1db29caa5c1239edd86e9e0835cdfe41f7253ec78f62d3da8558d6f3cd7: 0x104eef8fa35bf39f677d81855bc0b9f42317f32792e98e95e4df441deb634211, 0xa0953566119395c11186b334805fc1a16175ecac0ecc93ae0322264f0dc2e40d: 0x10c5a00466ab7c0adae1e93537cc275ea8cf23ff509d5466a1fd6f56b0a61d1b, 0xaa0dbf8241ef3ae07c254e6869e84895ba2be0779a7f261c8308a3114be1c54a: 4, 0xaffe808b495d13a14391ce5f27c211c36da12826969cd7841ee0d81e5b900e2d: 1, 0xaffe808b495d13a14391ce5f27c211c36da12826969cd7841ee0d81e5b900e2e: 1, 0xb4a2b68c48ef78aeb641ee538fad51781022fd23ed9d93d211017db6a02376ce: 0xfbc06642245cf2fed7ed46ea0a18a7185830b6f2c4e0a4ca55246041e8bfa72, 0xba8d79990898383919e437f2458b93b340072c89d963808d9e04f51858e3c5ec: 0x41d2cac534d90a0dbd199117481a63e32cc11411dab2eaa36c91c0eec62823cf, 0xbb3bc1a2015123750df57d4ceff7e28cb847910b79b34841de905b59a8bb177c: 0x734417eb19e1873427257f1ea1594748c16cfa866a7b7cf896e281f2ec774a40, 0xbf30cdcb83ab2bd5f5eee691ffa4107b58b75ba6a5c2e6754d4c5c0437f2876c: 5, 0xc2a26b80067fc36b8268b0d5b31afff953fa91cebea39f191e2763d6e71259b9: 0x2a43c547fe8de2400d2a141016550e8bae058d41164247c099e787ddd40e789, 0xc98339d275eef16e0562ca8521212cef61aa0f39b12e2a27502aaa97a9e5e70f: 0x5a3de2a5c268cdb75f4b01507aa80c4e4a1bc67bcb0df265bbb00060774e5978, 0xcbd6ae6bd61bc9270ec836f1919b3268113abe076c7febfdb8cf573b199ce9a9: 0xf402b17773c1f7534034ee58dc0d2a3421470a7a67daf4fa790dc3b420eef790, 0xd2c8cbb562fccd0c9a3d0d491b7f65cc6a89856498f933427d9d21b745b9d50e: 0x3625a26fdb7b747501f1ee2500f98c49d9cd290383a21254587c3c49d2805321, 0xd66f52a4e24585238ccc03443b2fdb8b2b100259bc7260f39097c7c339211ffe: 0x1641851904381915c86b60df7e288896fb5f8ebad65d594829fb9f2b59cd1da6, 0xd8f720c05a5526dd621d1831ae122abddd3dfecd8b63b0ba4c92fa7b2ade44ff: 0xad393086f30b49511b08fdd27ac78810b084c7cd7de6ac354f614c18ea9e7df4, 0xdc22d3171b82817c910bbeac1f8b50c8de99f8c524f172aef3491981bd5ed4fb: 0x94b8cba4ea090d1c392fbc94b82fb9ef9f468a15bbc537f4d051776f4d422b1d, 0xdce8adbdefa929dbe60245f359446db4174c62824b42e5d4d9e7b834b4d61deb: 0x2c9069845b2e74c577ff1cd18df6bc452805f527a9ee91fd4a059e0408b5dea6, 0xdd9493073db9e42fd955e834c89a74089f99196186ee0b2688124989be00d196: 1, 0xdd9493073db9e42fd955e834c89a74089f99196186ee0b2688124989be00d197: 1, 0xdd9493073db9e42fd955e834c89a74089f99196186ee0b2688124989be00d198: 1, 0xdd9493073db9e42fd955e834c89a74089f99196186ee0b2688124989be00d199: 1, 0xdd9493073db9e42fd955e834c89a74089f99196186ee0b2688124989be00d19a: 1, 0xe54f074c81bfa60b5bf413934c108086298b77291560edfeead8aa1232e95236: 0xf40aaa24323c9e6983ccffafeebe4b426509b901e8c98b8a40d881804804e6b, 0xe66c0f55f66c752edf73027d45b7b1ae729ae15e1c67c362dbc6f25edf8d76ff: 1, 0xe983d899f807bbcb5881f2ddf875b2ebb5cb8a7a4e77a8c98a40aaae6a468735: 0x6d0be832b2007ea28cda705b73922cbf9794c5a25b89bd2f28b7347ed2b96c86, 0xed7d6e2d40fbd5046412ffad1c45b63d87c6197182d6dbc66bb1e5c6e4ded5c7: 0xaba4cd295118a482a0a62579e35e4ba5bdd76146cc9e4d96172fce8be8977ab4, 0xf043b5a1952847579f233706a8f130889a484d2da3e574fdd5859f05aaf52111: 2, 0xf40f4cfdacb62dd799f36b580349fac1f4a4caf8dd3383cc387c35adb6574e21: 0x2f0000000000000000, 0xf60fa6e25e9028a6dc6b26bbc1eadae3da157df0d1d6f6628bc33cad68a7e455: 0x2d7d00618c059ebe40593b9497c633e1ac6e161dadbd5bb734c2663cd3e8a8e1, 0xfd280ac5182d5b2366122f38acfa6dc471240ffde9d5feb985ce7a2325c960e7: 3},
            code=Op.MSTORE8(offset=0x289f, value=0x0) + Op.DIV(Op.CALLDATALOAD(offset=0x0), 0x100000000000000000000000000000000000000000000000000000000) + Op.MSTORE(offset=0x20, value=0xc9ae5868651bf7b7db6e360217db49ce4e69c07e) + Op.JUMPI(pc=0x127, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xc4982a85))) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=0xa0, value=Op.SLOAD(key=Op.SHA3)) + Op.MLOAD(offset=0xa0) + Op.ADD(0x20, Op.MUL(0x20, Op.DUP1)) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0xe0] + Op.MSTORE + Op.MSTORE(offset=0x140, value=0x0) + Op.JUMPDEST + Op.JUMPI(pc=0x10b, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x140), Op.MLOAD(offset=0xa0)))) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x1) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=Op.MLOAD(offset=0x140)) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0xe0), Op.MUL(0x20, Op.MLOAD(offset=0x140))), value=Op.SLOAD(key=Op.SHA3)) + Op.MSTORE(offset=0x140, value=Op.ADD(Op.MLOAD(offset=0x140), 0x1)) + Op.JUMP(pc=Op.PUSH2[0xad]) + Op.JUMPDEST + Op.MLOAD(offset=0xe0) + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20) + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20))) + Op.POP + Op.JUMPDEST + Op.JUMPI(pc=0x176, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xcc1c944e))) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=0x1a0, value=Op.SLOAD(key=Op.SHA3)) + Op.RETURN(offset=0x1a0, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x1d5, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x95a405b9))) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x1e0, value=Op.CALLDATALOAD(offset=0x44)) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x1) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=Op.MLOAD(offset=0x1e0)) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=0x200, value=Op.SLOAD(key=Op.SHA3)) + Op.RETURN(offset=0x200, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x224, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x71ebb662))) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x2) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=0x240, value=Op.SLOAD(key=Op.SHA3)) + Op.RETURN(offset=0x240, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x325, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x7a57a3db))) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x280, value=Op.CALLDATALOAD(offset=0x44)) + Op.PUSH1[0xc0] + Op.PUSH1[0xc0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x3) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=Op.MLOAD(offset=0x280)) + Op.MSTORE(offset=Op.ADD(0xa0, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MUL(0x20, Op.SLOAD(key=Op.SHA3)) + Op.DUP1 + Op.ADD(0x20, Op.DUP1) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x2e9, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DIV(Op.DUP4, 0x20)))) + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.SLOAD(key=Op.ADD(Op.DUP5, Op.DUP1))) + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x2c8) + Op.JUMPDEST + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.AND(Op.SLOAD(key=Op.ADD(Op.DUP6, Op.DUP2)), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20)))))) + Op.DUP2 + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20) + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20))) + Op.POP + Op.JUMPDEST + Op.JUMPI(pc=0x394, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xf73dc690))) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x3c0, value=Op.CALLDATALOAD(offset=0x44)) + Op.MSTORE(offset=0x3e0, value=Op.CALLDATALOAD(offset=0x64)) + Op.PUSH1[0xc0] + Op.PUSH1[0xc0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x3) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=Op.MLOAD(offset=0x3c0)) + Op.MSTORE(offset=Op.ADD(0xa0, Op.DUP2), value=Op.MLOAD(offset=0x3e0)) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=0x400, value=Op.SLOAD(key=Op.SHA3)) + Op.RETURN(offset=0x400, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x3f3, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x54cc6109))) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x3c0, value=Op.CALLDATALOAD(offset=0x44)) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x4) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=Op.MLOAD(offset=0x3c0)) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=0x440, value=Op.SLOAD(key=Op.SHA3)) + Op.RETURN(offset=0x440, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x442, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xc63ef546))) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x5) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=0x480, value=Op.SLOAD(key=Op.SHA3)) + Op.RETURN(offset=0x480, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x533, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x9381779b))) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x6) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x5) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MUL(0x20, Op.SLOAD(key=Op.SHA3)) + Op.DUP1 + Op.ADD(0x20, Op.DUP1) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x4f7, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DIV(Op.DUP4, 0x20)))) + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.SLOAD(key=Op.ADD(Op.DUP5, Op.DUP1))) + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x4d6) + Op.JUMPDEST + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.AND(Op.SLOAD(key=Op.ADD(Op.DUP6, Op.DUP2)), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20)))))) + Op.DUP2 + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20) + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20))) + Op.POP + Op.JUMPDEST + Op.JUMPI(pc=0x624, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x4f9c6eeb))) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x7) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x5) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MUL(0x20, Op.SLOAD(key=Op.SHA3)) + Op.DUP1 + Op.ADD(0x20, Op.DUP1) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x5e8, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DIV(Op.DUP4, 0x20)))) + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.SLOAD(key=Op.ADD(Op.DUP5, Op.DUP1))) + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x5c7) + Op.JUMPDEST + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.AND(Op.SLOAD(key=Op.ADD(Op.DUP6, Op.DUP2)), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20)))))) + Op.DUP2 + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20) + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20))) + Op.POP + Op.JUMPDEST + Op.JUMPI(pc=0x715, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x7dc12195))) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x8) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x5) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MUL(0x20, Op.SLOAD(key=Op.SHA3)) + Op.DUP1 + Op.ADD(0x20, Op.DUP1) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x6d9, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DIV(Op.DUP4, 0x20)))) + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.SLOAD(key=Op.ADD(Op.DUP5, Op.DUP1))) + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x6b8) + Op.JUMPDEST + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.AND(Op.SLOAD(key=Op.ADD(Op.DUP6, Op.DUP2)), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20)))))) + Op.DUP2 + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20) + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20))) + Op.POP + Op.JUMPDEST + Op.JUMPI(pc=0x806, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xfa9832d1))) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x9) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MUL(0x20, Op.SLOAD(key=Op.SHA3)) + Op.DUP1 + Op.ADD(0x20, Op.DUP1) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x7ca, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DIV(Op.DUP4, 0x20)))) + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.SLOAD(key=Op.ADD(Op.DUP5, Op.DUP1))) + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x7a9) + Op.JUMPDEST + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.AND(Op.SLOAD(key=Op.ADD(Op.DUP6, Op.DUP2)), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20)))))) + Op.DUP2 + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20) + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20))) + Op.POP + Op.JUMPDEST + Op.JUMPI(pc=0x8f7, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x2c5a40d5))) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0xa) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x5) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MUL(0x20, Op.SLOAD(key=Op.SHA3)) + Op.DUP1 + Op.ADD(0x20, Op.DUP1) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x8bb, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DIV(Op.DUP4, 0x20)))) + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.SLOAD(key=Op.ADD(Op.DUP5, Op.DUP1))) + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x89a) + Op.JUMPDEST + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.AND(Op.SLOAD(key=Op.ADD(Op.DUP6, Op.DUP2)), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20)))))) + Op.DUP2 + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20) + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20))) + Op.POP + Op.JUMPDEST + Op.JUMPI(pc=0x9eb, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xe05dcb56))) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0xb) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.PUSH1[0x2] + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MUL(0x20, Op.SLOAD(key=Op.SHA3)) + Op.ADD + Op.DUP1 + Op.ADD(0x20, Op.DUP1) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x9af, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DIV(Op.DUP4, 0x20)))) + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.SLOAD(key=Op.ADD(Op.DUP5, Op.DUP1))) + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x98e) + Op.JUMPDEST + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.AND(Op.SLOAD(key=Op.ADD(Op.DUP6, Op.DUP2)), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20)))))) + Op.DUP2 + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20) + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20))) + Op.POP + Op.JUMPDEST + Op.JUMPI(pc=0xa3a, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x586b5be0))) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0xc) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=0xb80, value=Op.SLOAD(key=Op.SHA3)) + Op.RETURN(offset=0xb80, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0xb58, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xeb8af5aa))) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0xd) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x5) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.MUL(0x20, Op.SDIV) + Op.DUP1 + Op.ADD(0x20, Op.DUP1) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0xb1c, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DIV(Op.DUP4, 0x20)))) + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.SLOAD(key=Op.ADD(Op.DUP5, Op.DUP1))) + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0xafb) + Op.JUMPDEST + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.AND(Op.SLOAD(key=Op.ADD(Op.DUP6, Op.DUP2)), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20)))))) + Op.DUP2 + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20) + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20))) + Op.POP + Op.JUMPDEST + Op.JUMPI(pc=0xc76, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x7ab6ea8a))) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0xe) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x5) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.MUL(0x20, Op.SDIV) + Op.DUP1 + Op.ADD(0x20, Op.DUP1) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0xc3a, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DIV(Op.DUP4, 0x20)))) + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.SLOAD(key=Op.ADD(Op.DUP5, Op.DUP1))) + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0xc19) + Op.JUMPDEST + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.AND(Op.SLOAD(key=Op.ADD(Op.DUP6, Op.DUP2)), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20)))))) + Op.DUP2 + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20) + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20))) + Op.POP + Op.JUMPDEST + Op.JUMPI(pc=0xd94, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x2b810cb9))) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0xf) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x5) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.MUL(0x20, Op.SDIV) + Op.DUP1 + Op.ADD(0x20, Op.DUP1) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0xd58, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DIV(Op.DUP4, 0x20)))) + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.SLOAD(key=Op.ADD(Op.DUP5, Op.DUP1))) + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0xd37) + Op.JUMPDEST + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.AND(Op.SLOAD(key=Op.ADD(Op.DUP6, Op.DUP2)), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20)))))) + Op.DUP2 + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20) + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20))) + Op.POP + Op.JUMPDEST + Op.JUMPI(pc=0xe85, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x7fb42e46))) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x10) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MUL(0x20, Op.SLOAD(key=Op.SHA3)) + Op.DUP1 + Op.ADD(0x20, Op.DUP1) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0xe49, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DIV(Op.DUP4, 0x20)))) + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.SLOAD(key=Op.ADD(Op.DUP5, Op.DUP1))) + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0xe28) + Op.JUMPDEST + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.AND(Op.SLOAD(key=Op.ADD(Op.DUP6, Op.DUP2)), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20)))))) + Op.DUP2 + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20) + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20))) + Op.POP + Op.JUMPDEST + Op.JUMPI(pc=0xf76, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x734fa727))) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x11) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MUL(0x20, Op.SLOAD(key=Op.SHA3)) + Op.DUP1 + Op.ADD(0x20, Op.DUP1) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0xf3a, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DIV(Op.DUP4, 0x20)))) + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.SLOAD(key=Op.ADD(Op.DUP5, Op.DUP1))) + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0xf19) + Op.JUMPDEST + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.AND(Op.SLOAD(key=Op.ADD(Op.DUP6, Op.DUP2)), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20)))))) + Op.DUP2 + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20) + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20))) + Op.POP + Op.JUMPDEST + Op.JUMPI(pc=0x1067, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xc67fa857))) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x12) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MUL(0x20, Op.SLOAD(key=Op.SHA3)) + Op.DUP1 + Op.ADD(0x20, Op.DUP1) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x102b, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DIV(Op.DUP4, 0x20)))) + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.SLOAD(key=Op.ADD(Op.DUP5, Op.DUP1))) + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x100a) + Op.JUMPDEST + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.AND(Op.SLOAD(key=Op.ADD(Op.DUP6, Op.DUP2)), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20)))))) + Op.DUP2 + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20) + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20))) + Op.POP + Op.JUMPDEST + Op.JUMPI(pc=0x1185, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x5ed853e4))) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x13) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x5) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.MUL(0x20, Op.SDIV) + Op.DUP1 + Op.ADD(0x20, Op.DUP1) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x1149, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DIV(Op.DUP4, 0x20)))) + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.SLOAD(key=Op.ADD(Op.DUP5, Op.DUP1))) + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x1128) + Op.JUMPDEST + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.AND(Op.SLOAD(key=Op.ADD(Op.DUP6, Op.DUP2)), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20)))))) + Op.DUP2 + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20) + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20))) + Op.POP + Op.JUMPDEST + Op.JUMPI(pc=0x12a3, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xb86f5125))) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x14) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x5) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.MUL(0x20, Op.SDIV) + Op.DUP1 + Op.ADD(0x20, Op.DUP1) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x1267, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DIV(Op.DUP4, 0x20)))) + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.SLOAD(key=Op.ADD(Op.DUP5, Op.DUP1))) + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x1246) + Op.JUMPDEST + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.AND(Op.SLOAD(key=Op.ADD(Op.DUP6, Op.DUP2)), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20)))))) + Op.DUP2 + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20) + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20))) + Op.POP + Op.JUMPDEST + Op.JUMPI(pc=0x1394, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xbc3d7d85))) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x15) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MUL(0x20, Op.SLOAD(key=Op.SHA3)) + Op.DUP1 + Op.ADD(0x20, Op.DUP1) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x1358, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DIV(Op.DUP4, 0x20)))) + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.SLOAD(key=Op.ADD(Op.DUP5, Op.DUP1))) + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x1337) + Op.JUMPDEST + Op.MSTORE(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)), value=Op.AND(Op.SLOAD(key=Op.ADD(Op.DUP6, Op.DUP2)), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20)))))) + Op.DUP2 + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20) + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20))) + Op.POP + Op.JUMPDEST + Op.JUMPI(pc=0x1481, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xa2302f2f))) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x1680, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x16a0, value=Op.CALLDATALOAD(offset=0x44)) + Op.MLOAD(offset=0x16a0) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x1680)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x1) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x1680)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=Op.SLOAD(key=Op.SHA3)) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.PUSH1[0x1] + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x1680)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.ADD + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x1680)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.MSTORE(offset=0x1740, value=0x1) + Op.RETURN(offset=0x1740, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x14dd, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x58ca2bc))) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x1760, value=Op.CALLDATALOAD(offset=0x44)) + Op.MLOAD(offset=0x1760) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x2) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.MSTORE(offset=0x17a0, value=0x1) + Op.RETURN(offset=0x17a0, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x1617, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x5d3b965b))) + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x280, value=Op.CALLDATALOAD(offset=0x44)) + Op.MSTORE(offset=0x17e0, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x64))) + Op.MSTORE(offset=0x1800, value=Op.CALLDATALOAD(offset=0x84)) + Op.POP + Op.PUSH1[0xc0] + Op.PUSH1[0xc0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x3) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=Op.MLOAD(offset=0x280)) + Op.MSTORE(offset=Op.ADD(0xa0, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x17e0), 0x20))) + Op.DIV(Op.DUP2, 0x20) + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x158c, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DUP2))) + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x17e0), Op.MUL(0x20, Op.DUP1)))) + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x156b) + Op.JUMPDEST + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.AND(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x17e0), Op.MUL(0x20, Op.DUP2))), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20)))))) + Op.POP + Op.POP + Op.POP + Op.POP + Op.MLOAD(offset=0x1800) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x2) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.ADD + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x2) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.MSTORE(offset=0x1900, value=0x1) + Op.RETURN(offset=0x1900, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x1673, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xb0e14f0f))) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x1920, value=Op.CALLDATALOAD(offset=0x44)) + Op.MLOAD(offset=0x1920) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x5) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.MSTORE(offset=0x1960, value=0x1) + Op.RETURN(offset=0x1960, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x1739, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x6acccdbc))) + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x1980, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x44))) + Op.POP + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x6) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x1980), 0x20))) + Op.DIV(Op.DUP2, 0x20) + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x170b, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DUP2))) + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x1980), Op.MUL(0x20, Op.DUP1)))) + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x16ea) + Op.JUMPDEST + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.AND(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x1980), Op.MUL(0x20, Op.DUP2))), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20)))))) + Op.POP + Op.POP + Op.POP + Op.POP + Op.MSTORE(offset=0x1a40, value=0x1) + Op.RETURN(offset=0x1a40, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x17ff, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xa1fa51f9))) + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x1a60, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x44))) + Op.POP + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x7) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x1a60), 0x20))) + Op.DIV(Op.DUP2, 0x20) + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x17d1, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DUP2))) + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x1a60), Op.MUL(0x20, Op.DUP1)))) + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x17b0) + Op.JUMPDEST + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.AND(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x1a60), Op.MUL(0x20, Op.DUP2))), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20)))))) + Op.POP + Op.POP + Op.POP + Op.POP + Op.MSTORE(offset=0x1b20, value=0x1) + Op.RETURN(offset=0x1b20, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x18c5, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xcd87f43a))) + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x1b40, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x44))) + Op.POP + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x8) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x1b40), 0x20))) + Op.DIV(Op.DUP2, 0x20) + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x1897, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DUP2))) + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x1b40), Op.MUL(0x20, Op.DUP1)))) + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x1876) + Op.JUMPDEST + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.AND(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x1b40), Op.MUL(0x20, Op.DUP2))), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20)))))) + Op.POP + Op.POP + Op.POP + Op.POP + Op.MSTORE(offset=0x1c00, value=0x1) + Op.RETURN(offset=0x1c00, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x198b, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x222a8663))) + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x1c20, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x44))) + Op.POP + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x9) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x1c20), 0x20))) + Op.DIV(Op.DUP2, 0x20) + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x195d, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DUP2))) + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x1c20), Op.MUL(0x20, Op.DUP1)))) + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x193c) + Op.JUMPDEST + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.AND(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x1c20), Op.MUL(0x20, Op.DUP2))), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20)))))) + Op.POP + Op.POP + Op.POP + Op.POP + Op.MSTORE(offset=0x1ce0, value=0x1) + Op.RETURN(offset=0x1ce0, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x1a51, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xb39e1faa))) + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x1d00, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x44))) + Op.POP + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0xa) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x1d00), 0x20))) + Op.DIV(Op.DUP2, 0x20) + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x1a23, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DUP2))) + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x1d00), Op.MUL(0x20, Op.DUP1)))) + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x1a02) + Op.JUMPDEST + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.AND(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x1d00), Op.MUL(0x20, Op.DUP2))), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20)))))) + Op.POP + Op.POP + Op.POP + Op.POP + Op.MSTORE(offset=0x1dc0, value=0x1) + Op.RETURN(offset=0x1dc0, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x1b17, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xe365736b))) + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x1de0, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x44))) + Op.POP + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0xb) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x1de0), 0x20))) + Op.DIV(Op.DUP2, 0x20) + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x1ae9, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DUP2))) + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x1de0), Op.MUL(0x20, Op.DUP1)))) + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x1ac8) + Op.JUMPDEST + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.AND(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x1de0), Op.MUL(0x20, Op.DUP2))), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20)))))) + Op.POP + Op.POP + Op.POP + Op.POP + Op.MSTORE(offset=0x1ea0, value=0x1) + Op.RETURN(offset=0x1ea0, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x1b73, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xaad7d6e3))) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x1ec0, value=Op.CALLDATALOAD(offset=0x44)) + Op.MLOAD(offset=0x1ec0) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0xc) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.MSTORE(offset=0x1f00, value=0x1) + Op.RETURN(offset=0x1f00, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x1c39, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x1112b27))) + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x1f20, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x44))) + Op.POP + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0xd) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x1f20), 0x20))) + Op.DIV(Op.DUP2, 0x20) + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x1c0b, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DUP2))) + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x1f20), Op.MUL(0x20, Op.DUP1)))) + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x1bea) + Op.JUMPDEST + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.AND(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x1f20), Op.MUL(0x20, Op.DUP2))), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20)))))) + Op.POP + Op.POP + Op.POP + Op.POP + Op.MSTORE(offset=0x1fe0, value=0x1) + Op.RETURN(offset=0x1fe0, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x1cff, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xbdbb239b))) + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x2000, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x44))) + Op.POP + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0xe) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x2000), 0x20))) + Op.DIV(Op.DUP2, 0x20) + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x1cd1, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DUP2))) + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x2000), Op.MUL(0x20, Op.DUP1)))) + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x1cb0) + Op.JUMPDEST + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.AND(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x2000), Op.MUL(0x20, Op.DUP2))), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20)))))) + Op.POP + Op.POP + Op.POP + Op.POP + Op.MSTORE(offset=0x20c0, value=0x1) + Op.RETURN(offset=0x20c0, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x1dc5, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x5a0cd48))) + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x20e0, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x44))) + Op.POP + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0xf) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x20e0), 0x20))) + Op.DIV(Op.DUP2, 0x20) + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x1d97, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DUP2))) + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x20e0), Op.MUL(0x20, Op.DUP1)))) + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x1d76) + Op.JUMPDEST + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.AND(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x20e0), Op.MUL(0x20, Op.DUP2))), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20)))))) + Op.POP + Op.POP + Op.POP + Op.POP + Op.MSTORE(offset=0x21a0, value=0x1) + Op.RETURN(offset=0x21a0, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x1e8b, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xaaa1fe35))) + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x21c0, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x44))) + Op.POP + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x10) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x21c0), 0x20))) + Op.DIV(Op.DUP2, 0x20) + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x1e5d, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DUP2))) + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x21c0), Op.MUL(0x20, Op.DUP1)))) + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x1e3c) + Op.JUMPDEST + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.AND(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x21c0), Op.MUL(0x20, Op.DUP2))), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20)))))) + Op.POP + Op.POP + Op.POP + Op.POP + Op.MSTORE(offset=0x2280, value=0x1) + Op.RETURN(offset=0x2280, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x1f51, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x2be4935d))) + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x22a0, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x44))) + Op.POP + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x11) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x22a0), 0x20))) + Op.DIV(Op.DUP2, 0x20) + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x1f23, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DUP2))) + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x22a0), Op.MUL(0x20, Op.DUP1)))) + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x1f02) + Op.JUMPDEST + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.AND(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x22a0), Op.MUL(0x20, Op.DUP2))), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20)))))) + Op.POP + Op.POP + Op.POP + Op.POP + Op.MSTORE(offset=0x2360, value=0x1) + Op.RETURN(offset=0x2360, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x2017, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x13a8350d))) + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x2380, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x44))) + Op.POP + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x12) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x2380), 0x20))) + Op.DIV(Op.DUP2, 0x20) + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x1fe9, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DUP2))) + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x2380), Op.MUL(0x20, Op.DUP1)))) + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x1fc8) + Op.JUMPDEST + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.AND(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x2380), Op.MUL(0x20, Op.DUP2))), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20)))))) + Op.POP + Op.POP + Op.POP + Op.POP + Op.MSTORE(offset=0x2440, value=0x1) + Op.RETURN(offset=0x2440, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x20dd, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xcb540b45))) + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x2460, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x44))) + Op.POP + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x13) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x2460), 0x20))) + Op.DIV(Op.DUP2, 0x20) + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x20af, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DUP2))) + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x2460), Op.MUL(0x20, Op.DUP1)))) + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x208e) + Op.JUMPDEST + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.AND(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x2460), Op.MUL(0x20, Op.DUP2))), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20)))))) + Op.POP + Op.POP + Op.POP + Op.POP + Op.MSTORE(offset=0x2520, value=0x1) + Op.RETURN(offset=0x2520, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x21a3, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xbe030627))) + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x2540, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x44))) + Op.POP + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x14) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x2540), 0x20))) + Op.DIV(Op.DUP2, 0x20) + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x2175, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DUP2))) + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x2540), Op.MUL(0x20, Op.DUP1)))) + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x2154) + Op.JUMPDEST + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.AND(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x2540), Op.MUL(0x20, Op.DUP2))), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20)))))) + Op.POP + Op.POP + Op.POP + Op.POP + Op.MSTORE(offset=0x2600, value=0x1) + Op.RETURN(offset=0x2600, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x2269, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x83fd77f0))) + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x2620, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x44))) + Op.POP + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x15) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x2620), 0x20))) + Op.DIV(Op.DUP2, 0x20) + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x223b, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DUP2))) + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x2620), Op.MUL(0x20, Op.DUP1)))) + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x221a) + Op.JUMPDEST + Op.SSTORE(key=Op.ADD(Op.DUP3, Op.DUP5), value=Op.AND(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x2620), Op.MUL(0x20, Op.DUP2))), Op.SUB(0x0, Op.EXP(0x100, Op.SUB(0x20, Op.MOD(Op.DUP4, 0x20)))))) + Op.POP + Op.POP + Op.POP + Op.POP + Op.MSTORE(offset=0x26e0, value=0x1) + Op.RETURN(offset=0x26e0, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x22d5, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x59462205))) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x3c0, value=Op.CALLDATALOAD(offset=0x44)) + Op.MSTORE(offset=0x2700, value=Op.CALLDATALOAD(offset=0x64)) + Op.MLOAD(offset=0x2700) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x4) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=Op.MLOAD(offset=0x3c0)) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.MSTORE(offset=0x2740, value=0x1) + Op.RETURN(offset=0x2740, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x2448, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xbb8e4196))) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x2760, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x2780, value=Op.CALLDATALOAD(offset=0x44)) + Op.MSTORE(offset=0x27a0, value=0x0) + Op.JUMPDEST + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.SUB(Op.MLOAD(offset=0x2760), 0x1)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.JUMPI(pc=0x243b, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x27a0), Op.SLOAD(key=Op.SHA3)))) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.SUB(Op.MLOAD(offset=0x2760), 0x1)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x1) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=Op.MLOAD(offset=0x27a0)) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x2780)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x1) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x2780)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=Op.SLOAD(key=Op.SHA3)) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.PUSH1[0x1] + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x2780)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.ADD + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x2780)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.MSTORE(offset=0x27a0, value=Op.ADD(Op.MLOAD(offset=0x27a0), 0x1)) + Op.JUMP(pc=0x22fc) + Op.JUMPDEST + Op.MSTORE(offset=0x2880, value=0x1) + Op.RETURN(offset=0x2880, size=0x20) + Op.JUMPDEST + Op.POP,
        ),
        callee_6: Account(
            code=Op.MSTORE8(offset=0x31f, value=0x0) + Op.DIV(Op.CALLDATALOAD(offset=0x0), 0x100000000000000000000000000000000000000000000000000000000) + Op.MSTORE(offset=0x20, value=0xc9ae5868651bf7b7db6e360217db49ce4e69c07e) + Op.MSTORE(offset=0x40, value=0xea65418d7bf32680f55572c943a94b590804998) + Op.JUMPI(pc=0x38d, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x27138bfb))) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x4)) + Op.PUSH1[0x1c] + Op.PUSH1[0x44] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x7a66d7ca) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x80)) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP4, args_size=0x24, ret_offset=0xe0, ret_size=0x20)) + Op.MLOAD(offset=0xe0) + Op.SWAP1 + Op.POP + Op.PUSH1[0xa0] + Op.MSTORE + Op.PUSH1[0x1c] + Op.PUSH1[0x44] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xc60409c6) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x80)) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP4, args_size=0x24, ret_offset=0x120, ret_size=0x20)) + Op.MLOAD(offset=0x120) + Op.SWAP1 + Op.POP + Op.NUMBER + Op.MSTORE(offset=0x100, value=Op.SDIV) + Op.MSTORE(offset=0x140, value=0x0) + Op.MSTORE(offset=0x160, value=0x0) + Op.MSTORE(offset=0x180, value=0x0) + Op.JUMPI(pc=0x10a, condition=Op.ISZERO(Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x100), Op.ADD(Op.MLOAD(offset=0xa0), 0x2))))) + Op.MSTORE(offset=0x140, value=0x1) + Op.JUMPDEST + Op.MSTORE(offset=0x1a0, value=0x0) + Op.MSTORE(offset=0x1c0, value=Op.MLOAD(offset=0x100)) + Op.JUMPDEST + Op.JUMPI(pc=0x184, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x1c0), Op.ADD(Op.MLOAD(offset=0x100), 0x64)))) + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xcc1c944e) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0x1c0)) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x40), value=0x0, args_offset=Op.DUP4, args_size=0x44, ret_offset=0x1e0, ret_size=0x20)) + Op.MLOAD(offset=0x1e0) + Op.SWAP1 + Op.POP + Op.MLOAD(offset=0x1a0) + Op.MSTORE(offset=0x1a0, value=Op.ADD) + Op.MSTORE(offset=0x1c0, value=Op.ADD(Op.MLOAD(offset=0x1c0), 0x1)) + Op.JUMP(pc=0x119) + Op.JUMPDEST + Op.PUSH1[0x5] + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xcc1c944e) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0xa0)) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x40), value=0x0, args_offset=Op.DUP4, args_size=0x44, ret_offset=0x200, ret_size=0x20)) + Op.MLOAD(offset=0x200) + Op.SWAP1 + Op.POP + Op.SLT + Op.JUMPI(pc=0x1d3, condition=Op.ISZERO(Op.DUP1)) + Op.DUP1 + Op.JUMP(pc=0x1db) + Op.JUMPDEST + Op.SLT(Op.MLOAD(offset=0x1a0), 0xa) + Op.JUMPDEST + Op.SWAP1 + Op.POP + Op.JUMPI(pc=0x1eb, condition=Op.ISZERO) + Op.MLOAD(offset=0x140) + Op.JUMP(pc=0x1ee) + Op.JUMPDEST + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x336, condition=Op.ISZERO) + Op.PUSH1[0x1c] + Op.PUSH1[0x44] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xc5476efe) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x80)) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP4, args_size=0x24, ret_offset=0x240, ret_size=0x20)) + Op.MLOAD(offset=0x240) + Op.SWAP1 + Op.POP + Op.POP + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x7265802d) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=0x0) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP4, args_size=0x44, ret_offset=0x260, ret_size=0x20)) + Op.MLOAD(offset=0x260) + Op.SWAP1 + Op.POP + Op.POP + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xc286273a) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=0x0) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP4, args_size=0x44, ret_offset=0x280, ret_size=0x20)) + Op.MLOAD(offset=0x280) + Op.SWAP1 + Op.POP + Op.POP + Op.PUSH1[0x1c] + Op.PUSH1[0x44] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x7a66d7ca) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x80)) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP4, args_size=0x24, ret_offset=0x2a0, ret_size=0x20)) + Op.MLOAD(offset=0x2a0) + Op.SWAP1 + Op.POP + Op.PUSH1[0xa0] + Op.MSTORE + Op.PUSH1[0x1c] + Op.PUSH1[0x84] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xbb8e4196) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0xa0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=Op.MLOAD(offset=0x100)) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x40), value=0x0, args_offset=Op.DUP4, args_size=0x64, ret_offset=0x2c0, ret_size=0x20)) + Op.MLOAD(offset=0x2c0) + Op.SWAP1 + Op.POP + Op.POP + Op.JUMP(pc=0x343) + Op.JUMPDEST + Op.MSTORE(offset=0x160, value=0x1) + Op.MSTORE(offset=0x180, value=0x1) + Op.JUMPDEST + Op.JUMPI(pc=0x355, condition=Op.ISZERO(Op.MLOAD(offset=0x140))) + Op.MLOAD(offset=0x160) + Op.JUMP(pc=0x358) + Op.JUMPDEST + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x366, condition=Op.ISZERO) + Op.MLOAD(offset=0x180) + Op.JUMP(pc=0x369) + Op.JUMPDEST + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x37f, condition=Op.ISZERO) + Op.MSTORE(offset=0x2e0, value=0x1) + Op.RETURN(offset=0x2e0, size=0x20) + Op.JUMP(pc=0x38c) + Op.JUMPDEST + Op.MSTORE(offset=0x300, value=0x0) + Op.RETURN(offset=0x300, size=0x20) + Op.JUMPDEST + Op.JUMPDEST + Op.POP,
        ),
        callee_7: Account(
            code=Op.MSTORE8(offset=0x5df, value=0x0) + Op.DIV(Op.CALLDATALOAD(offset=0x0), 0x100000000000000000000000000000000000000000000000000000000) + Op.MSTORE(offset=0x20, value=0xea65418d7bf32680f55572c943a94b590804998) + Op.MSTORE(offset=0x40, value=0xe509e3a93beb1eba72f8cb8d25f93a85e2d54afb) + Op.MSTORE(offset=0x60, value=0xc9ae5868651bf7b7db6e360217db49ce4e69c07e) + Op.MSTORE(offset=0x80, value=0xf1562e1c0d0baa3ea746442bb7f11153fcf5cfda) + Op.JUMPI(pc=0x38d, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x546fdeb3))) + Op.MSTORE(offset=0xc0, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0xe0, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x100, value=Op.CALLDATALOAD(offset=0x44)) + Op.MSTORE(offset=0x120, value=Op.CALLDATALOAD(offset=0x64)) + Op.MSTORE(offset=0x140, value=Op.CALLDATALOAD(offset=0x84)) + Op.ADD(Op.MLOAD(offset=0x100), 0x2) + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xe05dcb56) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0xc0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0xe0)) + Op.ADD(Op.MLOAD(offset=0x100), 0x2) + Op.ADD(Op.MUL(0x20, Op.DUP2), 0x40) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP6, args_size=0x44, ret_offset=Op.DUP2, ret_size=Op.ADD(0x40, Op.MUL(0x20, Op.DUP2)))) + Op.ADD(Op.DUP2, 0x40) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.JUMPI(pc=0x250, condition=Op.ISZERO(Op.EQ(Op.MLOAD(offset=Op.ADD(Op.DUP3, Op.MUL(0x20, Op.ADD(Op.MLOAD(offset=0x100), 0x1)))), 0x0))) + Op.PUSH1[0x60] + Op.PUSH1[0x1c] + Op.PUSH2[0x14c] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xe365736b) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0xc0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0xe0)) + Op.PUSH1[0x1c] + Op.PUSH1[0x84] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x2f300bee) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=0x2) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=0x5) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=Op.MLOAD(offset=0x100)) + Op.DUP5 + Op.ADD(Op.MUL(0x20, Op.DUP2), 0x40) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x80), value=0x0, args_offset=Op.DUP6, args_size=0x64, ret_offset=Op.DUP2, ret_size=Op.ADD(0x40, Op.MUL(0x20, Op.DUP2)))) + Op.ADD(Op.DUP2, 0x40) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.ADD(0x20, Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.DUP2, 0x20)))) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x44), value=Op.DUP4) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0xa4), value=Op.SUB(Op.DUP3, 0x20)) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x108), value=Op.DUP1) + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.POP + Op.ADD(0x4, Op.DUP2) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.JUMPI(pc=0x1fc, condition=Op.CALL(gas=0x1c, address=0x4, value=0x0, args_offset=Op.DUP5, args_size=0x64, ret_offset=Op.DUP2, ret_size=0x64)) + Op.INVALID + Op.JUMPDEST + Op.ADD(Op.DUP2, 0x64) + Op.SWAP3 + Op.POP + Op.MLOAD(offset=Op.ADD(Op.DUP3, 0x108)) + Op.DUP1 + Op.JUMPI(pc=0x223, condition=Op.CALL(gas=Op.ADD(0x12, Op.SDIV(Op.DUP8, 0xa)), address=0x4, value=0x0, args_offset=Op.MLOAD(offset=Op.ADD(Op.DUP8, 0xa4)), args_size=Op.DUP3, ret_offset=Op.DUP6, ret_size=Op.DUP1)) + Op.INVALID + Op.JUMPDEST + Op.POP + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.SUB(Op.DUP4, Op.DUP1) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP5, args_size=Op.DUP3, ret_offset=0x280, ret_size=0x20)) + Op.MLOAD(offset=0x280) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x37d) + Op.JUMPDEST + Op.PUSH1[0x60] + Op.PUSH1[0x1c] + Op.PUSH2[0x14c] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xe365736b) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0xc0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0xe0)) + Op.PUSH1[0x1c] + Op.PUSH1[0x84] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x2f300bee) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.SUB(Op.MLOAD(offset=Op.ADD(Op.DUP6, Op.MUL(0x20, Op.ADD(Op.MLOAD(offset=0x100), 0x1)))), 0x1)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=0x5) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=Op.MLOAD(offset=0x100)) + Op.DUP5 + Op.ADD(Op.MUL(0x20, Op.DUP2), 0x40) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x80), value=0x0, args_offset=Op.DUP6, args_size=0x64, ret_offset=Op.DUP2, ret_size=Op.ADD(0x40, Op.MUL(0x20, Op.DUP2)))) + Op.ADD(Op.DUP2, 0x40) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.ADD(0x20, Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.DUP2, 0x20)))) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x44), value=Op.DUP4) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0xa4), value=Op.SUB(Op.DUP3, 0x20)) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x108), value=Op.DUP1) + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.POP + Op.ADD(0x4, Op.DUP2) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.JUMPI(pc=0x32d, condition=Op.CALL(gas=0x1c, address=0x4, value=0x0, args_offset=Op.DUP5, args_size=0x64, ret_offset=Op.DUP2, ret_size=0x64)) + Op.INVALID + Op.JUMPDEST + Op.ADD(Op.DUP2, 0x64) + Op.SWAP3 + Op.POP + Op.MLOAD(offset=Op.ADD(Op.DUP3, 0x108)) + Op.DUP1 + Op.JUMPI(pc=0x354, condition=Op.CALL(gas=Op.ADD(0x12, Op.SDIV(Op.DUP8, 0xa)), address=0x4, value=0x0, args_offset=Op.MLOAD(offset=Op.ADD(Op.DUP8, 0xa4)), args_size=Op.DUP3, ret_offset=Op.DUP6, ret_size=Op.DUP1)) + Op.INVALID + Op.JUMPDEST + Op.POP + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.SUB(Op.DUP4, Op.DUP1) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP5, args_size=Op.DUP3, ret_offset=0x2c0, ret_size=0x20)) + Op.MLOAD(offset=0x2c0) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.JUMPDEST + Op.POP + Op.MSTORE(offset=0x2e0, value=0x1) + Op.RETURN(offset=0x2e0, size=0x20) + Op.POP + Op.POP + Op.JUMPDEST + Op.JUMPI(pc=0x764, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xde9080c8))) + Op.MSTORE(offset=0xc0, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0xe0, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x100, value=Op.CALLDATALOAD(offset=0x44)) + Op.MSTORE(offset=0x120, value=Op.CALLDATALOAD(offset=0x64)) + Op.MSTORE(offset=0x140, value=Op.CALLDATALOAD(offset=0x84)) + Op.ADD(Op.MLOAD(offset=0x100), 0x2) + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xe05dcb56) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0xc0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0xe0)) + Op.DUP2 + Op.ADD(Op.MUL(0x20, Op.DUP2), 0x40) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP6, args_size=0x44, ret_offset=Op.DUP2, ret_size=Op.ADD(0x40, Op.MUL(0x20, Op.DUP2)))) + Op.ADD(Op.DUP2, 0x40) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x2c5a40d5) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0xc0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0xe0)) + Op.MLOAD(offset=0x140) + Op.ADD(Op.MUL(0x20, Op.DUP2), 0x40) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP6, args_size=0x44, ret_offset=Op.DUP2, ret_size=Op.ADD(0x40, Op.MUL(0x20, Op.DUP2)))) + Op.ADD(Op.DUP2, 0x40) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.MLOAD(offset=0x120) + Op.ADD(0x20, Op.MUL(0x20, Op.DUP1)) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x4ee, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.MLOAD(offset=0x120)))) + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x28c8b315) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0xc0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.DUP2) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x40), value=0x0, args_offset=Op.DUP4, args_size=0x44, ret_offset=0x360, ret_size=0x20)) + Op.MLOAD(offset=0x360) + Op.SWAP1 + Op.POP + Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP2)) + Op.MSTORE + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x493) + Op.JUMPDEST + Op.POP + Op.PUSH1[0xa0] + Op.PUSH1[0x1c] + Op.PUSH2[0x20c] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xa647a5b9) + Op.DUP5 + Op.ADD(0x20, Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.DUP2, 0x20)))) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x4), value=Op.DUP4) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0xa4), value=Op.SUB(Op.DUP3, 0x20)) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x148), value=Op.DUP1) + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.POP + Op.DUP4 + Op.ADD(0x20, Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.DUP2, 0x20)))) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x24), value=Op.DUP4) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0xc4), value=Op.SUB(Op.DUP3, 0x20)) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x168), value=Op.DUP1) + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.POP + Op.DUP3 + Op.ADD(0x20, Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.DUP2, 0x20)))) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x44), value=Op.DUP4) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0xe4), value=Op.SUB(Op.DUP3, 0x20)) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x188), value=Op.DUP1) + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.POP + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x64), value=Op.MLOAD(offset=0x120)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x84), value=Op.MLOAD(offset=0x100)) + Op.ADD(0x4, Op.DUP2) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.JUMPI(pc=0x5b5, condition=Op.CALL(gas=0x22, address=0x4, value=0x0, args_offset=Op.DUP5, args_size=0xa4, ret_offset=Op.DUP2, ret_size=0xa4)) + Op.INVALID + Op.JUMPDEST + Op.ADD(Op.DUP2, 0xa4) + Op.SWAP3 + Op.POP + Op.MLOAD(offset=Op.ADD(Op.DUP3, 0x148)) + Op.DUP1 + Op.JUMPI(pc=0x5dc, condition=Op.CALL(gas=Op.ADD(0x12, Op.SDIV(Op.DUP8, 0xa)), address=0x4, value=0x0, args_offset=Op.MLOAD(offset=Op.ADD(Op.DUP8, 0xa4)), args_size=Op.DUP3, ret_offset=Op.DUP6, ret_size=Op.DUP1)) + Op.INVALID + Op.JUMPDEST + Op.POP + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.MLOAD(offset=Op.ADD(Op.DUP3, 0x168)) + Op.DUP1 + Op.JUMPI(pc=0x604, condition=Op.CALL(gas=Op.ADD(0x12, Op.SDIV(Op.DUP8, 0xa)), address=0x4, value=0x0, args_offset=Op.MLOAD(offset=Op.ADD(Op.DUP8, 0xc4)), args_size=Op.DUP3, ret_offset=Op.DUP6, ret_size=Op.DUP1)) + Op.INVALID + Op.JUMPDEST + Op.POP + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.MLOAD(offset=Op.ADD(Op.DUP3, 0x188)) + Op.DUP1 + Op.JUMPI(pc=0x62c, condition=Op.CALL(gas=Op.ADD(0x12, Op.SDIV(Op.DUP8, 0xa)), address=0x4, value=0x0, args_offset=Op.MLOAD(offset=Op.ADD(Op.DUP8, 0xe4)), args_size=Op.DUP3, ret_offset=Op.DUP6, ret_size=Op.DUP1)) + Op.INVALID + Op.JUMPDEST + Op.POP + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.SUB(Op.DUP4, Op.DUP1) + Op.DUP8 + Op.ADD(Op.MUL(0x20, Op.DUP2), 0x40) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x80), value=0x0, args_offset=Op.DUP7, args_size=Op.DUP5, ret_offset=Op.DUP2, ret_size=Op.ADD(0x40, Op.MUL(0x20, Op.DUP2)))) + Op.ADD(Op.DUP2, 0x40) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP3 + Op.POP + Op.PUSH1[0x60] + Op.PUSH1[0x1c] + Op.PUSH2[0x14c] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xe365736b) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0xc0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0xe0)) + Op.DUP5 + Op.ADD(0x20, Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.DUP2, 0x20)))) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x44), value=Op.DUP4) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0xa4), value=Op.SUB(Op.DUP3, 0x20)) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x108), value=Op.DUP1) + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.POP + Op.ADD(0x4, Op.DUP2) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.JUMPI(pc=0x6df, condition=Op.CALL(gas=0x1c, address=0x4, value=0x0, args_offset=Op.DUP5, args_size=0x64, ret_offset=Op.DUP2, ret_size=0x64)) + Op.INVALID + Op.JUMPDEST + Op.ADD(Op.DUP2, 0x64) + Op.SWAP3 + Op.POP + Op.MLOAD(offset=Op.ADD(Op.DUP3, 0x108)) + Op.DUP1 + Op.JUMPI(pc=0x706, condition=Op.CALL(gas=Op.ADD(0x12, Op.SDIV(Op.DUP8, 0xa)), address=0x4, value=0x0, args_offset=Op.MLOAD(offset=Op.ADD(Op.DUP8, 0xa4)), args_size=Op.DUP3, ret_offset=Op.DUP6, ret_size=Op.DUP1)) + Op.INVALID + Op.JUMPDEST + Op.POP + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.SUB(Op.DUP4, Op.DUP1) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP5, args_size=Op.DUP3, ret_offset=0x3c0, ret_size=0x20)) + Op.MLOAD(offset=0x3c0) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.POP + Op.JUMPI(pc=0x752, condition=Op.ISZERO(Op.EQ(Op.MLOAD(offset=Op.ADD(Op.DUP5, Op.MUL(0x20, Op.MLOAD(offset=0x100)))), 0x0))) + Op.MSTORE(offset=0x3e0, value=0x0) + Op.RETURN(offset=0x3e0, size=0x20) + Op.JUMP(pc=0x75f) + Op.JUMPDEST + Op.MSTORE(offset=0x400, value=0x1) + Op.RETURN(offset=0x400, size=0x20) + Op.JUMPDEST + Op.POP + Op.POP + Op.POP + Op.POP + Op.JUMPDEST + Op.JUMPI(pc=0xa66, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x384ca8dd))) + Op.MSTORE(offset=0xc0, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0xe0, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x100, value=Op.CALLDATALOAD(offset=0x44)) + Op.MSTORE(offset=0x120, value=Op.CALLDATALOAD(offset=0x64)) + Op.MSTORE(offset=0x140, value=Op.CALLDATALOAD(offset=0x84)) + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xe05dcb56) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0xc0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0xe0)) + Op.ADD(Op.MLOAD(offset=0x100), 0x2) + Op.ADD(Op.MUL(0x20, Op.DUP2), 0x40) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP6, args_size=0x44, ret_offset=Op.DUP2, ret_size=Op.ADD(0x40, Op.MUL(0x20, Op.DUP2)))) + Op.ADD(Op.DUP2, 0x40) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xfa9832d1) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0xc0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0xe0)) + Op.MLOAD(offset=0x100) + Op.ADD(Op.MUL(0x20, Op.DUP2), 0x40) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP6, args_size=0x44, ret_offset=Op.DUP2, ret_size=Op.ADD(0x40, Op.MUL(0x20, Op.DUP2)))) + Op.ADD(Op.DUP2, 0x40) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x1c] + Op.PUSH1[0x84] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xaad7d6e3) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0xc0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0xe0)) + Op.PUSH1[0x60] + Op.PUSH1[0x1c] + Op.PUSH2[0x14c] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x5b180229) + Op.DUP4 + Op.ADD(0x20, Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.DUP2, 0x20)))) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x4), value=Op.DUP4) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x64), value=Op.SUB(Op.DUP3, 0x20)) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0xc8), value=Op.DUP1) + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.POP + Op.DUP5 + Op.ADD(0x20, Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.DUP2, 0x20)))) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x24), value=Op.DUP4) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x84), value=Op.SUB(Op.DUP3, 0x20)) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0xe8), value=Op.DUP1) + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.POP + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=Op.MLOAD(offset=0x100)) + Op.ADD(0x4, Op.DUP2) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.JUMPI(pc=0x901, condition=Op.CALL(gas=0x1c, address=0x4, value=0x0, args_offset=Op.DUP5, args_size=0x64, ret_offset=Op.DUP2, ret_size=0x64)) + Op.INVALID + Op.JUMPDEST + Op.ADD(Op.DUP2, 0x64) + Op.SWAP3 + Op.POP + Op.MLOAD(offset=Op.ADD(Op.DUP3, 0xc8)) + Op.DUP1 + Op.JUMPI(pc=0x927, condition=Op.CALL(gas=Op.ADD(0x12, Op.SDIV(Op.DUP8, 0xa)), address=0x4, value=0x0, args_offset=Op.MLOAD(offset=Op.ADD(Op.DUP8, 0x64)), args_size=Op.DUP3, ret_offset=Op.DUP6, ret_size=Op.DUP1)) + Op.INVALID + Op.JUMPDEST + Op.POP + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.MLOAD(offset=Op.ADD(Op.DUP3, 0xe8)) + Op.DUP1 + Op.JUMPI(pc=0x94e, condition=Op.CALL(gas=Op.ADD(0x12, Op.SDIV(Op.DUP8, 0xa)), address=0x4, value=0x0, args_offset=Op.MLOAD(offset=Op.ADD(Op.DUP8, 0x84)), args_size=Op.DUP3, ret_offset=Op.DUP6, ret_size=Op.DUP1)) + Op.INVALID + Op.JUMPDEST + Op.POP + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.SUB(Op.DUP4, Op.DUP1) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x80), value=0x0, args_offset=Op.DUP5, args_size=Op.DUP3, ret_offset=0x440, ret_size=0x20)) + Op.MLOAD(offset=0x440) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.ADD(Op.DUP3, 0x44) + Op.MSTORE + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP4, args_size=0x64, ret_offset=0x460, ret_size=0x20)) + Op.MLOAD(offset=0x460) + Op.SWAP1 + Op.POP + Op.POP + Op.PUSH1[0x60] + Op.PUSH1[0x1c] + Op.PUSH2[0x14c] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x222a8663) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0xc0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0xe0)) + Op.DUP3 + Op.ADD(0x20, Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.DUP2, 0x20)))) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x44), value=Op.DUP4) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0xa4), value=Op.SUB(Op.DUP3, 0x20)) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x108), value=Op.DUP1) + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.POP + Op.ADD(0x4, Op.DUP2) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.JUMPI(pc=0xa07, condition=Op.CALL(gas=0x1c, address=0x4, value=0x0, args_offset=Op.DUP5, args_size=0x64, ret_offset=Op.DUP2, ret_size=0x64)) + Op.INVALID + Op.JUMPDEST + Op.ADD(Op.DUP2, 0x64) + Op.SWAP3 + Op.POP + Op.MLOAD(offset=Op.ADD(Op.DUP3, 0x108)) + Op.DUP1 + Op.JUMPI(pc=0xa2e, condition=Op.CALL(gas=Op.ADD(0x12, Op.SDIV(Op.DUP8, 0xa)), address=0x4, value=0x0, args_offset=Op.MLOAD(offset=Op.ADD(Op.DUP8, 0xa4)), args_size=Op.DUP3, ret_offset=Op.DUP6, ret_size=Op.DUP1)) + Op.INVALID + Op.JUMPDEST + Op.POP + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.SUB(Op.DUP4, Op.DUP1) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP5, args_size=Op.DUP3, ret_offset=0x480, ret_size=0x20)) + Op.MLOAD(offset=0x480) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.POP + Op.MSTORE(offset=0x4a0, value=0x1) + Op.RETURN(offset=0x4a0, size=0x20) + Op.POP + Op.POP + Op.JUMPDEST + Op.JUMPI(pc=0xd4b, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xd5dc5af1))) + Op.MSTORE(offset=0xc0, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0xe0, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x100, value=Op.CALLDATALOAD(offset=0x44)) + Op.MSTORE(offset=0x120, value=Op.CALLDATALOAD(offset=0x64)) + Op.MSTORE(offset=0x140, value=Op.CALLDATALOAD(offset=0x84)) + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xe05dcb56) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0xc0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0xe0)) + Op.ADD(Op.MLOAD(offset=0x100), 0x2) + Op.ADD(Op.MUL(0x20, Op.DUP2), 0x40) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP6, args_size=0x44, ret_offset=Op.DUP2, ret_size=Op.ADD(0x40, Op.MUL(0x20, Op.DUP2)))) + Op.ADD(Op.DUP2, 0x40) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x2c5a40d5) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0xc0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0xe0)) + Op.MLOAD(offset=0x140) + Op.ADD(Op.MUL(0x20, Op.DUP2), 0x40) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP6, args_size=0x44, ret_offset=Op.DUP2, ret_size=Op.ADD(0x40, Op.MUL(0x20, Op.DUP2)))) + Op.ADD(Op.DUP2, 0x40) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x80] + Op.PUSH1[0x1c] + Op.PUSH2[0x1ac] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xf4ca7dc4) + Op.DUP4 + Op.ADD(0x20, Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.DUP2, 0x20)))) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x4), value=Op.DUP4) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x84), value=Op.SUB(Op.DUP3, 0x20)) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x108), value=Op.DUP1) + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.POP + Op.DUP3 + Op.ADD(0x20, Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.DUP2, 0x20)))) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x24), value=Op.DUP4) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0xa4), value=Op.SUB(Op.DUP3, 0x20)) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x128), value=Op.DUP1) + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.POP + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=Op.MLOAD(offset=0x120)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x64), value=Op.MLOAD(offset=0x100)) + Op.ADD(0x4, Op.DUP2) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.JUMPI(pc=0xbe7, condition=Op.CALL(gas=0x1f, address=0x4, value=0x0, args_offset=Op.DUP5, args_size=0x84, ret_offset=Op.DUP2, ret_size=0x84)) + Op.INVALID + Op.JUMPDEST + Op.ADD(Op.DUP2, 0x84) + Op.SWAP3 + Op.POP + Op.MLOAD(offset=Op.ADD(Op.DUP3, 0x108)) + Op.DUP1 + Op.JUMPI(pc=0xc0e, condition=Op.CALL(gas=Op.ADD(0x12, Op.SDIV(Op.DUP8, 0xa)), address=0x4, value=0x0, args_offset=Op.MLOAD(offset=Op.ADD(Op.DUP8, 0x84)), args_size=Op.DUP3, ret_offset=Op.DUP6, ret_size=Op.DUP1)) + Op.INVALID + Op.JUMPDEST + Op.POP + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.MLOAD(offset=Op.ADD(Op.DUP3, 0x128)) + Op.DUP1 + Op.JUMPI(pc=0xc36, condition=Op.CALL(gas=Op.ADD(0x12, Op.SDIV(Op.DUP8, 0xa)), address=0x4, value=0x0, args_offset=Op.MLOAD(offset=Op.ADD(Op.DUP8, 0xa4)), args_size=Op.DUP3, ret_offset=Op.DUP6, ret_size=Op.DUP1)) + Op.INVALID + Op.JUMPDEST + Op.POP + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.SUB(Op.DUP4, Op.DUP1) + Op.MLOAD(offset=0x140) + Op.ADD(Op.MUL(0x20, Op.DUP2), 0x40) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x80), value=0x0, args_offset=Op.DUP7, args_size=Op.DUP5, ret_offset=Op.DUP2, ret_size=Op.ADD(0x40, Op.MUL(0x20, Op.DUP2)))) + Op.ADD(Op.DUP2, 0x40) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x60] + Op.PUSH1[0x1c] + Op.PUSH2[0x14c] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xb39e1faa) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0xc0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0xe0)) + Op.DUP3 + Op.ADD(0x20, Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.DUP2, 0x20)))) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x44), value=Op.DUP4) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0xa4), value=Op.SUB(Op.DUP3, 0x20)) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x108), value=Op.DUP1) + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.POP + Op.ADD(0x4, Op.DUP2) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.JUMPI(pc=0xcec, condition=Op.CALL(gas=0x1c, address=0x4, value=0x0, args_offset=Op.DUP5, args_size=0x64, ret_offset=Op.DUP2, ret_size=0x64)) + Op.INVALID + Op.JUMPDEST + Op.ADD(Op.DUP2, 0x64) + Op.SWAP3 + Op.POP + Op.MLOAD(offset=Op.ADD(Op.DUP3, 0x108)) + Op.DUP1 + Op.JUMPI(pc=0xd13, condition=Op.CALL(gas=Op.ADD(0x12, Op.SDIV(Op.DUP8, 0xa)), address=0x4, value=0x0, args_offset=Op.MLOAD(offset=Op.ADD(Op.DUP8, 0xa4)), args_size=Op.DUP3, ret_offset=Op.DUP6, ret_size=Op.DUP1)) + Op.INVALID + Op.JUMPDEST + Op.POP + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.SUB(Op.DUP4, Op.DUP1) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP5, args_size=Op.DUP3, ret_offset=0x4c0, ret_size=0x20)) + Op.MLOAD(offset=0x4c0) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.POP + Op.MSTORE(offset=0x4e0, value=0x1) + Op.RETURN(offset=0x4e0, size=0x20) + Op.POP + Op.POP + Op.JUMPDEST + Op.JUMPI(pc=0x114c, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x939aa8c))) + Op.MSTORE(offset=0xc0, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0xe0, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x100, value=Op.CALLDATALOAD(offset=0x44)) + Op.MSTORE(offset=0x120, value=Op.CALLDATALOAD(offset=0x64)) + Op.MSTORE(offset=0x140, value=Op.CALLDATALOAD(offset=0x84)) + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xe05dcb56) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0xc0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0xe0)) + Op.ADD(Op.MLOAD(offset=0x100), 0x2) + Op.ADD(Op.MUL(0x20, Op.DUP2), 0x40) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP6, args_size=0x44, ret_offset=Op.DUP2, ret_size=Op.ADD(0x40, Op.MUL(0x20, Op.DUP2)))) + Op.ADD(Op.DUP2, 0x40) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x7dc12195) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0xc0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0xe0)) + Op.MLOAD(offset=0x140) + Op.ADD(Op.MUL(0x20, Op.DUP2), 0x40) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP6, args_size=0x44, ret_offset=Op.DUP2, ret_size=Op.ADD(0x40, Op.MUL(0x20, Op.DUP2)))) + Op.ADD(Op.DUP2, 0x40) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x586b5be0) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0xc0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0xe0)) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP4, args_size=0x44, ret_offset=0x500, ret_size=0x20)) + Op.MLOAD(offset=0x500) + Op.SWAP1 + Op.POP + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xeb8af5aa) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0xc0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0xe0)) + Op.MLOAD(offset=0x120) + Op.ADD(Op.MUL(0x20, Op.DUP2), 0x40) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP6, args_size=0x44, ret_offset=Op.DUP2, ret_size=Op.ADD(0x40, Op.MUL(0x20, Op.DUP2)))) + Op.ADD(Op.DUP2, 0x40) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0xc0] + Op.PUSH1[0x1c] + Op.PUSH2[0x26c] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x232b2734) + Op.DUP3 + Op.ADD(0x20, Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.DUP2, 0x20)))) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x4), value=Op.DUP4) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0xc4), value=Op.SUB(Op.DUP3, 0x20)) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x188), value=Op.DUP1) + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.POP + Op.DUP6 + Op.ADD(0x20, Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.DUP2, 0x20)))) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x24), value=Op.DUP4) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0xe4), value=Op.SUB(Op.DUP3, 0x20)) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x1a8), value=Op.DUP1) + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.POP + Op.DUP5 + Op.ADD(0x20, Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.DUP2, 0x20)))) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x44), value=Op.DUP4) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x104), value=Op.SUB(Op.DUP3, 0x20)) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x1c8), value=Op.DUP1) + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.POP + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x64), value=Op.DUP4) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x84), value=Op.MLOAD(offset=0x120)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0xa4), value=Op.MLOAD(offset=0x100)) + Op.ADD(0x4, Op.DUP2) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.JUMPI(pc=0xf96, condition=Op.CALL(gas=0x25, address=0x4, value=0x0, args_offset=Op.DUP5, args_size=0xc4, ret_offset=Op.DUP2, ret_size=0xc4)) + Op.INVALID + Op.JUMPDEST + Op.ADD(Op.DUP2, 0xc4) + Op.SWAP3 + Op.POP + Op.MLOAD(offset=Op.ADD(Op.DUP3, 0x188)) + Op.DUP1 + Op.JUMPI(pc=0xfbd, condition=Op.CALL(gas=Op.ADD(0x12, Op.SDIV(Op.DUP8, 0xa)), address=0x4, value=0x0, args_offset=Op.MLOAD(offset=Op.ADD(Op.DUP8, 0xc4)), args_size=Op.DUP3, ret_offset=Op.DUP6, ret_size=Op.DUP1)) + Op.INVALID + Op.JUMPDEST + Op.POP + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.MLOAD(offset=Op.ADD(Op.DUP3, 0x1a8)) + Op.DUP1 + Op.JUMPI(pc=0xfe5, condition=Op.CALL(gas=Op.ADD(0x12, Op.SDIV(Op.DUP8, 0xa)), address=0x4, value=0x0, args_offset=Op.MLOAD(offset=Op.ADD(Op.DUP8, 0xe4)), args_size=Op.DUP3, ret_offset=Op.DUP6, ret_size=Op.DUP1)) + Op.INVALID + Op.JUMPDEST + Op.POP + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.MLOAD(offset=Op.ADD(Op.DUP3, 0x1c8)) + Op.DUP1 + Op.JUMPI(pc=0x100e, condition=Op.CALL(gas=Op.ADD(0x12, Op.SDIV(Op.DUP8, 0xa)), address=0x4, value=0x0, args_offset=Op.MLOAD(offset=Op.ADD(Op.DUP8, 0x104)), args_size=Op.DUP3, ret_offset=Op.DUP6, ret_size=Op.DUP1)) + Op.INVALID + Op.JUMPDEST + Op.POP + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.SUB(Op.DUP4, Op.DUP1) + Op.MLOAD(offset=0x120) + Op.ADD(Op.MUL(0x20, Op.DUP2), 0x40) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x80), value=0x0, args_offset=Op.DUP7, args_size=Op.DUP5, ret_offset=Op.DUP2, ret_size=Op.ADD(0x40, Op.MUL(0x20, Op.DUP2)))) + Op.ADD(Op.DUP2, 0x40) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x60] + Op.PUSH1[0x1c] + Op.PUSH2[0x14c] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x1112b27) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0xc0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0xe0)) + Op.DUP3 + Op.ADD(0x20, Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.DUP2, 0x20)))) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x44), value=Op.DUP4) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0xa4), value=Op.SUB(Op.DUP3, 0x20)) + Op.MSTORE(offset=Op.ADD(Op.DUP5, 0x108), value=Op.DUP1) + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.POP + Op.ADD(0x4, Op.DUP2) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.JUMPI(pc=0x10c4, condition=Op.CALL(gas=0x1c, address=0x4, value=0x0, args_offset=Op.DUP5, args_size=0x64, ret_offset=Op.DUP2, ret_size=0x64)) + Op.INVALID + Op.JUMPDEST + Op.ADD(Op.DUP2, 0x64) + Op.SWAP3 + Op.POP + Op.MLOAD(offset=Op.ADD(Op.DUP3, 0x108)) + Op.DUP1 + Op.JUMPI(pc=0x10eb, condition=Op.CALL(gas=Op.ADD(0x12, Op.SDIV(Op.DUP8, 0xa)), address=0x4, value=0x0, args_offset=Op.MLOAD(offset=Op.ADD(Op.DUP8, 0xa4)), args_size=Op.DUP3, ret_offset=Op.DUP6, ret_size=Op.DUP1)) + Op.INVALID + Op.JUMPDEST + Op.POP + Op.ADD(Op.DUP5, Op.DUP1) + Op.SWAP4 + Op.POP + Op.POP + Op.SUB(Op.DUP4, Op.DUP1) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP5, args_size=Op.DUP3, ret_offset=0x580, ret_size=0x20)) + Op.MLOAD(offset=0x580) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.POP + Op.JUMPI(pc=0x113a, condition=Op.ISZERO(Op.EQ(Op.MLOAD(offset=Op.ADD(Op.DUP6, Op.MUL(0x20, Op.ADD(Op.MLOAD(offset=0x100), 0x1)))), 0x0))) + Op.MSTORE(offset=0x5a0, value=0x0) + Op.RETURN(offset=0x5a0, size=0x20) + Op.JUMP(pc=0x1147) + Op.JUMPDEST + Op.MSTORE(offset=0x5c0, value=0x1) + Op.RETURN(offset=0x5c0, size=0x20) + Op.JUMPDEST + Op.POP + Op.POP + Op.POP + Op.POP + Op.JUMPDEST + Op.POP,
        ),
        contract: Account(
            code=Op.MSTORE8(offset=0x75f, value=0x0) + Op.DIV(Op.CALLDATALOAD(offset=0x0), 0x100000000000000000000000000000000000000000000000000000000) + Op.MSTORE(offset=0x20, value=0x1e147037f0a63df228fe6e7aef730f1ea31c8ce3) + Op.MSTORE(offset=0x40, value=0xea65418d7bf32680f55572c943a94b590804998) + Op.MSTORE(offset=0x60, value=0xe509e3a93beb1eba72f8cb8d25f93a85e2d54afb) + Op.MSTORE(offset=0x80, value=0xc9ae5868651bf7b7db6e360217db49ce4e69c07e) + Op.MSTORE(offset=0xa0, value=0x142a6927cf0060133187ba8a8e74d641438f0c1c) + Op.MSTORE(offset=0xc0, value=0xb163e767e4c1ba5ae88b2ee7594f3a3fec2bb096) + Op.MSTORE(offset=0xe0, value=0xba7b277319128ef4c22635534d0f61dffdaa13ab) + Op.MSTORE(offset=0x100, value=0x9761fecf88590592cf05ce545504d376d1693ab3) + Op.MSTORE(offset=0x120, value=0xf70bbc50f1468cecae0761ef09386a87c1c696ea) + Op.MSTORE(offset=0x140, value=0xa89d22f049aaa5bbfb5f1a1939fff3ae7a26ae74) + Op.MSTORE(offset=0x160, value=0x174827f7e53e8ce13b047adcac0eb3f2cb0c3285) + Op.JUMPI(pc=0xa88, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x36a560bd))) + Op.MSTORE(offset=0x1a0, value=Op.CALLDATALOAD(offset=0x4)) + Op.PUSH1[0x1c] + Op.PUSH1[0x44] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x27138bfb) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0)) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0xa0), value=0x0, args_offset=Op.DUP4, args_size=0x24, ret_offset=0x1e0, ret_size=0x20)) + Op.MLOAD(offset=0x1e0) + Op.SWAP1 + Op.POP + Op.JUMPI(pc=0x195, condition=Op.ISZERO(Op.ISZERO)) + Op.MSTORE(offset=0x200, value=Op.SUB(0x0, 0x1)) + Op.RETURN(offset=0x200, size=0x20) + Op.JUMPDEST + Op.PUSH1[0x1c] + Op.PUSH1[0x44] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x7a66d7ca) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0)) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x80), value=0x0, args_offset=Op.DUP4, args_size=0x24, ret_offset=0x220, ret_size=0x20)) + Op.MLOAD(offset=0x220) + Op.SWAP1 + Op.POP + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xcc1c944e) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.DUP2) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x280), value=0x0, args_offset=Op.DUP4, args_size=0x44, ret_offset=0x260, ret_size=0x20)) + Op.MLOAD(offset=0x260) + Op.SWAP1 + Op.POP + Op.PUSH1[0x1c] + Op.PUSH1[0x44] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x80b5e7bd) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0)) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x60), value=0x0, args_offset=Op.DUP4, args_size=0x24, ret_offset=0x2a0, ret_size=0x20)) + Op.MLOAD(offset=0x2a0) + Op.SWAP1 + Op.POP + Op.MUL(Op.DUP3, Op.DUP1) + Op.PUSH1[0x1c] + Op.PUSH1[0x44] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x18633576) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0)) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x80), value=0x0, args_offset=Op.DUP4, args_size=0x24, ret_offset=0x300, ret_size=0x20)) + Op.MLOAD(offset=0x300) + Op.SWAP1 + Op.POP + Op.JUMPI(pc=0x36d, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x9))) + Op.PUSH1[0x1c] + Op.PUSH1[0xc4] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xac44d71e) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.DUP6) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=Op.DUP5) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x64), value=Op.DUP4) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x84), value=Op.DUP3) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x160), value=0x0, args_offset=Op.DUP4, args_size=0xa4, ret_offset=0x360, ret_size=0x20)) + Op.MLOAD(offset=0x360) + Op.SWAP1 + Op.POP + Op.POP + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x7265802d) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=0x0) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x80), value=0x0, args_offset=Op.DUP4, args_size=0x44, ret_offset=0x380, ret_size=0x20)) + Op.MLOAD(offset=0x380) + Op.SWAP1 + Op.POP + Op.POP + Op.PUSH1[0x1c] + Op.PUSH1[0x44] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xc5476efe) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0)) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x80), value=0x0, args_offset=Op.DUP4, args_size=0x24, ret_offset=0x3a0, ret_size=0x20)) + Op.MLOAD(offset=0x3a0) + Op.SWAP1 + Op.POP + Op.POP + Op.MSTORE(offset=0x3c0, value=Op.ADD(Op.DUP6, 0x1)) + Op.RETURN(offset=0x3c0, size=0x20) + Op.JUMP(pc=0xa3a) + Op.JUMPDEST + Op.JUMPI(pc=0x3cd, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x0))) + Op.PUSH1[0x1c] + Op.PUSH1[0xc4] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xef72638a) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.DUP6) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=Op.DUP5) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x64), value=Op.DUP4) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x84), value=Op.DUP3) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0xc0), value=0x0, args_offset=Op.DUP4, args_size=0xa4, ret_offset=0x3e0, ret_size=0x20)) + Op.MLOAD(offset=0x3e0) + Op.SWAP1 + Op.POP + Op.POP + Op.JUMP(pc=0xa39) + Op.JUMPDEST + Op.JUMPI(pc=0x42d, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x1))) + Op.PUSH1[0x1c] + Op.PUSH1[0xc4] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xa63e976c) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.DUP6) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=Op.DUP5) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x64), value=Op.DUP4) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x84), value=Op.DUP3) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0xe0), value=0x0, args_offset=Op.DUP4, args_size=0xa4, ret_offset=0x400, ret_size=0x20)) + Op.MLOAD(offset=0x400) + Op.SWAP1 + Op.POP + Op.POP + Op.JUMP(pc=0xa38) + Op.JUMPDEST + Op.JUMPI(pc=0x48d, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x2))) + Op.PUSH1[0x1c] + Op.PUSH1[0xc4] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x533ea0ed) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.DUP6) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=Op.DUP5) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x64), value=Op.DUP4) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x84), value=Op.DUP3) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0xe0), value=0x0, args_offset=Op.DUP4, args_size=0xa4, ret_offset=0x420, ret_size=0x20)) + Op.MLOAD(offset=0x420) + Op.SWAP1 + Op.POP + Op.POP + Op.JUMP(pc=0xa37) + Op.JUMPDEST + Op.JUMPI(pc=0x850, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x3))) + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xe05dcb56) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.DUP6) + Op.ADD(Op.DUP6, 0x2) + Op.ADD(Op.MUL(0x20, Op.DUP2), 0x40) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x280), value=0x0, args_offset=Op.DUP6, args_size=0x44, ret_offset=Op.DUP2, ret_size=Op.ADD(0x40, Op.MUL(0x20, Op.DUP2)))) + Op.ADD(Op.DUP2, 0x40) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x1c] + Op.PUSH1[0x44] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x3d905045) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0)) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x80), value=0x0, args_offset=Op.DUP4, args_size=0x24, ret_offset=0x480, ret_size=0x20)) + Op.MLOAD(offset=0x480) + Op.SWAP1 + Op.POP + Op.JUMPI(pc=0x633, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x4))) + Op.PUSH1[0x1c] + Op.PUSH1[0xc4] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x939aa8c) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.DUP8) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=Op.DUP7) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x64), value=Op.DUP6) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x84), value=Op.DUP5) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x100), value=0x0, args_offset=Op.DUP4, args_size=0xa4, ret_offset=0x4e0, ret_size=0x20)) + Op.MLOAD(offset=0x4e0) + Op.SWAP1 + Op.POP + Op.PUSH2[0x4c0] + Op.MSTORE + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xc286273a) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=0x0) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x80), value=0x0, args_offset=Op.DUP4, args_size=0x44, ret_offset=0x500, ret_size=0x20)) + Op.MLOAD(offset=0x500) + Op.SWAP1 + Op.POP + Op.POP + Op.JUMPI(pc=0x5e5, condition=Op.ISZERO(Op.EQ(Op.MLOAD(offset=0x4c0), 0x1))) + Op.MSTORE(offset=0x520, value=Op.DUP3) + Op.RETURN(offset=0x520, size=0x20) + Op.JUMP(pc=0x62e) + Op.JUMPDEST + Op.PUSH1[0x1c] + Op.PUSH1[0x44] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xaac2ffb5) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0)) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x80), value=0x0, args_offset=Op.DUP4, args_size=0x24, ret_offset=0x540, ret_size=0x20)) + Op.MLOAD(offset=0x540) + Op.SWAP1 + Op.POP + Op.POP + Op.MSTORE(offset=0x560, value=Op.ADD(Op.DUP4, 0x1)) + Op.RETURN(offset=0x560, size=0x20) + Op.JUMPDEST + Op.JUMP(pc=0x804) + Op.JUMPDEST + Op.JUMPI(pc=0x694, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x0))) + Op.PUSH1[0x1c] + Op.PUSH1[0xc4] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x546fdeb3) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.DUP8) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=Op.DUP7) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x64), value=Op.DUP6) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x84), value=Op.DUP5) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x100), value=0x0, args_offset=Op.DUP4, args_size=0xa4, ret_offset=0x580, ret_size=0x20)) + Op.MLOAD(offset=0x580) + Op.SWAP1 + Op.POP + Op.POP + Op.JUMP(pc=0x803) + Op.JUMPDEST + Op.JUMPI(pc=0x742, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x1))) + Op.PUSH1[0x0] + Op.PUSH1[0x1c] + Op.PUSH1[0xc4] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xde9080c8) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.DUP9) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=Op.DUP8) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x64), value=Op.DUP7) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x84), value=Op.DUP6) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x100), value=0x0, args_offset=Op.DUP4, args_size=0xa4, ret_offset=0x5a0, ret_size=0x20)) + Op.MLOAD(offset=0x5a0) + Op.SWAP1 + Op.POP + Op.JUMPI(pc=0x732, condition=Op.ISZERO(Op.EQ)) + Op.PUSH1[0x1c] + Op.PUSH1[0x44] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x1cda01ef) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0)) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x80), value=0x0, args_offset=Op.DUP4, args_size=0x24, ret_offset=0x5c0, ret_size=0x20)) + Op.MLOAD(offset=0x5c0) + Op.SWAP1 + Op.POP + Op.POP + Op.JUMPDEST + Op.MSTORE(offset=0x5e0, value=Op.DUP3) + Op.RETURN(offset=0x5e0, size=0x20) + Op.JUMP(pc=0x802) + Op.JUMPDEST + Op.JUMPI(pc=0x7a3, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x2))) + Op.PUSH1[0x1c] + Op.PUSH1[0xc4] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x384ca8dd) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.DUP8) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=Op.DUP7) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x64), value=Op.DUP6) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x84), value=Op.DUP5) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x100), value=0x0, args_offset=Op.DUP4, args_size=0xa4, ret_offset=0x600, ret_size=0x20)) + Op.MLOAD(offset=0x600) + Op.SWAP1 + Op.POP + Op.POP + Op.JUMP(pc=0x801) + Op.JUMPDEST + Op.JUMPI(pc=0x800, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x3))) + Op.PUSH1[0x1c] + Op.PUSH1[0xc4] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xd5dc5af1) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.DUP8) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=Op.DUP7) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x64), value=Op.DUP6) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x84), value=Op.DUP5) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x100), value=0x0, args_offset=Op.DUP4, args_size=0xa4, ret_offset=0x620, ret_size=0x20)) + Op.MLOAD(offset=0x620) + Op.SWAP1 + Op.POP + Op.POP + Op.JUMPDEST + Op.JUMPDEST + Op.JUMPDEST + Op.JUMPDEST + Op.JUMPDEST + Op.PUSH1[0x1c] + Op.PUSH1[0x44] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x1cda01ef) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0)) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x80), value=0x0, args_offset=Op.DUP4, args_size=0x24, ret_offset=0x640, ret_size=0x20)) + Op.MLOAD(offset=0x640) + Op.SWAP1 + Op.POP + Op.POP + Op.MSTORE(offset=0x660, value=Op.DUP3) + Op.RETURN(offset=0x660, size=0x20) + Op.POP + Op.POP + Op.JUMP(pc=0xa36) + Op.JUMPDEST + Op.JUMPI(pc=0x8b1, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x4))) + Op.PUSH1[0x1c] + Op.PUSH1[0xc4] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xf6559853) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.DUP6) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=Op.DUP5) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x64), value=Op.DUP4) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x84), value=Op.DUP3) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x120), value=0x0, args_offset=Op.DUP4, args_size=0xa4, ret_offset=0x680, ret_size=0x20)) + Op.MLOAD(offset=0x680) + Op.SWAP1 + Op.POP + Op.POP + Op.JUMP(pc=0xa35) + Op.JUMPDEST + Op.JUMPI(pc=0x912, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x5))) + Op.PUSH1[0x1c] + Op.PUSH1[0xc4] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xd8e5473d) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.DUP6) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=Op.DUP5) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x64), value=Op.DUP4) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x84), value=Op.DUP3) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x120), value=0x0, args_offset=Op.DUP4, args_size=0xa4, ret_offset=0x6a0, ret_size=0x20)) + Op.MLOAD(offset=0x6a0) + Op.SWAP1 + Op.POP + Op.POP + Op.JUMP(pc=0xa34) + Op.JUMPDEST + Op.JUMPI(pc=0x973, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x6))) + Op.PUSH1[0x1c] + Op.PUSH1[0xc4] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x90507ea) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.DUP6) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=Op.DUP5) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x64), value=Op.DUP4) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x84), value=Op.DUP3) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x120), value=0x0, args_offset=Op.DUP4, args_size=0xa4, ret_offset=0x6c0, ret_size=0x20)) + Op.MLOAD(offset=0x6c0) + Op.SWAP1 + Op.POP + Op.POP + Op.JUMP(pc=0xa33) + Op.JUMPDEST + Op.JUMPI(pc=0x9d4, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x7))) + Op.PUSH1[0x1c] + Op.PUSH1[0xc4] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x5b911842) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.DUP6) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=Op.DUP5) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x64), value=Op.DUP4) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x84), value=Op.DUP3) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x140), value=0x0, args_offset=Op.DUP4, args_size=0xa4, ret_offset=0x6e0, ret_size=0x20)) + Op.MLOAD(offset=0x6e0) + Op.SWAP1 + Op.POP + Op.POP + Op.JUMP(pc=0xa32) + Op.JUMPDEST + Op.JUMPI(pc=0xa31, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x8))) + Op.PUSH1[0x1c] + Op.PUSH1[0xc4] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xabe22b84) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.DUP6) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=Op.DUP5) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x64), value=Op.DUP4) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x84), value=Op.DUP3) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x140), value=0x0, args_offset=Op.DUP4, args_size=0xa4, ret_offset=0x700, ret_size=0x20)) + Op.MLOAD(offset=0x700) + Op.SWAP1 + Op.POP + Op.POP + Op.JUMPDEST + Op.JUMPDEST + Op.JUMPDEST + Op.JUMPDEST + Op.JUMPDEST + Op.JUMPDEST + Op.JUMPDEST + Op.JUMPDEST + Op.JUMPDEST + Op.JUMPDEST + Op.PUSH1[0x1c] + Op.PUSH1[0x44] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xaac2ffb5) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x1a0)) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x80), value=0x0, args_offset=Op.DUP4, args_size=0x24, ret_offset=0x720, ret_size=0x20)) + Op.MLOAD(offset=0x720) + Op.SWAP1 + Op.POP + Op.POP + Op.MSTORE(offset=0x740, value=Op.ADD(Op.DUP2, 0x1)) + Op.RETURN(offset=0x740, size=0x20) + Op.POP + Op.POP + Op.POP + Op.POP + Op.POP + Op.JUMPDEST + Op.POP,
        ),
        callee_8: Account(
            storage={0: 1, 0xa4470e9d0419df71f6257fcdfd2c0a3bad96a23f5ab414bc10aaf1a31a536a7: 0xb4876148229c22bd2291f1a4f5468c8c789b23639370c4d447f270ba341dbbec, 0x16ef4193a274568d283ff919c299729e07696d9ada48187b81d68e12e7b962de: 0xa103c04e7ecb9b3395f77c7b0cad28e62c85f042de4767ccc6c005e6f47f8d4, 0x1f1866e966f321b84535705846689749d34d5dc02994613e2931973c605d9e93: 0xc723d0aa4a60529fe42277c8094aa19263aff36650136efc5edfd0785d457634, 0x252a4ec7133643fddcdb22a86c415f78b2dd251f18d1efcd6a44acf590c4ae72: 0x9caf94b82715869e71d3cee986094ea612f0258570b7e5ef47b5d09e9515322b, 0x41b451e8d86d28add758cbd3f48a18fd04b11a80288c1dc434a5bf2d8fb1ca64: 0xb602498f12a8b4af3a1fca357cea6b19bcd163dfec1d845364ce1395f7c21fa7, 0x491d10658c1ec762152d8ad2d890ad59111b1ee7b4bc25736046923d3534d9a5: 25246, 0x5b0e8552efd72a845e47318abbbef9dc9fcdfe0d1a06cda44494401301581511: 0xfbc98f4017ae5c20459daadaa6bee519b6de871d3dbaa9ab3f34340fef4cb643, 0x5b672a107ba6fab01cbddf079042e9f6176a8e6f154584fc4df4b15674c9456e: 0x1603da41d610854d85536b37d000e5eb7ca09786c43f50e7441c0afbff1de0a9, 0x605b934bd26c9ecdf7029a7dc062d3a6b87338511cff96e0c5f13de9eea3462e: 0xf0d24f3d0eda573fc5d43e3d0680993c51293752cd6de205040d3197f412f475, 0x618355e25491dfe86175f9d9b3147e4d680aa561d98384e3621dc6a3088b0846: 0x6b2e6d2d5deb27dffec973f23af4caf111e66d1397f467dbbedf5ab2192fb6b6, 0x65112936bec0f1e84fda6623fb54e12baadc8a4a208c8c4eb3ed5e79cbd7e85f: 0xa59ac24e3e0663413d0f87516ba8fb44c6c3e14da8eaabbde80f8ee285f65934, 0x687cb2122de7bacf42b9cd380b04ff2a2ce92a0b63706a9a78263b3ce86f3313: 0x200000000000000, 0x72a539b064c98d29a514ee55694225e05fb41fe63e5fe710e4536bd9ba3591b4: 0x338ecfe6c523ed1184918b19584d97dd1095ecaadc49c7ba9da62b8b513026e0, 0x7aeb0a0ce8882a12d853078382a2bc72f7a94af6109f167de37b36c0a7deb828: 0x4c428400ea8a7bd7c46ba9895b508770efa4551f0d793e1beb1207da01d9962f, 0x7c8f4a98e086f64e28c75f54712b5d44bec3c29b5c70519e8880d3046a5618dc: 0xaafc1f2601752b114d722070f75539bfec7faf49f0d48a48d27862f0c3b09903, 0x809c325f50acf5787776e960985e72443b4330ad1e2f466557fffee16ba51d44: 0xb940a56e64b5b661d87919b8ef03640ec077a6d72dd0b524adedaa7ddc91ff7a, 0x84e4a80d33c5d2abd2b0a5aec0fdc5eaeed90ab31db556e404a81718ea286e39: 28, 0x877305412fa2486f563c457b744e5c8b1e4d0eca73371de5e771f2abc263f4dc: 0x7088a36f67276d475aa62127cfde9790cc802fdf3a54df49461a25eb8bf15707, 0x922a8f2fc1cbe67c8acc6a8a720983c366d71d3e2e78e3048949ebc913ea611a: 0x50fb9f913ca102534bb0a8eb8ebf19c68dfd16ffe5e207bcc580084cd4ecd8b4, 0x987cb9ecfd8ce499d9d0e9e6b7da29617aa02774a34f4a8ea54442f44a1e1936: 0x5179f98f555f1e9f1d4a335d16f41154579a53e361e9859269b6fa74ea9c7d21, 0xada5013122d395ba3c54772283fb069b10426056ef8ca54750cb9bb552a59e7d: 0xf69b5, 0xb16b117660f31197087f4d6fe50d3d4579152244956f753f9653ccf85f4b35c4: 0x830272e3bb35226b047244cbdc46f1b6b864a280461e7a592f70e0863f4f1d33, 0xb1f1aaedfb83c7755a2bffc9e2557f1723f9abe5642397963e76248c9209af57: 0xe9be955c5fbfcd846d7425eaea05ce897786aefad99665342cbf30761b352526, 0xb7bd50fdf7b043411c9ac33f0af2cebc69c393eb0b91f4976946f9c7b15ad0da: 0xfccca0e7832bae9afe799a6d6177dc3869fa6c5b5105f8df6f365de5723820ec, 0xbc96058eb03504ee6f5c0a9582f8720d99a6e9738b171499507facff0b2c0b5b: 0x9db6a4f2766b51013b8d2f9038131d1bb4af725d019d111d7e26ff96c023b23f, 0xc186c4f377b7f13892ade9656acd1522aa1f8ac151ac4f62457b5073241d79fc: 0x7289738fef00f1770eeb098db9bd486c01ac12398d79cdf935514a128c585c51, 0xcae57ae3017972d63effd8eae44f5054402c3e890d154b905ed6b5b533327fa9: 0xd2e4bf465e61993d13089b940a7c55017a5117d8e43e4115550a139e1d4b3e3a, 0xcf569ee7bf3accc0f893dffd04f1a757f373efe80893eff504fb3678f688ec1d: 3, 0xd69b7284545a9f5275df64ce94848dc954fcb8a8b525e7ac801517c12a75af84: 0x4202995350abae303b43e564aa79121a30b5f1aea31f69cd25e07dd3fa64dce7, 0xd8f6f90f51e657690ee28d1cc80d81bc1b89290065891fdd853d09caaaf756aa: 1, 0xde72f8eed43cc2a5a3eaa51483d14b17dc92bb26c154ae184cee4b4895011edc: 0x47ce2b6fdb72c3fabb9c74f82c1e3e522bcd42e614fd85c208ac3c4c840cea72, 0xe0e687ddf317f3d2b209ae3884148eff0f636e16827f82eded14ada8fc603009: 0xfa7c8939f9b033162cf8d75ea69671bb8a27041bd4cdc76594e61e99333cb041, 0xe8cda339d72a1a350b62f1e3fa52e254c395cc9fdd9f60adb21c7633fbdab531: 0x128c4fdf4801a30eae99dd58f0f3ff5ca65f71b66a9ac0f38dd450fb24b4aaaa, 0xec5e7f54fa5e516e616b04f9d5a0ee433a80e09ed47d7e5269afd76c05ff251e: 20, 0xf9a3bf5f2ccb903ee1a7644113b794db0260de404fb8f11203e75a7fff151618: 0xbd94773c0d85c68240ae8dfd53d9d33cd137509bfc5d3433381299df768c8377},
            code=Op.MSTORE8(offset=0x83f, value=0x0) + Op.DIV(Op.CALLDATALOAD(offset=0x0), 0x100000000000000000000000000000000000000000000000000000000) + Op.JUMPI(pc=Op.PUSH2[0x66], condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x7a66d7ca))) + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x4)) + Op.PUSH1[0x60] + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=0x60, value=Op.SLOAD(key=Op.SHA3)) + Op.RETURN(offset=0x60, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=Op.PUSH2[0xa5], condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xc60409c6))) + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x4)) + Op.PUSH1[0x60] + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=0xa0, value=Op.SLOAD(key=Op.SHA3)) + Op.RETURN(offset=0xa0, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=Op.PUSH2[0xe4], condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x18633576))) + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x4)) + Op.PUSH1[0x60] + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x2) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=0xe0, value=Op.SLOAD(key=Op.SHA3)) + Op.RETURN(offset=0xe0, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x1bc, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xb3903c8a))) + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x4)) + Op.PUSH1[0x60] + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x5) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=0x120, value=Op.SLOAD(key=Op.SHA3)) + Op.MLOAD(offset=0x120) + Op.ADD(0x20, Op.MUL(0x20, Op.DUP1)) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH2[0x160] + Op.MSTORE + Op.MSTORE(offset=0x1c0, value=0x0) + Op.JUMPDEST + Op.JUMPI(pc=0x19f, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x1c0), Op.MLOAD(offset=0x120)))) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x4) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0)) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x160), Op.MUL(0x20, Op.MLOAD(offset=0x1c0))), value=Op.SLOAD(key=Op.SHA3)) + Op.MSTORE(offset=0x1c0, value=Op.ADD(Op.MLOAD(offset=0x1c0), 0x1)) + Op.JUMP(pc=0x147) + Op.JUMPDEST + Op.MLOAD(offset=0x160) + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20) + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20))) + Op.POP + Op.JUMPDEST + Op.JUMPI(pc=0x1fd, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x6824e0fb))) + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x4)) + Op.PUSH1[0x60] + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x5) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=0x220, value=Op.SLOAD(key=Op.SHA3)) + Op.RETURN(offset=0x220, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x23e, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x3db16be3))) + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x4)) + Op.PUSH1[0x60] + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x6) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=0x260, value=Op.SLOAD(key=Op.SHA3)) + Op.RETURN(offset=0x260, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x2e0, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xc3387858))) + Op.MSTORE(offset=0x2a0, value=0x0) + Op.MSTORE(offset=0x2c0, value=Op.SLOAD(key=0x0)) + Op.MLOAD(offset=0x2c0) + Op.ADD(0x20, Op.MUL(0x20, Op.DUP1)) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH2[0x2e0] + Op.MSTORE + Op.JUMPDEST + Op.JUMPI(pc=0x2c3, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x2a0), Op.MLOAD(offset=0x2c0)))) + Op.PUSH1[0x40] + Op.PUSH1[0x40] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x1) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x2a0)) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x2e0), Op.MUL(0x20, Op.MLOAD(offset=0x2a0))), value=Op.SLOAD(key=Op.SHA3)) + Op.MSTORE(offset=0x2a0, value=Op.ADD(Op.MLOAD(offset=0x2a0), 0x1)) + Op.JUMP(pc=0x27a) + Op.JUMPDEST + Op.MLOAD(offset=0x2e0) + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20) + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20))) + Op.POP + Op.JUMPDEST + Op.JUMPI(pc=0x2fa, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x175c6322))) + Op.MSTORE(offset=0x380, value=Op.SLOAD(key=0x0)) + Op.RETURN(offset=0x380, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x336, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xd861f2b4))) + Op.MSTORE(offset=0x3a0, value=Op.CALLDATALOAD(offset=0x4)) + Op.PUSH1[0x40] + Op.PUSH1[0x40] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x1) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x3a0)) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=0x3c0, value=Op.SLOAD(key=Op.SHA3)) + Op.RETURN(offset=0x3c0, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x44f, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xb0dab01f))) + Op.MSTORE(offset=0x400, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x420, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x440, value=Op.CALLDATALOAD(offset=0x44)) + Op.MSTORE(offset=0x460, value=Op.CALLDATALOAD(offset=0x64)) + Op.PUSH1[0x0] + Op.PUSH1[0x60] + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x400)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.JUMPI(pc=0x441, condition=Op.ISZERO(Op.EQ)) + Op.MLOAD(offset=0x420) + Op.PUSH1[0x60] + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x400)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.MLOAD(offset=0x440) + Op.PUSH1[0x60] + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x400)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.MLOAD(offset=0x460) + Op.PUSH1[0x60] + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x400)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x6) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.MLOAD(offset=0x400) + Op.PUSH1[0x40] + Op.PUSH1[0x40] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x1) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.SLOAD(key=0x0)) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.SSTORE(key=0x0, value=Op.ADD(Op.SLOAD(key=0x0), 0x1)) + Op.MSTORE(offset=0x520, value=0x1) + Op.RETURN(offset=0x520, size=0x20) + Op.JUMP(pc=0x44e) + Op.JUMPDEST + Op.MSTORE(offset=0x540, value=0x0) + Op.RETURN(offset=0x540, size=0x20) + Op.JUMPDEST + Op.JUMPDEST + Op.JUMPI(pc=0x4b9, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xaac2ffb5))) + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x4)) + Op.PUSH1[0x1] + Op.PUSH1[0x60] + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x2) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.ADD + Op.PUSH1[0x60] + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x2) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.MSTORE(offset=0x5a0, value=0x1) + Op.RETURN(offset=0x5a0, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x507, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x7265802d))) + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x5c0, value=Op.CALLDATALOAD(offset=0x24)) + Op.MLOAD(offset=0x5c0) + Op.PUSH1[0x60] + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x2) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.MSTORE(offset=0x600, value=0x1) + Op.RETURN(offset=0x600, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x571, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xc5476efe))) + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x4)) + Op.PUSH1[0x1] + Op.PUSH1[0x60] + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.ADD + Op.PUSH1[0x60] + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.MSTORE(offset=0x660, value=0x1) + Op.RETURN(offset=0x660, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x63b, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xc551e31e))) + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x680, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0x60] + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x5) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=0x120, value=Op.SLOAD(key=Op.SHA3)) + Op.MLOAD(offset=0x680) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x4) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x120)) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.PUSH1[0x1] + Op.PUSH1[0x60] + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x5) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.ADD + Op.PUSH1[0x60] + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x5) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.MSTORE(offset=0x720, value=0x1) + Op.RETURN(offset=0x720, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x67c, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x3d905045))) + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x4)) + Op.PUSH1[0x60] + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x3) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=0x740, value=Op.SLOAD(key=Op.SHA3)) + Op.RETURN(offset=0x740, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x6e6, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x1cda01ef))) + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x4)) + Op.PUSH1[0x1] + Op.PUSH1[0x60] + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x3) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.ADD + Op.PUSH1[0x60] + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x3) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.MSTORE(offset=0x7c0, value=0x1) + Op.RETURN(offset=0x7c0, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x734, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xc286273a))) + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x7e0, value=Op.CALLDATALOAD(offset=0x24)) + Op.MLOAD(offset=0x7e0) + Op.PUSH1[0x60] + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x3) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.MSTORE(offset=0x820, value=0x1) + Op.RETURN(offset=0x820, size=0x20) + Op.JUMPDEST + Op.POP,
        ),
        callee_9: Account(
            storage={0xf299dbbe3a7a5d949fe794e9a47b3106699c8110ff986eb84921c183e69e7f0: 0x2f0000000000000000, 0x1edcd36f61cae5dc6414157dfbadf9f11ca013ac763e27f8af55feaa8a239c89: 1, 0x689082d076ec3c02cbe4b99f6d9833e3c4a161072fd42fb7649eee5189a67ccc: 0x63524e3fe4791aefce1e932bbfb3fdf375bfad89, 0xaf1d6676be3ab502a59d91f6f5c49baffc15b2cfc65a41c4d96857c0f535adba: 0x1d60000000000000000, 0xdf1a770f69d93d1719292f384fdb4da22c0e88aef2ba462bff16674bc7848730: 0x1c11aa45c792e202e9ffdc2f12f99d0d209bef70, 0xec5e7f54fa5e516e616b04f9d5a0ee433a80e09ed47d7e5269afd76c05ff251e: 2},
            code=Op.MSTORE8(offset=0xb7f, value=0x0) + Op.DIV(Op.CALLDATALOAD(offset=0x0), 0x100000000000000000000000000000000000000000000000000000000) + Op.MSTORE(offset=0x20, value=0xc9ae5868651bf7b7db6e360217db49ce4e69c07e) + Op.JUMPI(pc=0x245, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x8d3d587))) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.PUSH1[0x60] + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=0x80, value=Op.SLOAD(key=Op.SHA3)) + Op.PUSH1[0x0] + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x2) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.ORIGIN) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.JUMPI(pc=0x14e, condition=Op.ISZERO(Op.ISZERO(Op.EQ))) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x2) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.ORIGIN) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=0x80, value=Op.SLOAD(key=Op.SHA3)) + Op.PUSH9[0x2f0000000000000000] + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.ORIGIN + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.JUMP(pc=0x238) + Op.JUMPDEST + Op.MLOAD(offset=0x80) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x2) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.ORIGIN) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.PUSH9[0x2f0000000000000000] + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.ORIGIN + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.PUSH1[0x1] + Op.PUSH1[0x60] + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.ADD + Op.PUSH1[0x60] + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.JUMPDEST + Op.MSTORE(offset=0x1e0, value=0x1) + Op.RETURN(offset=0x1e0, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x29d, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x28c8b315))) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x200, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x200)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=0x220, value=Op.SLOAD(key=Op.SHA3)) + Op.RETURN(offset=0x220, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x386, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x74af23ec))) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x260, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x2) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x260)) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=0x200, value=Op.SLOAD(key=Op.SHA3)) + Op.JUMPI(pc=0x332, condition=Op.ISZERO(Op.EQ(Op.MLOAD(offset=0x200), 0x0))) + Op.MLOAD(offset=0x260) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x200)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.ISZERO(Op.EQ) + Op.JUMP(pc=0x335) + Op.JUMPDEST + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x347, condition=Op.ISZERO) + Op.MSTORE(offset=0x2c0, value=0x0) + Op.RETURN(offset=0x2c0, size=0x20) + Op.JUMPDEST + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x200)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=0x2e0, value=Op.SLOAD(key=Op.SHA3)) + Op.RETURN(offset=0x2e0, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x3dc, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x84d646ee))) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=0x320, value=Op.SLOAD(key=Op.SHA3)) + Op.RETURN(offset=0x320, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x6f4, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xf4229427))) + Op.MSTORE(offset=0x260, value=Op.CALLDATALOAD(offset=0x4)) + Op.PUSH1[0x1c] + Op.PUSH1[0x24] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x175c6322) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP4, args_size=0x4, ret_offset=0x3a0, ret_size=0x20)) + Op.MLOAD(offset=0x3a0) + Op.SWAP1 + Op.POP + Op.PUSH2[0x360] + Op.MSTORE + Op.JUMPI(pc=0x581, condition=Op.ISZERO(Op.MLOAD(offset=0x260))) + Op.MUL(0x2, Op.MLOAD(offset=0x360)) + Op.ADD(0x20, Op.MUL(0x20, Op.DUP1)) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH2[0x3c0] + Op.MSTORE + Op.MLOAD(offset=0x360) + Op.ADD(0x20, Op.MUL(0x20, Op.DUP1)) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH2[0x420] + Op.MSTORE + Op.PUSH1[0x1c] + Op.PUSH1[0x24] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xc3387858) + Op.MLOAD(offset=0x360) + Op.ADD(Op.MUL(0x20, Op.DUP2), 0x40) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP6, args_size=0x4, ret_offset=Op.DUP2, ret_size=Op.ADD(0x40, Op.MUL(0x20, Op.DUP2)))) + Op.ADD(Op.DUP2, 0x40) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH2[0x420] + Op.MSTORE + Op.MSTORE(offset=0x4c0, value=0x0) + Op.MSTORE(offset=0x4e0, value=0x0) + Op.JUMPDEST + Op.JUMPI(pc=0x57c, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x4c0), Op.MLOAD(offset=0x360)))) + Op.MSTORE(offset=0x60, value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x420), Op.MUL(0x20, Op.MLOAD(offset=0x4c0))))) + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x74af23ec) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0x260)) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.ADDRESS, value=0x0, args_offset=Op.DUP4, args_size=0x44, ret_offset=0x520, ret_size=0x20)) + Op.MLOAD(offset=0x520) + Op.SWAP1 + Op.POP + Op.PUSH2[0x500] + Op.MSTORE + Op.JUMPI(pc=0x56c, condition=Op.ISZERO(Op.ISZERO(Op.EQ(Op.MLOAD(offset=0x500), 0x0)))) + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x3c0), Op.MUL(0x20, Op.MLOAD(offset=0x4e0))), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x3c0), Op.MUL(0x20, Op.ADD(Op.MLOAD(offset=0x4e0), 0x1))), value=Op.MLOAD(offset=0x500)) + Op.MSTORE(offset=0x4e0, value=Op.ADD(Op.MLOAD(offset=0x4e0), 0x2)) + Op.JUMPDEST + Op.MSTORE(offset=0x4c0, value=Op.ADD(Op.MLOAD(offset=0x4c0), 0x1)) + Op.JUMP(pc=0x4ce) + Op.JUMPDEST + Op.JUMP(pc=0x6d7) + Op.JUMPDEST + Op.MSTORE(offset=0x260, value=Op.ORIGIN) + Op.MUL(0x2, Op.MLOAD(offset=0x360)) + Op.ADD(0x20, Op.MUL(0x20, Op.DUP1)) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH2[0x3c0] + Op.MSTORE + Op.MLOAD(offset=0x360) + Op.ADD(0x20, Op.MUL(0x20, Op.DUP1)) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH2[0x420] + Op.MSTORE + Op.PUSH1[0x1c] + Op.PUSH1[0x24] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xc3387858) + Op.MLOAD(offset=0x360) + Op.ADD(Op.MUL(0x20, Op.DUP2), 0x40) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x20), value=0x0, args_offset=Op.DUP6, args_size=0x4, ret_offset=Op.DUP2, ret_size=Op.ADD(0x40, Op.MUL(0x20, Op.DUP2)))) + Op.ADD(Op.DUP2, 0x40) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH2[0x420] + Op.MSTORE + Op.MSTORE(offset=0x4c0, value=0x0) + Op.MSTORE(offset=0x4e0, value=0x0) + Op.JUMPDEST + Op.JUMPI(pc=0x6d6, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x4c0), Op.MLOAD(offset=0x360)))) + Op.MSTORE(offset=0x60, value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x420), Op.MUL(0x20, Op.MLOAD(offset=0x4c0))))) + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x74af23ec) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0x260)) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.ADDRESS, value=0x0, args_offset=Op.DUP4, args_size=0x44, ret_offset=0x5c0, ret_size=0x20)) + Op.MLOAD(offset=0x5c0) + Op.SWAP1 + Op.POP + Op.PUSH2[0x500] + Op.MSTORE + Op.JUMPI(pc=0x6c6, condition=Op.ISZERO(Op.ISZERO(Op.EQ(Op.MLOAD(offset=0x500), 0x0)))) + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x3c0), Op.MUL(0x20, Op.MLOAD(offset=0x4e0))), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x3c0), Op.MUL(0x20, Op.ADD(Op.MLOAD(offset=0x4e0), 0x1))), value=Op.MLOAD(offset=0x500)) + Op.MSTORE(offset=0x4e0, value=Op.ADD(Op.MLOAD(offset=0x4e0), 0x2)) + Op.JUMPDEST + Op.MSTORE(offset=0x4c0, value=Op.ADD(Op.MLOAD(offset=0x4c0), 0x1)) + Op.JUMP(pc=0x628) + Op.JUMPDEST + Op.JUMPDEST + Op.MLOAD(offset=0x3c0) + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20) + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20))) + Op.POP + Op.JUMPDEST + Op.JUMPI(pc=0x735, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x80b5e7bd))) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.PUSH1[0x60] + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=0x600, value=Op.SLOAD(key=Op.SHA3)) + Op.RETURN(offset=0x600, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x786, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x156f1c32))) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x640, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x2) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x640)) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=0x660, value=Op.SLOAD(key=Op.SHA3)) + Op.RETURN(offset=0x660, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x878, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xb3a24fc0))) + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE) + Op.MSTORE(offset=0x6c0, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x4))) + Op.MSTORE(offset=0x6e0, value=Op.CALLDATALOAD(offset=0x24)) + Op.POP + Op.ADD(Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x6c0), 0x20)), 0x2) + Op.ADD(0x20, Op.MUL(0x20, Op.DUP1)) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH2[0x700] + Op.MSTORE + Op.MSTORE(offset=Op.MLOAD(offset=0x700), value=Op.ORIGIN) + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x700), 0x20), value=Op.MLOAD(offset=0x6e0)) + Op.MSTORE(offset=0x4c0, value=0x2) + Op.JUMPDEST + Op.JUMPI(pc=0x838, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x4c0), Op.ADD(Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x6c0), 0x20)), 0x2)))) + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x700), Op.MUL(0x20, Op.MLOAD(offset=0x4c0))), value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x6c0), Op.MUL(0x20, Op.SUB(Op.MLOAD(offset=0x4c0), 0x2))))) + Op.MSTORE(offset=0x4c0, value=Op.ADD(Op.MLOAD(offset=0x4c0), 0x1)) + Op.JUMP(pc=0x7f6) + Op.JUMPDEST + Op.MUL(0x20, Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x700), 0x20))) + Op.PUSH1[0x20] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.POP(Op.CALL(gas=Op.ADD(0x48, Op.DUP8), address=0x2, value=0x0, args_offset=Op.MLOAD(offset=0x700), args_size=Op.DUP4, ret_offset=Op.DUP2, ret_size=0x20)) + Op.MLOAD(offset=Op.DUP1) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH2[0x760] + Op.MSTORE + Op.MSTORE(offset=0x7c0, value=Op.MLOAD(offset=0x760)) + Op.RETURN(offset=0x7c0, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0xa1c, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xe346f5fc))) + Op.MSTORE(offset=0x7e0, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x800, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x4c0, value=0x0) + Op.JUMPDEST + Op.PUSH1[0x60] + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x7e0)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.JUMPI(pc=0x9e6, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x4c0), Op.SLOAD(key=Op.SHA3)))) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x7e0)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x4c0)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=0x840, value=Op.SLOAD(key=Op.SHA3)) + Op.MLOAD(offset=0x840) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x800)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x4c0)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x7e0)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x4c0)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x800)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x4c0)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.MLOAD(offset=0x4c0) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x800)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x2) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x840)) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.MSTORE(offset=0x4c0, value=Op.ADD(Op.MLOAD(offset=0x4c0), 0x1)) + Op.JUMP(pc=0x899) + Op.JUMPDEST + Op.MLOAD(offset=0x4c0) + Op.PUSH1[0x60] + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x800)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.MSTORE(offset=0x920, value=0x1) + Op.RETURN(offset=0x920, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0xb54, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x3fb57036))) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x940, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0x60] + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=0x960, value=Op.SLOAD(key=Op.SHA3)) + Op.MLOAD(offset=0x960) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x2) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x940)) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.PUSH1[0x0] + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x960)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.MLOAD(offset=0x940) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x960)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.PUSH1[0x1] + Op.PUSH1[0x60] + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.ADD + Op.PUSH1[0x60] + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.MSTORE(offset=0xa40, value=0x1) + Op.RETURN(offset=0xa40, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0xbeb, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x12709a33))) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0xa60, value=Op.CALLDATALOAD(offset=0x44)) + Op.MLOAD(offset=0xa60) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.ADD + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.MSTORE(offset=0xac0, value=0x1) + Op.RETURN(offset=0xac0, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0xc82, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x3229cf6e))) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0xa60, value=Op.CALLDATALOAD(offset=0x44)) + Op.MLOAD(offset=0xa60) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.SUB + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.MSTORE(offset=0xb20, value=0x1) + Op.RETURN(offset=0xb20, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0xce5, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xa75f5c6a))) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0xa60, value=Op.CALLDATALOAD(offset=0x44)) + Op.MLOAD(offset=0xa60) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0x0) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.MSTORE(offset=0xb60, value=0x1) + Op.RETURN(offset=0xb60, size=0x20) + Op.JUMPDEST + Op.POP,
        ),
        callee_10: Account(
            code=Op.MSTORE8(offset=0x67f, value=0x0) + Op.DIV(Op.CALLDATALOAD(offset=0x0), 0x100000000000000000000000000000000000000000000000000000000) + Op.JUMPI(pc=Op.PUSH2[0xac], condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x2f300bee))) + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x44)) + Op.ADD(Op.MLOAD(offset=0x80), 0x2) + Op.DUP1 + Op.ADD(0x20, Op.MUL(0x20, Op.DUP1)) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.DUP2, value=0x10000000000000000) + Op.MSTORE(offset=Op.ADD(Op.DUP3, Op.MUL(0x20, Op.MLOAD(offset=0x80))), value=Op.MLOAD(offset=0x60)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, Op.MUL(0x20, Op.ADD(Op.MLOAD(offset=0x80), 0x1))), value=Op.SUB(Op.MLOAD(offset=0x40), 0x1)) + Op.DUP1 + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20) + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20))) + Op.POP + Op.POP + Op.POP + Op.JUMPDEST + Op.JUMPI(pc=0x2c8, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xa647a5b9))) + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE) + Op.MSTORE(offset=0x100, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x4))) + Op.MSTORE(offset=0x160, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x24))) + Op.MSTORE(offset=0x180, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x44))) + Op.MSTORE(offset=0x1a0, value=Op.CALLDATALOAD(offset=0x64)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x84)) + Op.POP + Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x100), 0x20)) + Op.DUP1 + Op.ADD(0x20, Op.MUL(0x20, Op.DUP1)) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x1d5, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.MLOAD(offset=0x1a0)))) + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x162, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.MLOAD(offset=0x80)))) + Op.ADD(Op.DUP3, Op.MUL(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x160), Op.MUL(0x20, Op.ADD(Op.MUL(Op.DUP6, Op.MLOAD(offset=0x80)), Op.DUP2)))), Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x100), Op.MUL(0x20, Op.DUP1))))) + Op.SWAP2 + Op.POP + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x12e) + Op.JUMPDEST + Op.POP + Op.SDIV(Op.DUP2, 0x10000000000000000) + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x1c8, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.MLOAD(offset=0x80)))) + Op.MSTORE(offset=Op.ADD(Op.DUP6, Op.MUL(0x20, Op.DUP2)), value=Op.SUB(Op.MLOAD(offset=Op.ADD(Op.DUP6, Op.MUL(0x20, Op.DUP2))), Op.SDIV(Op.MUL(Op.MUL(Op.DUP5, Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x160), Op.MUL(0x20, Op.ADD(Op.MUL(Op.DUP7, Op.MLOAD(offset=0x80)), Op.DUP3))))), Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x180), Op.MUL(0x20, Op.DUP4)))), 0x100000000000000000000000000000000))) + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x174) + Op.JUMPDEST + Op.POP + Op.POP + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x11e) + Op.JUMPDEST + Op.POP + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x203, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.MLOAD(offset=0x80)))) + Op.ADD(Op.DUP3, Op.MUL(Op.MLOAD(offset=Op.ADD(Op.DUP5, Op.MUL(0x20, Op.DUP2))), Op.MLOAD(offset=Op.ADD(Op.DUP4, Op.MUL(0x20, Op.DUP1))))) + Op.SWAP2 + Op.POP + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x1db) + Op.JUMPDEST + Op.POP + Op.SDIV(Op.DUP2, 0x10000000000000000) + Op.SWAP1 + Op.POP + Op.SDIV(Op.DUP2, 0x2) + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x242, condition=Op.ISZERO(Op.SLT(Op.DUP2, 0xb))) + Op.SDIV(Op.ADD(Op.DUP4, Op.SDIV(Op.MUL(Op.DUP6, 0x10000000000000000), Op.DUP3)), 0x2) + Op.SWAP2 + Op.POP + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x219) + Op.JUMPDEST + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x276, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.MLOAD(offset=0x80)))) + Op.MSTORE(offset=Op.ADD(Op.DUP6, Op.MUL(0x20, Op.DUP2)), value=Op.SDIV(Op.MUL(Op.MLOAD(offset=Op.ADD(Op.DUP7, Op.MUL(0x20, Op.DUP3))), 0x10000000000000000), Op.DUP2)) + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x246) + Op.JUMPDEST + Op.POP + Op.POP + Op.POP + Op.MSTORE(offset=Op.ADD(Op.DUP3, Op.MUL(0x20, Op.MLOAD(offset=0x80))), value=Op.SUB(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x100), Op.MUL(0x20, Op.MLOAD(offset=0x80)))), 0x1)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, Op.MUL(0x20, Op.ADD(Op.MLOAD(offset=0x80), 0x1))), value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x100), Op.MUL(0x20, Op.ADD(Op.MLOAD(offset=0x80), 0x1))))) + Op.DUP1 + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20) + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20))) + Op.POP + Op.POP + Op.POP + Op.JUMPDEST + Op.JUMPI(pc=0x379, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x5b180229))) + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE) + Op.MSTORE(offset=0x300, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x4))) + Op.MSTORE(offset=0x320, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x24))) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x44)) + Op.POP + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x33f, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.MLOAD(offset=0x80)))) + Op.ADD(Op.DUP3, Op.SDIV(Op.MUL(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x300), Op.MUL(0x20, Op.DUP3))), Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x320), Op.MUL(0x20, Op.DUP2)))), 0x10000000000000000)) + Op.SWAP2 + Op.POP + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x306) + Op.JUMPDEST + Op.JUMPI(pc=0x366, condition=Op.ISZERO(Op.ISZERO(Op.EQ(Op.MLOAD(offset=Op.MLOAD(offset=0x320)), 0x0)))) + Op.SDIV(Op.MUL(Op.DUP4, 0x10000000000000000), Op.MLOAD(offset=Op.MLOAD(offset=0x320))) + Op.SWAP2 + Op.POP + Op.JUMP(pc=0x36b) + Op.JUMPDEST + Op.PUSH1[0x0] + Op.SWAP2 + Op.POP + Op.JUMPDEST + Op.MSTORE(offset=0x380, value=Op.DUP2) + Op.RETURN(offset=0x380, size=0x20) + Op.POP + Op.POP + Op.JUMPDEST + Op.JUMPI(pc=0x571, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xf4ca7dc4))) + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE) + Op.MSTORE(offset=0x3a0, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x4))) + Op.MSTORE(offset=0x3c0, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x24))) + Op.MSTORE(offset=0x1a0, value=Op.CALLDATALOAD(offset=0x44)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x64)) + Op.POP + Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x3c0), 0x20)) + Op.EXP(Op.MLOAD(offset=0x80), 0x2) + Op.ADD(0x20, Op.MUL(0x20, Op.DUP1)) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x44d, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.MLOAD(offset=0x80)))) + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x441, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.MLOAD(offset=0x80)))) + Op.MSTORE(offset=Op.ADD(Op.DUP5, Op.MUL(0x20, Op.ADD(Op.MUL(Op.DUP5, Op.MLOAD(offset=0x80)), Op.DUP2))), value=Op.ADD(Op.MLOAD(offset=Op.ADD(Op.DUP5, Op.MUL(0x20, Op.ADD(Op.MUL(Op.DUP5, Op.MLOAD(offset=0x80)), Op.DUP2)))), Op.SDIV(Op.MUL(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x3a0), Op.MUL(0x20, Op.DUP4))), Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x3a0), Op.MUL(0x20, Op.DUP2)))), 0x10000000000000000))) + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x3f1) + Op.JUMPDEST + Op.POP + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x3e4) + Op.JUMPDEST + Op.DUP2 + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.DUP2 + Op.ADD(0x20, Op.MUL(0x20, Op.DUP1)) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.MUL(Op.MLOAD(offset=0x1a0), Op.MLOAD(offset=0x80)) + Op.ADD(0x20, Op.MUL(0x20, Op.DUP1)) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x51e, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.MLOAD(offset=0x1a0)))) + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x512, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.MLOAD(offset=0x80)))) + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x506, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.MLOAD(offset=0x80)))) + Op.MSTORE(offset=Op.ADD(Op.DUP6, Op.MUL(0x20, Op.ADD(Op.MUL(Op.DUP6, Op.MLOAD(offset=0x80)), Op.DUP3))), value=Op.ADD(Op.MLOAD(offset=Op.ADD(Op.DUP6, Op.MUL(0x20, Op.ADD(Op.MUL(Op.DUP6, Op.MLOAD(offset=0x80)), Op.DUP3)))), Op.SDIV(Op.MUL(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x3c0), Op.MUL(0x20, Op.ADD(Op.MUL(Op.DUP7, Op.MLOAD(offset=0x80)), Op.DUP3)))), Op.MLOAD(offset=Op.ADD(Op.DUP8, Op.MUL(0x20, Op.ADD(Op.MUL(Op.DUP4, Op.MLOAD(offset=0x80)), Op.DUP3))))), 0x10000000000000000))) + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x4ad) + Op.JUMPDEST + Op.POP + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x4a0) + Op.JUMPDEST + Op.POP + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x492) + Op.JUMPDEST + Op.DUP2 + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x552, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.DUP5))) + Op.MSTORE(offset=Op.ADD(Op.DUP5, Op.MUL(0x20, Op.DUP2)), value=Op.SUB(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x3c0), Op.MUL(0x20, Op.DUP2))), Op.MLOAD(offset=Op.ADD(Op.DUP3, Op.MUL(0x20, Op.DUP1))))) + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x526) + Op.JUMPDEST + Op.POP + Op.DUP2 + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20) + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20))) + Op.POP + Op.POP + Op.POP + Op.POP + Op.POP + Op.JUMPDEST + Op.JUMPI(pc=0x69d, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x232b2734))) + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE) + Op.MSTORE(offset=0x620, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x4))) + Op.MSTORE(offset=0x280, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x24))) + Op.MSTORE(offset=0x3c0, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x44))) + Op.MSTORE(offset=0x640, value=Op.CALLDATALOAD(offset=0x64)) + Op.MSTORE(offset=0x1a0, value=Op.CALLDATALOAD(offset=0x84)) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0xa4)) + Op.POP + Op.JUMPI(pc=0x602, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=Op.MLOAD(offset=0x280)), 0x0))) + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x600, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.MLOAD(offset=0x80)))) + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x280), Op.MUL(0x20, Op.DUP2)), value=Op.SUB(0x0, Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x280), Op.MUL(0x20, Op.DUP1))))) + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x5d4) + Op.JUMPDEST + Op.POP + Op.JUMPDEST + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x67f, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.MLOAD(offset=0x1a0)))) + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x673, condition=Op.ISZERO(Op.SLT(Op.DUP2, Op.MLOAD(offset=0x80)))) + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x620), Op.MUL(0x20, Op.DUP3)), value=Op.ADD(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x620), Op.MUL(0x20, Op.DUP3))), Op.SDIV(Op.MUL(Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x3c0), Op.MUL(0x20, Op.ADD(Op.MUL(Op.DUP6, Op.MLOAD(offset=0x80)), Op.DUP3)))), Op.SDIV(Op.MUL(Op.MLOAD(offset=0x640), Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x280), Op.MUL(0x20, Op.DUP3)))), 0x10000000000000000)), 0x10000000000000000))) + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x613) + Op.JUMPDEST + Op.POP + Op.ADD(Op.DUP2, 0x1) + Op.SWAP1 + Op.POP + Op.JUMP(pc=0x605) + Op.JUMPDEST + Op.MLOAD(offset=0x620) + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20) + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20))) + Op.POP + Op.POP + Op.JUMPDEST + Op.POP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
