"""
SELFBALANCE tests inside CALL, DELEGATECALL, and CALLCODE

Ported from:
tests/static/state_tests/stSelfBalance/selfBalanceCallTypesFiller.json
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
    ["tests/static/state_tests/stSelfBalance/selfBalanceCallTypesFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        ("0000000000000000000000000000000000000000000000000000000000000001", {Address("0x76bac61ee2056f42f6cc29f5400adae3e5705237"): Account(storage={33: 4352}, code=Op.SSTORE(key=0x21, value=Op.SELFBALANCE) + Op.STOP), Address("0x84bf87fbef135afea15330fdf5847eb504cff901"): Account(storage={0: 0xa590bbf1b07b00fed987724e1db1bf206c2bc37c, 1: 0x76bac61ee2056f42f6cc29f5400adae3e5705237, 2: 0x8537ce29429ea557e3903c255ee6554dd8d21d26, 3: 0xe1ce93b3251fb38ae74d41af9f865978c572cf63}, code=Op.MSTORE(offset=0x80, value=0x0) + Op.JUMPDEST + Op.JUMPI(pc=0x75, condition=Op.ISZERO(Op.SLOAD(key=Op.MLOAD(offset=0x80)))) + Op.JUMPI(pc=0x2c, condition=Op.ISZERO(Op.EQ(0x1, Op.CALLDATALOAD(offset=0x0)))) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x15), address=Op.SLOAD(key=Op.MLOAD(offset=0x80)), value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.JUMPDEST + Op.JUMPI(pc=0x49, condition=Op.ISZERO(Op.EQ(0x2, Op.CALLDATALOAD(offset=0x0)))) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x15), address=Op.SLOAD(key=Op.MLOAD(offset=0x80)), args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.JUMPDEST + Op.JUMPI(pc=0x68, condition=Op.ISZERO(Op.EQ(0x3, Op.CALLDATALOAD(offset=0x0)))) + Op.POP(Op.CALLCODE(gas=Op.SUB(Op.GAS, 0x15), address=Op.SLOAD(key=Op.MLOAD(offset=0x80)), value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.JUMPDEST + Op.MSTORE(offset=0x80, value=Op.ADD(Op.MLOAD(offset=0x80), 0x1)) + Op.JUMP(pc=0x5) + Op.JUMPDEST + Op.STOP), Address("0x8537ce29429ea557e3903c255ee6554dd8d21d26"): Account(storage={49: 5}, code=Op.GAS + Op.SELFBALANCE + Op.GAS + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.SUB + Op.PUSH1[0x2] + Op.SWAP1 + Op.SSTORE(key=0x31, value=Op.SUB) + Op.STOP), Address("0xa590bbf1b07b00fed987724e1db1bf206c2bc37c"): Account(storage={17: 1}, code=Op.SSTORE(key=0x11, value=Op.EQ(Op.SELFBALANCE, Op.BALANCE(address=Op.ADDRESS))) + Op.STOP), Address("0xe1ce93b3251fb38ae74d41af9f865978c572cf63"): Account(storage={65: 4864, 66: 4863, 67: 1}, code=Op.SELFBALANCE + Op.SSTORE(key=0x41, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x0, address=0x0, value=0x1, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SELFBALANCE + Op.SSTORE(key=0x42, value=Op.DUP1) + Op.SWAP1 + Op.SSTORE(key=0x43, value=Op.SUB) + Op.STOP)}),
        ("0000000000000000000000000000000000000000000000000000000000000002", {Address("0x76bac61ee2056f42f6cc29f5400adae3e5705237"): Account(code=Op.SSTORE(key=0x21, value=Op.SELFBALANCE) + Op.STOP), Address("0x84bf87fbef135afea15330fdf5847eb504cff901"): Account(storage={0: 0xa590bbf1b07b00fed987724e1db1bf206c2bc37c, 1: 0x76bac61ee2056f42f6cc29f5400adae3e5705237, 2: 0x8537ce29429ea557e3903c255ee6554dd8d21d26, 3: 0xe1ce93b3251fb38ae74d41af9f865978c572cf63, 17: 1, 33: 8192, 49: 5, 65: 8192, 66: 8191, 67: 1}, code=Op.MSTORE(offset=0x80, value=0x0) + Op.JUMPDEST + Op.JUMPI(pc=0x75, condition=Op.ISZERO(Op.SLOAD(key=Op.MLOAD(offset=0x80)))) + Op.JUMPI(pc=0x2c, condition=Op.ISZERO(Op.EQ(0x1, Op.CALLDATALOAD(offset=0x0)))) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x15), address=Op.SLOAD(key=Op.MLOAD(offset=0x80)), value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.JUMPDEST + Op.JUMPI(pc=0x49, condition=Op.ISZERO(Op.EQ(0x2, Op.CALLDATALOAD(offset=0x0)))) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x15), address=Op.SLOAD(key=Op.MLOAD(offset=0x80)), args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.JUMPDEST + Op.JUMPI(pc=0x68, condition=Op.ISZERO(Op.EQ(0x3, Op.CALLDATALOAD(offset=0x0)))) + Op.POP(Op.CALLCODE(gas=Op.SUB(Op.GAS, 0x15), address=Op.SLOAD(key=Op.MLOAD(offset=0x80)), value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.JUMPDEST + Op.MSTORE(offset=0x80, value=Op.ADD(Op.MLOAD(offset=0x80), 0x1)) + Op.JUMP(pc=0x5) + Op.JUMPDEST + Op.STOP), Address("0x8537ce29429ea557e3903c255ee6554dd8d21d26"): Account(code=Op.GAS + Op.SELFBALANCE + Op.GAS + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.SUB + Op.PUSH1[0x2] + Op.SWAP1 + Op.SSTORE(key=0x31, value=Op.SUB) + Op.STOP), Address("0xa590bbf1b07b00fed987724e1db1bf206c2bc37c"): Account(code=Op.SSTORE(key=0x11, value=Op.EQ(Op.SELFBALANCE, Op.BALANCE(address=Op.ADDRESS))) + Op.STOP), Address("0xe1ce93b3251fb38ae74d41af9f865978c572cf63"): Account(code=Op.SELFBALANCE + Op.SSTORE(key=0x41, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x0, address=0x0, value=0x1, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SELFBALANCE + Op.SSTORE(key=0x42, value=Op.DUP1) + Op.SWAP1 + Op.SSTORE(key=0x43, value=Op.SUB) + Op.STOP)}),
        ("0000000000000000000000000000000000000000000000000000000000000003", {Address("0x76bac61ee2056f42f6cc29f5400adae3e5705237"): Account(code=Op.SSTORE(key=0x21, value=Op.SELFBALANCE) + Op.STOP), Address("0x84bf87fbef135afea15330fdf5847eb504cff901"): Account(storage={0: 0xa590bbf1b07b00fed987724e1db1bf206c2bc37c, 1: 0x76bac61ee2056f42f6cc29f5400adae3e5705237, 2: 0x8537ce29429ea557e3903c255ee6554dd8d21d26, 3: 0xe1ce93b3251fb38ae74d41af9f865978c572cf63, 17: 1, 33: 8192, 49: 5, 65: 8192, 66: 8191, 67: 1}, code=Op.MSTORE(offset=0x80, value=0x0) + Op.JUMPDEST + Op.JUMPI(pc=0x75, condition=Op.ISZERO(Op.SLOAD(key=Op.MLOAD(offset=0x80)))) + Op.JUMPI(pc=0x2c, condition=Op.ISZERO(Op.EQ(0x1, Op.CALLDATALOAD(offset=0x0)))) + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x15), address=Op.SLOAD(key=Op.MLOAD(offset=0x80)), value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.JUMPDEST + Op.JUMPI(pc=0x49, condition=Op.ISZERO(Op.EQ(0x2, Op.CALLDATALOAD(offset=0x0)))) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x15), address=Op.SLOAD(key=Op.MLOAD(offset=0x80)), args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.JUMPDEST + Op.JUMPI(pc=0x68, condition=Op.ISZERO(Op.EQ(0x3, Op.CALLDATALOAD(offset=0x0)))) + Op.POP(Op.CALLCODE(gas=Op.SUB(Op.GAS, 0x15), address=Op.SLOAD(key=Op.MLOAD(offset=0x80)), value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.JUMPDEST + Op.MSTORE(offset=0x80, value=Op.ADD(Op.MLOAD(offset=0x80), 0x1)) + Op.JUMP(pc=0x5) + Op.JUMPDEST + Op.STOP), Address("0x8537ce29429ea557e3903c255ee6554dd8d21d26"): Account(code=Op.GAS + Op.SELFBALANCE + Op.GAS + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.SUB + Op.PUSH1[0x2] + Op.SWAP1 + Op.SSTORE(key=0x31, value=Op.SUB) + Op.STOP), Address("0xa590bbf1b07b00fed987724e1db1bf206c2bc37c"): Account(code=Op.SSTORE(key=0x11, value=Op.EQ(Op.SELFBALANCE, Op.BALANCE(address=Op.ADDRESS))) + Op.STOP), Address("0xe1ce93b3251fb38ae74d41af9f865978c572cf63"): Account(code=Op.SELFBALANCE + Op.SSTORE(key=0x41, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x0, address=0x0, value=0x1, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SELFBALANCE + Op.SSTORE(key=0x42, value=Op.DUP1) + Op.SWAP1 + Op.SSTORE(key=0x43, value=Op.SUB) + Op.STOP)}),
    ],
    ids=['case0', 'case1', 'case2'],
)
@pytest.mark.pre_alloc_mutable
def test_self_balance_call_types(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """SELFBALANCE tests inside CALL, DELEGATECALL, and CALLCODE."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xd187b36e8532efd7f15218fb1781d79330c0cda2")
    contract = Address("0x84bf87fbef135afea15330fdf5847eb504cff901")
    callee = Address("0x76bac61ee2056f42f6cc29f5400adae3e5705237")
    callee_1 = Address("0x8537ce29429ea557e3903c255ee6554dd8d21d26")
    callee_2 = Address("0xa590bbf1b07b00fed987724e1db1bf206c2bc37c")
    callee_3 = Address("0xe1ce93b3251fb38ae74d41af9f865978c572cf63")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000000,
    )

    pre[callee] = Account(
        balance=4352,
        nonce=0,
        code=Op.SSTORE(key=0x21, value=Op.SELFBALANCE) + Op.STOP,
    )
    pre[contract] = Account(
        balance=8192,
        nonce=0,
        code=(
        Op.MSTORE(offset=0x80, value=0x0) + Op.JUMPDEST
        + Op.JUMPI(pc=0x75, condition=Op.ISZERO(Op.SLOAD(key=Op.MLOAD(offset=0x80))))
        + Op.JUMPI(pc=0x2c, condition=Op.ISZERO(Op.EQ(0x1, Op.CALLDATALOAD(offset=0x0))))
        + Op.POP(Op.CALL(gas=Op.SUB(Op.GAS, 0x15), address=Op.SLOAD(key=Op.MLOAD(offset=0x80)), value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.JUMPDEST
        + Op.JUMPI(pc=0x49, condition=Op.ISZERO(Op.EQ(0x2, Op.CALLDATALOAD(offset=0x0))))
        + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x15), address=Op.SLOAD(key=Op.MLOAD(offset=0x80)), args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.JUMPDEST
        + Op.JUMPI(pc=0x68, condition=Op.ISZERO(Op.EQ(0x3, Op.CALLDATALOAD(offset=0x0))))
        + Op.POP(Op.CALLCODE(gas=Op.SUB(Op.GAS, 0x15), address=Op.SLOAD(key=Op.MLOAD(offset=0x80)), value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.JUMPDEST
        + Op.MSTORE(offset=0x80, value=Op.ADD(Op.MLOAD(offset=0x80), 0x1))
        + Op.JUMP(pc=0x5) + Op.JUMPDEST + Op.STOP
    ),
        storage={0x0: 0xa590bbf1b07b00fed987724e1db1bf206c2bc37c, 0x1: 0x76bac61ee2056f42f6cc29f5400adae3e5705237, 0x2: 0x8537ce29429ea557e3903c255ee6554dd8d21d26, 0x3: 0xe1ce93b3251fb38ae74d41af9f865978c572cf63},
    )
    pre[callee_1] = Account(
        balance=4608,
        nonce=0,
        code=(
        Op.GAS + Op.SELFBALANCE + Op.GAS + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.SUB
        + Op.PUSH1[0x2] + Op.SWAP1 + Op.SSTORE(key=0x31, value=Op.SUB) + Op.STOP
    ),
    )
    pre[callee_2] = Account(
        balance=4096,
        nonce=0,
        code=(
        Op.SSTORE(key=0x11, value=Op.EQ(Op.SELFBALANCE, Op.BALANCE(address=Op.ADDRESS)))
        + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0x3635c9adc5dea00000, nonce=0)
    pre[callee_3] = Account(
        balance=4864,
        nonce=0,
        code=(
        Op.SELFBALANCE + Op.SSTORE(key=0x41, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x0, address=0x0, value=0x1, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.SELFBALANCE + Op.SSTORE(key=0x42, value=Op.DUP1) + Op.SWAP1
        + Op.SSTORE(key=0x43, value=Op.SUB) + Op.STOP
    ),
    )

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x897b12d02d588d8a4fe16ff831cbd4459c6f62f8c845b0ccdd31caf068c84a26"
        ),
        to=contract,
        data=tx_data,
        gas_limit=1000000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
