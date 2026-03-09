"""
Ported from:
tests/static/state_tests/stSolidityTest/CallLowLevelCreatesSolidityFiller.json
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
    ["tests/static/state_tests/stSolidityTest/CallLowLevelCreatesSolidityFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_call_low_level_creates_solidity(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x7f3f285918d9b5e764174551e10b7539b97bbb27")
    contract = Address("0x5da6fbe439a0c3ab33f813671a4e7767ee0a263b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000,
    )

    pre[contract] = Account(
        balance=0x186a0,
        nonce=0,
        code=(
        Op.CALLDATALOAD(offset=0x0) + Op.EXP(0x2, 0xe0) + Op.SWAP1 + Op.DIV
        + Op.JUMPI(pc=Op.PUSH2[0x21], condition=Op.EQ(0x30debb42, Op.DUP1))
        + Op.JUMPI(pc=Op.PUSH2[0x32], condition=Op.EQ(0xc0406226, Op.DUP1)) + Op.STOP
        + Op.JUMPDEST + Op.PUSH2[0x2c] + Op.CALLDATALOAD(offset=0x4)
        + Op.JUMP(pc=Op.PUSH2[0xc7]) + Op.JUMPDEST + Op.RETURN(offset=0x0, size=0x0)
        + Op.JUMPDEST + Op.PUSH2[0x3a] + Op.JUMP(pc=Op.PUSH2[0x44]) + Op.JUMPDEST
        + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.RETURN(offset=0x0, size=0x20)
        + Op.JUMPDEST + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x1] + Op.PUSH1[0x0]
        + Op.DUP2 + Op.SWAP1 + Op.SSTORE + Op.POP
        + Op.PUSH20[0x5da6fbe439a0c3ab33f813671a4e7767ee0a263b] + Op.PUSH1[0x1]
        + Op.DUP2 + Op.SWAP1 + Op.SSTORE + Op.POP
        + Op.CODECOPY(dest_offset=0x0, offset=Op.PUSH2[0xd2], size=0x6a)
        + Op.CREATE(value=0x0, offset=0x0, size=0x6a) + Op.SWAP1 + Op.POP
        + Op.AND(Op.SUB(Op.EXP(0x2, 0xa0), 0x1), Op.DUP1) + Op.PUSH4[0x19ab453c]
        + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.MSTORE(offset=0x0, value=Op.MUL(Op.EXP(0x2, 0xe0), Op.DUP3))
        + Op.PUSH1[0x4]
        + Op.MSTORE(offset=Op.DUP2, value=Op.AND(Op.SUB(Op.EXP(0x2, 0xa0), 0x1), Op.SLOAD(key=0x1)))
        + Op.PUSH1[0x20] + Op.ADD + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.DUP7
        + Op.SUB(Op.GAS, 0x32) + Op.JUMPI(pc=Op.PUSH2[0xbc], condition=Op.CALL)
        + Op.STOP + Op.JUMPDEST + Op.POP + Op.POP + Op.SLOAD(key=0x0) + Op.SWAP2
        + Op.POP + Op.POP + Op.SWAP1 + Op.JUMP + Op.JUMPDEST + Op.DUP1 + Op.PUSH1[0x0]
        + Op.DUP2 + Op.SWAP1 + Op.SSTORE + Op.POP + Op.POP + Op.JUMP + Op.STOP
        + Op.PUSH1[0x5e] + Op.CODECOPY(dest_offset=0x0, offset=0xc, size=Op.DUP1)
        + Op.PUSH1[0x0] + Op.RETURN + Op.STOP + Op.CALLDATALOAD(offset=0x0)
        + Op.EXP(0x2, 0xe0) + Op.SWAP1 + Op.DIV
        + Op.JUMPI(pc=0x15, condition=Op.EQ(0x19ab453c, Op.DUP1)) + Op.STOP
        + Op.JUMPDEST + Op.PUSH1[0x1e] + Op.CALLDATALOAD(offset=0x4)
        + Op.JUMP(pc=0x24) + Op.JUMPDEST + Op.RETURN(offset=0x0, size=0x0)
        + Op.JUMPDEST + Op.AND(Op.SUB(Op.EXP(0x2, 0xa0), 0x1), Op.DUP1)
        + Op.PUSH4[0x30debb42] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.MSTORE(offset=0x0, value=Op.MUL(Op.EXP(0x2, 0xe0), Op.DUP3))
        + Op.PUSH1[0x4] + Op.MSTORE(offset=Op.DUP2, value=0xe1) + Op.PUSH1[0x20]
        + Op.ADD + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.DUP7 + Op.SUB(Op.GAS, 0x32)
        + Op.JUMPI(pc=0x59, condition=Op.CALL) + Op.STOP + Op.JUMPDEST + Op.POP
        + Op.POP + Op.POP + Op.JUMP
    ),
    )
    pre[sender] = Account(balance=0x5f5e100, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xa2333eef5630066b928dea5fd85a239f511b5b067d1441ee7ac290d0122b917b"
        ),
        to=contract,
        data=bytes.fromhex("c0406226"),
        gas_limit=350000,
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = {
        contract: Account(
            storage={0: 225, 1: 0x5da6fbe439a0c3ab33f813671a4e7767ee0a263b},
            code=Op.CALLDATALOAD(offset=0x0) + Op.EXP(0x2, 0xe0) + Op.SWAP1 + Op.DIV + Op.JUMPI(pc=Op.PUSH2[0x21], condition=Op.EQ(0x30debb42, Op.DUP1)) + Op.JUMPI(pc=Op.PUSH2[0x32], condition=Op.EQ(0xc0406226, Op.DUP1)) + Op.STOP + Op.JUMPDEST + Op.PUSH2[0x2c] + Op.CALLDATALOAD(offset=0x4) + Op.JUMP(pc=Op.PUSH2[0xc7]) + Op.JUMPDEST + Op.RETURN(offset=0x0, size=0x0) + Op.JUMPDEST + Op.PUSH2[0x3a] + Op.JUMP(pc=Op.PUSH2[0x44]) + Op.JUMPDEST + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.RETURN(offset=0x0, size=0x20) + Op.JUMPDEST + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x1] + Op.PUSH1[0x0] + Op.DUP2 + Op.SWAP1 + Op.SSTORE + Op.POP + Op.PUSH20[0x5da6fbe439a0c3ab33f813671a4e7767ee0a263b] + Op.PUSH1[0x1] + Op.DUP2 + Op.SWAP1 + Op.SSTORE + Op.POP + Op.CODECOPY(dest_offset=0x0, offset=Op.PUSH2[0xd2], size=0x6a) + Op.CREATE(value=0x0, offset=0x0, size=0x6a) + Op.SWAP1 + Op.POP + Op.AND(Op.SUB(Op.EXP(0x2, 0xa0), 0x1), Op.DUP1) + Op.PUSH4[0x19ab453c] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.MSTORE(offset=0x0, value=Op.MUL(Op.EXP(0x2, 0xe0), Op.DUP3)) + Op.PUSH1[0x4] + Op.MSTORE(offset=Op.DUP2, value=Op.AND(Op.SUB(Op.EXP(0x2, 0xa0), 0x1), Op.SLOAD(key=0x1))) + Op.PUSH1[0x20] + Op.ADD + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.DUP7 + Op.SUB(Op.GAS, 0x32) + Op.JUMPI(pc=Op.PUSH2[0xbc], condition=Op.CALL) + Op.STOP + Op.JUMPDEST + Op.POP + Op.POP + Op.SLOAD(key=0x0) + Op.SWAP2 + Op.POP + Op.POP + Op.SWAP1 + Op.JUMP + Op.JUMPDEST + Op.DUP1 + Op.PUSH1[0x0] + Op.DUP2 + Op.SWAP1 + Op.SSTORE + Op.POP + Op.POP + Op.JUMP + Op.STOP + Op.PUSH1[0x5e] + Op.CODECOPY(dest_offset=0x0, offset=0xc, size=Op.DUP1) + Op.PUSH1[0x0] + Op.RETURN + Op.STOP + Op.CALLDATALOAD(offset=0x0) + Op.EXP(0x2, 0xe0) + Op.SWAP1 + Op.DIV + Op.JUMPI(pc=0x15, condition=Op.EQ(0x19ab453c, Op.DUP1)) + Op.STOP + Op.JUMPDEST + Op.PUSH1[0x1e] + Op.CALLDATALOAD(offset=0x4) + Op.JUMP(pc=0x24) + Op.JUMPDEST + Op.RETURN(offset=0x0, size=0x0) + Op.JUMPDEST + Op.AND(Op.SUB(Op.EXP(0x2, 0xa0), 0x1), Op.DUP1) + Op.PUSH4[0x30debb42] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.MSTORE(offset=0x0, value=Op.MUL(Op.EXP(0x2, 0xe0), Op.DUP3)) + Op.PUSH1[0x4] + Op.MSTORE(offset=Op.DUP2, value=0xe1) + Op.PUSH1[0x20] + Op.ADD + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.DUP7 + Op.SUB(Op.GAS, 0x32) + Op.JUMPI(pc=0x59, condition=Op.CALL) + Op.STOP + Op.JUMPDEST + Op.POP + Op.POP + Op.POP + Op.JUMP,
        ),
        Address("0xdb95dad3113b9a7b8d67924d5878f2be23c3cedf"): Account(
            code=Op.CALLDATALOAD(offset=0x0) + Op.EXP(0x2, 0xe0) + Op.SWAP1 + Op.DIV + Op.JUMPI(pc=0x15, condition=Op.EQ(0x19ab453c, Op.DUP1)) + Op.STOP + Op.JUMPDEST + Op.PUSH1[0x1e] + Op.CALLDATALOAD(offset=0x4) + Op.JUMP(pc=0x24) + Op.JUMPDEST + Op.RETURN(offset=0x0, size=0x0) + Op.JUMPDEST + Op.AND(Op.SUB(Op.EXP(0x2, 0xa0), 0x1), Op.DUP1) + Op.PUSH4[0x30debb42] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.MSTORE(offset=0x0, value=Op.MUL(Op.EXP(0x2, 0xe0), Op.DUP3)) + Op.PUSH1[0x4] + Op.MSTORE(offset=Op.DUP2, value=0xe1) + Op.PUSH1[0x20] + Op.ADD + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.DUP7 + Op.SUB(Op.GAS, 0x32) + Op.JUMPI(pc=0x59, condition=Op.CALL) + Op.STOP + Op.JUMPDEST + Op.POP + Op.POP + Op.POP + Op.JUMP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
