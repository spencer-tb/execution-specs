"""
Ported from:
tests/static/state_tests/stSpecialTest/tx_e1c174e2Filler.json
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
    ["tests/static/state_tests/stSpecialTest/tx_e1c174e2Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_tx_e1c174e2(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x68795c4aa09d6f4ed3e5deddf8c2ad3049a601da")
    sender = Address("0x57e3080b624809c72f75eae38de87b9d75c9a073")
    contract = Address("0xf47bacb0d8f13fa44d31623c3d5ae72907d241c1")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=3141592,
    )

    pre[sender] = Account(balance=0xde0b6b3a7640000, nonce=24)
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.MSTORE8(offset=0x155f, value=0x0)
        + Op.DIV(Op.CALLDATALOAD(offset=0x0), 0x100000000000000000000000000000000000000000000000000000000)
        + Op.JUMPI(pc=Op.PUSH2[0x65], condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x55f10aaf)))
        + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x4))
        + Op.JUMPI(pc=Op.PUSH2[0x52], condition=Op.ISZERO(Op.SGT(Op.CALLVALUE, 0x0)))
        + Op.POP(Op.CALL(gas=0x1388, address=Op.CALLER, value=Op.CALLVALUE, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.JUMPDEST
        + Op.MSTORE(offset=0x60, value=Op.SLOAD(key=Op.ADD(0x7, Op.MUL(Op.MLOAD(offset=0x40), 0xc))))
        + Op.RETURN(offset=0x60, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x53f, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x69e0998b)))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0xa0, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x44))
        + Op.JUMPI(pc=Op.PUSH2[0x9a], condition=Op.ISZERO(Op.ISZERO(Op.SGT(Op.MLOAD(offset=0x80), 0x0))))
        + Op.MSTORE(offset=0xc0, value=0x2) + Op.RETURN(offset=0xc0, size=0x20)
        + Op.JUMPDEST
        + Op.JUMPI(pc=Op.PUSH2[0xb1], condition=Op.ISZERO(Op.ISZERO(Op.SGT(Op.MLOAD(offset=0xa0), 0x0))))
        + Op.MSTORE(offset=0xe0, value=0x3) + Op.RETURN(offset=0xe0, size=0x20)
        + Op.JUMPDEST
        + Op.JUMPI(pc=Op.PUSH2[0xca], condition=Op.ISZERO(Op.ISZERO(Op.SGT(Op.MLOAD(offset=0x40), 0x0))))
        + Op.MSTORE(offset=0x100, value=0x4) + Op.RETURN(offset=0x100, size=0x20)
        + Op.JUMPDEST
        + Op.MSTORE(offset=0x120, value=Op.MUL(Op.SDIV(Op.MUL(Op.MLOAD(offset=0x80), Op.MLOAD(offset=0xa0)), Op.MUL(Op.SLOAD(key=Op.ADD(0x4, Op.MUL(Op.MLOAD(offset=0x40), 0xc))), Op.EXP(0xa, Op.SLOAD(key=Op.ADD(0x3, Op.MUL(Op.MLOAD(offset=0x40), 0xc)))))), 0xde0b6b3a7640000))
        + Op.JUMPI(pc=0x12f, condition=Op.ISZERO(Op.SLT(Op.CALLVALUE, Op.SLOAD(key=Op.ADD(0x5, Op.MUL(Op.MLOAD(offset=0x40), 0xc))))))
        + Op.JUMPI(pc=0x122, condition=Op.ISZERO(Op.SGT(Op.CALLVALUE, 0x0)))
        + Op.POP(Op.CALL(gas=0x1388, address=Op.CALLER, value=Op.CALLVALUE, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.JUMPDEST + Op.MSTORE(offset=0x140, value=0xb)
        + Op.RETURN(offset=0x140, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x160, condition=Op.ISZERO(Op.SLT(Op.CALLVALUE, Op.MLOAD(offset=0x120))))
        + Op.JUMPI(pc=0x153, condition=Op.ISZERO(Op.SGT(Op.CALLVALUE, 0x0)))
        + Op.POP(Op.CALL(gas=0x1388, address=Op.CALLER, value=Op.CALLVALUE, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.JUMPDEST + Op.MSTORE(offset=0x160, value=0x14)
        + Op.RETURN(offset=0x160, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x180, condition=Op.ISZERO(Op.SGT(Op.CALLVALUE, Op.MLOAD(offset=0x120))))
        + Op.POP(Op.CALL(gas=0x1388, address=Op.CALLER, value=Op.SUB(Op.CALLVALUE, Op.MLOAD(offset=0x120)), args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.JUMPDEST + Op.PUSH1[0xe0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x6)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x20), value=0x1)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x40), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x60), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x80), value=Op.MLOAD(offset=0xa0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0xa0), value=Op.CALLER)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0xc0), value=Op.NUMBER)
        + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.PUSH2[0x180] + Op.MSTORE
        + Op.MLOAD(offset=0x180)
        + Op.SHA3(offset=Op.DUP2, size=Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20))
        + Op.SWAP1 + Op.POP + Op.PUSH2[0x1c0] + Op.MSTORE
        + Op.JUMPI(pc=0x4be, condition=Op.ISZERO(Op.ISZERO(Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000000, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8))))))
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000000, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=Op.MLOAD(offset=0x1c0))
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000001, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x1)
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000002, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=Op.MLOAD(offset=0x40))
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000003, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=Op.MLOAD(offset=0x80))
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000004, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=Op.MLOAD(offset=0xa0))
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000005, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=Op.CALLER)
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000006, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=Op.NUMBER)
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000007, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=Op.ADD(0xe0000000000000000000000000000000000000000, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)))
        + Op.MSTORE(offset=0x200, value=Op.SLOAD(key=Op.ADD(0xb, Op.MUL(Op.MLOAD(offset=0x40), 0xc))))
        + Op.MLOAD(offset=0x1c0) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x200))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.MLOAD(offset=0x200) + Op.PUSH1[0xa0]
        + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x2) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.MLOAD(offset=0x1c0) + Op.PUSH1[0xa0]
        + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE
        + Op.SSTORE(key=Op.ADD(0xb, Op.MUL(Op.MLOAD(offset=0x40), 0xc)), value=Op.MLOAD(offset=0x1c0))
        + Op.SSTORE(key=Op.ADD(0xa, Op.MUL(Op.MLOAD(offset=0x40), 0xc)), value=Op.ADD(Op.SLOAD(key=Op.ADD(0xa, Op.MUL(Op.MLOAD(offset=0x40), 0xc))), 0x1))
        + Op.JUMPI(pc=0x4b9, condition=Op.ISZERO(Op.EQ(0x1, 0x2)))
        + Op.MLOAD(offset=0x80) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x4)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER)
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.SUB + Op.PUSH1[0x80] + Op.PUSH1[0x80]
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER)
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.MLOAD(offset=0x80) + Op.PUSH1[0x80]
        + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER)
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.ADD + Op.PUSH1[0x80] + Op.PUSH1[0x80]
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER)
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.JUMPDEST + Op.JUMP(pc=0x4cb) + Op.JUMPDEST
        + Op.MSTORE(offset=0x300, value=0x15) + Op.RETURN(offset=0x300, size=0x20)
        + Op.JUMPDEST + Op.PUSH1[0x1c] + Op.PUSH1[0xc0] + Op.MSIZE + Op.SWAP1
        + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.DUP2, value=Op.CALLER)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x20), value=0x1)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x40), value=Op.MLOAD(offset=0xa0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x60), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x80), value=Op.MLOAD(offset=0x1c0))
        + Op.LOG2(offset=Op.DUP4, size=0xa0, topic_1=0x9463d1cc4aa2db0dc624c996b1846f028d43c48cfc8b9f427f13336e4a732264, topic_2=Op.MLOAD(offset=0x40))
        + Op.POP + Op.MSTORE(offset=0x340, value=Op.MLOAD(offset=0x1c0))
        + Op.RETURN(offset=0x340, size=0x20) + Op.MSTORE(offset=0x360, value=0x0)
        + Op.RETURN(offset=0x360, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0xa0c, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x909f073)))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0xa0, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x44))
        + Op.JUMPI(pc=0x576, condition=Op.ISZERO(Op.ISZERO(Op.SGT(Op.MLOAD(offset=0x80), 0x0))))
        + Op.MSTORE(offset=0x380, value=0x2) + Op.RETURN(offset=0x380, size=0x20)
        + Op.JUMPDEST
        + Op.JUMPI(pc=0x58f, condition=Op.ISZERO(Op.ISZERO(Op.SGT(Op.MLOAD(offset=0xa0), 0x0))))
        + Op.MSTORE(offset=0x3a0, value=0x3) + Op.RETURN(offset=0x3a0, size=0x20)
        + Op.JUMPDEST
        + Op.JUMPI(pc=0x5a8, condition=Op.ISZERO(Op.ISZERO(Op.SGT(Op.MLOAD(offset=0x40), 0x0))))
        + Op.MSTORE(offset=0x3c0, value=0x4) + Op.RETURN(offset=0x3c0, size=0x20)
        + Op.JUMPDEST
        + Op.MSTORE(offset=0x120, value=Op.MUL(Op.SDIV(Op.MUL(Op.MLOAD(offset=0x80), Op.MLOAD(offset=0xa0)), Op.MUL(Op.SLOAD(key=Op.ADD(0x4, Op.MUL(Op.MLOAD(offset=0x40), 0xc))), Op.EXP(0xa, Op.SLOAD(key=Op.ADD(0x3, Op.MUL(Op.MLOAD(offset=0x40), 0xc)))))), 0xde0b6b3a7640000))
        + Op.JUMPI(pc=0x610, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x120), Op.SLOAD(key=Op.ADD(0x5, Op.MUL(Op.MLOAD(offset=0x40), 0xc))))))
        + Op.JUMPI(pc=0x603, condition=Op.ISZERO(Op.SGT(Op.CALLVALUE, 0x0)))
        + Op.POP(Op.CALL(gas=0x1388, address=Op.CALLER, value=Op.CALLVALUE, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.JUMPDEST + Op.MSTORE(offset=0x3e0, value=0xb)
        + Op.RETURN(offset=0x3e0, size=0x20) + Op.JUMPDEST + Op.PUSH1[0x80]
        + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER)
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MSTORE(offset=0x400, value=Op.SLOAD(key=Op.SHA3))
        + Op.JUMPI(pc=0x9ff, condition=Op.ISZERO(Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x400), Op.MLOAD(offset=0x80)))))
        + Op.PUSH1[0xe0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x6)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x20), value=0x2)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x40), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x60), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x80), value=Op.MLOAD(offset=0xa0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0xa0), value=Op.CALLER)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0xc0), value=Op.NUMBER)
        + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.PUSH2[0x180] + Op.MSTORE
        + Op.MLOAD(offset=0x180)
        + Op.SHA3(offset=Op.DUP2, size=Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20))
        + Op.SWAP1 + Op.POP + Op.PUSH2[0x1c0] + Op.MSTORE
        + Op.JUMPI(pc=0x98a, condition=Op.ISZERO(Op.ISZERO(Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000000, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8))))))
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000000, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=Op.MLOAD(offset=0x1c0))
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000001, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x2)
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000002, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=Op.MLOAD(offset=0x40))
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000003, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=Op.MLOAD(offset=0x80))
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000004, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=Op.MLOAD(offset=0xa0))
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000005, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=Op.CALLER)
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000006, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=Op.NUMBER)
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000007, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=Op.ADD(0xe0000000000000000000000000000000000000000, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)))
        + Op.MSTORE(offset=0x200, value=Op.SLOAD(key=Op.ADD(0xb, Op.MUL(Op.MLOAD(offset=0x40), 0xc))))
        + Op.MLOAD(offset=0x1c0) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x200))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.MLOAD(offset=0x200) + Op.PUSH1[0xa0]
        + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x2) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.MLOAD(offset=0x1c0) + Op.PUSH1[0xa0]
        + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE
        + Op.SSTORE(key=Op.ADD(0xb, Op.MUL(Op.MLOAD(offset=0x40), 0xc)), value=Op.MLOAD(offset=0x1c0))
        + Op.SSTORE(key=Op.ADD(0xa, Op.MUL(Op.MLOAD(offset=0x40), 0xc)), value=Op.ADD(Op.SLOAD(key=Op.ADD(0xa, Op.MUL(Op.MLOAD(offset=0x40), 0xc))), 0x1))
        + Op.JUMPI(pc=0x985, condition=Op.ISZERO(Op.EQ(0x2, 0x2)))
        + Op.MLOAD(offset=0x80) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x4)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER)
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.SUB + Op.PUSH1[0x80] + Op.PUSH1[0x80]
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER)
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.MLOAD(offset=0x80) + Op.PUSH1[0x80]
        + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER)
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.ADD + Op.PUSH1[0x80] + Op.PUSH1[0x80]
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER)
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.JUMPDEST + Op.JUMP(pc=0x997) + Op.JUMPDEST
        + Op.MSTORE(offset=0x560, value=0x15) + Op.RETURN(offset=0x560, size=0x20)
        + Op.JUMPDEST + Op.PUSH1[0x1c] + Op.PUSH1[0xc0] + Op.MSIZE + Op.SWAP1
        + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.DUP2, value=Op.CALLER)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x20), value=0x2)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x40), value=Op.MLOAD(offset=0xa0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x60), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x80), value=Op.MLOAD(offset=0x1c0))
        + Op.LOG2(offset=Op.DUP4, size=0xa0, topic_1=0x9463d1cc4aa2db0dc624c996b1846f028d43c48cfc8b9f427f13336e4a732264, topic_2=Op.MLOAD(offset=0x40))
        + Op.POP + Op.MSTORE(offset=0x580, value=Op.MLOAD(offset=0x1c0))
        + Op.RETURN(offset=0x580, size=0x20) + Op.JUMPDEST
        + Op.MSTORE(offset=0x5a0, value=0x0) + Op.RETURN(offset=0x5a0, size=0x20)
        + Op.JUMPDEST
        + Op.JUMPI(pc=0x1733, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x9998bd00)))
        + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE
        + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE)
        + Op.MSTORE(offset=0x5e0, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x600, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x24)))
        + Op.POP + Op.MSTORE(offset=0x620, value=Op.CALLVALUE)
        + Op.MSTORE(offset=0x640, value=0x0) + Op.JUMPDEST
        + Op.JUMPI(pc=0x170a, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x640), Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x600), 0x20)))))
        + Op.MSTORE(offset=0x1c0, value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x600), Op.MUL(0x20, Op.MLOAD(offset=0x640)))))
        + Op.JUMPI(pc=0xa9d, condition=Op.ISZERO(Op.ISZERO(Op.SGT(Op.NUMBER, Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000006, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)))))))
        + Op.MSTORE(offset=0x660, value=0x16) + Op.RETURN(offset=0x660, size=0x20)
        + Op.JUMPDEST
        + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000002, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8))))
        + Op.MSTORE(offset=0x680, value=Op.SLOAD(key=Op.ADD(0x2, Op.MUL(Op.MLOAD(offset=0x40), 0xc))))
        + Op.MSTORE(offset=0x6a0, value=Op.SLOAD(key=Op.ADD(0x3, Op.MUL(Op.MLOAD(offset=0x40), 0xc))))
        + Op.MSTORE(offset=0x6c0, value=Op.SLOAD(key=Op.ADD(0x4, Op.MUL(Op.MLOAD(offset=0x40), 0xc))))
        + Op.MSTORE(offset=0x6e0, value=Op.SLOAD(key=Op.ADD(0x5, Op.MUL(Op.MLOAD(offset=0x40), 0xc))))
        + Op.MSTORE(offset=0x700, value=Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000001, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8))))
        + Op.MSTORE(offset=0x80, value=Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000003, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8))))
        + Op.MSTORE(offset=0xa0, value=Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000004, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8))))
        + Op.MSTORE(offset=0x720, value=Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000005, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8))))
        + Op.JUMPI(pc=0x110e, condition=Op.ISZERO(Op.EQ(Op.MLOAD(offset=0x700), 0x1)))
        + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER)
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MSTORE(offset=0x400, value=Op.SLOAD(key=Op.SHA3))
        + Op.JUMPI(pc=0x10fc, condition=Op.ISZERO(Op.SGT(Op.MLOAD(offset=0x400), 0x0)))
        + Op.MLOAD(offset=0x80) + Op.MLOAD(offset=0x400) + Op.MLOAD(offset=0x5e0)
        + Op.JUMPI(pc=0xbe0, condition=Op.ISZERO(Op.SLT(Op.DUP3, Op.DUP1))) + Op.DUP2
        + Op.JUMP(pc=0xbe2) + Op.JUMPDEST + Op.DUP1 + Op.JUMPDEST + Op.SWAP1 + Op.POP
        + Op.SWAP1 + Op.POP
        + Op.JUMPI(pc=0xbf4, condition=Op.ISZERO(Op.SLT(Op.DUP3, Op.DUP1))) + Op.DUP2
        + Op.JUMP(pc=0xbf6) + Op.JUMPDEST + Op.DUP1 + Op.JUMPDEST + Op.SWAP1 + Op.POP
        + Op.SWAP1 + Op.POP + Op.PUSH2[0x760] + Op.MSTORE
        + Op.MSTORE(offset=0x120, value=Op.SDIV(Op.MUL(Op.MUL(Op.MLOAD(offset=0x760), Op.MLOAD(offset=0xa0)), 0xde0b6b3a7640000), Op.MUL(Op.MLOAD(offset=0x6c0), Op.EXP(0xa, Op.MLOAD(offset=0x6a0)))))
        + Op.JUMPI(pc=0xc5b, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x120), Op.MLOAD(offset=0x6e0))))
        + Op.JUMPI(pc=0xc4e, condition=Op.ISZERO(Op.SGT(Op.MLOAD(offset=0x620), 0x0)))
        + Op.POP(Op.CALL(gas=0x1388, address=Op.CALLER, value=Op.MLOAD(offset=0x620), args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.JUMPDEST + Op.MSTORE(offset=0x800, value=0xc)
        + Op.RETURN(offset=0x800, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0xcb0, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x760), Op.MLOAD(offset=0x80))))
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000003, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=Op.SUB(Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000003, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8))), Op.MLOAD(offset=0x760)))
        + Op.JUMP(pc=0xfd4) + Op.JUMPDEST
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000000, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0)
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000001, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0)
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000002, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0)
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000003, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0)
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000004, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0)
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000005, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0)
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000006, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0)
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000007, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0)
        + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x2) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MSTORE(offset=0x820, value=Op.SLOAD(key=Op.SHA3))
        + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MSTORE(offset=0x860, value=Op.SLOAD(key=Op.SHA3))
        + Op.JUMPI(pc=0xe3a, condition=Op.ISZERO(Op.MLOAD(offset=0x820)))
        + Op.MLOAD(offset=0x860) + Op.JUMP(pc=0xe3d) + Op.JUMPDEST + Op.PUSH1[0x0]
        + Op.JUMPDEST + Op.JUMPI(pc=0xeb7, condition=Op.ISZERO)
        + Op.MLOAD(offset=0x860) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x820))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.MLOAD(offset=0x820) + Op.PUSH1[0xa0]
        + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x860))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x2) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.JUMP(pc=0xf06) + Op.JUMPDEST
        + Op.JUMPI(pc=0xf05, condition=Op.ISZERO(Op.MLOAD(offset=0x820)))
        + Op.SSTORE(key=Op.ADD(0xb, Op.MUL(Op.MLOAD(offset=0x40), 0xc)), value=Op.MLOAD(offset=0x820))
        + Op.PUSH1[0x0] + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1
        + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x820))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.JUMPDEST + Op.JUMPDEST
        + Op.JUMPI(pc=0xf46, condition=Op.ISZERO(Op.MLOAD(offset=0x860)))
        + Op.PUSH1[0x0] + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1
        + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.JUMPDEST
        + Op.JUMPI(pc=0xf86, condition=Op.ISZERO(Op.MLOAD(offset=0x820)))
        + Op.PUSH1[0x0] + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1
        + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x2) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.JUMPDEST + Op.PUSH1[0x0] + Op.PUSH1[0xa0]
        + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE
        + Op.SSTORE(key=Op.ADD(0xa, Op.MUL(Op.MLOAD(offset=0x40), 0xc)), value=Op.SUB(Op.SLOAD(key=Op.ADD(0xa, Op.MUL(Op.MLOAD(offset=0x40), 0xc))), 0x1))
        + Op.JUMPDEST + Op.MLOAD(offset=0x760) + Op.PUSH1[0x80] + Op.PUSH1[0x80]
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER)
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.SUB + Op.PUSH1[0x80] + Op.PUSH1[0x80]
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER)
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.MLOAD(offset=0x760) + Op.PUSH1[0x80]
        + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x720))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.ADD + Op.PUSH1[0x80] + Op.PUSH1[0x80]
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x720))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE
        + Op.POP(Op.CALL(gas=0x1388, address=Op.CALLER, value=Op.MLOAD(offset=0x120), args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.PUSH1[0x1c] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.DUP2, value=0x2)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x20), value=Op.MLOAD(offset=0xa0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x40), value=Op.MLOAD(offset=0x760))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x60), value=Op.MLOAD(offset=0x1c0))
        + Op.LOG4(offset=Op.DUP6, size=0x80, topic_1=0xf9fe89f83633cc2eca9b17e1f77422f037cb026eaca4e6a5337fa1595f50a81, topic_2=Op.MLOAD(offset=0x40), topic_3=Op.CALLER, topic_4=Op.MLOAD(offset=0x720))
        + Op.POP + Op.JUMP(pc=0x1109) + Op.JUMPDEST
        + Op.MSTORE(offset=0x9e0, value=0xa) + Op.RETURN(offset=0x9e0, size=0x20)
        + Op.JUMPDEST + Op.JUMP(pc=0x1680) + Op.JUMPDEST
        + Op.JUMPI(pc=0x167f, condition=Op.ISZERO(Op.EQ(Op.MLOAD(offset=0x700), 0x2)))
        + Op.JUMPI(pc=0x1671, condition=Op.ISZERO(Op.SGT(Op.MLOAD(offset=0x620), 0x0)))
        + Op.JUMPI(pc=0x1160, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x620), Op.MLOAD(offset=0x6e0))))
        + Op.JUMPI(pc=0x1153, condition=Op.ISZERO(Op.SGT(Op.MLOAD(offset=0x620), 0x0)))
        + Op.POP(Op.CALL(gas=0x1388, address=Op.CALLER, value=Op.MLOAD(offset=0x620), args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.JUMPDEST + Op.MSTORE(offset=0xa00, value=0xc)
        + Op.RETURN(offset=0xa00, size=0x20) + Op.JUMPDEST
        + Op.MSTORE(offset=0xa20, value=Op.SDIV(Op.MUL(Op.MUL(Op.MLOAD(offset=0x80), Op.MLOAD(offset=0xa0)), 0xde0b6b3a7640000), Op.MUL(Op.MLOAD(offset=0x6c0), Op.EXP(0xa, Op.MLOAD(offset=0x6a0)))))
        + Op.MLOAD(offset=0x620) + Op.MLOAD(offset=0xa20)
        + Op.JUMPI(pc=0x1198, condition=Op.ISZERO(Op.SLT(Op.DUP3, Op.DUP1))) + Op.DUP2
        + Op.JUMP(pc=0x119a) + Op.JUMPDEST + Op.DUP1 + Op.JUMPDEST + Op.SWAP1 + Op.POP
        + Op.SWAP1 + Op.POP + Op.PUSH2[0x120] + Op.MSTORE
        + Op.JUMPI(pc=0x121b, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x120), Op.MLOAD(offset=0xa20))))
        + Op.MSTORE(offset=0x760, value=Op.SDIV(Op.SDIV(Op.MUL(Op.MLOAD(offset=0x120), Op.MUL(Op.MLOAD(offset=0x6c0), Op.EXP(0xa, Op.MLOAD(offset=0x6a0)))), Op.MLOAD(offset=0xa0)), 0xde0b6b3a7640000))
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000003, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=Op.SUB(Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000003, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8))), Op.MLOAD(offset=0x760)))
        + Op.JUMP(pc=0x1546) + Op.JUMPDEST
        + Op.MSTORE(offset=0x760, value=Op.MLOAD(offset=0x80))
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000000, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0)
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000001, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0)
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000002, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0)
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000003, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0)
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000004, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0)
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000005, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0)
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000006, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0)
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000007, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0)
        + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x2) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MSTORE(offset=0x820, value=Op.SLOAD(key=Op.SHA3))
        + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MSTORE(offset=0x860, value=Op.SLOAD(key=Op.SHA3))
        + Op.JUMPI(pc=0x13ac, condition=Op.ISZERO(Op.MLOAD(offset=0x820)))
        + Op.MLOAD(offset=0x860) + Op.JUMP(pc=0x13af) + Op.JUMPDEST + Op.PUSH1[0x0]
        + Op.JUMPDEST + Op.JUMPI(pc=0x1429, condition=Op.ISZERO)
        + Op.MLOAD(offset=0x860) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x820))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.MLOAD(offset=0x820) + Op.PUSH1[0xa0]
        + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x860))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x2) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.JUMP(pc=0x1478) + Op.JUMPDEST
        + Op.JUMPI(pc=0x1477, condition=Op.ISZERO(Op.MLOAD(offset=0x820)))
        + Op.SSTORE(key=Op.ADD(0xb, Op.MUL(Op.MLOAD(offset=0x40), 0xc)), value=Op.MLOAD(offset=0x820))
        + Op.PUSH1[0x0] + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1
        + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x820))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.JUMPDEST + Op.JUMPDEST
        + Op.JUMPI(pc=0x14b8, condition=Op.ISZERO(Op.MLOAD(offset=0x860)))
        + Op.PUSH1[0x0] + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1
        + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.JUMPDEST
        + Op.JUMPI(pc=0x14f8, condition=Op.ISZERO(Op.MLOAD(offset=0x820)))
        + Op.PUSH1[0x0] + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1
        + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x2) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.JUMPDEST + Op.PUSH1[0x0] + Op.PUSH1[0xa0]
        + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE
        + Op.SSTORE(key=Op.ADD(0xa, Op.MUL(Op.MLOAD(offset=0x40), 0xc)), value=Op.SUB(Op.SLOAD(key=Op.ADD(0xa, Op.MUL(Op.MLOAD(offset=0x40), 0xc))), 0x1))
        + Op.JUMPDEST + Op.MLOAD(offset=0x760) + Op.PUSH1[0x80] + Op.PUSH1[0x80]
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x720))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.SUB + Op.PUSH1[0x80] + Op.PUSH1[0x80]
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x720))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.MLOAD(offset=0x760) + Op.PUSH1[0x80]
        + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER)
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.ADD + Op.PUSH1[0x80] + Op.PUSH1[0x80]
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER)
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE
        + Op.POP(Op.CALL(gas=0x1388, address=Op.MLOAD(offset=0x720), value=Op.MLOAD(offset=0x120), args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.PUSH1[0x1c] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.DUP2, value=0x1)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x20), value=Op.MLOAD(offset=0xa0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x40), value=Op.MLOAD(offset=0x760))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x60), value=Op.MLOAD(offset=0x1c0))
        + Op.LOG4(offset=Op.DUP6, size=0x80, topic_1=0xf9fe89f83633cc2eca9b17e1f77422f037cb026eaca4e6a5337fa1595f50a81, topic_2=Op.MLOAD(offset=0x40), topic_3=Op.CALLER, topic_4=Op.MLOAD(offset=0x720))
        + Op.POP + Op.JUMP(pc=0x167e) + Op.JUMPDEST
        + Op.MSTORE(offset=0xc00, value=0xa) + Op.RETURN(offset=0xc00, size=0x20)
        + Op.JUMPDEST + Op.JUMPDEST + Op.JUMPDEST
        + Op.SSTORE(key=Op.ADD(0x7, Op.MUL(Op.MLOAD(offset=0x40), 0xc)), value=Op.MLOAD(offset=0xa0))
        + Op.PUSH1[0x1c] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.DUP2, value=Op.MLOAD(offset=0x700))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x20), value=Op.MLOAD(offset=0xa0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x40), value=Op.MLOAD(offset=0x760))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x60), value=Op.TIMESTAMP)
        + Op.LOG2(offset=Op.DUP4, size=0x80, topic_1=0x50944f09ce56f9f0e2cb67683c9b451049c39f60452b850b169148f3daa51ed6, topic_2=Op.MLOAD(offset=0x40))
        + Op.POP
        + Op.MSTORE(offset=0x5e0, value=Op.SUB(Op.MLOAD(offset=0x5e0), Op.MLOAD(offset=0x760)))
        + Op.MSTORE(offset=0x620, value=Op.SUB(Op.MLOAD(offset=0x620), Op.MLOAD(offset=0x120)))
        + Op.MSTORE(offset=0x640, value=Op.ADD(Op.MLOAD(offset=0x640), 0x1))
        + Op.JUMP(pc=0xa46) + Op.JUMPDEST
        + Op.JUMPI(pc=0x1726, condition=Op.ISZERO(Op.MLOAD(offset=0x620)))
        + Op.POP(Op.CALL(gas=0x1388, address=Op.CALLER, value=Op.MLOAD(offset=0x620), args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.JUMPDEST + Op.MSTORE(offset=0xc20, value=0x1)
        + Op.RETURN(offset=0xc20, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x185b, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x34a501c7)))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0x1c]
        + Op.PUSH1[0x84] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x27f08b00)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.CALLER)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.ADDRESS)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=Op.MLOAD(offset=0x80))
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.SLOAD(key=Op.ADD(0x2, Op.MUL(Op.MLOAD(offset=0x40), 0xc))), value=0x0, args_offset=Op.DUP4, args_size=0x64, ret_offset=0xc40, ret_size=0x20))
        + Op.MLOAD(offset=0xc40) + Op.SWAP1 + Op.POP
        + Op.JUMPI(pc=0x184e, condition=Op.ISZERO) + Op.PUSH1[0x80] + Op.PUSH1[0x80]
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER)
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MSTORE(offset=0x400, value=Op.SLOAD(key=Op.SHA3))
        + Op.MSTORE(offset=0xc80, value=Op.ADD(Op.MLOAD(offset=0x400), Op.MLOAD(offset=0x80)))
        + Op.MLOAD(offset=0xc80) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x4)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER)
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.PUSH1[0x1c] + Op.PUSH1[0x40] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.DUP2, value=Op.MLOAD(offset=0x80))
        + Op.LOG3(offset=Op.DUP5, size=0x20, topic_1=0x301cd746dbb5e7f9ade2bcd9e8a849b968bfcc222de48d2086ba200184acc83d, topic_2=Op.MLOAD(offset=0x40), topic_3=Op.CALLER)
        + Op.POP + Op.MSTORE(offset=0xcc0, value=Op.MLOAD(offset=0xc80))
        + Op.RETURN(offset=0xcc0, size=0x20) + Op.JUMPDEST
        + Op.MSTORE(offset=0xce0, value=0x0) + Op.RETURN(offset=0xce0, size=0x20)
        + Op.JUMPDEST
        + Op.JUMPI(pc=0x1982, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xe1ed3ad3)))
        + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0x80]
        + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER)
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MSTORE(offset=0x400, value=Op.SLOAD(key=Op.SHA3))
        + Op.JUMPI(pc=0x1975, condition=Op.ISZERO(Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x400), Op.MLOAD(offset=0x80)))))
        + Op.SUB(Op.MLOAD(offset=0x400), Op.MLOAD(offset=0x80)) + Op.PUSH1[0x80]
        + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER)
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x86744558)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.CALLER)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0x80))
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.SLOAD(key=Op.ADD(0x2, Op.MUL(Op.MLOAD(offset=0x40), 0xc))), value=0x0, args_offset=Op.DUP4, args_size=0x44, ret_offset=0xd60, ret_size=0x20))
        + Op.MLOAD(offset=0xd60) + Op.SWAP1 + Op.POP + Op.PUSH2[0xd40] + Op.MSTORE
        + Op.PUSH1[0x1c] + Op.PUSH1[0x40] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.DUP2, value=Op.MLOAD(offset=0x80))
        + Op.LOG3(offset=Op.DUP5, size=0x20, topic_1=0xfa4460934f383b326d79dcd4f1e59a17ac8ee9a87312169933e7f68b85c1a8ce, topic_2=Op.MLOAD(offset=0x40), topic_3=Op.CALLER)
        + Op.POP + Op.MSTORE(offset=0xd80, value=Op.MLOAD(offset=0xd40))
        + Op.RETURN(offset=0xd80, size=0x20) + Op.JUMPDEST
        + Op.MSTORE(offset=0xda0, value=0x0) + Op.RETURN(offset=0xda0, size=0x20)
        + Op.JUMPDEST
        + Op.JUMPI(pc=0x1f08, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x327a22f1)))
        + Op.MSTORE(offset=0x1c0, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x700, value=Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000001, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8))))
        + Op.MSTORE(offset=0x80, value=Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000003, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8))))
        + Op.MSTORE(offset=0xa0, value=Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000004, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8))))
        + Op.MSTORE(offset=0x720, value=Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000005, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8))))
        + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000002, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8))))
        + Op.MSTORE(offset=0x680, value=Op.SLOAD(key=Op.ADD(0x2, Op.MUL(Op.MLOAD(offset=0x40), 0xc))))
        + Op.MSTORE(offset=0x6a0, value=Op.SLOAD(key=Op.ADD(0x3, Op.MUL(Op.MLOAD(offset=0x40), 0xc))))
        + Op.MSTORE(offset=0x6c0, value=Op.SLOAD(key=Op.ADD(0x4, Op.MUL(Op.MLOAD(offset=0x40), 0xc))))
        + Op.JUMPI(pc=0x1efb, condition=Op.ISZERO(Op.EQ(Op.CALLER, Op.MLOAD(offset=0x720))))
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000000, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0)
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000001, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0)
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000002, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0)
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000003, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0)
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000004, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0)
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000005, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0)
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000006, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0)
        + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000007, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0)
        + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x2) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MSTORE(offset=0x820, value=Op.SLOAD(key=Op.SHA3))
        + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MSTORE(offset=0x860, value=Op.SLOAD(key=Op.SHA3))
        + Op.JUMPI(pc=0x1c00, condition=Op.ISZERO(Op.MLOAD(offset=0x820)))
        + Op.MLOAD(offset=0x860) + Op.JUMP(pc=0x1c03) + Op.JUMPDEST + Op.PUSH1[0x0]
        + Op.JUMPDEST + Op.JUMPI(pc=0x1c7d, condition=Op.ISZERO)
        + Op.MLOAD(offset=0x860) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x820))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.MLOAD(offset=0x820) + Op.PUSH1[0xa0]
        + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x860))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x2) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.JUMP(pc=0x1ccc) + Op.JUMPDEST
        + Op.JUMPI(pc=0x1ccb, condition=Op.ISZERO(Op.MLOAD(offset=0x820)))
        + Op.SSTORE(key=Op.ADD(0xb, Op.MUL(Op.MLOAD(offset=0x40), 0xc)), value=Op.MLOAD(offset=0x820))
        + Op.PUSH1[0x0] + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1
        + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x820))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.JUMPDEST + Op.JUMPDEST
        + Op.JUMPI(pc=0x1d0c, condition=Op.ISZERO(Op.MLOAD(offset=0x860)))
        + Op.PUSH1[0x0] + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1
        + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.JUMPDEST
        + Op.JUMPI(pc=0x1d4c, condition=Op.ISZERO(Op.MLOAD(offset=0x820)))
        + Op.PUSH1[0x0] + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1
        + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x2) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.JUMPDEST + Op.PUSH1[0x0] + Op.PUSH1[0xa0]
        + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE
        + Op.SSTORE(key=Op.ADD(0xa, Op.MUL(Op.MLOAD(offset=0x40), 0xc)), value=Op.SUB(Op.SLOAD(key=Op.ADD(0xa, Op.MUL(Op.MLOAD(offset=0x40), 0xc))), 0x1))
        + Op.JUMPI(pc=0x1dde, condition=Op.ISZERO(Op.EQ(Op.MLOAD(offset=0x700), 0x1)))
        + Op.MSTORE(offset=0x120, value=Op.MUL(Op.SDIV(Op.MUL(Op.MLOAD(offset=0x80), Op.MLOAD(offset=0xa0)), Op.MUL(Op.MLOAD(offset=0x6c0), Op.EXP(0xa, Op.MLOAD(offset=0x6a0)))), 0xde0b6b3a7640000))
        + Op.POP(Op.CALL(gas=0x1388, address=Op.CALLER, value=Op.MLOAD(offset=0x120), args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.JUMP(pc=0x1e9c) + Op.JUMPDEST
        + Op.JUMPI(pc=0x1e9b, condition=Op.ISZERO(Op.EQ(Op.MLOAD(offset=0x700), 0x2)))
        + Op.MLOAD(offset=0x80) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x4)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER)
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.SUB + Op.PUSH1[0x80] + Op.PUSH1[0x80]
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER)
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.MLOAD(offset=0x80) + Op.PUSH1[0x80]
        + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER)
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.ADD + Op.PUSH1[0x80] + Op.PUSH1[0x80]
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER)
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.SHA3 + Op.SSTORE + Op.JUMPDEST + Op.JUMPDEST + Op.PUSH1[0x1c]
        + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.DUP2, value=Op.CALLER)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x20), value=Op.MLOAD(offset=0xa0))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x40), value=Op.MLOAD(offset=0x80))
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x60), value=Op.MLOAD(offset=0x1c0))
        + Op.LOG2(offset=Op.DUP4, size=0x80, topic_1=0xac6333455d304288767a0f1039d666d16882d10b6ea83693d2556e4c8098001, topic_2=Op.MLOAD(offset=0x40))
        + Op.POP + Op.MSTORE(offset=0xf40, value=0x1)
        + Op.RETURN(offset=0xf40, size=0x20) + Op.JUMPDEST
        + Op.MSTORE(offset=0xf60, value=0x0) + Op.RETURN(offset=0xf60, size=0x20)
        + Op.JUMPDEST
        + Op.JUMPI(pc=0x22f0, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xd91e22f4)))
        + Op.MSTORE(offset=0xf80, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x680, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0x6a0, value=Op.CALLDATALOAD(offset=0x44))
        + Op.MSTORE(offset=0x6c0, value=Op.CALLDATALOAD(offset=0x64))
        + Op.MSTORE(offset=0x6e0, value=Op.CALLDATALOAD(offset=0x84))
        + Op.MSTORE(offset=0xfa0, value=Op.CALLDATALOAD(offset=0xa4))
        + Op.MSTORE(offset=0xfc0, value=Op.ADD(Op.SLOAD(key=0x160000000000000000000000000000000000000000), 0x1))
        + Op.JUMPI(pc=0x1f76, condition=Op.ISZERO(Op.ISZERO(Op.SGT(Op.MLOAD(offset=0xf80), 0x0))))
        + Op.MSTORE(offset=0xfe0, value=0x1e) + Op.RETURN(offset=0xfe0, size=0x20)
        + Op.JUMPDEST
        + Op.JUMPI(pc=0x1fa4, condition=Op.ISZERO(Op.SLOAD(key=Op.ADD(0xd0000000000000000000000000000000000000000, Op.MLOAD(offset=0xf80)))))
        + Op.MSTORE(offset=0x1000, value=0x1f) + Op.RETURN(offset=0x1000, size=0x20)
        + Op.JUMPDEST
        + Op.JUMPI(pc=0x1fbe, condition=Op.ISZERO(Op.ISZERO(Op.SGT(Op.MLOAD(offset=0x680), 0x0))))
        + Op.MSTORE(offset=0x1020, value=0x20) + Op.RETURN(offset=0x1020, size=0x20)
        + Op.JUMPDEST
        + Op.JUMPI(pc=0x1fd7, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=0xfa0), 0x0)))
        + Op.MSTORE(offset=0x1040, value=0x21) + Op.RETURN(offset=0x1040, size=0x20)
        + Op.JUMPDEST
        + Op.JUMPI(pc=0x1ff0, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x6a0), 0x0)))
        + Op.MSTORE(offset=0x1060, value=0x22) + Op.RETURN(offset=0x1060, size=0x20)
        + Op.JUMPDEST
        + Op.JUMPI(pc=0x2009, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x6c0), 0x0)))
        + Op.MSTORE(offset=0x1080, value=0x23) + Op.RETURN(offset=0x1080, size=0x20)
        + Op.JUMPDEST
        + Op.JUMPI(pc=0x2022, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x6e0), 0x0)))
        + Op.MSTORE(offset=0x10a0, value=0x24) + Op.RETURN(offset=0x10a0, size=0x20)
        + Op.JUMPDEST + Op.PUSH1[0x0] + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xc32d01a1)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.CALLER)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.ADDRESS)
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x680), value=0x0, args_offset=Op.DUP4, args_size=0x44, ret_offset=0x10c0, ret_size=0x20))
        + Op.MLOAD(offset=0x10c0) + Op.SWAP1 + Op.POP
        + Op.JUMPI(pc=0x2075, condition=Op.ISZERO(Op.ISZERO(Op.EQ)))
        + Op.MSTORE(offset=0x10e0, value=0x28) + Op.RETURN(offset=0x10e0, size=0x20)
        + Op.JUMPDEST + Op.PUSH1[0x1] + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x83b58638)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.ADDRESS)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=0x0)
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x680), value=0x0, args_offset=Op.DUP4, args_size=0x44, ret_offset=0x1100, ret_size=0x20))
        + Op.MLOAD(offset=0x1100) + Op.SWAP1 + Op.POP
        + Op.JUMPI(pc=0x20c9, condition=Op.ISZERO(Op.ISZERO(Op.EQ)))
        + Op.MSTORE(offset=0x1120, value=0x29) + Op.RETURN(offset=0x1120, size=0x20)
        + Op.JUMPDEST + Op.PUSH1[0x0] + Op.PUSH1[0x1c] + Op.PUSH1[0x44] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x26690247)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.ADDRESS)
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x680), value=0x0, args_offset=Op.DUP4, args_size=0x24, ret_offset=0x1140, ret_size=0x20))
        + Op.MLOAD(offset=0x1140) + Op.SWAP1 + Op.POP
        + Op.JUMPI(pc=0x2116, condition=Op.ISZERO(Op.ISZERO(Op.EQ)))
        + Op.MSTORE(offset=0x1160, value=0x2a) + Op.RETURN(offset=0x1160, size=0x20)
        + Op.JUMPDEST + Op.PUSH1[0x0] + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x86744558)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.CALLER)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=0x0)
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x680), value=0x0, args_offset=Op.DUP4, args_size=0x44, ret_offset=0x1180, ret_size=0x20))
        + Op.MLOAD(offset=0x1180) + Op.SWAP1 + Op.POP
        + Op.JUMPI(pc=0x216a, condition=Op.ISZERO(Op.ISZERO(Op.EQ)))
        + Op.MSTORE(offset=0x11a0, value=0x2b) + Op.RETURN(offset=0x11a0, size=0x20)
        + Op.JUMPDEST + Op.PUSH1[0x0] + Op.PUSH1[0x1c] + Op.PUSH1[0x84] + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x27f08b00)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.ADDRESS)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.CALLER)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=0x0)
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x680), value=0x0, args_offset=Op.DUP4, args_size=0x64, ret_offset=0x11c0, ret_size=0x20))
        + Op.MLOAD(offset=0x11c0) + Op.SWAP1 + Op.POP
        + Op.JUMPI(pc=0x21c4, condition=Op.ISZERO(Op.ISZERO(Op.EQ)))
        + Op.MSTORE(offset=0x11e0, value=0x2c) + Op.RETURN(offset=0x11e0, size=0x20)
        + Op.JUMPDEST
        + Op.SSTORE(key=Op.MUL(Op.MLOAD(offset=0xfc0), 0xc), value=Op.MLOAD(offset=0xfc0))
        + Op.SSTORE(key=Op.ADD(0x1, Op.MUL(Op.MLOAD(offset=0xfc0), 0xc)), value=Op.MLOAD(offset=0xf80))
        + Op.SSTORE(key=Op.ADD(0x2, Op.MUL(Op.MLOAD(offset=0xfc0), 0xc)), value=Op.MLOAD(offset=0x680))
        + Op.SSTORE(key=Op.ADD(0x6, Op.MUL(Op.MLOAD(offset=0xfc0), 0xc)), value=Op.MLOAD(offset=0xfa0))
        + Op.SSTORE(key=Op.ADD(0x3, Op.MUL(Op.MLOAD(offset=0xfc0), 0xc)), value=Op.MLOAD(offset=0x6a0))
        + Op.SSTORE(key=Op.ADD(0x4, Op.MUL(Op.MLOAD(offset=0xfc0), 0xc)), value=Op.MLOAD(offset=0x6c0))
        + Op.SSTORE(key=Op.ADD(0x5, Op.MUL(Op.MLOAD(offset=0xfc0), 0xc)), value=Op.MLOAD(offset=0x6e0))
        + Op.SSTORE(key=Op.ADD(0x7, Op.MUL(Op.MLOAD(offset=0xfc0), 0xc)), value=0x1)
        + Op.SSTORE(key=Op.ADD(0x8, Op.MUL(Op.MLOAD(offset=0xfc0), 0xc)), value=Op.CALLER)
        + Op.SSTORE(key=Op.ADD(0x9, Op.MUL(Op.MLOAD(offset=0xfc0), 0xc)), value=Op.NUMBER)
        + Op.SSTORE(key=Op.ADD(0xc0000000000000000000000000000000000000000, Op.MLOAD(offset=0x680)), value=Op.MLOAD(offset=0xfc0))
        + Op.SSTORE(key=Op.ADD(0xd0000000000000000000000000000000000000000, Op.MLOAD(offset=0xf80)), value=Op.MLOAD(offset=0xfc0))
        + Op.SSTORE(key=0x160000000000000000000000000000000000000000, value=Op.MLOAD(offset=0xfc0))
        + Op.PUSH1[0x1c] + Op.PUSH1[0x40] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD
        + Op.MSTORE(offset=Op.DUP2, value=Op.MLOAD(offset=0xfc0))
        + Op.LOG1(offset=Op.DUP3, size=0x20, topic_1=0x1238fe6d44cf796960d61b74766b3a383110e472d849f5ca16ae50215bc05e58)
        + Op.POP + Op.MSTORE(offset=0x1200, value=0x1)
        + Op.RETURN(offset=0x1200, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x232a, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x41569661)))
        + Op.MSTORE(offset=0x1220, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x1240, value=Op.SLOAD(key=Op.ADD(0xc0000000000000000000000000000000000000000, Op.MLOAD(offset=0x1220))))
        + Op.RETURN(offset=0x1240, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x2364, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xfcde9f78)))
        + Op.MSTORE(offset=0xf80, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x1260, value=Op.SLOAD(key=Op.ADD(0xd0000000000000000000000000000000000000000, Op.MLOAD(offset=0xf80))))
        + Op.RETURN(offset=0x1260, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x2392, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x6e5b4343)))
        + Op.MSTORE(offset=0x1280, value=Op.SLOAD(key=0x160000000000000000000000000000000000000000))
        + Op.RETURN(offset=0x1280, size=0x20) + Op.JUMPDEST
        + Op.JUMPI(pc=0x24e6, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xfafa69c2)))
        + Op.MSTORE(offset=0xfc0, value=Op.CALLDATALOAD(offset=0x4)) + Op.PUSH2[0x180]
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0xb) + Op.ADD(Op.DUP2, 0x20)
        + Op.SWAP1 + Op.POP + Op.PUSH2[0x12a0] + Op.MSTORE
        + Op.MSTORE(offset=Op.MLOAD(offset=0x12a0), value=Op.SLOAD(key=Op.MUL(Op.MLOAD(offset=0xfc0), 0xc)))
        + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x12a0), 0x20), value=Op.SLOAD(key=Op.ADD(0x1, Op.MUL(Op.MLOAD(offset=0xfc0), 0xc))))
        + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x12a0), 0x40), value=Op.SLOAD(key=Op.ADD(0x2, Op.MUL(Op.MLOAD(offset=0xfc0), 0xc))))
        + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x12a0), 0x60), value=Op.SLOAD(key=Op.ADD(0x3, Op.MUL(Op.MLOAD(offset=0xfc0), 0xc))))
        + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x12a0), 0x80), value=Op.SLOAD(key=Op.ADD(0x4, Op.MUL(Op.MLOAD(offset=0xfc0), 0xc))))
        + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x12a0), 0xa0), value=Op.SLOAD(key=Op.ADD(0x5, Op.MUL(Op.MLOAD(offset=0xfc0), 0xc))))
        + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x12a0), 0xc0), value=Op.SLOAD(key=Op.ADD(0x7, Op.MUL(Op.MLOAD(offset=0xfc0), 0xc))))
        + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x12a0), 0xe0), value=Op.SLOAD(key=Op.ADD(0x8, Op.MUL(Op.MLOAD(offset=0xfc0), 0xc))))
        + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x12a0), 0x100), value=Op.SLOAD(key=Op.ADD(0x9, Op.MUL(Op.MLOAD(offset=0xfc0), 0xc))))
        + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x12a0), 0x120), value=Op.SLOAD(key=Op.ADD(0xa, Op.MUL(Op.MLOAD(offset=0xfc0), 0xc))))
        + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x12a0), 0x140), value=Op.SLOAD(key=Op.ADD(0x6, Op.MUL(Op.MLOAD(offset=0xfc0), 0xc))))
        + Op.JUMPI(pc=0x24b2, condition=Op.ISZERO(Op.MLOAD(offset=0x12a0)))
        + Op.MLOAD(offset=0x12a0)
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20)
        + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20)))
        + Op.POP + Op.JUMPDEST + Op.PUSH1[0x40] + Op.MSIZE + Op.SWAP1 + Op.MSIZE
        + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x1)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x20), value=0x0) + Op.ADD(Op.DUP2, 0x20)
        + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20)
        + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20)))
        + Op.POP + Op.JUMPDEST
        + Op.JUMPI(pc=0x262e, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x9cfc1535)))
        + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x1340, value=Op.SLOAD(key=Op.ADD(0xa, Op.MUL(Op.MLOAD(offset=0x40), 0xc))))
        + Op.MSTORE(offset=0x1c0, value=Op.SLOAD(key=Op.ADD(0xb, Op.MUL(Op.MLOAD(offset=0x40), 0xc))))
        + Op.MLOAD(offset=0x1340) + Op.ADD(0x20, Op.MUL(0x20, Op.DUP1)) + Op.MSIZE
        + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1
        + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH2[0x600] + Op.MSTORE
        + Op.MSTORE(offset=0x13a0, value=0x0) + Op.JUMPDEST
        + Op.JUMPI(pc=0x25d4, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x13a0), Op.MLOAD(offset=0x1340))))
        + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP
        + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x600), Op.MUL(0x20, Op.MLOAD(offset=0x13a0))), value=Op.SLOAD(key=Op.SHA3))
        + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc)
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0))
        + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x2) + Op.DUP1 + Op.SWAP1
        + Op.POP + Op.MSTORE(offset=0x1c0, value=Op.SLOAD(key=Op.SHA3))
        + Op.MSTORE(offset=0x13a0, value=Op.ADD(Op.MLOAD(offset=0x13a0), 0x1))
        + Op.JUMP(pc=0x253d) + Op.JUMPDEST
        + Op.JUMPI(pc=0x25fa, condition=Op.ISZERO(Op.MLOAD(offset=0x600)))
        + Op.MLOAD(offset=0x600) + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20)
        + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20)))
        + Op.POP + Op.JUMPDEST + Op.PUSH1[0x40] + Op.MSIZE + Op.SWAP1 + Op.MSIZE
        + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x1)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x20), value=0x0) + Op.ADD(Op.DUP2, 0x20)
        + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20)
        + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20)))
        + Op.POP + Op.JUMPDEST
        + Op.JUMPI(pc=0x27e9, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xf718190)))
        + Op.MSTORE(offset=0xfc0, value=Op.CALLDATALOAD(offset=0x4)) + Op.PUSH2[0x120]
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x8) + Op.ADD(Op.DUP2, 0x20)
        + Op.SWAP1 + Op.POP + Op.PUSH2[0x180] + Op.MSTORE
        + Op.MSTORE(offset=Op.MLOAD(offset=0x180), value=Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000000, Op.MUL(Op.MLOAD(offset=0xfc0), 0x8))))
        + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x180), 0x20), value=Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000001, Op.MUL(Op.MLOAD(offset=0xfc0), 0x8))))
        + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x180), 0x40), value=Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000002, Op.MUL(Op.MLOAD(offset=0xfc0), 0x8))))
        + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x180), 0x60), value=Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000003, Op.MUL(Op.MLOAD(offset=0xfc0), 0x8))))
        + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x180), 0x80), value=Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000004, Op.MUL(Op.MLOAD(offset=0xfc0), 0x8))))
        + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x180), 0xa0), value=Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000005, Op.MUL(Op.MLOAD(offset=0xfc0), 0x8))))
        + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x180), 0xc0), value=Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000006, Op.MUL(Op.MLOAD(offset=0xfc0), 0x8))))
        + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x180), 0xe0), value=Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000007, Op.MUL(Op.MLOAD(offset=0xfc0), 0x8))))
        + Op.JUMPI(pc=0x27b5, condition=Op.ISZERO(Op.MLOAD(offset=0x180)))
        + Op.MLOAD(offset=0x180) + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20)
        + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20)))
        + Op.POP + Op.JUMPDEST + Op.PUSH1[0x40] + Op.MSIZE + Op.SWAP1 + Op.MSIZE
        + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE
        + Op.MSTORE(offset=Op.DUP2, value=0x1)
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x20), value=0x0) + Op.ADD(Op.DUP2, 0x20)
        + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20)
        + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20)))
        + Op.POP + Op.JUMPDEST
        + Op.JUMPI(pc=0x2893, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x1c9aa4b6)))
        + Op.MSTORE(offset=0x1220, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0x60]
        + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1
        + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x2) + Op.PUSH1[0x80]
        + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x1220))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1
        + Op.POP
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x20), value=Op.SLOAD(key=Op.SHA3))
        + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4)
        + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x1220))
        + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40))
        + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1
        + Op.POP
        + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x40), value=Op.SLOAD(key=Op.SHA3))
        + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20)
        + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20)))
        + Op.POP + Op.JUMPDEST + Op.POP
    ),
        storage={0xd0000000000000000000000000000000000505347: 0x0, 0x160000000000000000000000000000000000000000: 0x1},
    )

    tx = Transaction(
        secret_key=Hash(
            "0x98d5e7375843784f7eb2606a693bab39ebac533561559e372dc3017f30519535"
        ),
        to=contract,
        data=bytes.fromhex(
            "d91e22f40000000000000000000000000000000000000000000000000000000000505347"
            "000000000000000000000000000000000000000000000000000000002450534700000000"
            "000000000000000000000000000000000000000000000000000000010000000000000000"
            "000000000000000000000000000000000000000005f5e100000000000000000000000000"
            "000000000000000000000000002386f26fc1000000000000000000000000000000000000"
            "00000000000000000000000000000001"
        ),
        gas_limit=500000,
        gas_price=52637211012,
        nonce=24,
        value=0,
    )

    post = {
        contract: Account(
            storage={0x160000000000000000000000000000000000000000: 1},
            code=Op.MSTORE8(offset=0x155f, value=0x0) + Op.DIV(Op.CALLDATALOAD(offset=0x0), 0x100000000000000000000000000000000000000000000000000000000) + Op.JUMPI(pc=Op.PUSH2[0x65], condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x55f10aaf))) + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x4)) + Op.JUMPI(pc=Op.PUSH2[0x52], condition=Op.ISZERO(Op.SGT(Op.CALLVALUE, 0x0))) + Op.POP(Op.CALL(gas=0x1388, address=Op.CALLER, value=Op.CALLVALUE, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.JUMPDEST + Op.MSTORE(offset=0x60, value=Op.SLOAD(key=Op.ADD(0x7, Op.MUL(Op.MLOAD(offset=0x40), 0xc)))) + Op.RETURN(offset=0x60, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x53f, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x69e0998b))) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0xa0, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x44)) + Op.JUMPI(pc=Op.PUSH2[0x9a], condition=Op.ISZERO(Op.ISZERO(Op.SGT(Op.MLOAD(offset=0x80), 0x0)))) + Op.MSTORE(offset=0xc0, value=0x2) + Op.RETURN(offset=0xc0, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=Op.PUSH2[0xb1], condition=Op.ISZERO(Op.ISZERO(Op.SGT(Op.MLOAD(offset=0xa0), 0x0)))) + Op.MSTORE(offset=0xe0, value=0x3) + Op.RETURN(offset=0xe0, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=Op.PUSH2[0xca], condition=Op.ISZERO(Op.ISZERO(Op.SGT(Op.MLOAD(offset=0x40), 0x0)))) + Op.MSTORE(offset=0x100, value=0x4) + Op.RETURN(offset=0x100, size=0x20) + Op.JUMPDEST + Op.MSTORE(offset=0x120, value=Op.MUL(Op.SDIV(Op.MUL(Op.MLOAD(offset=0x80), Op.MLOAD(offset=0xa0)), Op.MUL(Op.SLOAD(key=Op.ADD(0x4, Op.MUL(Op.MLOAD(offset=0x40), 0xc))), Op.EXP(0xa, Op.SLOAD(key=Op.ADD(0x3, Op.MUL(Op.MLOAD(offset=0x40), 0xc)))))), 0xde0b6b3a7640000)) + Op.JUMPI(pc=0x12f, condition=Op.ISZERO(Op.SLT(Op.CALLVALUE, Op.SLOAD(key=Op.ADD(0x5, Op.MUL(Op.MLOAD(offset=0x40), 0xc)))))) + Op.JUMPI(pc=0x122, condition=Op.ISZERO(Op.SGT(Op.CALLVALUE, 0x0))) + Op.POP(Op.CALL(gas=0x1388, address=Op.CALLER, value=Op.CALLVALUE, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.JUMPDEST + Op.MSTORE(offset=0x140, value=0xb) + Op.RETURN(offset=0x140, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x160, condition=Op.ISZERO(Op.SLT(Op.CALLVALUE, Op.MLOAD(offset=0x120)))) + Op.JUMPI(pc=0x153, condition=Op.ISZERO(Op.SGT(Op.CALLVALUE, 0x0))) + Op.POP(Op.CALL(gas=0x1388, address=Op.CALLER, value=Op.CALLVALUE, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.JUMPDEST + Op.MSTORE(offset=0x160, value=0x14) + Op.RETURN(offset=0x160, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x180, condition=Op.ISZERO(Op.SGT(Op.CALLVALUE, Op.MLOAD(offset=0x120)))) + Op.POP(Op.CALL(gas=0x1388, address=Op.CALLER, value=Op.SUB(Op.CALLVALUE, Op.MLOAD(offset=0x120)), args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.JUMPDEST + Op.PUSH1[0xe0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x6) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x20), value=0x1) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x40), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x60), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x80), value=Op.MLOAD(offset=0xa0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0xa0), value=Op.CALLER) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0xc0), value=Op.NUMBER) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.PUSH2[0x180] + Op.MSTORE + Op.MLOAD(offset=0x180) + Op.SHA3(offset=Op.DUP2, size=Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20)) + Op.SWAP1 + Op.POP + Op.PUSH2[0x1c0] + Op.MSTORE + Op.JUMPI(pc=0x4be, condition=Op.ISZERO(Op.ISZERO(Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000000, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)))))) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000000, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=Op.MLOAD(offset=0x1c0)) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000001, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x1) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000002, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=Op.MLOAD(offset=0x40)) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000003, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=Op.MLOAD(offset=0x80)) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000004, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=Op.MLOAD(offset=0xa0)) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000005, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=Op.CALLER) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000006, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=Op.NUMBER) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000007, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=Op.ADD(0xe0000000000000000000000000000000000000000, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8))) + Op.MSTORE(offset=0x200, value=Op.SLOAD(key=Op.ADD(0xb, Op.MUL(Op.MLOAD(offset=0x40), 0xc)))) + Op.MLOAD(offset=0x1c0) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x200)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.MLOAD(offset=0x200) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x2) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.MLOAD(offset=0x1c0) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.SSTORE(key=Op.ADD(0xb, Op.MUL(Op.MLOAD(offset=0x40), 0xc)), value=Op.MLOAD(offset=0x1c0)) + Op.SSTORE(key=Op.ADD(0xa, Op.MUL(Op.MLOAD(offset=0x40), 0xc)), value=Op.ADD(Op.SLOAD(key=Op.ADD(0xa, Op.MUL(Op.MLOAD(offset=0x40), 0xc))), 0x1)) + Op.JUMPI(pc=0x4b9, condition=Op.ISZERO(Op.EQ(0x1, 0x2))) + Op.MLOAD(offset=0x80) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.SUB + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.MLOAD(offset=0x80) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.ADD + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.JUMPDEST + Op.JUMP(pc=0x4cb) + Op.JUMPDEST + Op.MSTORE(offset=0x300, value=0x15) + Op.RETURN(offset=0x300, size=0x20) + Op.JUMPDEST + Op.PUSH1[0x1c] + Op.PUSH1[0xc0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.DUP2, value=Op.CALLER) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x20), value=0x1) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x40), value=Op.MLOAD(offset=0xa0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x60), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x80), value=Op.MLOAD(offset=0x1c0)) + Op.LOG2(offset=Op.DUP4, size=0xa0, topic_1=0x9463d1cc4aa2db0dc624c996b1846f028d43c48cfc8b9f427f13336e4a732264, topic_2=Op.MLOAD(offset=0x40)) + Op.POP + Op.MSTORE(offset=0x340, value=Op.MLOAD(offset=0x1c0)) + Op.RETURN(offset=0x340, size=0x20) + Op.MSTORE(offset=0x360, value=0x0) + Op.RETURN(offset=0x360, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0xa0c, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x909f073))) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0xa0, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x44)) + Op.JUMPI(pc=0x576, condition=Op.ISZERO(Op.ISZERO(Op.SGT(Op.MLOAD(offset=0x80), 0x0)))) + Op.MSTORE(offset=0x380, value=0x2) + Op.RETURN(offset=0x380, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x58f, condition=Op.ISZERO(Op.ISZERO(Op.SGT(Op.MLOAD(offset=0xa0), 0x0)))) + Op.MSTORE(offset=0x3a0, value=0x3) + Op.RETURN(offset=0x3a0, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x5a8, condition=Op.ISZERO(Op.ISZERO(Op.SGT(Op.MLOAD(offset=0x40), 0x0)))) + Op.MSTORE(offset=0x3c0, value=0x4) + Op.RETURN(offset=0x3c0, size=0x20) + Op.JUMPDEST + Op.MSTORE(offset=0x120, value=Op.MUL(Op.SDIV(Op.MUL(Op.MLOAD(offset=0x80), Op.MLOAD(offset=0xa0)), Op.MUL(Op.SLOAD(key=Op.ADD(0x4, Op.MUL(Op.MLOAD(offset=0x40), 0xc))), Op.EXP(0xa, Op.SLOAD(key=Op.ADD(0x3, Op.MUL(Op.MLOAD(offset=0x40), 0xc)))))), 0xde0b6b3a7640000)) + Op.JUMPI(pc=0x610, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x120), Op.SLOAD(key=Op.ADD(0x5, Op.MUL(Op.MLOAD(offset=0x40), 0xc)))))) + Op.JUMPI(pc=0x603, condition=Op.ISZERO(Op.SGT(Op.CALLVALUE, 0x0))) + Op.POP(Op.CALL(gas=0x1388, address=Op.CALLER, value=Op.CALLVALUE, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.JUMPDEST + Op.MSTORE(offset=0x3e0, value=0xb) + Op.RETURN(offset=0x3e0, size=0x20) + Op.JUMPDEST + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=0x400, value=Op.SLOAD(key=Op.SHA3)) + Op.JUMPI(pc=0x9ff, condition=Op.ISZERO(Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x400), Op.MLOAD(offset=0x80))))) + Op.PUSH1[0xe0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x6) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x20), value=0x2) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x40), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x60), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x80), value=Op.MLOAD(offset=0xa0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0xa0), value=Op.CALLER) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0xc0), value=Op.NUMBER) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.PUSH2[0x180] + Op.MSTORE + Op.MLOAD(offset=0x180) + Op.SHA3(offset=Op.DUP2, size=Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20)) + Op.SWAP1 + Op.POP + Op.PUSH2[0x1c0] + Op.MSTORE + Op.JUMPI(pc=0x98a, condition=Op.ISZERO(Op.ISZERO(Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000000, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)))))) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000000, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=Op.MLOAD(offset=0x1c0)) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000001, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x2) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000002, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=Op.MLOAD(offset=0x40)) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000003, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=Op.MLOAD(offset=0x80)) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000004, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=Op.MLOAD(offset=0xa0)) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000005, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=Op.CALLER) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000006, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=Op.NUMBER) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000007, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=Op.ADD(0xe0000000000000000000000000000000000000000, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8))) + Op.MSTORE(offset=0x200, value=Op.SLOAD(key=Op.ADD(0xb, Op.MUL(Op.MLOAD(offset=0x40), 0xc)))) + Op.MLOAD(offset=0x1c0) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x200)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.MLOAD(offset=0x200) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x2) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.MLOAD(offset=0x1c0) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.SSTORE(key=Op.ADD(0xb, Op.MUL(Op.MLOAD(offset=0x40), 0xc)), value=Op.MLOAD(offset=0x1c0)) + Op.SSTORE(key=Op.ADD(0xa, Op.MUL(Op.MLOAD(offset=0x40), 0xc)), value=Op.ADD(Op.SLOAD(key=Op.ADD(0xa, Op.MUL(Op.MLOAD(offset=0x40), 0xc))), 0x1)) + Op.JUMPI(pc=0x985, condition=Op.ISZERO(Op.EQ(0x2, 0x2))) + Op.MLOAD(offset=0x80) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.SUB + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.MLOAD(offset=0x80) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.ADD + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.JUMPDEST + Op.JUMP(pc=0x997) + Op.JUMPDEST + Op.MSTORE(offset=0x560, value=0x15) + Op.RETURN(offset=0x560, size=0x20) + Op.JUMPDEST + Op.PUSH1[0x1c] + Op.PUSH1[0xc0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.DUP2, value=Op.CALLER) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x20), value=0x2) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x40), value=Op.MLOAD(offset=0xa0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x60), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x80), value=Op.MLOAD(offset=0x1c0)) + Op.LOG2(offset=Op.DUP4, size=0xa0, topic_1=0x9463d1cc4aa2db0dc624c996b1846f028d43c48cfc8b9f427f13336e4a732264, topic_2=Op.MLOAD(offset=0x40)) + Op.POP + Op.MSTORE(offset=0x580, value=Op.MLOAD(offset=0x1c0)) + Op.RETURN(offset=0x580, size=0x20) + Op.JUMPDEST + Op.MSTORE(offset=0x5a0, value=0x0) + Op.RETURN(offset=0x5a0, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x1733, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x9998bd00))) + Op.CALLDATASIZE + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.CALLDATACOPY(dest_offset=Op.DUP3, offset=0x4, size=Op.CALLDATASIZE) + Op.MSTORE(offset=0x5e0, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x600, value=Op.ADD(Op.ADD(Op.DUP3, 0x20), Op.CALLDATALOAD(offset=0x24))) + Op.POP + Op.MSTORE(offset=0x620, value=Op.CALLVALUE) + Op.MSTORE(offset=0x640, value=0x0) + Op.JUMPDEST + Op.JUMPI(pc=0x170a, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x640), Op.MLOAD(offset=Op.SUB(Op.MLOAD(offset=0x600), 0x20))))) + Op.MSTORE(offset=0x1c0, value=Op.MLOAD(offset=Op.ADD(Op.MLOAD(offset=0x600), Op.MUL(0x20, Op.MLOAD(offset=0x640))))) + Op.JUMPI(pc=0xa9d, condition=Op.ISZERO(Op.ISZERO(Op.SGT(Op.NUMBER, Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000006, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8))))))) + Op.MSTORE(offset=0x660, value=0x16) + Op.RETURN(offset=0x660, size=0x20) + Op.JUMPDEST + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000002, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)))) + Op.MSTORE(offset=0x680, value=Op.SLOAD(key=Op.ADD(0x2, Op.MUL(Op.MLOAD(offset=0x40), 0xc)))) + Op.MSTORE(offset=0x6a0, value=Op.SLOAD(key=Op.ADD(0x3, Op.MUL(Op.MLOAD(offset=0x40), 0xc)))) + Op.MSTORE(offset=0x6c0, value=Op.SLOAD(key=Op.ADD(0x4, Op.MUL(Op.MLOAD(offset=0x40), 0xc)))) + Op.MSTORE(offset=0x6e0, value=Op.SLOAD(key=Op.ADD(0x5, Op.MUL(Op.MLOAD(offset=0x40), 0xc)))) + Op.MSTORE(offset=0x700, value=Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000001, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)))) + Op.MSTORE(offset=0x80, value=Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000003, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)))) + Op.MSTORE(offset=0xa0, value=Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000004, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)))) + Op.MSTORE(offset=0x720, value=Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000005, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)))) + Op.JUMPI(pc=0x110e, condition=Op.ISZERO(Op.EQ(Op.MLOAD(offset=0x700), 0x1))) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=0x400, value=Op.SLOAD(key=Op.SHA3)) + Op.JUMPI(pc=0x10fc, condition=Op.ISZERO(Op.SGT(Op.MLOAD(offset=0x400), 0x0))) + Op.MLOAD(offset=0x80) + Op.MLOAD(offset=0x400) + Op.MLOAD(offset=0x5e0) + Op.JUMPI(pc=0xbe0, condition=Op.ISZERO(Op.SLT(Op.DUP3, Op.DUP1))) + Op.DUP2 + Op.JUMP(pc=0xbe2) + Op.JUMPDEST + Op.DUP1 + Op.JUMPDEST + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.JUMPI(pc=0xbf4, condition=Op.ISZERO(Op.SLT(Op.DUP3, Op.DUP1))) + Op.DUP2 + Op.JUMP(pc=0xbf6) + Op.JUMPDEST + Op.DUP1 + Op.JUMPDEST + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH2[0x760] + Op.MSTORE + Op.MSTORE(offset=0x120, value=Op.SDIV(Op.MUL(Op.MUL(Op.MLOAD(offset=0x760), Op.MLOAD(offset=0xa0)), 0xde0b6b3a7640000), Op.MUL(Op.MLOAD(offset=0x6c0), Op.EXP(0xa, Op.MLOAD(offset=0x6a0))))) + Op.JUMPI(pc=0xc5b, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x120), Op.MLOAD(offset=0x6e0)))) + Op.JUMPI(pc=0xc4e, condition=Op.ISZERO(Op.SGT(Op.MLOAD(offset=0x620), 0x0))) + Op.POP(Op.CALL(gas=0x1388, address=Op.CALLER, value=Op.MLOAD(offset=0x620), args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.JUMPDEST + Op.MSTORE(offset=0x800, value=0xc) + Op.RETURN(offset=0x800, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0xcb0, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x760), Op.MLOAD(offset=0x80)))) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000003, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=Op.SUB(Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000003, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8))), Op.MLOAD(offset=0x760))) + Op.JUMP(pc=0xfd4) + Op.JUMPDEST + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000000, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000001, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000002, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000003, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000004, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000005, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000006, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000007, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x2) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=0x820, value=Op.SLOAD(key=Op.SHA3)) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=0x860, value=Op.SLOAD(key=Op.SHA3)) + Op.JUMPI(pc=0xe3a, condition=Op.ISZERO(Op.MLOAD(offset=0x820))) + Op.MLOAD(offset=0x860) + Op.JUMP(pc=0xe3d) + Op.JUMPDEST + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0xeb7, condition=Op.ISZERO) + Op.MLOAD(offset=0x860) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x820)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.MLOAD(offset=0x820) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x860)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x2) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.JUMP(pc=0xf06) + Op.JUMPDEST + Op.JUMPI(pc=0xf05, condition=Op.ISZERO(Op.MLOAD(offset=0x820))) + Op.SSTORE(key=Op.ADD(0xb, Op.MUL(Op.MLOAD(offset=0x40), 0xc)), value=Op.MLOAD(offset=0x820)) + Op.PUSH1[0x0] + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x820)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.JUMPDEST + Op.JUMPDEST + Op.JUMPI(pc=0xf46, condition=Op.ISZERO(Op.MLOAD(offset=0x860))) + Op.PUSH1[0x0] + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.JUMPDEST + Op.JUMPI(pc=0xf86, condition=Op.ISZERO(Op.MLOAD(offset=0x820))) + Op.PUSH1[0x0] + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x2) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.JUMPDEST + Op.PUSH1[0x0] + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.SSTORE(key=Op.ADD(0xa, Op.MUL(Op.MLOAD(offset=0x40), 0xc)), value=Op.SUB(Op.SLOAD(key=Op.ADD(0xa, Op.MUL(Op.MLOAD(offset=0x40), 0xc))), 0x1)) + Op.JUMPDEST + Op.MLOAD(offset=0x760) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.SUB + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.MLOAD(offset=0x760) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x720)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.ADD + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x720)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.POP(Op.CALL(gas=0x1388, address=Op.CALLER, value=Op.MLOAD(offset=0x120), args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.PUSH1[0x1c] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.DUP2, value=0x2) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x20), value=Op.MLOAD(offset=0xa0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x40), value=Op.MLOAD(offset=0x760)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x60), value=Op.MLOAD(offset=0x1c0)) + Op.LOG4(offset=Op.DUP6, size=0x80, topic_1=0xf9fe89f83633cc2eca9b17e1f77422f037cb026eaca4e6a5337fa1595f50a81, topic_2=Op.MLOAD(offset=0x40), topic_3=Op.CALLER, topic_4=Op.MLOAD(offset=0x720)) + Op.POP + Op.JUMP(pc=0x1109) + Op.JUMPDEST + Op.MSTORE(offset=0x9e0, value=0xa) + Op.RETURN(offset=0x9e0, size=0x20) + Op.JUMPDEST + Op.JUMP(pc=0x1680) + Op.JUMPDEST + Op.JUMPI(pc=0x167f, condition=Op.ISZERO(Op.EQ(Op.MLOAD(offset=0x700), 0x2))) + Op.JUMPI(pc=0x1671, condition=Op.ISZERO(Op.SGT(Op.MLOAD(offset=0x620), 0x0))) + Op.JUMPI(pc=0x1160, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x620), Op.MLOAD(offset=0x6e0)))) + Op.JUMPI(pc=0x1153, condition=Op.ISZERO(Op.SGT(Op.MLOAD(offset=0x620), 0x0))) + Op.POP(Op.CALL(gas=0x1388, address=Op.CALLER, value=Op.MLOAD(offset=0x620), args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.JUMPDEST + Op.MSTORE(offset=0xa00, value=0xc) + Op.RETURN(offset=0xa00, size=0x20) + Op.JUMPDEST + Op.MSTORE(offset=0xa20, value=Op.SDIV(Op.MUL(Op.MUL(Op.MLOAD(offset=0x80), Op.MLOAD(offset=0xa0)), 0xde0b6b3a7640000), Op.MUL(Op.MLOAD(offset=0x6c0), Op.EXP(0xa, Op.MLOAD(offset=0x6a0))))) + Op.MLOAD(offset=0x620) + Op.MLOAD(offset=0xa20) + Op.JUMPI(pc=0x1198, condition=Op.ISZERO(Op.SLT(Op.DUP3, Op.DUP1))) + Op.DUP2 + Op.JUMP(pc=0x119a) + Op.JUMPDEST + Op.DUP1 + Op.JUMPDEST + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH2[0x120] + Op.MSTORE + Op.JUMPI(pc=0x121b, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x120), Op.MLOAD(offset=0xa20)))) + Op.MSTORE(offset=0x760, value=Op.SDIV(Op.SDIV(Op.MUL(Op.MLOAD(offset=0x120), Op.MUL(Op.MLOAD(offset=0x6c0), Op.EXP(0xa, Op.MLOAD(offset=0x6a0)))), Op.MLOAD(offset=0xa0)), 0xde0b6b3a7640000)) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000003, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=Op.SUB(Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000003, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8))), Op.MLOAD(offset=0x760))) + Op.JUMP(pc=0x1546) + Op.JUMPDEST + Op.MSTORE(offset=0x760, value=Op.MLOAD(offset=0x80)) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000000, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000001, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000002, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000003, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000004, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000005, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000006, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000007, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x2) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=0x820, value=Op.SLOAD(key=Op.SHA3)) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=0x860, value=Op.SLOAD(key=Op.SHA3)) + Op.JUMPI(pc=0x13ac, condition=Op.ISZERO(Op.MLOAD(offset=0x820))) + Op.MLOAD(offset=0x860) + Op.JUMP(pc=0x13af) + Op.JUMPDEST + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x1429, condition=Op.ISZERO) + Op.MLOAD(offset=0x860) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x820)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.MLOAD(offset=0x820) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x860)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x2) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.JUMP(pc=0x1478) + Op.JUMPDEST + Op.JUMPI(pc=0x1477, condition=Op.ISZERO(Op.MLOAD(offset=0x820))) + Op.SSTORE(key=Op.ADD(0xb, Op.MUL(Op.MLOAD(offset=0x40), 0xc)), value=Op.MLOAD(offset=0x820)) + Op.PUSH1[0x0] + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x820)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.JUMPDEST + Op.JUMPDEST + Op.JUMPI(pc=0x14b8, condition=Op.ISZERO(Op.MLOAD(offset=0x860))) + Op.PUSH1[0x0] + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.JUMPDEST + Op.JUMPI(pc=0x14f8, condition=Op.ISZERO(Op.MLOAD(offset=0x820))) + Op.PUSH1[0x0] + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x2) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.JUMPDEST + Op.PUSH1[0x0] + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.SSTORE(key=Op.ADD(0xa, Op.MUL(Op.MLOAD(offset=0x40), 0xc)), value=Op.SUB(Op.SLOAD(key=Op.ADD(0xa, Op.MUL(Op.MLOAD(offset=0x40), 0xc))), 0x1)) + Op.JUMPDEST + Op.MLOAD(offset=0x760) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x720)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.SUB + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x720)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.MLOAD(offset=0x760) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.ADD + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.POP(Op.CALL(gas=0x1388, address=Op.MLOAD(offset=0x720), value=Op.MLOAD(offset=0x120), args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.PUSH1[0x1c] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.DUP2, value=0x1) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x20), value=Op.MLOAD(offset=0xa0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x40), value=Op.MLOAD(offset=0x760)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x60), value=Op.MLOAD(offset=0x1c0)) + Op.LOG4(offset=Op.DUP6, size=0x80, topic_1=0xf9fe89f83633cc2eca9b17e1f77422f037cb026eaca4e6a5337fa1595f50a81, topic_2=Op.MLOAD(offset=0x40), topic_3=Op.CALLER, topic_4=Op.MLOAD(offset=0x720)) + Op.POP + Op.JUMP(pc=0x167e) + Op.JUMPDEST + Op.MSTORE(offset=0xc00, value=0xa) + Op.RETURN(offset=0xc00, size=0x20) + Op.JUMPDEST + Op.JUMPDEST + Op.JUMPDEST + Op.SSTORE(key=Op.ADD(0x7, Op.MUL(Op.MLOAD(offset=0x40), 0xc)), value=Op.MLOAD(offset=0xa0)) + Op.PUSH1[0x1c] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.DUP2, value=Op.MLOAD(offset=0x700)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x20), value=Op.MLOAD(offset=0xa0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x40), value=Op.MLOAD(offset=0x760)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x60), value=Op.TIMESTAMP) + Op.LOG2(offset=Op.DUP4, size=0x80, topic_1=0x50944f09ce56f9f0e2cb67683c9b451049c39f60452b850b169148f3daa51ed6, topic_2=Op.MLOAD(offset=0x40)) + Op.POP + Op.MSTORE(offset=0x5e0, value=Op.SUB(Op.MLOAD(offset=0x5e0), Op.MLOAD(offset=0x760))) + Op.MSTORE(offset=0x620, value=Op.SUB(Op.MLOAD(offset=0x620), Op.MLOAD(offset=0x120))) + Op.MSTORE(offset=0x640, value=Op.ADD(Op.MLOAD(offset=0x640), 0x1)) + Op.JUMP(pc=0xa46) + Op.JUMPDEST + Op.JUMPI(pc=0x1726, condition=Op.ISZERO(Op.MLOAD(offset=0x620))) + Op.POP(Op.CALL(gas=0x1388, address=Op.CALLER, value=Op.MLOAD(offset=0x620), args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.JUMPDEST + Op.MSTORE(offset=0xc20, value=0x1) + Op.RETURN(offset=0xc20, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x185b, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x34a501c7))) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0x1c] + Op.PUSH1[0x84] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x27f08b00) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.CALLER) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.ADDRESS) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=Op.MLOAD(offset=0x80)) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.SLOAD(key=Op.ADD(0x2, Op.MUL(Op.MLOAD(offset=0x40), 0xc))), value=0x0, args_offset=Op.DUP4, args_size=0x64, ret_offset=0xc40, ret_size=0x20)) + Op.MLOAD(offset=0xc40) + Op.SWAP1 + Op.POP + Op.JUMPI(pc=0x184e, condition=Op.ISZERO) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=0x400, value=Op.SLOAD(key=Op.SHA3)) + Op.MSTORE(offset=0xc80, value=Op.ADD(Op.MLOAD(offset=0x400), Op.MLOAD(offset=0x80))) + Op.MLOAD(offset=0xc80) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.PUSH1[0x1c] + Op.PUSH1[0x40] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.DUP2, value=Op.MLOAD(offset=0x80)) + Op.LOG3(offset=Op.DUP5, size=0x20, topic_1=0x301cd746dbb5e7f9ade2bcd9e8a849b968bfcc222de48d2086ba200184acc83d, topic_2=Op.MLOAD(offset=0x40), topic_3=Op.CALLER) + Op.POP + Op.MSTORE(offset=0xcc0, value=Op.MLOAD(offset=0xc80)) + Op.RETURN(offset=0xcc0, size=0x20) + Op.JUMPDEST + Op.MSTORE(offset=0xce0, value=0x0) + Op.RETURN(offset=0xce0, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x1982, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xe1ed3ad3))) + Op.MSTORE(offset=0x80, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=0x400, value=Op.SLOAD(key=Op.SHA3)) + Op.JUMPI(pc=0x1975, condition=Op.ISZERO(Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x400), Op.MLOAD(offset=0x80))))) + Op.SUB(Op.MLOAD(offset=0x400), Op.MLOAD(offset=0x80)) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x86744558) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.CALLER) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.MLOAD(offset=0x80)) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.SLOAD(key=Op.ADD(0x2, Op.MUL(Op.MLOAD(offset=0x40), 0xc))), value=0x0, args_offset=Op.DUP4, args_size=0x44, ret_offset=0xd60, ret_size=0x20)) + Op.MLOAD(offset=0xd60) + Op.SWAP1 + Op.POP + Op.PUSH2[0xd40] + Op.MSTORE + Op.PUSH1[0x1c] + Op.PUSH1[0x40] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.DUP2, value=Op.MLOAD(offset=0x80)) + Op.LOG3(offset=Op.DUP5, size=0x20, topic_1=0xfa4460934f383b326d79dcd4f1e59a17ac8ee9a87312169933e7f68b85c1a8ce, topic_2=Op.MLOAD(offset=0x40), topic_3=Op.CALLER) + Op.POP + Op.MSTORE(offset=0xd80, value=Op.MLOAD(offset=0xd40)) + Op.RETURN(offset=0xd80, size=0x20) + Op.JUMPDEST + Op.MSTORE(offset=0xda0, value=0x0) + Op.RETURN(offset=0xda0, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x1f08, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x327a22f1))) + Op.MSTORE(offset=0x1c0, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x700, value=Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000001, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)))) + Op.MSTORE(offset=0x80, value=Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000003, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)))) + Op.MSTORE(offset=0xa0, value=Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000004, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)))) + Op.MSTORE(offset=0x720, value=Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000005, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)))) + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000002, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)))) + Op.MSTORE(offset=0x680, value=Op.SLOAD(key=Op.ADD(0x2, Op.MUL(Op.MLOAD(offset=0x40), 0xc)))) + Op.MSTORE(offset=0x6a0, value=Op.SLOAD(key=Op.ADD(0x3, Op.MUL(Op.MLOAD(offset=0x40), 0xc)))) + Op.MSTORE(offset=0x6c0, value=Op.SLOAD(key=Op.ADD(0x4, Op.MUL(Op.MLOAD(offset=0x40), 0xc)))) + Op.JUMPI(pc=0x1efb, condition=Op.ISZERO(Op.EQ(Op.CALLER, Op.MLOAD(offset=0x720)))) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000000, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000001, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000002, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000003, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000004, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000005, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000006, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0) + Op.SSTORE(key=Op.ADD(0xe0000000000000000000000000000000000000007, Op.MUL(Op.MLOAD(offset=0x1c0), 0x8)), value=0x0) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x2) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=0x820, value=Op.SLOAD(key=Op.SHA3)) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=0x860, value=Op.SLOAD(key=Op.SHA3)) + Op.JUMPI(pc=0x1c00, condition=Op.ISZERO(Op.MLOAD(offset=0x820))) + Op.MLOAD(offset=0x860) + Op.JUMP(pc=0x1c03) + Op.JUMPDEST + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x1c7d, condition=Op.ISZERO) + Op.MLOAD(offset=0x860) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x820)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.MLOAD(offset=0x820) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x860)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x2) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.JUMP(pc=0x1ccc) + Op.JUMPDEST + Op.JUMPI(pc=0x1ccb, condition=Op.ISZERO(Op.MLOAD(offset=0x820))) + Op.SSTORE(key=Op.ADD(0xb, Op.MUL(Op.MLOAD(offset=0x40), 0xc)), value=Op.MLOAD(offset=0x820)) + Op.PUSH1[0x0] + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x820)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.JUMPDEST + Op.JUMPDEST + Op.JUMPI(pc=0x1d0c, condition=Op.ISZERO(Op.MLOAD(offset=0x860))) + Op.PUSH1[0x0] + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.JUMPDEST + Op.JUMPI(pc=0x1d4c, condition=Op.ISZERO(Op.MLOAD(offset=0x820))) + Op.PUSH1[0x0] + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x2) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.JUMPDEST + Op.PUSH1[0x0] + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.SSTORE(key=Op.ADD(0xa, Op.MUL(Op.MLOAD(offset=0x40), 0xc)), value=Op.SUB(Op.SLOAD(key=Op.ADD(0xa, Op.MUL(Op.MLOAD(offset=0x40), 0xc))), 0x1)) + Op.JUMPI(pc=0x1dde, condition=Op.ISZERO(Op.EQ(Op.MLOAD(offset=0x700), 0x1))) + Op.MSTORE(offset=0x120, value=Op.MUL(Op.SDIV(Op.MUL(Op.MLOAD(offset=0x80), Op.MLOAD(offset=0xa0)), Op.MUL(Op.MLOAD(offset=0x6c0), Op.EXP(0xa, Op.MLOAD(offset=0x6a0)))), 0xde0b6b3a7640000)) + Op.POP(Op.CALL(gas=0x1388, address=Op.CALLER, value=Op.MLOAD(offset=0x120), args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.JUMP(pc=0x1e9c) + Op.JUMPDEST + Op.JUMPI(pc=0x1e9b, condition=Op.ISZERO(Op.EQ(Op.MLOAD(offset=0x700), 0x2))) + Op.MLOAD(offset=0x80) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.SUB + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.MLOAD(offset=0x80) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SLOAD(key=Op.SHA3) + Op.ADD + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.CALLER) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.SHA3 + Op.SSTORE + Op.JUMPDEST + Op.JUMPDEST + Op.PUSH1[0x1c] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.DUP2, value=Op.CALLER) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x20), value=Op.MLOAD(offset=0xa0)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x40), value=Op.MLOAD(offset=0x80)) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x60), value=Op.MLOAD(offset=0x1c0)) + Op.LOG2(offset=Op.DUP4, size=0x80, topic_1=0xac6333455d304288767a0f1039d666d16882d10b6ea83693d2556e4c8098001, topic_2=Op.MLOAD(offset=0x40)) + Op.POP + Op.MSTORE(offset=0xf40, value=0x1) + Op.RETURN(offset=0xf40, size=0x20) + Op.JUMPDEST + Op.MSTORE(offset=0xf60, value=0x0) + Op.RETURN(offset=0xf60, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x22f0, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xd91e22f4))) + Op.MSTORE(offset=0xf80, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x680, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x6a0, value=Op.CALLDATALOAD(offset=0x44)) + Op.MSTORE(offset=0x6c0, value=Op.CALLDATALOAD(offset=0x64)) + Op.MSTORE(offset=0x6e0, value=Op.CALLDATALOAD(offset=0x84)) + Op.MSTORE(offset=0xfa0, value=Op.CALLDATALOAD(offset=0xa4)) + Op.MSTORE(offset=0xfc0, value=Op.ADD(Op.SLOAD(key=0x160000000000000000000000000000000000000000), 0x1)) + Op.JUMPI(pc=0x1f76, condition=Op.ISZERO(Op.ISZERO(Op.SGT(Op.MLOAD(offset=0xf80), 0x0)))) + Op.MSTORE(offset=0xfe0, value=0x1e) + Op.RETURN(offset=0xfe0, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x1fa4, condition=Op.ISZERO(Op.SLOAD(key=Op.ADD(0xd0000000000000000000000000000000000000000, Op.MLOAD(offset=0xf80))))) + Op.MSTORE(offset=0x1000, value=0x1f) + Op.RETURN(offset=0x1000, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x1fbe, condition=Op.ISZERO(Op.ISZERO(Op.SGT(Op.MLOAD(offset=0x680), 0x0)))) + Op.MSTORE(offset=0x1020, value=0x20) + Op.RETURN(offset=0x1020, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x1fd7, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=0xfa0), 0x0))) + Op.MSTORE(offset=0x1040, value=0x21) + Op.RETURN(offset=0x1040, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x1ff0, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x6a0), 0x0))) + Op.MSTORE(offset=0x1060, value=0x22) + Op.RETURN(offset=0x1060, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x2009, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x6c0), 0x0))) + Op.MSTORE(offset=0x1080, value=0x23) + Op.RETURN(offset=0x1080, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x2022, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x6e0), 0x0))) + Op.MSTORE(offset=0x10a0, value=0x24) + Op.RETURN(offset=0x10a0, size=0x20) + Op.JUMPDEST + Op.PUSH1[0x0] + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0xc32d01a1) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.CALLER) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.ADDRESS) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x680), value=0x0, args_offset=Op.DUP4, args_size=0x44, ret_offset=0x10c0, ret_size=0x20)) + Op.MLOAD(offset=0x10c0) + Op.SWAP1 + Op.POP + Op.JUMPI(pc=0x2075, condition=Op.ISZERO(Op.ISZERO(Op.EQ))) + Op.MSTORE(offset=0x10e0, value=0x28) + Op.RETURN(offset=0x10e0, size=0x20) + Op.JUMPDEST + Op.PUSH1[0x1] + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x83b58638) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.ADDRESS) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=0x0) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x680), value=0x0, args_offset=Op.DUP4, args_size=0x44, ret_offset=0x1100, ret_size=0x20)) + Op.MLOAD(offset=0x1100) + Op.SWAP1 + Op.POP + Op.JUMPI(pc=0x20c9, condition=Op.ISZERO(Op.ISZERO(Op.EQ))) + Op.MSTORE(offset=0x1120, value=0x29) + Op.RETURN(offset=0x1120, size=0x20) + Op.JUMPDEST + Op.PUSH1[0x0] + Op.PUSH1[0x1c] + Op.PUSH1[0x44] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x26690247) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.ADDRESS) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x680), value=0x0, args_offset=Op.DUP4, args_size=0x24, ret_offset=0x1140, ret_size=0x20)) + Op.MLOAD(offset=0x1140) + Op.SWAP1 + Op.POP + Op.JUMPI(pc=0x2116, condition=Op.ISZERO(Op.ISZERO(Op.EQ))) + Op.MSTORE(offset=0x1160, value=0x2a) + Op.RETURN(offset=0x1160, size=0x20) + Op.JUMPDEST + Op.PUSH1[0x0] + Op.PUSH1[0x1c] + Op.PUSH1[0x64] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x86744558) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.CALLER) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=0x0) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x680), value=0x0, args_offset=Op.DUP4, args_size=0x44, ret_offset=0x1180, ret_size=0x20)) + Op.MLOAD(offset=0x1180) + Op.SWAP1 + Op.POP + Op.JUMPI(pc=0x216a, condition=Op.ISZERO(Op.ISZERO(Op.EQ))) + Op.MSTORE(offset=0x11a0, value=0x2b) + Op.RETURN(offset=0x11a0, size=0x20) + Op.JUMPDEST + Op.PUSH1[0x0] + Op.PUSH1[0x1c] + Op.PUSH1[0x84] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x1c), value=0x27f08b00) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x4), value=Op.ADDRESS) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x24), value=Op.CALLER) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x44), value=0x0) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x2d), address=Op.MLOAD(offset=0x680), value=0x0, args_offset=Op.DUP4, args_size=0x64, ret_offset=0x11c0, ret_size=0x20)) + Op.MLOAD(offset=0x11c0) + Op.SWAP1 + Op.POP + Op.JUMPI(pc=0x21c4, condition=Op.ISZERO(Op.ISZERO(Op.EQ))) + Op.MSTORE(offset=0x11e0, value=0x2c) + Op.RETURN(offset=0x11e0, size=0x20) + Op.JUMPDEST + Op.SSTORE(key=Op.MUL(Op.MLOAD(offset=0xfc0), 0xc), value=Op.MLOAD(offset=0xfc0)) + Op.SSTORE(key=Op.ADD(0x1, Op.MUL(Op.MLOAD(offset=0xfc0), 0xc)), value=Op.MLOAD(offset=0xf80)) + Op.SSTORE(key=Op.ADD(0x2, Op.MUL(Op.MLOAD(offset=0xfc0), 0xc)), value=Op.MLOAD(offset=0x680)) + Op.SSTORE(key=Op.ADD(0x6, Op.MUL(Op.MLOAD(offset=0xfc0), 0xc)), value=Op.MLOAD(offset=0xfa0)) + Op.SSTORE(key=Op.ADD(0x3, Op.MUL(Op.MLOAD(offset=0xfc0), 0xc)), value=Op.MLOAD(offset=0x6a0)) + Op.SSTORE(key=Op.ADD(0x4, Op.MUL(Op.MLOAD(offset=0xfc0), 0xc)), value=Op.MLOAD(offset=0x6c0)) + Op.SSTORE(key=Op.ADD(0x5, Op.MUL(Op.MLOAD(offset=0xfc0), 0xc)), value=Op.MLOAD(offset=0x6e0)) + Op.SSTORE(key=Op.ADD(0x7, Op.MUL(Op.MLOAD(offset=0xfc0), 0xc)), value=0x1) + Op.SSTORE(key=Op.ADD(0x8, Op.MUL(Op.MLOAD(offset=0xfc0), 0xc)), value=Op.CALLER) + Op.SSTORE(key=Op.ADD(0x9, Op.MUL(Op.MLOAD(offset=0xfc0), 0xc)), value=Op.NUMBER) + Op.SSTORE(key=Op.ADD(0xc0000000000000000000000000000000000000000, Op.MLOAD(offset=0x680)), value=Op.MLOAD(offset=0xfc0)) + Op.SSTORE(key=Op.ADD(0xd0000000000000000000000000000000000000000, Op.MLOAD(offset=0xf80)), value=Op.MLOAD(offset=0xfc0)) + Op.SSTORE(key=0x160000000000000000000000000000000000000000, value=Op.MLOAD(offset=0xfc0)) + Op.PUSH1[0x1c] + Op.PUSH1[0x40] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.ADD + Op.MSTORE(offset=Op.DUP2, value=Op.MLOAD(offset=0xfc0)) + Op.LOG1(offset=Op.DUP3, size=0x20, topic_1=0x1238fe6d44cf796960d61b74766b3a383110e472d849f5ca16ae50215bc05e58) + Op.POP + Op.MSTORE(offset=0x1200, value=0x1) + Op.RETURN(offset=0x1200, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x232a, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x41569661))) + Op.MSTORE(offset=0x1220, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x1240, value=Op.SLOAD(key=Op.ADD(0xc0000000000000000000000000000000000000000, Op.MLOAD(offset=0x1220)))) + Op.RETURN(offset=0x1240, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x2364, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xfcde9f78))) + Op.MSTORE(offset=0xf80, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x1260, value=Op.SLOAD(key=Op.ADD(0xd0000000000000000000000000000000000000000, Op.MLOAD(offset=0xf80)))) + Op.RETURN(offset=0x1260, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x2392, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x6e5b4343))) + Op.MSTORE(offset=0x1280, value=Op.SLOAD(key=0x160000000000000000000000000000000000000000)) + Op.RETURN(offset=0x1280, size=0x20) + Op.JUMPDEST + Op.JUMPI(pc=0x24e6, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xfafa69c2))) + Op.MSTORE(offset=0xfc0, value=Op.CALLDATALOAD(offset=0x4)) + Op.PUSH2[0x180] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0xb) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.PUSH2[0x12a0] + Op.MSTORE + Op.MSTORE(offset=Op.MLOAD(offset=0x12a0), value=Op.SLOAD(key=Op.MUL(Op.MLOAD(offset=0xfc0), 0xc))) + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x12a0), 0x20), value=Op.SLOAD(key=Op.ADD(0x1, Op.MUL(Op.MLOAD(offset=0xfc0), 0xc)))) + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x12a0), 0x40), value=Op.SLOAD(key=Op.ADD(0x2, Op.MUL(Op.MLOAD(offset=0xfc0), 0xc)))) + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x12a0), 0x60), value=Op.SLOAD(key=Op.ADD(0x3, Op.MUL(Op.MLOAD(offset=0xfc0), 0xc)))) + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x12a0), 0x80), value=Op.SLOAD(key=Op.ADD(0x4, Op.MUL(Op.MLOAD(offset=0xfc0), 0xc)))) + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x12a0), 0xa0), value=Op.SLOAD(key=Op.ADD(0x5, Op.MUL(Op.MLOAD(offset=0xfc0), 0xc)))) + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x12a0), 0xc0), value=Op.SLOAD(key=Op.ADD(0x7, Op.MUL(Op.MLOAD(offset=0xfc0), 0xc)))) + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x12a0), 0xe0), value=Op.SLOAD(key=Op.ADD(0x8, Op.MUL(Op.MLOAD(offset=0xfc0), 0xc)))) + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x12a0), 0x100), value=Op.SLOAD(key=Op.ADD(0x9, Op.MUL(Op.MLOAD(offset=0xfc0), 0xc)))) + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x12a0), 0x120), value=Op.SLOAD(key=Op.ADD(0xa, Op.MUL(Op.MLOAD(offset=0xfc0), 0xc)))) + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x12a0), 0x140), value=Op.SLOAD(key=Op.ADD(0x6, Op.MUL(Op.MLOAD(offset=0xfc0), 0xc)))) + Op.JUMPI(pc=0x24b2, condition=Op.ISZERO(Op.MLOAD(offset=0x12a0))) + Op.MLOAD(offset=0x12a0) + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20) + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20))) + Op.POP + Op.JUMPDEST + Op.PUSH1[0x40] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x1) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x20), value=0x0) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20) + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20))) + Op.POP + Op.JUMPDEST + Op.JUMPI(pc=0x262e, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x9cfc1535))) + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x1340, value=Op.SLOAD(key=Op.ADD(0xa, Op.MUL(Op.MLOAD(offset=0x40), 0xc)))) + Op.MSTORE(offset=0x1c0, value=Op.SLOAD(key=Op.ADD(0xb, Op.MUL(Op.MLOAD(offset=0x40), 0xc)))) + Op.MLOAD(offset=0x1340) + Op.ADD(0x20, Op.MUL(0x20, Op.DUP1)) + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.POP + Op.PUSH2[0x600] + Op.MSTORE + Op.MSTORE(offset=0x13a0, value=0x0) + Op.JUMPDEST + Op.JUMPI(pc=0x25d4, condition=Op.ISZERO(Op.SLT(Op.MLOAD(offset=0x13a0), Op.MLOAD(offset=0x1340)))) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x600), Op.MUL(0x20, Op.MLOAD(offset=0x13a0))), value=Op.SLOAD(key=Op.SHA3)) + Op.PUSH1[0xa0] + Op.PUSH1[0xa0] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x0) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=0xc) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=Op.MLOAD(offset=0x1c0)) + Op.MSTORE(offset=Op.ADD(0x80, Op.DUP2), value=0x2) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=0x1c0, value=Op.SLOAD(key=Op.SHA3)) + Op.MSTORE(offset=0x13a0, value=Op.ADD(Op.MLOAD(offset=0x13a0), 0x1)) + Op.JUMP(pc=0x253d) + Op.JUMPDEST + Op.JUMPI(pc=0x25fa, condition=Op.ISZERO(Op.MLOAD(offset=0x600))) + Op.MLOAD(offset=0x600) + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20) + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20))) + Op.POP + Op.JUMPDEST + Op.PUSH1[0x40] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x1) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x20), value=0x0) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20) + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20))) + Op.POP + Op.JUMPDEST + Op.JUMPI(pc=0x27e9, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0xf718190))) + Op.MSTORE(offset=0xfc0, value=Op.CALLDATALOAD(offset=0x4)) + Op.PUSH2[0x120] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x8) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.PUSH2[0x180] + Op.MSTORE + Op.MSTORE(offset=Op.MLOAD(offset=0x180), value=Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000000, Op.MUL(Op.MLOAD(offset=0xfc0), 0x8)))) + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x180), 0x20), value=Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000001, Op.MUL(Op.MLOAD(offset=0xfc0), 0x8)))) + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x180), 0x40), value=Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000002, Op.MUL(Op.MLOAD(offset=0xfc0), 0x8)))) + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x180), 0x60), value=Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000003, Op.MUL(Op.MLOAD(offset=0xfc0), 0x8)))) + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x180), 0x80), value=Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000004, Op.MUL(Op.MLOAD(offset=0xfc0), 0x8)))) + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x180), 0xa0), value=Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000005, Op.MUL(Op.MLOAD(offset=0xfc0), 0x8)))) + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x180), 0xc0), value=Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000006, Op.MUL(Op.MLOAD(offset=0xfc0), 0x8)))) + Op.MSTORE(offset=Op.ADD(Op.MLOAD(offset=0x180), 0xe0), value=Op.SLOAD(key=Op.ADD(0xe0000000000000000000000000000000000000007, Op.MUL(Op.MLOAD(offset=0xfc0), 0x8)))) + Op.JUMPI(pc=0x27b5, condition=Op.ISZERO(Op.MLOAD(offset=0x180))) + Op.MLOAD(offset=0x180) + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20) + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20))) + Op.POP + Op.JUMPDEST + Op.PUSH1[0x40] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x1) + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x20), value=0x0) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20) + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20))) + Op.POP + Op.JUMPDEST + Op.JUMPI(pc=0x2893, condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x1c9aa4b6))) + Op.MSTORE(offset=0x1220, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x24)) + Op.PUSH1[0x60] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x2) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x1220)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x0) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x20), value=Op.SLOAD(key=Op.SHA3)) + Op.PUSH1[0x80] + Op.PUSH1[0x80] + Op.MSIZE + Op.SWAP1 + Op.MSIZE + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.MSTORE + Op.MSTORE(offset=Op.DUP2, value=0x4) + Op.MSTORE(offset=Op.ADD(0x20, Op.DUP2), value=Op.MLOAD(offset=0x1220)) + Op.MSTORE(offset=Op.ADD(0x40, Op.DUP2), value=Op.MLOAD(offset=0x40)) + Op.MSTORE(offset=Op.ADD(0x60, Op.DUP2), value=0x1) + Op.DUP1 + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.ADD(Op.DUP3, 0x40), value=Op.SLOAD(key=Op.SHA3)) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP1 + Op.POP + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x40), value=0x20) + Op.RETURN(offset=Op.SUB(Op.DUP3, 0x40), size=Op.ADD(0x40, Op.MUL(Op.MLOAD(offset=Op.SUB(Op.DUP3, 0x20)), 0x20))) + Op.POP + Op.JUMPDEST + Op.POP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
