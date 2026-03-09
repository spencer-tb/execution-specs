"""
Danno Ferrin danno.ferrin@gmail.com

Ported from:
tests/static/state_tests/stEIP150Specific/Transaction64Rule_integerBoundariesFiller.yml
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
    ["tests/static/state_tests/stEIP150Specific/Transaction64Rule_integerBoundariesFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        ("000000000000000000000000000000007fffffffffffffffffffffffffffffff", {Address("0x0000000000000000000000000000000000001000"): Account(code=Op.PUSH1[0x0] + Op.PUSH1[0xff] + Op.STOP), Address("0x000000000000000000000000000000000000c0de"): Account(storage={0: 1, 1: 1, 2: 1, 3: 1}, code=Op.GAS + Op.PUSH1[0x20] + Op.PUSH1[0x0] + Op.DUP2 + Op.DUP2 + Op.PUSH2[0x1000] + Op.CALLDATALOAD(offset=Op.DUP2) + Op.POP(Op.CALL(gas=Op.DUP7, address=Op.DUP7, value=Op.DUP1, args_offset=Op.DUP1, args_size=Op.DUP1, ret_offset=Op.DUP4, ret_size=Op.DUP4)) + Op.SSTORE(key=Op.DUP4, value=Op.LT(Op.GAS, Op.DUP7)) + Op.POP(Op.CALLCODE(gas=Op.DUP7, address=Op.DUP7, value=Op.DUP1, args_offset=Op.DUP1, args_size=Op.DUP1, ret_offset=Op.DUP4, ret_size=Op.DUP4)) + Op.SSTORE(key=0x1, value=Op.LT(Op.GAS, Op.DUP7)) + Op.POP(Op.DELEGATECALL(gas=Op.DUP6, address=Op.DUP6, args_offset=Op.DUP2, args_size=Op.DUP2, ret_offset=Op.DUP4, ret_size=Op.DUP4)) + Op.SSTORE(key=0x2, value=Op.LT(Op.GAS, Op.DUP7)) + Op.POP(Op.STATICCALL) + Op.GAS + Op.SSTORE(key=0x3, value=Op.LT) + Op.STOP)}),
        ("0000000000000000000000000000000000000000000000000000000000007fff", {Address("0x0000000000000000000000000000000000001000"): Account(code=Op.PUSH1[0x0] + Op.PUSH1[0xff] + Op.STOP), Address("0x000000000000000000000000000000000000c0de"): Account(storage={0: 1, 1: 1, 2: 1, 3: 1}, code=Op.GAS + Op.PUSH1[0x20] + Op.PUSH1[0x0] + Op.DUP2 + Op.DUP2 + Op.PUSH2[0x1000] + Op.CALLDATALOAD(offset=Op.DUP2) + Op.POP(Op.CALL(gas=Op.DUP7, address=Op.DUP7, value=Op.DUP1, args_offset=Op.DUP1, args_size=Op.DUP1, ret_offset=Op.DUP4, ret_size=Op.DUP4)) + Op.SSTORE(key=Op.DUP4, value=Op.LT(Op.GAS, Op.DUP7)) + Op.POP(Op.CALLCODE(gas=Op.DUP7, address=Op.DUP7, value=Op.DUP1, args_offset=Op.DUP1, args_size=Op.DUP1, ret_offset=Op.DUP4, ret_size=Op.DUP4)) + Op.SSTORE(key=0x1, value=Op.LT(Op.GAS, Op.DUP7)) + Op.POP(Op.DELEGATECALL(gas=Op.DUP6, address=Op.DUP6, args_offset=Op.DUP2, args_size=Op.DUP2, ret_offset=Op.DUP4, ret_size=Op.DUP4)) + Op.SSTORE(key=0x2, value=Op.LT(Op.GAS, Op.DUP7)) + Op.POP(Op.STATICCALL) + Op.GAS + Op.SSTORE(key=0x3, value=Op.LT) + Op.STOP)}),
        ("7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", {Address("0x0000000000000000000000000000000000001000"): Account(code=Op.PUSH1[0x0] + Op.PUSH1[0xff] + Op.STOP), Address("0x000000000000000000000000000000000000c0de"): Account(storage={0: 1, 1: 1, 2: 1, 3: 1}, code=Op.GAS + Op.PUSH1[0x20] + Op.PUSH1[0x0] + Op.DUP2 + Op.DUP2 + Op.PUSH2[0x1000] + Op.CALLDATALOAD(offset=Op.DUP2) + Op.POP(Op.CALL(gas=Op.DUP7, address=Op.DUP7, value=Op.DUP1, args_offset=Op.DUP1, args_size=Op.DUP1, ret_offset=Op.DUP4, ret_size=Op.DUP4)) + Op.SSTORE(key=Op.DUP4, value=Op.LT(Op.GAS, Op.DUP7)) + Op.POP(Op.CALLCODE(gas=Op.DUP7, address=Op.DUP7, value=Op.DUP1, args_offset=Op.DUP1, args_size=Op.DUP1, ret_offset=Op.DUP4, ret_size=Op.DUP4)) + Op.SSTORE(key=0x1, value=Op.LT(Op.GAS, Op.DUP7)) + Op.POP(Op.DELEGATECALL(gas=Op.DUP6, address=Op.DUP6, args_offset=Op.DUP2, args_size=Op.DUP2, ret_offset=Op.DUP4, ret_size=Op.DUP4)) + Op.SSTORE(key=0x2, value=Op.LT(Op.GAS, Op.DUP7)) + Op.POP(Op.STATICCALL) + Op.GAS + Op.SSTORE(key=0x3, value=Op.LT) + Op.STOP)}),
        ("000000000000000000000000000000000000000000000000000000007fffffff", {Address("0x0000000000000000000000000000000000001000"): Account(code=Op.PUSH1[0x0] + Op.PUSH1[0xff] + Op.STOP), Address("0x000000000000000000000000000000000000c0de"): Account(storage={0: 1, 1: 1, 2: 1, 3: 1}, code=Op.GAS + Op.PUSH1[0x20] + Op.PUSH1[0x0] + Op.DUP2 + Op.DUP2 + Op.PUSH2[0x1000] + Op.CALLDATALOAD(offset=Op.DUP2) + Op.POP(Op.CALL(gas=Op.DUP7, address=Op.DUP7, value=Op.DUP1, args_offset=Op.DUP1, args_size=Op.DUP1, ret_offset=Op.DUP4, ret_size=Op.DUP4)) + Op.SSTORE(key=Op.DUP4, value=Op.LT(Op.GAS, Op.DUP7)) + Op.POP(Op.CALLCODE(gas=Op.DUP7, address=Op.DUP7, value=Op.DUP1, args_offset=Op.DUP1, args_size=Op.DUP1, ret_offset=Op.DUP4, ret_size=Op.DUP4)) + Op.SSTORE(key=0x1, value=Op.LT(Op.GAS, Op.DUP7)) + Op.POP(Op.DELEGATECALL(gas=Op.DUP6, address=Op.DUP6, args_offset=Op.DUP2, args_size=Op.DUP2, ret_offset=Op.DUP4, ret_size=Op.DUP4)) + Op.SSTORE(key=0x2, value=Op.LT(Op.GAS, Op.DUP7)) + Op.POP(Op.STATICCALL) + Op.GAS + Op.SSTORE(key=0x3, value=Op.LT) + Op.STOP)}),
        ("0000000000000000000000000000000000000000000000007fffffffffffffff", {Address("0x0000000000000000000000000000000000001000"): Account(code=Op.PUSH1[0x0] + Op.PUSH1[0xff] + Op.STOP), Address("0x000000000000000000000000000000000000c0de"): Account(storage={0: 1, 1: 1, 2: 1, 3: 1}, code=Op.GAS + Op.PUSH1[0x20] + Op.PUSH1[0x0] + Op.DUP2 + Op.DUP2 + Op.PUSH2[0x1000] + Op.CALLDATALOAD(offset=Op.DUP2) + Op.POP(Op.CALL(gas=Op.DUP7, address=Op.DUP7, value=Op.DUP1, args_offset=Op.DUP1, args_size=Op.DUP1, ret_offset=Op.DUP4, ret_size=Op.DUP4)) + Op.SSTORE(key=Op.DUP4, value=Op.LT(Op.GAS, Op.DUP7)) + Op.POP(Op.CALLCODE(gas=Op.DUP7, address=Op.DUP7, value=Op.DUP1, args_offset=Op.DUP1, args_size=Op.DUP1, ret_offset=Op.DUP4, ret_size=Op.DUP4)) + Op.SSTORE(key=0x1, value=Op.LT(Op.GAS, Op.DUP7)) + Op.POP(Op.DELEGATECALL(gas=Op.DUP6, address=Op.DUP6, args_offset=Op.DUP2, args_size=Op.DUP2, ret_offset=Op.DUP4, ret_size=Op.DUP4)) + Op.SSTORE(key=0x2, value=Op.LT(Op.GAS, Op.DUP7)) + Op.POP(Op.STATICCALL) + Op.GAS + Op.SSTORE(key=0x3, value=Op.LT) + Op.STOP)}),
        ("000000000000000000000000000000000000000000000000000000000000007f", {Address("0x0000000000000000000000000000000000001000"): Account(code=Op.PUSH1[0x0] + Op.PUSH1[0xff] + Op.STOP), Address("0x000000000000000000000000000000000000c0de"): Account(storage={0: 1, 1: 1, 2: 1, 3: 1}, code=Op.GAS + Op.PUSH1[0x20] + Op.PUSH1[0x0] + Op.DUP2 + Op.DUP2 + Op.PUSH2[0x1000] + Op.CALLDATALOAD(offset=Op.DUP2) + Op.POP(Op.CALL(gas=Op.DUP7, address=Op.DUP7, value=Op.DUP1, args_offset=Op.DUP1, args_size=Op.DUP1, ret_offset=Op.DUP4, ret_size=Op.DUP4)) + Op.SSTORE(key=Op.DUP4, value=Op.LT(Op.GAS, Op.DUP7)) + Op.POP(Op.CALLCODE(gas=Op.DUP7, address=Op.DUP7, value=Op.DUP1, args_offset=Op.DUP1, args_size=Op.DUP1, ret_offset=Op.DUP4, ret_size=Op.DUP4)) + Op.SSTORE(key=0x1, value=Op.LT(Op.GAS, Op.DUP7)) + Op.POP(Op.DELEGATECALL(gas=Op.DUP6, address=Op.DUP6, args_offset=Op.DUP2, args_size=Op.DUP2, ret_offset=Op.DUP4, ret_size=Op.DUP4)) + Op.SSTORE(key=0x2, value=Op.LT(Op.GAS, Op.DUP7)) + Op.POP(Op.STATICCALL) + Op.GAS + Op.SSTORE(key=0x3, value=Op.LT) + Op.STOP)}),
        ("000000000000000000000000000000008fffffffffffffffffffffffffffffff", {Address("0x0000000000000000000000000000000000001000"): Account(code=Op.PUSH1[0x0] + Op.PUSH1[0xff] + Op.STOP), Address("0x000000000000000000000000000000000000c0de"): Account(storage={0: 1, 1: 1, 2: 1, 3: 1}, code=Op.GAS + Op.PUSH1[0x20] + Op.PUSH1[0x0] + Op.DUP2 + Op.DUP2 + Op.PUSH2[0x1000] + Op.CALLDATALOAD(offset=Op.DUP2) + Op.POP(Op.CALL(gas=Op.DUP7, address=Op.DUP7, value=Op.DUP1, args_offset=Op.DUP1, args_size=Op.DUP1, ret_offset=Op.DUP4, ret_size=Op.DUP4)) + Op.SSTORE(key=Op.DUP4, value=Op.LT(Op.GAS, Op.DUP7)) + Op.POP(Op.CALLCODE(gas=Op.DUP7, address=Op.DUP7, value=Op.DUP1, args_offset=Op.DUP1, args_size=Op.DUP1, ret_offset=Op.DUP4, ret_size=Op.DUP4)) + Op.SSTORE(key=0x1, value=Op.LT(Op.GAS, Op.DUP7)) + Op.POP(Op.DELEGATECALL(gas=Op.DUP6, address=Op.DUP6, args_offset=Op.DUP2, args_size=Op.DUP2, ret_offset=Op.DUP4, ret_size=Op.DUP4)) + Op.SSTORE(key=0x2, value=Op.LT(Op.GAS, Op.DUP7)) + Op.POP(Op.STATICCALL) + Op.GAS + Op.SSTORE(key=0x3, value=Op.LT) + Op.STOP)}),
        ("0000000000000000000000000000000000000000000000000000000000008fff", {Address("0x0000000000000000000000000000000000001000"): Account(code=Op.PUSH1[0x0] + Op.PUSH1[0xff] + Op.STOP), Address("0x000000000000000000000000000000000000c0de"): Account(storage={0: 1, 1: 1, 2: 1, 3: 1}, code=Op.GAS + Op.PUSH1[0x20] + Op.PUSH1[0x0] + Op.DUP2 + Op.DUP2 + Op.PUSH2[0x1000] + Op.CALLDATALOAD(offset=Op.DUP2) + Op.POP(Op.CALL(gas=Op.DUP7, address=Op.DUP7, value=Op.DUP1, args_offset=Op.DUP1, args_size=Op.DUP1, ret_offset=Op.DUP4, ret_size=Op.DUP4)) + Op.SSTORE(key=Op.DUP4, value=Op.LT(Op.GAS, Op.DUP7)) + Op.POP(Op.CALLCODE(gas=Op.DUP7, address=Op.DUP7, value=Op.DUP1, args_offset=Op.DUP1, args_size=Op.DUP1, ret_offset=Op.DUP4, ret_size=Op.DUP4)) + Op.SSTORE(key=0x1, value=Op.LT(Op.GAS, Op.DUP7)) + Op.POP(Op.DELEGATECALL(gas=Op.DUP6, address=Op.DUP6, args_offset=Op.DUP2, args_size=Op.DUP2, ret_offset=Op.DUP4, ret_size=Op.DUP4)) + Op.SSTORE(key=0x2, value=Op.LT(Op.GAS, Op.DUP7)) + Op.POP(Op.STATICCALL) + Op.GAS + Op.SSTORE(key=0x3, value=Op.LT) + Op.STOP)}),
        ("8fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", {Address("0x0000000000000000000000000000000000001000"): Account(code=Op.PUSH1[0x0] + Op.PUSH1[0xff] + Op.STOP), Address("0x000000000000000000000000000000000000c0de"): Account(storage={0: 1, 1: 1, 2: 1, 3: 1}, code=Op.GAS + Op.PUSH1[0x20] + Op.PUSH1[0x0] + Op.DUP2 + Op.DUP2 + Op.PUSH2[0x1000] + Op.CALLDATALOAD(offset=Op.DUP2) + Op.POP(Op.CALL(gas=Op.DUP7, address=Op.DUP7, value=Op.DUP1, args_offset=Op.DUP1, args_size=Op.DUP1, ret_offset=Op.DUP4, ret_size=Op.DUP4)) + Op.SSTORE(key=Op.DUP4, value=Op.LT(Op.GAS, Op.DUP7)) + Op.POP(Op.CALLCODE(gas=Op.DUP7, address=Op.DUP7, value=Op.DUP1, args_offset=Op.DUP1, args_size=Op.DUP1, ret_offset=Op.DUP4, ret_size=Op.DUP4)) + Op.SSTORE(key=0x1, value=Op.LT(Op.GAS, Op.DUP7)) + Op.POP(Op.DELEGATECALL(gas=Op.DUP6, address=Op.DUP6, args_offset=Op.DUP2, args_size=Op.DUP2, ret_offset=Op.DUP4, ret_size=Op.DUP4)) + Op.SSTORE(key=0x2, value=Op.LT(Op.GAS, Op.DUP7)) + Op.POP(Op.STATICCALL) + Op.GAS + Op.SSTORE(key=0x3, value=Op.LT) + Op.STOP)}),
        ("000000000000000000000000000000000000000000000000000000008fffffff", {Address("0x0000000000000000000000000000000000001000"): Account(code=Op.PUSH1[0x0] + Op.PUSH1[0xff] + Op.STOP), Address("0x000000000000000000000000000000000000c0de"): Account(storage={0: 1, 1: 1, 2: 1, 3: 1}, code=Op.GAS + Op.PUSH1[0x20] + Op.PUSH1[0x0] + Op.DUP2 + Op.DUP2 + Op.PUSH2[0x1000] + Op.CALLDATALOAD(offset=Op.DUP2) + Op.POP(Op.CALL(gas=Op.DUP7, address=Op.DUP7, value=Op.DUP1, args_offset=Op.DUP1, args_size=Op.DUP1, ret_offset=Op.DUP4, ret_size=Op.DUP4)) + Op.SSTORE(key=Op.DUP4, value=Op.LT(Op.GAS, Op.DUP7)) + Op.POP(Op.CALLCODE(gas=Op.DUP7, address=Op.DUP7, value=Op.DUP1, args_offset=Op.DUP1, args_size=Op.DUP1, ret_offset=Op.DUP4, ret_size=Op.DUP4)) + Op.SSTORE(key=0x1, value=Op.LT(Op.GAS, Op.DUP7)) + Op.POP(Op.DELEGATECALL(gas=Op.DUP6, address=Op.DUP6, args_offset=Op.DUP2, args_size=Op.DUP2, ret_offset=Op.DUP4, ret_size=Op.DUP4)) + Op.SSTORE(key=0x2, value=Op.LT(Op.GAS, Op.DUP7)) + Op.POP(Op.STATICCALL) + Op.GAS + Op.SSTORE(key=0x3, value=Op.LT) + Op.STOP)}),
        ("0000000000000000000000000000000000000000000000008fffffffffffffff", {Address("0x0000000000000000000000000000000000001000"): Account(code=Op.PUSH1[0x0] + Op.PUSH1[0xff] + Op.STOP), Address("0x000000000000000000000000000000000000c0de"): Account(storage={0: 1, 1: 1, 2: 1, 3: 1}, code=Op.GAS + Op.PUSH1[0x20] + Op.PUSH1[0x0] + Op.DUP2 + Op.DUP2 + Op.PUSH2[0x1000] + Op.CALLDATALOAD(offset=Op.DUP2) + Op.POP(Op.CALL(gas=Op.DUP7, address=Op.DUP7, value=Op.DUP1, args_offset=Op.DUP1, args_size=Op.DUP1, ret_offset=Op.DUP4, ret_size=Op.DUP4)) + Op.SSTORE(key=Op.DUP4, value=Op.LT(Op.GAS, Op.DUP7)) + Op.POP(Op.CALLCODE(gas=Op.DUP7, address=Op.DUP7, value=Op.DUP1, args_offset=Op.DUP1, args_size=Op.DUP1, ret_offset=Op.DUP4, ret_size=Op.DUP4)) + Op.SSTORE(key=0x1, value=Op.LT(Op.GAS, Op.DUP7)) + Op.POP(Op.DELEGATECALL(gas=Op.DUP6, address=Op.DUP6, args_offset=Op.DUP2, args_size=Op.DUP2, ret_offset=Op.DUP4, ret_size=Op.DUP4)) + Op.SSTORE(key=0x2, value=Op.LT(Op.GAS, Op.DUP7)) + Op.POP(Op.STATICCALL) + Op.GAS + Op.SSTORE(key=0x3, value=Op.LT) + Op.STOP)}),
        ("000000000000000000000000000000000000000000000000000000000000008f", {Address("0x0000000000000000000000000000000000001000"): Account(code=Op.PUSH1[0x0] + Op.PUSH1[0xff] + Op.STOP), Address("0x000000000000000000000000000000000000c0de"): Account(storage={0: 1, 1: 1, 2: 1, 3: 1}, code=Op.GAS + Op.PUSH1[0x20] + Op.PUSH1[0x0] + Op.DUP2 + Op.DUP2 + Op.PUSH2[0x1000] + Op.CALLDATALOAD(offset=Op.DUP2) + Op.POP(Op.CALL(gas=Op.DUP7, address=Op.DUP7, value=Op.DUP1, args_offset=Op.DUP1, args_size=Op.DUP1, ret_offset=Op.DUP4, ret_size=Op.DUP4)) + Op.SSTORE(key=Op.DUP4, value=Op.LT(Op.GAS, Op.DUP7)) + Op.POP(Op.CALLCODE(gas=Op.DUP7, address=Op.DUP7, value=Op.DUP1, args_offset=Op.DUP1, args_size=Op.DUP1, ret_offset=Op.DUP4, ret_size=Op.DUP4)) + Op.SSTORE(key=0x1, value=Op.LT(Op.GAS, Op.DUP7)) + Op.POP(Op.DELEGATECALL(gas=Op.DUP6, address=Op.DUP6, args_offset=Op.DUP2, args_size=Op.DUP2, ret_offset=Op.DUP4, ret_size=Op.DUP4)) + Op.SSTORE(key=0x2, value=Op.LT(Op.GAS, Op.DUP7)) + Op.POP(Op.STATICCALL) + Op.GAS + Op.SSTORE(key=0x3, value=Op.LT) + Op.STOP)}),
    ],
    ids=['case0', 'case1', 'case2', 'case3', 'case4', 'case5', 'case6', 'case7', 'case8', 'case9', 'case10', 'case11'],
)
@pytest.mark.pre_alloc_mutable
def test_transaction64_rule_integer_boundaries(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Danno Ferrin danno.ferrin@gmail.com."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x000000000000000000000000000000000000c0de")
    callee = Address("0x0000000000000000000000000000000000001000")

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
        code=Op.PUSH1[0x0] + Op.PUSH1[0xff] + Op.STOP,
    )
    pre[contract] = Account(
        balance=0xba1a9ce0ba1a9ce,
        nonce=0,
        code=(
        Op.GAS + Op.PUSH1[0x20] + Op.PUSH1[0x0] + Op.DUP2 + Op.DUP2
        + Op.PUSH2[0x1000] + Op.CALLDATALOAD(offset=Op.DUP2)
        + Op.POP(Op.CALL(gas=Op.DUP7, address=Op.DUP7, value=Op.DUP1, args_offset=Op.DUP1, args_size=Op.DUP1, ret_offset=Op.DUP4, ret_size=Op.DUP4))
        + Op.SSTORE(key=Op.DUP4, value=Op.LT(Op.GAS, Op.DUP7))
        + Op.POP(Op.CALLCODE(gas=Op.DUP7, address=Op.DUP7, value=Op.DUP1, args_offset=Op.DUP1, args_size=Op.DUP1, ret_offset=Op.DUP4, ret_size=Op.DUP4))
        + Op.SSTORE(key=0x1, value=Op.LT(Op.GAS, Op.DUP7))
        + Op.POP(Op.DELEGATECALL(gas=Op.DUP6, address=Op.DUP6, args_offset=Op.DUP2, args_size=Op.DUP2, ret_offset=Op.DUP4, ret_size=Op.DUP4))
        + Op.SSTORE(key=0x2, value=Op.LT(Op.GAS, Op.DUP7)) + Op.POP(Op.STATICCALL)
        + Op.GAS + Op.SSTORE(key=0x3, value=Op.LT) + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0x10000000000000000, nonce=0)

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=tx_data,
        gas_limit=800000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
