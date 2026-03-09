"""
Ori Pomerantz qbzzt1@gmail.com

Ported from:
tests/static/state_tests/stCreateTest/CodeInConstructorFiller.yml
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
    ["tests/static/state_tests/stCreateTest/CodeInConstructorFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        ("83c7d7580000000000000000000000000000000000000000000000000000000000000001", {Address("0x000000000000000000000000000000000000da7a"): Account(storage={0: 8, 1: 10, 2: 0x8af6a7af30d840ba137e8f3f34d54cfb8beba6e2, 3: 262, 5: 0x610100610100610100395861026052600060006020610260600061da7a62ffff, 7: 184}, code=Op.SSTORE(key=Op.SLOAD(key=0x0), value=Op.CALLDATALOAD(offset=0x0)) + Op.SSTORE(key=0x0, value=Op.ADD(Op.SLOAD(key=0x0), 0x1)) + Op.STOP), Address("0x8af6a7af30d840ba137e8f3f34d54cfb8beba6e2"): Account(code=Op.STOP + Op.STOP + Op.STOP + Op.STOP + Op.STOP + Op.STOP), Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(code=Op.PUSH1[0x6] + Op.CODECOPY(dest_offset=0x100, offset=Op.PUSH2[0x4c], size=Op.DUP1) + Op.PUSH2[0x200] + Op.MSTORE + Op.PUSH1[0xdb] + Op.CODECOPY(dest_offset=0x0, offset=Op.PUSH2[0x52], size=Op.DUP1) + Op.PUSH2[0x220] + Op.MSTORE + Op.JUMPI(pc=0x37, condition=Op.EQ(Op.CALLDATALOAD(offset=0x4), 0x1)) + Op.CREATE2(value=0x0, offset=0x0, size=Op.ADD(0x100, Op.MLOAD(offset=0x200)), salt=0x5a17) + Op.JUMP(pc=0x45) + Op.JUMPDEST + Op.CREATE(value=0x0, offset=0x0, size=Op.ADD(0x100, Op.MLOAD(offset=0x200))) + Op.JUMPDEST + Op.PUSH2[0x240] + Op.MSTORE + Op.STOP + Op.INVALID + Op.SSTORE(key=0x0, value=0xff) + Op.STOP + Op.CODECOPY(dest_offset=0x100, offset=0x100, size=0x100) + Op.MSTORE(offset=0x260, value=Op.PC) + Op.POP(Op.CALL(gas=0xffffff, address=0xda7a, value=0x0, args_offset=0x260, args_size=0x20, ret_offset=0x0, ret_size=0x0)) + Op.MSTORE(offset=0x260, value=Op.ADDRESS) + Op.POP(Op.CALL(gas=0xffffff, address=0xda7a, value=0x0, args_offset=0x260, args_size=0x20, ret_offset=0x0, ret_size=0x0)) + Op.MSTORE(offset=0x260, value=Op.CODESIZE) + Op.POP(Op.CALL(gas=0xffffff, address=0xda7a, value=0x0, args_offset=0x260, args_size=0x20, ret_offset=0x0, ret_size=0x0)) + Op.MSTORE(offset=0x260, value=Op.EXTCODESIZE(address=Op.ADDRESS)) + Op.POP(Op.CALL(gas=0xffffff, address=0xda7a, value=0x0, args_offset=0x260, args_size=0x20, ret_offset=0x0, ret_size=0x0)) + Op.CODECOPY(dest_offset=0x100, offset=0x0, size=0x20) + Op.MSTORE(offset=0x260, value=Op.MLOAD(offset=0x100)) + Op.POP(Op.CALL(gas=0xffffff, address=0xda7a, value=0x0, args_offset=0x260, args_size=0x20, ret_offset=0x0, ret_size=0x0)) + Op.EXTCODECOPY(address=Op.ADDRESS, dest_offset=0x100, offset=0x0, size=0x20) + Op.MSTORE(offset=0x260, value=Op.MLOAD(offset=0x100)) + Op.POP(Op.CALL(gas=0xffffff, address=0xda7a, value=0x0, args_offset=0x260, args_size=0x20, ret_offset=0x0, ret_size=0x0)) + Op.MSTORE(offset=0x260, value=Op.PC) + Op.POP(Op.CALL(gas=0xffffff, address=0xda7a, value=0x0, args_offset=0x260, args_size=0x20, ret_offset=0x0, ret_size=0x0)) + Op.RETURN(offset=0x100, size=Op.SUB(Op.CODESIZE, 0x100)) + Op.STOP)}),
        ("83c7d7580000000000000000000000000000000000000000000000000000000000000002", {Address("0x000000000000000000000000000000000000da7a"): Account(storage={0: 8, 1: 10, 2: 0x33c409678a4289f0184c95c627ba09da2daeaa46, 3: 262, 5: 0x610100610100610100395861026052600060006020610260600061da7a62ffff, 7: 184}, code=Op.SSTORE(key=Op.SLOAD(key=0x0), value=Op.CALLDATALOAD(offset=0x0)) + Op.SSTORE(key=0x0, value=Op.ADD(Op.SLOAD(key=0x0), 0x1)) + Op.STOP), Address("0x33c409678a4289f0184c95c627ba09da2daeaa46"): Account(code=Op.STOP + Op.STOP + Op.STOP + Op.STOP + Op.STOP + Op.STOP), Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(code=Op.PUSH1[0x6] + Op.CODECOPY(dest_offset=0x100, offset=Op.PUSH2[0x4c], size=Op.DUP1) + Op.PUSH2[0x200] + Op.MSTORE + Op.PUSH1[0xdb] + Op.CODECOPY(dest_offset=0x0, offset=Op.PUSH2[0x52], size=Op.DUP1) + Op.PUSH2[0x220] + Op.MSTORE + Op.JUMPI(pc=0x37, condition=Op.EQ(Op.CALLDATALOAD(offset=0x4), 0x1)) + Op.CREATE2(value=0x0, offset=0x0, size=Op.ADD(0x100, Op.MLOAD(offset=0x200)), salt=0x5a17) + Op.JUMP(pc=0x45) + Op.JUMPDEST + Op.CREATE(value=0x0, offset=0x0, size=Op.ADD(0x100, Op.MLOAD(offset=0x200))) + Op.JUMPDEST + Op.PUSH2[0x240] + Op.MSTORE + Op.STOP + Op.INVALID + Op.SSTORE(key=0x0, value=0xff) + Op.STOP + Op.CODECOPY(dest_offset=0x100, offset=0x100, size=0x100) + Op.MSTORE(offset=0x260, value=Op.PC) + Op.POP(Op.CALL(gas=0xffffff, address=0xda7a, value=0x0, args_offset=0x260, args_size=0x20, ret_offset=0x0, ret_size=0x0)) + Op.MSTORE(offset=0x260, value=Op.ADDRESS) + Op.POP(Op.CALL(gas=0xffffff, address=0xda7a, value=0x0, args_offset=0x260, args_size=0x20, ret_offset=0x0, ret_size=0x0)) + Op.MSTORE(offset=0x260, value=Op.CODESIZE) + Op.POP(Op.CALL(gas=0xffffff, address=0xda7a, value=0x0, args_offset=0x260, args_size=0x20, ret_offset=0x0, ret_size=0x0)) + Op.MSTORE(offset=0x260, value=Op.EXTCODESIZE(address=Op.ADDRESS)) + Op.POP(Op.CALL(gas=0xffffff, address=0xda7a, value=0x0, args_offset=0x260, args_size=0x20, ret_offset=0x0, ret_size=0x0)) + Op.CODECOPY(dest_offset=0x100, offset=0x0, size=0x20) + Op.MSTORE(offset=0x260, value=Op.MLOAD(offset=0x100)) + Op.POP(Op.CALL(gas=0xffffff, address=0xda7a, value=0x0, args_offset=0x260, args_size=0x20, ret_offset=0x0, ret_size=0x0)) + Op.EXTCODECOPY(address=Op.ADDRESS, dest_offset=0x100, offset=0x0, size=0x20) + Op.MSTORE(offset=0x260, value=Op.MLOAD(offset=0x100)) + Op.POP(Op.CALL(gas=0xffffff, address=0xda7a, value=0x0, args_offset=0x260, args_size=0x20, ret_offset=0x0, ret_size=0x0)) + Op.MSTORE(offset=0x260, value=Op.PC) + Op.POP(Op.CALL(gas=0xffffff, address=0xda7a, value=0x0, args_offset=0x260, args_size=0x20, ret_offset=0x0, ret_size=0x0)) + Op.RETURN(offset=0x100, size=Op.SUB(Op.CODESIZE, 0x100)) + Op.STOP)}),
    ],
    ids=['case0', 'case1'],
)
@pytest.mark.pre_alloc_mutable
def test_code_in_constructor(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Ori Pomerantz qbzzt1@gmail.com."""
    coinbase = Address("0xba5e0000ba5e0000ba5e0000ba5e0000ba5e0000")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xcccccccccccccccccccccccccccccccccccccccc")
    callee = Address("0x000000000000000000000000000000000000da7a")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=4294967296,
    )

    pre[callee] = Account(
        balance=0xba1a9ce0ba1a9ce,
        nonce=0,
        code=(
        Op.SSTORE(key=Op.SLOAD(key=0x0), value=Op.CALLDATALOAD(offset=0x0))
        + Op.SSTORE(key=0x0, value=Op.ADD(Op.SLOAD(key=0x0), 0x1)) + Op.STOP
    ),
        storage={0x0: 0x1},
    )
    pre[sender] = Account(balance=0xba1a9ce0ba1a9ce, nonce=0)
    pre[contract] = Account(
        balance=0xba1a9ce0ba1a9ce,
        nonce=0,
        code=(
        Op.PUSH1[0x6]
        + Op.CODECOPY(dest_offset=0x100, offset=Op.PUSH2[0x4c], size=Op.DUP1)
        + Op.PUSH2[0x200] + Op.MSTORE + Op.PUSH1[0xdb]
        + Op.CODECOPY(dest_offset=0x0, offset=Op.PUSH2[0x52], size=Op.DUP1)
        + Op.PUSH2[0x220] + Op.MSTORE
        + Op.JUMPI(pc=0x37, condition=Op.EQ(Op.CALLDATALOAD(offset=0x4), 0x1))
        + Op.CREATE2(value=0x0, offset=0x0, size=Op.ADD(0x100, Op.MLOAD(offset=0x200)), salt=0x5a17)
        + Op.JUMP(pc=0x45) + Op.JUMPDEST
        + Op.CREATE(value=0x0, offset=0x0, size=Op.ADD(0x100, Op.MLOAD(offset=0x200)))
        + Op.JUMPDEST + Op.PUSH2[0x240] + Op.MSTORE + Op.STOP + Op.INVALID
        + Op.SSTORE(key=0x0, value=0xff) + Op.STOP
        + Op.CODECOPY(dest_offset=0x100, offset=0x100, size=0x100)
        + Op.MSTORE(offset=0x260, value=Op.PC)
        + Op.POP(Op.CALL(gas=0xffffff, address=0xda7a, value=0x0, args_offset=0x260, args_size=0x20, ret_offset=0x0, ret_size=0x0))
        + Op.MSTORE(offset=0x260, value=Op.ADDRESS)
        + Op.POP(Op.CALL(gas=0xffffff, address=0xda7a, value=0x0, args_offset=0x260, args_size=0x20, ret_offset=0x0, ret_size=0x0))
        + Op.MSTORE(offset=0x260, value=Op.CODESIZE)
        + Op.POP(Op.CALL(gas=0xffffff, address=0xda7a, value=0x0, args_offset=0x260, args_size=0x20, ret_offset=0x0, ret_size=0x0))
        + Op.MSTORE(offset=0x260, value=Op.EXTCODESIZE(address=Op.ADDRESS))
        + Op.POP(Op.CALL(gas=0xffffff, address=0xda7a, value=0x0, args_offset=0x260, args_size=0x20, ret_offset=0x0, ret_size=0x0))
        + Op.CODECOPY(dest_offset=0x100, offset=0x0, size=0x20)
        + Op.MSTORE(offset=0x260, value=Op.MLOAD(offset=0x100))
        + Op.POP(Op.CALL(gas=0xffffff, address=0xda7a, value=0x0, args_offset=0x260, args_size=0x20, ret_offset=0x0, ret_size=0x0))
        + Op.EXTCODECOPY(address=Op.ADDRESS, dest_offset=0x100, offset=0x0, size=0x20)
        + Op.MSTORE(offset=0x260, value=Op.MLOAD(offset=0x100))
        + Op.POP(Op.CALL(gas=0xffffff, address=0xda7a, value=0x0, args_offset=0x260, args_size=0x20, ret_offset=0x0, ret_size=0x0))
        + Op.MSTORE(offset=0x260, value=Op.PC)
        + Op.POP(Op.CALL(gas=0xffffff, address=0xda7a, value=0x0, args_offset=0x260, args_size=0x20, ret_offset=0x0, ret_size=0x0))
        + Op.RETURN(offset=0x100, size=Op.SUB(Op.CODESIZE, 0x100)) + Op.STOP
    ),
    )

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=tx_data,
        gas_limit=9437184,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
