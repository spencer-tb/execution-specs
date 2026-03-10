"""
Ori Pomerantz qbzzt1@gmail.com.

Ported from:
tests/static/state_tests/stEIP2930/variedContextFiller.yml
"""

import pytest
from execution_testing import (
    AccessList,
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
    ["tests/static/state_tests/stEIP2930/variedContextFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, tx_access_list, expected_post",
    [
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000001",  # noqa: E501
            [
                AccessList(
                    address=Address(
                        "0x000000000000000000000000000000000000c057"
                    ),
                    storage_keys=[
                        Hash(
                            "0x0000000000000000000000000000000000000000000000000000000000000000"  # noqa: E501
                        ),
                        Hash(
                            "0x00000000000000000000000000000000000000000000000000000000000060a7"  # noqa: E501
                        ),
                    ],
                )
            ],
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xC057,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xEAD0C057,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    storage={24743: 48879},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x1A
                        ),
                    )
                    + Op.REVERT(offset=0x0, size=0x40)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001011"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0111,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001012"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0112,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001013"): Account(
                    storage={0: 24743},
                    code=Op.MSTORE(offset=0x0, value=0xBAD)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xF113,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001014"): Account(
                    code=Op.CALL(
                        gas=0xB65,
                        address=0xF114,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001015"): Account(
                    code=Op.CALL(
                        gas=0x1800,
                        address=0xF115,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001016"): Account(
                    storage={0: 15, 24743: 57005},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0xBEEF, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0xA0, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x23
                        ),
                    )
                    + Op.MSTORE(offset=0x40, value=Op.GAS)
                    + Op.SSTORE(
                        key=Op.ADD(0xF000, Op.SLOAD(key=0x0)), value=0xBEEF
                    )
                    + Op.MSTORE(
                        offset=0x40,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x40), Op.GAS), 0x78
                        ),
                    )
                    + Op.MSTORE(offset=0x60, value=Op.GAS)
                    + Op.POP(Op.SLOAD(key=Op.ADD(0xF010, Op.SLOAD(key=0x0))))
                    + Op.MSTORE(
                        offset=0x60,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x60), Op.GAS), 0x7A
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x100, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x0),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x200, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x20),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x300, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x40),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x400, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x60),
                    )
                    + Op.JUMPI(
                        pc=0x9B, condition=Op.GT(Op.SLOAD(key=0x0), 0x0)
                    )
                    + Op.PUSH1[0x0]
                    + Op.JUMP(pc=0xB4)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=Op.SUB(Op.SLOAD(key=0x0), 0x1))
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0x1016,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.JUMPDEST
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001020"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x33, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x39, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001021"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x36, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x3C, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001022"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001023"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001024"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001025"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001026"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xF126,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0xF126,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000c057"): Account(
                    storage={0: 2, 1: 20003, 2: 107, 24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x10
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f113"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD60A7)
                    + Op.MSTORE(offset=0x0, value=0x600D)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000f114"): Account(
                    storage={0: 2989},
                    code=Op.SSTORE(key=0x0, value=0x600D) + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f115"): Account(
                    storage={0: 2989, 24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.SLOAD(key=0x60A7))
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f126"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x60A7)
                    + Op.MSTORE(
                        offset=0x0, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.JUMPI(
                        pc=0x24, condition=Op.EQ(Op.SLOAD(key=0x1), 0x0)
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.JUMP(pc=0x2B)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0111"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD)
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0112"): Account(
                    storage={0: 0xDEAD0060A7},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP,
                ),
                Address("0x00000000000000000000000000000000ead0c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x13
                        ),
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP,
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.ADD(
                                0x1000, Op.CALLDATALOAD(offset=0x4)
                            ),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x40,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x20))
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000001",  # noqa: E501
            [
                AccessList(
                    address=Address(
                        "0x0000000000000000000000000000000000001001"
                    ),
                    storage_keys=[
                        Hash(
                            "0x0000000000000000000000000000000000000000000000000000000000000000"  # noqa: E501
                        ),
                        Hash(
                            "0x00000000000000000000000000000000000000000000000000000000000060a7"  # noqa: E501
                        ),
                    ],
                )
            ],
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xC057,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xEAD0C057,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    storage={24743: 48879},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x1A
                        ),
                    )
                    + Op.REVERT(offset=0x0, size=0x40)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001011"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0111,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001012"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0112,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001013"): Account(
                    storage={0: 24743},
                    code=Op.MSTORE(offset=0x0, value=0xBAD)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xF113,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001014"): Account(
                    code=Op.CALL(
                        gas=0xB65,
                        address=0xF114,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001015"): Account(
                    code=Op.CALL(
                        gas=0x1800,
                        address=0xF115,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001016"): Account(
                    storage={0: 15, 24743: 57005},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0xBEEF, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0xA0, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x23
                        ),
                    )
                    + Op.MSTORE(offset=0x40, value=Op.GAS)
                    + Op.SSTORE(
                        key=Op.ADD(0xF000, Op.SLOAD(key=0x0)), value=0xBEEF
                    )
                    + Op.MSTORE(
                        offset=0x40,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x40), Op.GAS), 0x78
                        ),
                    )
                    + Op.MSTORE(offset=0x60, value=Op.GAS)
                    + Op.POP(Op.SLOAD(key=Op.ADD(0xF010, Op.SLOAD(key=0x0))))
                    + Op.MSTORE(
                        offset=0x60,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x60), Op.GAS), 0x7A
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x100, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x0),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x200, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x20),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x300, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x40),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x400, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x60),
                    )
                    + Op.JUMPI(
                        pc=0x9B, condition=Op.GT(Op.SLOAD(key=0x0), 0x0)
                    )
                    + Op.PUSH1[0x0]
                    + Op.JUMP(pc=0xB4)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=Op.SUB(Op.SLOAD(key=0x0), 0x1))
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0x1016,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.JUMPDEST
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001020"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x33, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x39, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001021"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x36, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x3C, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001022"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001023"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001024"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001025"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001026"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xF126,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0xF126,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000c057"): Account(
                    storage={0: 2, 1: 22103, 2: 2107, 24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x10
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f113"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD60A7)
                    + Op.MSTORE(offset=0x0, value=0x600D)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000f114"): Account(
                    storage={0: 2989},
                    code=Op.SSTORE(key=0x0, value=0x600D) + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f115"): Account(
                    storage={0: 2989, 24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.SLOAD(key=0x60A7))
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f126"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x60A7)
                    + Op.MSTORE(
                        offset=0x0, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.JUMPI(
                        pc=0x24, condition=Op.EQ(Op.SLOAD(key=0x1), 0x0)
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.JUMP(pc=0x2B)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0111"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD)
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0112"): Account(
                    storage={0: 0xDEAD0060A7},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP,
                ),
                Address("0x00000000000000000000000000000000ead0c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x13
                        ),
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP,
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.ADD(
                                0x1000, Op.CALLDATALOAD(offset=0x4)
                            ),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x40,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x20))
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000023",  # noqa: E501
            [
                AccessList(
                    address=Address(
                        "0x58fd03a2d731b2fb751e4a0f593d373ee77d39e6"
                    ),
                    storage_keys=[
                        Hash(
                            "0x000000000000000000000000000000000000000000000000000000000000ffff"  # noqa: E501
                        )
                    ],
                )
            ],
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xC057,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xEAD0C057,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    storage={24743: 48879},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x1A
                        ),
                    )
                    + Op.REVERT(offset=0x0, size=0x40)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001011"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0111,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001012"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0112,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001013"): Account(
                    storage={0: 24743},
                    code=Op.MSTORE(offset=0x0, value=0xBAD)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xF113,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001014"): Account(
                    code=Op.CALL(
                        gas=0xB65,
                        address=0xF114,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001015"): Account(
                    code=Op.CALL(
                        gas=0x1800,
                        address=0xF115,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001016"): Account(
                    storage={0: 15, 24743: 57005},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0xBEEF, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0xA0, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x23
                        ),
                    )
                    + Op.MSTORE(offset=0x40, value=Op.GAS)
                    + Op.SSTORE(
                        key=Op.ADD(0xF000, Op.SLOAD(key=0x0)), value=0xBEEF
                    )
                    + Op.MSTORE(
                        offset=0x40,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x40), Op.GAS), 0x78
                        ),
                    )
                    + Op.MSTORE(offset=0x60, value=Op.GAS)
                    + Op.POP(Op.SLOAD(key=Op.ADD(0xF010, Op.SLOAD(key=0x0))))
                    + Op.MSTORE(
                        offset=0x60,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x60), Op.GAS), 0x7A
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x100, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x0),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x200, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x20),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x300, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x40),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x400, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x60),
                    )
                    + Op.JUMPI(
                        pc=0x9B, condition=Op.GT(Op.SLOAD(key=0x0), 0x0)
                    )
                    + Op.PUSH1[0x0]
                    + Op.JUMP(pc=0xB4)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=Op.SUB(Op.SLOAD(key=0x0), 0x1))
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0x1016,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.JUMPDEST
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001020"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x33, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x39, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001021"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x36, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x3C, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001022"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001023"): Account(
                    storage={1: 0x530508498D2AA75D8E591612809FEC3D37A45615},
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001024"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001025"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001026"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xF126,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0xF126,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x10
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f113"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD60A7)
                    + Op.MSTORE(offset=0x0, value=0x600D)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000f114"): Account(
                    storage={0: 2989},
                    code=Op.SSTORE(key=0x0, value=0x600D) + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f115"): Account(
                    storage={0: 2989, 24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.SLOAD(key=0x60A7))
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f126"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x60A7)
                    + Op.MSTORE(
                        offset=0x0, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.JUMPI(
                        pc=0x24, condition=Op.EQ(Op.SLOAD(key=0x1), 0x0)
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.JUMP(pc=0x2B)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0111"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD)
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0112"): Account(
                    storage={0: 0xDEAD0060A7},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP,
                ),
                Address("0x00000000000000000000000000000000ead0c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x13
                        ),
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP,
                ),
                Address("0x530508498d2aa75d8e591612809fec3d37a45615"): Account(
                    storage={0: 65535, 1: 22117},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP,
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.ADD(
                                0x1000, Op.CALLDATALOAD(offset=0x4)
                            ),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x40,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x20))
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000023",  # noqa: E501
            [
                AccessList(
                    address=Address(
                        "0x530508498d2aa75d8e591612809fec3d37a45615"
                    ),
                    storage_keys=[
                        Hash(
                            "0x0000000000000000000000000000000000000000000000000000000000000000"  # noqa: E501
                        )
                    ],
                )
            ],
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xC057,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xEAD0C057,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    storage={24743: 48879},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x1A
                        ),
                    )
                    + Op.REVERT(offset=0x0, size=0x40)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001011"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0111,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001012"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0112,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001013"): Account(
                    storage={0: 24743},
                    code=Op.MSTORE(offset=0x0, value=0xBAD)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xF113,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001014"): Account(
                    code=Op.CALL(
                        gas=0xB65,
                        address=0xF114,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001015"): Account(
                    code=Op.CALL(
                        gas=0x1800,
                        address=0xF115,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001016"): Account(
                    storage={0: 15, 24743: 57005},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0xBEEF, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0xA0, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x23
                        ),
                    )
                    + Op.MSTORE(offset=0x40, value=Op.GAS)
                    + Op.SSTORE(
                        key=Op.ADD(0xF000, Op.SLOAD(key=0x0)), value=0xBEEF
                    )
                    + Op.MSTORE(
                        offset=0x40,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x40), Op.GAS), 0x78
                        ),
                    )
                    + Op.MSTORE(offset=0x60, value=Op.GAS)
                    + Op.POP(Op.SLOAD(key=Op.ADD(0xF010, Op.SLOAD(key=0x0))))
                    + Op.MSTORE(
                        offset=0x60,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x60), Op.GAS), 0x7A
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x100, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x0),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x200, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x20),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x300, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x40),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x400, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x60),
                    )
                    + Op.JUMPI(
                        pc=0x9B, condition=Op.GT(Op.SLOAD(key=0x0), 0x0)
                    )
                    + Op.PUSH1[0x0]
                    + Op.JUMP(pc=0xB4)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=Op.SUB(Op.SLOAD(key=0x0), 0x1))
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0x1016,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.JUMPDEST
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001020"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x33, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x39, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001021"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x36, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x3C, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001022"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001023"): Account(
                    storage={1: 0x530508498D2AA75D8E591612809FEC3D37A45615},
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001024"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001025"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001026"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xF126,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0xF126,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x10
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f113"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD60A7)
                    + Op.MSTORE(offset=0x0, value=0x600D)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000f114"): Account(
                    storage={0: 2989},
                    code=Op.SSTORE(key=0x0, value=0x600D) + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f115"): Account(
                    storage={0: 2989, 24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.SLOAD(key=0x60A7))
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f126"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x60A7)
                    + Op.MSTORE(
                        offset=0x0, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.JUMPI(
                        pc=0x24, condition=Op.EQ(Op.SLOAD(key=0x1), 0x0)
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.JUMP(pc=0x2B)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0111"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD)
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0112"): Account(
                    storage={0: 0xDEAD0060A7},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP,
                ),
                Address("0x00000000000000000000000000000000ead0c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x13
                        ),
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP,
                ),
                Address("0x530508498d2aa75d8e591612809fec3d37a45615"): Account(
                    storage={0: 65535, 1: 20017},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP,
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.ADD(
                                0x1000, Op.CALLDATALOAD(offset=0x4)
                            ),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x40,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x20))
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000022",  # noqa: E501
            [
                AccessList(
                    address=Address(
                        "0x58fd03a2d731b2fb751e4a0f593d373ee77d39e6"
                    ),
                    storage_keys=[
                        Hash(
                            "0x000000000000000000000000000000000000000000000000000000000000ffff"  # noqa: E501
                        )
                    ],
                )
            ],
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xC057,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xEAD0C057,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    storage={24743: 48879},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x1A
                        ),
                    )
                    + Op.REVERT(offset=0x0, size=0x40)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001011"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0111,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001012"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0112,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001013"): Account(
                    storage={0: 24743},
                    code=Op.MSTORE(offset=0x0, value=0xBAD)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xF113,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001014"): Account(
                    code=Op.CALL(
                        gas=0xB65,
                        address=0xF114,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001015"): Account(
                    code=Op.CALL(
                        gas=0x1800,
                        address=0xF115,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001016"): Account(
                    storage={0: 15, 24743: 57005},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0xBEEF, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0xA0, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x23
                        ),
                    )
                    + Op.MSTORE(offset=0x40, value=Op.GAS)
                    + Op.SSTORE(
                        key=Op.ADD(0xF000, Op.SLOAD(key=0x0)), value=0xBEEF
                    )
                    + Op.MSTORE(
                        offset=0x40,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x40), Op.GAS), 0x78
                        ),
                    )
                    + Op.MSTORE(offset=0x60, value=Op.GAS)
                    + Op.POP(Op.SLOAD(key=Op.ADD(0xF010, Op.SLOAD(key=0x0))))
                    + Op.MSTORE(
                        offset=0x60,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x60), Op.GAS), 0x7A
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x100, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x0),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x200, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x20),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x300, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x40),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x400, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x60),
                    )
                    + Op.JUMPI(
                        pc=0x9B, condition=Op.GT(Op.SLOAD(key=0x0), 0x0)
                    )
                    + Op.PUSH1[0x0]
                    + Op.JUMP(pc=0xB4)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=Op.SUB(Op.SLOAD(key=0x0), 0x1))
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0x1016,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.JUMPDEST
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001020"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x33, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x39, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001021"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x36, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x3C, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001022"): Account(
                    storage={1: 0x58FD03A2D731B2FB751E4A0F593D373EE77D39E6},
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001023"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001024"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001025"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001026"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xF126,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0xF126,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x10
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f113"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD60A7)
                    + Op.MSTORE(offset=0x0, value=0x600D)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000f114"): Account(
                    storage={0: 2989},
                    code=Op.SSTORE(key=0x0, value=0x600D) + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f115"): Account(
                    storage={0: 2989, 24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.SLOAD(key=0x60A7))
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f126"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x60A7)
                    + Op.MSTORE(
                        offset=0x0, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.JUMPI(
                        pc=0x24, condition=Op.EQ(Op.SLOAD(key=0x1), 0x0)
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.JUMP(pc=0x2B)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0111"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD)
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0112"): Account(
                    storage={0: 0xDEAD0060A7},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP,
                ),
                Address("0x00000000000000000000000000000000ead0c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x13
                        ),
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP,
                ),
                Address("0x58fd03a2d731b2fb751e4a0f593d373ee77d39e6"): Account(
                    storage={0: 65535, 1: 22117},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP,
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.ADD(
                                0x1000, Op.CALLDATALOAD(offset=0x4)
                            ),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x40,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x20))
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000022",  # noqa: E501
            [
                AccessList(
                    address=Address(
                        "0x58fd03a2d731b2fb751e4a0f593d373ee77d39e6"
                    ),
                    storage_keys=[
                        Hash(
                            "0x0000000000000000000000000000000000000000000000000000000000000000"  # noqa: E501
                        )
                    ],
                )
            ],
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xC057,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xEAD0C057,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    storage={24743: 48879},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x1A
                        ),
                    )
                    + Op.REVERT(offset=0x0, size=0x40)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001011"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0111,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001012"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0112,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001013"): Account(
                    storage={0: 24743},
                    code=Op.MSTORE(offset=0x0, value=0xBAD)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xF113,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001014"): Account(
                    code=Op.CALL(
                        gas=0xB65,
                        address=0xF114,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001015"): Account(
                    code=Op.CALL(
                        gas=0x1800,
                        address=0xF115,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001016"): Account(
                    storage={0: 15, 24743: 57005},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0xBEEF, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0xA0, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x23
                        ),
                    )
                    + Op.MSTORE(offset=0x40, value=Op.GAS)
                    + Op.SSTORE(
                        key=Op.ADD(0xF000, Op.SLOAD(key=0x0)), value=0xBEEF
                    )
                    + Op.MSTORE(
                        offset=0x40,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x40), Op.GAS), 0x78
                        ),
                    )
                    + Op.MSTORE(offset=0x60, value=Op.GAS)
                    + Op.POP(Op.SLOAD(key=Op.ADD(0xF010, Op.SLOAD(key=0x0))))
                    + Op.MSTORE(
                        offset=0x60,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x60), Op.GAS), 0x7A
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x100, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x0),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x200, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x20),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x300, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x40),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x400, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x60),
                    )
                    + Op.JUMPI(
                        pc=0x9B, condition=Op.GT(Op.SLOAD(key=0x0), 0x0)
                    )
                    + Op.PUSH1[0x0]
                    + Op.JUMP(pc=0xB4)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=Op.SUB(Op.SLOAD(key=0x0), 0x1))
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0x1016,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.JUMPDEST
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001020"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x33, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x39, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001021"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x36, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x3C, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001022"): Account(
                    storage={1: 0x58FD03A2D731B2FB751E4A0F593D373EE77D39E6},
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001023"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001024"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001025"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001026"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xF126,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0xF126,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x10
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f113"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD60A7)
                    + Op.MSTORE(offset=0x0, value=0x600D)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000f114"): Account(
                    storage={0: 2989},
                    code=Op.SSTORE(key=0x0, value=0x600D) + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f115"): Account(
                    storage={0: 2989, 24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.SLOAD(key=0x60A7))
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f126"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x60A7)
                    + Op.MSTORE(
                        offset=0x0, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.JUMPI(
                        pc=0x24, condition=Op.EQ(Op.SLOAD(key=0x1), 0x0)
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.JUMP(pc=0x2B)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0111"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD)
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0112"): Account(
                    storage={0: 0xDEAD0060A7},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP,
                ),
                Address("0x00000000000000000000000000000000ead0c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x13
                        ),
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP,
                ),
                Address("0x58fd03a2d731b2fb751e4a0f593d373ee77d39e6"): Account(
                    storage={0: 65535, 1: 20017},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP,
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.ADD(
                                0x1000, Op.CALLDATALOAD(offset=0x4)
                            ),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x40,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x20))
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000012",  # noqa: E501
            [
                AccessList(
                    address=Address(
                        "0x0000000000000000000000000000000000001012"
                    ),
                    storage_keys=[
                        Hash(
                            "0x0000000000000000000000000000000000000000000000000000000000000000"  # noqa: E501
                        )
                    ],
                )
            ],
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xC057,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xEAD0C057,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    storage={24743: 48879},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x1A
                        ),
                    )
                    + Op.REVERT(offset=0x0, size=0x40)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001011"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0111,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001012"): Account(
                    storage={0: 4600},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0112,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001013"): Account(
                    storage={0: 24743},
                    code=Op.MSTORE(offset=0x0, value=0xBAD)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xF113,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001014"): Account(
                    code=Op.CALL(
                        gas=0xB65,
                        address=0xF114,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001015"): Account(
                    code=Op.CALL(
                        gas=0x1800,
                        address=0xF115,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001016"): Account(
                    storage={0: 15, 24743: 57005},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0xBEEF, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0xA0, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x23
                        ),
                    )
                    + Op.MSTORE(offset=0x40, value=Op.GAS)
                    + Op.SSTORE(
                        key=Op.ADD(0xF000, Op.SLOAD(key=0x0)), value=0xBEEF
                    )
                    + Op.MSTORE(
                        offset=0x40,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x40), Op.GAS), 0x78
                        ),
                    )
                    + Op.MSTORE(offset=0x60, value=Op.GAS)
                    + Op.POP(Op.SLOAD(key=Op.ADD(0xF010, Op.SLOAD(key=0x0))))
                    + Op.MSTORE(
                        offset=0x60,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x60), Op.GAS), 0x7A
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x100, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x0),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x200, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x20),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x300, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x40),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x400, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x60),
                    )
                    + Op.JUMPI(
                        pc=0x9B, condition=Op.GT(Op.SLOAD(key=0x0), 0x0)
                    )
                    + Op.PUSH1[0x0]
                    + Op.JUMP(pc=0xB4)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=Op.SUB(Op.SLOAD(key=0x0), 0x1))
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0x1016,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.JUMPDEST
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001020"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x33, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x39, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001021"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x36, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x3C, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001022"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001023"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001024"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001025"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001026"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xF126,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0xF126,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x10
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f113"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD60A7)
                    + Op.MSTORE(offset=0x0, value=0x600D)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000f114"): Account(
                    storage={0: 2989},
                    code=Op.SSTORE(key=0x0, value=0x600D) + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f115"): Account(
                    storage={0: 2989, 24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.SLOAD(key=0x60A7))
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f126"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x60A7)
                    + Op.MSTORE(
                        offset=0x0, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.JUMPI(
                        pc=0x24, condition=Op.EQ(Op.SLOAD(key=0x1), 0x0)
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.JUMP(pc=0x2B)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0111"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD)
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0112"): Account(
                    storage={0: 0xDEAD0060A7},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP,
                ),
                Address("0x00000000000000000000000000000000ead0c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x13
                        ),
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP,
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.ADD(
                                0x1000, Op.CALLDATALOAD(offset=0x4)
                            ),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x40,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x20))
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000012",  # noqa: E501
            [
                AccessList(
                    address=Address(
                        "0x00000000000000000000000000000000dead0112"
                    ),
                    storage_keys=[
                        Hash(
                            "0x0000000000000000000000000000000000000000000000000000000000000000"  # noqa: E501
                        )
                    ],
                )
            ],
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xC057,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xEAD0C057,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    storage={24743: 48879},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x1A
                        ),
                    )
                    + Op.REVERT(offset=0x0, size=0x40)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001011"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0111,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001012"): Account(
                    storage={0: 100},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0112,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001013"): Account(
                    storage={0: 24743},
                    code=Op.MSTORE(offset=0x0, value=0xBAD)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xF113,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001014"): Account(
                    code=Op.CALL(
                        gas=0xB65,
                        address=0xF114,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001015"): Account(
                    code=Op.CALL(
                        gas=0x1800,
                        address=0xF115,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001016"): Account(
                    storage={0: 15, 24743: 57005},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0xBEEF, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0xA0, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x23
                        ),
                    )
                    + Op.MSTORE(offset=0x40, value=Op.GAS)
                    + Op.SSTORE(
                        key=Op.ADD(0xF000, Op.SLOAD(key=0x0)), value=0xBEEF
                    )
                    + Op.MSTORE(
                        offset=0x40,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x40), Op.GAS), 0x78
                        ),
                    )
                    + Op.MSTORE(offset=0x60, value=Op.GAS)
                    + Op.POP(Op.SLOAD(key=Op.ADD(0xF010, Op.SLOAD(key=0x0))))
                    + Op.MSTORE(
                        offset=0x60,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x60), Op.GAS), 0x7A
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x100, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x0),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x200, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x20),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x300, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x40),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x400, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x60),
                    )
                    + Op.JUMPI(
                        pc=0x9B, condition=Op.GT(Op.SLOAD(key=0x0), 0x0)
                    )
                    + Op.PUSH1[0x0]
                    + Op.JUMP(pc=0xB4)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=Op.SUB(Op.SLOAD(key=0x0), 0x1))
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0x1016,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.JUMPDEST
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001020"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x33, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x39, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001021"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x36, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x3C, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001022"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001023"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001024"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001025"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001026"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xF126,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0xF126,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x10
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f113"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD60A7)
                    + Op.MSTORE(offset=0x0, value=0x600D)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000f114"): Account(
                    storage={0: 2989},
                    code=Op.SSTORE(key=0x0, value=0x600D) + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f115"): Account(
                    storage={0: 2989, 24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.SLOAD(key=0x60A7))
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f126"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x60A7)
                    + Op.MSTORE(
                        offset=0x0, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.JUMPI(
                        pc=0x24, condition=Op.EQ(Op.SLOAD(key=0x1), 0x0)
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.JUMP(pc=0x2B)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0111"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD)
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0112"): Account(
                    storage={0: 0xDEAD0060A7},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP,
                ),
                Address("0x00000000000000000000000000000000ead0c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x13
                        ),
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP,
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.ADD(
                                0x1000, Op.CALLDATALOAD(offset=0x4)
                            ),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x40,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x20))
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000010",  # noqa: E501
            [
                AccessList(
                    address=Address(
                        "0x0000000000000000000000000000000000001010"
                    ),
                    storage_keys=[
                        Hash(
                            "0x0000000000000000000000000000000000000000000000000000000000000000"  # noqa: E501
                        ),
                        Hash(
                            "0x00000000000000000000000000000000000000000000000000000000000060a7"  # noqa: E501
                        ),
                    ],
                )
            ],
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xC057,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xEAD0C057,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    storage={24743: 48879},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x1A
                        ),
                    )
                    + Op.REVERT(offset=0x0, size=0x40)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001011"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0111,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001012"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0112,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001013"): Account(
                    storage={0: 24743},
                    code=Op.MSTORE(offset=0x0, value=0xBAD)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xF113,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001014"): Account(
                    code=Op.CALL(
                        gas=0xB65,
                        address=0xF114,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001015"): Account(
                    code=Op.CALL(
                        gas=0x1800,
                        address=0xF115,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001016"): Account(
                    storage={0: 15, 24743: 57005},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0xBEEF, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0xA0, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x23
                        ),
                    )
                    + Op.MSTORE(offset=0x40, value=Op.GAS)
                    + Op.SSTORE(
                        key=Op.ADD(0xF000, Op.SLOAD(key=0x0)), value=0xBEEF
                    )
                    + Op.MSTORE(
                        offset=0x40,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x40), Op.GAS), 0x78
                        ),
                    )
                    + Op.MSTORE(offset=0x60, value=Op.GAS)
                    + Op.POP(Op.SLOAD(key=Op.ADD(0xF010, Op.SLOAD(key=0x0))))
                    + Op.MSTORE(
                        offset=0x60,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x60), Op.GAS), 0x7A
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x100, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x0),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x200, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x20),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x300, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x40),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x400, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x60),
                    )
                    + Op.JUMPI(
                        pc=0x9B, condition=Op.GT(Op.SLOAD(key=0x0), 0x0)
                    )
                    + Op.PUSH1[0x0]
                    + Op.JUMP(pc=0xB4)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=Op.SUB(Op.SLOAD(key=0x0), 0x1))
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0x1016,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.JUMPDEST
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001020"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x33, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x39, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001021"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x36, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x3C, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001022"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001023"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001024"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001025"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001026"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xF126,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0xF126,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x10
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f113"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD60A7)
                    + Op.MSTORE(offset=0x0, value=0x600D)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000f114"): Account(
                    storage={0: 2989},
                    code=Op.SSTORE(key=0x0, value=0x600D) + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f115"): Account(
                    storage={0: 2989, 24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.SLOAD(key=0x60A7))
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f126"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x60A7)
                    + Op.MSTORE(
                        offset=0x0, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.JUMPI(
                        pc=0x24, condition=Op.EQ(Op.SLOAD(key=0x1), 0x0)
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.JUMP(pc=0x2B)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0111"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD)
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0112"): Account(
                    storage={0: 0xDEAD0060A7},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP,
                ),
                Address("0x00000000000000000000000000000000ead0c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x13
                        ),
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP,
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 20003, 1: 100},
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.ADD(
                                0x1000, Op.CALLDATALOAD(offset=0x4)
                            ),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x40,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x20))
                    + Op.STOP,
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000010",  # noqa: E501
            [
                AccessList(
                    address=Address(
                        "0xcccccccccccccccccccccccccccccccccccccccc"
                    ),
                    storage_keys=[
                        Hash(
                            "0x0000000000000000000000000000000000000000000000000000000000000000"  # noqa: E501
                        ),
                        Hash(
                            "0x00000000000000000000000000000000000000000000000000000000000060a7"  # noqa: E501
                        ),
                    ],
                )
            ],
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xC057,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xEAD0C057,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    storage={24743: 48879},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x1A
                        ),
                    )
                    + Op.REVERT(offset=0x0, size=0x40)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001011"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0111,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001012"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0112,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001013"): Account(
                    storage={0: 24743},
                    code=Op.MSTORE(offset=0x0, value=0xBAD)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xF113,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001014"): Account(
                    code=Op.CALL(
                        gas=0xB65,
                        address=0xF114,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001015"): Account(
                    code=Op.CALL(
                        gas=0x1800,
                        address=0xF115,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001016"): Account(
                    storage={0: 15, 24743: 57005},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0xBEEF, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0xA0, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x23
                        ),
                    )
                    + Op.MSTORE(offset=0x40, value=Op.GAS)
                    + Op.SSTORE(
                        key=Op.ADD(0xF000, Op.SLOAD(key=0x0)), value=0xBEEF
                    )
                    + Op.MSTORE(
                        offset=0x40,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x40), Op.GAS), 0x78
                        ),
                    )
                    + Op.MSTORE(offset=0x60, value=Op.GAS)
                    + Op.POP(Op.SLOAD(key=Op.ADD(0xF010, Op.SLOAD(key=0x0))))
                    + Op.MSTORE(
                        offset=0x60,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x60), Op.GAS), 0x7A
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x100, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x0),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x200, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x20),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x300, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x40),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x400, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x60),
                    )
                    + Op.JUMPI(
                        pc=0x9B, condition=Op.GT(Op.SLOAD(key=0x0), 0x0)
                    )
                    + Op.PUSH1[0x0]
                    + Op.JUMP(pc=0xB4)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=Op.SUB(Op.SLOAD(key=0x0), 0x1))
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0x1016,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.JUMPDEST
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001020"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x33, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x39, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001021"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x36, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x3C, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001022"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001023"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001024"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001025"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001026"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xF126,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0xF126,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x10
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f113"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD60A7)
                    + Op.MSTORE(offset=0x0, value=0x600D)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000f114"): Account(
                    storage={0: 2989},
                    code=Op.SSTORE(key=0x0, value=0x600D) + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f115"): Account(
                    storage={0: 2989, 24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.SLOAD(key=0x60A7))
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f126"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x60A7)
                    + Op.MSTORE(
                        offset=0x0, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.JUMPI(
                        pc=0x24, condition=Op.EQ(Op.SLOAD(key=0x1), 0x0)
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.JUMP(pc=0x2B)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0111"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD)
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0112"): Account(
                    storage={0: 0xDEAD0060A7},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP,
                ),
                Address("0x00000000000000000000000000000000ead0c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x13
                        ),
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP,
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 22103, 1: 2100},
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.ADD(
                                0x1000, Op.CALLDATALOAD(offset=0x4)
                            ),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x40,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x20))
                    + Op.STOP,
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000026",  # noqa: E501
            [
                AccessList(
                    address=Address(
                        "0x000000000000000000000000000000000000f126"
                    ),
                    storage_keys=[
                        Hash(
                            "0x0000000000000000000000000000000000000000000000000000000000000020"  # noqa: E501
                        )
                    ],
                )
            ],
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xC057,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xEAD0C057,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    storage={24743: 48879},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x1A
                        ),
                    )
                    + Op.REVERT(offset=0x0, size=0x40)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001011"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0111,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001012"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0112,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001013"): Account(
                    storage={0: 24743},
                    code=Op.MSTORE(offset=0x0, value=0xBAD)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xF113,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001014"): Account(
                    code=Op.CALL(
                        gas=0xB65,
                        address=0xF114,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001015"): Account(
                    code=Op.CALL(
                        gas=0x1800,
                        address=0xF115,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001016"): Account(
                    storage={0: 15, 24743: 57005},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0xBEEF, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0xA0, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x23
                        ),
                    )
                    + Op.MSTORE(offset=0x40, value=Op.GAS)
                    + Op.SSTORE(
                        key=Op.ADD(0xF000, Op.SLOAD(key=0x0)), value=0xBEEF
                    )
                    + Op.MSTORE(
                        offset=0x40,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x40), Op.GAS), 0x78
                        ),
                    )
                    + Op.MSTORE(offset=0x60, value=Op.GAS)
                    + Op.POP(Op.SLOAD(key=Op.ADD(0xF010, Op.SLOAD(key=0x0))))
                    + Op.MSTORE(
                        offset=0x60,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x60), Op.GAS), 0x7A
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x100, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x0),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x200, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x20),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x300, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x40),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x400, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x60),
                    )
                    + Op.JUMPI(
                        pc=0x9B, condition=Op.GT(Op.SLOAD(key=0x0), 0x0)
                    )
                    + Op.PUSH1[0x0]
                    + Op.JUMP(pc=0xB4)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=Op.SUB(Op.SLOAD(key=0x0), 0x1))
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0x1016,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.JUMPDEST
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001020"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x33, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x39, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001021"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x36, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x3C, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001022"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001023"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001024"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001025"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001026"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xF126,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0xF126,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x10
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f113"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD60A7)
                    + Op.MSTORE(offset=0x0, value=0x600D)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000f114"): Account(
                    storage={0: 2989},
                    code=Op.SSTORE(key=0x0, value=0x600D) + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f115"): Account(
                    storage={0: 2989, 24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.SLOAD(key=0x60A7))
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f126"): Account(
                    storage={0: 24743, 1: 22117, 2: 117},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x60A7)
                    + Op.MSTORE(
                        offset=0x0, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.JUMPI(
                        pc=0x24, condition=Op.EQ(Op.SLOAD(key=0x1), 0x0)
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.JUMP(pc=0x2B)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.JUMPDEST
                    + Op.STOP,
                ),
                Address("0x00000000000000000000000000000000dead0111"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD)
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0112"): Account(
                    storage={0: 0xDEAD0060A7},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP,
                ),
                Address("0x00000000000000000000000000000000ead0c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x13
                        ),
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP,
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.ADD(
                                0x1000, Op.CALLDATALOAD(offset=0x4)
                            ),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x40,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x20))
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000026",  # noqa: E501
            [
                AccessList(
                    address=Address(
                        "0x000000000000000000000000000000000000f126"
                    ),
                    storage_keys=[
                        Hash(
                            "0x0000000000000000000000000000000000000000000000000000000000000000"  # noqa: E501
                        )
                    ],
                )
            ],
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xC057,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xEAD0C057,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    storage={24743: 48879},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x1A
                        ),
                    )
                    + Op.REVERT(offset=0x0, size=0x40)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001011"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0111,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001012"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0112,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001013"): Account(
                    storage={0: 24743},
                    code=Op.MSTORE(offset=0x0, value=0xBAD)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xF113,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001014"): Account(
                    code=Op.CALL(
                        gas=0xB65,
                        address=0xF114,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001015"): Account(
                    code=Op.CALL(
                        gas=0x1800,
                        address=0xF115,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001016"): Account(
                    storage={0: 15, 24743: 57005},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0xBEEF, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0xA0, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x23
                        ),
                    )
                    + Op.MSTORE(offset=0x40, value=Op.GAS)
                    + Op.SSTORE(
                        key=Op.ADD(0xF000, Op.SLOAD(key=0x0)), value=0xBEEF
                    )
                    + Op.MSTORE(
                        offset=0x40,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x40), Op.GAS), 0x78
                        ),
                    )
                    + Op.MSTORE(offset=0x60, value=Op.GAS)
                    + Op.POP(Op.SLOAD(key=Op.ADD(0xF010, Op.SLOAD(key=0x0))))
                    + Op.MSTORE(
                        offset=0x60,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x60), Op.GAS), 0x7A
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x100, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x0),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x200, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x20),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x300, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x40),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x400, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x60),
                    )
                    + Op.JUMPI(
                        pc=0x9B, condition=Op.GT(Op.SLOAD(key=0x0), 0x0)
                    )
                    + Op.PUSH1[0x0]
                    + Op.JUMP(pc=0xB4)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=Op.SUB(Op.SLOAD(key=0x0), 0x1))
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0x1016,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.JUMPDEST
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001020"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x33, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x39, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001021"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x36, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x3C, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001022"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001023"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001024"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001025"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001026"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xF126,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0xF126,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x10
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f113"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD60A7)
                    + Op.MSTORE(offset=0x0, value=0x600D)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000f114"): Account(
                    storage={0: 2989},
                    code=Op.SSTORE(key=0x0, value=0x600D) + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f115"): Account(
                    storage={0: 2989, 24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.SLOAD(key=0x60A7))
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f126"): Account(
                    storage={0: 24743, 1: 20017, 2: 117},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x60A7)
                    + Op.MSTORE(
                        offset=0x0, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.JUMPI(
                        pc=0x24, condition=Op.EQ(Op.SLOAD(key=0x1), 0x0)
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.JUMP(pc=0x2B)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.JUMPDEST
                    + Op.STOP,
                ),
                Address("0x00000000000000000000000000000000dead0111"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD)
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0112"): Account(
                    storage={0: 0xDEAD0060A7},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP,
                ),
                Address("0x00000000000000000000000000000000ead0c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x13
                        ),
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP,
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.ADD(
                                0x1000, Op.CALLDATALOAD(offset=0x4)
                            ),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x40,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x20))
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000011",  # noqa: E501
            [
                AccessList(
                    address=Address(
                        "0x0000000000000000000000000000000000001011"
                    ),
                    storage_keys=[
                        Hash(
                            "0x0000000000000000000000000000000000000000000000000000000000000000"  # noqa: E501
                        )
                    ],
                )
            ],
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xC057,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xEAD0C057,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    storage={24743: 48879},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x1A
                        ),
                    )
                    + Op.REVERT(offset=0x0, size=0x40)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001011"): Account(
                    storage={0: 24601},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0111,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001012"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0112,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001013"): Account(
                    storage={0: 24743},
                    code=Op.MSTORE(offset=0x0, value=0xBAD)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xF113,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001014"): Account(
                    code=Op.CALL(
                        gas=0xB65,
                        address=0xF114,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001015"): Account(
                    code=Op.CALL(
                        gas=0x1800,
                        address=0xF115,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001016"): Account(
                    storage={0: 15, 24743: 57005},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0xBEEF, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0xA0, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x23
                        ),
                    )
                    + Op.MSTORE(offset=0x40, value=Op.GAS)
                    + Op.SSTORE(
                        key=Op.ADD(0xF000, Op.SLOAD(key=0x0)), value=0xBEEF
                    )
                    + Op.MSTORE(
                        offset=0x40,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x40), Op.GAS), 0x78
                        ),
                    )
                    + Op.MSTORE(offset=0x60, value=Op.GAS)
                    + Op.POP(Op.SLOAD(key=Op.ADD(0xF010, Op.SLOAD(key=0x0))))
                    + Op.MSTORE(
                        offset=0x60,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x60), Op.GAS), 0x7A
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x100, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x0),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x200, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x20),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x300, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x40),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x400, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x60),
                    )
                    + Op.JUMPI(
                        pc=0x9B, condition=Op.GT(Op.SLOAD(key=0x0), 0x0)
                    )
                    + Op.PUSH1[0x0]
                    + Op.JUMP(pc=0xB4)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=Op.SUB(Op.SLOAD(key=0x0), 0x1))
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0x1016,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.JUMPDEST
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001020"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x33, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x39, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001021"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x36, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x3C, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001022"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001023"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001024"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001025"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001026"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xF126,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0xF126,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x10
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f113"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD60A7)
                    + Op.MSTORE(offset=0x0, value=0x600D)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000f114"): Account(
                    storage={0: 2989},
                    code=Op.SSTORE(key=0x0, value=0x600D) + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f115"): Account(
                    storage={0: 2989, 24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.SLOAD(key=0x60A7))
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f126"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x60A7)
                    + Op.MSTORE(
                        offset=0x0, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.JUMPI(
                        pc=0x24, condition=Op.EQ(Op.SLOAD(key=0x1), 0x0)
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.JUMP(pc=0x2B)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0111"): Account(
                    storage={0: 57005},
                    code=Op.SSTORE(key=0x0, value=0xDEAD)
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP,
                ),
                Address("0x00000000000000000000000000000000dead0112"): Account(
                    storage={0: 0xDEAD0060A7},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP,
                ),
                Address("0x00000000000000000000000000000000ead0c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x13
                        ),
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP,
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.ADD(
                                0x1000, Op.CALLDATALOAD(offset=0x4)
                            ),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x40,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x20))
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000011",  # noqa: E501
            [
                AccessList(
                    address=Address(
                        "0x00000000000000000000000000000000dead0111"
                    ),
                    storage_keys=[
                        Hash(
                            "0x0000000000000000000000000000000000000000000000000000000000000000"  # noqa: E501
                        )
                    ],
                )
            ],
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xC057,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xEAD0C057,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    storage={24743: 48879},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x1A
                        ),
                    )
                    + Op.REVERT(offset=0x0, size=0x40)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001011"): Account(
                    storage={0: 20001},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0111,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001012"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0112,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001013"): Account(
                    storage={0: 24743},
                    code=Op.MSTORE(offset=0x0, value=0xBAD)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xF113,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001014"): Account(
                    code=Op.CALL(
                        gas=0xB65,
                        address=0xF114,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001015"): Account(
                    code=Op.CALL(
                        gas=0x1800,
                        address=0xF115,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001016"): Account(
                    storage={0: 15, 24743: 57005},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0xBEEF, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0xA0, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x23
                        ),
                    )
                    + Op.MSTORE(offset=0x40, value=Op.GAS)
                    + Op.SSTORE(
                        key=Op.ADD(0xF000, Op.SLOAD(key=0x0)), value=0xBEEF
                    )
                    + Op.MSTORE(
                        offset=0x40,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x40), Op.GAS), 0x78
                        ),
                    )
                    + Op.MSTORE(offset=0x60, value=Op.GAS)
                    + Op.POP(Op.SLOAD(key=Op.ADD(0xF010, Op.SLOAD(key=0x0))))
                    + Op.MSTORE(
                        offset=0x60,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x60), Op.GAS), 0x7A
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x100, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x0),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x200, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x20),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x300, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x40),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x400, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x60),
                    )
                    + Op.JUMPI(
                        pc=0x9B, condition=Op.GT(Op.SLOAD(key=0x0), 0x0)
                    )
                    + Op.PUSH1[0x0]
                    + Op.JUMP(pc=0xB4)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=Op.SUB(Op.SLOAD(key=0x0), 0x1))
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0x1016,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.JUMPDEST
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001020"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x33, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x39, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001021"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x36, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x3C, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001022"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001023"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001024"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001025"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001026"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xF126,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0xF126,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x10
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f113"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD60A7)
                    + Op.MSTORE(offset=0x0, value=0x600D)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000f114"): Account(
                    storage={0: 2989},
                    code=Op.SSTORE(key=0x0, value=0x600D) + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f115"): Account(
                    storage={0: 2989, 24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.SLOAD(key=0x60A7))
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f126"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x60A7)
                    + Op.MSTORE(
                        offset=0x0, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.JUMPI(
                        pc=0x24, condition=Op.EQ(Op.SLOAD(key=0x1), 0x0)
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.JUMP(pc=0x2B)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0111"): Account(
                    storage={0: 57005},
                    code=Op.SSTORE(key=0x0, value=0xDEAD)
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP,
                ),
                Address("0x00000000000000000000000000000000dead0112"): Account(
                    storage={0: 0xDEAD0060A7},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP,
                ),
                Address("0x00000000000000000000000000000000ead0c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x13
                        ),
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP,
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.ADD(
                                0x1000, Op.CALLDATALOAD(offset=0x4)
                            ),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x40,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x20))
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000002",  # noqa: E501
            [
                AccessList(
                    address=Address(
                        "0x000000000000000000000000000000000000c057"
                    ),
                    storage_keys=[
                        Hash(
                            "0x0000000000000000000000000000000000000000000000000000000000000000"  # noqa: E501
                        ),
                        Hash(
                            "0x00000000000000000000000000000000000000000000000000000000000060a7"  # noqa: E501
                        ),
                    ],
                )
            ],
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xC057,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    storage={0: 2, 1: 22103, 2: 2107},
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xEAD0C057,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    storage={24743: 48879},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x1A
                        ),
                    )
                    + Op.REVERT(offset=0x0, size=0x40)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001011"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0111,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001012"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0112,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001013"): Account(
                    storage={0: 24743},
                    code=Op.MSTORE(offset=0x0, value=0xBAD)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xF113,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001014"): Account(
                    code=Op.CALL(
                        gas=0xB65,
                        address=0xF114,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001015"): Account(
                    code=Op.CALL(
                        gas=0x1800,
                        address=0xF115,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001016"): Account(
                    storage={0: 15, 24743: 57005},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0xBEEF, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0xA0, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x23
                        ),
                    )
                    + Op.MSTORE(offset=0x40, value=Op.GAS)
                    + Op.SSTORE(
                        key=Op.ADD(0xF000, Op.SLOAD(key=0x0)), value=0xBEEF
                    )
                    + Op.MSTORE(
                        offset=0x40,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x40), Op.GAS), 0x78
                        ),
                    )
                    + Op.MSTORE(offset=0x60, value=Op.GAS)
                    + Op.POP(Op.SLOAD(key=Op.ADD(0xF010, Op.SLOAD(key=0x0))))
                    + Op.MSTORE(
                        offset=0x60,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x60), Op.GAS), 0x7A
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x100, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x0),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x200, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x20),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x300, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x40),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x400, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x60),
                    )
                    + Op.JUMPI(
                        pc=0x9B, condition=Op.GT(Op.SLOAD(key=0x0), 0x0)
                    )
                    + Op.PUSH1[0x0]
                    + Op.JUMP(pc=0xB4)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=Op.SUB(Op.SLOAD(key=0x0), 0x1))
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0x1016,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.JUMPDEST
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001020"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x33, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x39, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001021"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x36, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x3C, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001022"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001023"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001024"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001025"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001026"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xF126,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0xF126,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x10
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f113"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD60A7)
                    + Op.MSTORE(offset=0x0, value=0x600D)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000f114"): Account(
                    storage={0: 2989},
                    code=Op.SSTORE(key=0x0, value=0x600D) + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f115"): Account(
                    storage={0: 2989, 24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.SLOAD(key=0x60A7))
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f126"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x60A7)
                    + Op.MSTORE(
                        offset=0x0, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.JUMPI(
                        pc=0x24, condition=Op.EQ(Op.SLOAD(key=0x1), 0x0)
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.JUMP(pc=0x2B)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0111"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD)
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0112"): Account(
                    storage={0: 0xDEAD0060A7},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP,
                ),
                Address("0x00000000000000000000000000000000ead0c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x13
                        ),
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP,
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.ADD(
                                0x1000, Op.CALLDATALOAD(offset=0x4)
                            ),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x40,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x20))
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000002",  # noqa: E501
            [
                AccessList(
                    address=Address(
                        "0x0000000000000000000000000000000000001002"
                    ),
                    storage_keys=[
                        Hash(
                            "0x0000000000000000000000000000000000000000000000000000000000000000"  # noqa: E501
                        ),
                        Hash(
                            "0x00000000000000000000000000000000000000000000000000000000000060a7"  # noqa: E501
                        ),
                    ],
                )
            ],
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xC057,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    storage={0: 2, 1: 20003, 2: 107},
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xEAD0C057,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    storage={24743: 48879},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x1A
                        ),
                    )
                    + Op.REVERT(offset=0x0, size=0x40)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001011"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0111,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001012"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0112,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001013"): Account(
                    storage={0: 24743},
                    code=Op.MSTORE(offset=0x0, value=0xBAD)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xF113,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001014"): Account(
                    code=Op.CALL(
                        gas=0xB65,
                        address=0xF114,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001015"): Account(
                    code=Op.CALL(
                        gas=0x1800,
                        address=0xF115,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001016"): Account(
                    storage={0: 15, 24743: 57005},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0xBEEF, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0xA0, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x23
                        ),
                    )
                    + Op.MSTORE(offset=0x40, value=Op.GAS)
                    + Op.SSTORE(
                        key=Op.ADD(0xF000, Op.SLOAD(key=0x0)), value=0xBEEF
                    )
                    + Op.MSTORE(
                        offset=0x40,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x40), Op.GAS), 0x78
                        ),
                    )
                    + Op.MSTORE(offset=0x60, value=Op.GAS)
                    + Op.POP(Op.SLOAD(key=Op.ADD(0xF010, Op.SLOAD(key=0x0))))
                    + Op.MSTORE(
                        offset=0x60,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x60), Op.GAS), 0x7A
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x100, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x0),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x200, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x20),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x300, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x40),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x400, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x60),
                    )
                    + Op.JUMPI(
                        pc=0x9B, condition=Op.GT(Op.SLOAD(key=0x0), 0x0)
                    )
                    + Op.PUSH1[0x0]
                    + Op.JUMP(pc=0xB4)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=Op.SUB(Op.SLOAD(key=0x0), 0x1))
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0x1016,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.JUMPDEST
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001020"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x33, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x39, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001021"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x36, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x3C, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001022"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001023"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001024"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001025"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001026"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xF126,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0xF126,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x10
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f113"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD60A7)
                    + Op.MSTORE(offset=0x0, value=0x600D)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000f114"): Account(
                    storage={0: 2989},
                    code=Op.SSTORE(key=0x0, value=0x600D) + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f115"): Account(
                    storage={0: 2989, 24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.SLOAD(key=0x60A7))
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f126"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x60A7)
                    + Op.MSTORE(
                        offset=0x0, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.JUMPI(
                        pc=0x24, condition=Op.EQ(Op.SLOAD(key=0x1), 0x0)
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.JUMP(pc=0x2B)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0111"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD)
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0112"): Account(
                    storage={0: 0xDEAD0060A7},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP,
                ),
                Address("0x00000000000000000000000000000000ead0c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x13
                        ),
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP,
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.ADD(
                                0x1000, Op.CALLDATALOAD(offset=0x4)
                            ),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x40,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x20))
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000025",  # noqa: E501
            [
                AccessList(
                    address=Address(
                        "0x58fd03a2d731b2fb751e4a0f593d373ee77d39e6"
                    ),
                    storage_keys=[
                        Hash(
                            "0x000000000000000000000000000000000000000000000000000000000000ffff"  # noqa: E501
                        )
                    ],
                )
            ],
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xC057,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xEAD0C057,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    storage={24743: 48879},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x1A
                        ),
                    )
                    + Op.REVERT(offset=0x0, size=0x40)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001011"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0111,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001012"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0112,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001013"): Account(
                    storage={0: 24743},
                    code=Op.MSTORE(offset=0x0, value=0xBAD)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xF113,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001014"): Account(
                    code=Op.CALL(
                        gas=0xB65,
                        address=0xF114,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001015"): Account(
                    code=Op.CALL(
                        gas=0x1800,
                        address=0xF115,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001016"): Account(
                    storage={0: 15, 24743: 57005},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0xBEEF, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0xA0, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x23
                        ),
                    )
                    + Op.MSTORE(offset=0x40, value=Op.GAS)
                    + Op.SSTORE(
                        key=Op.ADD(0xF000, Op.SLOAD(key=0x0)), value=0xBEEF
                    )
                    + Op.MSTORE(
                        offset=0x40,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x40), Op.GAS), 0x78
                        ),
                    )
                    + Op.MSTORE(offset=0x60, value=Op.GAS)
                    + Op.POP(Op.SLOAD(key=Op.ADD(0xF010, Op.SLOAD(key=0x0))))
                    + Op.MSTORE(
                        offset=0x60,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x60), Op.GAS), 0x7A
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x100, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x0),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x200, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x20),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x300, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x40),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x400, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x60),
                    )
                    + Op.JUMPI(
                        pc=0x9B, condition=Op.GT(Op.SLOAD(key=0x0), 0x0)
                    )
                    + Op.PUSH1[0x0]
                    + Op.JUMP(pc=0xB4)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=Op.SUB(Op.SLOAD(key=0x0), 0x1))
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0x1016,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.JUMPDEST
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001020"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x33, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x39, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001021"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x36, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x3C, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001022"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001023"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001024"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001025"): Account(
                    storage={1: 0x83FBDAE70258AC0FA837B701CC63CEDF48D4B6BF},
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001026"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xF126,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0xF126,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x10
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f113"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD60A7)
                    + Op.MSTORE(offset=0x0, value=0x600D)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000f114"): Account(
                    storage={0: 2989},
                    code=Op.SSTORE(key=0x0, value=0x600D) + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f115"): Account(
                    storage={0: 2989, 24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.SLOAD(key=0x60A7))
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f126"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x60A7)
                    + Op.MSTORE(
                        offset=0x0, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.JUMPI(
                        pc=0x24, condition=Op.EQ(Op.SLOAD(key=0x1), 0x0)
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.JUMP(pc=0x2B)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0111"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD)
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0112"): Account(
                    storage={0: 0xDEAD0060A7},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP,
                ),
                Address("0x00000000000000000000000000000000ead0c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x13
                        ),
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP,
                ),
                Address("0x83fbdae70258ac0fa837b701cc63cedf48d4b6bf"): Account(
                    storage={0: 65535, 1: 22117, 2: 117},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP,
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.ADD(
                                0x1000, Op.CALLDATALOAD(offset=0x4)
                            ),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x40,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x20))
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000025",  # noqa: E501
            [
                AccessList(
                    address=Address(
                        "0x83fbdae70258ac0fa837b701cc63cedf48d4b6bf"
                    ),
                    storage_keys=[
                        Hash(
                            "0x0000000000000000000000000000000000000000000000000000000000000000"  # noqa: E501
                        )
                    ],
                )
            ],
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xC057,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xEAD0C057,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    storage={24743: 48879},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x1A
                        ),
                    )
                    + Op.REVERT(offset=0x0, size=0x40)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001011"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0111,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001012"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0112,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001013"): Account(
                    storage={0: 24743},
                    code=Op.MSTORE(offset=0x0, value=0xBAD)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xF113,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001014"): Account(
                    code=Op.CALL(
                        gas=0xB65,
                        address=0xF114,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001015"): Account(
                    code=Op.CALL(
                        gas=0x1800,
                        address=0xF115,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001016"): Account(
                    storage={0: 15, 24743: 57005},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0xBEEF, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0xA0, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x23
                        ),
                    )
                    + Op.MSTORE(offset=0x40, value=Op.GAS)
                    + Op.SSTORE(
                        key=Op.ADD(0xF000, Op.SLOAD(key=0x0)), value=0xBEEF
                    )
                    + Op.MSTORE(
                        offset=0x40,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x40), Op.GAS), 0x78
                        ),
                    )
                    + Op.MSTORE(offset=0x60, value=Op.GAS)
                    + Op.POP(Op.SLOAD(key=Op.ADD(0xF010, Op.SLOAD(key=0x0))))
                    + Op.MSTORE(
                        offset=0x60,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x60), Op.GAS), 0x7A
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x100, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x0),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x200, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x20),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x300, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x40),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x400, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x60),
                    )
                    + Op.JUMPI(
                        pc=0x9B, condition=Op.GT(Op.SLOAD(key=0x0), 0x0)
                    )
                    + Op.PUSH1[0x0]
                    + Op.JUMP(pc=0xB4)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=Op.SUB(Op.SLOAD(key=0x0), 0x1))
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0x1016,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.JUMPDEST
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001020"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x33, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x39, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001021"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x36, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x3C, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001022"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001023"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001024"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001025"): Account(
                    storage={1: 0x83FBDAE70258AC0FA837B701CC63CEDF48D4B6BF},
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001026"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xF126,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0xF126,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x10
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f113"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD60A7)
                    + Op.MSTORE(offset=0x0, value=0x600D)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000f114"): Account(
                    storage={0: 2989},
                    code=Op.SSTORE(key=0x0, value=0x600D) + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f115"): Account(
                    storage={0: 2989, 24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.SLOAD(key=0x60A7))
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f126"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x60A7)
                    + Op.MSTORE(
                        offset=0x0, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.JUMPI(
                        pc=0x24, condition=Op.EQ(Op.SLOAD(key=0x1), 0x0)
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.JUMP(pc=0x2B)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0111"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD)
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0112"): Account(
                    storage={0: 0xDEAD0060A7},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP,
                ),
                Address("0x00000000000000000000000000000000ead0c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x13
                        ),
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP,
                ),
                Address("0x83fbdae70258ac0fa837b701cc63cedf48d4b6bf"): Account(
                    storage={0: 65535, 1: 20017, 2: 117},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP,
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.ADD(
                                0x1000, Op.CALLDATALOAD(offset=0x4)
                            ),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x40,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x20))
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000021",  # noqa: E501
            [
                AccessList(
                    address=Address(
                        "0xf342e57f24e0333f3af34af08fdbbe9c72cbd37c"
                    ),
                    storage_keys=[
                        Hash(
                            "0x0000000000000000000000000000000000000000000000000000000000000000"  # noqa: E501
                        )
                    ],
                )
            ],
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xC057,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xEAD0C057,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    storage={24743: 48879},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x1A
                        ),
                    )
                    + Op.REVERT(offset=0x0, size=0x40)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001011"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0111,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001012"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0112,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001013"): Account(
                    storage={0: 24743},
                    code=Op.MSTORE(offset=0x0, value=0xBAD)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xF113,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001014"): Account(
                    code=Op.CALL(
                        gas=0xB65,
                        address=0xF114,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001015"): Account(
                    code=Op.CALL(
                        gas=0x1800,
                        address=0xF115,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001016"): Account(
                    storage={0: 15, 24743: 57005},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0xBEEF, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0xA0, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x23
                        ),
                    )
                    + Op.MSTORE(offset=0x40, value=Op.GAS)
                    + Op.SSTORE(
                        key=Op.ADD(0xF000, Op.SLOAD(key=0x0)), value=0xBEEF
                    )
                    + Op.MSTORE(
                        offset=0x40,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x40), Op.GAS), 0x78
                        ),
                    )
                    + Op.MSTORE(offset=0x60, value=Op.GAS)
                    + Op.POP(Op.SLOAD(key=Op.ADD(0xF010, Op.SLOAD(key=0x0))))
                    + Op.MSTORE(
                        offset=0x60,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x60), Op.GAS), 0x7A
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x100, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x0),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x200, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x20),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x300, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x40),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x400, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x60),
                    )
                    + Op.JUMPI(
                        pc=0x9B, condition=Op.GT(Op.SLOAD(key=0x0), 0x0)
                    )
                    + Op.PUSH1[0x0]
                    + Op.JUMP(pc=0xB4)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=Op.SUB(Op.SLOAD(key=0x0), 0x1))
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0x1016,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.JUMPDEST
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001020"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x33, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x39, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001021"): Account(
                    storage={1: 0xD82F21135ED7D7D833A9F2A0F1CF6C3DA214B8E3},
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x36, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x3C, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001022"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001023"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001024"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001025"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001026"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xF126,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0xF126,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x10
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f113"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD60A7)
                    + Op.MSTORE(offset=0x0, value=0x600D)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000f114"): Account(
                    storage={0: 2989},
                    code=Op.SSTORE(key=0x0, value=0x600D) + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f115"): Account(
                    storage={0: 2989, 24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.SLOAD(key=0x60A7))
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f126"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x60A7)
                    + Op.MSTORE(
                        offset=0x0, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.JUMPI(
                        pc=0x24, condition=Op.EQ(Op.SLOAD(key=0x1), 0x0)
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.JUMP(pc=0x2B)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0111"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD)
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0112"): Account(
                    storage={0: 0xDEAD0060A7},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP,
                ),
                Address("0x00000000000000000000000000000000ead0c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x13
                        ),
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP,
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.ADD(
                                0x1000, Op.CALLDATALOAD(offset=0x4)
                            ),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x40,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x20))
                    + Op.STOP
                ),
                Address("0xd82f21135ed7d7d833a9f2a0f1cf6c3da214b8e3"): Account(
                    storage={0: 65535, 1: 22117},
                    code=Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP,
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000021",  # noqa: E501
            [
                AccessList(
                    address=Address(
                        "0xd82f21135ed7d7d833a9f2a0f1cf6c3da214b8e3"
                    ),
                    storage_keys=[
                        Hash(
                            "0x0000000000000000000000000000000000000000000000000000000000000000"  # noqa: E501
                        )
                    ],
                )
            ],
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xC057,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xEAD0C057,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    storage={24743: 48879},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x1A
                        ),
                    )
                    + Op.REVERT(offset=0x0, size=0x40)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001011"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0111,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001012"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0112,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001013"): Account(
                    storage={0: 24743},
                    code=Op.MSTORE(offset=0x0, value=0xBAD)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xF113,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001014"): Account(
                    code=Op.CALL(
                        gas=0xB65,
                        address=0xF114,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001015"): Account(
                    code=Op.CALL(
                        gas=0x1800,
                        address=0xF115,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001016"): Account(
                    storage={0: 15, 24743: 57005},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0xBEEF, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0xA0, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x23
                        ),
                    )
                    + Op.MSTORE(offset=0x40, value=Op.GAS)
                    + Op.SSTORE(
                        key=Op.ADD(0xF000, Op.SLOAD(key=0x0)), value=0xBEEF
                    )
                    + Op.MSTORE(
                        offset=0x40,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x40), Op.GAS), 0x78
                        ),
                    )
                    + Op.MSTORE(offset=0x60, value=Op.GAS)
                    + Op.POP(Op.SLOAD(key=Op.ADD(0xF010, Op.SLOAD(key=0x0))))
                    + Op.MSTORE(
                        offset=0x60,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x60), Op.GAS), 0x7A
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x100, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x0),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x200, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x20),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x300, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x40),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x400, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x60),
                    )
                    + Op.JUMPI(
                        pc=0x9B, condition=Op.GT(Op.SLOAD(key=0x0), 0x0)
                    )
                    + Op.PUSH1[0x0]
                    + Op.JUMP(pc=0xB4)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=Op.SUB(Op.SLOAD(key=0x0), 0x1))
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0x1016,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.JUMPDEST
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001020"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x33, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x39, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001021"): Account(
                    storage={1: 0xD82F21135ED7D7D833A9F2A0F1CF6C3DA214B8E3},
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x36, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x3C, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001022"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001023"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001024"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001025"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001026"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xF126,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0xF126,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x10
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f113"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD60A7)
                    + Op.MSTORE(offset=0x0, value=0x600D)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000f114"): Account(
                    storage={0: 2989},
                    code=Op.SSTORE(key=0x0, value=0x600D) + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f115"): Account(
                    storage={0: 2989, 24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.SLOAD(key=0x60A7))
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f126"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x60A7)
                    + Op.MSTORE(
                        offset=0x0, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.JUMPI(
                        pc=0x24, condition=Op.EQ(Op.SLOAD(key=0x1), 0x0)
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.JUMP(pc=0x2B)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0111"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD)
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0112"): Account(
                    storage={0: 0xDEAD0060A7},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP,
                ),
                Address("0x00000000000000000000000000000000ead0c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x13
                        ),
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP,
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.ADD(
                                0x1000, Op.CALLDATALOAD(offset=0x4)
                            ),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x40,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x20))
                    + Op.STOP
                ),
                Address("0xd82f21135ed7d7d833a9f2a0f1cf6c3da214b8e3"): Account(
                    storage={0: 65535, 1: 20017},
                    code=Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP,
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000024",  # noqa: E501
            [
                AccessList(
                    address=Address(
                        "0x58fd03a2d731b2fb751e4a0f593d373ee77d39e6"
                    ),
                    storage_keys=[
                        Hash(
                            "0x000000000000000000000000000000000000000000000000000000000000ffff"  # noqa: E501
                        )
                    ],
                )
            ],
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xC057,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xEAD0C057,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    storage={24743: 48879},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x1A
                        ),
                    )
                    + Op.REVERT(offset=0x0, size=0x40)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001011"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0111,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001012"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0112,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001013"): Account(
                    storage={0: 24743},
                    code=Op.MSTORE(offset=0x0, value=0xBAD)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xF113,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001014"): Account(
                    code=Op.CALL(
                        gas=0xB65,
                        address=0xF114,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001015"): Account(
                    code=Op.CALL(
                        gas=0x1800,
                        address=0xF115,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001016"): Account(
                    storage={0: 15, 24743: 57005},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0xBEEF, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0xA0, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x23
                        ),
                    )
                    + Op.MSTORE(offset=0x40, value=Op.GAS)
                    + Op.SSTORE(
                        key=Op.ADD(0xF000, Op.SLOAD(key=0x0)), value=0xBEEF
                    )
                    + Op.MSTORE(
                        offset=0x40,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x40), Op.GAS), 0x78
                        ),
                    )
                    + Op.MSTORE(offset=0x60, value=Op.GAS)
                    + Op.POP(Op.SLOAD(key=Op.ADD(0xF010, Op.SLOAD(key=0x0))))
                    + Op.MSTORE(
                        offset=0x60,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x60), Op.GAS), 0x7A
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x100, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x0),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x200, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x20),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x300, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x40),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x400, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x60),
                    )
                    + Op.JUMPI(
                        pc=0x9B, condition=Op.GT(Op.SLOAD(key=0x0), 0x0)
                    )
                    + Op.PUSH1[0x0]
                    + Op.JUMP(pc=0xB4)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=Op.SUB(Op.SLOAD(key=0x0), 0x1))
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0x1016,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.JUMPDEST
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001020"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x33, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x39, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001021"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x36, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x3C, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001022"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001023"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001024"): Account(
                    storage={1: 0xB76AB2D646C4DF221EDD345957D0A396A2AB1B6D},
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001025"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001026"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xF126,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0xF126,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x10
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f113"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD60A7)
                    + Op.MSTORE(offset=0x0, value=0x600D)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000f114"): Account(
                    storage={0: 2989},
                    code=Op.SSTORE(key=0x0, value=0x600D) + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f115"): Account(
                    storage={0: 2989, 24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.SLOAD(key=0x60A7))
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f126"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x60A7)
                    + Op.MSTORE(
                        offset=0x0, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.JUMPI(
                        pc=0x24, condition=Op.EQ(Op.SLOAD(key=0x1), 0x0)
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.JUMP(pc=0x2B)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0111"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD)
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0112"): Account(
                    storage={0: 0xDEAD0060A7},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP,
                ),
                Address("0x00000000000000000000000000000000ead0c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x13
                        ),
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP,
                ),
                Address("0xb76ab2d646c4df221edd345957d0a396a2ab1b6d"): Account(
                    storage={0: 65535, 1: 22117, 2: 117},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP,
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.ADD(
                                0x1000, Op.CALLDATALOAD(offset=0x4)
                            ),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x40,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x20))
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000024",  # noqa: E501
            [
                AccessList(
                    address=Address(
                        "0xb76ab2d646c4df221edd345957d0a396a2ab1b6d"
                    ),
                    storage_keys=[
                        Hash(
                            "0x0000000000000000000000000000000000000000000000000000000000000000"  # noqa: E501
                        )
                    ],
                )
            ],
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xC057,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xEAD0C057,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    storage={24743: 48879},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x1A
                        ),
                    )
                    + Op.REVERT(offset=0x0, size=0x40)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001011"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0111,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001012"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0112,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001013"): Account(
                    storage={0: 24743},
                    code=Op.MSTORE(offset=0x0, value=0xBAD)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xF113,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001014"): Account(
                    code=Op.CALL(
                        gas=0xB65,
                        address=0xF114,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001015"): Account(
                    code=Op.CALL(
                        gas=0x1800,
                        address=0xF115,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001016"): Account(
                    storage={0: 15, 24743: 57005},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0xBEEF, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0xA0, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x23
                        ),
                    )
                    + Op.MSTORE(offset=0x40, value=Op.GAS)
                    + Op.SSTORE(
                        key=Op.ADD(0xF000, Op.SLOAD(key=0x0)), value=0xBEEF
                    )
                    + Op.MSTORE(
                        offset=0x40,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x40), Op.GAS), 0x78
                        ),
                    )
                    + Op.MSTORE(offset=0x60, value=Op.GAS)
                    + Op.POP(Op.SLOAD(key=Op.ADD(0xF010, Op.SLOAD(key=0x0))))
                    + Op.MSTORE(
                        offset=0x60,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x60), Op.GAS), 0x7A
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x100, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x0),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x200, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x20),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x300, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x40),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x400, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x60),
                    )
                    + Op.JUMPI(
                        pc=0x9B, condition=Op.GT(Op.SLOAD(key=0x0), 0x0)
                    )
                    + Op.PUSH1[0x0]
                    + Op.JUMP(pc=0xB4)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=Op.SUB(Op.SLOAD(key=0x0), 0x1))
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0x1016,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.JUMPDEST
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001020"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x33, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x39, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001021"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x36, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x3C, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001022"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001023"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001024"): Account(
                    storage={1: 0xB76AB2D646C4DF221EDD345957D0A396A2AB1B6D},
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001025"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001026"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xF126,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0xF126,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x10
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f113"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD60A7)
                    + Op.MSTORE(offset=0x0, value=0x600D)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000f114"): Account(
                    storage={0: 2989},
                    code=Op.SSTORE(key=0x0, value=0x600D) + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f115"): Account(
                    storage={0: 2989, 24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.SLOAD(key=0x60A7))
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f126"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x60A7)
                    + Op.MSTORE(
                        offset=0x0, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.JUMPI(
                        pc=0x24, condition=Op.EQ(Op.SLOAD(key=0x1), 0x0)
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.JUMP(pc=0x2B)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0111"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD)
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0112"): Account(
                    storage={0: 0xDEAD0060A7},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP,
                ),
                Address("0x00000000000000000000000000000000ead0c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x13
                        ),
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP,
                ),
                Address("0xb76ab2d646c4df221edd345957d0a396a2ab1b6d"): Account(
                    storage={0: 65535, 1: 20017, 2: 117},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP,
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.ADD(
                                0x1000, Op.CALLDATALOAD(offset=0x4)
                            ),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x40,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x20))
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000020",  # noqa: E501
            [
                AccessList(
                    address=Address(
                        "0xf342e57f24e0333f3af34af08fdbbe9c72cbd37c"
                    ),
                    storage_keys=[
                        Hash(
                            "0x0000000000000000000000000000000000000000000000000000000000000001"  # noqa: E501
                        )
                    ],
                )
            ],
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xC057,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xEAD0C057,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    storage={24743: 48879},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x1A
                        ),
                    )
                    + Op.REVERT(offset=0x0, size=0x40)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001011"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0111,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001012"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0112,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001013"): Account(
                    storage={0: 24743},
                    code=Op.MSTORE(offset=0x0, value=0xBAD)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xF113,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001014"): Account(
                    code=Op.CALL(
                        gas=0xB65,
                        address=0xF114,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001015"): Account(
                    code=Op.CALL(
                        gas=0x1800,
                        address=0xF115,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001016"): Account(
                    storage={0: 15, 24743: 57005},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0xBEEF, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0xA0, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x23
                        ),
                    )
                    + Op.MSTORE(offset=0x40, value=Op.GAS)
                    + Op.SSTORE(
                        key=Op.ADD(0xF000, Op.SLOAD(key=0x0)), value=0xBEEF
                    )
                    + Op.MSTORE(
                        offset=0x40,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x40), Op.GAS), 0x78
                        ),
                    )
                    + Op.MSTORE(offset=0x60, value=Op.GAS)
                    + Op.POP(Op.SLOAD(key=Op.ADD(0xF010, Op.SLOAD(key=0x0))))
                    + Op.MSTORE(
                        offset=0x60,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x60), Op.GAS), 0x7A
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x100, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x0),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x200, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x20),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x300, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x40),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x400, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x60),
                    )
                    + Op.JUMPI(
                        pc=0x9B, condition=Op.GT(Op.SLOAD(key=0x0), 0x0)
                    )
                    + Op.PUSH1[0x0]
                    + Op.JUMP(pc=0xB4)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=Op.SUB(Op.SLOAD(key=0x0), 0x1))
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0x1016,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.JUMPDEST
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001020"): Account(
                    storage={1: 0xF342E57F24E0333F3AF34AF08FDBBE9C72CBD37C},
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x33, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x39, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001021"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x36, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x3C, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001022"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001023"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001024"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001025"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001026"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xF126,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0xF126,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x10
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f113"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD60A7)
                    + Op.MSTORE(offset=0x0, value=0x600D)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000f114"): Account(
                    storage={0: 2989},
                    code=Op.SSTORE(key=0x0, value=0x600D) + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f115"): Account(
                    storage={0: 2989, 24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.SLOAD(key=0x60A7))
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f126"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x60A7)
                    + Op.MSTORE(
                        offset=0x0, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.JUMPI(
                        pc=0x24, condition=Op.EQ(Op.SLOAD(key=0x1), 0x0)
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.JUMP(pc=0x2B)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0111"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD)
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0112"): Account(
                    storage={0: 0xDEAD0060A7},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP,
                ),
                Address("0x00000000000000000000000000000000ead0c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x13
                        ),
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP,
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.ADD(
                                0x1000, Op.CALLDATALOAD(offset=0x4)
                            ),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x40,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x20))
                    + Op.STOP
                ),
                Address("0xf342e57f24e0333f3af34af08fdbbe9c72cbd37c"): Account(
                    storage={0: 65535, 1: 22117},
                    code=Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP,
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000020",  # noqa: E501
            [
                AccessList(
                    address=Address(
                        "0xf342e57f24e0333f3af34af08fdbbe9c72cbd37c"
                    ),
                    storage_keys=[
                        Hash(
                            "0x0000000000000000000000000000000000000000000000000000000000000000"  # noqa: E501
                        )
                    ],
                )
            ],
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xC057,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xEAD0C057,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    storage={24743: 48879},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x1A
                        ),
                    )
                    + Op.REVERT(offset=0x0, size=0x40)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001011"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0111,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001012"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0112,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001013"): Account(
                    storage={0: 24743},
                    code=Op.MSTORE(offset=0x0, value=0xBAD)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xF113,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001014"): Account(
                    code=Op.CALL(
                        gas=0xB65,
                        address=0xF114,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001015"): Account(
                    code=Op.CALL(
                        gas=0x1800,
                        address=0xF115,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001016"): Account(
                    storage={0: 15, 24743: 57005},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0xBEEF, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0xA0, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x23
                        ),
                    )
                    + Op.MSTORE(offset=0x40, value=Op.GAS)
                    + Op.SSTORE(
                        key=Op.ADD(0xF000, Op.SLOAD(key=0x0)), value=0xBEEF
                    )
                    + Op.MSTORE(
                        offset=0x40,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x40), Op.GAS), 0x78
                        ),
                    )
                    + Op.MSTORE(offset=0x60, value=Op.GAS)
                    + Op.POP(Op.SLOAD(key=Op.ADD(0xF010, Op.SLOAD(key=0x0))))
                    + Op.MSTORE(
                        offset=0x60,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x60), Op.GAS), 0x7A
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x100, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x0),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x200, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x20),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x300, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x40),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x400, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x60),
                    )
                    + Op.JUMPI(
                        pc=0x9B, condition=Op.GT(Op.SLOAD(key=0x0), 0x0)
                    )
                    + Op.PUSH1[0x0]
                    + Op.JUMP(pc=0xB4)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=Op.SUB(Op.SLOAD(key=0x0), 0x1))
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0x1016,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.JUMPDEST
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001020"): Account(
                    storage={1: 0xF342E57F24E0333F3AF34AF08FDBBE9C72CBD37C},
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x33, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x39, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001021"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x36, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x3C, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001022"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001023"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001024"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001025"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001026"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xF126,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0xF126,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x10
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f113"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD60A7)
                    + Op.MSTORE(offset=0x0, value=0x600D)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000f114"): Account(
                    storage={0: 2989},
                    code=Op.SSTORE(key=0x0, value=0x600D) + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f115"): Account(
                    storage={0: 2989, 24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.SLOAD(key=0x60A7))
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f126"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x60A7)
                    + Op.MSTORE(
                        offset=0x0, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.JUMPI(
                        pc=0x24, condition=Op.EQ(Op.SLOAD(key=0x1), 0x0)
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.JUMP(pc=0x2B)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0111"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD)
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0112"): Account(
                    storage={0: 0xDEAD0060A7},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP,
                ),
                Address("0x00000000000000000000000000000000ead0c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x13
                        ),
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP,
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.ADD(
                                0x1000, Op.CALLDATALOAD(offset=0x4)
                            ),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x40,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x20))
                    + Op.STOP
                ),
                Address("0xf342e57f24e0333f3af34af08fdbbe9c72cbd37c"): Account(
                    storage={0: 65535, 1: 20017},
                    code=Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP
                    + Op.STOP,
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000000",  # noqa: E501
            [
                AccessList(
                    address=Address(
                        "0x000000000000000000000000000000000000c057"
                    ),
                    storage_keys=[
                        Hash(
                            "0x0000000000000000000000000000000000000000000000000000000000000000"  # noqa: E501
                        ),
                        Hash(
                            "0x00000000000000000000000000000000000000000000000000000000000060a7"  # noqa: E501
                        ),
                    ],
                )
            ],
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    storage={0: 2, 1: 22103, 2: 2107},
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xC057,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xEAD0C057,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    storage={24743: 48879},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x1A
                        ),
                    )
                    + Op.REVERT(offset=0x0, size=0x40)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001011"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0111,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001012"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0112,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001013"): Account(
                    storage={0: 24743},
                    code=Op.MSTORE(offset=0x0, value=0xBAD)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xF113,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001014"): Account(
                    code=Op.CALL(
                        gas=0xB65,
                        address=0xF114,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001015"): Account(
                    code=Op.CALL(
                        gas=0x1800,
                        address=0xF115,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001016"): Account(
                    storage={0: 15, 24743: 57005},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0xBEEF, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0xA0, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x23
                        ),
                    )
                    + Op.MSTORE(offset=0x40, value=Op.GAS)
                    + Op.SSTORE(
                        key=Op.ADD(0xF000, Op.SLOAD(key=0x0)), value=0xBEEF
                    )
                    + Op.MSTORE(
                        offset=0x40,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x40), Op.GAS), 0x78
                        ),
                    )
                    + Op.MSTORE(offset=0x60, value=Op.GAS)
                    + Op.POP(Op.SLOAD(key=Op.ADD(0xF010, Op.SLOAD(key=0x0))))
                    + Op.MSTORE(
                        offset=0x60,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x60), Op.GAS), 0x7A
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x100, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x0),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x200, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x20),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x300, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x40),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x400, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x60),
                    )
                    + Op.JUMPI(
                        pc=0x9B, condition=Op.GT(Op.SLOAD(key=0x0), 0x0)
                    )
                    + Op.PUSH1[0x0]
                    + Op.JUMP(pc=0xB4)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=Op.SUB(Op.SLOAD(key=0x0), 0x1))
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0x1016,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.JUMPDEST
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001020"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x33, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x39, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001021"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x36, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x3C, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001022"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001023"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001024"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001025"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001026"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xF126,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0xF126,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x10
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f113"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD60A7)
                    + Op.MSTORE(offset=0x0, value=0x600D)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000f114"): Account(
                    storage={0: 2989},
                    code=Op.SSTORE(key=0x0, value=0x600D) + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f115"): Account(
                    storage={0: 2989, 24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.SLOAD(key=0x60A7))
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f126"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x60A7)
                    + Op.MSTORE(
                        offset=0x0, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.JUMPI(
                        pc=0x24, condition=Op.EQ(Op.SLOAD(key=0x1), 0x0)
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.JUMP(pc=0x2B)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0111"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD)
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0112"): Account(
                    storage={0: 0xDEAD0060A7},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP,
                ),
                Address("0x00000000000000000000000000000000ead0c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x13
                        ),
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP,
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.ADD(
                                0x1000, Op.CALLDATALOAD(offset=0x4)
                            ),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x40,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x20))
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000000",  # noqa: E501
            [
                AccessList(
                    address=Address(
                        "0x0000000000000000000000000000000000001000"
                    ),
                    storage_keys=[
                        Hash(
                            "0x0000000000000000000000000000000000000000000000000000000000000000"  # noqa: E501
                        ),
                        Hash(
                            "0x00000000000000000000000000000000000000000000000000000000000060a7"  # noqa: E501
                        ),
                    ],
                )
            ],
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    storage={0: 2, 1: 20003, 2: 107},
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xC057,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xEAD0C057,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    storage={24743: 48879},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x1A
                        ),
                    )
                    + Op.REVERT(offset=0x0, size=0x40)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001011"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0111,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001012"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0112,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001013"): Account(
                    storage={0: 24743},
                    code=Op.MSTORE(offset=0x0, value=0xBAD)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xF113,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001014"): Account(
                    code=Op.CALL(
                        gas=0xB65,
                        address=0xF114,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001015"): Account(
                    code=Op.CALL(
                        gas=0x1800,
                        address=0xF115,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001016"): Account(
                    storage={0: 15, 24743: 57005},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0xBEEF, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0xA0, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x23
                        ),
                    )
                    + Op.MSTORE(offset=0x40, value=Op.GAS)
                    + Op.SSTORE(
                        key=Op.ADD(0xF000, Op.SLOAD(key=0x0)), value=0xBEEF
                    )
                    + Op.MSTORE(
                        offset=0x40,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x40), Op.GAS), 0x78
                        ),
                    )
                    + Op.MSTORE(offset=0x60, value=Op.GAS)
                    + Op.POP(Op.SLOAD(key=Op.ADD(0xF010, Op.SLOAD(key=0x0))))
                    + Op.MSTORE(
                        offset=0x60,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x60), Op.GAS), 0x7A
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x100, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x0),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x200, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x20),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x300, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x40),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x400, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x60),
                    )
                    + Op.JUMPI(
                        pc=0x9B, condition=Op.GT(Op.SLOAD(key=0x0), 0x0)
                    )
                    + Op.PUSH1[0x0]
                    + Op.JUMP(pc=0xB4)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=Op.SUB(Op.SLOAD(key=0x0), 0x1))
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0x1016,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.JUMPDEST
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001020"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x33, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x39, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001021"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x36, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x3C, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001022"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001023"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001024"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001025"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001026"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xF126,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0xF126,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x10
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f113"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD60A7)
                    + Op.MSTORE(offset=0x0, value=0x600D)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000f114"): Account(
                    storage={0: 2989},
                    code=Op.SSTORE(key=0x0, value=0x600D) + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f115"): Account(
                    storage={0: 2989, 24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.SLOAD(key=0x60A7))
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f126"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x60A7)
                    + Op.MSTORE(
                        offset=0x0, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.JUMPI(
                        pc=0x24, condition=Op.EQ(Op.SLOAD(key=0x1), 0x0)
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.JUMP(pc=0x2B)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0111"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD)
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0112"): Account(
                    storage={0: 0xDEAD0060A7},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP,
                ),
                Address("0x00000000000000000000000000000000ead0c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x13
                        ),
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP,
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.ADD(
                                0x1000, Op.CALLDATALOAD(offset=0x4)
                            ),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x40,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x20))
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000015",  # noqa: E501
            [
                AccessList(
                    address=Address(
                        "0x0000000000000000000000000000000000001015"
                    ),
                    storage_keys=[
                        Hash(
                            "0x00000000000000000000000000000000000000000000000000000000000060a7"  # noqa: E501
                        )
                    ],
                )
            ],
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xC057,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xEAD0C057,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    storage={24743: 48879},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x1A
                        ),
                    )
                    + Op.REVERT(offset=0x0, size=0x40)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001011"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0111,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001012"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0112,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001013"): Account(
                    storage={0: 24743},
                    code=Op.MSTORE(offset=0x0, value=0xBAD)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xF113,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001014"): Account(
                    code=Op.CALL(
                        gas=0xB65,
                        address=0xF114,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001015"): Account(
                    code=Op.CALL(
                        gas=0x1800,
                        address=0xF115,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001016"): Account(
                    storage={0: 15, 24743: 57005},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0xBEEF, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0xA0, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x23
                        ),
                    )
                    + Op.MSTORE(offset=0x40, value=Op.GAS)
                    + Op.SSTORE(
                        key=Op.ADD(0xF000, Op.SLOAD(key=0x0)), value=0xBEEF
                    )
                    + Op.MSTORE(
                        offset=0x40,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x40), Op.GAS), 0x78
                        ),
                    )
                    + Op.MSTORE(offset=0x60, value=Op.GAS)
                    + Op.POP(Op.SLOAD(key=Op.ADD(0xF010, Op.SLOAD(key=0x0))))
                    + Op.MSTORE(
                        offset=0x60,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x60), Op.GAS), 0x7A
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x100, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x0),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x200, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x20),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x300, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x40),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x400, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x60),
                    )
                    + Op.JUMPI(
                        pc=0x9B, condition=Op.GT(Op.SLOAD(key=0x0), 0x0)
                    )
                    + Op.PUSH1[0x0]
                    + Op.JUMP(pc=0xB4)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=Op.SUB(Op.SLOAD(key=0x0), 0x1))
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0x1016,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.JUMPDEST
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001020"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x33, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x39, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001021"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x36, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x3C, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001022"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001023"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001024"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001025"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001026"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xF126,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0xF126,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x10
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f113"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD60A7)
                    + Op.MSTORE(offset=0x0, value=0x600D)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000f114"): Account(
                    storage={0: 2989},
                    code=Op.SSTORE(key=0x0, value=0x600D) + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f115"): Account(
                    storage={0: 2989, 24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.SLOAD(key=0x60A7))
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f126"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x60A7)
                    + Op.MSTORE(
                        offset=0x0, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.JUMPI(
                        pc=0x24, condition=Op.EQ(Op.SLOAD(key=0x1), 0x0)
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.JUMP(pc=0x2B)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0111"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD)
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0112"): Account(
                    storage={0: 0xDEAD0060A7},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP,
                ),
                Address("0x00000000000000000000000000000000ead0c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x13
                        ),
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP,
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.ADD(
                                0x1000, Op.CALLDATALOAD(offset=0x4)
                            ),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x40,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x20))
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000015",  # noqa: E501
            [
                AccessList(
                    address=Address(
                        "0x000000000000000000000000000000000000f115"
                    ),
                    storage_keys=[
                        Hash(
                            "0x00000000000000000000000000000000000000000000000000000000000060a7"  # noqa: E501
                        )
                    ],
                )
            ],
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xC057,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xEAD0C057,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    storage={24743: 48879},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x1A
                        ),
                    )
                    + Op.REVERT(offset=0x0, size=0x40)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001011"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0111,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001012"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0112,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001013"): Account(
                    storage={0: 24743},
                    code=Op.MSTORE(offset=0x0, value=0xBAD)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xF113,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001014"): Account(
                    code=Op.CALL(
                        gas=0xB65,
                        address=0xF114,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001015"): Account(
                    code=Op.CALL(
                        gas=0x1800,
                        address=0xF115,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001016"): Account(
                    storage={0: 15, 24743: 57005},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0xBEEF, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0xA0, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x23
                        ),
                    )
                    + Op.MSTORE(offset=0x40, value=Op.GAS)
                    + Op.SSTORE(
                        key=Op.ADD(0xF000, Op.SLOAD(key=0x0)), value=0xBEEF
                    )
                    + Op.MSTORE(
                        offset=0x40,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x40), Op.GAS), 0x78
                        ),
                    )
                    + Op.MSTORE(offset=0x60, value=Op.GAS)
                    + Op.POP(Op.SLOAD(key=Op.ADD(0xF010, Op.SLOAD(key=0x0))))
                    + Op.MSTORE(
                        offset=0x60,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x60), Op.GAS), 0x7A
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x100, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x0),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x200, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x20),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x300, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x40),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x400, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x60),
                    )
                    + Op.JUMPI(
                        pc=0x9B, condition=Op.GT(Op.SLOAD(key=0x0), 0x0)
                    )
                    + Op.PUSH1[0x0]
                    + Op.JUMP(pc=0xB4)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=Op.SUB(Op.SLOAD(key=0x0), 0x1))
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0x1016,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.JUMPDEST
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001020"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x33, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x39, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001021"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x36, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x3C, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001022"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001023"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001024"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001025"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001026"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xF126,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0xF126,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x10
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f113"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD60A7)
                    + Op.MSTORE(offset=0x0, value=0x600D)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000f114"): Account(
                    storage={0: 2989},
                    code=Op.SSTORE(key=0x0, value=0x600D) + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f115"): Account(
                    storage={0: 24589, 24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.SLOAD(key=0x60A7))
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f126"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x60A7)
                    + Op.MSTORE(
                        offset=0x0, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.JUMPI(
                        pc=0x24, condition=Op.EQ(Op.SLOAD(key=0x1), 0x0)
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.JUMP(pc=0x2B)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0111"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD)
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0112"): Account(
                    storage={0: 0xDEAD0060A7},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP,
                ),
                Address("0x00000000000000000000000000000000ead0c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x13
                        ),
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP,
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.ADD(
                                0x1000, Op.CALLDATALOAD(offset=0x4)
                            ),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x40,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x20))
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000016",  # noqa: E501
            [
                AccessList(
                    address=Address(
                        "0xf000000000000000000000000000000000000116"
                    ),
                    storage_keys=[
                        Hash(
                            "0x00000000000000000000000000000000000000000000000000000000000060a7"  # noqa: E501
                        ),
                        Hash(
                            "0x000000000000000000000000000000000000000000000000000000000000beef"  # noqa: E501
                        ),
                    ],
                )
            ],
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xC057,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xEAD0C057,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    storage={24743: 48879},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x1A
                        ),
                    )
                    + Op.REVERT(offset=0x0, size=0x40)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001011"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0111,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001012"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0112,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001013"): Account(
                    storage={0: 24743},
                    code=Op.MSTORE(offset=0x0, value=0xBAD)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xF113,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001014"): Account(
                    code=Op.CALL(
                        gas=0xB65,
                        address=0xF114,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001015"): Account(
                    code=Op.CALL(
                        gas=0x1800,
                        address=0xF115,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001016"): Account(
                    storage={
                        256: 103,
                        257: 103,
                        258: 103,
                        259: 103,
                        260: 103,
                        261: 103,
                        262: 103,
                        263: 103,
                        264: 103,
                        265: 103,
                        266: 103,
                        267: 103,
                        268: 103,
                        269: 103,
                        270: 103,
                        271: 22103,
                        512: 100,
                        513: 100,
                        514: 100,
                        515: 100,
                        516: 100,
                        517: 100,
                        518: 100,
                        519: 100,
                        520: 100,
                        521: 100,
                        522: 100,
                        523: 100,
                        524: 100,
                        525: 100,
                        526: 100,
                        527: 2100,
                        768: 22103,
                        769: 22103,
                        770: 22103,
                        771: 22103,
                        772: 22103,
                        773: 22103,
                        774: 22103,
                        775: 22103,
                        776: 22103,
                        777: 22103,
                        778: 22103,
                        779: 22103,
                        780: 22103,
                        781: 22103,
                        782: 22103,
                        783: 22103,
                        1024: 2100,
                        1025: 2100,
                        1026: 2100,
                        1027: 2100,
                        1028: 2100,
                        1029: 2100,
                        1030: 2100,
                        1031: 2100,
                        1032: 2100,
                        1033: 2100,
                        1034: 2100,
                        1035: 2100,
                        1036: 2100,
                        1037: 2100,
                        1038: 2100,
                        1039: 2100,
                        24743: 57005,
                        48879: 2,
                        61440: 48879,
                        61441: 48879,
                        61442: 48879,
                        61443: 48879,
                        61444: 48879,
                        61445: 48879,
                        61446: 48879,
                        61447: 48879,
                        61448: 48879,
                        61449: 48879,
                        61450: 48879,
                        61451: 48879,
                        61452: 48879,
                        61453: 48879,
                        61454: 48879,
                        61455: 48879,
                    },
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0xBEEF, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0xA0, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x23
                        ),
                    )
                    + Op.MSTORE(offset=0x40, value=Op.GAS)
                    + Op.SSTORE(
                        key=Op.ADD(0xF000, Op.SLOAD(key=0x0)), value=0xBEEF
                    )
                    + Op.MSTORE(
                        offset=0x40,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x40), Op.GAS), 0x78
                        ),
                    )
                    + Op.MSTORE(offset=0x60, value=Op.GAS)
                    + Op.POP(Op.SLOAD(key=Op.ADD(0xF010, Op.SLOAD(key=0x0))))
                    + Op.MSTORE(
                        offset=0x60,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x60), Op.GAS), 0x7A
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x100, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x0),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x200, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x20),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x300, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x40),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x400, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x60),
                    )
                    + Op.JUMPI(
                        pc=0x9B, condition=Op.GT(Op.SLOAD(key=0x0), 0x0)
                    )
                    + Op.PUSH1[0x0]
                    + Op.JUMP(pc=0xB4)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=Op.SUB(Op.SLOAD(key=0x0), 0x1))
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0x1016,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.JUMPDEST
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001020"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x33, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x39, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001021"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x36, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x3C, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001022"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001023"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001024"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001025"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001026"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xF126,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0xF126,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x10
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f113"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD60A7)
                    + Op.MSTORE(offset=0x0, value=0x600D)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000f114"): Account(
                    storage={0: 2989},
                    code=Op.SSTORE(key=0x0, value=0x600D) + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f115"): Account(
                    storage={0: 2989, 24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.SLOAD(key=0x60A7))
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f126"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x60A7)
                    + Op.MSTORE(
                        offset=0x0, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.JUMPI(
                        pc=0x24, condition=Op.EQ(Op.SLOAD(key=0x1), 0x0)
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.JUMP(pc=0x2B)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0111"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD)
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0112"): Account(
                    storage={0: 0xDEAD0060A7},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP,
                ),
                Address("0x00000000000000000000000000000000ead0c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x13
                        ),
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP,
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.ADD(
                                0x1000, Op.CALLDATALOAD(offset=0x4)
                            ),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x40,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x20))
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000016",  # noqa: E501
            [
                AccessList(
                    address=Address(
                        "0x0000000000000000000000000000000000001016"
                    ),
                    storage_keys=[
                        Hash(
                            "0x00000000000000000000000000000000000000000000000000000000000060a7"  # noqa: E501
                        ),
                        Hash(
                            "0x000000000000000000000000000000000000000000000000000000000000beef"  # noqa: E501
                        ),
                        Hash(
                            "0x000000000000000000000000000000000000000000000000000000000000f000"  # noqa: E501
                        ),
                        Hash(
                            "0x000000000000000000000000000000000000000000000000000000000000f001"  # noqa: E501
                        ),
                        Hash(
                            "0x000000000000000000000000000000000000000000000000000000000000f002"  # noqa: E501
                        ),
                        Hash(
                            "0x000000000000000000000000000000000000000000000000000000000000f003"  # noqa: E501
                        ),
                        Hash(
                            "0x000000000000000000000000000000000000000000000000000000000000f004"  # noqa: E501
                        ),
                        Hash(
                            "0x000000000000000000000000000000000000000000000000000000000000f005"  # noqa: E501
                        ),
                        Hash(
                            "0x000000000000000000000000000000000000000000000000000000000000f006"  # noqa: E501
                        ),
                        Hash(
                            "0x000000000000000000000000000000000000000000000000000000000000f007"  # noqa: E501
                        ),
                        Hash(
                            "0x000000000000000000000000000000000000000000000000000000000000f008"  # noqa: E501
                        ),
                        Hash(
                            "0x000000000000000000000000000000000000000000000000000000000000f009"  # noqa: E501
                        ),
                        Hash(
                            "0x000000000000000000000000000000000000000000000000000000000000f00a"  # noqa: E501
                        ),
                        Hash(
                            "0x000000000000000000000000000000000000000000000000000000000000f00b"  # noqa: E501
                        ),
                        Hash(
                            "0x000000000000000000000000000000000000000000000000000000000000f00c"  # noqa: E501
                        ),
                        Hash(
                            "0x000000000000000000000000000000000000000000000000000000000000f00d"  # noqa: E501
                        ),
                        Hash(
                            "0x000000000000000000000000000000000000000000000000000000000000f00e"  # noqa: E501
                        ),
                        Hash(
                            "0x000000000000000000000000000000000000000000000000000000000000f00f"  # noqa: E501
                        ),
                        Hash(
                            "0x000000000000000000000000000000000000000000000000000000000000f010"  # noqa: E501
                        ),
                        Hash(
                            "0x000000000000000000000000000000000000000000000000000000000000f011"  # noqa: E501
                        ),
                        Hash(
                            "0x000000000000000000000000000000000000000000000000000000000000f012"  # noqa: E501
                        ),
                        Hash(
                            "0x000000000000000000000000000000000000000000000000000000000000f013"  # noqa: E501
                        ),
                        Hash(
                            "0x000000000000000000000000000000000000000000000000000000000000f014"  # noqa: E501
                        ),
                        Hash(
                            "0x000000000000000000000000000000000000000000000000000000000000f015"  # noqa: E501
                        ),
                        Hash(
                            "0x000000000000000000000000000000000000000000000000000000000000f016"  # noqa: E501
                        ),
                        Hash(
                            "0x000000000000000000000000000000000000000000000000000000000000f017"  # noqa: E501
                        ),
                        Hash(
                            "0x000000000000000000000000000000000000000000000000000000000000f018"  # noqa: E501
                        ),
                        Hash(
                            "0x000000000000000000000000000000000000000000000000000000000000f019"  # noqa: E501
                        ),
                        Hash(
                            "0x000000000000000000000000000000000000000000000000000000000000f01a"  # noqa: E501
                        ),
                        Hash(
                            "0x000000000000000000000000000000000000000000000000000000000000f01b"  # noqa: E501
                        ),
                        Hash(
                            "0x000000000000000000000000000000000000000000000000000000000000f01c"  # noqa: E501
                        ),
                        Hash(
                            "0x000000000000000000000000000000000000000000000000000000000000f01d"  # noqa: E501
                        ),
                        Hash(
                            "0x000000000000000000000000000000000000000000000000000000000000f01e"  # noqa: E501
                        ),
                        Hash(
                            "0x000000000000000000000000000000000000000000000000000000000000f01f"  # noqa: E501
                        ),
                    ],
                )
            ],
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xC057,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xEAD0C057,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    storage={24743: 48879},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x1A
                        ),
                    )
                    + Op.REVERT(offset=0x0, size=0x40)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001011"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0111,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001012"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0112,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001013"): Account(
                    storage={0: 24743},
                    code=Op.MSTORE(offset=0x0, value=0xBAD)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xF113,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001014"): Account(
                    code=Op.CALL(
                        gas=0xB65,
                        address=0xF114,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001015"): Account(
                    code=Op.CALL(
                        gas=0x1800,
                        address=0xF115,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001016"): Account(
                    storage={
                        256: 103,
                        257: 103,
                        258: 103,
                        259: 103,
                        260: 103,
                        261: 103,
                        262: 103,
                        263: 103,
                        264: 103,
                        265: 103,
                        266: 103,
                        267: 103,
                        268: 103,
                        269: 103,
                        270: 103,
                        271: 20003,
                        512: 100,
                        513: 100,
                        514: 100,
                        515: 100,
                        516: 100,
                        517: 100,
                        518: 100,
                        519: 100,
                        520: 100,
                        521: 100,
                        522: 100,
                        523: 100,
                        524: 100,
                        525: 100,
                        526: 100,
                        527: 100,
                        768: 20003,
                        769: 20003,
                        770: 20003,
                        771: 20003,
                        772: 20003,
                        773: 20003,
                        774: 20003,
                        775: 20003,
                        776: 20003,
                        777: 20003,
                        778: 20003,
                        779: 20003,
                        780: 20003,
                        781: 20003,
                        782: 20003,
                        783: 20003,
                        1024: 100,
                        1025: 100,
                        1026: 100,
                        1027: 100,
                        1028: 100,
                        1029: 100,
                        1030: 100,
                        1031: 100,
                        1032: 100,
                        1033: 100,
                        1034: 100,
                        1035: 100,
                        1036: 100,
                        1037: 100,
                        1038: 100,
                        1039: 100,
                        24743: 57005,
                        48879: 2,
                        61440: 48879,
                        61441: 48879,
                        61442: 48879,
                        61443: 48879,
                        61444: 48879,
                        61445: 48879,
                        61446: 48879,
                        61447: 48879,
                        61448: 48879,
                        61449: 48879,
                        61450: 48879,
                        61451: 48879,
                        61452: 48879,
                        61453: 48879,
                        61454: 48879,
                        61455: 48879,
                    },
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0xBEEF, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0xA0, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x23
                        ),
                    )
                    + Op.MSTORE(offset=0x40, value=Op.GAS)
                    + Op.SSTORE(
                        key=Op.ADD(0xF000, Op.SLOAD(key=0x0)), value=0xBEEF
                    )
                    + Op.MSTORE(
                        offset=0x40,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x40), Op.GAS), 0x78
                        ),
                    )
                    + Op.MSTORE(offset=0x60, value=Op.GAS)
                    + Op.POP(Op.SLOAD(key=Op.ADD(0xF010, Op.SLOAD(key=0x0))))
                    + Op.MSTORE(
                        offset=0x60,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x60), Op.GAS), 0x7A
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x100, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x0),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x200, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x20),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x300, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x40),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x400, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x60),
                    )
                    + Op.JUMPI(
                        pc=0x9B, condition=Op.GT(Op.SLOAD(key=0x0), 0x0)
                    )
                    + Op.PUSH1[0x0]
                    + Op.JUMP(pc=0xB4)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=Op.SUB(Op.SLOAD(key=0x0), 0x1))
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0x1016,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.JUMPDEST
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001020"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x33, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x39, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001021"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x36, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x3C, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001022"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001023"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001024"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001025"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001026"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xF126,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0xF126,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x10
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f113"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD60A7)
                    + Op.MSTORE(offset=0x0, value=0x600D)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000f114"): Account(
                    storage={0: 2989},
                    code=Op.SSTORE(key=0x0, value=0x600D) + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f115"): Account(
                    storage={0: 2989, 24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.SLOAD(key=0x60A7))
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f126"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x60A7)
                    + Op.MSTORE(
                        offset=0x0, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.JUMPI(
                        pc=0x24, condition=Op.EQ(Op.SLOAD(key=0x1), 0x0)
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.JUMP(pc=0x2B)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0111"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD)
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0112"): Account(
                    storage={0: 0xDEAD0060A7},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP,
                ),
                Address("0x00000000000000000000000000000000ead0c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x13
                        ),
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP,
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.ADD(
                                0x1000, Op.CALLDATALOAD(offset=0x4)
                            ),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x40,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x20))
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000013",  # noqa: E501
            [
                AccessList(
                    address=Address(
                        "0x0000000000000000000000000000000000000000"
                    ),
                    storage_keys=[
                        Hash(
                            "0x0000000000000000000000000000000000000000000000000000000000000000"  # noqa: E501
                        )
                    ],
                )
            ],
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xC057,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xEAD0C057,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    storage={24743: 48879},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x1A
                        ),
                    )
                    + Op.REVERT(offset=0x0, size=0x40)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001011"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0111,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001012"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0112,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001013"): Account(
                    storage={0: 2989},
                    code=Op.MSTORE(offset=0x0, value=0xBAD)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xF113,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001014"): Account(
                    code=Op.CALL(
                        gas=0xB65,
                        address=0xF114,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001015"): Account(
                    code=Op.CALL(
                        gas=0x1800,
                        address=0xF115,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001016"): Account(
                    storage={0: 15, 24743: 57005},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0xBEEF, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0xA0, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x23
                        ),
                    )
                    + Op.MSTORE(offset=0x40, value=Op.GAS)
                    + Op.SSTORE(
                        key=Op.ADD(0xF000, Op.SLOAD(key=0x0)), value=0xBEEF
                    )
                    + Op.MSTORE(
                        offset=0x40,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x40), Op.GAS), 0x78
                        ),
                    )
                    + Op.MSTORE(offset=0x60, value=Op.GAS)
                    + Op.POP(Op.SLOAD(key=Op.ADD(0xF010, Op.SLOAD(key=0x0))))
                    + Op.MSTORE(
                        offset=0x60,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x60), Op.GAS), 0x7A
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x100, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x0),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x200, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x20),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x300, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x40),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x400, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x60),
                    )
                    + Op.JUMPI(
                        pc=0x9B, condition=Op.GT(Op.SLOAD(key=0x0), 0x0)
                    )
                    + Op.PUSH1[0x0]
                    + Op.JUMP(pc=0xB4)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=Op.SUB(Op.SLOAD(key=0x0), 0x1))
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0x1016,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.JUMPDEST
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001020"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x33, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x39, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001021"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x36, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x3C, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001022"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001023"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001024"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001025"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001026"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xF126,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0xF126,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x10
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f113"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD60A7)
                    + Op.MSTORE(offset=0x0, value=0x600D)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000f114"): Account(
                    storage={0: 2989},
                    code=Op.SSTORE(key=0x0, value=0x600D) + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f115"): Account(
                    storage={0: 2989, 24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.SLOAD(key=0x60A7))
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f126"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x60A7)
                    + Op.MSTORE(
                        offset=0x0, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.JUMPI(
                        pc=0x24, condition=Op.EQ(Op.SLOAD(key=0x1), 0x0)
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.JUMP(pc=0x2B)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0111"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD)
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0112"): Account(
                    storage={0: 0xDEAD0060A7},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP,
                ),
                Address("0x00000000000000000000000000000000ead0c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x13
                        ),
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP,
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.ADD(
                                0x1000, Op.CALLDATALOAD(offset=0x4)
                            ),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x40,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x20))
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000013",  # noqa: E501
            [
                AccessList(
                    address=Address(
                        "0x000000000000000000000000000000000000f113"
                    ),
                    storage_keys=[
                        Hash(
                            "0x0000000000000000000000000000000000000000000000000000000000000000"  # noqa: E501
                        )
                    ],
                )
            ],
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xC057,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xEAD0C057,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    storage={24743: 48879},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x1A
                        ),
                    )
                    + Op.REVERT(offset=0x0, size=0x40)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001011"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0111,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001012"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0112,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001013"): Account(
                    storage={0: 2989},
                    code=Op.MSTORE(offset=0x0, value=0xBAD)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xF113,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001014"): Account(
                    code=Op.CALL(
                        gas=0xB65,
                        address=0xF114,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001015"): Account(
                    code=Op.CALL(
                        gas=0x1800,
                        address=0xF115,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001016"): Account(
                    storage={0: 15, 24743: 57005},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0xBEEF, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0xA0, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x23
                        ),
                    )
                    + Op.MSTORE(offset=0x40, value=Op.GAS)
                    + Op.SSTORE(
                        key=Op.ADD(0xF000, Op.SLOAD(key=0x0)), value=0xBEEF
                    )
                    + Op.MSTORE(
                        offset=0x40,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x40), Op.GAS), 0x78
                        ),
                    )
                    + Op.MSTORE(offset=0x60, value=Op.GAS)
                    + Op.POP(Op.SLOAD(key=Op.ADD(0xF010, Op.SLOAD(key=0x0))))
                    + Op.MSTORE(
                        offset=0x60,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x60), Op.GAS), 0x7A
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x100, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x0),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x200, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x20),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x300, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x40),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x400, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x60),
                    )
                    + Op.JUMPI(
                        pc=0x9B, condition=Op.GT(Op.SLOAD(key=0x0), 0x0)
                    )
                    + Op.PUSH1[0x0]
                    + Op.JUMP(pc=0xB4)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=Op.SUB(Op.SLOAD(key=0x0), 0x1))
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0x1016,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.JUMPDEST
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001020"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x33, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x39, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001021"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x36, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x3C, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001022"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001023"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001024"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001025"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001026"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xF126,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0xF126,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x10
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f113"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD60A7)
                    + Op.MSTORE(offset=0x0, value=0x600D)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000f114"): Account(
                    storage={0: 2989},
                    code=Op.SSTORE(key=0x0, value=0x600D) + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f115"): Account(
                    storage={0: 2989, 24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.SLOAD(key=0x60A7))
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f126"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x60A7)
                    + Op.MSTORE(
                        offset=0x0, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.JUMPI(
                        pc=0x24, condition=Op.EQ(Op.SLOAD(key=0x1), 0x0)
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.JUMP(pc=0x2B)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0111"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD)
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0112"): Account(
                    storage={0: 0xDEAD0060A7},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP,
                ),
                Address("0x00000000000000000000000000000000ead0c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x13
                        ),
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP,
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.ADD(
                                0x1000, Op.CALLDATALOAD(offset=0x4)
                            ),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x40,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x20))
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000003",  # noqa: E501
            [
                AccessList(
                    address=Address(
                        "0x00000000000000000000000000000000ead0c057"
                    ),
                    storage_keys=[
                        Hash(
                            "0x0000000000000000000000000000000000000000000000000000000000000000"  # noqa: E501
                        ),
                        Hash(
                            "0x00000000000000000000000000000000000000000000000000000000000060a7"  # noqa: E501
                        ),
                    ],
                )
            ],
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xC057,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    storage={0: 107},
                    code=Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xEAD0C057,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    storage={24743: 48879},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x1A
                        ),
                    )
                    + Op.REVERT(offset=0x0, size=0x40)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001011"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0111,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001012"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0112,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001013"): Account(
                    storage={0: 24743},
                    code=Op.MSTORE(offset=0x0, value=0xBAD)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xF113,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001014"): Account(
                    code=Op.CALL(
                        gas=0xB65,
                        address=0xF114,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001015"): Account(
                    code=Op.CALL(
                        gas=0x1800,
                        address=0xF115,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001016"): Account(
                    storage={0: 15, 24743: 57005},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0xBEEF, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0xA0, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x23
                        ),
                    )
                    + Op.MSTORE(offset=0x40, value=Op.GAS)
                    + Op.SSTORE(
                        key=Op.ADD(0xF000, Op.SLOAD(key=0x0)), value=0xBEEF
                    )
                    + Op.MSTORE(
                        offset=0x40,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x40), Op.GAS), 0x78
                        ),
                    )
                    + Op.MSTORE(offset=0x60, value=Op.GAS)
                    + Op.POP(Op.SLOAD(key=Op.ADD(0xF010, Op.SLOAD(key=0x0))))
                    + Op.MSTORE(
                        offset=0x60,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x60), Op.GAS), 0x7A
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x100, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x0),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x200, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x20),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x300, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x40),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x400, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x60),
                    )
                    + Op.JUMPI(
                        pc=0x9B, condition=Op.GT(Op.SLOAD(key=0x0), 0x0)
                    )
                    + Op.PUSH1[0x0]
                    + Op.JUMP(pc=0xB4)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=Op.SUB(Op.SLOAD(key=0x0), 0x1))
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0x1016,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.JUMPDEST
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001020"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x33, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x39, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001021"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x36, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x3C, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001022"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001023"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001024"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001025"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001026"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xF126,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0xF126,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x10
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f113"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD60A7)
                    + Op.MSTORE(offset=0x0, value=0x600D)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000f114"): Account(
                    storage={0: 2989},
                    code=Op.SSTORE(key=0x0, value=0x600D) + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f115"): Account(
                    storage={0: 2989, 24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.SLOAD(key=0x60A7))
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f126"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x60A7)
                    + Op.MSTORE(
                        offset=0x0, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.JUMPI(
                        pc=0x24, condition=Op.EQ(Op.SLOAD(key=0x1), 0x0)
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.JUMP(pc=0x2B)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0111"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD)
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0112"): Account(
                    storage={0: 0xDEAD0060A7},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP,
                ),
                Address("0x00000000000000000000000000000000ead0c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x13
                        ),
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP,
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.ADD(
                                0x1000, Op.CALLDATALOAD(offset=0x4)
                            ),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x40,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x20))
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000003",  # noqa: E501
            [
                AccessList(
                    address=Address(
                        "0x0000000000000000000000000000000000001003"
                    ),
                    storage_keys=[
                        Hash(
                            "0x0000000000000000000000000000000000000000000000000000000000000000"  # noqa: E501
                        ),
                        Hash(
                            "0x00000000000000000000000000000000000000000000000000000000000060a7"  # noqa: E501
                        ),
                    ],
                )
            ],
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xC057,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    storage={0: 2107},
                    code=Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xEAD0C057,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    storage={24743: 48879},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x1A
                        ),
                    )
                    + Op.REVERT(offset=0x0, size=0x40)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001011"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0111,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001012"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0112,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001013"): Account(
                    storage={0: 24743},
                    code=Op.MSTORE(offset=0x0, value=0xBAD)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xF113,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001014"): Account(
                    code=Op.CALL(
                        gas=0xB65,
                        address=0xF114,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001015"): Account(
                    code=Op.CALL(
                        gas=0x1800,
                        address=0xF115,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001016"): Account(
                    storage={0: 15, 24743: 57005},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0xBEEF, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0xA0, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x23
                        ),
                    )
                    + Op.MSTORE(offset=0x40, value=Op.GAS)
                    + Op.SSTORE(
                        key=Op.ADD(0xF000, Op.SLOAD(key=0x0)), value=0xBEEF
                    )
                    + Op.MSTORE(
                        offset=0x40,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x40), Op.GAS), 0x78
                        ),
                    )
                    + Op.MSTORE(offset=0x60, value=Op.GAS)
                    + Op.POP(Op.SLOAD(key=Op.ADD(0xF010, Op.SLOAD(key=0x0))))
                    + Op.MSTORE(
                        offset=0x60,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x60), Op.GAS), 0x7A
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x100, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x0),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x200, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x20),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x300, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x40),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x400, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x60),
                    )
                    + Op.JUMPI(
                        pc=0x9B, condition=Op.GT(Op.SLOAD(key=0x0), 0x0)
                    )
                    + Op.PUSH1[0x0]
                    + Op.JUMP(pc=0xB4)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=Op.SUB(Op.SLOAD(key=0x0), 0x1))
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0x1016,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.JUMPDEST
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001020"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x33, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x39, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001021"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x36, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x3C, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001022"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001023"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001024"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001025"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001026"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xF126,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0xF126,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x10
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f113"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD60A7)
                    + Op.MSTORE(offset=0x0, value=0x600D)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000f114"): Account(
                    storage={0: 2989},
                    code=Op.SSTORE(key=0x0, value=0x600D) + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f115"): Account(
                    storage={0: 2989, 24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.SLOAD(key=0x60A7))
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f126"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x60A7)
                    + Op.MSTORE(
                        offset=0x0, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.JUMPI(
                        pc=0x24, condition=Op.EQ(Op.SLOAD(key=0x1), 0x0)
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.JUMP(pc=0x2B)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0111"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD)
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0112"): Account(
                    storage={0: 0xDEAD0060A7},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP,
                ),
                Address("0x00000000000000000000000000000000ead0c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x13
                        ),
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP,
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.ADD(
                                0x1000, Op.CALLDATALOAD(offset=0x4)
                            ),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x40,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x20))
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000014",  # noqa: E501
            [
                AccessList(
                    address=Address(
                        "0x0000000000000000000000000000000000001014"
                    ),
                    storage_keys=[
                        Hash(
                            "0x0000000000000000000000000000000000000000000000000000000000000000"  # noqa: E501
                        )
                    ],
                )
            ],
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xC057,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xEAD0C057,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    storage={24743: 48879},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x1A
                        ),
                    )
                    + Op.REVERT(offset=0x0, size=0x40)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001011"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0111,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001012"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0112,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001013"): Account(
                    storage={0: 24743},
                    code=Op.MSTORE(offset=0x0, value=0xBAD)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xF113,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001014"): Account(
                    code=Op.CALL(
                        gas=0xB65,
                        address=0xF114,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001015"): Account(
                    code=Op.CALL(
                        gas=0x1800,
                        address=0xF115,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001016"): Account(
                    storage={0: 15, 24743: 57005},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0xBEEF, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0xA0, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x23
                        ),
                    )
                    + Op.MSTORE(offset=0x40, value=Op.GAS)
                    + Op.SSTORE(
                        key=Op.ADD(0xF000, Op.SLOAD(key=0x0)), value=0xBEEF
                    )
                    + Op.MSTORE(
                        offset=0x40,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x40), Op.GAS), 0x78
                        ),
                    )
                    + Op.MSTORE(offset=0x60, value=Op.GAS)
                    + Op.POP(Op.SLOAD(key=Op.ADD(0xF010, Op.SLOAD(key=0x0))))
                    + Op.MSTORE(
                        offset=0x60,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x60), Op.GAS), 0x7A
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x100, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x0),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x200, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x20),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x300, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x40),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x400, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x60),
                    )
                    + Op.JUMPI(
                        pc=0x9B, condition=Op.GT(Op.SLOAD(key=0x0), 0x0)
                    )
                    + Op.PUSH1[0x0]
                    + Op.JUMP(pc=0xB4)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=Op.SUB(Op.SLOAD(key=0x0), 0x1))
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0x1016,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.JUMPDEST
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001020"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x33, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x39, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001021"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x36, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x3C, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001022"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001023"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001024"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001025"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001026"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xF126,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0xF126,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x10
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f113"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD60A7)
                    + Op.MSTORE(offset=0x0, value=0x600D)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000f114"): Account(
                    storage={0: 2989},
                    code=Op.SSTORE(key=0x0, value=0x600D) + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f115"): Account(
                    storage={0: 2989, 24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.SLOAD(key=0x60A7))
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f126"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x60A7)
                    + Op.MSTORE(
                        offset=0x0, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.JUMPI(
                        pc=0x24, condition=Op.EQ(Op.SLOAD(key=0x1), 0x0)
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.JUMP(pc=0x2B)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0111"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD)
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0112"): Account(
                    storage={0: 0xDEAD0060A7},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP,
                ),
                Address("0x00000000000000000000000000000000ead0c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x13
                        ),
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP,
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.ADD(
                                0x1000, Op.CALLDATALOAD(offset=0x4)
                            ),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x40,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x20))
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000014",  # noqa: E501
            [
                AccessList(
                    address=Address(
                        "0x000000000000000000000000000000000000f114"
                    ),
                    storage_keys=[
                        Hash(
                            "0x0000000000000000000000000000000000000000000000000000000000000000"  # noqa: E501
                        )
                    ],
                )
            ],
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xC057,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xC057,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xEAD0C057,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    storage={24743: 48879},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x1A
                        ),
                    )
                    + Op.REVERT(offset=0x0, size=0x40)
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001011"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0111,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001012"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xDEAD0112,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001013"): Account(
                    storage={0: 24743},
                    code=Op.MSTORE(offset=0x0, value=0xBAD)
                    + Op.POP(
                        Op.STATICCALL(
                            gas=Op.GAS,
                            address=0xF113,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001014"): Account(
                    code=Op.CALL(
                        gas=0xB65,
                        address=0xF114,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001015"): Account(
                    code=Op.CALL(
                        gas=0x1800,
                        address=0xF115,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001016"): Account(
                    storage={0: 15, 24743: 57005},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0xBEEF, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.MSTORE(offset=0x20, value=Op.GAS)
                    + Op.MSTORE(offset=0xA0, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x20,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x23
                        ),
                    )
                    + Op.MSTORE(offset=0x40, value=Op.GAS)
                    + Op.SSTORE(
                        key=Op.ADD(0xF000, Op.SLOAD(key=0x0)), value=0xBEEF
                    )
                    + Op.MSTORE(
                        offset=0x40,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x40), Op.GAS), 0x78
                        ),
                    )
                    + Op.MSTORE(offset=0x60, value=Op.GAS)
                    + Op.POP(Op.SLOAD(key=Op.ADD(0xF010, Op.SLOAD(key=0x0))))
                    + Op.MSTORE(
                        offset=0x60,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x60), Op.GAS), 0x7A
                        ),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x100, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x0),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x200, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x20),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x300, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x40),
                    )
                    + Op.SSTORE(
                        key=Op.ADD(0x400, Op.SLOAD(key=0x0)),
                        value=Op.MLOAD(offset=0x60),
                    )
                    + Op.JUMPI(
                        pc=0x9B, condition=Op.GT(Op.SLOAD(key=0x0), 0x0)
                    )
                    + Op.PUSH1[0x0]
                    + Op.JUMP(pc=0xB4)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=Op.SUB(Op.SLOAD(key=0x0), 0x1))
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0x1016,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.JUMPDEST
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001020"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x33, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x39, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001021"): Account(
                    code=Op.PUSH1[0x6]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x36, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x3C, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(key=0x0, value=0xFF)
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x10)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001022"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001023"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001024"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001025"): Account(
                    code=Op.PUSH1[0x13]
                    + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
                    + Op.PUSH2[0x200]
                    + Op.MSTORE
                    + Op.PUSH1[0x21]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
                    + Op.PUSH2[0x220]
                    + Op.MSTORE
                    + Op.MSTORE(
                        offset=0x240,
                        value=Op.CREATE2(
                            value=0x0,
                            offset=0x0,
                            size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                            salt=0x5A17,
                        ),
                    )
                    + Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.MLOAD(offset=0x240),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.STOP
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0xFFFF)
                    + Op.SSTORE(
                        key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
                    + Op.RETURN(offset=0x0, size=0x80)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001026"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=0xF126,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.CALL(
                        gas=Op.GAS,
                        address=0xF126,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x2)
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x10
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f113"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD60A7)
                    + Op.MSTORE(offset=0x0, value=0x600D)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000f114"): Account(
                    storage={0: 24589},
                    code=Op.SSTORE(key=0x0, value=0x600D) + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f115"): Account(
                    storage={0: 2989, 24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.SLOAD(key=0x60A7))
                    + Op.SSTORE(key=0x0, value=0x600D)
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000f126"): Account(
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.SSTORE(key=0x0, value=0x60A7)
                    + Op.MSTORE(
                        offset=0x0, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                    )
                    + Op.JUMPI(
                        pc=0x24, condition=Op.EQ(Op.SLOAD(key=0x1), 0x0)
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.JUMP(pc=0x2B)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.JUMPDEST
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0111"): Account(
                    code=Op.SSTORE(key=0x0, value=0xDEAD)
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000dead0112"): Account(
                    storage={0: 0xDEAD0060A7},
                    code=Op.POP(Op.SLOAD(key=0x0))
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP,
                ),
                Address("0x00000000000000000000000000000000ead0c057"): Account(
                    storage={24743: 57005},
                    code=Op.MSTORE(offset=0x0, value=Op.GAS)
                    + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
                    + Op.MSTORE(
                        offset=0x0,
                        value=Op.SUB(
                            Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x13
                        ),
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP,
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.GAS,
                            address=Op.ADD(
                                0x1000, Op.CALLDATALOAD(offset=0x4)
                            ),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x40,
                        )
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x20))
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
        "case28",
        "case29",
        "case30",
        "case31",
        "case32",
        "case33",
        "case34",
        "case35",
    ],
)
@pytest.mark.pre_alloc_mutable
def test_varied_context(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    tx_access_list: list | None,
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
    callee_4 = Address("0x0000000000000000000000000000000000001010")
    callee_5 = Address("0x0000000000000000000000000000000000001011")
    callee_6 = Address("0x0000000000000000000000000000000000001012")
    callee_7 = Address("0x0000000000000000000000000000000000001013")
    callee_8 = Address("0x0000000000000000000000000000000000001014")
    callee_9 = Address("0x0000000000000000000000000000000000001015")
    callee_10 = Address("0x0000000000000000000000000000000000001016")
    callee_11 = Address("0x0000000000000000000000000000000000001020")
    callee_12 = Address("0x0000000000000000000000000000000000001021")
    callee_13 = Address("0x0000000000000000000000000000000000001022")
    callee_14 = Address("0x0000000000000000000000000000000000001023")
    callee_15 = Address("0x0000000000000000000000000000000000001024")
    callee_16 = Address("0x0000000000000000000000000000000000001025")
    callee_17 = Address("0x0000000000000000000000000000000000001026")
    callee_18 = Address("0x000000000000000000000000000000000000c057")
    callee_19 = Address("0x000000000000000000000000000000000000f113")
    callee_20 = Address("0x000000000000000000000000000000000000f114")
    callee_21 = Address("0x000000000000000000000000000000000000f115")
    callee_22 = Address("0x000000000000000000000000000000000000f126")
    callee_23 = Address("0x00000000000000000000000000000000dead0111")
    callee_24 = Address("0x00000000000000000000000000000000dead0112")
    callee_25 = Address("0x00000000000000000000000000000000ead0c057")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=71794957647893862,
    )

    pre[callee] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.DELEGATECALL(
                gas=Op.GAS,
                address=0xC057,
                args_offset=0x0,
                args_size=0x0,
                ret_offset=0x0,
                ret_size=0x0,
            )
            + Op.STOP
        ),
    )
    pre[callee_1] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.CALL(
                gas=Op.GAS,
                address=0xC057,
                value=0x0,
                args_offset=0x0,
                args_size=0x0,
                ret_offset=0x0,
                ret_size=0x0,
            )
            + Op.STOP
        ),
    )
    pre[callee_2] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.CALLCODE(
                gas=Op.GAS,
                address=0xC057,
                value=0x0,
                args_offset=0x0,
                args_size=0x0,
                ret_offset=0x0,
                ret_size=0x0,
            )
            + Op.STOP
        ),
    )
    pre[callee_3] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.POP(
                Op.STATICCALL(
                    gas=Op.GAS,
                    address=0xEAD0C057,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x20,
                ),
            )
            + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
            + Op.STOP
        ),
    )
    pre[callee_4] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.MSTORE(offset=0x0, value=Op.GAS)
            + Op.SSTORE(key=0x0, value=0x2)
            + Op.MSTORE(
                offset=0x0,
                value=Op.SUB(Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11),
            )
            + Op.MSTORE(offset=0x20, value=Op.GAS)
            + Op.MSTORE(offset=0x40, value=Op.SLOAD(key=0x60A7))
            + Op.MSTORE(
                offset=0x20,
                value=Op.SUB(Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x1A),
            )
            + Op.REVERT(offset=0x0, size=0x40)
            + Op.STOP
        ),
        storage={0x60A7: 0xBEEF},
    )
    pre[callee_5] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.MSTORE(offset=0x0, value=Op.GAS)
            + Op.POP(
                Op.CALL(
                    gas=Op.GAS,
                    address=0xDEAD0111,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.SSTORE(
                key=0x0,
                value=Op.SUB(Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8),
            )
            + Op.STOP
        ),
    )
    pre[callee_6] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.MSTORE(offset=0x0, value=Op.GAS)
            + Op.POP(
                Op.CALL(
                    gas=Op.GAS,
                    address=0xDEAD0112,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.SSTORE(
                key=0x0,
                value=Op.SUB(Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x7FE8),
            )
            + Op.STOP
        ),
    )
    pre[callee_7] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.MSTORE(offset=0x0, value=0xBAD)
            + Op.POP(
                Op.STATICCALL(
                    gas=Op.GAS,
                    address=0xF113,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x20,
                ),
            )
            + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
            + Op.STOP
        ),
        storage={0x0: 0x60A7},
    )
    pre[callee_8] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.CALL(
                gas=0xB65,
                address=0xF114,
                value=0x0,
                args_offset=0x0,
                args_size=0x0,
                ret_offset=0x0,
                ret_size=0x20,
            )
            + Op.STOP
        ),
    )
    pre[callee_9] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.CALL(
                gas=0x1800,
                address=0xF115,
                value=0x0,
                args_offset=0x0,
                args_size=0x0,
                ret_offset=0x0,
                ret_size=0x20,
            )
            + Op.STOP
        ),
    )
    pre[callee_10] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.POP(Op.SLOAD(key=0x0))
            + Op.MSTORE(offset=0x0, value=Op.GAS)
            + Op.SSTORE(key=0xBEEF, value=0x2)
            + Op.MSTORE(
                offset=0x0,
                value=Op.SUB(Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11),
            )
            + Op.MSTORE(offset=0x20, value=Op.GAS)
            + Op.MSTORE(offset=0xA0, value=Op.SLOAD(key=0x60A7))
            + Op.MSTORE(
                offset=0x20,
                value=Op.SUB(Op.SUB(Op.MLOAD(offset=0x20), Op.GAS), 0x23),
            )
            + Op.MSTORE(offset=0x40, value=Op.GAS)
            + Op.SSTORE(key=Op.ADD(0xF000, Op.SLOAD(key=0x0)), value=0xBEEF)
            + Op.MSTORE(
                offset=0x40,
                value=Op.SUB(Op.SUB(Op.MLOAD(offset=0x40), Op.GAS), 0x78),
            )
            + Op.MSTORE(offset=0x60, value=Op.GAS)
            + Op.POP(Op.SLOAD(key=Op.ADD(0xF010, Op.SLOAD(key=0x0))))
            + Op.MSTORE(
                offset=0x60,
                value=Op.SUB(Op.SUB(Op.MLOAD(offset=0x60), Op.GAS), 0x7A),
            )
            + Op.SSTORE(
                key=Op.ADD(0x100, Op.SLOAD(key=0x0)),
                value=Op.MLOAD(offset=0x0),
            )
            + Op.SSTORE(
                key=Op.ADD(0x200, Op.SLOAD(key=0x0)),
                value=Op.MLOAD(offset=0x20),
            )
            + Op.SSTORE(
                key=Op.ADD(0x300, Op.SLOAD(key=0x0)),
                value=Op.MLOAD(offset=0x40),
            )
            + Op.SSTORE(
                key=Op.ADD(0x400, Op.SLOAD(key=0x0)),
                value=Op.MLOAD(offset=0x60),
            )
            + Op.JUMPI(pc=0x9B, condition=Op.GT(Op.SLOAD(key=0x0), 0x0))
            + Op.PUSH1[0x0]
            + Op.JUMP(pc=0xB4)
            + Op.JUMPDEST
            + Op.SSTORE(key=0x0, value=Op.SUB(Op.SLOAD(key=0x0), 0x1))
            + Op.CALL(
                gas=Op.GAS,
                address=0x1016,
                value=0x0,
                args_offset=0x0,
                args_size=0x0,
                ret_offset=0x0,
                ret_size=0x0,
            )
            + Op.JUMPDEST
            + Op.STOP
        ),
        storage={0x0: 0xF, 0x60A7: 0xDEAD},
    )
    pre[callee_11] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.PUSH1[0x6]
            + Op.CODECOPY(dest_offset=0x100, offset=0x33, size=Op.DUP1)
            + Op.PUSH2[0x200]
            + Op.MSTORE
            + Op.PUSH1[0x21]
            + Op.CODECOPY(dest_offset=0x0, offset=0x39, size=Op.DUP1)
            + Op.PUSH2[0x220]
            + Op.MSTORE
            + Op.MSTORE(
                offset=0x240,
                value=Op.CREATE(
                    value=0x0,
                    offset=0x0,
                    size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                ),
            )
            + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
            + Op.STOP
            + Op.INVALID
            + Op.SSTORE(key=0x0, value=0xFF)
            + Op.STOP
            + Op.MSTORE(offset=0x0, value=Op.GAS)
            + Op.SSTORE(key=0x0, value=0xFFFF)
            + Op.SSTORE(key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS))
            + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
            + Op.RETURN(offset=0x0, size=0x10)
            + Op.STOP
        ),
    )
    pre[callee_12] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.PUSH1[0x6]
            + Op.CODECOPY(dest_offset=0x100, offset=0x36, size=Op.DUP1)
            + Op.PUSH2[0x200]
            + Op.MSTORE
            + Op.PUSH1[0x21]
            + Op.CODECOPY(dest_offset=0x0, offset=0x3C, size=Op.DUP1)
            + Op.PUSH2[0x220]
            + Op.MSTORE
            + Op.MSTORE(
                offset=0x240,
                value=Op.CREATE2(
                    value=0x0,
                    offset=0x0,
                    size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                    salt=0x5A17,
                ),
            )
            + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
            + Op.STOP
            + Op.INVALID
            + Op.SSTORE(key=0x0, value=0xFF)
            + Op.STOP
            + Op.MSTORE(offset=0x0, value=Op.GAS)
            + Op.SSTORE(key=0x0, value=0xFFFF)
            + Op.SSTORE(key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS))
            + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
            + Op.RETURN(offset=0x0, size=0x10)
            + Op.STOP
        ),
    )
    pre[callee_13] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.PUSH1[0x13]
            + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
            + Op.PUSH2[0x200]
            + Op.MSTORE
            + Op.PUSH1[0xF]
            + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
            + Op.PUSH2[0x220]
            + Op.MSTORE
            + Op.MSTORE(
                offset=0x240,
                value=Op.CREATE(
                    value=0x0,
                    offset=0x0,
                    size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                ),
            )
            + Op.POP(
                Op.CALL(
                    gas=Op.GAS,
                    address=Op.MLOAD(offset=0x240),
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
            + Op.STOP
            + Op.INVALID
            + Op.MSTORE(offset=0x0, value=Op.GAS)
            + Op.SSTORE(key=0x0, value=0xFFFF)
            + Op.SSTORE(key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS))
            + Op.STOP
            + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
            + Op.RETURN(offset=0x0, size=0x80)
            + Op.STOP
        ),
    )
    pre[callee_14] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.PUSH1[0x13]
            + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
            + Op.PUSH2[0x200]
            + Op.MSTORE
            + Op.PUSH1[0xF]
            + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
            + Op.PUSH2[0x220]
            + Op.MSTORE
            + Op.MSTORE(
                offset=0x240,
                value=Op.CREATE2(
                    value=0x0,
                    offset=0x0,
                    size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                    salt=0x5A17,
                ),
            )
            + Op.POP(
                Op.CALL(
                    gas=Op.GAS,
                    address=Op.MLOAD(offset=0x240),
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
            + Op.STOP
            + Op.INVALID
            + Op.MSTORE(offset=0x0, value=Op.GAS)
            + Op.SSTORE(key=0x0, value=0xFFFF)
            + Op.SSTORE(key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS))
            + Op.STOP
            + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
            + Op.RETURN(offset=0x0, size=0x80)
            + Op.STOP
        ),
    )
    pre[callee_15] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.PUSH1[0x13]
            + Op.CODECOPY(dest_offset=0x100, offset=0x44, size=Op.DUP1)
            + Op.PUSH2[0x200]
            + Op.MSTORE
            + Op.PUSH1[0x21]
            + Op.CODECOPY(dest_offset=0x0, offset=0x57, size=Op.DUP1)
            + Op.PUSH2[0x220]
            + Op.MSTORE
            + Op.MSTORE(
                offset=0x240,
                value=Op.CREATE(
                    value=0x0,
                    offset=0x0,
                    size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                ),
            )
            + Op.POP(
                Op.CALL(
                    gas=Op.GAS,
                    address=Op.MLOAD(offset=0x240),
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
            + Op.STOP
            + Op.INVALID
            + Op.MSTORE(offset=0x0, value=Op.GAS)
            + Op.SSTORE(key=0x0, value=0xFFFF)
            + Op.SSTORE(key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS))
            + Op.STOP
            + Op.MSTORE(offset=0x0, value=Op.GAS)
            + Op.SSTORE(key=0x0, value=0xFFFF)
            + Op.SSTORE(key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS))
            + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
            + Op.RETURN(offset=0x0, size=0x80)
            + Op.STOP
        ),
    )
    pre[callee_16] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.PUSH1[0x13]
            + Op.CODECOPY(dest_offset=0x100, offset=0x47, size=Op.DUP1)
            + Op.PUSH2[0x200]
            + Op.MSTORE
            + Op.PUSH1[0x21]
            + Op.CODECOPY(dest_offset=0x0, offset=0x5A, size=Op.DUP1)
            + Op.PUSH2[0x220]
            + Op.MSTORE
            + Op.MSTORE(
                offset=0x240,
                value=Op.CREATE2(
                    value=0x0,
                    offset=0x0,
                    size=Op.ADD(0x100, Op.MLOAD(offset=0x200)),
                    salt=0x5A17,
                ),
            )
            + Op.POP(
                Op.CALL(
                    gas=Op.GAS,
                    address=Op.MLOAD(offset=0x240),
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x240))
            + Op.STOP
            + Op.INVALID
            + Op.MSTORE(offset=0x0, value=Op.GAS)
            + Op.SSTORE(key=0x0, value=0xFFFF)
            + Op.SSTORE(key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS))
            + Op.STOP
            + Op.MSTORE(offset=0x0, value=Op.GAS)
            + Op.SSTORE(key=0x0, value=0xFFFF)
            + Op.SSTORE(key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS))
            + Op.CODECOPY(dest_offset=0x0, offset=0x100, size=0x100)
            + Op.RETURN(offset=0x0, size=0x80)
            + Op.STOP
        ),
    )
    pre[callee_17] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.POP(
                Op.CALL(
                    gas=Op.GAS,
                    address=0xF126,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.CALL(
                gas=Op.GAS,
                address=0xF126,
                value=0x0,
                args_offset=0x0,
                args_size=0x0,
                ret_offset=0x0,
                ret_size=0x0,
            )
            + Op.STOP
        ),
    )
    pre[callee_18] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.MSTORE(offset=0x0, value=Op.GAS)
            + Op.SSTORE(key=0x0, value=0x2)
            + Op.MSTORE(
                offset=0x0,
                value=Op.SUB(Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x11),
            )
            + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
            + Op.MSTORE(offset=0x0, value=Op.GAS)
            + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
            + Op.MSTORE(
                offset=0x0,
                value=Op.SUB(Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x10),
            )
            + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
            + Op.STOP
        ),
        storage={0x60A7: 0xDEAD},
    )
    pre[callee_19] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=0xDEAD60A7)
            + Op.MSTORE(offset=0x0, value=0x600D)
            + Op.RETURN(offset=0x0, size=0x20)
            + Op.STOP
        ),
    )
    pre[callee_20] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=Op.SSTORE(key=0x0, value=0x600D) + Op.STOP,
        storage={0x0: 0xBAD},
    )
    pre[callee_21] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.MSTORE(offset=0x0, value=Op.SLOAD(key=0x60A7))
            + Op.SSTORE(key=0x0, value=0x600D)
            + Op.STOP
        ),
        storage={0x0: 0xBAD, 0x60A7: 0xDEAD},
    )
    pre[callee_22] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.MSTORE(offset=0x0, value=Op.GAS)
            + Op.SSTORE(key=0x0, value=0x60A7)
            + Op.MSTORE(offset=0x0, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS))
            + Op.JUMPI(pc=0x24, condition=Op.EQ(Op.SLOAD(key=0x1), 0x0))
            + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
            + Op.JUMP(pc=0x2B)
            + Op.JUMPDEST
            + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
            + Op.JUMPDEST
            + Op.STOP
        ),
    )
    pre[callee_23] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=0xDEAD)
            + Op.SELFDESTRUCT(address=0x0)
            + Op.STOP
        ),
    )
    pre[callee_24] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.POP(Op.SLOAD(key=0x0)) + Op.SELFDESTRUCT(address=0x0) + Op.STOP
        ),
        storage={0x0: 0xDEAD0060A7},
    )
    pre[callee_25] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.MSTORE(offset=0x0, value=Op.GAS)
            + Op.MSTORE(offset=0x20, value=Op.SLOAD(key=0x60A7))
            + Op.MSTORE(
                offset=0x0,
                value=Op.SUB(Op.SUB(Op.MLOAD(offset=0x0), Op.GAS), 0x13),
            )
            + Op.RETURN(offset=0x0, size=0x20)
            + Op.STOP
        ),
        storage={0x60A7: 0xDEAD},
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.POP(
                Op.CALL(
                    gas=Op.GAS,
                    address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x40,
                ),
            )
            + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
            + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x20))
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
        gas_limit=16777216,
        gas_price=10,
        nonce=0,
        value=100000,
        access_list=tx_access_list,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
