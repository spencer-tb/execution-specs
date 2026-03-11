"""
Ori Pomerantz qbzzt1@gmail.com.

Ported from:
tests/static/state_tests/VMTests/vmArithmeticTest/expFiller.yml
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
    ["tests/static/state_tests/VMTests/vmArithmeticTest/expFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000008",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0x2)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.EXP(
                            0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE,  # noqa: E501
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.EXP(0x7FFFFFFF, 0x7FFFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x0, 0x7FFFFFFF))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x7FFFFFFF, 0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x101, 0x1)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x1, 0x101)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0x101)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    storage={0: 1},
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x0, 0x0)) + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0x100000000000F))
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0xF)) + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=0xFFFFFF,
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
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
            "693c61390000000000000000000000000000000000000000000000000000000000000003",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0x2)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.EXP(
                            0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE,  # noqa: E501
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.EXP(0x7FFFFFFF, 0x7FFFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x0, 0x7FFFFFFF))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x7FFFFFFF, 0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x101, 0x1)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x1, 0x101)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0x101)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x0, 0x0)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0x100000000000F))
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0xF)) + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=0xFFFFFF,
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
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
            "693c61390000000000000000000000000000000000000000000000000000000000000006",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0x2)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.EXP(
                            0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE,  # noqa: E501
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.EXP(0x7FFFFFFF, 0x7FFFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x0, 0x7FFFFFFF))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x7FFFFFFF, 0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x101, 0x1)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    storage={0: 1},
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x1, 0x101))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0x101)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x0, 0x0)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0x100000000000F))
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0xF)) + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=0xFFFFFF,
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
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
            "693c61390000000000000000000000000000000000000000000000000000000000000005",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0x2)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.EXP(
                            0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE,  # noqa: E501
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.EXP(0x7FFFFFFF, 0x7FFFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x0, 0x7FFFFFFF))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x7FFFFFFF, 0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    storage={0: 257},
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x101, 0x1))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x1, 0x101)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0x101)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x0, 0x0)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0x100000000000F))
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0xF)) + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=0xFFFFFF,
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
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
            "693c6139000000000000000000000000000000000000000000000000000000000000000a",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0x2)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.EXP(
                            0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE,  # noqa: E501
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.EXP(0x7FFFFFFF, 0x7FFFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x0, 0x7FFFFFFF))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x7FFFFFFF, 0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x101, 0x1)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x1, 0x101)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0x101)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x0, 0x0)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0x100000000000F))
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    storage={0: 32768},
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0xF)) + Op.STOP,
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=0xFFFFFF,
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
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
            "693c61390000000000000000000000000000000000000000000000000000000000000007",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0x2)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.EXP(
                            0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE,  # noqa: E501
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.EXP(0x7FFFFFFF, 0x7FFFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x0, 0x7FFFFFFF))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x7FFFFFFF, 0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x101, 0x1)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x1, 0x101)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0x101)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x0, 0x0)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0x100000000000F))
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0xF)) + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=0xFFFFFF,
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
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
            "693c61390000000000000000000000000000000000000000000000000000000000000000",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    storage={0: 4},
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0x2)) + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.EXP(
                            0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE,  # noqa: E501
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.EXP(0x7FFFFFFF, 0x7FFFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x0, 0x7FFFFFFF))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x7FFFFFFF, 0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x101, 0x1)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x1, 0x101)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0x101)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x0, 0x0)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0x100000000000F))
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0xF)) + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=0xFFFFFF,
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
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
            "693c61390000000000000000000000000000000000000000000000000000000000000009",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0x2)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.EXP(
                            0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE,  # noqa: E501
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.EXP(0x7FFFFFFF, 0x7FFFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x0, 0x7FFFFFFF))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x7FFFFFFF, 0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x101, 0x1)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x1, 0x101)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0x101)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x0, 0x0)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0x100000000000F))
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0xF)) + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=0xFFFFFF,
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
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
            "693c61390000000000000000000000000000000000000000000000000000000000000004",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0x2)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.EXP(
                            0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE,  # noqa: E501
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.EXP(0x7FFFFFFF, 0x7FFFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x0, 0x7FFFFFFF))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    storage={0: 1},
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x7FFFFFFF, 0x0))
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x101, 0x1)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x1, 0x101)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0x101)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x0, 0x0)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0x100000000000F))
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0xF)) + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=0xFFFFFF,
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
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
            "693c61390000000000000000000000000000000000000000000000000000000000000002",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0x2)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.EXP(
                            0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE,  # noqa: E501
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    storage={
                        0: 0xBC8CCCCCCCC888888880000000AAAAAAB00000000FFFFFFFFFFFFFFF7FFFFFFF  # noqa: E501
                    },
                    code=Op.SSTORE(
                        key=0x0, value=Op.EXP(0x7FFFFFFF, 0x7FFFFFFF)
                    )
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x0, 0x7FFFFFFF))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x7FFFFFFF, 0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x101, 0x1)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x1, 0x101)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0x101)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x0, 0x0)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0x100000000000F))
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0xF)) + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=0xFFFFFF,
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
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
            "693c61390000000000000000000000000000000000000000000000000000000000000001",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0x2)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    storage={0: 1},
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.EXP(
                            0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE,  # noqa: E501
                        ),
                    )
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.EXP(0x7FFFFFFF, 0x7FFFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x0, 0x7FFFFFFF))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x7FFFFFFF, 0x0))
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x101, 0x1)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x1, 0x101)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0x101)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x0, 0x0)) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0x100000000000F))
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0xF)) + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=0xFFFFFF,
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
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
    ],
)
@pytest.mark.pre_alloc_mutable
def test_exp(
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
    callee_10 = Address("0x000000000000000000000000000000000000100a")

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
        code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0x2)) + Op.STOP,
    )
    pre[callee_1] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.SSTORE(
                key=0x0,
                value=Op.EXP(
                    0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                    0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE,  # noqa: E501
                ),
            )
            + Op.STOP
        ),
    )
    pre[callee_2] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=Op.EXP(0x7FFFFFFF, 0x7FFFFFFF)) + Op.STOP
        ),
    )
    pre[callee_3] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=Op.SSTORE(key=0x0, value=Op.EXP(0x0, 0x7FFFFFFF)) + Op.STOP,
    )
    pre[callee_4] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=Op.SSTORE(key=0x0, value=Op.EXP(0x7FFFFFFF, 0x0)) + Op.STOP,
    )
    pre[callee_5] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=Op.SSTORE(key=0x0, value=Op.EXP(0x101, 0x1)) + Op.STOP,
    )
    pre[callee_6] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=Op.SSTORE(key=0x0, value=Op.EXP(0x1, 0x101)) + Op.STOP,
    )
    pre[callee_7] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0x101)) + Op.STOP,
    )
    # Source: LLL
    # {  ; 0^0 (that is 1 in evm arithmetic)
    #    [[0]] (exp 0 0)
    # }
    pre[callee_8] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=Op.SSTORE(key=0x0, value=Op.EXP(0x0, 0x0)) + Op.STOP,
    )
    # Source: LLL
    # {  ; 2^big = 0
    #    [[0]] (exp 2 0x0100000000000f)
    # }
    pre[callee_9] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0x100000000000F)) + Op.STOP,
    )
    # Source: LLL
    # {  ; 2^15 = 0x8000
    #    [[0]] (exp 2 15)
    # }
    pre[callee_10] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=Op.SSTORE(key=0x0, value=Op.EXP(0x2, 0xF)) + Op.STOP,
    )
    pre[sender] = Account(balance=0xBA1A9CE0BA1A9CE, nonce=0)
    # Source: LLL
    # {
    #     (call 0xffffff (+ 0x1000 $4) 0 0 0 0 0)
    # }
    pre[contract] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.CALL(
                gas=0xFFFFFF,
                address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
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
