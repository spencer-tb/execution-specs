"""
Ori Pomerantz qbzzt1@gmail.com.

Ported from:
tests/static/state_tests/VMTests/vmBitwiseLogicOperation/byteFiller.yml
"""

import pytest
from execution_testing import (
    Account,
    Address,
    Alloc,
    EOA,
    Environment,
    Hash,
    StateTestFiller,
    Transaction,
)
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


@pytest.mark.ported_from(
    [
        "tests/static/state_tests/VMTests/vmBitwiseLogicOperation/byteFiller.yml",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        (
            "693c61390000000000000000000000000000000000000000000000000000000000001008",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000200"): Account(
                    code=Op.MSTORE(offset=0x100, value=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=0x4A,
                        condition=Op.ISZERO(
                            Op.LT(Op.MLOAD(offset=0x100), 0x20)
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.MLOAD(offset=0x100),
                        value=Op.BYTE(
                            Op.MLOAD(offset=0x100),
                            0x102030405060708090A0B0C0D0E0F101112131415161718191A1B1C1D1E1F,  # noqa: E501
                        ),
                    )
                    + Op.MSTORE(
                        offset=0x100, value=Op.ADD(Op.MLOAD(offset=0x100), 0x1)
                    )
                    + Op.JUMP(pc=0x6)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x0), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x1), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x2), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x3), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x4), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x5), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x6), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x7), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x1F), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SDIV(0x1F, 0x20), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.SSTORE(
                        key=0x1,
                        value=Op.ADD(Op.DUP1, Op.BYTE(0x1F, 0x1234523456)),
                    )
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=0xFFFFFF,
                        address=Op.CALLDATALOAD(offset=0x4),
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000001009",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000200"): Account(
                    code=Op.MSTORE(offset=0x100, value=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=0x4A,
                        condition=Op.ISZERO(
                            Op.LT(Op.MLOAD(offset=0x100), 0x20)
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.MLOAD(offset=0x100),
                        value=Op.BYTE(
                            Op.MLOAD(offset=0x100),
                            0x102030405060708090A0B0C0D0E0F101112131415161718191A1B1C1D1E1F,  # noqa: E501
                        ),
                    )
                    + Op.MSTORE(
                        offset=0x100, value=Op.ADD(Op.MLOAD(offset=0x100), 0x1)
                    )
                    + Op.JUMP(pc=0x6)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x0), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x1), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x2), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x3), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x4), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x5), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x6), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x7), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x1F), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SDIV(0x1F, 0x20), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.SSTORE(
                        key=0x1,
                        value=Op.ADD(Op.DUP1, Op.BYTE(0x1F, 0x1234523456)),
                    )
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=0xFFFFFF,
                        address=Op.CALLDATALOAD(offset=0x4),
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000001007",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000200"): Account(
                    code=Op.MSTORE(offset=0x100, value=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=0x4A,
                        condition=Op.ISZERO(
                            Op.LT(Op.MLOAD(offset=0x100), 0x20)
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.MLOAD(offset=0x100),
                        value=Op.BYTE(
                            Op.MLOAD(offset=0x100),
                            0x102030405060708090A0B0C0D0E0F101112131415161718191A1B1C1D1E1F,  # noqa: E501
                        ),
                    )
                    + Op.MSTORE(
                        offset=0x100, value=Op.ADD(Op.MLOAD(offset=0x100), 0x1)
                    )
                    + Op.JUMP(pc=0x6)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x0), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x1), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x2), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x3), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x4), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x5), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x6), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    storage={0: 128},
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x7), 0x8040201008040201),
                    )
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x1F), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SDIV(0x1F, 0x20), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.SSTORE(
                        key=0x1,
                        value=Op.ADD(Op.DUP1, Op.BYTE(0x1F, 0x1234523456)),
                    )
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=0xFFFFFF,
                        address=Op.CALLDATALOAD(offset=0x4),
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000001006",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000200"): Account(
                    code=Op.MSTORE(offset=0x100, value=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=0x4A,
                        condition=Op.ISZERO(
                            Op.LT(Op.MLOAD(offset=0x100), 0x20)
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.MLOAD(offset=0x100),
                        value=Op.BYTE(
                            Op.MLOAD(offset=0x100),
                            0x102030405060708090A0B0C0D0E0F101112131415161718191A1B1C1D1E1F,  # noqa: E501
                        ),
                    )
                    + Op.MSTORE(
                        offset=0x100, value=Op.ADD(Op.MLOAD(offset=0x100), 0x1)
                    )
                    + Op.JUMP(pc=0x6)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x0), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x1), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x2), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x3), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x4), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x5), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    storage={0: 64},
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x6), 0x8040201008040201),
                    )
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x7), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x1F), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SDIV(0x1F, 0x20), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.SSTORE(
                        key=0x1,
                        value=Op.ADD(Op.DUP1, Op.BYTE(0x1F, 0x1234523456)),
                    )
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=0xFFFFFF,
                        address=Op.CALLDATALOAD(offset=0x4),
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000001005",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000200"): Account(
                    code=Op.MSTORE(offset=0x100, value=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=0x4A,
                        condition=Op.ISZERO(
                            Op.LT(Op.MLOAD(offset=0x100), 0x20)
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.MLOAD(offset=0x100),
                        value=Op.BYTE(
                            Op.MLOAD(offset=0x100),
                            0x102030405060708090A0B0C0D0E0F101112131415161718191A1B1C1D1E1F,  # noqa: E501
                        ),
                    )
                    + Op.MSTORE(
                        offset=0x100, value=Op.ADD(Op.MLOAD(offset=0x100), 0x1)
                    )
                    + Op.JUMP(pc=0x6)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x0), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x1), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x2), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x3), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x4), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    storage={0: 32},
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x5), 0x8040201008040201),
                    )
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x6), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x7), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x1F), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SDIV(0x1F, 0x20), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.SSTORE(
                        key=0x1,
                        value=Op.ADD(Op.DUP1, Op.BYTE(0x1F, 0x1234523456)),
                    )
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=0xFFFFFF,
                        address=Op.CALLDATALOAD(offset=0x4),
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000001004",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000200"): Account(
                    code=Op.MSTORE(offset=0x100, value=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=0x4A,
                        condition=Op.ISZERO(
                            Op.LT(Op.MLOAD(offset=0x100), 0x20)
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.MLOAD(offset=0x100),
                        value=Op.BYTE(
                            Op.MLOAD(offset=0x100),
                            0x102030405060708090A0B0C0D0E0F101112131415161718191A1B1C1D1E1F,  # noqa: E501
                        ),
                    )
                    + Op.MSTORE(
                        offset=0x100, value=Op.ADD(Op.MLOAD(offset=0x100), 0x1)
                    )
                    + Op.JUMP(pc=0x6)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x0), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x1), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x2), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x3), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    storage={0: 16},
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x4), 0x8040201008040201),
                    )
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x5), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x6), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x7), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x1F), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SDIV(0x1F, 0x20), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.SSTORE(
                        key=0x1,
                        value=Op.ADD(Op.DUP1, Op.BYTE(0x1F, 0x1234523456)),
                    )
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=0xFFFFFF,
                        address=Op.CALLDATALOAD(offset=0x4),
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000001003",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000200"): Account(
                    code=Op.MSTORE(offset=0x100, value=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=0x4A,
                        condition=Op.ISZERO(
                            Op.LT(Op.MLOAD(offset=0x100), 0x20)
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.MLOAD(offset=0x100),
                        value=Op.BYTE(
                            Op.MLOAD(offset=0x100),
                            0x102030405060708090A0B0C0D0E0F101112131415161718191A1B1C1D1E1F,  # noqa: E501
                        ),
                    )
                    + Op.MSTORE(
                        offset=0x100, value=Op.ADD(Op.MLOAD(offset=0x100), 0x1)
                    )
                    + Op.JUMP(pc=0x6)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x0), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x1), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x2), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    storage={0: 8},
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x3), 0x8040201008040201),
                    )
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x4), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x5), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x6), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x7), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x1F), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SDIV(0x1F, 0x20), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.SSTORE(
                        key=0x1,
                        value=Op.ADD(Op.DUP1, Op.BYTE(0x1F, 0x1234523456)),
                    )
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=0xFFFFFF,
                        address=Op.CALLDATALOAD(offset=0x4),
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000001002",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000200"): Account(
                    code=Op.MSTORE(offset=0x100, value=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=0x4A,
                        condition=Op.ISZERO(
                            Op.LT(Op.MLOAD(offset=0x100), 0x20)
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.MLOAD(offset=0x100),
                        value=Op.BYTE(
                            Op.MLOAD(offset=0x100),
                            0x102030405060708090A0B0C0D0E0F101112131415161718191A1B1C1D1E1F,  # noqa: E501
                        ),
                    )
                    + Op.MSTORE(
                        offset=0x100, value=Op.ADD(Op.MLOAD(offset=0x100), 0x1)
                    )
                    + Op.JUMP(pc=0x6)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x0), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x1), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    storage={0: 4},
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x2), 0x8040201008040201),
                    )
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x3), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x4), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x5), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x6), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x7), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x1F), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SDIV(0x1F, 0x20), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.SSTORE(
                        key=0x1,
                        value=Op.ADD(Op.DUP1, Op.BYTE(0x1F, 0x1234523456)),
                    )
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=0xFFFFFF,
                        address=Op.CALLDATALOAD(offset=0x4),
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000001001",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000200"): Account(
                    code=Op.MSTORE(offset=0x100, value=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=0x4A,
                        condition=Op.ISZERO(
                            Op.LT(Op.MLOAD(offset=0x100), 0x20)
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.MLOAD(offset=0x100),
                        value=Op.BYTE(
                            Op.MLOAD(offset=0x100),
                            0x102030405060708090A0B0C0D0E0F101112131415161718191A1B1C1D1E1F,  # noqa: E501
                        ),
                    )
                    + Op.MSTORE(
                        offset=0x100, value=Op.ADD(Op.MLOAD(offset=0x100), 0x1)
                    )
                    + Op.JUMP(pc=0x6)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x0), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    storage={0: 2},
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x1), 0x8040201008040201),
                    )
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x2), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x3), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x4), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x5), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x6), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x7), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x1F), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SDIV(0x1F, 0x20), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.SSTORE(
                        key=0x1,
                        value=Op.ADD(Op.DUP1, Op.BYTE(0x1F, 0x1234523456)),
                    )
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=0xFFFFFF,
                        address=Op.CALLDATALOAD(offset=0x4),
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000001000",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000200"): Account(
                    code=Op.MSTORE(offset=0x100, value=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=0x4A,
                        condition=Op.ISZERO(
                            Op.LT(Op.MLOAD(offset=0x100), 0x20)
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.MLOAD(offset=0x100),
                        value=Op.BYTE(
                            Op.MLOAD(offset=0x100),
                            0x102030405060708090A0B0C0D0E0F101112131415161718191A1B1C1D1E1F,  # noqa: E501
                        ),
                    )
                    + Op.MSTORE(
                        offset=0x100, value=Op.ADD(Op.MLOAD(offset=0x100), 0x1)
                    )
                    + Op.JUMP(pc=0x6)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001000"): Account(
                    storage={0: 1},
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x0), 0x8040201008040201),
                    )
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x1), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x2), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x3), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x4), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x5), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x6), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x7), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x1F), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SDIV(0x1F, 0x20), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.SSTORE(
                        key=0x1,
                        value=Op.ADD(Op.DUP1, Op.BYTE(0x1F, 0x1234523456)),
                    )
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=0xFFFFFF,
                        address=Op.CALLDATALOAD(offset=0x4),
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000200",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000200"): Account(
                    storage={
                        1: 1,
                        2: 2,
                        3: 3,
                        4: 4,
                        5: 5,
                        6: 6,
                        7: 7,
                        8: 8,
                        9: 9,
                        10: 10,
                        11: 11,
                        12: 12,
                        13: 13,
                        14: 14,
                        15: 15,
                        16: 16,
                        17: 17,
                        18: 18,
                        19: 19,
                        20: 20,
                        21: 21,
                        22: 22,
                        23: 23,
                        24: 24,
                        25: 25,
                        26: 26,
                        27: 27,
                        28: 28,
                        29: 29,
                        30: 30,
                        31: 31,
                    },
                    code=Op.MSTORE(offset=0x100, value=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=0x4A,
                        condition=Op.ISZERO(
                            Op.LT(Op.MLOAD(offset=0x100), 0x20)
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.MLOAD(offset=0x100),
                        value=Op.BYTE(
                            Op.MLOAD(offset=0x100),
                            0x102030405060708090A0B0C0D0E0F101112131415161718191A1B1C1D1E1F,  # noqa: E501
                        ),
                    )
                    + Op.MSTORE(
                        offset=0x100, value=Op.ADD(Op.MLOAD(offset=0x100), 0x1)
                    )
                    + Op.JUMP(pc=0x6)
                    + Op.JUMPDEST
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x0), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x1), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x2), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x3), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x4), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x5), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x6), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x7), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x1F), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SDIV(0x1F, 0x20), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.SSTORE(
                        key=0x1,
                        value=Op.ADD(Op.DUP1, Op.BYTE(0x1F, 0x1234523456)),
                    )
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=0xFFFFFF,
                        address=Op.CALLDATALOAD(offset=0x4),
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000100a",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000200"): Account(
                    code=Op.MSTORE(offset=0x100, value=0x0)
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=0x4A,
                        condition=Op.ISZERO(
                            Op.LT(Op.MLOAD(offset=0x100), 0x20)
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.MLOAD(offset=0x100),
                        value=Op.BYTE(
                            Op.MLOAD(offset=0x100),
                            0x102030405060708090A0B0C0D0E0F101112131415161718191A1B1C1D1E1F,  # noqa: E501
                        ),
                    )
                    + Op.MSTORE(
                        offset=0x100, value=Op.ADD(Op.MLOAD(offset=0x100), 0x1)
                    )
                    + Op.JUMP(pc=0x6)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x0), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x1), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x2), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x3), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x4), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x5), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x6), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x7), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SUB(0x1F, 0x1F), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.BYTE(Op.SDIV(0x1F, 0x20), 0x8040201008040201),
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    storage={1: 172},
                    code=Op.SSTORE(
                        key=0x1,
                        value=Op.ADD(Op.DUP1, Op.BYTE(0x1F, 0x1234523456)),
                    ),
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=0xFFFFFF,
                        address=Op.CALLDATALOAD(offset=0x4),
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
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
    ],
)
@pytest.mark.pre_alloc_mutable
def test_byte(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Ori Pomerantz qbzzt1@gmail.com."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = EOA(
        key=0x45A915E4D060149EB4365960E6A7A45F334393093061116B197E3240065FF2D8
    )
    contract = Address("0xcccccccccccccccccccccccccccccccccccccccc")
    callee = Address("0x0000000000000000000000000000000000000200")
    callee_1 = Address("0x0000000000000000000000000000000000001000")
    callee_2 = Address("0x0000000000000000000000000000000000001001")
    callee_3 = Address("0x0000000000000000000000000000000000001002")
    callee_4 = Address("0x0000000000000000000000000000000000001003")
    callee_5 = Address("0x0000000000000000000000000000000000001004")
    callee_6 = Address("0x0000000000000000000000000000000000001005")
    callee_7 = Address("0x0000000000000000000000000000000000001006")
    callee_8 = Address("0x0000000000000000000000000000000000001007")
    callee_9 = Address("0x0000000000000000000000000000000000001008")
    callee_10 = Address("0x0000000000000000000000000000000000001009")
    callee_11 = Address("0x000000000000000000000000000000000000100a")

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
            Op.MSTORE(offset=0x100, value=0x0)
            + Op.JUMPDEST
            + Op.JUMPI(
                pc=0x4A,
                condition=Op.ISZERO(Op.LT(Op.MLOAD(offset=0x100), 0x20)),
            )
            + Op.SSTORE(
                key=Op.MLOAD(offset=0x100),
                value=Op.BYTE(
                    Op.MLOAD(offset=0x100),
                    0x102030405060708090A0B0C0D0E0F101112131415161718191A1B1C1D1E1F,  # noqa: E501
                ),
            )
            + Op.MSTORE(
                offset=0x100, value=Op.ADD(Op.MLOAD(offset=0x100), 0x1)
            )
            + Op.JUMP(pc=0x6)
            + Op.JUMPDEST
            + Op.STOP
        ),
    )
    pre[callee_1] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.SSTORE(
                key=0x0,
                value=Op.BYTE(Op.SUB(0x1F, 0x0), 0x8040201008040201),
            )
            + Op.STOP
        ),
    )
    pre[callee_2] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.SSTORE(
                key=0x0,
                value=Op.BYTE(Op.SUB(0x1F, 0x1), 0x8040201008040201),
            )
            + Op.STOP
        ),
    )
    pre[callee_3] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.SSTORE(
                key=0x0,
                value=Op.BYTE(Op.SUB(0x1F, 0x2), 0x8040201008040201),
            )
            + Op.STOP
        ),
    )
    pre[callee_4] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.SSTORE(
                key=0x0,
                value=Op.BYTE(Op.SUB(0x1F, 0x3), 0x8040201008040201),
            )
            + Op.STOP
        ),
    )
    pre[callee_5] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.SSTORE(
                key=0x0,
                value=Op.BYTE(Op.SUB(0x1F, 0x4), 0x8040201008040201),
            )
            + Op.STOP
        ),
    )
    pre[callee_6] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.SSTORE(
                key=0x0,
                value=Op.BYTE(Op.SUB(0x1F, 0x5), 0x8040201008040201),
            )
            + Op.STOP
        ),
    )
    pre[callee_7] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.SSTORE(
                key=0x0,
                value=Op.BYTE(Op.SUB(0x1F, 0x6), 0x8040201008040201),
            )
            + Op.STOP
        ),
    )
    pre[callee_8] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.SSTORE(
                key=0x0,
                value=Op.BYTE(Op.SUB(0x1F, 0x7), 0x8040201008040201),
            )
            + Op.STOP
        ),
    )
    # Source: LLL
    # {
    #    [[0]] (byte (- 31 31) 0x8040201008040201)
    # }
    pre[callee_9] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.SSTORE(
                key=0x0,
                value=Op.BYTE(Op.SUB(0x1F, 0x1F), 0x8040201008040201),
            )
            + Op.STOP
        ),
    )
    # Source: LLL
    # {
    #    [[0]] (byte (sdiv 31 32) 0x8040201008040201)
    # }
    pre[callee_10] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.SSTORE(
                key=0x0,
                value=Op.BYTE(Op.SDIV(0x1F, 0x20), 0x8040201008040201),
            )
            + Op.STOP
        ),
    )
    # Source: raw bytecode
    pre[callee_11] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.SSTORE(
                key=0x1,
                value=Op.ADD(Op.DUP1, Op.BYTE(0x1F, 0x1234523456)),
            )
        ),
    )
    pre[sender] = Account(balance=0xBA1A9CE0BA1A9CE, nonce=0)
    # Source: LLL
    # {
    #     (call 0xffffff $4 0 0 0 0 0)
    # }
    pre[contract] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.CALL(
                gas=0xFFFFFF,
                address=Op.CALLDATALOAD(offset=0x4),
                value=0x0,
                args_offset=0x0,
                args_size=0x0,
                ret_offset=0x0,
                ret_size=0x0,
            )
            + Op.STOP
        ),
    )

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        sender=sender,
        to=contract,
        data=tx_data,
        gas_limit=16777216,
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
