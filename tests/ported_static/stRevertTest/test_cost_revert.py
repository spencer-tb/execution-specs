"""
Ori Pomerantz qbzzt1@gmail.com.

Ported from:
tests/static/state_tests/stRevertTest/costRevertFiller.yml
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
    ["tests/static/state_tests/stRevertTest/costRevertFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.valid_until("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000010030000000000000000000000000000000000000000000000000000000000000001",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.REVERT(offset=0x0, size=0x10) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.JUMPDEST
                    + Op.JUMPI(pc=0x13, condition=Op.ISZERO(0x1))
                    + Op.POP(Op.SHA3(offset=0x0, size=0x1000000))
                    + Op.JUMP(pc=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SHA3(offset=0x0, size=Op.SUB(0x0, 0x1)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex(
                        "610103600155600060006000600061dead6175305a03f450ba"
                    )
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x1, value=0x104)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=0xDEAD,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.JUMP(pc=0x0)
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.LT + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.JUMPDEST + Op.PC + Op.JUMP(pc=Op.SUB(Op.PC, 0x4))
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 0xFFFFFF},
                    code=Op.JUMPI(
                        pc=Op.PUSH2[0x11],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x0),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x3B])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x4D],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x1),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x75])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x87],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x2),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xAF])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0xC1],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x3),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xEB])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALLCODE(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=0x100, condition=Op.GT(Op.SLOAD(key=0x0), 0x4000000)
                    )
                    + Op.SLOAD(key=0x0)
                    + Op.JUMP(pc=0x105)
                    + Op.JUMPDEST
                    + Op.PUSH3[0xFFFFFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                    + Op.STOP,
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000010030000000000000000000000000000000000000000000000000000000000000002",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.REVERT(offset=0x0, size=0x10) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.JUMPDEST
                    + Op.JUMPI(pc=0x13, condition=Op.ISZERO(0x1))
                    + Op.POP(Op.SHA3(offset=0x0, size=0x1000000))
                    + Op.JUMP(pc=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SHA3(offset=0x0, size=Op.SUB(0x0, 0x1)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex(
                        "610103600155600060006000600061dead6175305a03f450ba"
                    )
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x1, value=0x104)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=0xDEAD,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.JUMP(pc=0x0)
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.LT + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.JUMPDEST + Op.PC + Op.JUMP(pc=Op.SUB(Op.PC, 0x4))
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 0xFFFFFF},
                    code=Op.JUMPI(
                        pc=Op.PUSH2[0x11],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x0),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x3B])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x4D],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x1),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x75])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x87],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x2),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xAF])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0xC1],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x3),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xEB])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALLCODE(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=0x100, condition=Op.GT(Op.SLOAD(key=0x0), 0x4000000)
                    )
                    + Op.SLOAD(key=0x0)
                    + Op.JUMP(pc=0x105)
                    + Op.JUMPDEST
                    + Op.PUSH3[0xFFFFFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                    + Op.STOP,
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000010030000000000000000000000000000000000000000000000000000000000000003",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.REVERT(offset=0x0, size=0x10) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.JUMPDEST
                    + Op.JUMPI(pc=0x13, condition=Op.ISZERO(0x1))
                    + Op.POP(Op.SHA3(offset=0x0, size=0x1000000))
                    + Op.JUMP(pc=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SHA3(offset=0x0, size=Op.SUB(0x0, 0x1)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex(
                        "610103600155600060006000600061dead6175305a03f450ba"
                    )
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x1, value=0x104)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=0xDEAD,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.JUMP(pc=0x0)
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.LT + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.JUMPDEST + Op.PC + Op.JUMP(pc=Op.SUB(Op.PC, 0x4))
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 0xFFFFFF},
                    code=Op.JUMPI(
                        pc=Op.PUSH2[0x11],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x0),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x3B])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x4D],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x1),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x75])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x87],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x2),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xAF])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0xC1],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x3),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xEB])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALLCODE(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=0x100, condition=Op.GT(Op.SLOAD(key=0x0), 0x4000000)
                    )
                    + Op.SLOAD(key=0x0)
                    + Op.JUMP(pc=0x105)
                    + Op.JUMPDEST
                    + Op.PUSH3[0xFFFFFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                    + Op.STOP,
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000010030000000000000000000000000000000000000000000000000000000000000000",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.REVERT(offset=0x0, size=0x10) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.JUMPDEST
                    + Op.JUMPI(pc=0x13, condition=Op.ISZERO(0x1))
                    + Op.POP(Op.SHA3(offset=0x0, size=0x1000000))
                    + Op.JUMP(pc=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SHA3(offset=0x0, size=Op.SUB(0x0, 0x1)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex(
                        "610103600155600060006000600061dead6175305a03f450ba"
                    )
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x1, value=0x104)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=0xDEAD,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.JUMP(pc=0x0)
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.LT + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.JUMPDEST + Op.PC + Op.JUMP(pc=Op.SUB(Op.PC, 0x4))
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 0xFFFFFF},
                    code=Op.JUMPI(
                        pc=Op.PUSH2[0x11],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x0),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x3B])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x4D],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x1),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x75])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x87],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x2),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xAF])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0xC1],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x3),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xEB])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALLCODE(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=0x100, condition=Op.GT(Op.SLOAD(key=0x0), 0x4000000)
                    )
                    + Op.SLOAD(key=0x0)
                    + Op.JUMP(pc=0x105)
                    + Op.JUMPDEST
                    + Op.PUSH3[0xFFFFFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                    + Op.STOP,
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000010040000000000000000000000000000000000000000000000000000000000000001",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.REVERT(offset=0x0, size=0x10) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.JUMPDEST
                    + Op.JUMPI(pc=0x13, condition=Op.ISZERO(0x1))
                    + Op.POP(Op.SHA3(offset=0x0, size=0x1000000))
                    + Op.JUMP(pc=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SHA3(offset=0x0, size=Op.SUB(0x0, 0x1)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex(
                        "610103600155600060006000600061dead6175305a03f450ba"
                    )
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x1, value=0x104)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=0xDEAD,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.JUMP(pc=0x0)
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.LT + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.JUMPDEST + Op.PC + Op.JUMP(pc=Op.SUB(Op.PC, 0x4))
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 0xFFFFFF},
                    code=Op.JUMPI(
                        pc=Op.PUSH2[0x11],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x0),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x3B])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x4D],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x1),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x75])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x87],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x2),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xAF])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0xC1],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x3),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xEB])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALLCODE(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=0x100, condition=Op.GT(Op.SLOAD(key=0x0), 0x4000000)
                    )
                    + Op.SLOAD(key=0x0)
                    + Op.JUMP(pc=0x105)
                    + Op.JUMPDEST
                    + Op.PUSH3[0xFFFFFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                    + Op.STOP,
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000010040000000000000000000000000000000000000000000000000000000000000002",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.REVERT(offset=0x0, size=0x10) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.JUMPDEST
                    + Op.JUMPI(pc=0x13, condition=Op.ISZERO(0x1))
                    + Op.POP(Op.SHA3(offset=0x0, size=0x1000000))
                    + Op.JUMP(pc=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SHA3(offset=0x0, size=Op.SUB(0x0, 0x1)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex(
                        "610103600155600060006000600061dead6175305a03f450ba"
                    )
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x1, value=0x104)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=0xDEAD,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.JUMP(pc=0x0)
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.LT + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.JUMPDEST + Op.PC + Op.JUMP(pc=Op.SUB(Op.PC, 0x4))
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 0xFFFFFF},
                    code=Op.JUMPI(
                        pc=Op.PUSH2[0x11],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x0),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x3B])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x4D],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x1),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x75])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x87],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x2),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xAF])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0xC1],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x3),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xEB])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALLCODE(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=0x100, condition=Op.GT(Op.SLOAD(key=0x0), 0x4000000)
                    )
                    + Op.SLOAD(key=0x0)
                    + Op.JUMP(pc=0x105)
                    + Op.JUMPDEST
                    + Op.PUSH3[0xFFFFFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                    + Op.STOP,
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000010040000000000000000000000000000000000000000000000000000000000000003",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.REVERT(offset=0x0, size=0x10) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.JUMPDEST
                    + Op.JUMPI(pc=0x13, condition=Op.ISZERO(0x1))
                    + Op.POP(Op.SHA3(offset=0x0, size=0x1000000))
                    + Op.JUMP(pc=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SHA3(offset=0x0, size=Op.SUB(0x0, 0x1)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex(
                        "610103600155600060006000600061dead6175305a03f450ba"
                    )
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x1, value=0x104)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=0xDEAD,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.JUMP(pc=0x0)
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.LT + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.JUMPDEST + Op.PC + Op.JUMP(pc=Op.SUB(Op.PC, 0x4))
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 0xFFFFFF},
                    code=Op.JUMPI(
                        pc=Op.PUSH2[0x11],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x0),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x3B])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x4D],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x1),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x75])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x87],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x2),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xAF])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0xC1],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x3),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xEB])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALLCODE(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=0x100, condition=Op.GT(Op.SLOAD(key=0x0), 0x4000000)
                    )
                    + Op.SLOAD(key=0x0)
                    + Op.JUMP(pc=0x105)
                    + Op.JUMPDEST
                    + Op.PUSH3[0xFFFFFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                    + Op.STOP,
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000010040000000000000000000000000000000000000000000000000000000000000000",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.REVERT(offset=0x0, size=0x10) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.JUMPDEST
                    + Op.JUMPI(pc=0x13, condition=Op.ISZERO(0x1))
                    + Op.POP(Op.SHA3(offset=0x0, size=0x1000000))
                    + Op.JUMP(pc=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SHA3(offset=0x0, size=Op.SUB(0x0, 0x1)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex(
                        "610103600155600060006000600061dead6175305a03f450ba"
                    )
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x1, value=0x104)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=0xDEAD,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.JUMP(pc=0x0)
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.LT + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.JUMPDEST + Op.PC + Op.JUMP(pc=Op.SUB(Op.PC, 0x4))
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 0xFFFFFF},
                    code=Op.JUMPI(
                        pc=Op.PUSH2[0x11],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x0),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x3B])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x4D],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x1),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x75])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x87],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x2),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xAF])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0xC1],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x3),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xEB])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALLCODE(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=0x100, condition=Op.GT(Op.SLOAD(key=0x0), 0x4000000)
                    )
                    + Op.SLOAD(key=0x0)
                    + Op.JUMP(pc=0x105)
                    + Op.JUMPDEST
                    + Op.PUSH3[0xFFFFFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                    + Op.STOP,
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000010010000000000000000000000000000000000000000000000000000000000000001",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.REVERT(offset=0x0, size=0x10) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.JUMPDEST
                    + Op.JUMPI(pc=0x13, condition=Op.ISZERO(0x1))
                    + Op.POP(Op.SHA3(offset=0x0, size=0x1000000))
                    + Op.JUMP(pc=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SHA3(offset=0x0, size=Op.SUB(0x0, 0x1)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex(
                        "610103600155600060006000600061dead6175305a03f450ba"
                    )
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x1, value=0x104)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=0xDEAD,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.JUMP(pc=0x0)
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.LT + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.JUMPDEST + Op.PC + Op.JUMP(pc=Op.SUB(Op.PC, 0x4))
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 0xFFFFFF},
                    code=Op.JUMPI(
                        pc=Op.PUSH2[0x11],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x0),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x3B])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x4D],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x1),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x75])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x87],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x2),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xAF])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0xC1],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x3),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xEB])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALLCODE(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=0x100, condition=Op.GT(Op.SLOAD(key=0x0), 0x4000000)
                    )
                    + Op.SLOAD(key=0x0)
                    + Op.JUMP(pc=0x105)
                    + Op.JUMPDEST
                    + Op.PUSH3[0xFFFFFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                    + Op.STOP,
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000010010000000000000000000000000000000000000000000000000000000000000002",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.REVERT(offset=0x0, size=0x10) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.JUMPDEST
                    + Op.JUMPI(pc=0x13, condition=Op.ISZERO(0x1))
                    + Op.POP(Op.SHA3(offset=0x0, size=0x1000000))
                    + Op.JUMP(pc=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SHA3(offset=0x0, size=Op.SUB(0x0, 0x1)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex(
                        "610103600155600060006000600061dead6175305a03f450ba"
                    )
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x1, value=0x104)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=0xDEAD,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.JUMP(pc=0x0)
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.LT + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.JUMPDEST + Op.PC + Op.JUMP(pc=Op.SUB(Op.PC, 0x4))
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 0xFFFFFF},
                    code=Op.JUMPI(
                        pc=Op.PUSH2[0x11],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x0),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x3B])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x4D],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x1),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x75])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x87],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x2),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xAF])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0xC1],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x3),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xEB])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALLCODE(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=0x100, condition=Op.GT(Op.SLOAD(key=0x0), 0x4000000)
                    )
                    + Op.SLOAD(key=0x0)
                    + Op.JUMP(pc=0x105)
                    + Op.JUMPDEST
                    + Op.PUSH3[0xFFFFFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                    + Op.STOP,
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000010010000000000000000000000000000000000000000000000000000000000000003",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.REVERT(offset=0x0, size=0x10) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.JUMPDEST
                    + Op.JUMPI(pc=0x13, condition=Op.ISZERO(0x1))
                    + Op.POP(Op.SHA3(offset=0x0, size=0x1000000))
                    + Op.JUMP(pc=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SHA3(offset=0x0, size=Op.SUB(0x0, 0x1)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex(
                        "610103600155600060006000600061dead6175305a03f450ba"
                    )
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x1, value=0x104)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=0xDEAD,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.JUMP(pc=0x0)
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.LT + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.JUMPDEST + Op.PC + Op.JUMP(pc=Op.SUB(Op.PC, 0x4))
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 0xFFFFFF},
                    code=Op.JUMPI(
                        pc=Op.PUSH2[0x11],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x0),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x3B])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x4D],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x1),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x75])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x87],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x2),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xAF])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0xC1],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x3),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xEB])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALLCODE(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=0x100, condition=Op.GT(Op.SLOAD(key=0x0), 0x4000000)
                    )
                    + Op.SLOAD(key=0x0)
                    + Op.JUMP(pc=0x105)
                    + Op.JUMPDEST
                    + Op.PUSH3[0xFFFFFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                    + Op.STOP,
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000010010000000000000000000000000000000000000000000000000000000000000000",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.REVERT(offset=0x0, size=0x10) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.JUMPDEST
                    + Op.JUMPI(pc=0x13, condition=Op.ISZERO(0x1))
                    + Op.POP(Op.SHA3(offset=0x0, size=0x1000000))
                    + Op.JUMP(pc=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SHA3(offset=0x0, size=Op.SUB(0x0, 0x1)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex(
                        "610103600155600060006000600061dead6175305a03f450ba"
                    )
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x1, value=0x104)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=0xDEAD,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.JUMP(pc=0x0)
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.LT + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.JUMPDEST + Op.PC + Op.JUMP(pc=Op.SUB(Op.PC, 0x4))
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 0xFFFFFF},
                    code=Op.JUMPI(
                        pc=Op.PUSH2[0x11],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x0),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x3B])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x4D],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x1),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x75])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x87],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x2),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xAF])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0xC1],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x3),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xEB])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALLCODE(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=0x100, condition=Op.GT(Op.SLOAD(key=0x0), 0x4000000)
                    )
                    + Op.SLOAD(key=0x0)
                    + Op.JUMP(pc=0x105)
                    + Op.JUMPDEST
                    + Op.PUSH3[0xFFFFFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                    + Op.STOP,
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000001",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.REVERT(offset=0x0, size=0x10) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.JUMPDEST
                    + Op.JUMPI(pc=0x13, condition=Op.ISZERO(0x1))
                    + Op.POP(Op.SHA3(offset=0x0, size=0x1000000))
                    + Op.JUMP(pc=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SHA3(offset=0x0, size=Op.SUB(0x0, 0x1)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex(
                        "610103600155600060006000600061dead6175305a03f450ba"
                    )
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x1, value=0x104)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=0xDEAD,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.JUMP(pc=0x0)
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.LT + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.JUMPDEST + Op.PC + Op.JUMP(pc=Op.SUB(Op.PC, 0x4))
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 2609},
                    code=Op.JUMPI(
                        pc=Op.PUSH2[0x11],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x0),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x3B])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x4D],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x1),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x75])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x87],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x2),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xAF])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0xC1],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x3),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xEB])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALLCODE(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=0x100, condition=Op.GT(Op.SLOAD(key=0x0), 0x4000000)
                    )
                    + Op.SLOAD(key=0x0)
                    + Op.JUMP(pc=0x105)
                    + Op.JUMPDEST
                    + Op.PUSH3[0xFFFFFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                    + Op.STOP,
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000002",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.REVERT(offset=0x0, size=0x10) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.JUMPDEST
                    + Op.JUMPI(pc=0x13, condition=Op.ISZERO(0x1))
                    + Op.POP(Op.SHA3(offset=0x0, size=0x1000000))
                    + Op.JUMP(pc=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SHA3(offset=0x0, size=Op.SUB(0x0, 0x1)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex(
                        "610103600155600060006000600061dead6175305a03f450ba"
                    )
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x1, value=0x104)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=0xDEAD,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.JUMP(pc=0x0)
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.LT + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.JUMPDEST + Op.PC + Op.JUMP(pc=Op.SUB(Op.PC, 0x4))
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 2609},
                    code=Op.JUMPI(
                        pc=Op.PUSH2[0x11],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x0),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x3B])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x4D],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x1),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x75])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x87],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x2),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xAF])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0xC1],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x3),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xEB])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALLCODE(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=0x100, condition=Op.GT(Op.SLOAD(key=0x0), 0x4000000)
                    )
                    + Op.SLOAD(key=0x0)
                    + Op.JUMP(pc=0x105)
                    + Op.JUMPDEST
                    + Op.PUSH3[0xFFFFFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                    + Op.STOP,
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000003",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.REVERT(offset=0x0, size=0x10) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.JUMPDEST
                    + Op.JUMPI(pc=0x13, condition=Op.ISZERO(0x1))
                    + Op.POP(Op.SHA3(offset=0x0, size=0x1000000))
                    + Op.JUMP(pc=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SHA3(offset=0x0, size=Op.SUB(0x0, 0x1)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex(
                        "610103600155600060006000600061dead6175305a03f450ba"
                    )
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x1, value=0x104)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=0xDEAD,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.JUMP(pc=0x0)
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.LT + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.JUMPDEST + Op.PC + Op.JUMP(pc=Op.SUB(Op.PC, 0x4))
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 2609},
                    code=Op.JUMPI(
                        pc=Op.PUSH2[0x11],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x0),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x3B])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x4D],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x1),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x75])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x87],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x2),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xAF])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0xC1],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x3),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xEB])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALLCODE(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=0x100, condition=Op.GT(Op.SLOAD(key=0x0), 0x4000000)
                    )
                    + Op.SLOAD(key=0x0)
                    + Op.JUMP(pc=0x105)
                    + Op.JUMPDEST
                    + Op.PUSH3[0xFFFFFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                    + Op.STOP,
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000000",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.REVERT(offset=0x0, size=0x10) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.JUMPDEST
                    + Op.JUMPI(pc=0x13, condition=Op.ISZERO(0x1))
                    + Op.POP(Op.SHA3(offset=0x0, size=0x1000000))
                    + Op.JUMP(pc=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SHA3(offset=0x0, size=Op.SUB(0x0, 0x1)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex(
                        "610103600155600060006000600061dead6175305a03f450ba"
                    )
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x1, value=0x104)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=0xDEAD,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.JUMP(pc=0x0)
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.LT + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.JUMPDEST + Op.PC + Op.JUMP(pc=Op.SUB(Op.PC, 0x4))
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 2609},
                    code=Op.JUMPI(
                        pc=Op.PUSH2[0x11],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x0),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x3B])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x4D],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x1),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x75])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x87],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x2),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xAF])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0xC1],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x3),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xEB])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALLCODE(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=0x100, condition=Op.GT(Op.SLOAD(key=0x0), 0x4000000)
                    )
                    + Op.SLOAD(key=0x0)
                    + Op.JUMP(pc=0x105)
                    + Op.JUMPDEST
                    + Op.PUSH3[0xFFFFFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                    + Op.STOP,
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000010060000000000000000000000000000000000000000000000000000000000000001",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.REVERT(offset=0x0, size=0x10) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.JUMPDEST
                    + Op.JUMPI(pc=0x13, condition=Op.ISZERO(0x1))
                    + Op.POP(Op.SHA3(offset=0x0, size=0x1000000))
                    + Op.JUMP(pc=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SHA3(offset=0x0, size=Op.SUB(0x0, 0x1)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex(
                        "610103600155600060006000600061dead6175305a03f450ba"
                    )
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x1, value=0x104)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=0xDEAD,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.JUMP(pc=0x0)
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.LT + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.JUMPDEST + Op.PC + Op.JUMP(pc=Op.SUB(Op.PC, 0x4))
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 0xFFFFFF},
                    code=Op.JUMPI(
                        pc=Op.PUSH2[0x11],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x0),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x3B])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x4D],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x1),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x75])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x87],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x2),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xAF])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0xC1],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x3),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xEB])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALLCODE(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=0x100, condition=Op.GT(Op.SLOAD(key=0x0), 0x4000000)
                    )
                    + Op.SLOAD(key=0x0)
                    + Op.JUMP(pc=0x105)
                    + Op.JUMPDEST
                    + Op.PUSH3[0xFFFFFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                    + Op.STOP,
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000010060000000000000000000000000000000000000000000000000000000000000002",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.REVERT(offset=0x0, size=0x10) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.JUMPDEST
                    + Op.JUMPI(pc=0x13, condition=Op.ISZERO(0x1))
                    + Op.POP(Op.SHA3(offset=0x0, size=0x1000000))
                    + Op.JUMP(pc=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SHA3(offset=0x0, size=Op.SUB(0x0, 0x1)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex(
                        "610103600155600060006000600061dead6175305a03f450ba"
                    )
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x1, value=0x104)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=0xDEAD,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.JUMP(pc=0x0)
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.LT + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.JUMPDEST + Op.PC + Op.JUMP(pc=Op.SUB(Op.PC, 0x4))
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 0xFFFFFF},
                    code=Op.JUMPI(
                        pc=Op.PUSH2[0x11],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x0),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x3B])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x4D],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x1),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x75])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x87],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x2),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xAF])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0xC1],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x3),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xEB])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALLCODE(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=0x100, condition=Op.GT(Op.SLOAD(key=0x0), 0x4000000)
                    )
                    + Op.SLOAD(key=0x0)
                    + Op.JUMP(pc=0x105)
                    + Op.JUMPDEST
                    + Op.PUSH3[0xFFFFFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                    + Op.STOP,
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000010060000000000000000000000000000000000000000000000000000000000000003",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.REVERT(offset=0x0, size=0x10) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.JUMPDEST
                    + Op.JUMPI(pc=0x13, condition=Op.ISZERO(0x1))
                    + Op.POP(Op.SHA3(offset=0x0, size=0x1000000))
                    + Op.JUMP(pc=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SHA3(offset=0x0, size=Op.SUB(0x0, 0x1)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex(
                        "610103600155600060006000600061dead6175305a03f450ba"
                    )
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x1, value=0x104)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=0xDEAD,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.JUMP(pc=0x0)
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.LT + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.JUMPDEST + Op.PC + Op.JUMP(pc=Op.SUB(Op.PC, 0x4))
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 0xFFFFFF},
                    code=Op.JUMPI(
                        pc=Op.PUSH2[0x11],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x0),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x3B])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x4D],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x1),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x75])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x87],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x2),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xAF])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0xC1],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x3),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xEB])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALLCODE(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=0x100, condition=Op.GT(Op.SLOAD(key=0x0), 0x4000000)
                    )
                    + Op.SLOAD(key=0x0)
                    + Op.JUMP(pc=0x105)
                    + Op.JUMPDEST
                    + Op.PUSH3[0xFFFFFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                    + Op.STOP,
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000010060000000000000000000000000000000000000000000000000000000000000000",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.REVERT(offset=0x0, size=0x10) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.JUMPDEST
                    + Op.JUMPI(pc=0x13, condition=Op.ISZERO(0x1))
                    + Op.POP(Op.SHA3(offset=0x0, size=0x1000000))
                    + Op.JUMP(pc=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SHA3(offset=0x0, size=Op.SUB(0x0, 0x1)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex(
                        "610103600155600060006000600061dead6175305a03f450ba"
                    )
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x1, value=0x104)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=0xDEAD,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.JUMP(pc=0x0)
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.LT + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.JUMPDEST + Op.PC + Op.JUMP(pc=Op.SUB(Op.PC, 0x4))
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 0xFFFFFF},
                    code=Op.JUMPI(
                        pc=Op.PUSH2[0x11],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x0),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x3B])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x4D],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x1),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x75])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x87],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x2),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xAF])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0xC1],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x3),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xEB])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALLCODE(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=0x100, condition=Op.GT(Op.SLOAD(key=0x0), 0x4000000)
                    )
                    + Op.SLOAD(key=0x0)
                    + Op.JUMP(pc=0x105)
                    + Op.JUMPDEST
                    + Op.PUSH3[0xFFFFFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                    + Op.STOP,
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000010050000000000000000000000000000000000000000000000000000000000000001",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.REVERT(offset=0x0, size=0x10) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.JUMPDEST
                    + Op.JUMPI(pc=0x13, condition=Op.ISZERO(0x1))
                    + Op.POP(Op.SHA3(offset=0x0, size=0x1000000))
                    + Op.JUMP(pc=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SHA3(offset=0x0, size=Op.SUB(0x0, 0x1)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex(
                        "610103600155600060006000600061dead6175305a03f450ba"
                    )
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x1, value=0x104)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=0xDEAD,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.JUMP(pc=0x0)
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.LT + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.JUMPDEST + Op.PC + Op.JUMP(pc=Op.SUB(Op.PC, 0x4))
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 0xFFFFFF},
                    code=Op.JUMPI(
                        pc=Op.PUSH2[0x11],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x0),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x3B])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x4D],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x1),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x75])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x87],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x2),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xAF])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0xC1],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x3),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xEB])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALLCODE(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=0x100, condition=Op.GT(Op.SLOAD(key=0x0), 0x4000000)
                    )
                    + Op.SLOAD(key=0x0)
                    + Op.JUMP(pc=0x105)
                    + Op.JUMPDEST
                    + Op.PUSH3[0xFFFFFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                    + Op.STOP,
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000010050000000000000000000000000000000000000000000000000000000000000002",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.REVERT(offset=0x0, size=0x10) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.JUMPDEST
                    + Op.JUMPI(pc=0x13, condition=Op.ISZERO(0x1))
                    + Op.POP(Op.SHA3(offset=0x0, size=0x1000000))
                    + Op.JUMP(pc=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SHA3(offset=0x0, size=Op.SUB(0x0, 0x1)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex(
                        "610103600155600060006000600061dead6175305a03f450ba"
                    )
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x1, value=0x104)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=0xDEAD,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.JUMP(pc=0x0)
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.LT + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.JUMPDEST + Op.PC + Op.JUMP(pc=Op.SUB(Op.PC, 0x4))
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 0xFFFFFF},
                    code=Op.JUMPI(
                        pc=Op.PUSH2[0x11],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x0),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x3B])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x4D],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x1),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x75])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x87],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x2),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xAF])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0xC1],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x3),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xEB])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALLCODE(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=0x100, condition=Op.GT(Op.SLOAD(key=0x0), 0x4000000)
                    )
                    + Op.SLOAD(key=0x0)
                    + Op.JUMP(pc=0x105)
                    + Op.JUMPDEST
                    + Op.PUSH3[0xFFFFFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                    + Op.STOP,
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000010050000000000000000000000000000000000000000000000000000000000000003",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.REVERT(offset=0x0, size=0x10) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.JUMPDEST
                    + Op.JUMPI(pc=0x13, condition=Op.ISZERO(0x1))
                    + Op.POP(Op.SHA3(offset=0x0, size=0x1000000))
                    + Op.JUMP(pc=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SHA3(offset=0x0, size=Op.SUB(0x0, 0x1)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex(
                        "610103600155600060006000600061dead6175305a03f450ba"
                    )
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x1, value=0x104)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=0xDEAD,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.JUMP(pc=0x0)
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.LT + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.JUMPDEST + Op.PC + Op.JUMP(pc=Op.SUB(Op.PC, 0x4))
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 0xFFFFFF},
                    code=Op.JUMPI(
                        pc=Op.PUSH2[0x11],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x0),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x3B])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x4D],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x1),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x75])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x87],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x2),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xAF])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0xC1],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x3),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xEB])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALLCODE(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=0x100, condition=Op.GT(Op.SLOAD(key=0x0), 0x4000000)
                    )
                    + Op.SLOAD(key=0x0)
                    + Op.JUMP(pc=0x105)
                    + Op.JUMPDEST
                    + Op.PUSH3[0xFFFFFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                    + Op.STOP,
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000010050000000000000000000000000000000000000000000000000000000000000000",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.REVERT(offset=0x0, size=0x10) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.JUMPDEST
                    + Op.JUMPI(pc=0x13, condition=Op.ISZERO(0x1))
                    + Op.POP(Op.SHA3(offset=0x0, size=0x1000000))
                    + Op.JUMP(pc=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SHA3(offset=0x0, size=Op.SUB(0x0, 0x1)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex(
                        "610103600155600060006000600061dead6175305a03f450ba"
                    )
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x1, value=0x104)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=0xDEAD,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.JUMP(pc=0x0)
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.LT + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.JUMPDEST + Op.PC + Op.JUMP(pc=Op.SUB(Op.PC, 0x4))
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 0xFFFFFF},
                    code=Op.JUMPI(
                        pc=Op.PUSH2[0x11],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x0),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x3B])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x4D],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x1),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x75])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x87],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x2),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xAF])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0xC1],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x3),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xEB])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALLCODE(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=0x100, condition=Op.GT(Op.SLOAD(key=0x0), 0x4000000)
                    )
                    + Op.SLOAD(key=0x0)
                    + Op.JUMP(pc=0x105)
                    + Op.JUMPDEST
                    + Op.PUSH3[0xFFFFFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                    + Op.STOP,
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000010020000000000000000000000000000000000000000000000000000000000000001",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.REVERT(offset=0x0, size=0x10) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.JUMPDEST
                    + Op.JUMPI(pc=0x13, condition=Op.ISZERO(0x1))
                    + Op.POP(Op.SHA3(offset=0x0, size=0x1000000))
                    + Op.JUMP(pc=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SHA3(offset=0x0, size=Op.SUB(0x0, 0x1)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex(
                        "610103600155600060006000600061dead6175305a03f450ba"
                    )
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x1, value=0x104)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=0xDEAD,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.JUMP(pc=0x0)
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.LT + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.JUMPDEST + Op.PC + Op.JUMP(pc=Op.SUB(Op.PC, 0x4))
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 0xFFFFFF},
                    code=Op.JUMPI(
                        pc=Op.PUSH2[0x11],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x0),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x3B])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x4D],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x1),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x75])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x87],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x2),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xAF])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0xC1],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x3),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xEB])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALLCODE(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=0x100, condition=Op.GT(Op.SLOAD(key=0x0), 0x4000000)
                    )
                    + Op.SLOAD(key=0x0)
                    + Op.JUMP(pc=0x105)
                    + Op.JUMPDEST
                    + Op.PUSH3[0xFFFFFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                    + Op.STOP,
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000010020000000000000000000000000000000000000000000000000000000000000002",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.REVERT(offset=0x0, size=0x10) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.JUMPDEST
                    + Op.JUMPI(pc=0x13, condition=Op.ISZERO(0x1))
                    + Op.POP(Op.SHA3(offset=0x0, size=0x1000000))
                    + Op.JUMP(pc=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SHA3(offset=0x0, size=Op.SUB(0x0, 0x1)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex(
                        "610103600155600060006000600061dead6175305a03f450ba"
                    )
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x1, value=0x104)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=0xDEAD,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.JUMP(pc=0x0)
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.LT + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.JUMPDEST + Op.PC + Op.JUMP(pc=Op.SUB(Op.PC, 0x4))
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 0xFFFFFF},
                    code=Op.JUMPI(
                        pc=Op.PUSH2[0x11],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x0),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x3B])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x4D],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x1),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x75])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x87],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x2),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xAF])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0xC1],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x3),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xEB])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALLCODE(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=0x100, condition=Op.GT(Op.SLOAD(key=0x0), 0x4000000)
                    )
                    + Op.SLOAD(key=0x0)
                    + Op.JUMP(pc=0x105)
                    + Op.JUMPDEST
                    + Op.PUSH3[0xFFFFFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                    + Op.STOP,
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000010020000000000000000000000000000000000000000000000000000000000000003",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.REVERT(offset=0x0, size=0x10) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.JUMPDEST
                    + Op.JUMPI(pc=0x13, condition=Op.ISZERO(0x1))
                    + Op.POP(Op.SHA3(offset=0x0, size=0x1000000))
                    + Op.JUMP(pc=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SHA3(offset=0x0, size=Op.SUB(0x0, 0x1)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex(
                        "610103600155600060006000600061dead6175305a03f450ba"
                    )
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x1, value=0x104)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=0xDEAD,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.JUMP(pc=0x0)
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.LT + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.JUMPDEST + Op.PC + Op.JUMP(pc=Op.SUB(Op.PC, 0x4))
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 0xFFFFFF},
                    code=Op.JUMPI(
                        pc=Op.PUSH2[0x11],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x0),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x3B])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x4D],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x1),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x75])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x87],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x2),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xAF])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0xC1],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x3),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xEB])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALLCODE(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=0x100, condition=Op.GT(Op.SLOAD(key=0x0), 0x4000000)
                    )
                    + Op.SLOAD(key=0x0)
                    + Op.JUMP(pc=0x105)
                    + Op.JUMPDEST
                    + Op.PUSH3[0xFFFFFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
                    + Op.STOP,
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000010020000000000000000000000000000000000000000000000000000000000000000",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.REVERT(offset=0x0, size=0x10) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.JUMPDEST
                    + Op.JUMPI(pc=0x13, condition=Op.ISZERO(0x1))
                    + Op.POP(Op.SHA3(offset=0x0, size=0x1000000))
                    + Op.JUMP(pc=0x0)
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SHA3(offset=0x0, size=Op.SUB(0x0, 0x1)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex(
                        "610103600155600060006000600061dead6175305a03f450ba"
                    )
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x1, value=0x104)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=0xDEAD,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.JUMP(pc=0x0)
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.LT + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.JUMPDEST + Op.PC + Op.JUMP(pc=Op.SUB(Op.PC, 0x4))
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 0xFFFFFF},
                    code=Op.JUMPI(
                        pc=Op.PUSH2[0x11],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x0),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x3B])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x4D],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x1),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0x75])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.DELEGATECALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0x87],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x2),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xAF])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x27,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=Op.PUSH2[0xC1],
                        condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x3),
                    )
                    + Op.POP(0x0)
                    + Op.JUMP(pc=Op.PUSH2[0xEB])
                    + Op.JUMPDEST
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALLCODE(
                            gas=Op.SUB(Op.GAS, 0x7530),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(
                                Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)
                            ),
                            0x2A,
                        ),
                    )
                    + Op.JUMPDEST
                    + Op.JUMPI(
                        pc=0x100, condition=Op.GT(Op.SLOAD(key=0x0), 0x4000000)
                    )
                    + Op.SLOAD(key=0x0)
                    + Op.JUMP(pc=0x105)
                    + Op.JUMPDEST
                    + Op.PUSH3[0xFFFFFF]
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.SSTORE
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
        "case26",
        "case27",
    ],
)
@pytest.mark.pre_alloc_mutable
def test_cost_revert(
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
        code=Op.REVERT(offset=0x0, size=0x10) + Op.STOP,
    )
    pre[callee_1] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.JUMPDEST
            + Op.JUMPI(pc=0x13, condition=Op.ISZERO(0x1))
            + Op.POP(Op.SHA3(offset=0x0, size=0x1000000))
            + Op.JUMP(pc=0x0)
            + Op.JUMPDEST
            + Op.STOP
        ),
    )
    pre[callee_2] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=Op.SHA3(offset=0x0, size=Op.SUB(0x0, 0x1)) + Op.STOP,
    )
    pre[callee_3] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex(
            "610103600155600060006000600061dead6175305a03f450ba"
        ),
    )
    pre[callee_4] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.SSTORE(key=0x1, value=0x104)
            + Op.POP(
                Op.DELEGATECALL(
                    gas=Op.SUB(Op.GAS, 0x7530),
                    address=0xDEAD,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.JUMP(pc=0x0)
        ),
    )
    pre[callee_5] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=Op.LT + Op.STOP,
    )
    pre[callee_6] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=Op.JUMPDEST + Op.PC + Op.JUMP(pc=Op.SUB(Op.PC, 0x4)),
    )
    pre[sender] = Account(balance=0x100000000000, nonce=0)
    pre[contract] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.JUMPI(
                pc=Op.PUSH2[0x11],
                condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x0),
            )
            + Op.POP(0x0)
            + Op.JUMP(pc=Op.PUSH2[0x3B])
            + Op.JUMPDEST
            + Op.MSTORE(offset=0x0, value=Op.GAS)
            + Op.POP(
                Op.CALL(
                    gas=Op.SUB(Op.GAS, 0x7530),
                    address=Op.CALLDATALOAD(offset=0x4),
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.MSTORE(offset=0x20, value=Op.GAS)
            + Op.SSTORE(
                key=0x0,
                value=Op.SUB(
                    Op.SUB(Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)),
                    0x2A,
                ),
            )
            + Op.JUMPDEST
            + Op.JUMPI(
                pc=Op.PUSH2[0x4D],
                condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x1),
            )
            + Op.POP(0x0)
            + Op.JUMP(pc=Op.PUSH2[0x75])
            + Op.JUMPDEST
            + Op.MSTORE(offset=0x0, value=Op.GAS)
            + Op.POP(
                Op.DELEGATECALL(
                    gas=Op.SUB(Op.GAS, 0x7530),
                    address=Op.CALLDATALOAD(offset=0x4),
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.MSTORE(offset=0x20, value=Op.GAS)
            + Op.SSTORE(
                key=0x0,
                value=Op.SUB(
                    Op.SUB(Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)),
                    0x27,
                ),
            )
            + Op.JUMPDEST
            + Op.JUMPI(
                pc=Op.PUSH2[0x87],
                condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x2),
            )
            + Op.POP(0x0)
            + Op.JUMP(pc=Op.PUSH2[0xAF])
            + Op.JUMPDEST
            + Op.MSTORE(offset=0x0, value=Op.GAS)
            + Op.POP(
                Op.STATICCALL(
                    gas=Op.SUB(Op.GAS, 0x7530),
                    address=Op.CALLDATALOAD(offset=0x4),
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.MSTORE(offset=0x20, value=Op.GAS)
            + Op.SSTORE(
                key=0x0,
                value=Op.SUB(
                    Op.SUB(Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)),
                    0x27,
                ),
            )
            + Op.JUMPDEST
            + Op.JUMPI(
                pc=Op.PUSH2[0xC1],
                condition=Op.EQ(Op.CALLDATALOAD(offset=0x24), 0x3),
            )
            + Op.POP(0x0)
            + Op.JUMP(pc=Op.PUSH2[0xEB])
            + Op.JUMPDEST
            + Op.MSTORE(offset=0x0, value=Op.GAS)
            + Op.POP(
                Op.CALLCODE(
                    gas=Op.SUB(Op.GAS, 0x7530),
                    address=Op.CALLDATALOAD(offset=0x4),
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.MSTORE(offset=0x20, value=Op.GAS)
            + Op.SSTORE(
                key=0x0,
                value=Op.SUB(
                    Op.SUB(Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)),
                    0x2A,
                ),
            )
            + Op.JUMPDEST
            + Op.JUMPI(pc=0x100, condition=Op.GT(Op.SLOAD(key=0x0), 0x4000000))
            + Op.SLOAD(key=0x0)
            + Op.JUMP(pc=0x105)
            + Op.JUMPDEST
            + Op.PUSH3[0xFFFFFF]
            + Op.JUMPDEST
            + Op.PUSH1[0x0]
            + Op.SSTORE
            + Op.STOP
        ),
    )

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=tx_data,
        gas_limit=80000000,
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
