"""
create contract A in a subcall. go OOG in a subcall (revert happens) check...

Ported from:
tests/static/state_tests/stExtCodeHash/extCodeHashSubcallOOGFiller.yml
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
    ["tests/static/state_tests/stExtCodeHash/extCodeHashSubcallOOGFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        (
            "0000000000000000000000002000000000000000000000000000000000000000",
            {
                Address("0x1000000000000000000000000000000000000000"): Account(
                    storage={
                        1: 0x9FF1F274B33E3B56EDD7734520CBCDF2699FC1DC78B51644CDC56CA65BEBEEAE,  # noqa: E501
                        2: 5,
                        3: 0x6020602055000000000000000000000000000000000000000000000000000000,  # noqa: E501
                        4: 1,
                    },
                    code=Op.POP(
                        Op.CALLCODE(
                            gas=0x55730,
                            address=Op.CALLDATALOAD(offset=0x0),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(
                        key=0x1,
                        value=Op.EXTCODEHASH(address=Op.MLOAD(offset=0x0)),
                    )
                    + Op.SSTORE(
                        key=0x2,
                        value=Op.EXTCODESIZE(address=Op.MLOAD(offset=0x0)),
                    )
                    + Op.EXTCODECOPY(
                        address=Op.MLOAD(offset=0x0),
                        dest_offset=0x0,
                        offset=0x0,
                        size=0x20,
                    )
                    + Op.SSTORE(key=0x3, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(
                        key=0x4,
                        value=Op.CALLCODE(
                            gas=0xC350,
                            address=Op.MLOAD(offset=0x0),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.STOP,
                ),
                Address("0x2000000000000000000000000000000000000000"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=0x249F0,
                            address=0xA000000000000000000000000000000000000000,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x2100000000000000000000000000000000000000"): Account(
                    code=Op.POP(
                        Op.CALLCODE(
                            gas=0x249F0,
                            address=0xA000000000000000000000000000000000000000,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x2200000000000000000000000000000000000000"): Account(
                    code=Op.POP(
                        Op.DELEGATECALL(
                            gas=0x249F0,
                            address=0xA000000000000000000000000000000000000000,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x3000000000000000000000000000000000000000"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=0x249F0,
                            address=0xA100000000000000000000000000000000000000,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x3100000000000000000000000000000000000000"): Account(
                    code=Op.POP(
                        Op.CALLCODE(
                            gas=0x3D090,
                            address=0xA100000000000000000000000000000000000000,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x3200000000000000000000000000000000000000"): Account(
                    code=Op.POP(
                        Op.DELEGATECALL(
                            gas=0x249F0,
                            address=0xA100000000000000000000000000000000000000,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0xa000000000000000000000000000000000000000"): Account(
                    code=Op.PUSH1[0x0]
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x1A, size=Op.DUP1)
                    + Op.PUSH1[0x0]
                    + Op.PUSH1[0x0]
                    + Op.MSTORE(offset=0x0, value=Op.CREATE2)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=0x6020602055)
                    + Op.RETURN(offset=0x1B, size=0x5)
                    + Op.STOP
                ),
                Address("0xa100000000000000000000000000000000000000"): Account(
                    code=Op.PUSH1[0x0]
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x60, size=Op.DUP1)
                    + Op.PUSH1[0x0]
                    + Op.PUSH1[0x0]
                    + Op.MSTORE(offset=0x0, value=Op.CREATE2)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x2, value=0x1)
                    + Op.SSTORE(key=0x3, value=0x1)
                    + Op.SSTORE(key=0x4, value=0x1)
                    + Op.SSTORE(key=0x5, value=0x1)
                    + Op.SSTORE(key=0x6, value=0x1)
                    + Op.SSTORE(key=0x7, value=0x1)
                    + Op.SSTORE(key=0x8, value=0x1)
                    + Op.SSTORE(key=0x9, value=0x1)
                    + Op.SSTORE(key=0xA, value=0x1)
                    + Op.SSTORE(key=0xB, value=0x1)
                    + Op.SSTORE(key=0xC, value=0x1)
                    + Op.SSTORE(key=0xD, value=0x1)
                    + Op.SSTORE(key=0xE, value=0x1)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=0x6020602055)
                    + Op.RETURN(offset=0x1B, size=0x5)
                    + Op.STOP
                ),
                Address("0xefd05436d647298d0c6a6cc2f41f5b3461688690"): Account(
                    code=Op.SSTORE(key=0x20, value=0x20)
                ),
            },
        ),
        (
            "0000000000000000000000002100000000000000000000000000000000000000",
            {
                Address("0x1000000000000000000000000000000000000000"): Account(
                    storage={
                        1: 0x9FF1F274B33E3B56EDD7734520CBCDF2699FC1DC78B51644CDC56CA65BEBEEAE,  # noqa: E501
                        2: 5,
                        3: 0x6020602055000000000000000000000000000000000000000000000000000000,  # noqa: E501
                        4: 1,
                    },
                    code=Op.POP(
                        Op.CALLCODE(
                            gas=0x55730,
                            address=Op.CALLDATALOAD(offset=0x0),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(
                        key=0x1,
                        value=Op.EXTCODEHASH(address=Op.MLOAD(offset=0x0)),
                    )
                    + Op.SSTORE(
                        key=0x2,
                        value=Op.EXTCODESIZE(address=Op.MLOAD(offset=0x0)),
                    )
                    + Op.EXTCODECOPY(
                        address=Op.MLOAD(offset=0x0),
                        dest_offset=0x0,
                        offset=0x0,
                        size=0x20,
                    )
                    + Op.SSTORE(key=0x3, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(
                        key=0x4,
                        value=Op.CALLCODE(
                            gas=0xC350,
                            address=Op.MLOAD(offset=0x0),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.STOP,
                ),
                Address("0x2000000000000000000000000000000000000000"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=0x249F0,
                            address=0xA000000000000000000000000000000000000000,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x2100000000000000000000000000000000000000"): Account(
                    code=Op.POP(
                        Op.CALLCODE(
                            gas=0x249F0,
                            address=0xA000000000000000000000000000000000000000,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x2200000000000000000000000000000000000000"): Account(
                    code=Op.POP(
                        Op.DELEGATECALL(
                            gas=0x249F0,
                            address=0xA000000000000000000000000000000000000000,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x3000000000000000000000000000000000000000"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=0x249F0,
                            address=0xA100000000000000000000000000000000000000,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x3100000000000000000000000000000000000000"): Account(
                    code=Op.POP(
                        Op.CALLCODE(
                            gas=0x3D090,
                            address=0xA100000000000000000000000000000000000000,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x3200000000000000000000000000000000000000"): Account(
                    code=Op.POP(
                        Op.DELEGATECALL(
                            gas=0x249F0,
                            address=0xA100000000000000000000000000000000000000,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0xa000000000000000000000000000000000000000"): Account(
                    code=Op.PUSH1[0x0]
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x1A, size=Op.DUP1)
                    + Op.PUSH1[0x0]
                    + Op.PUSH1[0x0]
                    + Op.MSTORE(offset=0x0, value=Op.CREATE2)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=0x6020602055)
                    + Op.RETURN(offset=0x1B, size=0x5)
                    + Op.STOP
                ),
                Address("0xa100000000000000000000000000000000000000"): Account(
                    code=Op.PUSH1[0x0]
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x60, size=Op.DUP1)
                    + Op.PUSH1[0x0]
                    + Op.PUSH1[0x0]
                    + Op.MSTORE(offset=0x0, value=Op.CREATE2)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x2, value=0x1)
                    + Op.SSTORE(key=0x3, value=0x1)
                    + Op.SSTORE(key=0x4, value=0x1)
                    + Op.SSTORE(key=0x5, value=0x1)
                    + Op.SSTORE(key=0x6, value=0x1)
                    + Op.SSTORE(key=0x7, value=0x1)
                    + Op.SSTORE(key=0x8, value=0x1)
                    + Op.SSTORE(key=0x9, value=0x1)
                    + Op.SSTORE(key=0xA, value=0x1)
                    + Op.SSTORE(key=0xB, value=0x1)
                    + Op.SSTORE(key=0xC, value=0x1)
                    + Op.SSTORE(key=0xD, value=0x1)
                    + Op.SSTORE(key=0xE, value=0x1)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=0x6020602055)
                    + Op.RETURN(offset=0x1B, size=0x5)
                    + Op.STOP
                ),
                Address("0xe6db4802a3e991d7322a740ef5de5949fadc4cd5"): Account(
                    code=Op.SSTORE(key=0x20, value=0x20)
                ),
            },
        ),
        (
            "0000000000000000000000002200000000000000000000000000000000000000",
            {
                Address("0x1000000000000000000000000000000000000000"): Account(
                    storage={
                        1: 0x9FF1F274B33E3B56EDD7734520CBCDF2699FC1DC78B51644CDC56CA65BEBEEAE,  # noqa: E501
                        2: 5,
                        3: 0x6020602055000000000000000000000000000000000000000000000000000000,  # noqa: E501
                        4: 1,
                    },
                    code=Op.POP(
                        Op.CALLCODE(
                            gas=0x55730,
                            address=Op.CALLDATALOAD(offset=0x0),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(
                        key=0x1,
                        value=Op.EXTCODEHASH(address=Op.MLOAD(offset=0x0)),
                    )
                    + Op.SSTORE(
                        key=0x2,
                        value=Op.EXTCODESIZE(address=Op.MLOAD(offset=0x0)),
                    )
                    + Op.EXTCODECOPY(
                        address=Op.MLOAD(offset=0x0),
                        dest_offset=0x0,
                        offset=0x0,
                        size=0x20,
                    )
                    + Op.SSTORE(key=0x3, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(
                        key=0x4,
                        value=Op.CALLCODE(
                            gas=0xC350,
                            address=Op.MLOAD(offset=0x0),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.STOP,
                ),
                Address("0x2000000000000000000000000000000000000000"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=0x249F0,
                            address=0xA000000000000000000000000000000000000000,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x2100000000000000000000000000000000000000"): Account(
                    code=Op.POP(
                        Op.CALLCODE(
                            gas=0x249F0,
                            address=0xA000000000000000000000000000000000000000,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x2200000000000000000000000000000000000000"): Account(
                    code=Op.POP(
                        Op.DELEGATECALL(
                            gas=0x249F0,
                            address=0xA000000000000000000000000000000000000000,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x3000000000000000000000000000000000000000"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=0x249F0,
                            address=0xA100000000000000000000000000000000000000,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x3100000000000000000000000000000000000000"): Account(
                    code=Op.POP(
                        Op.CALLCODE(
                            gas=0x3D090,
                            address=0xA100000000000000000000000000000000000000,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x3200000000000000000000000000000000000000"): Account(
                    code=Op.POP(
                        Op.DELEGATECALL(
                            gas=0x249F0,
                            address=0xA100000000000000000000000000000000000000,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0xa000000000000000000000000000000000000000"): Account(
                    code=Op.PUSH1[0x0]
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x1A, size=Op.DUP1)
                    + Op.PUSH1[0x0]
                    + Op.PUSH1[0x0]
                    + Op.MSTORE(offset=0x0, value=Op.CREATE2)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=0x6020602055)
                    + Op.RETURN(offset=0x1B, size=0x5)
                    + Op.STOP
                ),
                Address("0xa100000000000000000000000000000000000000"): Account(
                    code=Op.PUSH1[0x0]
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x60, size=Op.DUP1)
                    + Op.PUSH1[0x0]
                    + Op.PUSH1[0x0]
                    + Op.MSTORE(offset=0x0, value=Op.CREATE2)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x2, value=0x1)
                    + Op.SSTORE(key=0x3, value=0x1)
                    + Op.SSTORE(key=0x4, value=0x1)
                    + Op.SSTORE(key=0x5, value=0x1)
                    + Op.SSTORE(key=0x6, value=0x1)
                    + Op.SSTORE(key=0x7, value=0x1)
                    + Op.SSTORE(key=0x8, value=0x1)
                    + Op.SSTORE(key=0x9, value=0x1)
                    + Op.SSTORE(key=0xA, value=0x1)
                    + Op.SSTORE(key=0xB, value=0x1)
                    + Op.SSTORE(key=0xC, value=0x1)
                    + Op.SSTORE(key=0xD, value=0x1)
                    + Op.SSTORE(key=0xE, value=0x1)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=0x6020602055)
                    + Op.RETURN(offset=0x1B, size=0x5)
                    + Op.STOP
                ),
                Address("0xe6db4802a3e991d7322a740ef5de5949fadc4cd5"): Account(
                    code=Op.SSTORE(key=0x20, value=0x20)
                ),
            },
        ),
        (
            "0000000000000000000000003000000000000000000000000000000000000000",
            {
                Address("0x1000000000000000000000000000000000000000"): Account(
                    storage={4: 1},
                    code=Op.POP(
                        Op.CALLCODE(
                            gas=0x55730,
                            address=Op.CALLDATALOAD(offset=0x0),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(
                        key=0x1,
                        value=Op.EXTCODEHASH(address=Op.MLOAD(offset=0x0)),
                    )
                    + Op.SSTORE(
                        key=0x2,
                        value=Op.EXTCODESIZE(address=Op.MLOAD(offset=0x0)),
                    )
                    + Op.EXTCODECOPY(
                        address=Op.MLOAD(offset=0x0),
                        dest_offset=0x0,
                        offset=0x0,
                        size=0x20,
                    )
                    + Op.SSTORE(key=0x3, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(
                        key=0x4,
                        value=Op.CALLCODE(
                            gas=0xC350,
                            address=Op.MLOAD(offset=0x0),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.STOP,
                ),
                Address("0x2000000000000000000000000000000000000000"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=0x249F0,
                            address=0xA000000000000000000000000000000000000000,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x2100000000000000000000000000000000000000"): Account(
                    code=Op.POP(
                        Op.CALLCODE(
                            gas=0x249F0,
                            address=0xA000000000000000000000000000000000000000,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x2200000000000000000000000000000000000000"): Account(
                    code=Op.POP(
                        Op.DELEGATECALL(
                            gas=0x249F0,
                            address=0xA000000000000000000000000000000000000000,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x3000000000000000000000000000000000000000"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=0x249F0,
                            address=0xA100000000000000000000000000000000000000,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x3100000000000000000000000000000000000000"): Account(
                    code=Op.POP(
                        Op.CALLCODE(
                            gas=0x3D090,
                            address=0xA100000000000000000000000000000000000000,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x3200000000000000000000000000000000000000"): Account(
                    code=Op.POP(
                        Op.DELEGATECALL(
                            gas=0x249F0,
                            address=0xA100000000000000000000000000000000000000,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0xa000000000000000000000000000000000000000"): Account(
                    code=Op.PUSH1[0x0]
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x1A, size=Op.DUP1)
                    + Op.PUSH1[0x0]
                    + Op.PUSH1[0x0]
                    + Op.MSTORE(offset=0x0, value=Op.CREATE2)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=0x6020602055)
                    + Op.RETURN(offset=0x1B, size=0x5)
                    + Op.STOP
                ),
                Address("0xa100000000000000000000000000000000000000"): Account(
                    code=Op.PUSH1[0x0]
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x60, size=Op.DUP1)
                    + Op.PUSH1[0x0]
                    + Op.PUSH1[0x0]
                    + Op.MSTORE(offset=0x0, value=Op.CREATE2)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x2, value=0x1)
                    + Op.SSTORE(key=0x3, value=0x1)
                    + Op.SSTORE(key=0x4, value=0x1)
                    + Op.SSTORE(key=0x5, value=0x1)
                    + Op.SSTORE(key=0x6, value=0x1)
                    + Op.SSTORE(key=0x7, value=0x1)
                    + Op.SSTORE(key=0x8, value=0x1)
                    + Op.SSTORE(key=0x9, value=0x1)
                    + Op.SSTORE(key=0xA, value=0x1)
                    + Op.SSTORE(key=0xB, value=0x1)
                    + Op.SSTORE(key=0xC, value=0x1)
                    + Op.SSTORE(key=0xD, value=0x1)
                    + Op.SSTORE(key=0xE, value=0x1)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=0x6020602055)
                    + Op.RETURN(offset=0x1B, size=0x5)
                    + Op.STOP
                ),
            },
        ),
        (
            "0000000000000000000000003100000000000000000000000000000000000000",
            {
                Address("0x1000000000000000000000000000000000000000"): Account(
                    storage={4: 1},
                    code=Op.POP(
                        Op.CALLCODE(
                            gas=0x55730,
                            address=Op.CALLDATALOAD(offset=0x0),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(
                        key=0x1,
                        value=Op.EXTCODEHASH(address=Op.MLOAD(offset=0x0)),
                    )
                    + Op.SSTORE(
                        key=0x2,
                        value=Op.EXTCODESIZE(address=Op.MLOAD(offset=0x0)),
                    )
                    + Op.EXTCODECOPY(
                        address=Op.MLOAD(offset=0x0),
                        dest_offset=0x0,
                        offset=0x0,
                        size=0x20,
                    )
                    + Op.SSTORE(key=0x3, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(
                        key=0x4,
                        value=Op.CALLCODE(
                            gas=0xC350,
                            address=Op.MLOAD(offset=0x0),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.STOP,
                ),
                Address("0x2000000000000000000000000000000000000000"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=0x249F0,
                            address=0xA000000000000000000000000000000000000000,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x2100000000000000000000000000000000000000"): Account(
                    code=Op.POP(
                        Op.CALLCODE(
                            gas=0x249F0,
                            address=0xA000000000000000000000000000000000000000,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x2200000000000000000000000000000000000000"): Account(
                    code=Op.POP(
                        Op.DELEGATECALL(
                            gas=0x249F0,
                            address=0xA000000000000000000000000000000000000000,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x3000000000000000000000000000000000000000"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=0x249F0,
                            address=0xA100000000000000000000000000000000000000,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x3100000000000000000000000000000000000000"): Account(
                    code=Op.POP(
                        Op.CALLCODE(
                            gas=0x3D090,
                            address=0xA100000000000000000000000000000000000000,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x3200000000000000000000000000000000000000"): Account(
                    code=Op.POP(
                        Op.DELEGATECALL(
                            gas=0x249F0,
                            address=0xA100000000000000000000000000000000000000,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0xa000000000000000000000000000000000000000"): Account(
                    code=Op.PUSH1[0x0]
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x1A, size=Op.DUP1)
                    + Op.PUSH1[0x0]
                    + Op.PUSH1[0x0]
                    + Op.MSTORE(offset=0x0, value=Op.CREATE2)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=0x6020602055)
                    + Op.RETURN(offset=0x1B, size=0x5)
                    + Op.STOP
                ),
                Address("0xa100000000000000000000000000000000000000"): Account(
                    code=Op.PUSH1[0x0]
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x60, size=Op.DUP1)
                    + Op.PUSH1[0x0]
                    + Op.PUSH1[0x0]
                    + Op.MSTORE(offset=0x0, value=Op.CREATE2)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x2, value=0x1)
                    + Op.SSTORE(key=0x3, value=0x1)
                    + Op.SSTORE(key=0x4, value=0x1)
                    + Op.SSTORE(key=0x5, value=0x1)
                    + Op.SSTORE(key=0x6, value=0x1)
                    + Op.SSTORE(key=0x7, value=0x1)
                    + Op.SSTORE(key=0x8, value=0x1)
                    + Op.SSTORE(key=0x9, value=0x1)
                    + Op.SSTORE(key=0xA, value=0x1)
                    + Op.SSTORE(key=0xB, value=0x1)
                    + Op.SSTORE(key=0xC, value=0x1)
                    + Op.SSTORE(key=0xD, value=0x1)
                    + Op.SSTORE(key=0xE, value=0x1)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=0x6020602055)
                    + Op.RETURN(offset=0x1B, size=0x5)
                    + Op.STOP
                ),
            },
        ),
        (
            "0000000000000000000000003200000000000000000000000000000000000000",
            {
                Address("0x1000000000000000000000000000000000000000"): Account(
                    storage={4: 1},
                    code=Op.POP(
                        Op.CALLCODE(
                            gas=0x55730,
                            address=Op.CALLDATALOAD(offset=0x0),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.SSTORE(
                        key=0x1,
                        value=Op.EXTCODEHASH(address=Op.MLOAD(offset=0x0)),
                    )
                    + Op.SSTORE(
                        key=0x2,
                        value=Op.EXTCODESIZE(address=Op.MLOAD(offset=0x0)),
                    )
                    + Op.EXTCODECOPY(
                        address=Op.MLOAD(offset=0x0),
                        dest_offset=0x0,
                        offset=0x0,
                        size=0x20,
                    )
                    + Op.SSTORE(key=0x3, value=Op.MLOAD(offset=0x0))
                    + Op.SSTORE(
                        key=0x4,
                        value=Op.CALLCODE(
                            gas=0xC350,
                            address=Op.MLOAD(offset=0x0),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.STOP,
                ),
                Address("0x2000000000000000000000000000000000000000"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=0x249F0,
                            address=0xA000000000000000000000000000000000000000,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x2100000000000000000000000000000000000000"): Account(
                    code=Op.POP(
                        Op.CALLCODE(
                            gas=0x249F0,
                            address=0xA000000000000000000000000000000000000000,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x2200000000000000000000000000000000000000"): Account(
                    code=Op.POP(
                        Op.DELEGATECALL(
                            gas=0x249F0,
                            address=0xA000000000000000000000000000000000000000,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x3000000000000000000000000000000000000000"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=0x249F0,
                            address=0xA100000000000000000000000000000000000000,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x3100000000000000000000000000000000000000"): Account(
                    code=Op.POP(
                        Op.CALLCODE(
                            gas=0x3D090,
                            address=0xA100000000000000000000000000000000000000,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x3200000000000000000000000000000000000000"): Account(
                    code=Op.POP(
                        Op.DELEGATECALL(
                            gas=0x249F0,
                            address=0xA100000000000000000000000000000000000000,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        )
                    )
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0xa000000000000000000000000000000000000000"): Account(
                    code=Op.PUSH1[0x0]
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x1A, size=Op.DUP1)
                    + Op.PUSH1[0x0]
                    + Op.PUSH1[0x0]
                    + Op.MSTORE(offset=0x0, value=Op.CREATE2)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=0x6020602055)
                    + Op.RETURN(offset=0x1B, size=0x5)
                    + Op.STOP
                ),
                Address("0xa100000000000000000000000000000000000000"): Account(
                    code=Op.PUSH1[0x0]
                    + Op.PUSH1[0xF]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x60, size=Op.DUP1)
                    + Op.PUSH1[0x0]
                    + Op.PUSH1[0x0]
                    + Op.MSTORE(offset=0x0, value=Op.CREATE2)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x2, value=0x1)
                    + Op.SSTORE(key=0x3, value=0x1)
                    + Op.SSTORE(key=0x4, value=0x1)
                    + Op.SSTORE(key=0x5, value=0x1)
                    + Op.SSTORE(key=0x6, value=0x1)
                    + Op.SSTORE(key=0x7, value=0x1)
                    + Op.SSTORE(key=0x8, value=0x1)
                    + Op.SSTORE(key=0x9, value=0x1)
                    + Op.SSTORE(key=0xA, value=0x1)
                    + Op.SSTORE(key=0xB, value=0x1)
                    + Op.SSTORE(key=0xC, value=0x1)
                    + Op.SSTORE(key=0xD, value=0x1)
                    + Op.SSTORE(key=0xE, value=0x1)
                    + Op.RETURN(offset=0x0, size=0x20)
                    + Op.STOP
                    + Op.STOP
                    + Op.INVALID
                    + Op.MSTORE(offset=0x0, value=0x6020602055)
                    + Op.RETURN(offset=0x1B, size=0x5)
                    + Op.STOP
                ),
            },
        ),
    ],
    ids=["case0", "case1", "case2", "case3", "case4", "case5"],
)
@pytest.mark.pre_alloc_mutable
def test_ext_code_hash_subcall_oog(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Create contract A in a subcall. go OOG in a subcall (revert..."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x1000000000000000000000000000000000000000")
    callee = Address("0x2000000000000000000000000000000000000000")
    callee_1 = Address("0x2100000000000000000000000000000000000000")
    callee_2 = Address("0x2200000000000000000000000000000000000000")
    callee_3 = Address("0x3000000000000000000000000000000000000000")
    callee_4 = Address("0x3100000000000000000000000000000000000000")
    callee_5 = Address("0x3200000000000000000000000000000000000000")
    callee_6 = Address("0xa000000000000000000000000000000000000000")
    callee_7 = Address("0xa100000000000000000000000000000000000000")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.POP(
                Op.CALLCODE(
                    gas=0x55730,
                    address=Op.CALLDATALOAD(offset=0x0),
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x20,
                ),
            )
            + Op.SSTORE(
                key=0x1,
                value=Op.EXTCODEHASH(address=Op.MLOAD(offset=0x0)),
            )
            + Op.SSTORE(
                key=0x2,
                value=Op.EXTCODESIZE(address=Op.MLOAD(offset=0x0)),
            )
            + Op.EXTCODECOPY(
                address=Op.MLOAD(offset=0x0),
                dest_offset=0x0,
                offset=0x0,
                size=0x20,
            )
            + Op.SSTORE(key=0x3, value=Op.MLOAD(offset=0x0))
            + Op.SSTORE(
                key=0x4,
                value=Op.CALLCODE(
                    gas=0xC350,
                    address=Op.MLOAD(offset=0x0),
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.STOP
        ),
    )
    pre[callee] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.POP(
                Op.CALL(
                    gas=0x249F0,
                    address=0xA000000000000000000000000000000000000000,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x20,
                ),
            )
            + Op.RETURN(offset=0x0, size=0x20)
            + Op.STOP
        ),
    )
    pre[callee_1] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.POP(
                Op.CALLCODE(
                    gas=0x249F0,
                    address=0xA000000000000000000000000000000000000000,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x20,
                ),
            )
            + Op.RETURN(offset=0x0, size=0x20)
            + Op.STOP
        ),
    )
    pre[callee_2] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.POP(
                Op.DELEGATECALL(
                    gas=0x249F0,
                    address=0xA000000000000000000000000000000000000000,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x20,
                ),
            )
            + Op.RETURN(offset=0x0, size=0x20)
            + Op.STOP
        ),
    )
    pre[callee_3] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.POP(
                Op.CALL(
                    gas=0x249F0,
                    address=0xA100000000000000000000000000000000000000,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x20,
                ),
            )
            + Op.RETURN(offset=0x0, size=0x20)
            + Op.STOP
        ),
    )
    pre[callee_4] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.POP(
                Op.CALLCODE(
                    gas=0x3D090,
                    address=0xA100000000000000000000000000000000000000,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x20,
                ),
            )
            + Op.RETURN(offset=0x0, size=0x20)
            + Op.STOP
        ),
    )
    pre[callee_5] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.POP(
                Op.DELEGATECALL(
                    gas=0x249F0,
                    address=0xA100000000000000000000000000000000000000,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x20,
                ),
            )
            + Op.RETURN(offset=0x0, size=0x20)
            + Op.STOP
        ),
    )
    pre[callee_6] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.PUSH1[0x0]
            + Op.PUSH1[0xF]
            + Op.CODECOPY(dest_offset=0x0, offset=0x1A, size=Op.DUP1)
            + Op.PUSH1[0x0]
            + Op.PUSH1[0x0]
            + Op.MSTORE(offset=0x0, value=Op.CREATE2)
            + Op.RETURN(offset=0x0, size=0x20)
            + Op.STOP
            + Op.STOP
            + Op.INVALID
            + Op.MSTORE(offset=0x0, value=0x6020602055)
            + Op.RETURN(offset=0x1B, size=0x5)
            + Op.STOP
        ),
    )
    pre[callee_7] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.PUSH1[0x0]
            + Op.PUSH1[0xF]
            + Op.CODECOPY(dest_offset=0x0, offset=0x60, size=Op.DUP1)
            + Op.PUSH1[0x0]
            + Op.PUSH1[0x0]
            + Op.MSTORE(offset=0x0, value=Op.CREATE2)
            + Op.SSTORE(key=0x1, value=0x1)
            + Op.SSTORE(key=0x2, value=0x1)
            + Op.SSTORE(key=0x3, value=0x1)
            + Op.SSTORE(key=0x4, value=0x1)
            + Op.SSTORE(key=0x5, value=0x1)
            + Op.SSTORE(key=0x6, value=0x1)
            + Op.SSTORE(key=0x7, value=0x1)
            + Op.SSTORE(key=0x8, value=0x1)
            + Op.SSTORE(key=0x9, value=0x1)
            + Op.SSTORE(key=0xA, value=0x1)
            + Op.SSTORE(key=0xB, value=0x1)
            + Op.SSTORE(key=0xC, value=0x1)
            + Op.SSTORE(key=0xD, value=0x1)
            + Op.SSTORE(key=0xE, value=0x1)
            + Op.RETURN(offset=0x0, size=0x20)
            + Op.STOP
            + Op.STOP
            + Op.INVALID
            + Op.MSTORE(offset=0x0, value=0x6020602055)
            + Op.RETURN(offset=0x1B, size=0x5)
            + Op.STOP
        ),
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=tx_data,
        gas_limit=400000,
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
