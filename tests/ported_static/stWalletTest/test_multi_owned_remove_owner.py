"""
Ported from:
tests/static/state_tests/stWalletTest/multiOwnedRemoveOwnerFiller.json
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
    ["tests/static/state_tests/stWalletTest/multiOwnedRemoveOwnerFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_multi_owned_remove_owner(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000,
    )

    pre[contract] = Account(
        balance=100,
        nonce=0,
        code=(
        Op.DIV(Op.CALLDATALOAD(offset=0x0), 0x100000000000000000000000000000000000000000000000000000000)
        + Op.JUMPI(pc=Op.PUSH2[0x65], condition=Op.EQ(Op.DUP2, 0x173825d9))
        + Op.JUMPI(pc=Op.PUSH2[0xb7], condition=Op.EQ(0x2f54bf6e, Op.DUP1))
        + Op.JUMPI(pc=Op.PUSH2[0xe8], condition=Op.EQ(0x7065cb48, Op.DUP1))
        + Op.JUMPI(pc=0x105, condition=Op.EQ(0xb75c7dc6, Op.DUP1))
        + Op.JUMPI(pc=0x142, condition=Op.EQ(0xba51a6df, Op.DUP1))
        + Op.JUMPI(pc=0x15f, condition=Op.EQ(0xf00d4b5d, Op.DUP1)) + Op.STOP
        + Op.JUMPDEST + Op.PUSH2[0x181] + Op.CALLDATALOAD(offset=0x4) + Op.PUSH1[0x0]
        + Op.PUSH1[0x40] + Op.PUSH1[0x0] + Op.CALLDATASIZE
        + Op.CALLDATACOPY(dest_offset=Op.DUP5, offset=Op.DUP3, size=Op.DUP1)
        + Op.SWAP1 + Op.SWAP2 + Op.SHA3 + Op.SWAP1 + Op.POP + Op.PUSH2[0x46d]
        + Op.DUP2 + Op.JUMPDEST
        + Op.AND(Op.CALLER, 0xffffffffffffffffffffffffffffffffffffffff)
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.DUP2 + Op.MSTORE
        + Op.MSTORE(offset=0x20, value=0x102)
        + Op.SLOAD(key=Op.SHA3(offset=Op.DUP2, size=0x40)) + Op.DUP2 + Op.DUP1
        + Op.DUP1 + Op.JUMPI(pc=0x58f, condition=Op.ISZERO(Op.EQ(Op.DUP2, Op.DUP4)))
        + Op.JUMP(pc=0x586) + Op.JUMPDEST + Op.PUSH2[0x187]
        + Op.CALLDATALOAD(offset=0x4) + Op.JUMPDEST
        + Op.PUSH20[0xffffffffffffffffffffffffffffffffffffffff] + Op.AND
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.DUP2 + Op.MSTORE
        + Op.MSTORE(offset=0x20, value=0x102)
        + Op.SLOAD(key=Op.SHA3(offset=Op.DUP2, size=0x40)) + Op.GT + Op.SWAP1
        + Op.JUMP + Op.JUMPDEST + Op.PUSH2[0x181] + Op.CALLDATALOAD(offset=0x4)
        + Op.PUSH1[0x40] + Op.PUSH1[0x0] + Op.CALLDATASIZE
        + Op.CALLDATACOPY(dest_offset=Op.DUP5, offset=Op.DUP3, size=Op.DUP1)
        + Op.SWAP1 + Op.SWAP2 + Op.SHA3 + Op.SWAP1 + Op.POP + Op.PUSH2[0x37c]
        + Op.DUP2 + Op.JUMP(pc=Op.PUSH2[0x80]) + Op.JUMPDEST + Op.PUSH2[0x181]
        + Op.CALLDATALOAD(offset=0x4)
        + Op.AND(Op.CALLER, 0xffffffffffffffffffffffffffffffffffffffff)
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.DUP2 + Op.MSTORE
        + Op.MSTORE(offset=0x20, value=0x102)
        + Op.SLOAD(key=Op.SHA3(offset=Op.DUP2, size=0x40)) + Op.SWAP1 + Op.DUP1
        + Op.DUP1 + Op.JUMPI(pc=0x191, condition=Op.ISZERO(Op.EQ(Op.DUP2, Op.DUP4)))
        + Op.JUMP(pc=0x213) + Op.JUMPDEST + Op.PUSH2[0x181]
        + Op.CALLDATALOAD(offset=0x4) + Op.PUSH1[0x40] + Op.PUSH1[0x0]
        + Op.CALLDATASIZE
        + Op.CALLDATACOPY(dest_offset=Op.DUP5, offset=Op.DUP3, size=Op.DUP1)
        + Op.SWAP1 + Op.SWAP2 + Op.SHA3 + Op.SWAP1 + Op.POP + Op.PUSH2[0x533]
        + Op.DUP2 + Op.JUMP(pc=Op.PUSH2[0x80]) + Op.JUMPDEST + Op.PUSH2[0x181]
        + Op.CALLDATALOAD(offset=0x4) + Op.CALLDATALOAD(offset=0x24) + Op.PUSH1[0x0]
        + Op.PUSH1[0x40] + Op.PUSH1[0x0] + Op.CALLDATASIZE
        + Op.CALLDATACOPY(dest_offset=Op.DUP5, offset=Op.DUP3, size=Op.DUP1)
        + Op.SWAP1 + Op.SWAP2 + Op.SHA3 + Op.SWAP1 + Op.POP + Op.PUSH2[0x286]
        + Op.DUP2 + Op.JUMP(pc=Op.PUSH2[0x80]) + Op.JUMPDEST
        + Op.RETURN(offset=0x0, size=0x0) + Op.JUMPDEST
        + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.RETURN(offset=0x0, size=0x20)
        + Op.JUMPDEST + Op.POP + Op.POP + Op.POP + Op.PUSH1[0x0]
        + Op.MSTORE(offset=Op.DUP2, value=Op.DUP3)
        + Op.MSTORE(offset=0x20, value=0x103) + Op.SHA3(offset=Op.DUP2, size=0x40)
        + Op.SLOAD(key=Op.ADD(Op.DUP2, 0x1)) + Op.PUSH1[0x2] + Op.DUP5 + Op.SWAP1
        + Op.EXP + Op.SWAP3 + Op.SWAP1 + Op.DUP4 + Op.AND + Op.DUP2 + Op.SWAP1
        + Op.JUMPI(pc=0x213, condition=Op.ISZERO(Op.GT)) + Op.SLOAD(key=Op.DUP2)
        + Op.PUSH1[0x1] + Op.ADD(Op.DUP5, Op.DUP1) + Op.SLOAD(key=Op.DUP1) + Op.SWAP2
        + Op.SWAP1 + Op.SWAP3 + Op.SSTORE(key=Op.DUP5, value=Op.ADD) + Op.DUP5
        + Op.SWAP1 + Op.SUB + Op.SWAP1 + Op.SSTORE
        + Op.AND(Op.CALLER, 0xffffffffffffffffffffffffffffffffffffffff)
        + Op.PUSH1[0x40] + Op.SWAP1 + Op.DUP2 + Op.MSTORE + Op.PUSH1[0x60] + Op.DUP7
        + Op.SWAP1 + Op.MSTORE
        + Op.PUSH32[0xc7fb647e59b18047309aa15aad418e5d7ca96d173ad704f1031a2c3d7591734b]
        + Op.SWAP1 + Op.DUP1 + Op.LOG1 + Op.JUMPDEST + Op.POP + Op.POP + Op.POP
        + Op.POP + Op.POP + Op.JUMP + Op.JUMPDEST + Op.ADD + Op.SSTORE
        + Op.PUSH20[0xffffffffffffffffffffffffffffffffffffffff]
        + Op.AND(Op.DUP2, Op.DUP5) + Op.PUSH1[0x0]
        + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2)
        + Op.MSTORE(offset=0x20, value=0x102) + Op.PUSH1[0x40]
        + Op.SHA3(offset=Op.DUP3, size=Op.DUP1) + Op.DUP3 + Op.SWAP1 + Op.SSTORE
        + Op.SWAP3 + Op.DUP7 + Op.AND + Op.MSTORE(offset=Op.DUP3, value=Op.DUP1)
        + Op.SWAP1 + Op.DUP4 + Op.SWAP1 + Op.SHA3 + Op.DUP6 + Op.SWAP1 + Op.SSTORE
        + Op.SWAP1 + Op.DUP3 + Op.MSTORE + Op.PUSH1[0x60] + Op.MSTORE
        + Op.PUSH32[0xb532073b38c83145e3e5135377a08bf9aab55bc0fd7c1179cd4fb995d2a5159c]
        + Op.SWAP1 + Op.DUP1 + Op.LOG1 + Op.JUMPDEST + Op.POP + Op.JUMPDEST + Op.POP
        + Op.POP + Op.POP + Op.JUMP + Op.JUMPDEST
        + Op.JUMPI(pc=0x27f, condition=Op.ISZERO) + Op.PUSH2[0x294] + Op.DUP4
        + Op.JUMP(pc=Op.PUSH2[0xbe]) + Op.JUMPDEST
        + Op.JUMPI(pc=0x29f, condition=Op.ISZERO) + Op.POP + Op.JUMP(pc=0x281)
        + Op.JUMPDEST + Op.AND(Op.DUP5, 0xffffffffffffffffffffffffffffffffffffffff)
        + Op.PUSH1[0x0] + Op.SWAP1 + Op.DUP2 + Op.MSTORE
        + Op.MSTORE(offset=0x20, value=0x102)
        + Op.SLOAD(key=Op.SHA3(offset=Op.DUP2, size=0x40)) + Op.SWAP3 + Op.POP
        + Op.DUP3 + Op.JUMPI(pc=0x2d5, condition=Op.ISZERO(Op.EQ)) + Op.POP
        + Op.JUMP(pc=0x281) + Op.JUMPDEST + Op.PUSH2[0x2f7] + Op.JUMPDEST
        + Op.SLOAD(key=0x104) + Op.PUSH1[0x0] + Op.JUMPDEST
        + Op.JUMPI(pc=0x80c, condition=Op.ISZERO(Op.LT(Op.DUP2, Op.DUP2)))
        + Op.PUSH2[0x104] + Op.SLOAD(key=Op.DUP1) + Op.DUP3 + Op.SWAP1 + Op.DUP2
        + Op.JUMPI(pc=0x854, condition=Op.LT) + Op.STOP + Op.JUMPDEST
        + Op.AND(Op.DUP4, 0xffffffffffffffffffffffffffffffffffffffff) + Op.PUSH1[0x2]
        + Op.DUP4 + Op.JUMPI(pc=0x21a, condition=Op.LT(Op.DUP2, 0x100)) + Op.STOP
        + Op.JUMPDEST + Op.ADD + Op.SSTORE + Op.SLOAD(key=0x1)
        + Op.AND(Op.DUP4, 0xffffffffffffffffffffffffffffffffffffffff) + Op.PUSH1[0x0]
        + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.PUSH2[0x102] + Op.PUSH1[0x20]
        + Op.SWAP1 + Op.DUP2 + Op.MSTORE + Op.PUSH1[0x40] + Op.SWAP2 + Op.DUP3
        + Op.SWAP1 + Op.SHA3 + Op.SWAP4 + Op.SWAP1 + Op.SWAP4 + Op.SSTORE + Op.SWAP1
        + Op.DUP2 + Op.MSTORE
        + Op.PUSH32[0x994a936646fe87ffe4f1e469d3d6aa417d6b855598397f323de5b449f765f0c3]
        + Op.SWAP2 + Op.SWAP1 + Op.LOG1 + Op.JUMPDEST + Op.POP + Op.JUMPDEST + Op.POP
        + Op.JUMP + Op.JUMPDEST + Op.JUMPI(pc=0x377, condition=Op.ISZERO)
        + Op.PUSH2[0x38a] + Op.DUP3 + Op.JUMP(pc=Op.PUSH2[0xbe]) + Op.JUMPDEST
        + Op.JUMPI(pc=0x395, condition=Op.ISZERO) + Op.POP + Op.JUMP(pc=0x379)
        + Op.JUMPDEST + Op.PUSH2[0x39d] + Op.JUMP(pc=0x2d9) + Op.JUMPDEST
        + Op.SLOAD(key=0x1) + Op.PUSH1[0xfa] + Op.SWAP1
        + Op.JUMPI(pc=0x3b4, condition=Op.ISZERO(Op.ISZERO(Op.LT))) + Op.PUSH2[0x3b2]
        + Op.JUMP(pc=0x3cb) + Op.JUMPDEST + Op.POP + Op.JUMPDEST + Op.SLOAD(key=0x1)
        + Op.PUSH1[0xfa] + Op.SWAP1
        + Op.JUMPI(pc=0x3f5, condition=Op.ISZERO(Op.ISZERO(Op.LT))) + Op.POP
        + Op.JUMP(pc=0x379) + Op.JUMPDEST + Op.PUSH2[0x425] + Op.JUMPDEST
        + Op.PUSH1[0x0] + Op.PUSH1[0x1] + Op.JUMPDEST
        + Op.JUMPI(pc=0x6f7, condition=Op.ISZERO(Op.LT(Op.DUP2, Op.SLOAD(key=0x1))))
        + Op.JUMPDEST + Op.LT(Op.DUP2, Op.SLOAD(key=0x1))
        + Op.JUMPI(pc=0x753, condition=Op.ISZERO(Op.DUP1)) + Op.POP + Op.PUSH1[0x2]
        + Op.DUP2 + Op.JUMPI(pc=0x74c, condition=Op.LT(Op.DUP2, 0x100)) + Op.STOP
        + Op.JUMPDEST + Op.PUSH1[0x1] + Op.ADD(Op.DUP2, Op.SLOAD(key=Op.DUP1))
        + Op.SWAP1 + Op.DUP2 + Op.SWAP1 + Op.SSTORE
        + Op.AND(Op.DUP4, 0xffffffffffffffffffffffffffffffffffffffff) + Op.SWAP1
        + Op.PUSH1[0x2] + Op.SWAP1
        + Op.JUMPI(pc=0x31c, condition=Op.LT(Op.DUP2, 0x100)) + Op.STOP + Op.JUMPDEST
        + Op.POP + Op.AND(Op.DUP4, 0xffffffffffffffffffffffffffffffffffffffff)
        + Op.PUSH1[0x40] + Op.SWAP1 + Op.DUP2 + Op.MSTORE
        + Op.PUSH32[0x58619076adf5bb0943d100ef88d52d7c3fd691b19d3a9071b555b651fbf418da]
        + Op.SWAP1 + Op.PUSH1[0x20] + Op.SWAP1 + Op.LOG1 + Op.POP + Op.POP + Op.POP
        + Op.JUMP + Op.JUMPDEST + Op.JUMPI(pc=0x281, condition=Op.ISZERO)
        + Op.AND(Op.DUP4, 0xffffffffffffffffffffffffffffffffffffffff) + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.DUP2 + Op.MSTORE + Op.MSTORE(offset=0x20, value=0x102)
        + Op.SLOAD(key=Op.SHA3(offset=Op.DUP2, size=0x40)) + Op.SWAP3 + Op.POP
        + Op.DUP3 + Op.JUMPI(pc=0x4a8, condition=Op.ISZERO(Op.EQ)) + Op.POP
        + Op.JUMP(pc=0x377) + Op.JUMPDEST + Op.PUSH1[0x1] + Op.PUSH1[0x1]
        + Op.POP(0x0) + Op.SLOAD + Op.SUB + Op.PUSH1[0x0] + Op.POP(0x0) + Op.SLOAD
        + Op.JUMPI(pc=0x4c3, condition=Op.ISZERO(Op.GT)) + Op.POP + Op.JUMP(pc=0x377)
        + Op.JUMPDEST + Op.PUSH1[0x0] + Op.PUSH1[0x2] + Op.DUP4
        + Op.JUMPI(pc=0x4d3, condition=Op.LT(Op.DUP2, 0x100)) + Op.STOP + Op.JUMPDEST
        + Op.ADD + Op.SSTORE
        + Op.AND(Op.DUP4, 0xffffffffffffffffffffffffffffffffffffffff) + Op.PUSH1[0x0]
        + Op.SWAP1 + Op.DUP2 + Op.MSTORE + Op.MSTORE(offset=0x20, value=0x102)
        + Op.SHA3(offset=Op.DUP2, size=0x40) + Op.SSTORE + Op.PUSH2[0x3c7]
        + Op.JUMP(pc=0x2d9) + Op.JUMPDEST + Op.PUSH1[0x40]
        + Op.MSTORE(offset=Op.DUP2, value=Op.DUP3)
        + Op.PUSH32[0xacbdb084c721332ac59f9b8e392196c9eb0e4932862da8eb9beaf0dad4f550da]
        + Op.SWAP1 + Op.PUSH1[0x20] + Op.SWAP1 + Op.LOG1 + Op.POP + Op.POP + Op.JUMP
        + Op.JUMPDEST + Op.JUMPI(pc=0x377, condition=Op.ISZERO)
        + Op.JUMPI(pc=0x548, condition=Op.ISZERO(Op.GT(Op.DUP3, Op.SLOAD(key=0x1))))
        + Op.POP + Op.JUMP(pc=0x379) + Op.JUMPDEST + Op.PUSH1[0x0] + Op.DUP3
        + Op.SWAP1 + Op.SSTORE + Op.PUSH2[0x504] + Op.JUMP(pc=0x2d9) + Op.JUMPDEST
        + Op.SSTORE(key=Op.DUP4, value=Op.ADD(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff, Op.SLOAD(key=Op.DUP3)))
        + Op.ADD(Op.DUP4, 0x1) + Op.OR(Op.DUP3, Op.SLOAD(key=Op.DUP1)) + Op.SWAP1
        + Op.SSTORE + Op.JUMPDEST + Op.POP + Op.POP + Op.POP + Op.POP + Op.SWAP2
        + Op.SWAP1 + Op.POP + Op.JUMP + Op.JUMPDEST + Op.PUSH1[0x0]
        + Op.MSTORE(offset=Op.DUP2, value=Op.DUP7)
        + Op.MSTORE(offset=0x20, value=0x103) + Op.SHA3(offset=Op.DUP2, size=0x40)
        + Op.SLOAD(key=Op.DUP1) + Op.SWAP1 + Op.SWAP5 + Op.POP + Op.SWAP1 + Op.SWAP3
        + Op.POP + Op.DUP3 + Op.JUMPI(pc=0x61a, condition=Op.ISZERO(Op.EQ))
        + Op.SSTORE(key=Op.DUP4, value=Op.SLOAD(key=Op.DUP2)) + Op.PUSH1[0x1]
        + Op.ADD(Op.DUP2, Op.DUP4) + Op.DUP4 + Op.SWAP1 + Op.SSTORE + Op.PUSH2[0x104]
        + Op.SLOAD(key=Op.DUP1) + Op.SWAP2 + Op.DUP3 + Op.ADD
        + Op.SSTORE(key=Op.DUP3, value=Op.DUP1) + Op.DUP3 + Op.ISZERO(Op.DUP1)
        + Op.DUP3 + Op.SWAP1 + Op.JUMPI(pc=0x6a6, condition=Op.GT)
        + Op.MSTORE(offset=Op.DUP7, value=Op.DUP3)
        + Op.PUSH32[0x4c0be60200faa20559308cb7b5a1bb3255c16cb1cab91f525b5ae7a03d02fabe]
        + Op.SWAP1 + Op.DUP2 + Op.ADD + Op.SWAP1 + Op.DUP3 + Op.ADD + Op.JUMPDEST
        + Op.JUMPI(pc=0x6a4, condition=Op.ISZERO(Op.GT(Op.DUP3, Op.DUP1)))
        + Op.SSTORE(key=Op.DUP2, value=0x0) + Op.PUSH1[0x1] + Op.ADD
        + Op.JUMP(pc=0x5f9) + Op.JUMPDEST + Op.PUSH1[0x0] + Op.SWAP2 + Op.DUP3
        + Op.MSTORE + Op.PUSH1[0x20] + Op.SWAP1 + Op.SWAP2
        + Op.SSTORE(key=Op.ADD, value=Op.SHA3) + Op.JUMPDEST + Op.POP
        + Op.SLOAD(key=Op.ADD(Op.DUP3, 0x1)) + Op.PUSH1[0x2] + Op.DUP5 + Op.SWAP1
        + Op.EXP + Op.SWAP1 + Op.DUP2
        + Op.JUMPI(pc=0x586, condition=Op.ISZERO(Op.EQ(0x0, Op.AND)))
        + Op.AND(Op.CALLER, 0xffffffffffffffffffffffffffffffffffffffff)
        + Op.PUSH1[0x40] + Op.SWAP1 + Op.DUP2 + Op.MSTORE + Op.PUSH1[0x60] + Op.DUP8
        + Op.SWAP1 + Op.MSTORE
        + Op.PUSH32[0xe1c52dc63b719ade82e8bea94cc41a0d5d28e4aaf536adb5e9cccc9ff8c1aeda]
        + Op.SWAP1 + Op.DUP1 + Op.LOG1 + Op.SLOAD(key=Op.DUP3) + Op.PUSH1[0x1]
        + Op.SWAP1 + Op.JUMPI(pc=0x555, condition=Op.ISZERO(Op.ISZERO(Op.GT)))
        + Op.PUSH1[0x0] + Op.MSTORE(offset=Op.DUP2, value=Op.DUP7)
        + Op.MSTORE(offset=0x20, value=0x103) + Op.PUSH2[0x104]
        + Op.SLOAD(key=Op.DUP1) + Op.PUSH1[0x40] + Op.SWAP1 + Op.SWAP3
        + Op.SLOAD(key=Op.ADD(0x2, Op.SHA3)) + Op.SWAP1 + Op.SWAP2 + Op.DUP2
        + Op.JUMPI(pc=0x6c0, condition=Op.LT) + Op.STOP + Op.JUMPDEST + Op.POP
        + Op.JUMPDEST + Op.POP + Op.POP + Op.POP + Op.ADD(Op.DUP5, 0x2) + Op.DUP2
        + Op.SWAP1 + Op.SSTORE + Op.PUSH2[0x104] + Op.SLOAD(key=Op.DUP1) + Op.DUP9
        + Op.SWAP3 + Op.SWAP1 + Op.DUP2 + Op.JUMPI(pc=0x60d, condition=Op.LT)
        + Op.STOP + Op.JUMPDEST + Op.PUSH1[0x0] + Op.SWAP2 + Op.DUP3 + Op.MSTORE
        + Op.PUSH1[0x20] + Op.SHA3(offset=Op.DUP4, size=Op.DUP1) + Op.SWAP1 + Op.SWAP2
        + Op.ADD + Op.DUP3 + Op.SWAP1 + Op.SSTORE
        + Op.MSTORE(offset=Op.DUP3, value=Op.DUP8) + Op.PUSH2[0x103] + Op.SWAP1
        + Op.MSTORE + Op.SHA3(offset=Op.DUP2, size=0x40)
        + Op.SSTORE(key=Op.DUP2, value=Op.DUP2) + Op.PUSH1[0x1]
        + Op.ADD(Op.DUP2, Op.DUP2) + Op.DUP4 + Op.SWAP1 + Op.SSTORE + Op.PUSH1[0x2]
        + Op.SWAP1 + Op.SWAP2 + Op.ADD + Op.SWAP2 + Op.SWAP1 + Op.SWAP2 + Op.SSTORE
        + Op.SWAP5 + Op.POP + Op.JUMP(pc=0x586) + Op.JUMPDEST + Op.POP + Op.SWAP1
        + Op.JUMP + Op.JUMPDEST + Op.EQ(0x0, Op.SLOAD(key=Op.ADD)) + Op.JUMPDEST
        + Op.JUMPI(pc=0x760, condition=Op.ISZERO) + Op.PUSH1[0x1]
        + Op.ADD(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff, Op.SLOAD(key=Op.DUP1))
        + Op.SWAP1 + Op.SSTORE + Op.JUMPDEST + Op.GT(Op.SLOAD(key=Op.DUP1), 0x1)
        + Op.JUMPI(pc=0x701, condition=Op.ISZERO(Op.DUP1)) + Op.POP
        + Op.SLOAD(key=0x1) + Op.PUSH1[0x2] + Op.SWAP1
        + Op.JUMPI(pc=0x6fb, condition=Op.LT(Op.DUP2, 0x100)) + Op.STOP + Op.JUMPDEST
        + Op.ISZERO(Op.EQ(0x0, Op.SLOAD(key=Op.ADD))) + Op.JUMPDEST
        + Op.JUMPI(pc=0x72f, condition=Op.ISZERO) + Op.PUSH1[0x1] + Op.ADD
        + Op.JUMP(pc=0x3db) + Op.JUMPDEST + Op.LT(Op.DUP2, Op.SLOAD(key=0x1))
        + Op.JUMPI(pc=0x784, condition=Op.ISZERO(Op.DUP1)) + Op.POP
        + Op.SLOAD(key=0x1) + Op.PUSH1[0x2] + Op.SWAP1
        + Op.JUMPI(pc=0x77d, condition=Op.LT(Op.DUP2, 0x100)) + Op.STOP + Op.JUMPDEST
        + Op.ISZERO(Op.EQ(0x0, Op.SLOAD(key=Op.ADD))) + Op.JUMPDEST
        + Op.JUMPI(pc=0x79f, condition=Op.ISZERO(Op.DUP1)) + Op.POP + Op.PUSH1[0x2]
        + Op.DUP2 + Op.JUMPI(pc=0x799, condition=Op.LT(Op.DUP2, 0x100)) + Op.STOP
        + Op.JUMPDEST + Op.EQ(0x0, Op.SLOAD(key=Op.ADD)) + Op.JUMPDEST
        + Op.JUMPI(pc=0x7b8, condition=Op.ISZERO) + Op.SLOAD(key=0x1) + Op.PUSH1[0x2]
        + Op.SWAP1 + Op.JUMPI(pc=0x7bd, condition=Op.LT(Op.DUP2, 0x100)) + Op.STOP
        + Op.JUMPDEST + Op.ADD + Op.SSTORE + Op.JUMPDEST + Op.JUMP(pc=0x3d0)
        + Op.JUMPDEST + Op.SLOAD(key=Op.ADD) + Op.PUSH1[0x2] + Op.DUP3
        + Op.JUMPI(pc=0x7cd, condition=Op.LT(Op.DUP2, 0x100)) + Op.STOP + Op.JUMPDEST
        + Op.ADD + Op.SSTORE + Op.DUP1 + Op.PUSH2[0x102] + Op.PUSH1[0x0]
        + Op.PUSH1[0x2] + Op.DUP4
        + Op.JUMPI(pc=0x7e3, condition=Op.LT(Op.DUP2, 0x100)) + Op.STOP + Op.JUMPDEST
        + Op.MSTORE(offset=Op.DUP2, value=Op.SLOAD(key=Op.ADD))
        + Op.ADD(Op.DUP2, 0x20) + Op.SWAP2 + Op.SWAP1 + Op.SWAP2 + Op.MSTORE
        + Op.PUSH1[0x40] + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.DUP2 + Op.SHA3
        + Op.SWAP2 + Op.SWAP1 + Op.SWAP2 + Op.SSTORE + Op.SLOAD(key=0x1)
        + Op.PUSH1[0x2] + Op.SWAP1
        + Op.JUMPI(pc=0x7b5, condition=Op.LT(Op.DUP2, 0x100)) + Op.STOP + Op.JUMPDEST
        + Op.PUSH2[0x104] + Op.SLOAD(key=Op.DUP1) + Op.PUSH1[0x0]
        + Op.SSTORE(key=Op.DUP4, value=Op.DUP1) + Op.SWAP2 + Op.SWAP1 + Op.SWAP2
        + Op.MSTORE
        + Op.PUSH32[0x4c0be60200faa20559308cb7b5a1bb3255c16cb1cab91f525b5ae7a03d02fabe]
        + Op.SWAP1 + Op.DUP2 + Op.ADD + Op.SWAP1 + Op.JUMPDEST
        + Op.JUMPI(pc=0x27f, condition=Op.ISZERO(Op.GT(Op.DUP3, Op.DUP1)))
        + Op.SSTORE(key=Op.DUP2, value=0x0) + Op.PUSH1[0x1] + Op.ADD
        + Op.JUMP(pc=0x840) + Op.JUMPDEST + Op.PUSH1[0x0] + Op.SWAP2 + Op.DUP3
        + Op.MSTORE
        + Op.JUMPI(pc=0x8a6, condition=Op.ISZERO(Op.ISZERO(Op.EQ(Op.SLOAD(key=Op.ADD), Op.SHA3(offset=Op.DUP3, size=0x20)))))
        + Op.PUSH2[0x104] + Op.SLOAD(key=Op.DUP1) + Op.PUSH2[0x103] + Op.SWAP2
        + Op.PUSH1[0x0] + Op.SWAP2 + Op.DUP5 + Op.SWAP1 + Op.DUP2
        + Op.JUMPI(pc=0x87c, condition=Op.LT) + Op.STOP + Op.JUMPDEST + Op.PUSH1[0x0]
        + Op.SWAP2 + Op.DUP3 + Op.MSTORE + Op.PUSH1[0x20]
        + Op.SHA3(offset=Op.DUP4, size=Op.DUP1) + Op.SWAP1 + Op.SWAP2
        + Op.MSTORE(offset=Op.DUP4, value=Op.SLOAD(key=Op.ADD)) + Op.DUP3 + Op.ADD
        + Op.SWAP3 + Op.SWAP1 + Op.SWAP3 + Op.MSTORE + Op.PUSH1[0x40]
        + Op.SHA3(offset=Op.DUP2, size=Op.ADD) + Op.SSTORE(key=Op.DUP2, value=Op.DUP2)
        + Op.ADD(Op.DUP2, 0x1) + Op.DUP3 + Op.SWAP1 + Op.SSTORE
        + Op.SSTORE(key=Op.ADD, value=0x2) + Op.JUMPDEST + Op.PUSH1[0x1] + Op.ADD
        + Op.JUMP(pc=0x2e0)
    ),
        storage={0x0: 0x1, 0x1: 0x2, 0x3: 0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b, 0x4: 0x3fb1cd2cd96c6d5c0b5eb3322d807b34482481d4, 0x6e369836487c234b9e553ef3f787c2d8865520739d340c67b3d251a33986e58d: 0x1, 0xd3e69d8c7f41f7aeaf8130ddc53047aeee8cb46a73d6bae86b7e7d6bf8312e6b: 0x2},
    )
    pre[sender] = Account(balance=0xde0b6b3a75ef08f, nonce=1)

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=bytes.fromhex("173825d9000000000000000000000000a94f5374fce5edbc8e2a8697c15331677e6ebf0b"),
        gas_limit=10000000,
        gas_price=10,
        nonce=1,
        value=100,
    )

    post = {
        contract: Account(
            storage={0: 1, 1: 1, 3: 0x3fb1cd2cd96c6d5c0b5eb3322d807b34482481d4, 0xd3e69d8c7f41f7aeaf8130ddc53047aeee8cb46a73d6bae86b7e7d6bf8312e6b: 1},
            code=Op.DIV(Op.CALLDATALOAD(offset=0x0), 0x100000000000000000000000000000000000000000000000000000000) + Op.JUMPI(pc=Op.PUSH2[0x65], condition=Op.EQ(Op.DUP2, 0x173825d9)) + Op.JUMPI(pc=Op.PUSH2[0xb7], condition=Op.EQ(0x2f54bf6e, Op.DUP1)) + Op.JUMPI(pc=Op.PUSH2[0xe8], condition=Op.EQ(0x7065cb48, Op.DUP1)) + Op.JUMPI(pc=0x105, condition=Op.EQ(0xb75c7dc6, Op.DUP1)) + Op.JUMPI(pc=0x142, condition=Op.EQ(0xba51a6df, Op.DUP1)) + Op.JUMPI(pc=0x15f, condition=Op.EQ(0xf00d4b5d, Op.DUP1)) + Op.STOP + Op.JUMPDEST + Op.PUSH2[0x181] + Op.CALLDATALOAD(offset=0x4) + Op.PUSH1[0x0] + Op.PUSH1[0x40] + Op.PUSH1[0x0] + Op.CALLDATASIZE + Op.CALLDATACOPY(dest_offset=Op.DUP5, offset=Op.DUP3, size=Op.DUP1) + Op.SWAP1 + Op.SWAP2 + Op.SHA3 + Op.SWAP1 + Op.POP + Op.PUSH2[0x46d] + Op.DUP2 + Op.JUMPDEST + Op.AND(Op.CALLER, 0xffffffffffffffffffffffffffffffffffffffff) + Op.PUSH1[0x0] + Op.SWAP1 + Op.DUP2 + Op.MSTORE + Op.MSTORE(offset=0x20, value=0x102) + Op.SLOAD(key=Op.SHA3(offset=Op.DUP2, size=0x40)) + Op.DUP2 + Op.DUP1 + Op.DUP1 + Op.JUMPI(pc=0x58f, condition=Op.ISZERO(Op.EQ(Op.DUP2, Op.DUP4))) + Op.JUMP(pc=0x586) + Op.JUMPDEST + Op.PUSH2[0x187] + Op.CALLDATALOAD(offset=0x4) + Op.JUMPDEST + Op.PUSH20[0xffffffffffffffffffffffffffffffffffffffff] + Op.AND + Op.PUSH1[0x0] + Op.SWAP1 + Op.DUP2 + Op.MSTORE + Op.MSTORE(offset=0x20, value=0x102) + Op.SLOAD(key=Op.SHA3(offset=Op.DUP2, size=0x40)) + Op.GT + Op.SWAP1 + Op.JUMP + Op.JUMPDEST + Op.PUSH2[0x181] + Op.CALLDATALOAD(offset=0x4) + Op.PUSH1[0x40] + Op.PUSH1[0x0] + Op.CALLDATASIZE + Op.CALLDATACOPY(dest_offset=Op.DUP5, offset=Op.DUP3, size=Op.DUP1) + Op.SWAP1 + Op.SWAP2 + Op.SHA3 + Op.SWAP1 + Op.POP + Op.PUSH2[0x37c] + Op.DUP2 + Op.JUMP(pc=Op.PUSH2[0x80]) + Op.JUMPDEST + Op.PUSH2[0x181] + Op.CALLDATALOAD(offset=0x4) + Op.AND(Op.CALLER, 0xffffffffffffffffffffffffffffffffffffffff) + Op.PUSH1[0x0] + Op.SWAP1 + Op.DUP2 + Op.MSTORE + Op.MSTORE(offset=0x20, value=0x102) + Op.SLOAD(key=Op.SHA3(offset=Op.DUP2, size=0x40)) + Op.SWAP1 + Op.DUP1 + Op.DUP1 + Op.JUMPI(pc=0x191, condition=Op.ISZERO(Op.EQ(Op.DUP2, Op.DUP4))) + Op.JUMP(pc=0x213) + Op.JUMPDEST + Op.PUSH2[0x181] + Op.CALLDATALOAD(offset=0x4) + Op.PUSH1[0x40] + Op.PUSH1[0x0] + Op.CALLDATASIZE + Op.CALLDATACOPY(dest_offset=Op.DUP5, offset=Op.DUP3, size=Op.DUP1) + Op.SWAP1 + Op.SWAP2 + Op.SHA3 + Op.SWAP1 + Op.POP + Op.PUSH2[0x533] + Op.DUP2 + Op.JUMP(pc=Op.PUSH2[0x80]) + Op.JUMPDEST + Op.PUSH2[0x181] + Op.CALLDATALOAD(offset=0x4) + Op.CALLDATALOAD(offset=0x24) + Op.PUSH1[0x0] + Op.PUSH1[0x40] + Op.PUSH1[0x0] + Op.CALLDATASIZE + Op.CALLDATACOPY(dest_offset=Op.DUP5, offset=Op.DUP3, size=Op.DUP1) + Op.SWAP1 + Op.SWAP2 + Op.SHA3 + Op.SWAP1 + Op.POP + Op.PUSH2[0x286] + Op.DUP2 + Op.JUMP(pc=Op.PUSH2[0x80]) + Op.JUMPDEST + Op.RETURN(offset=0x0, size=0x0) + Op.JUMPDEST + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.RETURN(offset=0x0, size=0x20) + Op.JUMPDEST + Op.POP + Op.POP + Op.POP + Op.PUSH1[0x0] + Op.MSTORE(offset=Op.DUP2, value=Op.DUP3) + Op.MSTORE(offset=0x20, value=0x103) + Op.SHA3(offset=Op.DUP2, size=0x40) + Op.SLOAD(key=Op.ADD(Op.DUP2, 0x1)) + Op.PUSH1[0x2] + Op.DUP5 + Op.SWAP1 + Op.EXP + Op.SWAP3 + Op.SWAP1 + Op.DUP4 + Op.AND + Op.DUP2 + Op.SWAP1 + Op.JUMPI(pc=0x213, condition=Op.ISZERO(Op.GT)) + Op.SLOAD(key=Op.DUP2) + Op.PUSH1[0x1] + Op.ADD(Op.DUP5, Op.DUP1) + Op.SLOAD(key=Op.DUP1) + Op.SWAP2 + Op.SWAP1 + Op.SWAP3 + Op.SSTORE(key=Op.DUP5, value=Op.ADD) + Op.DUP5 + Op.SWAP1 + Op.SUB + Op.SWAP1 + Op.SSTORE + Op.AND(Op.CALLER, 0xffffffffffffffffffffffffffffffffffffffff) + Op.PUSH1[0x40] + Op.SWAP1 + Op.DUP2 + Op.MSTORE + Op.PUSH1[0x60] + Op.DUP7 + Op.SWAP1 + Op.MSTORE + Op.PUSH32[0xc7fb647e59b18047309aa15aad418e5d7ca96d173ad704f1031a2c3d7591734b] + Op.SWAP1 + Op.DUP1 + Op.LOG1 + Op.JUMPDEST + Op.POP + Op.POP + Op.POP + Op.POP + Op.POP + Op.JUMP + Op.JUMPDEST + Op.ADD + Op.SSTORE + Op.PUSH20[0xffffffffffffffffffffffffffffffffffffffff] + Op.AND(Op.DUP2, Op.DUP5) + Op.PUSH1[0x0] + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.MSTORE(offset=0x20, value=0x102) + Op.PUSH1[0x40] + Op.SHA3(offset=Op.DUP3, size=Op.DUP1) + Op.DUP3 + Op.SWAP1 + Op.SSTORE + Op.SWAP3 + Op.DUP7 + Op.AND + Op.MSTORE(offset=Op.DUP3, value=Op.DUP1) + Op.SWAP1 + Op.DUP4 + Op.SWAP1 + Op.SHA3 + Op.DUP6 + Op.SWAP1 + Op.SSTORE + Op.SWAP1 + Op.DUP3 + Op.MSTORE + Op.PUSH1[0x60] + Op.MSTORE + Op.PUSH32[0xb532073b38c83145e3e5135377a08bf9aab55bc0fd7c1179cd4fb995d2a5159c] + Op.SWAP1 + Op.DUP1 + Op.LOG1 + Op.JUMPDEST + Op.POP + Op.JUMPDEST + Op.POP + Op.POP + Op.POP + Op.JUMP + Op.JUMPDEST + Op.JUMPI(pc=0x27f, condition=Op.ISZERO) + Op.PUSH2[0x294] + Op.DUP4 + Op.JUMP(pc=Op.PUSH2[0xbe]) + Op.JUMPDEST + Op.JUMPI(pc=0x29f, condition=Op.ISZERO) + Op.POP + Op.JUMP(pc=0x281) + Op.JUMPDEST + Op.AND(Op.DUP5, 0xffffffffffffffffffffffffffffffffffffffff) + Op.PUSH1[0x0] + Op.SWAP1 + Op.DUP2 + Op.MSTORE + Op.MSTORE(offset=0x20, value=0x102) + Op.SLOAD(key=Op.SHA3(offset=Op.DUP2, size=0x40)) + Op.SWAP3 + Op.POP + Op.DUP3 + Op.JUMPI(pc=0x2d5, condition=Op.ISZERO(Op.EQ)) + Op.POP + Op.JUMP(pc=0x281) + Op.JUMPDEST + Op.PUSH2[0x2f7] + Op.JUMPDEST + Op.SLOAD(key=0x104) + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPI(pc=0x80c, condition=Op.ISZERO(Op.LT(Op.DUP2, Op.DUP2))) + Op.PUSH2[0x104] + Op.SLOAD(key=Op.DUP1) + Op.DUP3 + Op.SWAP1 + Op.DUP2 + Op.JUMPI(pc=0x854, condition=Op.LT) + Op.STOP + Op.JUMPDEST + Op.AND(Op.DUP4, 0xffffffffffffffffffffffffffffffffffffffff) + Op.PUSH1[0x2] + Op.DUP4 + Op.JUMPI(pc=0x21a, condition=Op.LT(Op.DUP2, 0x100)) + Op.STOP + Op.JUMPDEST + Op.ADD + Op.SSTORE + Op.SLOAD(key=0x1) + Op.AND(Op.DUP4, 0xffffffffffffffffffffffffffffffffffffffff) + Op.PUSH1[0x0] + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2) + Op.PUSH2[0x102] + Op.PUSH1[0x20] + Op.SWAP1 + Op.DUP2 + Op.MSTORE + Op.PUSH1[0x40] + Op.SWAP2 + Op.DUP3 + Op.SWAP1 + Op.SHA3 + Op.SWAP4 + Op.SWAP1 + Op.SWAP4 + Op.SSTORE + Op.SWAP1 + Op.DUP2 + Op.MSTORE + Op.PUSH32[0x994a936646fe87ffe4f1e469d3d6aa417d6b855598397f323de5b449f765f0c3] + Op.SWAP2 + Op.SWAP1 + Op.LOG1 + Op.JUMPDEST + Op.POP + Op.JUMPDEST + Op.POP + Op.JUMP + Op.JUMPDEST + Op.JUMPI(pc=0x377, condition=Op.ISZERO) + Op.PUSH2[0x38a] + Op.DUP3 + Op.JUMP(pc=Op.PUSH2[0xbe]) + Op.JUMPDEST + Op.JUMPI(pc=0x395, condition=Op.ISZERO) + Op.POP + Op.JUMP(pc=0x379) + Op.JUMPDEST + Op.PUSH2[0x39d] + Op.JUMP(pc=0x2d9) + Op.JUMPDEST + Op.SLOAD(key=0x1) + Op.PUSH1[0xfa] + Op.SWAP1 + Op.JUMPI(pc=0x3b4, condition=Op.ISZERO(Op.ISZERO(Op.LT))) + Op.PUSH2[0x3b2] + Op.JUMP(pc=0x3cb) + Op.JUMPDEST + Op.POP + Op.JUMPDEST + Op.SLOAD(key=0x1) + Op.PUSH1[0xfa] + Op.SWAP1 + Op.JUMPI(pc=0x3f5, condition=Op.ISZERO(Op.ISZERO(Op.LT))) + Op.POP + Op.JUMP(pc=0x379) + Op.JUMPDEST + Op.PUSH2[0x425] + Op.JUMPDEST + Op.PUSH1[0x0] + Op.PUSH1[0x1] + Op.JUMPDEST + Op.JUMPI(pc=0x6f7, condition=Op.ISZERO(Op.LT(Op.DUP2, Op.SLOAD(key=0x1)))) + Op.JUMPDEST + Op.LT(Op.DUP2, Op.SLOAD(key=0x1)) + Op.JUMPI(pc=0x753, condition=Op.ISZERO(Op.DUP1)) + Op.POP + Op.PUSH1[0x2] + Op.DUP2 + Op.JUMPI(pc=0x74c, condition=Op.LT(Op.DUP2, 0x100)) + Op.STOP + Op.JUMPDEST + Op.PUSH1[0x1] + Op.ADD(Op.DUP2, Op.SLOAD(key=Op.DUP1)) + Op.SWAP1 + Op.DUP2 + Op.SWAP1 + Op.SSTORE + Op.AND(Op.DUP4, 0xffffffffffffffffffffffffffffffffffffffff) + Op.SWAP1 + Op.PUSH1[0x2] + Op.SWAP1 + Op.JUMPI(pc=0x31c, condition=Op.LT(Op.DUP2, 0x100)) + Op.STOP + Op.JUMPDEST + Op.POP + Op.AND(Op.DUP4, 0xffffffffffffffffffffffffffffffffffffffff) + Op.PUSH1[0x40] + Op.SWAP1 + Op.DUP2 + Op.MSTORE + Op.PUSH32[0x58619076adf5bb0943d100ef88d52d7c3fd691b19d3a9071b555b651fbf418da] + Op.SWAP1 + Op.PUSH1[0x20] + Op.SWAP1 + Op.LOG1 + Op.POP + Op.POP + Op.POP + Op.JUMP + Op.JUMPDEST + Op.JUMPI(pc=0x281, condition=Op.ISZERO) + Op.AND(Op.DUP4, 0xffffffffffffffffffffffffffffffffffffffff) + Op.PUSH1[0x0] + Op.SWAP1 + Op.DUP2 + Op.MSTORE + Op.MSTORE(offset=0x20, value=0x102) + Op.SLOAD(key=Op.SHA3(offset=Op.DUP2, size=0x40)) + Op.SWAP3 + Op.POP + Op.DUP3 + Op.JUMPI(pc=0x4a8, condition=Op.ISZERO(Op.EQ)) + Op.POP + Op.JUMP(pc=0x377) + Op.JUMPDEST + Op.PUSH1[0x1] + Op.PUSH1[0x1] + Op.POP(0x0) + Op.SLOAD + Op.SUB + Op.PUSH1[0x0] + Op.POP(0x0) + Op.SLOAD + Op.JUMPI(pc=0x4c3, condition=Op.ISZERO(Op.GT)) + Op.POP + Op.JUMP(pc=0x377) + Op.JUMPDEST + Op.PUSH1[0x0] + Op.PUSH1[0x2] + Op.DUP4 + Op.JUMPI(pc=0x4d3, condition=Op.LT(Op.DUP2, 0x100)) + Op.STOP + Op.JUMPDEST + Op.ADD + Op.SSTORE + Op.AND(Op.DUP4, 0xffffffffffffffffffffffffffffffffffffffff) + Op.PUSH1[0x0] + Op.SWAP1 + Op.DUP2 + Op.MSTORE + Op.MSTORE(offset=0x20, value=0x102) + Op.SHA3(offset=Op.DUP2, size=0x40) + Op.SSTORE + Op.PUSH2[0x3c7] + Op.JUMP(pc=0x2d9) + Op.JUMPDEST + Op.PUSH1[0x40] + Op.MSTORE(offset=Op.DUP2, value=Op.DUP3) + Op.PUSH32[0xacbdb084c721332ac59f9b8e392196c9eb0e4932862da8eb9beaf0dad4f550da] + Op.SWAP1 + Op.PUSH1[0x20] + Op.SWAP1 + Op.LOG1 + Op.POP + Op.POP + Op.JUMP + Op.JUMPDEST + Op.JUMPI(pc=0x377, condition=Op.ISZERO) + Op.JUMPI(pc=0x548, condition=Op.ISZERO(Op.GT(Op.DUP3, Op.SLOAD(key=0x1)))) + Op.POP + Op.JUMP(pc=0x379) + Op.JUMPDEST + Op.PUSH1[0x0] + Op.DUP3 + Op.SWAP1 + Op.SSTORE + Op.PUSH2[0x504] + Op.JUMP(pc=0x2d9) + Op.JUMPDEST + Op.SSTORE(key=Op.DUP4, value=Op.ADD(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff, Op.SLOAD(key=Op.DUP3))) + Op.ADD(Op.DUP4, 0x1) + Op.OR(Op.DUP3, Op.SLOAD(key=Op.DUP1)) + Op.SWAP1 + Op.SSTORE + Op.JUMPDEST + Op.POP + Op.POP + Op.POP + Op.POP + Op.SWAP2 + Op.SWAP1 + Op.POP + Op.JUMP + Op.JUMPDEST + Op.PUSH1[0x0] + Op.MSTORE(offset=Op.DUP2, value=Op.DUP7) + Op.MSTORE(offset=0x20, value=0x103) + Op.SHA3(offset=Op.DUP2, size=0x40) + Op.SLOAD(key=Op.DUP1) + Op.SWAP1 + Op.SWAP5 + Op.POP + Op.SWAP1 + Op.SWAP3 + Op.POP + Op.DUP3 + Op.JUMPI(pc=0x61a, condition=Op.ISZERO(Op.EQ)) + Op.SSTORE(key=Op.DUP4, value=Op.SLOAD(key=Op.DUP2)) + Op.PUSH1[0x1] + Op.ADD(Op.DUP2, Op.DUP4) + Op.DUP4 + Op.SWAP1 + Op.SSTORE + Op.PUSH2[0x104] + Op.SLOAD(key=Op.DUP1) + Op.SWAP2 + Op.DUP3 + Op.ADD + Op.SSTORE(key=Op.DUP3, value=Op.DUP1) + Op.DUP3 + Op.ISZERO(Op.DUP1) + Op.DUP3 + Op.SWAP1 + Op.JUMPI(pc=0x6a6, condition=Op.GT) + Op.MSTORE(offset=Op.DUP7, value=Op.DUP3) + Op.PUSH32[0x4c0be60200faa20559308cb7b5a1bb3255c16cb1cab91f525b5ae7a03d02fabe] + Op.SWAP1 + Op.DUP2 + Op.ADD + Op.SWAP1 + Op.DUP3 + Op.ADD + Op.JUMPDEST + Op.JUMPI(pc=0x6a4, condition=Op.ISZERO(Op.GT(Op.DUP3, Op.DUP1))) + Op.SSTORE(key=Op.DUP2, value=0x0) + Op.PUSH1[0x1] + Op.ADD + Op.JUMP(pc=0x5f9) + Op.JUMPDEST + Op.PUSH1[0x0] + Op.SWAP2 + Op.DUP3 + Op.MSTORE + Op.PUSH1[0x20] + Op.SWAP1 + Op.SWAP2 + Op.SSTORE(key=Op.ADD, value=Op.SHA3) + Op.JUMPDEST + Op.POP + Op.SLOAD(key=Op.ADD(Op.DUP3, 0x1)) + Op.PUSH1[0x2] + Op.DUP5 + Op.SWAP1 + Op.EXP + Op.SWAP1 + Op.DUP2 + Op.JUMPI(pc=0x586, condition=Op.ISZERO(Op.EQ(0x0, Op.AND))) + Op.AND(Op.CALLER, 0xffffffffffffffffffffffffffffffffffffffff) + Op.PUSH1[0x40] + Op.SWAP1 + Op.DUP2 + Op.MSTORE + Op.PUSH1[0x60] + Op.DUP8 + Op.SWAP1 + Op.MSTORE + Op.PUSH32[0xe1c52dc63b719ade82e8bea94cc41a0d5d28e4aaf536adb5e9cccc9ff8c1aeda] + Op.SWAP1 + Op.DUP1 + Op.LOG1 + Op.SLOAD(key=Op.DUP3) + Op.PUSH1[0x1] + Op.SWAP1 + Op.JUMPI(pc=0x555, condition=Op.ISZERO(Op.ISZERO(Op.GT))) + Op.PUSH1[0x0] + Op.MSTORE(offset=Op.DUP2, value=Op.DUP7) + Op.MSTORE(offset=0x20, value=0x103) + Op.PUSH2[0x104] + Op.SLOAD(key=Op.DUP1) + Op.PUSH1[0x40] + Op.SWAP1 + Op.SWAP3 + Op.SLOAD(key=Op.ADD(0x2, Op.SHA3)) + Op.SWAP1 + Op.SWAP2 + Op.DUP2 + Op.JUMPI(pc=0x6c0, condition=Op.LT) + Op.STOP + Op.JUMPDEST + Op.POP + Op.JUMPDEST + Op.POP + Op.POP + Op.POP + Op.ADD(Op.DUP5, 0x2) + Op.DUP2 + Op.SWAP1 + Op.SSTORE + Op.PUSH2[0x104] + Op.SLOAD(key=Op.DUP1) + Op.DUP9 + Op.SWAP3 + Op.SWAP1 + Op.DUP2 + Op.JUMPI(pc=0x60d, condition=Op.LT) + Op.STOP + Op.JUMPDEST + Op.PUSH1[0x0] + Op.SWAP2 + Op.DUP3 + Op.MSTORE + Op.PUSH1[0x20] + Op.SHA3(offset=Op.DUP4, size=Op.DUP1) + Op.SWAP1 + Op.SWAP2 + Op.ADD + Op.DUP3 + Op.SWAP1 + Op.SSTORE + Op.MSTORE(offset=Op.DUP3, value=Op.DUP8) + Op.PUSH2[0x103] + Op.SWAP1 + Op.MSTORE + Op.SHA3(offset=Op.DUP2, size=0x40) + Op.SSTORE(key=Op.DUP2, value=Op.DUP2) + Op.PUSH1[0x1] + Op.ADD(Op.DUP2, Op.DUP2) + Op.DUP4 + Op.SWAP1 + Op.SSTORE + Op.PUSH1[0x2] + Op.SWAP1 + Op.SWAP2 + Op.ADD + Op.SWAP2 + Op.SWAP1 + Op.SWAP2 + Op.SSTORE + Op.SWAP5 + Op.POP + Op.JUMP(pc=0x586) + Op.JUMPDEST + Op.POP + Op.SWAP1 + Op.JUMP + Op.JUMPDEST + Op.EQ(0x0, Op.SLOAD(key=Op.ADD)) + Op.JUMPDEST + Op.JUMPI(pc=0x760, condition=Op.ISZERO) + Op.PUSH1[0x1] + Op.ADD(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff, Op.SLOAD(key=Op.DUP1)) + Op.SWAP1 + Op.SSTORE + Op.JUMPDEST + Op.GT(Op.SLOAD(key=Op.DUP1), 0x1) + Op.JUMPI(pc=0x701, condition=Op.ISZERO(Op.DUP1)) + Op.POP + Op.SLOAD(key=0x1) + Op.PUSH1[0x2] + Op.SWAP1 + Op.JUMPI(pc=0x6fb, condition=Op.LT(Op.DUP2, 0x100)) + Op.STOP + Op.JUMPDEST + Op.ISZERO(Op.EQ(0x0, Op.SLOAD(key=Op.ADD))) + Op.JUMPDEST + Op.JUMPI(pc=0x72f, condition=Op.ISZERO) + Op.PUSH1[0x1] + Op.ADD + Op.JUMP(pc=0x3db) + Op.JUMPDEST + Op.LT(Op.DUP2, Op.SLOAD(key=0x1)) + Op.JUMPI(pc=0x784, condition=Op.ISZERO(Op.DUP1)) + Op.POP + Op.SLOAD(key=0x1) + Op.PUSH1[0x2] + Op.SWAP1 + Op.JUMPI(pc=0x77d, condition=Op.LT(Op.DUP2, 0x100)) + Op.STOP + Op.JUMPDEST + Op.ISZERO(Op.EQ(0x0, Op.SLOAD(key=Op.ADD))) + Op.JUMPDEST + Op.JUMPI(pc=0x79f, condition=Op.ISZERO(Op.DUP1)) + Op.POP + Op.PUSH1[0x2] + Op.DUP2 + Op.JUMPI(pc=0x799, condition=Op.LT(Op.DUP2, 0x100)) + Op.STOP + Op.JUMPDEST + Op.EQ(0x0, Op.SLOAD(key=Op.ADD)) + Op.JUMPDEST + Op.JUMPI(pc=0x7b8, condition=Op.ISZERO) + Op.SLOAD(key=0x1) + Op.PUSH1[0x2] + Op.SWAP1 + Op.JUMPI(pc=0x7bd, condition=Op.LT(Op.DUP2, 0x100)) + Op.STOP + Op.JUMPDEST + Op.ADD + Op.SSTORE + Op.JUMPDEST + Op.JUMP(pc=0x3d0) + Op.JUMPDEST + Op.SLOAD(key=Op.ADD) + Op.PUSH1[0x2] + Op.DUP3 + Op.JUMPI(pc=0x7cd, condition=Op.LT(Op.DUP2, 0x100)) + Op.STOP + Op.JUMPDEST + Op.ADD + Op.SSTORE + Op.DUP1 + Op.PUSH2[0x102] + Op.PUSH1[0x0] + Op.PUSH1[0x2] + Op.DUP4 + Op.JUMPI(pc=0x7e3, condition=Op.LT(Op.DUP2, 0x100)) + Op.STOP + Op.JUMPDEST + Op.MSTORE(offset=Op.DUP2, value=Op.SLOAD(key=Op.ADD)) + Op.ADD(Op.DUP2, 0x20) + Op.SWAP2 + Op.SWAP1 + Op.SWAP2 + Op.MSTORE + Op.PUSH1[0x40] + Op.ADD + Op.PUSH1[0x0] + Op.SWAP1 + Op.DUP2 + Op.SHA3 + Op.SWAP2 + Op.SWAP1 + Op.SWAP2 + Op.SSTORE + Op.SLOAD(key=0x1) + Op.PUSH1[0x2] + Op.SWAP1 + Op.JUMPI(pc=0x7b5, condition=Op.LT(Op.DUP2, 0x100)) + Op.STOP + Op.JUMPDEST + Op.PUSH2[0x104] + Op.SLOAD(key=Op.DUP1) + Op.PUSH1[0x0] + Op.SSTORE(key=Op.DUP4, value=Op.DUP1) + Op.SWAP2 + Op.SWAP1 + Op.SWAP2 + Op.MSTORE + Op.PUSH32[0x4c0be60200faa20559308cb7b5a1bb3255c16cb1cab91f525b5ae7a03d02fabe] + Op.SWAP1 + Op.DUP2 + Op.ADD + Op.SWAP1 + Op.JUMPDEST + Op.JUMPI(pc=0x27f, condition=Op.ISZERO(Op.GT(Op.DUP3, Op.DUP1))) + Op.SSTORE(key=Op.DUP2, value=0x0) + Op.PUSH1[0x1] + Op.ADD + Op.JUMP(pc=0x840) + Op.JUMPDEST + Op.PUSH1[0x0] + Op.SWAP2 + Op.DUP3 + Op.MSTORE + Op.JUMPI(pc=0x8a6, condition=Op.ISZERO(Op.ISZERO(Op.EQ(Op.SLOAD(key=Op.ADD), Op.SHA3(offset=Op.DUP3, size=0x20))))) + Op.PUSH2[0x104] + Op.SLOAD(key=Op.DUP1) + Op.PUSH2[0x103] + Op.SWAP2 + Op.PUSH1[0x0] + Op.SWAP2 + Op.DUP5 + Op.SWAP1 + Op.DUP2 + Op.JUMPI(pc=0x87c, condition=Op.LT) + Op.STOP + Op.JUMPDEST + Op.PUSH1[0x0] + Op.SWAP2 + Op.DUP3 + Op.MSTORE + Op.PUSH1[0x20] + Op.SHA3(offset=Op.DUP4, size=Op.DUP1) + Op.SWAP1 + Op.SWAP2 + Op.MSTORE(offset=Op.DUP4, value=Op.SLOAD(key=Op.ADD)) + Op.DUP3 + Op.ADD + Op.SWAP3 + Op.SWAP1 + Op.SWAP3 + Op.MSTORE + Op.PUSH1[0x40] + Op.SHA3(offset=Op.DUP2, size=Op.ADD) + Op.SSTORE(key=Op.DUP2, value=Op.DUP2) + Op.ADD(Op.DUP2, 0x1) + Op.DUP3 + Op.SWAP1 + Op.SSTORE + Op.SSTORE(key=Op.ADD, value=0x2) + Op.JUMPDEST + Op.PUSH1[0x1] + Op.ADD + Op.JUMP(pc=0x2e0),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
