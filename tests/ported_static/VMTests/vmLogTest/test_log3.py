"""
Ori Pomerantz qbzzt1@gmail.com

Ported from:
tests/static/state_tests/VMTests/vmLogTest/log3Filler.yml
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
    ["tests/static/state_tests/VMTests/vmLogTest/log3Filler.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        ("693c61390000000000000000000000000000000000000000000000000000000000000007", {Address("0x0000000000000000000000000000000000001000"): Account(code=Op.LOG3(offset=0x0, size=0x0, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001001"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=Op.SUB(0x0, 0x1), size=0x1, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001002"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x1, size=Op.SUB(0x0, 0x1), topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001003"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x1, size=0x0, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001004"): Account(code=Op.MSTORE(offset=0x0, value=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) + Op.LOG3(offset=0x0, size=0x20, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001005"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x0, size=0x1, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001006"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x1f, size=0x1, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001007"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x0, size=0x20, topic_1=0x0, topic_2=0x0, topic_3=Op.CALLER) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001008"): Account(code=Op.MSTORE8(offset=0x0, value=0xff) + Op.LOG3(offset=0x1f, size=0x1, topic_1=Op.SUB(0x0, 0x1), topic_2=Op.SUB(0x0, 0x1), topic_3=Op.SUB(0x0, 0x1)) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001009"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x1f, size=0x1, topic_1=Op.PC, topic_2=Op.PC, topic_3=Op.PC) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(storage={0: 24589}, code=Op.DELEGATECALL(gas=Op.GAS, address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)), args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0) + Op.STOP)}),
        ("693c61390000000000000000000000000000000000000000000000000000000000000000", {Address("0x0000000000000000000000000000000000001000"): Account(code=Op.LOG3(offset=0x0, size=0x0, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001001"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=Op.SUB(0x0, 0x1), size=0x1, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001002"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x1, size=Op.SUB(0x0, 0x1), topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001003"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x1, size=0x0, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001004"): Account(code=Op.MSTORE(offset=0x0, value=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) + Op.LOG3(offset=0x0, size=0x20, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001005"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x0, size=0x1, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001006"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x1f, size=0x1, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001007"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x0, size=0x20, topic_1=0x0, topic_2=0x0, topic_3=Op.CALLER) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001008"): Account(code=Op.MSTORE8(offset=0x0, value=0xff) + Op.LOG3(offset=0x1f, size=0x1, topic_1=Op.SUB(0x0, 0x1), topic_2=Op.SUB(0x0, 0x1), topic_3=Op.SUB(0x0, 0x1)) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001009"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x1f, size=0x1, topic_1=Op.PC, topic_2=Op.PC, topic_3=Op.PC) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(storage={0: 24589}, code=Op.DELEGATECALL(gas=Op.GAS, address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)), args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0) + Op.STOP)}),
        ("693c61390000000000000000000000000000000000000000000000000000000000000005", {Address("0x0000000000000000000000000000000000001000"): Account(code=Op.LOG3(offset=0x0, size=0x0, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001001"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=Op.SUB(0x0, 0x1), size=0x1, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001002"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x1, size=Op.SUB(0x0, 0x1), topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001003"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x1, size=0x0, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001004"): Account(code=Op.MSTORE(offset=0x0, value=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) + Op.LOG3(offset=0x0, size=0x20, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001005"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x0, size=0x1, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001006"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x1f, size=0x1, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001007"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x0, size=0x20, topic_1=0x0, topic_2=0x0, topic_3=Op.CALLER) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001008"): Account(code=Op.MSTORE8(offset=0x0, value=0xff) + Op.LOG3(offset=0x1f, size=0x1, topic_1=Op.SUB(0x0, 0x1), topic_2=Op.SUB(0x0, 0x1), topic_3=Op.SUB(0x0, 0x1)) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001009"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x1f, size=0x1, topic_1=Op.PC, topic_2=Op.PC, topic_3=Op.PC) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(storage={0: 24589}, code=Op.DELEGATECALL(gas=Op.GAS, address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)), args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0) + Op.STOP)}),
        ("693c61390000000000000000000000000000000000000000000000000000000000000006", {Address("0x0000000000000000000000000000000000001000"): Account(code=Op.LOG3(offset=0x0, size=0x0, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001001"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=Op.SUB(0x0, 0x1), size=0x1, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001002"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x1, size=Op.SUB(0x0, 0x1), topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001003"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x1, size=0x0, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001004"): Account(code=Op.MSTORE(offset=0x0, value=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) + Op.LOG3(offset=0x0, size=0x20, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001005"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x0, size=0x1, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001006"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x1f, size=0x1, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001007"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x0, size=0x20, topic_1=0x0, topic_2=0x0, topic_3=Op.CALLER) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001008"): Account(code=Op.MSTORE8(offset=0x0, value=0xff) + Op.LOG3(offset=0x1f, size=0x1, topic_1=Op.SUB(0x0, 0x1), topic_2=Op.SUB(0x0, 0x1), topic_3=Op.SUB(0x0, 0x1)) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001009"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x1f, size=0x1, topic_1=Op.PC, topic_2=Op.PC, topic_3=Op.PC) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(storage={0: 24589}, code=Op.DELEGATECALL(gas=Op.GAS, address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)), args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0) + Op.STOP)}),
        ("693c61390000000000000000000000000000000000000000000000000000000000000008", {Address("0x0000000000000000000000000000000000001000"): Account(code=Op.LOG3(offset=0x0, size=0x0, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001001"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=Op.SUB(0x0, 0x1), size=0x1, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001002"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x1, size=Op.SUB(0x0, 0x1), topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001003"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x1, size=0x0, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001004"): Account(code=Op.MSTORE(offset=0x0, value=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) + Op.LOG3(offset=0x0, size=0x20, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001005"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x0, size=0x1, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001006"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x1f, size=0x1, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001007"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x0, size=0x20, topic_1=0x0, topic_2=0x0, topic_3=Op.CALLER) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001008"): Account(code=Op.MSTORE8(offset=0x0, value=0xff) + Op.LOG3(offset=0x1f, size=0x1, topic_1=Op.SUB(0x0, 0x1), topic_2=Op.SUB(0x0, 0x1), topic_3=Op.SUB(0x0, 0x1)) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001009"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x1f, size=0x1, topic_1=Op.PC, topic_2=Op.PC, topic_3=Op.PC) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(storage={0: 24589}, code=Op.DELEGATECALL(gas=Op.GAS, address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)), args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0) + Op.STOP)}),
        ("693c61390000000000000000000000000000000000000000000000000000000000000002", {Address("0x0000000000000000000000000000000000001000"): Account(code=Op.LOG3(offset=0x0, size=0x0, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001001"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=Op.SUB(0x0, 0x1), size=0x1, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001002"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x1, size=Op.SUB(0x0, 0x1), topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001003"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x1, size=0x0, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001004"): Account(code=Op.MSTORE(offset=0x0, value=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) + Op.LOG3(offset=0x0, size=0x20, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001005"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x0, size=0x1, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001006"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x1f, size=0x1, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001007"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x0, size=0x20, topic_1=0x0, topic_2=0x0, topic_3=Op.CALLER) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001008"): Account(code=Op.MSTORE8(offset=0x0, value=0xff) + Op.LOG3(offset=0x1f, size=0x1, topic_1=Op.SUB(0x0, 0x1), topic_2=Op.SUB(0x0, 0x1), topic_3=Op.SUB(0x0, 0x1)) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001009"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x1f, size=0x1, topic_1=Op.PC, topic_2=Op.PC, topic_3=Op.PC) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(storage={0: 2989}, code=Op.DELEGATECALL(gas=Op.GAS, address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)), args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0) + Op.STOP)}),
        ("693c61390000000000000000000000000000000000000000000000000000000000000003", {Address("0x0000000000000000000000000000000000001000"): Account(code=Op.LOG3(offset=0x0, size=0x0, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001001"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=Op.SUB(0x0, 0x1), size=0x1, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001002"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x1, size=Op.SUB(0x0, 0x1), topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001003"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x1, size=0x0, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001004"): Account(code=Op.MSTORE(offset=0x0, value=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) + Op.LOG3(offset=0x0, size=0x20, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001005"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x0, size=0x1, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001006"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x1f, size=0x1, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001007"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x0, size=0x20, topic_1=0x0, topic_2=0x0, topic_3=Op.CALLER) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001008"): Account(code=Op.MSTORE8(offset=0x0, value=0xff) + Op.LOG3(offset=0x1f, size=0x1, topic_1=Op.SUB(0x0, 0x1), topic_2=Op.SUB(0x0, 0x1), topic_3=Op.SUB(0x0, 0x1)) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001009"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x1f, size=0x1, topic_1=Op.PC, topic_2=Op.PC, topic_3=Op.PC) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(storage={0: 24589}, code=Op.DELEGATECALL(gas=Op.GAS, address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)), args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0) + Op.STOP)}),
        ("693c61390000000000000000000000000000000000000000000000000000000000000001", {Address("0x0000000000000000000000000000000000001000"): Account(code=Op.LOG3(offset=0x0, size=0x0, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001001"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=Op.SUB(0x0, 0x1), size=0x1, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001002"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x1, size=Op.SUB(0x0, 0x1), topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001003"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x1, size=0x0, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001004"): Account(code=Op.MSTORE(offset=0x0, value=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) + Op.LOG3(offset=0x0, size=0x20, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001005"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x0, size=0x1, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001006"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x1f, size=0x1, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001007"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x0, size=0x20, topic_1=0x0, topic_2=0x0, topic_3=Op.CALLER) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001008"): Account(code=Op.MSTORE8(offset=0x0, value=0xff) + Op.LOG3(offset=0x1f, size=0x1, topic_1=Op.SUB(0x0, 0x1), topic_2=Op.SUB(0x0, 0x1), topic_3=Op.SUB(0x0, 0x1)) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001009"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x1f, size=0x1, topic_1=Op.PC, topic_2=Op.PC, topic_3=Op.PC) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(storage={0: 2989}, code=Op.DELEGATECALL(gas=Op.GAS, address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)), args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0) + Op.STOP)}),
        ("693c61390000000000000000000000000000000000000000000000000000000000000004", {Address("0x0000000000000000000000000000000000001000"): Account(code=Op.LOG3(offset=0x0, size=0x0, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001001"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=Op.SUB(0x0, 0x1), size=0x1, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001002"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x1, size=Op.SUB(0x0, 0x1), topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001003"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x1, size=0x0, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001004"): Account(code=Op.MSTORE(offset=0x0, value=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) + Op.LOG3(offset=0x0, size=0x20, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001005"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x0, size=0x1, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001006"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x1f, size=0x1, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001007"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x0, size=0x20, topic_1=0x0, topic_2=0x0, topic_3=Op.CALLER) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001008"): Account(code=Op.MSTORE8(offset=0x0, value=0xff) + Op.LOG3(offset=0x1f, size=0x1, topic_1=Op.SUB(0x0, 0x1), topic_2=Op.SUB(0x0, 0x1), topic_3=Op.SUB(0x0, 0x1)) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001009"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x1f, size=0x1, topic_1=Op.PC, topic_2=Op.PC, topic_3=Op.PC) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(storage={0: 24589}, code=Op.DELEGATECALL(gas=Op.GAS, address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)), args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0) + Op.STOP)}),
        ("693c61390000000000000000000000000000000000000000000000000000000000000009", {Address("0x0000000000000000000000000000000000001000"): Account(code=Op.LOG3(offset=0x0, size=0x0, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001001"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=Op.SUB(0x0, 0x1), size=0x1, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001002"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x1, size=Op.SUB(0x0, 0x1), topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001003"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x1, size=0x0, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001004"): Account(code=Op.MSTORE(offset=0x0, value=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) + Op.LOG3(offset=0x0, size=0x20, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001005"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x0, size=0x1, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001006"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x1f, size=0x1, topic_1=0x0, topic_2=0x0, topic_3=0x0) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001007"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x0, size=0x20, topic_1=0x0, topic_2=0x0, topic_3=Op.CALLER) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001008"): Account(code=Op.MSTORE8(offset=0x0, value=0xff) + Op.LOG3(offset=0x1f, size=0x1, topic_1=Op.SUB(0x0, 0x1), topic_2=Op.SUB(0x0, 0x1), topic_3=Op.SUB(0x0, 0x1)) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0x0000000000000000000000000000000000001009"): Account(code=Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd) + Op.LOG3(offset=0x1f, size=0x1, topic_1=Op.PC, topic_2=Op.PC, topic_3=Op.PC) + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP), Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(storage={0: 24589}, code=Op.DELEGATECALL(gas=Op.GAS, address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)), args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0) + Op.STOP)}),
    ],
    ids=['case0', 'case1', 'case2', 'case3', 'case4', 'case5', 'case6', 'case7', 'case8', 'case9'],
)
@pytest.mark.pre_alloc_mutable
def test_log3(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Ori Pomerantz qbzzt1@gmail.com."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xcccccccccccccccccccccccccccccccccccccccc")
    callee = Address("0x0000000000000000000000000000000000001000")
    callee_1 = Address("0x0000000000000000000000000000000000001001")
    callee_2 = Address("0x0000000000000000000000000000000000001002")
    callee_3 = Address("0x0000000000000000000000000000000000001003")
    callee_4 = Address("0x0000000000000000000000000000000000001004")
    callee_5 = Address("0x0000000000000000000000000000000000001005")
    callee_6 = Address("0x0000000000000000000000000000000000001006")
    callee_7 = Address("0x0000000000000000000000000000000000001007")
    callee_8 = Address("0x0000000000000000000000000000000000001008")
    callee_9 = Address("0x0000000000000000000000000000000000001009")

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
        code=(
        Op.LOG3(offset=0x0, size=0x0, topic_1=0x0, topic_2=0x0, topic_3=0x0)
        + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP
    ),
    )
    pre[callee_1] = Account(
        balance=0xba1a9ce0ba1a9ce,
        nonce=0,
        code=(
        Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd)
        + Op.LOG3(offset=Op.SUB(0x0, 0x1), size=0x1, topic_1=0x0, topic_2=0x0, topic_3=0x0)
        + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP
    ),
    )
    pre[callee_2] = Account(
        balance=0xba1a9ce0ba1a9ce,
        nonce=0,
        code=(
        Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd)
        + Op.LOG3(offset=0x1, size=Op.SUB(0x0, 0x1), topic_1=0x0, topic_2=0x0, topic_3=0x0)
        + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP
    ),
    )
    pre[callee_3] = Account(
        balance=0xba1a9ce0ba1a9ce,
        nonce=0,
        code=(
        Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd)
        + Op.LOG3(offset=0x1, size=0x0, topic_1=0x0, topic_2=0x0, topic_3=0x0)
        + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP
    ),
    )
    pre[callee_4] = Account(
        balance=0xba1a9ce0ba1a9ce,
        nonce=0,
        code=(
        Op.MSTORE(offset=0x0, value=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
        + Op.LOG3(offset=0x0, size=0x20, topic_1=0x0, topic_2=0x0, topic_3=0x0)
        + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP
    ),
    )
    pre[callee_5] = Account(
        balance=0xba1a9ce0ba1a9ce,
        nonce=0,
        code=(
        Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd)
        + Op.LOG3(offset=0x0, size=0x1, topic_1=0x0, topic_2=0x0, topic_3=0x0)
        + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP
    ),
    )
    pre[callee_6] = Account(
        balance=0xba1a9ce0ba1a9ce,
        nonce=0,
        code=(
        Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd)
        + Op.LOG3(offset=0x1f, size=0x1, topic_1=0x0, topic_2=0x0, topic_3=0x0)
        + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP
    ),
    )
    pre[callee_7] = Account(
        balance=0xba1a9ce0ba1a9ce,
        nonce=0,
        code=(
        Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd)
        + Op.LOG3(offset=0x0, size=0x20, topic_1=0x0, topic_2=0x0, topic_3=Op.CALLER)
        + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP
    ),
    )
    pre[callee_8] = Account(
        balance=0xba1a9ce0ba1a9ce,
        nonce=0,
        code=(
        Op.MSTORE8(offset=0x0, value=0xff)
        + Op.LOG3(offset=0x1f, size=0x1, topic_1=Op.SUB(0x0, 0x1), topic_2=Op.SUB(0x0, 0x1), topic_3=Op.SUB(0x0, 0x1))
        + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP
    ),
    )
    pre[callee_9] = Account(
        balance=0xba1a9ce0ba1a9ce,
        nonce=0,
        code=(
        Op.MSTORE(offset=0x0, value=0xaabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd)
        + Op.LOG3(offset=0x1f, size=0x1, topic_1=Op.PC, topic_2=Op.PC, topic_3=Op.PC)
        + Op.SSTORE(key=0x0, value=0x600d) + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0x100000000000, nonce=0)
    pre[contract] = Account(
        balance=0xba1a9ce0ba1a9ce,
        nonce=0,
        code=(
        Op.DELEGATECALL(gas=Op.GAS, address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)), args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)
        + Op.STOP
    ),
        storage={0x0: 0xbad},
    )

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
