"""
Ported from:
tests/static/state_tests/stSpecialTest/eoaEmptyParisFiller.yml
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
    TransactionException,
)
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


@pytest.mark.ported_from(
    ["tests/static/state_tests/stSpecialTest/eoaEmptyParisFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, tx_gas_limit, tx_value, tx_error, expected_post",
    [
        pytest.param("693c61390000000000000000000000000000000000000000000000000000000000000000", 10000000, 0, None, {Address("0x000000000000000000000000000000000000bad4"): Account(storage={57005: 48879}), Address("0x000000000000000000000000000000000000c0de"): Account(storage={0: 0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b, 63: 0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470, 241: 118, 255: 7626, 47825: 0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470, 47826: 0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470, 47827: 0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470, 47828: 0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470}, code=Op.ORIGIN + Op.SSTORE(key=0x0, value=Op.DUP1) + Op.SSTORE(key=0x31, value=Op.BALANCE(address=Op.DUP1)) + Op.SSTORE(key=0x3b, value=Op.EXTCODESIZE(address=Op.DUP1)) + Op.SSTORE(key=0x3f, value=Op.EXTCODEHASH(address=Op.DUP1)) + Op.SSTORE(key=0x13f, value=Op.EXTCODEHASH(address=Op.ADD(Op.DUP2, 0x1))) + Op.SSTORE(key=0xbad1, value=Op.EXTCODEHASH(address=0xbad1)) + Op.SSTORE(key=0xbad2, value=Op.EXTCODEHASH(address=0xbad2)) + Op.SSTORE(key=0xbad3, value=Op.EXTCODEHASH(address=0xbad3)) + Op.SSTORE(key=0xbad4, value=Op.EXTCODEHASH(address=0xbad4)) + Op.SSTORE(key=0xbad5, value=Op.EXTCODEHASH(address=0xbad5)) + Op.PUSH1[0x0] + Op.DUP1 + Op.DUP1 + Op.DUP1 + Op.GAS + Op.SWAP5 + Op.CALLDATALOAD(offset=0x4) + Op.SWAP1 + Op.GAS + Op.POP(Op.CALL) + Op.GAS + Op.SWAP1 + Op.SSTORE(key=0xf1, value=Op.SUB) + Op.GAS + Op.POP(Op.CALL(gas=Op.GAS, address=0xdead, value=Op.DUP1, args_offset=Op.DUP1, args_size=Op.DUP1, ret_offset=Op.DUP1, ret_size=0x0)) + Op.GAS + Op.SWAP1 + Op.SSTORE(key=0xff, value=Op.SUB) + Op.STOP), Address("0x000000000000000000000000000000000000dead"): Account(code=Op.SELFDESTRUCT(address=Op.ORIGIN))}, id="case0"),
        pytest.param("693c61390000000000000000000000000000000000000000000000000000000000000000", 10000000, 100, TransactionException.INSUFFICIENT_ACCOUNT_FUNDS, {Address("0x000000000000000000000000000000000000bad4"): Account(storage={57005: 48879}), Address("0x000000000000000000000000000000000000c0de"): Account(code=Op.ORIGIN + Op.SSTORE(key=0x0, value=Op.DUP1) + Op.SSTORE(key=0x31, value=Op.BALANCE(address=Op.DUP1)) + Op.SSTORE(key=0x3b, value=Op.EXTCODESIZE(address=Op.DUP1)) + Op.SSTORE(key=0x3f, value=Op.EXTCODEHASH(address=Op.DUP1)) + Op.SSTORE(key=0x13f, value=Op.EXTCODEHASH(address=Op.ADD(Op.DUP2, 0x1))) + Op.SSTORE(key=0xbad1, value=Op.EXTCODEHASH(address=0xbad1)) + Op.SSTORE(key=0xbad2, value=Op.EXTCODEHASH(address=0xbad2)) + Op.SSTORE(key=0xbad3, value=Op.EXTCODEHASH(address=0xbad3)) + Op.SSTORE(key=0xbad4, value=Op.EXTCODEHASH(address=0xbad4)) + Op.SSTORE(key=0xbad5, value=Op.EXTCODEHASH(address=0xbad5)) + Op.PUSH1[0x0] + Op.DUP1 + Op.DUP1 + Op.DUP1 + Op.GAS + Op.SWAP5 + Op.CALLDATALOAD(offset=0x4) + Op.SWAP1 + Op.GAS + Op.POP(Op.CALL) + Op.GAS + Op.SWAP1 + Op.SSTORE(key=0xf1, value=Op.SUB) + Op.GAS + Op.POP(Op.CALL(gas=Op.GAS, address=0xdead, value=Op.DUP1, args_offset=Op.DUP1, args_size=Op.DUP1, ret_offset=Op.DUP1, ret_size=0x0)) + Op.GAS + Op.SWAP1 + Op.SSTORE(key=0xff, value=Op.SUB) + Op.STOP), Address("0x000000000000000000000000000000000000dead"): Account(code=Op.SELFDESTRUCT(address=Op.ORIGIN))}, id="case1", marks=pytest.mark.exception_test),
        pytest.param("693c61390000000000000000000000000000000000000000000000000000000000000000", 9999999, 0, None, {Address("0x000000000000000000000000000000000000bad4"): Account(storage={57005: 48879}), Address("0x000000000000000000000000000000000000c0de"): Account(storage={0: 0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b, 49: 100, 63: 0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470, 241: 118, 255: 7626, 47825: 0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470, 47826: 0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470, 47827: 0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470, 47828: 0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470}, code=Op.ORIGIN + Op.SSTORE(key=0x0, value=Op.DUP1) + Op.SSTORE(key=0x31, value=Op.BALANCE(address=Op.DUP1)) + Op.SSTORE(key=0x3b, value=Op.EXTCODESIZE(address=Op.DUP1)) + Op.SSTORE(key=0x3f, value=Op.EXTCODEHASH(address=Op.DUP1)) + Op.SSTORE(key=0x13f, value=Op.EXTCODEHASH(address=Op.ADD(Op.DUP2, 0x1))) + Op.SSTORE(key=0xbad1, value=Op.EXTCODEHASH(address=0xbad1)) + Op.SSTORE(key=0xbad2, value=Op.EXTCODEHASH(address=0xbad2)) + Op.SSTORE(key=0xbad3, value=Op.EXTCODEHASH(address=0xbad3)) + Op.SSTORE(key=0xbad4, value=Op.EXTCODEHASH(address=0xbad4)) + Op.SSTORE(key=0xbad5, value=Op.EXTCODEHASH(address=0xbad5)) + Op.PUSH1[0x0] + Op.DUP1 + Op.DUP1 + Op.DUP1 + Op.GAS + Op.SWAP5 + Op.CALLDATALOAD(offset=0x4) + Op.SWAP1 + Op.GAS + Op.POP(Op.CALL) + Op.GAS + Op.SWAP1 + Op.SSTORE(key=0xf1, value=Op.SUB) + Op.GAS + Op.POP(Op.CALL(gas=Op.GAS, address=0xdead, value=Op.DUP1, args_offset=Op.DUP1, args_size=Op.DUP1, ret_offset=Op.DUP1, ret_size=0x0)) + Op.GAS + Op.SWAP1 + Op.SSTORE(key=0xff, value=Op.SUB) + Op.STOP), Address("0x000000000000000000000000000000000000dead"): Account(code=Op.SELFDESTRUCT(address=Op.ORIGIN))}, id="case2"),
        pytest.param("693c61390000000000000000000000000000000000000000000000000000000000000000", 9999999, 100, None, {Address("0x000000000000000000000000000000000000bad4"): Account(storage={57005: 48879}), Address("0x000000000000000000000000000000000000c0de"): Account(storage={0: 0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b, 63: 0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470, 241: 118, 255: 7626, 47825: 0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470, 47826: 0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470, 47827: 0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470, 47828: 0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470}, code=Op.ORIGIN + Op.SSTORE(key=0x0, value=Op.DUP1) + Op.SSTORE(key=0x31, value=Op.BALANCE(address=Op.DUP1)) + Op.SSTORE(key=0x3b, value=Op.EXTCODESIZE(address=Op.DUP1)) + Op.SSTORE(key=0x3f, value=Op.EXTCODEHASH(address=Op.DUP1)) + Op.SSTORE(key=0x13f, value=Op.EXTCODEHASH(address=Op.ADD(Op.DUP2, 0x1))) + Op.SSTORE(key=0xbad1, value=Op.EXTCODEHASH(address=0xbad1)) + Op.SSTORE(key=0xbad2, value=Op.EXTCODEHASH(address=0xbad2)) + Op.SSTORE(key=0xbad3, value=Op.EXTCODEHASH(address=0xbad3)) + Op.SSTORE(key=0xbad4, value=Op.EXTCODEHASH(address=0xbad4)) + Op.SSTORE(key=0xbad5, value=Op.EXTCODEHASH(address=0xbad5)) + Op.PUSH1[0x0] + Op.DUP1 + Op.DUP1 + Op.DUP1 + Op.GAS + Op.SWAP5 + Op.CALLDATALOAD(offset=0x4) + Op.SWAP1 + Op.GAS + Op.POP(Op.CALL) + Op.GAS + Op.SWAP1 + Op.SSTORE(key=0xf1, value=Op.SUB) + Op.GAS + Op.POP(Op.CALL(gas=Op.GAS, address=0xdead, value=Op.DUP1, args_offset=Op.DUP1, args_size=Op.DUP1, ret_offset=Op.DUP1, ret_size=0x0)) + Op.GAS + Op.SWAP1 + Op.SSTORE(key=0xff, value=Op.SUB) + Op.STOP), Address("0x000000000000000000000000000000000000dead"): Account(code=Op.SELFDESTRUCT(address=Op.ORIGIN))}, id="case3"),
        pytest.param("693c61390000000000000000000000000000000000000000000000000000000000000001", 10000000, 0, None, {Address("0x000000000000000000000000000000000000bad4"): Account(storage={57005: 48879}), Address("0x000000000000000000000000000000000000c0de"): Account(storage={0: 0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b, 63: 0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470, 241: 6818, 255: 7626, 47825: 0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470, 47826: 0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470, 47827: 0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470, 47828: 0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470}, code=Op.ORIGIN + Op.SSTORE(key=0x0, value=Op.DUP1) + Op.SSTORE(key=0x31, value=Op.BALANCE(address=Op.DUP1)) + Op.SSTORE(key=0x3b, value=Op.EXTCODESIZE(address=Op.DUP1)) + Op.SSTORE(key=0x3f, value=Op.EXTCODEHASH(address=Op.DUP1)) + Op.SSTORE(key=0x13f, value=Op.EXTCODEHASH(address=Op.ADD(Op.DUP2, 0x1))) + Op.SSTORE(key=0xbad1, value=Op.EXTCODEHASH(address=0xbad1)) + Op.SSTORE(key=0xbad2, value=Op.EXTCODEHASH(address=0xbad2)) + Op.SSTORE(key=0xbad3, value=Op.EXTCODEHASH(address=0xbad3)) + Op.SSTORE(key=0xbad4, value=Op.EXTCODEHASH(address=0xbad4)) + Op.SSTORE(key=0xbad5, value=Op.EXTCODEHASH(address=0xbad5)) + Op.PUSH1[0x0] + Op.DUP1 + Op.DUP1 + Op.DUP1 + Op.GAS + Op.SWAP5 + Op.CALLDATALOAD(offset=0x4) + Op.SWAP1 + Op.GAS + Op.POP(Op.CALL) + Op.GAS + Op.SWAP1 + Op.SSTORE(key=0xf1, value=Op.SUB) + Op.GAS + Op.POP(Op.CALL(gas=Op.GAS, address=0xdead, value=Op.DUP1, args_offset=Op.DUP1, args_size=Op.DUP1, ret_offset=Op.DUP1, ret_size=0x0)) + Op.GAS + Op.SWAP1 + Op.SSTORE(key=0xff, value=Op.SUB) + Op.STOP), Address("0x000000000000000000000000000000000000dead"): Account(code=Op.SELFDESTRUCT(address=Op.ORIGIN))}, id="case4"),
        pytest.param("693c61390000000000000000000000000000000000000000000000000000000000000001", 10000000, 100, TransactionException.INSUFFICIENT_ACCOUNT_FUNDS, {Address("0x000000000000000000000000000000000000bad4"): Account(storage={57005: 48879}), Address("0x000000000000000000000000000000000000c0de"): Account(code=Op.ORIGIN + Op.SSTORE(key=0x0, value=Op.DUP1) + Op.SSTORE(key=0x31, value=Op.BALANCE(address=Op.DUP1)) + Op.SSTORE(key=0x3b, value=Op.EXTCODESIZE(address=Op.DUP1)) + Op.SSTORE(key=0x3f, value=Op.EXTCODEHASH(address=Op.DUP1)) + Op.SSTORE(key=0x13f, value=Op.EXTCODEHASH(address=Op.ADD(Op.DUP2, 0x1))) + Op.SSTORE(key=0xbad1, value=Op.EXTCODEHASH(address=0xbad1)) + Op.SSTORE(key=0xbad2, value=Op.EXTCODEHASH(address=0xbad2)) + Op.SSTORE(key=0xbad3, value=Op.EXTCODEHASH(address=0xbad3)) + Op.SSTORE(key=0xbad4, value=Op.EXTCODEHASH(address=0xbad4)) + Op.SSTORE(key=0xbad5, value=Op.EXTCODEHASH(address=0xbad5)) + Op.PUSH1[0x0] + Op.DUP1 + Op.DUP1 + Op.DUP1 + Op.GAS + Op.SWAP5 + Op.CALLDATALOAD(offset=0x4) + Op.SWAP1 + Op.GAS + Op.POP(Op.CALL) + Op.GAS + Op.SWAP1 + Op.SSTORE(key=0xf1, value=Op.SUB) + Op.GAS + Op.POP(Op.CALL(gas=Op.GAS, address=0xdead, value=Op.DUP1, args_offset=Op.DUP1, args_size=Op.DUP1, ret_offset=Op.DUP1, ret_size=0x0)) + Op.GAS + Op.SWAP1 + Op.SSTORE(key=0xff, value=Op.SUB) + Op.STOP), Address("0x000000000000000000000000000000000000dead"): Account(code=Op.SELFDESTRUCT(address=Op.ORIGIN))}, id="case5", marks=pytest.mark.exception_test),
        pytest.param("693c61390000000000000000000000000000000000000000000000000000000000000001", 9999999, 0, None, {Address("0x000000000000000000000000000000000000bad4"): Account(storage={57005: 48879}), Address("0x000000000000000000000000000000000000c0de"): Account(storage={0: 0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b, 49: 100, 63: 0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470, 241: 6818, 255: 7626, 47825: 0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470, 47826: 0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470, 47827: 0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470, 47828: 0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470}, code=Op.ORIGIN + Op.SSTORE(key=0x0, value=Op.DUP1) + Op.SSTORE(key=0x31, value=Op.BALANCE(address=Op.DUP1)) + Op.SSTORE(key=0x3b, value=Op.EXTCODESIZE(address=Op.DUP1)) + Op.SSTORE(key=0x3f, value=Op.EXTCODEHASH(address=Op.DUP1)) + Op.SSTORE(key=0x13f, value=Op.EXTCODEHASH(address=Op.ADD(Op.DUP2, 0x1))) + Op.SSTORE(key=0xbad1, value=Op.EXTCODEHASH(address=0xbad1)) + Op.SSTORE(key=0xbad2, value=Op.EXTCODEHASH(address=0xbad2)) + Op.SSTORE(key=0xbad3, value=Op.EXTCODEHASH(address=0xbad3)) + Op.SSTORE(key=0xbad4, value=Op.EXTCODEHASH(address=0xbad4)) + Op.SSTORE(key=0xbad5, value=Op.EXTCODEHASH(address=0xbad5)) + Op.PUSH1[0x0] + Op.DUP1 + Op.DUP1 + Op.DUP1 + Op.GAS + Op.SWAP5 + Op.CALLDATALOAD(offset=0x4) + Op.SWAP1 + Op.GAS + Op.POP(Op.CALL) + Op.GAS + Op.SWAP1 + Op.SSTORE(key=0xf1, value=Op.SUB) + Op.GAS + Op.POP(Op.CALL(gas=Op.GAS, address=0xdead, value=Op.DUP1, args_offset=Op.DUP1, args_size=Op.DUP1, ret_offset=Op.DUP1, ret_size=0x0)) + Op.GAS + Op.SWAP1 + Op.SSTORE(key=0xff, value=Op.SUB) + Op.STOP), Address("0x000000000000000000000000000000000000dead"): Account(code=Op.SELFDESTRUCT(address=Op.ORIGIN))}, id="case6"),
        pytest.param("693c61390000000000000000000000000000000000000000000000000000000000000001", 9999999, 100, None, {Address("0x000000000000000000000000000000000000bad4"): Account(storage={57005: 48879}), Address("0x000000000000000000000000000000000000c0de"): Account(storage={0: 0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b, 63: 0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470, 241: 6818, 255: 7626, 47825: 0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470, 47826: 0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470, 47827: 0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470, 47828: 0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470}, code=Op.ORIGIN + Op.SSTORE(key=0x0, value=Op.DUP1) + Op.SSTORE(key=0x31, value=Op.BALANCE(address=Op.DUP1)) + Op.SSTORE(key=0x3b, value=Op.EXTCODESIZE(address=Op.DUP1)) + Op.SSTORE(key=0x3f, value=Op.EXTCODEHASH(address=Op.DUP1)) + Op.SSTORE(key=0x13f, value=Op.EXTCODEHASH(address=Op.ADD(Op.DUP2, 0x1))) + Op.SSTORE(key=0xbad1, value=Op.EXTCODEHASH(address=0xbad1)) + Op.SSTORE(key=0xbad2, value=Op.EXTCODEHASH(address=0xbad2)) + Op.SSTORE(key=0xbad3, value=Op.EXTCODEHASH(address=0xbad3)) + Op.SSTORE(key=0xbad4, value=Op.EXTCODEHASH(address=0xbad4)) + Op.SSTORE(key=0xbad5, value=Op.EXTCODEHASH(address=0xbad5)) + Op.PUSH1[0x0] + Op.DUP1 + Op.DUP1 + Op.DUP1 + Op.GAS + Op.SWAP5 + Op.CALLDATALOAD(offset=0x4) + Op.SWAP1 + Op.GAS + Op.POP(Op.CALL) + Op.GAS + Op.SWAP1 + Op.SSTORE(key=0xf1, value=Op.SUB) + Op.GAS + Op.POP(Op.CALL(gas=Op.GAS, address=0xdead, value=Op.DUP1, args_offset=Op.DUP1, args_size=Op.DUP1, ret_offset=Op.DUP1, ret_size=0x0)) + Op.GAS + Op.SWAP1 + Op.SSTORE(key=0xff, value=Op.SUB) + Op.STOP), Address("0x000000000000000000000000000000000000dead"): Account(code=Op.SELFDESTRUCT(address=Op.ORIGIN))}, id="case7"),
    ],
)
@pytest.mark.pre_alloc_mutable
def test_eoa_empty_paris(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    tx_gas_limit: int,
    tx_value: int,
    tx_error,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x000000000000000000000000000000000000c0de")
    callee = Address("0x000000000000000000000000000000000000bad1")
    callee_1 = Address("0x000000000000000000000000000000000000bad2")
    callee_2 = Address("0x000000000000000000000000000000000000bad3")
    callee_3 = Address("0x000000000000000000000000000000000000bad4")
    callee_4 = Address("0x000000000000000000000000000000000000dead")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=89128960,
    )

    pre[callee] = Account(balance=1, nonce=0)
    pre[callee_1] = Account(balance=0, nonce=1)
    pre[callee_2] = Account(balance=1, nonce=1)
    pre[callee_3] = Account(balance=10, nonce=0, storage={0xdead: 0xbeef})
    pre[contract] = Account(
        balance=0,
        nonce=1,
        code=(
        Op.ORIGIN + Op.SSTORE(key=0x0, value=Op.DUP1)
        + Op.SSTORE(key=0x31, value=Op.BALANCE(address=Op.DUP1))
        + Op.SSTORE(key=0x3b, value=Op.EXTCODESIZE(address=Op.DUP1))
        + Op.SSTORE(key=0x3f, value=Op.EXTCODEHASH(address=Op.DUP1))
        + Op.SSTORE(key=0x13f, value=Op.EXTCODEHASH(address=Op.ADD(Op.DUP2, 0x1)))
        + Op.SSTORE(key=0xbad1, value=Op.EXTCODEHASH(address=0xbad1))
        + Op.SSTORE(key=0xbad2, value=Op.EXTCODEHASH(address=0xbad2))
        + Op.SSTORE(key=0xbad3, value=Op.EXTCODEHASH(address=0xbad3))
        + Op.SSTORE(key=0xbad4, value=Op.EXTCODEHASH(address=0xbad4))
        + Op.SSTORE(key=0xbad5, value=Op.EXTCODEHASH(address=0xbad5)) + Op.PUSH1[0x0]
        + Op.DUP1 + Op.DUP1 + Op.DUP1 + Op.GAS + Op.SWAP5
        + Op.CALLDATALOAD(offset=0x4) + Op.SWAP1 + Op.GAS + Op.POP(Op.CALL) + Op.GAS
        + Op.SWAP1 + Op.SSTORE(key=0xf1, value=Op.SUB) + Op.GAS
        + Op.POP(Op.CALL(gas=Op.GAS, address=0xdead, value=Op.DUP1, args_offset=Op.DUP1, args_size=Op.DUP1, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.GAS + Op.SWAP1 + Op.SSTORE(key=0xff, value=Op.SUB) + Op.STOP
    ),
    )
    pre[callee_4] = Account(balance=0x2710, nonce=1, code=Op.SELFDESTRUCT(address=Op.ORIGIN))
    pre[sender] = Account(balance=0x3b9aca00, nonce=0)

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=tx_data,
        gas_limit=tx_gas_limit,
        gas_price=100,
        nonce=0,
        value=tx_value,
        error=tx_error,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
