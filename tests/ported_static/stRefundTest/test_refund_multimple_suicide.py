"""
Ported from:
tests/static/state_tests/stRefundTest/refund_multimpleSuicideFiller.json
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
    ["tests/static/state_tests/stRefundTest/refund_multimpleSuicideFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_refund_multimple_suicide(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0xeb201d2887816e041f6e807e804f64f3a7a226fe")
    sender = Address("0x2f8048c9a8457f574cd0c45ee76b2fcfdf464e8b")
    contract = Address("0x8b9574e5049501f581886404adf7037002276e78")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    pre[sender] = Account(balance=0x623a7c0, nonce=0)
    pre[contract] = Account(
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=(
        Op.MSTORE(offset=0x40, value=0x60)
        + Op.DIV(Op.CALLDATALOAD(offset=0x0), Op.EXP(0x2, 0xe0))
        + Op.JUMPI(pc=Op.PUSH2[0x31], condition=Op.EQ(Op.DUP2, 0x9e587a5))
        + Op.JUMPI(pc=Op.PUSH2[0x4d], condition=Op.EQ(0xc0406226, Op.DUP1))
        + Op.JUMPI(pc=Op.PUSH2[0x5a], condition=Op.EQ(0xdd4f1f2a, Op.DUP1))
        + Op.JUMPDEST + Op.STOP + Op.JUMPDEST + Op.PUSH2[0x2f]
        + Op.SELFDESTRUCT(address=Op.AND(0xffffffffffffffffffffffffffffffffffffffff, Op.CALLER))
        + Op.JUMPDEST + Op.PUSH2[0xf5] + Op.PUSH1[0x0] + Op.PUSH2[0x109]
        + Op.JUMP(pc=Op.PUSH2[0x5e]) + Op.JUMPDEST + Op.PUSH2[0x2f] + Op.JUMPDEST
        + Op.PUSH1[0x0] + Op.ADDRESS + Op.SWAP1 + Op.POP
        + Op.AND(0xffffffffffffffffffffffffffffffffffffffff, Op.DUP1)
        + Op.PUSH4[0x9e587a5] + Op.MLOAD(offset=0x40)
        + Op.MSTORE(offset=Op.DUP2, value=Op.MUL(Op.EXP(0x2, 0xe0), Op.DUP2))
        + Op.PUSH1[0x4] + Op.ADD + Op.DUP1 + Op.SWAP1 + Op.POP
        + Op.JUMPI(pc=Op.PUSH2[0x2], condition=Op.ISZERO(Op.CALL(gas=Op.SUB(Op.GAS, 0x61da), address=Op.DUP8, value=0x0, args_offset=Op.DUP2, args_size=Op.SUB(Op.DUP4, Op.DUP1), ret_offset=Op.MLOAD(offset=0x40), ret_size=0x0)))
        + Op.POP + Op.PUSH1[0x40] + Op.MLOAD(offset=Op.DUP1)
        + Op.MSTORE(offset=Op.DUP2, value=0x9e587a500000000000000000000000000000000000000000000000000000000)
        + Op.SWAP1 + Op.MLOAD + Op.PUSH1[0x4] + Op.ADD(Op.DUP2, Op.DUP3) + Op.SWAP3
        + Op.PUSH1[0x0] + Op.SWAP3 + Op.SWAP2 + Op.SWAP1 + Op.DUP3 + Op.SWAP1 + Op.SUB
        + Op.ADD + Op.DUP2 + Op.DUP4 + Op.DUP8 + Op.SUB(Op.GAS, 0x61da)
        + Op.JUMPI(pc=Op.PUSH2[0x2], condition=Op.ISZERO(Op.CALL)) + Op.POP + Op.POP
        + Op.POP + Op.POP + Op.JUMP + Op.JUMPDEST + Op.PUSH1[0x40]
        + Op.MLOAD(offset=Op.DUP1) + Op.SWAP2
        + Op.MSTORE(offset=Op.DUP3, value=Op.ISZERO(Op.ISZERO)) + Op.MLOAD + Op.SWAP1
        + Op.DUP2 + Op.SWAP1 + Op.ADD(0x20, Op.SUB) + Op.SWAP1 + Op.RETURN
        + Op.JUMPDEST + Op.POP + Op.PUSH1[0x1] + Op.SWAP1 + Op.JUMP
    ),
    )
    pre[coinbase] = Account(balance=0, nonce=1)

    tx = Transaction(
        secret_key=Hash(
            "0xc69694690a07d1418b0aadfd424a00ea9f25d84b94fecef12943de9cd38ede14"
        ),
        to=contract,
        data=bytes.fromhex("c0406226"),
        gas_limit=300000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            code=Op.MSTORE(offset=0x40, value=0x60) + Op.DIV(Op.CALLDATALOAD(offset=0x0), Op.EXP(0x2, 0xe0)) + Op.JUMPI(pc=Op.PUSH2[0x31], condition=Op.EQ(Op.DUP2, 0x9e587a5)) + Op.JUMPI(pc=Op.PUSH2[0x4d], condition=Op.EQ(0xc0406226, Op.DUP1)) + Op.JUMPI(pc=Op.PUSH2[0x5a], condition=Op.EQ(0xdd4f1f2a, Op.DUP1)) + Op.JUMPDEST + Op.STOP + Op.JUMPDEST + Op.PUSH2[0x2f] + Op.SELFDESTRUCT(address=Op.AND(0xffffffffffffffffffffffffffffffffffffffff, Op.CALLER)) + Op.JUMPDEST + Op.PUSH2[0xf5] + Op.PUSH1[0x0] + Op.PUSH2[0x109] + Op.JUMP(pc=Op.PUSH2[0x5e]) + Op.JUMPDEST + Op.PUSH2[0x2f] + Op.JUMPDEST + Op.PUSH1[0x0] + Op.ADDRESS + Op.SWAP1 + Op.POP + Op.AND(0xffffffffffffffffffffffffffffffffffffffff, Op.DUP1) + Op.PUSH4[0x9e587a5] + Op.MLOAD(offset=0x40) + Op.MSTORE(offset=Op.DUP2, value=Op.MUL(Op.EXP(0x2, 0xe0), Op.DUP2)) + Op.PUSH1[0x4] + Op.ADD + Op.DUP1 + Op.SWAP1 + Op.POP + Op.JUMPI(pc=Op.PUSH2[0x2], condition=Op.ISZERO(Op.CALL(gas=Op.SUB(Op.GAS, 0x61da), address=Op.DUP8, value=0x0, args_offset=Op.DUP2, args_size=Op.SUB(Op.DUP4, Op.DUP1), ret_offset=Op.MLOAD(offset=0x40), ret_size=0x0))) + Op.POP + Op.PUSH1[0x40] + Op.MLOAD(offset=Op.DUP1) + Op.MSTORE(offset=Op.DUP2, value=0x9e587a500000000000000000000000000000000000000000000000000000000) + Op.SWAP1 + Op.MLOAD + Op.PUSH1[0x4] + Op.ADD(Op.DUP2, Op.DUP3) + Op.SWAP3 + Op.PUSH1[0x0] + Op.SWAP3 + Op.SWAP2 + Op.SWAP1 + Op.DUP3 + Op.SWAP1 + Op.SUB + Op.ADD + Op.DUP2 + Op.DUP4 + Op.DUP8 + Op.SUB(Op.GAS, 0x61da) + Op.JUMPI(pc=Op.PUSH2[0x2], condition=Op.ISZERO(Op.CALL)) + Op.POP + Op.POP + Op.POP + Op.POP + Op.JUMP + Op.JUMPDEST + Op.PUSH1[0x40] + Op.MLOAD(offset=Op.DUP1) + Op.SWAP2 + Op.MSTORE(offset=Op.DUP3, value=Op.ISZERO(Op.ISZERO)) + Op.MLOAD + Op.SWAP1 + Op.DUP2 + Op.SWAP1 + Op.ADD(0x20, Op.SUB) + Op.SWAP1 + Op.RETURN + Op.JUMPDEST + Op.POP + Op.PUSH1[0x1] + Op.SWAP1 + Op.JUMP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
