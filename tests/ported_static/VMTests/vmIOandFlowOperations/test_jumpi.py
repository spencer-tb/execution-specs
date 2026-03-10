"""
Ori Pomerantz qbzzt1@gmail.com.

Ported from:
tests/static/state_tests/VMTests/vmIOandFlowOperations/jumpiFiller.yml
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
    ["tests/static/state_tests/VMTests/vmIOandFlowOperations/jumpiFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        (
            "693c61390000000000000000000000000000000000000000000000000000000000001005",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000110"): Account(
                    code=Op.JUMPI(pc=0xE, condition=0x1)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000000111"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.MSTORE(offset=0x0, value=0x10)
                    + Op.JUMPDEST
                    + Op.SUB(Op.MLOAD(offset=0x0), 0x1)
                    + Op.MSTORE(offset=0x0, value=Op.DUP1)
                    + Op.PUSH1[0xB]
                    + Op.JUMPI
                ),
                Address("0x0000000000000000000000000000000000000200"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000201"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000202"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000203"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0x0)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000208"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x0)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0xFF)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.PUSH1[0x23]
                    + Op.JUMPI(pc=0x8, condition=0x1)
                    + Op.PUSH1[0x1]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x2]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x6, condition=0x6)
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.PUSH2[0x600D]
                    + Op.JUMPI(pc=0xA, condition=0x1)
                    + Op.PUSH1[0xFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.JUMP(pc=0xB)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x3, condition=0x1)
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x5B]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x1]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xD, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xB, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x1)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 2989},
                    code=Op.DELEGATECALL(
                        gas=0x10000,
                        address=Op.CALLDATALOAD(offset=0x4),
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP,
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000100a",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000110"): Account(
                    code=Op.JUMPI(pc=0xE, condition=0x1)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000000111"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.MSTORE(offset=0x0, value=0x10)
                    + Op.JUMPDEST
                    + Op.SUB(Op.MLOAD(offset=0x0), 0x1)
                    + Op.MSTORE(offset=0x0, value=Op.DUP1)
                    + Op.PUSH1[0xB]
                    + Op.JUMPI
                ),
                Address("0x0000000000000000000000000000000000000200"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000201"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000202"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000203"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0x0)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000208"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x0)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0xFF)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.PUSH1[0x23]
                    + Op.JUMPI(pc=0x8, condition=0x1)
                    + Op.PUSH1[0x1]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x2]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x6, condition=0x6)
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.PUSH2[0x600D]
                    + Op.JUMPI(pc=0xA, condition=0x1)
                    + Op.PUSH1[0xFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.JUMP(pc=0xB)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x3, condition=0x1)
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x5B]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x1]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xD, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xB, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x1)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 2989},
                    code=Op.DELEGATECALL(
                        gas=0x10000,
                        address=Op.CALLDATALOAD(offset=0x4),
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP,
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000001009",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000110"): Account(
                    code=Op.JUMPI(pc=0xE, condition=0x1)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000000111"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.MSTORE(offset=0x0, value=0x10)
                    + Op.JUMPDEST
                    + Op.SUB(Op.MLOAD(offset=0x0), 0x1)
                    + Op.MSTORE(offset=0x0, value=Op.DUP1)
                    + Op.PUSH1[0xB]
                    + Op.JUMPI
                ),
                Address("0x0000000000000000000000000000000000000200"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000201"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000202"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000203"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0x0)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000208"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x0)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0xFF)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.PUSH1[0x23]
                    + Op.JUMPI(pc=0x8, condition=0x1)
                    + Op.PUSH1[0x1]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x2]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x6, condition=0x6)
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.PUSH2[0x600D]
                    + Op.JUMPI(pc=0xA, condition=0x1)
                    + Op.PUSH1[0xFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.JUMP(pc=0xB)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x3, condition=0x1)
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x5B]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x1]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xD, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xB, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x1)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 2989},
                    code=Op.DELEGATECALL(
                        gas=0x10000,
                        address=Op.CALLDATALOAD(offset=0x4),
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP,
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000001007",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000110"): Account(
                    code=Op.JUMPI(pc=0xE, condition=0x1)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000000111"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.MSTORE(offset=0x0, value=0x10)
                    + Op.JUMPDEST
                    + Op.SUB(Op.MLOAD(offset=0x0), 0x1)
                    + Op.MSTORE(offset=0x0, value=Op.DUP1)
                    + Op.PUSH1[0xB]
                    + Op.JUMPI
                ),
                Address("0x0000000000000000000000000000000000000200"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000201"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000202"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000203"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0x0)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000208"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x0)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0xFF)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.PUSH1[0x23]
                    + Op.JUMPI(pc=0x8, condition=0x1)
                    + Op.PUSH1[0x1]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x2]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x6, condition=0x6)
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.PUSH2[0x600D]
                    + Op.JUMPI(pc=0xA, condition=0x1)
                    + Op.PUSH1[0xFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.JUMP(pc=0xB)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x3, condition=0x1)
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x5B]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x1]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xD, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xB, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x1)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 24589},
                    code=Op.DELEGATECALL(
                        gas=0x10000,
                        address=Op.CALLDATALOAD(offset=0x4),
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP,
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000001006",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000110"): Account(
                    code=Op.JUMPI(pc=0xE, condition=0x1)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000000111"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.MSTORE(offset=0x0, value=0x10)
                    + Op.JUMPDEST
                    + Op.SUB(Op.MLOAD(offset=0x0), 0x1)
                    + Op.MSTORE(offset=0x0, value=Op.DUP1)
                    + Op.PUSH1[0xB]
                    + Op.JUMPI
                ),
                Address("0x0000000000000000000000000000000000000200"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000201"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000202"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000203"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0x0)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000208"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x0)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0xFF)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.PUSH1[0x23]
                    + Op.JUMPI(pc=0x8, condition=0x1)
                    + Op.PUSH1[0x1]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x2]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x6, condition=0x6)
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.PUSH2[0x600D]
                    + Op.JUMPI(pc=0xA, condition=0x1)
                    + Op.PUSH1[0xFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.JUMP(pc=0xB)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x3, condition=0x1)
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x5B]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x1]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xD, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xB, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x1)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 24589},
                    code=Op.DELEGATECALL(
                        gas=0x10000,
                        address=Op.CALLDATALOAD(offset=0x4),
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP,
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000001008",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000110"): Account(
                    code=Op.JUMPI(pc=0xE, condition=0x1)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000000111"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.MSTORE(offset=0x0, value=0x10)
                    + Op.JUMPDEST
                    + Op.SUB(Op.MLOAD(offset=0x0), 0x1)
                    + Op.MSTORE(offset=0x0, value=Op.DUP1)
                    + Op.PUSH1[0xB]
                    + Op.JUMPI
                ),
                Address("0x0000000000000000000000000000000000000200"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000201"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000202"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000203"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0x0)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000208"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x0)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0xFF)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.PUSH1[0x23]
                    + Op.JUMPI(pc=0x8, condition=0x1)
                    + Op.PUSH1[0x1]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x2]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x6, condition=0x6)
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.PUSH2[0x600D]
                    + Op.JUMPI(pc=0xA, condition=0x1)
                    + Op.PUSH1[0xFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.JUMP(pc=0xB)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x3, condition=0x1)
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x5B]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x1]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xD, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xB, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x1)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 24589},
                    code=Op.DELEGATECALL(
                        gas=0x10000,
                        address=Op.CALLDATALOAD(offset=0x4),
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP,
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000001001",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000110"): Account(
                    code=Op.JUMPI(pc=0xE, condition=0x1)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000000111"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.MSTORE(offset=0x0, value=0x10)
                    + Op.JUMPDEST
                    + Op.SUB(Op.MLOAD(offset=0x0), 0x1)
                    + Op.MSTORE(offset=0x0, value=Op.DUP1)
                    + Op.PUSH1[0xB]
                    + Op.JUMPI
                ),
                Address("0x0000000000000000000000000000000000000200"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000201"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000202"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000203"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0x0)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000208"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x0)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0xFF)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.PUSH1[0x23]
                    + Op.JUMPI(pc=0x8, condition=0x1)
                    + Op.PUSH1[0x1]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x2]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x6, condition=0x6)
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.PUSH2[0x600D]
                    + Op.JUMPI(pc=0xA, condition=0x1)
                    + Op.PUSH1[0xFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.JUMP(pc=0xB)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x3, condition=0x1)
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x5B]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x1]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xD, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xB, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x1)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 2989},
                    code=Op.DELEGATECALL(
                        gas=0x10000,
                        address=Op.CALLDATALOAD(offset=0x4),
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP,
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000001003",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000110"): Account(
                    code=Op.JUMPI(pc=0xE, condition=0x1)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000000111"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.MSTORE(offset=0x0, value=0x10)
                    + Op.JUMPDEST
                    + Op.SUB(Op.MLOAD(offset=0x0), 0x1)
                    + Op.MSTORE(offset=0x0, value=Op.DUP1)
                    + Op.PUSH1[0xB]
                    + Op.JUMPI
                ),
                Address("0x0000000000000000000000000000000000000200"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000201"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000202"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000203"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0x0)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000208"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x0)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0xFF)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.PUSH1[0x23]
                    + Op.JUMPI(pc=0x8, condition=0x1)
                    + Op.PUSH1[0x1]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x2]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x6, condition=0x6)
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.PUSH2[0x600D]
                    + Op.JUMPI(pc=0xA, condition=0x1)
                    + Op.PUSH1[0xFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.JUMP(pc=0xB)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x3, condition=0x1)
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x5B]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x1]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xD, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xB, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x1)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 2989},
                    code=Op.DELEGATECALL(
                        gas=0x10000,
                        address=Op.CALLDATALOAD(offset=0x4),
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP,
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000100d",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000110"): Account(
                    code=Op.JUMPI(pc=0xE, condition=0x1)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000000111"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.MSTORE(offset=0x0, value=0x10)
                    + Op.JUMPDEST
                    + Op.SUB(Op.MLOAD(offset=0x0), 0x1)
                    + Op.MSTORE(offset=0x0, value=Op.DUP1)
                    + Op.PUSH1[0xB]
                    + Op.JUMPI
                ),
                Address("0x0000000000000000000000000000000000000200"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000201"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000202"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000203"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0x0)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000208"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x0)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0xFF)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.PUSH1[0x23]
                    + Op.JUMPI(pc=0x8, condition=0x1)
                    + Op.PUSH1[0x1]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x2]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x6, condition=0x6)
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.PUSH2[0x600D]
                    + Op.JUMPI(pc=0xA, condition=0x1)
                    + Op.PUSH1[0xFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.JUMP(pc=0xB)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x3, condition=0x1)
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x5B]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x1]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xD, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xB, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x1)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 2989},
                    code=Op.DELEGATECALL(
                        gas=0x10000,
                        address=Op.CALLDATALOAD(offset=0x4),
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP,
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000100e",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000110"): Account(
                    code=Op.JUMPI(pc=0xE, condition=0x1)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000000111"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.MSTORE(offset=0x0, value=0x10)
                    + Op.JUMPDEST
                    + Op.SUB(Op.MLOAD(offset=0x0), 0x1)
                    + Op.MSTORE(offset=0x0, value=Op.DUP1)
                    + Op.PUSH1[0xB]
                    + Op.JUMPI
                ),
                Address("0x0000000000000000000000000000000000000200"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000201"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000202"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000203"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0x0)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000208"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x0)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0xFF)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.PUSH1[0x23]
                    + Op.JUMPI(pc=0x8, condition=0x1)
                    + Op.PUSH1[0x1]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x2]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x6, condition=0x6)
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.PUSH2[0x600D]
                    + Op.JUMPI(pc=0xA, condition=0x1)
                    + Op.PUSH1[0xFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.JUMP(pc=0xB)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x3, condition=0x1)
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x5B]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x1]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xD, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xB, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x1)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 2989},
                    code=Op.DELEGATECALL(
                        gas=0x10000,
                        address=Op.CALLDATALOAD(offset=0x4),
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP,
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000100f",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000110"): Account(
                    code=Op.JUMPI(pc=0xE, condition=0x1)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000000111"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.MSTORE(offset=0x0, value=0x10)
                    + Op.JUMPDEST
                    + Op.SUB(Op.MLOAD(offset=0x0), 0x1)
                    + Op.MSTORE(offset=0x0, value=Op.DUP1)
                    + Op.PUSH1[0xB]
                    + Op.JUMPI
                ),
                Address("0x0000000000000000000000000000000000000200"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000201"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000202"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000203"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0x0)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000208"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x0)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0xFF)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.PUSH1[0x23]
                    + Op.JUMPI(pc=0x8, condition=0x1)
                    + Op.PUSH1[0x1]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x2]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x6, condition=0x6)
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.PUSH2[0x600D]
                    + Op.JUMPI(pc=0xA, condition=0x1)
                    + Op.PUSH1[0xFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.JUMP(pc=0xB)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x3, condition=0x1)
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x5B]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x1]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xD, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xB, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x1)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 2989},
                    code=Op.DELEGATECALL(
                        gas=0x10000,
                        address=Op.CALLDATALOAD(offset=0x4),
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP,
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000001000",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000110"): Account(
                    code=Op.JUMPI(pc=0xE, condition=0x1)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000000111"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.MSTORE(offset=0x0, value=0x10)
                    + Op.JUMPDEST
                    + Op.SUB(Op.MLOAD(offset=0x0), 0x1)
                    + Op.MSTORE(offset=0x0, value=Op.DUP1)
                    + Op.PUSH1[0xB]
                    + Op.JUMPI
                ),
                Address("0x0000000000000000000000000000000000000200"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000201"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000202"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000203"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0x0)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000208"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x0)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0xFF)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.PUSH1[0x23]
                    + Op.JUMPI(pc=0x8, condition=0x1)
                    + Op.PUSH1[0x1]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x2]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x6, condition=0x6)
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.PUSH2[0x600D]
                    + Op.JUMPI(pc=0xA, condition=0x1)
                    + Op.PUSH1[0xFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.JUMP(pc=0xB)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x3, condition=0x1)
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x5B]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x1]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xD, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xB, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x1)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 2989},
                    code=Op.DELEGATECALL(
                        gas=0x10000,
                        address=Op.CALLDATALOAD(offset=0x4),
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP,
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000100b",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000110"): Account(
                    code=Op.JUMPI(pc=0xE, condition=0x1)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000000111"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.MSTORE(offset=0x0, value=0x10)
                    + Op.JUMPDEST
                    + Op.SUB(Op.MLOAD(offset=0x0), 0x1)
                    + Op.MSTORE(offset=0x0, value=Op.DUP1)
                    + Op.PUSH1[0xB]
                    + Op.JUMPI
                ),
                Address("0x0000000000000000000000000000000000000200"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000201"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000202"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000203"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0x0)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000208"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x0)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0xFF)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.PUSH1[0x23]
                    + Op.JUMPI(pc=0x8, condition=0x1)
                    + Op.PUSH1[0x1]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x2]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x6, condition=0x6)
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.PUSH2[0x600D]
                    + Op.JUMPI(pc=0xA, condition=0x1)
                    + Op.PUSH1[0xFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.JUMP(pc=0xB)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x3, condition=0x1)
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x5B]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x1]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xD, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xB, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x1)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 2989},
                    code=Op.DELEGATECALL(
                        gas=0x10000,
                        address=Op.CALLDATALOAD(offset=0x4),
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP,
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000100c",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000110"): Account(
                    code=Op.JUMPI(pc=0xE, condition=0x1)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000000111"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.MSTORE(offset=0x0, value=0x10)
                    + Op.JUMPDEST
                    + Op.SUB(Op.MLOAD(offset=0x0), 0x1)
                    + Op.MSTORE(offset=0x0, value=Op.DUP1)
                    + Op.PUSH1[0xB]
                    + Op.JUMPI
                ),
                Address("0x0000000000000000000000000000000000000200"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000201"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000202"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000203"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0x0)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000208"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x0)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0xFF)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.PUSH1[0x23]
                    + Op.JUMPI(pc=0x8, condition=0x1)
                    + Op.PUSH1[0x1]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x2]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x6, condition=0x6)
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.PUSH2[0x600D]
                    + Op.JUMPI(pc=0xA, condition=0x1)
                    + Op.PUSH1[0xFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.JUMP(pc=0xB)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x3, condition=0x1)
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x5B]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x1]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xD, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xB, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x1)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 2989},
                    code=Op.DELEGATECALL(
                        gas=0x10000,
                        address=Op.CALLDATALOAD(offset=0x4),
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP,
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000001004",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000110"): Account(
                    code=Op.JUMPI(pc=0xE, condition=0x1)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000000111"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.MSTORE(offset=0x0, value=0x10)
                    + Op.JUMPDEST
                    + Op.SUB(Op.MLOAD(offset=0x0), 0x1)
                    + Op.MSTORE(offset=0x0, value=Op.DUP1)
                    + Op.PUSH1[0xB]
                    + Op.JUMPI
                ),
                Address("0x0000000000000000000000000000000000000200"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000201"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000202"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000203"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0x0)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000208"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x0)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0xFF)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.PUSH1[0x23]
                    + Op.JUMPI(pc=0x8, condition=0x1)
                    + Op.PUSH1[0x1]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x2]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x6, condition=0x6)
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.PUSH2[0x600D]
                    + Op.JUMPI(pc=0xA, condition=0x1)
                    + Op.PUSH1[0xFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.JUMP(pc=0xB)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x3, condition=0x1)
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x5B]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x1]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xD, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xB, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x1)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 2989},
                    code=Op.DELEGATECALL(
                        gas=0x10000,
                        address=Op.CALLDATALOAD(offset=0x4),
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP,
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000001002",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000110"): Account(
                    code=Op.JUMPI(pc=0xE, condition=0x1)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000000111"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.MSTORE(offset=0x0, value=0x10)
                    + Op.JUMPDEST
                    + Op.SUB(Op.MLOAD(offset=0x0), 0x1)
                    + Op.MSTORE(offset=0x0, value=Op.DUP1)
                    + Op.PUSH1[0xB]
                    + Op.JUMPI
                ),
                Address("0x0000000000000000000000000000000000000200"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000201"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000202"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000203"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0x0)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000208"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x0)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0xFF)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.PUSH1[0x23]
                    + Op.JUMPI(pc=0x8, condition=0x1)
                    + Op.PUSH1[0x1]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x2]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x6, condition=0x6)
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.PUSH2[0x600D]
                    + Op.JUMPI(pc=0xA, condition=0x1)
                    + Op.PUSH1[0xFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.JUMP(pc=0xB)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x3, condition=0x1)
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x5B]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x1]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xD, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xB, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x1)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 24589},
                    code=Op.DELEGATECALL(
                        gas=0x10000,
                        address=Op.CALLDATALOAD(offset=0x4),
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP,
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000110",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000110"): Account(
                    code=Op.JUMPI(pc=0xE, condition=0x1)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000000111"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.MSTORE(offset=0x0, value=0x10)
                    + Op.JUMPDEST
                    + Op.SUB(Op.MLOAD(offset=0x0), 0x1)
                    + Op.MSTORE(offset=0x0, value=Op.DUP1)
                    + Op.PUSH1[0xB]
                    + Op.JUMPI
                ),
                Address("0x0000000000000000000000000000000000000200"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000201"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000202"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000203"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0x0)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000208"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x0)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0xFF)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.PUSH1[0x23]
                    + Op.JUMPI(pc=0x8, condition=0x1)
                    + Op.PUSH1[0x1]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x2]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x6, condition=0x6)
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.PUSH2[0x600D]
                    + Op.JUMPI(pc=0xA, condition=0x1)
                    + Op.PUSH1[0xFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.JUMP(pc=0xB)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x3, condition=0x1)
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x5B]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x1]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xD, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xB, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x1)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 24589},
                    code=Op.DELEGATECALL(
                        gas=0x10000,
                        address=Op.CALLDATALOAD(offset=0x4),
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP,
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000111",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000110"): Account(
                    code=Op.JUMPI(pc=0xE, condition=0x1)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000000111"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.MSTORE(offset=0x0, value=0x10)
                    + Op.JUMPDEST
                    + Op.SUB(Op.MLOAD(offset=0x0), 0x1)
                    + Op.MSTORE(offset=0x0, value=Op.DUP1)
                    + Op.PUSH1[0xB]
                    + Op.JUMPI
                ),
                Address("0x0000000000000000000000000000000000000200"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000201"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000202"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000203"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0x0)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000208"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x0)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0xFF)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.PUSH1[0x23]
                    + Op.JUMPI(pc=0x8, condition=0x1)
                    + Op.PUSH1[0x1]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x2]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x6, condition=0x6)
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.PUSH2[0x600D]
                    + Op.JUMPI(pc=0xA, condition=0x1)
                    + Op.PUSH1[0xFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.JUMP(pc=0xB)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x3, condition=0x1)
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x5B]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x1]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xD, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xB, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x1)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 24589},
                    code=Op.DELEGATECALL(
                        gas=0x10000,
                        address=Op.CALLDATALOAD(offset=0x4),
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP,
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000208",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000110"): Account(
                    code=Op.JUMPI(pc=0xE, condition=0x1)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000000111"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.MSTORE(offset=0x0, value=0x10)
                    + Op.JUMPDEST
                    + Op.SUB(Op.MLOAD(offset=0x0), 0x1)
                    + Op.MSTORE(offset=0x0, value=Op.DUP1)
                    + Op.PUSH1[0xB]
                    + Op.JUMPI
                ),
                Address("0x0000000000000000000000000000000000000200"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000201"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000202"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000203"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0x0)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000208"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x0)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0xFF)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.PUSH1[0x23]
                    + Op.JUMPI(pc=0x8, condition=0x1)
                    + Op.PUSH1[0x1]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x2]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x6, condition=0x6)
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.PUSH2[0x600D]
                    + Op.JUMPI(pc=0xA, condition=0x1)
                    + Op.PUSH1[0xFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.JUMP(pc=0xB)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x3, condition=0x1)
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x5B]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x1]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xD, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xB, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x1)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 2989},
                    code=Op.DELEGATECALL(
                        gas=0x10000,
                        address=Op.CALLDATALOAD(offset=0x4),
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP,
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000201",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000110"): Account(
                    code=Op.JUMPI(pc=0xE, condition=0x1)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000000111"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.MSTORE(offset=0x0, value=0x10)
                    + Op.JUMPDEST
                    + Op.SUB(Op.MLOAD(offset=0x0), 0x1)
                    + Op.MSTORE(offset=0x0, value=Op.DUP1)
                    + Op.PUSH1[0xB]
                    + Op.JUMPI
                ),
                Address("0x0000000000000000000000000000000000000200"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000201"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000202"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000203"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0x0)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000208"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x0)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0xFF)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.PUSH1[0x23]
                    + Op.JUMPI(pc=0x8, condition=0x1)
                    + Op.PUSH1[0x1]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x2]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x6, condition=0x6)
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.PUSH2[0x600D]
                    + Op.JUMPI(pc=0xA, condition=0x1)
                    + Op.PUSH1[0xFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.JUMP(pc=0xB)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x3, condition=0x1)
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x5B]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x1]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xD, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xB, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x1)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 24589},
                    code=Op.DELEGATECALL(
                        gas=0x10000,
                        address=Op.CALLDATALOAD(offset=0x4),
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP,
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000203",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000110"): Account(
                    code=Op.JUMPI(pc=0xE, condition=0x1)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000000111"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.MSTORE(offset=0x0, value=0x10)
                    + Op.JUMPDEST
                    + Op.SUB(Op.MLOAD(offset=0x0), 0x1)
                    + Op.MSTORE(offset=0x0, value=Op.DUP1)
                    + Op.PUSH1[0xB]
                    + Op.JUMPI
                ),
                Address("0x0000000000000000000000000000000000000200"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000201"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000202"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000203"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0x0)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000208"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x0)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0xFF)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.PUSH1[0x23]
                    + Op.JUMPI(pc=0x8, condition=0x1)
                    + Op.PUSH1[0x1]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x2]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x6, condition=0x6)
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.PUSH2[0x600D]
                    + Op.JUMPI(pc=0xA, condition=0x1)
                    + Op.PUSH1[0xFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.JUMP(pc=0xB)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x3, condition=0x1)
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x5B]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x1]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xD, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xB, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x1)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 24589},
                    code=Op.DELEGATECALL(
                        gas=0x10000,
                        address=Op.CALLDATALOAD(offset=0x4),
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP,
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000020d",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000110"): Account(
                    code=Op.JUMPI(pc=0xE, condition=0x1)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000000111"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.MSTORE(offset=0x0, value=0x10)
                    + Op.JUMPDEST
                    + Op.SUB(Op.MLOAD(offset=0x0), 0x1)
                    + Op.MSTORE(offset=0x0, value=Op.DUP1)
                    + Op.PUSH1[0xB]
                    + Op.JUMPI
                ),
                Address("0x0000000000000000000000000000000000000200"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000201"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000202"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000203"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0x0)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000208"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x0)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0xFF)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.PUSH1[0x23]
                    + Op.JUMPI(pc=0x8, condition=0x1)
                    + Op.PUSH1[0x1]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x2]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x6, condition=0x6)
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.PUSH2[0x600D]
                    + Op.JUMPI(pc=0xA, condition=0x1)
                    + Op.PUSH1[0xFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.JUMP(pc=0xB)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x3, condition=0x1)
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x5B]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x1]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xD, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xB, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x1)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 24589},
                    code=Op.DELEGATECALL(
                        gas=0x10000,
                        address=Op.CALLDATALOAD(offset=0x4),
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP,
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000020e",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000110"): Account(
                    code=Op.JUMPI(pc=0xE, condition=0x1)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000000111"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.MSTORE(offset=0x0, value=0x10)
                    + Op.JUMPDEST
                    + Op.SUB(Op.MLOAD(offset=0x0), 0x1)
                    + Op.MSTORE(offset=0x0, value=Op.DUP1)
                    + Op.PUSH1[0xB]
                    + Op.JUMPI
                ),
                Address("0x0000000000000000000000000000000000000200"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000201"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000202"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000203"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0x0)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000208"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x0)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0xFF)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.PUSH1[0x23]
                    + Op.JUMPI(pc=0x8, condition=0x1)
                    + Op.PUSH1[0x1]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x2]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x6, condition=0x6)
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.PUSH2[0x600D]
                    + Op.JUMPI(pc=0xA, condition=0x1)
                    + Op.PUSH1[0xFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.JUMP(pc=0xB)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x3, condition=0x1)
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x5B]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x1]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xD, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xB, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x1)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 24589},
                    code=Op.DELEGATECALL(
                        gas=0x10000,
                        address=Op.CALLDATALOAD(offset=0x4),
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP,
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000020f",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000110"): Account(
                    code=Op.JUMPI(pc=0xE, condition=0x1)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000000111"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.MSTORE(offset=0x0, value=0x10)
                    + Op.JUMPDEST
                    + Op.SUB(Op.MLOAD(offset=0x0), 0x1)
                    + Op.MSTORE(offset=0x0, value=Op.DUP1)
                    + Op.PUSH1[0xB]
                    + Op.JUMPI
                ),
                Address("0x0000000000000000000000000000000000000200"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000201"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000202"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000203"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0x0)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000208"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x0)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0xFF)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.PUSH1[0x23]
                    + Op.JUMPI(pc=0x8, condition=0x1)
                    + Op.PUSH1[0x1]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x2]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x6, condition=0x6)
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.PUSH2[0x600D]
                    + Op.JUMPI(pc=0xA, condition=0x1)
                    + Op.PUSH1[0xFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.JUMP(pc=0xB)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x3, condition=0x1)
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x5B]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x1]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xD, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xB, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x1)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 24589},
                    code=Op.DELEGATECALL(
                        gas=0x10000,
                        address=Op.CALLDATALOAD(offset=0x4),
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP,
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000200",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000110"): Account(
                    code=Op.JUMPI(pc=0xE, condition=0x1)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000000111"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.MSTORE(offset=0x0, value=0x10)
                    + Op.JUMPDEST
                    + Op.SUB(Op.MLOAD(offset=0x0), 0x1)
                    + Op.MSTORE(offset=0x0, value=Op.DUP1)
                    + Op.PUSH1[0xB]
                    + Op.JUMPI
                ),
                Address("0x0000000000000000000000000000000000000200"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000201"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000202"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000203"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0x0)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000208"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x0)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0xFF)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.PUSH1[0x23]
                    + Op.JUMPI(pc=0x8, condition=0x1)
                    + Op.PUSH1[0x1]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x2]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x6, condition=0x6)
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.PUSH2[0x600D]
                    + Op.JUMPI(pc=0xA, condition=0x1)
                    + Op.PUSH1[0xFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.JUMP(pc=0xB)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x3, condition=0x1)
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x5B]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x1]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xD, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xB, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x1)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 24589},
                    code=Op.DELEGATECALL(
                        gas=0x10000,
                        address=Op.CALLDATALOAD(offset=0x4),
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP,
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000202",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000110"): Account(
                    code=Op.JUMPI(pc=0xE, condition=0x1)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000000111"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.MSTORE(offset=0x0, value=0x10)
                    + Op.JUMPDEST
                    + Op.SUB(Op.MLOAD(offset=0x0), 0x1)
                    + Op.MSTORE(offset=0x0, value=Op.DUP1)
                    + Op.PUSH1[0xB]
                    + Op.JUMPI
                ),
                Address("0x0000000000000000000000000000000000000200"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000201"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000202"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000203"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0x0)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000000208"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x0)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000020f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x0)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.JUMPI(pc=0x6, condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xFFFFFFF, condition=0xFF)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.PUSH1[0x23]
                    + Op.JUMPI(pc=0x8, condition=0x1)
                    + Op.PUSH1[0x1]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x2]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x6, condition=0x6)
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.PUSH2[0x600D]
                    + Op.JUMPI(pc=0xA, condition=0x1)
                    + Op.PUSH1[0xFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.JUMP(pc=0xB)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x3, condition=0x1)
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x1)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x5B]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.JUMPI(pc=0x7, condition=0x1)
                    + Op.STOP
                    + Op.PUSH1[0x1]
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xD, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(key=0x0, value=0x600D)
                    + Op.JUMPI(pc=0xB, condition=0x1)
                    + Op.GAS
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.GAS)
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.JUMPI(pc=0x1000000000000000D, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.JUMPI(pc=0x100000009, condition=0x11)
                    + Op.JUMPDEST
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=0x600D)
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.POP(Op.SUB(0x0, 0x1))
                    + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x1)
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 2989},
                    code=Op.DELEGATECALL(
                        gas=0x10000,
                        address=Op.CALLDATALOAD(offset=0x4),
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP,
                ),
            },
        ),
    ],
    ids=[
        "case0",
        "case1",
        "case2",
        "case3",
        "case4",
        "case5",
        "case6",
        "case7",
        "case8",
        "case9",
        "case10",
        "case11",
        "case12",
        "case13",
        "case14",
        "case15",
        "case16",
        "case17",
        "case18",
        "case19",
        "case20",
        "case21",
        "case22",
        "case23",
        "case24",
        "case25",
    ],
)
@pytest.mark.pre_alloc_mutable
def test_jumpi(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Ori Pomerantz qbzzt1@gmail.com."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xcccccccccccccccccccccccccccccccccccccccc")
    callee = Address("0x0000000000000000000000000000000000000110")
    callee_1 = Address("0x0000000000000000000000000000000000000111")
    callee_2 = Address("0x0000000000000000000000000000000000000200")
    callee_3 = Address("0x0000000000000000000000000000000000000201")
    callee_4 = Address("0x0000000000000000000000000000000000000202")
    callee_5 = Address("0x0000000000000000000000000000000000000203")
    callee_6 = Address("0x0000000000000000000000000000000000000208")
    callee_7 = Address("0x000000000000000000000000000000000000020d")
    callee_8 = Address("0x000000000000000000000000000000000000020e")
    callee_9 = Address("0x000000000000000000000000000000000000020f")
    callee_10 = Address("0x0000000000000000000000000000000000001000")
    callee_11 = Address("0x0000000000000000000000000000000000001001")
    callee_12 = Address("0x0000000000000000000000000000000000001002")
    callee_13 = Address("0x0000000000000000000000000000000000001003")
    callee_14 = Address("0x0000000000000000000000000000000000001004")
    callee_15 = Address("0x0000000000000000000000000000000000001005")
    callee_16 = Address("0x0000000000000000000000000000000000001006")
    callee_17 = Address("0x0000000000000000000000000000000000001007")
    callee_18 = Address("0x0000000000000000000000000000000000001008")
    callee_19 = Address("0x0000000000000000000000000000000000001009")
    callee_20 = Address("0x000000000000000000000000000000000000100a")
    callee_21 = Address("0x000000000000000000000000000000000000100b")
    callee_22 = Address("0x000000000000000000000000000000000000100c")
    callee_23 = Address("0x000000000000000000000000000000000000100d")
    callee_24 = Address("0x000000000000000000000000000000000000100e")
    callee_25 = Address("0x000000000000000000000000000000000000100f")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000,
    )

    pre[callee] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.JUMPI(pc=0xE, condition=0x1)
            + Op.JUMPDEST
            + Op.JUMPDEST
            + Op.JUMPDEST
            + Op.JUMPDEST
            + Op.JUMPDEST
            + Op.JUMPDEST
            + Op.JUMPDEST
            + Op.JUMPDEST
            + Op.JUMPDEST
            + Op.JUMPDEST
            + Op.JUMPDEST
            + Op.JUMPDEST
            + Op.JUMPDEST
            + Op.JUMPDEST
            + Op.JUMPDEST
            + Op.JUMPDEST
            + Op.SSTORE(key=0x0, value=0x600D)
        ),
    )
    pre[callee_1] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=0x600D)
            + Op.MSTORE(offset=0x0, value=0x10)
            + Op.JUMPDEST
            + Op.SUB(Op.MLOAD(offset=0x0), 0x1)
            + Op.MSTORE(offset=0x0, value=Op.DUP1)
            + Op.PUSH1[0xB]
            + Op.JUMPI
        ),
    )
    pre[callee_2] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=0x600D)
            + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
            + Op.JUMPDEST
            + Op.STOP
        ),
    )
    pre[callee_3] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=0x600D)
            + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
            + Op.JUMPDEST
            + Op.STOP
        ),
    )
    pre[callee_4] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.JUMPI(pc=0x6, condition=0x0)
            + Op.STOP
            + Op.JUMPDEST
            + Op.SSTORE(key=0x0, value=0x600D)
            + Op.STOP
        ),
    )
    pre[callee_5] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=0x600D)
            + Op.JUMPI(pc=0xFFFFFFF, condition=0x0)
            + Op.STOP
        ),
    )
    pre[callee_6] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x0)
            + Op.STOP
            + Op.JUMPDEST
            + Op.SSTORE(key=0x0, value=0x600D)
        ),
    )
    pre[callee_7] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.JUMPI(pc=0x1000000000000000D, condition=0x0)
            + Op.JUMPDEST
            + Op.JUMPDEST
            + Op.SSTORE(key=0x0, value=0x600D)
        ),
    )
    pre[callee_8] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.JUMPI(pc=0x100000009, condition=0x0)
            + Op.JUMPDEST
            + Op.JUMPDEST
            + Op.SSTORE(key=0x0, value=0x600D)
        ),
    )
    pre[callee_9] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.POP(Op.MLOAD(offset=0x0))
            + Op.POP(Op.SUB(0x0, 0x1))
            + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x0)
            + Op.SSTORE(key=0x0, value=0x600D)
            + Op.STOP
        ),
    )
    pre[callee_10] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=0x600D)
            + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
            + Op.JUMPDEST
            + Op.STOP
        ),
    )
    pre[callee_11] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=0x600D)
            + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
            + Op.JUMPDEST
            + Op.STOP
        ),
    )
    pre[callee_12] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.JUMPI(pc=0x6, condition=0x1)
            + Op.STOP
            + Op.JUMPDEST
            + Op.SSTORE(key=0x0, value=0x600D)
            + Op.STOP
        ),
    )
    pre[callee_13] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=0x600D)
            + Op.JUMPI(pc=0xFFFFFFF, condition=0xFF)
            + Op.STOP
        ),
    )
    pre[callee_14] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.PUSH1[0x23]
            + Op.JUMPI(pc=0x8, condition=0x1)
            + Op.PUSH1[0x1]
            + Op.JUMPDEST
            + Op.PUSH1[0x2]
            + Op.SSTORE
        ),
    )
    pre[callee_15] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=0x600D)
            + Op.JUMPDEST
            + Op.JUMPI(pc=0x6, condition=0x6)
        ),
    )
    pre[callee_16] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.PUSH2[0x600D]
            + Op.JUMPI(pc=0xA, condition=0x1)
            + Op.PUSH1[0xFF]
            + Op.JUMPDEST
            + Op.PUSH1[0x0]
            + Op.SSTORE
        ),
    )
    pre[callee_17] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.JUMP(pc=0xB)
            + Op.JUMPDEST
            + Op.SSTORE(key=0x0, value=0x600D)
            + Op.STOP
            + Op.JUMPDEST
            + Op.JUMPI(pc=0x3, condition=0x1)
        ),
    )
    pre[callee_18] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x1)
            + Op.STOP
            + Op.JUMPDEST
            + Op.SSTORE(key=0x0, value=0x600D)
        ),
    )
    pre[callee_19] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.JUMPI(pc=0x7, condition=0x1)
            + Op.STOP
            + Op.PUSH1[0x5B]
            + Op.SSTORE(key=0x0, value=0x600D)
        ),
    )
    pre[callee_20] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.JUMPI(pc=0x7, condition=0x1)
            + Op.STOP
            + Op.PUSH1[0x1]
            + Op.SSTORE(key=0x0, value=0x600D)
        ),
    )
    pre[callee_21] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=0x600D)
            + Op.JUMPI(pc=0xD, condition=0x1)
            + Op.GAS
            + Op.JUMPDEST
            + Op.SSTORE(key=0x1, value=Op.GAS)
        ),
    )
    pre[callee_22] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=0x600D)
            + Op.JUMPI(pc=0xB, condition=0x1)
            + Op.GAS
            + Op.JUMPDEST
            + Op.SSTORE(key=0x1, value=Op.GAS)
        ),
    )
    pre[callee_23] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.JUMPI(pc=0x1000000000000000D, condition=0x11)
            + Op.JUMPDEST
            + Op.JUMPDEST
            + Op.SSTORE(key=0x0, value=0x600D)
        ),
    )
    pre[callee_24] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.JUMPI(pc=0x100000009, condition=0x11)
            + Op.JUMPDEST
            + Op.JUMPDEST
            + Op.SSTORE(key=0x0, value=0x600D)
        ),
    )
    pre[callee_25] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.POP(Op.MLOAD(offset=0x0))
            + Op.POP(Op.SUB(0x0, 0x1))
            + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x1)
            + Op.SSTORE(key=0x0, value=0x600D)
            + Op.STOP
        ),
    )
    pre[sender] = Account(balance=0x100000000000, nonce=0)
    pre[contract] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.DELEGATECALL(
                gas=0x10000,
                address=Op.CALLDATALOAD(offset=0x4),
                args_offset=0x0,
                args_size=0x0,
                ret_offset=0x0,
                ret_size=0x0,
            )
            + Op.STOP
        ),
        storage={0x0: 0xBAD},
    )

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
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
