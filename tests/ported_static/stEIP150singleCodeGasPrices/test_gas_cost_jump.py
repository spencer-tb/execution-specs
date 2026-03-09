"""
Ori Pomerantz qbzzt1@gmail.com

Ported from:
tests/static/state_tests/stEIP150singleCodeGasPrices/gasCostJumpFiller.yml
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
    ["tests/static/state_tests/stEIP150singleCodeGasPrices/gasCostJumpFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        ("c5b5a1ae00000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000004", {Address("0x0000000000000000000000000000000000001000"): Account(code=Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPDEST + Op.STOP), Address("0x0000000000000000000000000000000000002000"): Account(code=Op.PUSH1[0x0] + Op.JUMP(pc=0x5) + Op.JUMPDEST + Op.STOP), Address("0x0000000000000000000000000000000000003000"): Account(code=Op.JUMPI(pc=0x5, condition=0x1) + Op.JUMPDEST + Op.STOP), Address("0x0000000000000000000000000000000000004000"): Account(code=Op.JUMPI(pc=0x5, condition=0x0) + Op.JUMPDEST + Op.STOP), Address("0x095e7baea6a6c7c4c2dfeb977efac326af552d87"): Account(code=Op.MSTORE(offset=0x0, value=Op.GAS) + Op.POP(Op.CALL(gas=0x10000, address=0x1000, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.MSTORE(offset=0x20, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)) + Op.JUMPI(pc=0x2e, condition=Op.EQ(Op.CALLDATALOAD(offset=0x4), 0x1)) + Op.POP(0x0) + Op.JUMP(pc=0x4e) + Op.JUMPDEST + Op.MSTORE(offset=0x0, value=Op.GAS) + Op.POP(Op.CALL(gas=0x10000, address=0x2000, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.MSTORE(offset=0x40, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)) + Op.JUMPDEST + Op.JUMPI(pc=0x5e, condition=Op.EQ(Op.CALLDATALOAD(offset=0x4), 0x2)) + Op.POP(0x0) + Op.JUMP(pc=0x7e) + Op.JUMPDEST + Op.MSTORE(offset=0x0, value=Op.GAS) + Op.POP(Op.CALL(gas=0x10000, address=0x3000, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.MSTORE(offset=0x40, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)) + Op.JUMPDEST + Op.JUMPI(pc=0x8e, condition=Op.EQ(Op.CALLDATALOAD(offset=0x4), 0x3)) + Op.POP(0x0) + Op.JUMP(pc=0xae) + Op.JUMPDEST + Op.MSTORE(offset=0x0, value=Op.GAS) + Op.POP(Op.CALL(gas=0x10000, address=0x4000, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.MSTORE(offset=0x40, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)) + Op.JUMPDEST + Op.SSTORE(key=0x0, value=Op.SUB(Op.SUB(Op.MLOAD(offset=0x40), Op.MLOAD(offset=0x20)), Op.CALLDATALOAD(offset=0x24))) + Op.STOP)}),
        ("c5b5a1ae00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000006", {Address("0x0000000000000000000000000000000000001000"): Account(code=Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPDEST + Op.STOP), Address("0x0000000000000000000000000000000000002000"): Account(code=Op.PUSH1[0x0] + Op.JUMP(pc=0x5) + Op.JUMPDEST + Op.STOP), Address("0x0000000000000000000000000000000000003000"): Account(code=Op.JUMPI(pc=0x5, condition=0x1) + Op.JUMPDEST + Op.STOP), Address("0x0000000000000000000000000000000000004000"): Account(code=Op.JUMPI(pc=0x5, condition=0x0) + Op.JUMPDEST + Op.STOP), Address("0x095e7baea6a6c7c4c2dfeb977efac326af552d87"): Account(code=Op.MSTORE(offset=0x0, value=Op.GAS) + Op.POP(Op.CALL(gas=0x10000, address=0x1000, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.MSTORE(offset=0x20, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)) + Op.JUMPI(pc=0x2e, condition=Op.EQ(Op.CALLDATALOAD(offset=0x4), 0x1)) + Op.POP(0x0) + Op.JUMP(pc=0x4e) + Op.JUMPDEST + Op.MSTORE(offset=0x0, value=Op.GAS) + Op.POP(Op.CALL(gas=0x10000, address=0x2000, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.MSTORE(offset=0x40, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)) + Op.JUMPDEST + Op.JUMPI(pc=0x5e, condition=Op.EQ(Op.CALLDATALOAD(offset=0x4), 0x2)) + Op.POP(0x0) + Op.JUMP(pc=0x7e) + Op.JUMPDEST + Op.MSTORE(offset=0x0, value=Op.GAS) + Op.POP(Op.CALL(gas=0x10000, address=0x3000, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.MSTORE(offset=0x40, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)) + Op.JUMPDEST + Op.JUMPI(pc=0x8e, condition=Op.EQ(Op.CALLDATALOAD(offset=0x4), 0x3)) + Op.POP(0x0) + Op.JUMP(pc=0xae) + Op.JUMPDEST + Op.MSTORE(offset=0x0, value=Op.GAS) + Op.POP(Op.CALL(gas=0x10000, address=0x4000, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.MSTORE(offset=0x40, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)) + Op.JUMPDEST + Op.SSTORE(key=0x0, value=Op.SUB(Op.SUB(Op.MLOAD(offset=0x40), Op.MLOAD(offset=0x20)), Op.CALLDATALOAD(offset=0x24))) + Op.STOP)}),
        ("c5b5a1ae00000000000000000000000000000000000000000000000000000000000000030000000000000000000000000000000000000000000000000000000000000006", {Address("0x0000000000000000000000000000000000001000"): Account(code=Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPDEST + Op.STOP), Address("0x0000000000000000000000000000000000002000"): Account(code=Op.PUSH1[0x0] + Op.JUMP(pc=0x5) + Op.JUMPDEST + Op.STOP), Address("0x0000000000000000000000000000000000003000"): Account(code=Op.JUMPI(pc=0x5, condition=0x1) + Op.JUMPDEST + Op.STOP), Address("0x0000000000000000000000000000000000004000"): Account(code=Op.JUMPI(pc=0x5, condition=0x0) + Op.JUMPDEST + Op.STOP), Address("0x095e7baea6a6c7c4c2dfeb977efac326af552d87"): Account(code=Op.MSTORE(offset=0x0, value=Op.GAS) + Op.POP(Op.CALL(gas=0x10000, address=0x1000, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.MSTORE(offset=0x20, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)) + Op.JUMPI(pc=0x2e, condition=Op.EQ(Op.CALLDATALOAD(offset=0x4), 0x1)) + Op.POP(0x0) + Op.JUMP(pc=0x4e) + Op.JUMPDEST + Op.MSTORE(offset=0x0, value=Op.GAS) + Op.POP(Op.CALL(gas=0x10000, address=0x2000, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.MSTORE(offset=0x40, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)) + Op.JUMPDEST + Op.JUMPI(pc=0x5e, condition=Op.EQ(Op.CALLDATALOAD(offset=0x4), 0x2)) + Op.POP(0x0) + Op.JUMP(pc=0x7e) + Op.JUMPDEST + Op.MSTORE(offset=0x0, value=Op.GAS) + Op.POP(Op.CALL(gas=0x10000, address=0x3000, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.MSTORE(offset=0x40, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)) + Op.JUMPDEST + Op.JUMPI(pc=0x8e, condition=Op.EQ(Op.CALLDATALOAD(offset=0x4), 0x3)) + Op.POP(0x0) + Op.JUMP(pc=0xae) + Op.JUMPDEST + Op.MSTORE(offset=0x0, value=Op.GAS) + Op.POP(Op.CALL(gas=0x10000, address=0x4000, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.MSTORE(offset=0x40, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)) + Op.JUMPDEST + Op.SSTORE(key=0x0, value=Op.SUB(Op.SUB(Op.MLOAD(offset=0x40), Op.MLOAD(offset=0x20)), Op.CALLDATALOAD(offset=0x24))) + Op.STOP)}),
    ],
    ids=['case0', 'case1', 'case2'],
)
@pytest.mark.pre_alloc_mutable
def test_gas_cost_jump(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Ori Pomerantz qbzzt1@gmail.com."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x095e7baea6a6c7c4c2dfeb977efac326af552d87")
    callee = Address("0x0000000000000000000000000000000000001000")
    callee_1 = Address("0x0000000000000000000000000000000000002000")
    callee_2 = Address("0x0000000000000000000000000000000000003000")
    callee_3 = Address("0x0000000000000000000000000000000000004000")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000,
    )

    pre[callee] = Account(
        balance=0xba1a9ce0ba1a9ce,
        nonce=0,
        code=Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.JUMPDEST + Op.JUMPDEST + Op.STOP,
    )
    pre[callee_1] = Account(
        balance=0xba1a9ce0ba1a9ce,
        nonce=0,
        code=Op.PUSH1[0x0] + Op.JUMP(pc=0x5) + Op.JUMPDEST + Op.STOP,
    )
    pre[callee_2] = Account(
        balance=0xba1a9ce0ba1a9ce,
        nonce=0,
        code=Op.JUMPI(pc=0x5, condition=0x1) + Op.JUMPDEST + Op.STOP,
    )
    pre[callee_3] = Account(
        balance=0xba1a9ce0ba1a9ce,
        nonce=0,
        code=Op.JUMPI(pc=0x5, condition=0x0) + Op.JUMPDEST + Op.STOP,
    )
    pre[contract] = Account(
        balance=0xba1a9ce0ba1a9ce,
        nonce=0,
        code=(
        Op.MSTORE(offset=0x0, value=Op.GAS)
        + Op.POP(Op.CALL(gas=0x10000, address=0x1000, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.MSTORE(offset=0x20, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS))
        + Op.JUMPI(pc=0x2e, condition=Op.EQ(Op.CALLDATALOAD(offset=0x4), 0x1))
        + Op.POP(0x0) + Op.JUMP(pc=0x4e) + Op.JUMPDEST
        + Op.MSTORE(offset=0x0, value=Op.GAS)
        + Op.POP(Op.CALL(gas=0x10000, address=0x2000, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.MSTORE(offset=0x40, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS))
        + Op.JUMPDEST
        + Op.JUMPI(pc=0x5e, condition=Op.EQ(Op.CALLDATALOAD(offset=0x4), 0x2))
        + Op.POP(0x0) + Op.JUMP(pc=0x7e) + Op.JUMPDEST
        + Op.MSTORE(offset=0x0, value=Op.GAS)
        + Op.POP(Op.CALL(gas=0x10000, address=0x3000, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.MSTORE(offset=0x40, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS))
        + Op.JUMPDEST
        + Op.JUMPI(pc=0x8e, condition=Op.EQ(Op.CALLDATALOAD(offset=0x4), 0x3))
        + Op.POP(0x0) + Op.JUMP(pc=0xae) + Op.JUMPDEST
        + Op.MSTORE(offset=0x0, value=Op.GAS)
        + Op.POP(Op.CALL(gas=0x10000, address=0x4000, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.MSTORE(offset=0x40, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS))
        + Op.JUMPDEST
        + Op.SSTORE(key=0x0, value=Op.SUB(Op.SUB(Op.MLOAD(offset=0x40), Op.MLOAD(offset=0x20)), Op.CALLDATALOAD(offset=0x24)))
        + Op.STOP
    ),
        storage={0x0: 0x60a7},
    )
    pre[sender] = Account(balance=0xba1a9ce0ba1a9ce, nonce=0)

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=tx_data,
        gas_limit=16777216,
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
