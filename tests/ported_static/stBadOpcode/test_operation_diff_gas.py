"""
Ori Pomerantz   qbzzt1@gmail.com.

Ported from:
tests/static/state_tests/stBadOpcode/operationDiffGasFiller.yml
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
    ["tests/static/state_tests/stBadOpcode/operationDiffGasFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        (
            "048071d300000000000000000000000000000000000000000000000000000000000000f200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000064",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000ca11"): Account(
                    code=Op.MSTORE(offset=0x0, value=0xDEADBEEF)
                    + Op.RETURN(offset=0x0, size=0x100)
                ),
                Address("0x0000000000000000000000000000000000c0de20"): Account(
                    code=Op.SHA3(offset=0x0, size=0xBEEF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de3b"): Account(
                    code=Op.PUSH2[0xCA11]
                    + Op.PUSH1[0x0]
                    + Op.DUP1
                    + Op.EXTCODESIZE(address=Op.DUP3)
                    + Op.SWAP3
                    + Op.EXTCODECOPY
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de51"): Account(
                    code=Op.MLOAD(offset=0xBEEF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de52"): Account(
                    code=Op.MSTORE(offset=0xBEEF, value=0xFF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de53"): Account(
                    code=Op.MSTORE8(offset=0xBEEF, value=0xFF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def0"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.CREATE(value=Op.DUP1, offset=0x0, size=0x200),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def1"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xCA11,
                        value=Op.DUP1,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def2"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xCA11,
                        value=Op.DUP1,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def4"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xCA11,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def5"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.CREATE2(
                            value=Op.DUP1, offset=0x0, size=0x200, salt=0x5A17
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0defa"): Account(
                    code=Op.STATICCALL(
                        gas=Op.GAS,
                        address=0xCA11,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 2700},
                    code=Op.CALLDATALOAD(offset=0x44)
                    + Op.CALLDATALOAD(offset=0x24)
                    + Op.ADD(Op.CALLDATALOAD(offset=0x4), 0xC0DE00)
                    + Op.PUSH1[0x0]
                    + Op.DUP1
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x1C, condition=Op.EQ)
                    + Op.POP
                    + Op.SSTORE(key=0x0, value=Op.SUB)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.DUP4
                    + Op.CALL(
                        gas=Op.DUP10,
                        address=Op.DUP8,
                        value=Op.DUP1,
                        args_offset=Op.DUP1,
                        args_size=Op.DUP1,
                        ret_offset=Op.DUP1,
                        ret_size=Op.DUP2,
                    )
                    + Op.SWAP4
                    + Op.ADD
                    + Op.SWAP3
                    + Op.JUMP(pc=0x11),
                ),
            },
        ),
        (
            "048071d300000000000000000000000000000000000000000000000000000000000000f100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000064",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000ca11"): Account(
                    code=Op.MSTORE(offset=0x0, value=0xDEADBEEF)
                    + Op.RETURN(offset=0x0, size=0x100)
                ),
                Address("0x0000000000000000000000000000000000c0de20"): Account(
                    code=Op.SHA3(offset=0x0, size=0xBEEF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de3b"): Account(
                    code=Op.PUSH2[0xCA11]
                    + Op.PUSH1[0x0]
                    + Op.DUP1
                    + Op.EXTCODESIZE(address=Op.DUP3)
                    + Op.SWAP3
                    + Op.EXTCODECOPY
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de51"): Account(
                    code=Op.MLOAD(offset=0xBEEF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de52"): Account(
                    code=Op.MSTORE(offset=0xBEEF, value=0xFF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de53"): Account(
                    code=Op.MSTORE8(offset=0xBEEF, value=0xFF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def0"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.CREATE(value=Op.DUP1, offset=0x0, size=0x200),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def1"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xCA11,
                        value=Op.DUP1,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def2"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xCA11,
                        value=Op.DUP1,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def4"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xCA11,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def5"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.CREATE2(
                            value=Op.DUP1, offset=0x0, size=0x200, salt=0x5A17
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0defa"): Account(
                    code=Op.STATICCALL(
                        gas=Op.GAS,
                        address=0xCA11,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 2700},
                    code=Op.CALLDATALOAD(offset=0x44)
                    + Op.CALLDATALOAD(offset=0x24)
                    + Op.ADD(Op.CALLDATALOAD(offset=0x4), 0xC0DE00)
                    + Op.PUSH1[0x0]
                    + Op.DUP1
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x1C, condition=Op.EQ)
                    + Op.POP
                    + Op.SSTORE(key=0x0, value=Op.SUB)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.DUP4
                    + Op.CALL(
                        gas=Op.DUP10,
                        address=Op.DUP8,
                        value=Op.DUP1,
                        args_offset=Op.DUP1,
                        args_size=Op.DUP1,
                        ret_offset=Op.DUP1,
                        ret_size=Op.DUP2,
                    )
                    + Op.SWAP4
                    + Op.ADD
                    + Op.SWAP3
                    + Op.JUMP(pc=0x11),
                ),
            },
        ),
        (
            "048071d300000000000000000000000000000000000000000000000000000000000000f500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000064",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000ca11"): Account(
                    code=Op.MSTORE(offset=0x0, value=0xDEADBEEF)
                    + Op.RETURN(offset=0x0, size=0x100)
                ),
                Address("0x0000000000000000000000000000000000c0de20"): Account(
                    code=Op.SHA3(offset=0x0, size=0xBEEF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de3b"): Account(
                    code=Op.PUSH2[0xCA11]
                    + Op.PUSH1[0x0]
                    + Op.DUP1
                    + Op.EXTCODESIZE(address=Op.DUP3)
                    + Op.SWAP3
                    + Op.EXTCODECOPY
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de51"): Account(
                    code=Op.MLOAD(offset=0xBEEF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de52"): Account(
                    code=Op.MSTORE(offset=0xBEEF, value=0xFF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de53"): Account(
                    code=Op.MSTORE8(offset=0xBEEF, value=0xFF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def0"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.CREATE(value=Op.DUP1, offset=0x0, size=0x200),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def1"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xCA11,
                        value=Op.DUP1,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def2"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xCA11,
                        value=Op.DUP1,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def4"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xCA11,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def5"): Account(
                    storage={0: 0x1C1BD7A2F25CA2F4577AD12388656BC147F96DAB},
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.CREATE2(
                            value=Op.DUP1, offset=0x0, size=0x200, salt=0x5A17
                        ),
                    )
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000c0defa"): Account(
                    code=Op.STATICCALL(
                        gas=Op.GAS,
                        address=0xCA11,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 54300},
                    code=Op.CALLDATALOAD(offset=0x44)
                    + Op.CALLDATALOAD(offset=0x24)
                    + Op.ADD(Op.CALLDATALOAD(offset=0x4), 0xC0DE00)
                    + Op.PUSH1[0x0]
                    + Op.DUP1
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x1C, condition=Op.EQ)
                    + Op.POP
                    + Op.SSTORE(key=0x0, value=Op.SUB)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.DUP4
                    + Op.CALL(
                        gas=Op.DUP10,
                        address=Op.DUP8,
                        value=Op.DUP1,
                        args_offset=Op.DUP1,
                        args_size=Op.DUP1,
                        ret_offset=Op.DUP1,
                        ret_size=Op.DUP2,
                    )
                    + Op.SWAP4
                    + Op.ADD
                    + Op.SWAP3
                    + Op.JUMP(pc=0x11),
                ),
            },
        ),
        (
            "048071d300000000000000000000000000000000000000000000000000000000000000f000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000064",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000ca11"): Account(
                    code=Op.MSTORE(offset=0x0, value=0xDEADBEEF)
                    + Op.RETURN(offset=0x0, size=0x100)
                ),
                Address("0x0000000000000000000000000000000000c0de20"): Account(
                    code=Op.SHA3(offset=0x0, size=0xBEEF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de3b"): Account(
                    code=Op.PUSH2[0xCA11]
                    + Op.PUSH1[0x0]
                    + Op.DUP1
                    + Op.EXTCODESIZE(address=Op.DUP3)
                    + Op.SWAP3
                    + Op.EXTCODECOPY
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de51"): Account(
                    code=Op.MLOAD(offset=0xBEEF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de52"): Account(
                    code=Op.MSTORE(offset=0xBEEF, value=0xFF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de53"): Account(
                    code=Op.MSTORE8(offset=0xBEEF, value=0xFF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def0"): Account(
                    storage={0: 0xB44F2C88D3D4283CD1E54E418C4FF7E6A6C73202},
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.CREATE(value=Op.DUP1, offset=0x0, size=0x200),
                    )
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000c0def1"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xCA11,
                        value=Op.DUP1,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def2"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xCA11,
                        value=Op.DUP1,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def4"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xCA11,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def5"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.CREATE2(
                            value=Op.DUP1, offset=0x0, size=0x200, salt=0x5A17
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0defa"): Account(
                    code=Op.STATICCALL(
                        gas=Op.GAS,
                        address=0xCA11,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 54200},
                    code=Op.CALLDATALOAD(offset=0x44)
                    + Op.CALLDATALOAD(offset=0x24)
                    + Op.ADD(Op.CALLDATALOAD(offset=0x4), 0xC0DE00)
                    + Op.PUSH1[0x0]
                    + Op.DUP1
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x1C, condition=Op.EQ)
                    + Op.POP
                    + Op.SSTORE(key=0x0, value=Op.SUB)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.DUP4
                    + Op.CALL(
                        gas=Op.DUP10,
                        address=Op.DUP8,
                        value=Op.DUP1,
                        args_offset=Op.DUP1,
                        args_size=Op.DUP1,
                        ret_offset=Op.DUP1,
                        ret_size=Op.DUP2,
                    )
                    + Op.SWAP4
                    + Op.ADD
                    + Op.SWAP3
                    + Op.JUMP(pc=0x11),
                ),
            },
        ),
        (
            "048071d300000000000000000000000000000000000000000000000000000000000000f400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000064",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000ca11"): Account(
                    code=Op.MSTORE(offset=0x0, value=0xDEADBEEF)
                    + Op.RETURN(offset=0x0, size=0x100)
                ),
                Address("0x0000000000000000000000000000000000c0de20"): Account(
                    code=Op.SHA3(offset=0x0, size=0xBEEF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de3b"): Account(
                    code=Op.PUSH2[0xCA11]
                    + Op.PUSH1[0x0]
                    + Op.DUP1
                    + Op.EXTCODESIZE(address=Op.DUP3)
                    + Op.SWAP3
                    + Op.EXTCODECOPY
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de51"): Account(
                    code=Op.MLOAD(offset=0xBEEF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de52"): Account(
                    code=Op.MSTORE(offset=0xBEEF, value=0xFF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de53"): Account(
                    code=Op.MSTORE8(offset=0xBEEF, value=0xFF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def0"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.CREATE(value=Op.DUP1, offset=0x0, size=0x200),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def1"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xCA11,
                        value=Op.DUP1,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def2"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xCA11,
                        value=Op.DUP1,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def4"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xCA11,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def5"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.CREATE2(
                            value=Op.DUP1, offset=0x0, size=0x200, salt=0x5A17
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0defa"): Account(
                    code=Op.STATICCALL(
                        gas=Op.GAS,
                        address=0xCA11,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 2700},
                    code=Op.CALLDATALOAD(offset=0x44)
                    + Op.CALLDATALOAD(offset=0x24)
                    + Op.ADD(Op.CALLDATALOAD(offset=0x4), 0xC0DE00)
                    + Op.PUSH1[0x0]
                    + Op.DUP1
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x1C, condition=Op.EQ)
                    + Op.POP
                    + Op.SSTORE(key=0x0, value=Op.SUB)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.DUP4
                    + Op.CALL(
                        gas=Op.DUP10,
                        address=Op.DUP8,
                        value=Op.DUP1,
                        args_offset=Op.DUP1,
                        args_size=Op.DUP1,
                        ret_offset=Op.DUP1,
                        ret_size=Op.DUP2,
                    )
                    + Op.SWAP4
                    + Op.ADD
                    + Op.SWAP3
                    + Op.JUMP(pc=0x11),
                ),
            },
        ),
        (
            "048071d3000000000000000000000000000000000000000000000000000000000000003b00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000064",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000ca11"): Account(
                    code=Op.MSTORE(offset=0x0, value=0xDEADBEEF)
                    + Op.RETURN(offset=0x0, size=0x100)
                ),
                Address("0x0000000000000000000000000000000000c0de20"): Account(
                    code=Op.SHA3(offset=0x0, size=0xBEEF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de3b"): Account(
                    code=Op.PUSH2[0xCA11]
                    + Op.PUSH1[0x0]
                    + Op.DUP1
                    + Op.EXTCODESIZE(address=Op.DUP3)
                    + Op.SWAP3
                    + Op.EXTCODECOPY
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de51"): Account(
                    code=Op.MLOAD(offset=0xBEEF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de52"): Account(
                    code=Op.MSTORE(offset=0xBEEF, value=0xFF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de53"): Account(
                    code=Op.MSTORE8(offset=0xBEEF, value=0xFF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def0"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.CREATE(value=Op.DUP1, offset=0x0, size=0x200),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def1"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xCA11,
                        value=Op.DUP1,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def2"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xCA11,
                        value=Op.DUP1,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def4"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xCA11,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def5"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.CREATE2(
                            value=Op.DUP1, offset=0x0, size=0x200, salt=0x5A17
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0defa"): Account(
                    code=Op.STATICCALL(
                        gas=Op.GAS,
                        address=0xCA11,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 2800},
                    code=Op.CALLDATALOAD(offset=0x44)
                    + Op.CALLDATALOAD(offset=0x24)
                    + Op.ADD(Op.CALLDATALOAD(offset=0x4), 0xC0DE00)
                    + Op.PUSH1[0x0]
                    + Op.DUP1
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x1C, condition=Op.EQ)
                    + Op.POP
                    + Op.SSTORE(key=0x0, value=Op.SUB)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.DUP4
                    + Op.CALL(
                        gas=Op.DUP10,
                        address=Op.DUP8,
                        value=Op.DUP1,
                        args_offset=Op.DUP1,
                        args_size=Op.DUP1,
                        ret_offset=Op.DUP1,
                        ret_size=Op.DUP2,
                    )
                    + Op.SWAP4
                    + Op.ADD
                    + Op.SWAP3
                    + Op.JUMP(pc=0x11),
                ),
            },
        ),
        (
            "048071d3000000000000000000000000000000000000000000000000000000000000005100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000064",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000ca11"): Account(
                    code=Op.MSTORE(offset=0x0, value=0xDEADBEEF)
                    + Op.RETURN(offset=0x0, size=0x100)
                ),
                Address("0x0000000000000000000000000000000000c0de20"): Account(
                    code=Op.SHA3(offset=0x0, size=0xBEEF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de3b"): Account(
                    code=Op.PUSH2[0xCA11]
                    + Op.PUSH1[0x0]
                    + Op.DUP1
                    + Op.EXTCODESIZE(address=Op.DUP3)
                    + Op.SWAP3
                    + Op.EXTCODECOPY
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de51"): Account(
                    code=Op.MLOAD(offset=0xBEEF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de52"): Account(
                    code=Op.MSTORE(offset=0xBEEF, value=0xFF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de53"): Account(
                    code=Op.MSTORE8(offset=0xBEEF, value=0xFF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def0"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.CREATE(value=Op.DUP1, offset=0x0, size=0x200),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def1"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xCA11,
                        value=Op.DUP1,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def2"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xCA11,
                        value=Op.DUP1,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def4"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xCA11,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def5"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.CREATE2(
                            value=Op.DUP1, offset=0x0, size=0x200, salt=0x5A17
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0defa"): Account(
                    code=Op.STATICCALL(
                        gas=Op.GAS,
                        address=0xCA11,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 9200},
                    code=Op.CALLDATALOAD(offset=0x44)
                    + Op.CALLDATALOAD(offset=0x24)
                    + Op.ADD(Op.CALLDATALOAD(offset=0x4), 0xC0DE00)
                    + Op.PUSH1[0x0]
                    + Op.DUP1
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x1C, condition=Op.EQ)
                    + Op.POP
                    + Op.SSTORE(key=0x0, value=Op.SUB)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.DUP4
                    + Op.CALL(
                        gas=Op.DUP10,
                        address=Op.DUP8,
                        value=Op.DUP1,
                        args_offset=Op.DUP1,
                        args_size=Op.DUP1,
                        ret_offset=Op.DUP1,
                        ret_size=Op.DUP2,
                    )
                    + Op.SWAP4
                    + Op.ADD
                    + Op.SWAP3
                    + Op.JUMP(pc=0x11),
                ),
            },
        ),
        (
            "048071d3000000000000000000000000000000000000000000000000000000000000005300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000064",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000ca11"): Account(
                    code=Op.MSTORE(offset=0x0, value=0xDEADBEEF)
                    + Op.RETURN(offset=0x0, size=0x100)
                ),
                Address("0x0000000000000000000000000000000000c0de20"): Account(
                    code=Op.SHA3(offset=0x0, size=0xBEEF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de3b"): Account(
                    code=Op.PUSH2[0xCA11]
                    + Op.PUSH1[0x0]
                    + Op.DUP1
                    + Op.EXTCODESIZE(address=Op.DUP3)
                    + Op.SWAP3
                    + Op.EXTCODECOPY
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de51"): Account(
                    code=Op.MLOAD(offset=0xBEEF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de52"): Account(
                    code=Op.MSTORE(offset=0xBEEF, value=0xFF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de53"): Account(
                    code=Op.MSTORE8(offset=0xBEEF, value=0xFF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def0"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.CREATE(value=Op.DUP1, offset=0x0, size=0x200),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def1"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xCA11,
                        value=Op.DUP1,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def2"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xCA11,
                        value=Op.DUP1,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def4"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xCA11,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def5"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.CREATE2(
                            value=Op.DUP1, offset=0x0, size=0x200, salt=0x5A17
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0defa"): Account(
                    code=Op.STATICCALL(
                        gas=Op.GAS,
                        address=0xCA11,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 9200},
                    code=Op.CALLDATALOAD(offset=0x44)
                    + Op.CALLDATALOAD(offset=0x24)
                    + Op.ADD(Op.CALLDATALOAD(offset=0x4), 0xC0DE00)
                    + Op.PUSH1[0x0]
                    + Op.DUP1
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x1C, condition=Op.EQ)
                    + Op.POP
                    + Op.SSTORE(key=0x0, value=Op.SUB)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.DUP4
                    + Op.CALL(
                        gas=Op.DUP10,
                        address=Op.DUP8,
                        value=Op.DUP1,
                        args_offset=Op.DUP1,
                        args_size=Op.DUP1,
                        ret_offset=Op.DUP1,
                        ret_size=Op.DUP2,
                    )
                    + Op.SWAP4
                    + Op.ADD
                    + Op.SWAP3
                    + Op.JUMP(pc=0x11),
                ),
            },
        ),
        (
            "048071d3000000000000000000000000000000000000000000000000000000000000005200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000064",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000ca11"): Account(
                    code=Op.MSTORE(offset=0x0, value=0xDEADBEEF)
                    + Op.RETURN(offset=0x0, size=0x100)
                ),
                Address("0x0000000000000000000000000000000000c0de20"): Account(
                    code=Op.SHA3(offset=0x0, size=0xBEEF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de3b"): Account(
                    code=Op.PUSH2[0xCA11]
                    + Op.PUSH1[0x0]
                    + Op.DUP1
                    + Op.EXTCODESIZE(address=Op.DUP3)
                    + Op.SWAP3
                    + Op.EXTCODECOPY
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de51"): Account(
                    code=Op.MLOAD(offset=0xBEEF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de52"): Account(
                    code=Op.MSTORE(offset=0xBEEF, value=0xFF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de53"): Account(
                    code=Op.MSTORE8(offset=0xBEEF, value=0xFF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def0"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.CREATE(value=Op.DUP1, offset=0x0, size=0x200),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def1"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xCA11,
                        value=Op.DUP1,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def2"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xCA11,
                        value=Op.DUP1,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def4"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xCA11,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def5"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.CREATE2(
                            value=Op.DUP1, offset=0x0, size=0x200, salt=0x5A17
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0defa"): Account(
                    code=Op.STATICCALL(
                        gas=Op.GAS,
                        address=0xCA11,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 9200},
                    code=Op.CALLDATALOAD(offset=0x44)
                    + Op.CALLDATALOAD(offset=0x24)
                    + Op.ADD(Op.CALLDATALOAD(offset=0x4), 0xC0DE00)
                    + Op.PUSH1[0x0]
                    + Op.DUP1
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x1C, condition=Op.EQ)
                    + Op.POP
                    + Op.SSTORE(key=0x0, value=Op.SUB)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.DUP4
                    + Op.CALL(
                        gas=Op.DUP10,
                        address=Op.DUP8,
                        value=Op.DUP1,
                        args_offset=Op.DUP1,
                        args_size=Op.DUP1,
                        ret_offset=Op.DUP1,
                        ret_size=Op.DUP2,
                    )
                    + Op.SWAP4
                    + Op.ADD
                    + Op.SWAP3
                    + Op.JUMP(pc=0x11),
                ),
            },
        ),
        (
            "048071d3000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000064",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000ca11"): Account(
                    code=Op.MSTORE(offset=0x0, value=0xDEADBEEF)
                    + Op.RETURN(offset=0x0, size=0x100)
                ),
                Address("0x0000000000000000000000000000000000c0de20"): Account(
                    code=Op.SHA3(offset=0x0, size=0xBEEF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de3b"): Account(
                    code=Op.PUSH2[0xCA11]
                    + Op.PUSH1[0x0]
                    + Op.DUP1
                    + Op.EXTCODESIZE(address=Op.DUP3)
                    + Op.SWAP3
                    + Op.EXTCODECOPY
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de51"): Account(
                    code=Op.MLOAD(offset=0xBEEF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de52"): Account(
                    code=Op.MSTORE(offset=0xBEEF, value=0xFF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de53"): Account(
                    code=Op.MSTORE8(offset=0xBEEF, value=0xFF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def0"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.CREATE(value=Op.DUP1, offset=0x0, size=0x200),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def1"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xCA11,
                        value=Op.DUP1,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def2"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xCA11,
                        value=Op.DUP1,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def4"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xCA11,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def5"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.CREATE2(
                            value=Op.DUP1, offset=0x0, size=0x200, salt=0x5A17
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0defa"): Account(
                    code=Op.STATICCALL(
                        gas=Op.GAS,
                        address=0xCA11,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 18400},
                    code=Op.CALLDATALOAD(offset=0x44)
                    + Op.CALLDATALOAD(offset=0x24)
                    + Op.ADD(Op.CALLDATALOAD(offset=0x4), 0xC0DE00)
                    + Op.PUSH1[0x0]
                    + Op.DUP1
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x1C, condition=Op.EQ)
                    + Op.POP
                    + Op.SSTORE(key=0x0, value=Op.SUB)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.DUP4
                    + Op.CALL(
                        gas=Op.DUP10,
                        address=Op.DUP8,
                        value=Op.DUP1,
                        args_offset=Op.DUP1,
                        args_size=Op.DUP1,
                        ret_offset=Op.DUP1,
                        ret_size=Op.DUP2,
                    )
                    + Op.SWAP4
                    + Op.ADD
                    + Op.SWAP3
                    + Op.JUMP(pc=0x11),
                ),
            },
        ),
        (
            "048071d300000000000000000000000000000000000000000000000000000000000000fa00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000064",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000ca11"): Account(
                    code=Op.MSTORE(offset=0x0, value=0xDEADBEEF)
                    + Op.RETURN(offset=0x0, size=0x100)
                ),
                Address("0x0000000000000000000000000000000000c0de20"): Account(
                    code=Op.SHA3(offset=0x0, size=0xBEEF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de3b"): Account(
                    code=Op.PUSH2[0xCA11]
                    + Op.PUSH1[0x0]
                    + Op.DUP1
                    + Op.EXTCODESIZE(address=Op.DUP3)
                    + Op.SWAP3
                    + Op.EXTCODECOPY
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de51"): Account(
                    code=Op.MLOAD(offset=0xBEEF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de52"): Account(
                    code=Op.MSTORE(offset=0xBEEF, value=0xFF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0de53"): Account(
                    code=Op.MSTORE8(offset=0xBEEF, value=0xFF) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def0"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.CREATE(value=Op.DUP1, offset=0x0, size=0x200),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def1"): Account(
                    code=Op.CALL(
                        gas=Op.GAS,
                        address=0xCA11,
                        value=Op.DUP1,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def2"): Account(
                    code=Op.CALLCODE(
                        gas=Op.GAS,
                        address=0xCA11,
                        value=Op.DUP1,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def4"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=0xCA11,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0def5"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.CREATE2(
                            value=Op.DUP1, offset=0x0, size=0x200, salt=0x5A17
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000c0defa"): Account(
                    code=Op.STATICCALL(
                        gas=Op.GAS,
                        address=0xCA11,
                        args_offset=Op.DUP2,
                        args_size=Op.DUP2,
                        ret_offset=0x0,
                        ret_size=0x100,
                    )
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 2700},
                    code=Op.CALLDATALOAD(offset=0x44)
                    + Op.CALLDATALOAD(offset=0x24)
                    + Op.ADD(Op.CALLDATALOAD(offset=0x4), 0xC0DE00)
                    + Op.PUSH1[0x0]
                    + Op.DUP1
                    + Op.JUMPDEST
                    + Op.JUMPI(pc=0x1C, condition=Op.EQ)
                    + Op.POP
                    + Op.SSTORE(key=0x0, value=Op.SUB)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.PUSH1[0x0]
                    + Op.DUP4
                    + Op.CALL(
                        gas=Op.DUP10,
                        address=Op.DUP8,
                        value=Op.DUP1,
                        args_offset=Op.DUP1,
                        args_size=Op.DUP1,
                        ret_offset=Op.DUP1,
                        ret_size=Op.DUP2,
                    )
                    + Op.SWAP4
                    + Op.ADD
                    + Op.SWAP3
                    + Op.JUMP(pc=0x11),
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
    ],
)
@pytest.mark.pre_alloc_mutable
def test_operation_diff_gas(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Ori Pomerantz   qbzzt1@gmail.com."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xcccccccccccccccccccccccccccccccccccccccc")
    callee = Address("0x000000000000000000000000000000000000ca11")
    callee_1 = Address("0x0000000000000000000000000000000000c0de20")
    callee_2 = Address("0x0000000000000000000000000000000000c0de3b")
    callee_3 = Address("0x0000000000000000000000000000000000c0de51")
    callee_4 = Address("0x0000000000000000000000000000000000c0de52")
    callee_5 = Address("0x0000000000000000000000000000000000c0de53")
    callee_6 = Address("0x0000000000000000000000000000000000c0def0")
    callee_7 = Address("0x0000000000000000000000000000000000c0def1")
    callee_8 = Address("0x0000000000000000000000000000000000c0def2")
    callee_9 = Address("0x0000000000000000000000000000000000c0def4")
    callee_10 = Address("0x0000000000000000000000000000000000c0def5")
    callee_11 = Address("0x0000000000000000000000000000000000c0defa")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000,
    )

    # Source: Yul
    # {
    #    mstore(0, 0xDEADBEEF)
    #    return(0, 0x100)
    # }
    pre[callee] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=(
            Op.MSTORE(offset=0x0, value=0xDEADBEEF)
            + Op.RETURN(offset=0x0, size=0x100)
        ),
    )
    # Source: Yul
    # {
    #    let useless := keccak256(0,0xBEEF)
    # }
    pre[callee_1] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=Op.SHA3(offset=0x0, size=0xBEEF) + Op.STOP,
    )
    # Source: Yul
    # {
    #   let addr := 0xCA11
    #   extcodecopy(addr, 0, 0, extcodesize(addr))
    # }
    pre[callee_2] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=(
            Op.PUSH2[0xCA11]
            + Op.PUSH1[0x0]
            + Op.DUP1
            + Op.EXTCODESIZE(address=Op.DUP3)
            + Op.SWAP3
            + Op.EXTCODECOPY
            + Op.STOP
        ),
    )
    # Source: Yul
    # {
    #    let useless := mload(0xBEEF)
    # }
    pre[callee_3] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=Op.MLOAD(offset=0xBEEF) + Op.STOP,
    )
    # Source: Yul
    # {
    #    mstore(0xBEEF, 0xFF)
    # }
    pre[callee_4] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=Op.MSTORE(offset=0xBEEF, value=0xFF) + Op.STOP,
    )
    # Source: Yul
    # {
    #    mstore8(0xBEEF, 0xFF)
    # }
    pre[callee_5] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=Op.MSTORE8(offset=0xBEEF, value=0xFF) + Op.STOP,
    )
    # Source: Yul
    # {
    #    sstore(0,create(0, 0, 0x200))
    # }
    pre[callee_6] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=(
            Op.SSTORE(
                key=0x0,
                value=Op.CREATE(value=Op.DUP1, offset=0x0, size=0x200),
            )
            + Op.STOP
        ),
    )
    # Source: Yul
    # {
    #    let retval := call(gas(), 0xCA11, 0, 0, 0x100, 0, 0x100)
    # }
    pre[callee_7] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=(
            Op.CALL(
                gas=Op.GAS,
                address=0xCA11,
                value=Op.DUP1,
                args_offset=Op.DUP2,
                args_size=Op.DUP2,
                ret_offset=0x0,
                ret_size=0x100,
            )
            + Op.STOP
        ),
    )
    # Source: Yul
    # {
    #    let retval := callcode(gas(), 0xCA11, 0, 0, 0x100, 0, 0x100)
    # }
    pre[callee_8] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=(
            Op.CALLCODE(
                gas=Op.GAS,
                address=0xCA11,
                value=Op.DUP1,
                args_offset=Op.DUP2,
                args_size=Op.DUP2,
                ret_offset=0x0,
                ret_size=0x100,
            )
            + Op.STOP
        ),
    )
    # Source: Yul
    # {
    #    let retval := delegatecall(gas(), 0xCA11, 0, 0x100, 0, 0x100)
    # }
    pre[callee_9] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=(
            Op.DELEGATECALL(
                gas=Op.GAS,
                address=0xCA11,
                args_offset=Op.DUP2,
                args_size=Op.DUP2,
                ret_offset=0x0,
                ret_size=0x100,
            )
            + Op.STOP
        ),
    )
    # Source: Yul
    # {
    #    sstore(0,create2(0, 0, 0x200, 0x5A17))
    # }
    pre[callee_10] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=(
            Op.SSTORE(
                key=0x0,
                value=Op.CREATE2(
                    value=Op.DUP1,
                    offset=0x0,
                    size=0x200,
                    salt=0x5A17,
                ),
            )
            + Op.STOP
        ),
    )
    # Source: Yul
    # {
    #    let retval := staticcall(gas(), 0xCA11, 0, 0x100, 0, 0x100)
    # }
    pre[callee_11] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=(
            Op.STATICCALL(
                gas=Op.GAS,
                address=0xCA11,
                args_offset=Op.DUP2,
                args_size=Op.DUP2,
                ret_offset=0x0,
                ret_size=0x100,
            )
            + Op.STOP
        ),
    )
    pre[sender] = Account(balance=0xBA1A9CE0BA1A9CE, nonce=1)
    # Source: Yul
    # {
    #   // Run the operation with gasAmt, gasAmt+gasDiff, gasAmt+2*gasDiff, etc.  # noqa: E501
    #   let gasAmt := calldataload(0x24)
    #   let gasDiff := calldataload(0x44)
    #   let addr := add(0xC0DE00, calldataload(0x04))
    #   let result := 0
    #
    #   for { } eq(result, 0) { } {     // Until the operation is successful
    #      result := call(gasAmt, addr, 0, 0, 0, 0, 0)
    #      gasAmt := add(gasAmt, gasDiff)
    #   }
    #   sstore(0, sub(gasAmt, gasDiff))
    # }
    pre[contract] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=(
            Op.CALLDATALOAD(offset=0x44)
            + Op.CALLDATALOAD(offset=0x24)
            + Op.ADD(Op.CALLDATALOAD(offset=0x4), 0xC0DE00)
            + Op.PUSH1[0x0]
            + Op.DUP1
            + Op.JUMPDEST
            + Op.JUMPI(pc=0x1C, condition=Op.EQ)
            + Op.POP
            + Op.SSTORE(key=0x0, value=Op.SUB)
            + Op.STOP
            + Op.JUMPDEST
            + Op.PUSH1[0x0]
            + Op.DUP4
            + Op.CALL(
                gas=Op.DUP10,
                address=Op.DUP8,
                value=Op.DUP1,
                args_offset=Op.DUP1,
                args_size=Op.DUP1,
                ret_offset=Op.DUP1,
                ret_size=Op.DUP2,
            )
            + Op.SWAP4
            + Op.ADD
            + Op.SWAP3
            + Op.JUMP(pc=0x11)
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
        nonce=1,
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
