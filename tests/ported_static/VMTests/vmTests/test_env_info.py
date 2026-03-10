"""
Ori Pomerantz qbzzt1@gmail.com.

Ported from:
tests/static/state_tests/VMTests/vmTests/envInfoFiller.yml
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
    ["tests/static/state_tests/VMTests/vmTests/envInfoFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000000",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    storage={0: 4096},
                    code=Op.SSTORE(key=0x0, value=Op.ADDRESS) + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CODECOPY(dest_offset=0x0, offset=0x0, size=0x7)
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CODECOPY(dest_offset=0x0, offset=0x0, size=0x0)
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.CODECOPY(
                        dest_offset=0x0,
                        offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA,  # noqa: E501
                        size=0x8,
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.CALLER) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.CALLVALUE) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.CODESIZE) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.GASPRICE) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.ORIGIN) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.CALLDATASIZE) + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=0xFFFFFF,
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
                        value=0x10,
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
            "693c61390000000000000000000000000000000000000000000000000000000000000009",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.ADDRESS) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CODECOPY(dest_offset=0x0, offset=0x0, size=0x7)
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CODECOPY(dest_offset=0x0, offset=0x0, size=0x0)
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.CODECOPY(
                        dest_offset=0x0,
                        offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA,  # noqa: E501
                        size=0x8,
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.CALLER) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.CALLVALUE) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.CODESIZE) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.GASPRICE) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.ORIGIN) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.CALLDATASIZE) + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=0xFFFFFF,
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
                        value=0x10,
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
            "693c61390000000000000000000000000000000000000000000000000000000000000004",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.ADDRESS) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CODECOPY(dest_offset=0x0, offset=0x0, size=0x7)
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CODECOPY(dest_offset=0x0, offset=0x0, size=0x0)
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.CODECOPY(
                        dest_offset=0x0,
                        offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA,  # noqa: E501
                        size=0x8,
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    storage={0: 0xCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC},
                    code=Op.SSTORE(key=0x0, value=Op.CALLER) + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.CALLVALUE) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.CODESIZE) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.GASPRICE) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.ORIGIN) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.CALLDATASIZE) + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=0xFFFFFF,
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
                        value=0x10,
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
            "693c61390000000000000000000000000000000000000000000000000000000000000005",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.ADDRESS) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CODECOPY(dest_offset=0x0, offset=0x0, size=0x7)
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CODECOPY(dest_offset=0x0, offset=0x0, size=0x0)
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.CODECOPY(
                        dest_offset=0x0,
                        offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA,  # noqa: E501
                        size=0x8,
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.CALLER) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    storage={0: 16},
                    code=Op.SSTORE(key=0x0, value=Op.CALLVALUE) + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.CODESIZE) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.GASPRICE) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.ORIGIN) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.CALLDATASIZE) + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=0xFFFFFF,
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
                        value=0x10,
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
            "693c61390000000000000000000000000000000000000000000000000000000000000001",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.ADDRESS) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    storage={
                        0: 0x6007600060003900000000000000000000000000000000000000000000000000  # noqa: E501
                    },
                    code=Op.CODECOPY(dest_offset=0x0, offset=0x0, size=0x7)
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CODECOPY(dest_offset=0x0, offset=0x0, size=0x0)
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.CODECOPY(
                        dest_offset=0x0,
                        offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA,  # noqa: E501
                        size=0x8,
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.CALLER) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.CALLVALUE) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.CODESIZE) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.GASPRICE) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.ORIGIN) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.CALLDATASIZE) + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=0xFFFFFF,
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
                        value=0x10,
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
            "693c61390000000000000000000000000000000000000000000000000000000000000002",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.ADDRESS) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CODECOPY(dest_offset=0x0, offset=0x0, size=0x7)
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CODECOPY(dest_offset=0x0, offset=0x0, size=0x0)
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.CODECOPY(
                        dest_offset=0x0,
                        offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA,  # noqa: E501
                        size=0x8,
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.CALLER) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.CALLVALUE) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.CODESIZE) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.GASPRICE) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.ORIGIN) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.CALLDATASIZE) + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=0xFFFFFF,
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
                        value=0x10,
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
            "693c61390000000000000000000000000000000000000000000000000000000000000003",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.ADDRESS) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CODECOPY(dest_offset=0x0, offset=0x0, size=0x7)
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CODECOPY(dest_offset=0x0, offset=0x0, size=0x0)
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.CODECOPY(
                        dest_offset=0x0,
                        offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA,  # noqa: E501
                        size=0x8,
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.CALLER) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.CALLVALUE) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.CODESIZE) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.GASPRICE) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.ORIGIN) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.CALLDATASIZE) + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=0xFFFFFF,
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
                        value=0x10,
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
            "693c61390000000000000000000000000000000000000000000000000000000000000006",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.ADDRESS) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CODECOPY(dest_offset=0x0, offset=0x0, size=0x7)
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CODECOPY(dest_offset=0x0, offset=0x0, size=0x0)
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.CODECOPY(
                        dest_offset=0x0,
                        offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA,  # noqa: E501
                        size=0x8,
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.CALLER) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.CALLVALUE) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    storage={0: 5},
                    code=Op.SSTORE(key=0x0, value=Op.CODESIZE) + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.GASPRICE) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.ORIGIN) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.CALLDATASIZE) + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=0xFFFFFF,
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
                        value=0x10,
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
            "693c61390000000000000000000000000000000000000000000000000000000000000007",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.ADDRESS) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CODECOPY(dest_offset=0x0, offset=0x0, size=0x7)
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CODECOPY(dest_offset=0x0, offset=0x0, size=0x0)
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.CODECOPY(
                        dest_offset=0x0,
                        offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA,  # noqa: E501
                        size=0x8,
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.CALLER) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.CALLVALUE) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.CODESIZE) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    storage={0: 4660},
                    code=Op.SSTORE(key=0x0, value=Op.GASPRICE) + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.ORIGIN) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.CALLDATASIZE) + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=0xFFFFFF,
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
                        value=0x10,
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
            "693c61390000000000000000000000000000000000000000000000000000000000000008",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.ADDRESS) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.CODECOPY(dest_offset=0x0, offset=0x0, size=0x7)
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.CODECOPY(dest_offset=0x0, offset=0x0, size=0x0)
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.CODECOPY(
                        dest_offset=0x0,
                        offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA,  # noqa: E501
                        size=0x8,
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.CALLER) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.CALLVALUE) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.CODESIZE) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.GASPRICE) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    storage={0: 0xA94F5374FCE5EDBC8E2A8697C15331677E6EBF0B},
                    code=Op.SSTORE(key=0x0, value=Op.ORIGIN) + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.CALLDATASIZE) + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=0xFFFFFF,
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
                        value=0x10,
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
    ],
)
@pytest.mark.pre_alloc_mutable
def test_env_info(
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
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=Op.SSTORE(key=0x0, value=Op.ADDRESS) + Op.STOP,
    )
    pre[callee_1] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.CODECOPY(dest_offset=0x0, offset=0x0, size=0x7)
            + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
            + Op.STOP
        ),
    )
    pre[callee_2] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.CODECOPY(dest_offset=0x0, offset=0x0, size=0x0)
            + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
            + Op.STOP
        ),
    )
    pre[callee_3] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.CODECOPY(
                dest_offset=0x0,
                offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA,  # noqa: E501
                size=0x8,
            )
            + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
            + Op.STOP
        ),
    )
    pre[callee_4] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=Op.SSTORE(key=0x0, value=Op.CALLER) + Op.STOP,
    )
    pre[callee_5] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=Op.SSTORE(key=0x0, value=Op.CALLVALUE) + Op.STOP,
    )
    pre[callee_6] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=Op.SSTORE(key=0x0, value=Op.CODESIZE) + Op.STOP,
    )
    pre[callee_7] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=Op.SSTORE(key=0x0, value=Op.GASPRICE) + Op.STOP,
    )
    pre[callee_8] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=Op.SSTORE(key=0x0, value=Op.ORIGIN) + Op.STOP,
    )
    pre[callee_9] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=Op.SSTORE(key=0x0, value=Op.CALLDATASIZE) + Op.STOP,
    )
    pre[sender] = Account(balance=0xBA1A9CE0BA1A9CE, nonce=0)
    pre[contract] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.CALL(
                gas=0xFFFFFF,
                address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
                value=0x10,
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
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=tx_data,
        gas_limit=16777216,
        gas_price=4660,
        nonce=0,
        value=1,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
