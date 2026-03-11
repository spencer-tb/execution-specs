"""
Ori Pomerantz qbzzt1@gmail.com.

Ported from:
tests/static/state_tests/VMTests/vmTests/sha3Filler.yml
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
    ["tests/static/state_tests/VMTests/vmTests/sha3Filler.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000008",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x0, size=0x0)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x4, size=0x5)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0xA, size=0xA)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3E8, size=0xFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0xFFFFFFFFF, size=0x64)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x2710, size=0xFFFFFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.SHA3(
                            offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.SHA3(
                            offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            size=0x2,
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x1000000, size=0x2)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3C0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3E0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x400, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7C0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7E0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x800, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x400, size=0x0)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7E0, size=0x20)
                    )
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=Op.SUB(0x0, 0x1),
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
                        value=0x0,
                        args_offset=0xF,
                        args_size=0x10,
                        ret_offset=0x20,
                        ret_size=0x40,
                    )
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000003",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x0, size=0x0)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x4, size=0x5)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0xA, size=0xA)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    storage={
                        0: 0xBE6F1B42B34644F918560A07F959D23E532DEA5338E4B9F63DB0CAEB608018FA  # noqa: E501
                    },
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3E8, size=0xFFFFF)
                    )
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0xFFFFFFFFF, size=0x64)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x2710, size=0xFFFFFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.SHA3(
                            offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.SHA3(
                            offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            size=0x2,
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x1000000, size=0x2)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3C0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3E0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x400, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7C0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7E0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x800, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x400, size=0x0)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7E0, size=0x20)
                    )
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=Op.SUB(0x0, 0x1),
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
                        value=0x0,
                        args_offset=0xF,
                        args_size=0x10,
                        ret_offset=0x20,
                        ret_size=0x40,
                    )
                    + Op.STOP
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000000f",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x0, size=0x0)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x4, size=0x5)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0xA, size=0xA)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3E8, size=0xFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0xFFFFFFFFF, size=0x64)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x2710, size=0xFFFFFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.SHA3(
                            offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.SHA3(
                            offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            size=0x2,
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x1000000, size=0x2)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3C0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3E0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x400, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7C0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7E0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x800, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    storage={
                        0: 0xC5D2460186F7233C927E7DB2DCC703C0E500B653CA82273B7BFAD8045D85A470  # noqa: E501
                    },
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x400, size=0x0)
                    )
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7E0, size=0x20)
                    )
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=Op.SUB(0x0, 0x1),
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
                        value=0x0,
                        args_offset=0xF,
                        args_size=0x10,
                        ret_offset=0x20,
                        ret_size=0x40,
                    )
                    + Op.STOP
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000000b",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x0, size=0x0)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x4, size=0x5)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0xA, size=0xA)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3E8, size=0xFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0xFFFFFFFFF, size=0x64)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x2710, size=0xFFFFFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.SHA3(
                            offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.SHA3(
                            offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            size=0x2,
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x1000000, size=0x2)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3C0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3E0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    storage={
                        0: 0xBC36789E7A1E281436464229828F817D6612F7B477D66591FF96A9E064BCC98A  # noqa: E501
                    },
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x400, size=0x1)
                    )
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7C0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7E0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x800, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x400, size=0x0)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7E0, size=0x20)
                    )
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=Op.SUB(0x0, 0x1),
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
                        value=0x0,
                        args_offset=0xF,
                        args_size=0x10,
                        ret_offset=0x20,
                        ret_size=0x40,
                    )
                    + Op.STOP
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000000c",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x0, size=0x0)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x4, size=0x5)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0xA, size=0xA)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3E8, size=0xFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0xFFFFFFFFF, size=0x64)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x2710, size=0xFFFFFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.SHA3(
                            offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.SHA3(
                            offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            size=0x2,
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x1000000, size=0x2)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3C0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3E0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x400, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    storage={
                        0: 0xBC36789E7A1E281436464229828F817D6612F7B477D66591FF96A9E064BCC98A  # noqa: E501
                    },
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7C0, size=0x1)
                    )
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7E0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x800, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x400, size=0x0)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7E0, size=0x20)
                    )
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=Op.SUB(0x0, 0x1),
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
                        value=0x0,
                        args_offset=0xF,
                        args_size=0x10,
                        ret_offset=0x20,
                        ret_size=0x40,
                    )
                    + Op.STOP
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000000d",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x0, size=0x0)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x4, size=0x5)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0xA, size=0xA)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3E8, size=0xFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0xFFFFFFFFF, size=0x64)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x2710, size=0xFFFFFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.SHA3(
                            offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.SHA3(
                            offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            size=0x2,
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x1000000, size=0x2)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3C0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3E0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x400, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7C0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    storage={
                        0: 0xBC36789E7A1E281436464229828F817D6612F7B477D66591FF96A9E064BCC98A  # noqa: E501
                    },
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7E0, size=0x1)
                    )
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x800, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x400, size=0x0)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7E0, size=0x20)
                    )
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=Op.SUB(0x0, 0x1),
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
                        value=0x0,
                        args_offset=0xF,
                        args_size=0x10,
                        ret_offset=0x20,
                        ret_size=0x40,
                    )
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000010",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x0, size=0x0)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x4, size=0x5)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0xA, size=0xA)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3E8, size=0xFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0xFFFFFFFFF, size=0x64)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x2710, size=0xFFFFFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.SHA3(
                            offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.SHA3(
                            offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            size=0x2,
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x1000000, size=0x2)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3C0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3E0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x400, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7C0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7E0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x800, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x400, size=0x0)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    storage={
                        0: 0x290DECD9548B62A8D60345A988386FC84BA6BC95484008F6362F93160EF3E563  # noqa: E501
                    },
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7E0, size=0x20)
                    )
                    + Op.STOP,
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=Op.SUB(0x0, 0x1),
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
                        value=0x0,
                        args_offset=0xF,
                        args_size=0x10,
                        ret_offset=0x20,
                        ret_size=0x40,
                    )
                    + Op.STOP
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000000e",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x0, size=0x0)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x4, size=0x5)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0xA, size=0xA)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3E8, size=0xFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0xFFFFFFFFF, size=0x64)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x2710, size=0xFFFFFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.SHA3(
                            offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.SHA3(
                            offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            size=0x2,
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x1000000, size=0x2)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3C0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3E0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x400, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7C0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7E0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    storage={
                        0: 0xBC36789E7A1E281436464229828F817D6612F7B477D66591FF96A9E064BCC98A  # noqa: E501
                    },
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x800, size=0x1)
                    )
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x400, size=0x0)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7E0, size=0x20)
                    )
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=Op.SUB(0x0, 0x1),
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
                        value=0x0,
                        args_offset=0xF,
                        args_size=0x10,
                        ret_offset=0x20,
                        ret_size=0x40,
                    )
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000009",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x0, size=0x0)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x4, size=0x5)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0xA, size=0xA)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3E8, size=0xFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0xFFFFFFFFF, size=0x64)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x2710, size=0xFFFFFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.SHA3(
                            offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.SHA3(
                            offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            size=0x2,
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x1000000, size=0x2)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    storage={
                        0: 0xBC36789E7A1E281436464229828F817D6612F7B477D66591FF96A9E064BCC98A  # noqa: E501
                    },
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3C0, size=0x1)
                    )
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3E0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x400, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7C0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7E0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x800, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x400, size=0x0)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7E0, size=0x20)
                    )
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=Op.SUB(0x0, 0x1),
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
                        value=0x0,
                        args_offset=0xF,
                        args_size=0x10,
                        ret_offset=0x20,
                        ret_size=0x40,
                    )
                    + Op.STOP
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000000a",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x0, size=0x0)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x4, size=0x5)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0xA, size=0xA)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3E8, size=0xFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0xFFFFFFFFF, size=0x64)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x2710, size=0xFFFFFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.SHA3(
                            offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.SHA3(
                            offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            size=0x2,
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x1000000, size=0x2)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3C0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    storage={
                        0: 0xBC36789E7A1E281436464229828F817D6612F7B477D66591FF96A9E064BCC98A  # noqa: E501
                    },
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3E0, size=0x1)
                    )
                    + Op.STOP,
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x400, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7C0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7E0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x800, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x400, size=0x0)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7E0, size=0x20)
                    )
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=Op.SUB(0x0, 0x1),
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
                        value=0x0,
                        args_offset=0xF,
                        args_size=0x10,
                        ret_offset=0x20,
                        ret_size=0x40,
                    )
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000001",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x0, size=0x0)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    storage={
                        0: 0xC41589E7559804EA4A2080DAD19D876A024CCB05117835447D72CE08C1D020EC  # noqa: E501
                    },
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x4, size=0x5)
                    )
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0xA, size=0xA)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3E8, size=0xFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0xFFFFFFFFF, size=0x64)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x2710, size=0xFFFFFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.SHA3(
                            offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.SHA3(
                            offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            size=0x2,
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x1000000, size=0x2)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3C0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3E0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x400, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7C0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7E0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x800, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x400, size=0x0)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7E0, size=0x20)
                    )
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=Op.SUB(0x0, 0x1),
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
                        value=0x0,
                        args_offset=0xF,
                        args_size=0x10,
                        ret_offset=0x20,
                        ret_size=0x40,
                    )
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000004",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x0, size=0x0)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x4, size=0x5)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0xA, size=0xA)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3E8, size=0xFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0xFFFFFFFFF, size=0x64)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x2710, size=0xFFFFFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.SHA3(
                            offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.SHA3(
                            offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            size=0x2,
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x1000000, size=0x2)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3C0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3E0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x400, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7C0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7E0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x800, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x400, size=0x0)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7E0, size=0x20)
                    )
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=Op.SUB(0x0, 0x1),
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
                        value=0x0,
                        args_offset=0xF,
                        args_size=0x10,
                        ret_offset=0x20,
                        ret_size=0x40,
                    )
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000005",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x0, size=0x0)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x4, size=0x5)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0xA, size=0xA)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3E8, size=0xFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0xFFFFFFFFF, size=0x64)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x2710, size=0xFFFFFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.SHA3(
                            offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.SHA3(
                            offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            size=0x2,
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x1000000, size=0x2)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3C0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3E0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x400, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7C0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7E0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x800, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x400, size=0x0)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7E0, size=0x20)
                    )
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=Op.SUB(0x0, 0x1),
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
                        value=0x0,
                        args_offset=0xF,
                        args_size=0x10,
                        ret_offset=0x20,
                        ret_size=0x40,
                    )
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000007",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x0, size=0x0)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x4, size=0x5)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0xA, size=0xA)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3E8, size=0xFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0xFFFFFFFFF, size=0x64)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x2710, size=0xFFFFFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.SHA3(
                            offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.SHA3(
                            offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            size=0x2,
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x1000000, size=0x2)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3C0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3E0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x400, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7C0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7E0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x800, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x400, size=0x0)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7E0, size=0x20)
                    )
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=Op.SUB(0x0, 0x1),
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
                        value=0x0,
                        args_offset=0xF,
                        args_size=0x10,
                        ret_offset=0x20,
                        ret_size=0x40,
                    )
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000006",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x0, size=0x0)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x4, size=0x5)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0xA, size=0xA)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3E8, size=0xFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0xFFFFFFFFF, size=0x64)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x2710, size=0xFFFFFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.SHA3(
                            offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.SHA3(
                            offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            size=0x2,
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x1000000, size=0x2)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3C0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3E0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x400, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7C0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7E0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x800, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x400, size=0x0)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7E0, size=0x20)
                    )
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=Op.SUB(0x0, 0x1),
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
                        value=0x0,
                        args_offset=0xF,
                        args_size=0x10,
                        ret_offset=0x20,
                        ret_size=0x40,
                    )
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000000",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    storage={
                        0: 0xC5D2460186F7233C927E7DB2DCC703C0E500B653CA82273B7BFAD8045D85A470  # noqa: E501
                    },
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x0, size=0x0)
                    )
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x4, size=0x5)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0xA, size=0xA)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3E8, size=0xFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0xFFFFFFFFF, size=0x64)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x2710, size=0xFFFFFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.SHA3(
                            offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.SHA3(
                            offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            size=0x2,
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x1000000, size=0x2)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3C0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3E0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x400, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7C0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7E0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x800, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x400, size=0x0)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7E0, size=0x20)
                    )
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=Op.SUB(0x0, 0x1),
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
                        value=0x0,
                        args_offset=0xF,
                        args_size=0x10,
                        ret_offset=0x20,
                        ret_size=0x40,
                    )
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000002",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x0, size=0x0)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x4, size=0x5)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    storage={
                        0: 0x6BD2DD6BD408CBEE33429358BF24FDC64612FBF8B1B4DB604518F40FFD34B607  # noqa: E501
                    },
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0xA, size=0xA)
                    )
                    + Op.STOP,
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3E8, size=0xFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0xFFFFFFFFF, size=0x64)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x2710, size=0xFFFFFFFFF)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.SHA3(
                            offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.SHA3(
                            offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            size=0x2,
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x1000000, size=0x2)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3C0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x3E0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x400, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7C0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7E0, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x800, size=0x1)
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x400, size=0x0)
                    )
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.SHA3(offset=0x7E0, size=0x20)
                    )
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.CALL(
                        gas=Op.SUB(0x0, 0x1),
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
                        value=0x0,
                        args_offset=0xF,
                        args_size=0x10,
                        ret_offset=0x20,
                        ret_size=0x40,
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
        "case12",
        "case13",
        "case14",
        "case15",
        "case16",
    ],
)
@pytest.mark.pre_alloc_mutable
def test_sha3(
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
    callee_10 = Address("0x000000000000000000000000000000000000100a")
    callee_11 = Address("0x000000000000000000000000000000000000100b")
    callee_12 = Address("0x000000000000000000000000000000000000100c")
    callee_13 = Address("0x000000000000000000000000000000000000100d")
    callee_14 = Address("0x000000000000000000000000000000000000100e")
    callee_15 = Address("0x000000000000000000000000000000000000100f")
    callee_16 = Address("0x0000000000000000000000000000000000001010")

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
        code=Op.SSTORE(key=0x0, value=Op.SHA3(offset=0x0, size=0x0)) + Op.STOP,
    )
    pre[callee_1] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=Op.SSTORE(key=0x0, value=Op.SHA3(offset=0x4, size=0x5)) + Op.STOP,
    )
    pre[callee_2] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=Op.SSTORE(key=0x0, value=Op.SHA3(offset=0xA, size=0xA)) + Op.STOP,
    )
    pre[callee_3] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=Op.SHA3(offset=0x3E8, size=0xFFFFF))
            + Op.STOP
        ),
    )
    pre[callee_4] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=Op.SHA3(offset=0xFFFFFFFFF, size=0x64))
            + Op.STOP
        ),
    )
    pre[callee_5] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=Op.SHA3(offset=0x2710, size=0xFFFFFFFFF))
            + Op.STOP
        ),
    )
    pre[callee_6] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.SSTORE(
                key=0x0,
                value=Op.SHA3(
                    offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                    size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                ),
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
                value=Op.SHA3(
                    offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                    size=0x2,
                ),
            )
            + Op.STOP
        ),
    )
    # Source: LLL
    # {
    #     [[0]] (sha3 0x1000000 2)
    # }
    pre[callee_8] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=Op.SHA3(offset=0x1000000, size=0x2))
            + Op.STOP
        ),
    )
    # Source: LLL
    # {
    #   [[ 0 ]] (sha3 960 1)
    # }
    pre[callee_9] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=Op.SHA3(offset=0x3C0, size=0x1)) + Op.STOP
        ),
    )
    # Source: LLL
    # {
    #   [[ 0 ]] (sha3 992 1)
    # }
    pre[callee_10] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=Op.SHA3(offset=0x3E0, size=0x1)) + Op.STOP
        ),
    )
    # Source: LLL
    # {
    #   [[ 0 ]] (sha3 1024 1)
    # }
    pre[callee_11] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=Op.SHA3(offset=0x400, size=0x1)) + Op.STOP
        ),
    )
    # Source: LLL
    # {
    #   [[ 0 ]] (sha3 1984 1)
    # }
    pre[callee_12] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=Op.SHA3(offset=0x7C0, size=0x1)) + Op.STOP
        ),
    )
    # Source: LLL
    # {
    #   [[ 0 ]] (sha3 2016 1)
    # }
    pre[callee_13] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=Op.SHA3(offset=0x7E0, size=0x1)) + Op.STOP
        ),
    )
    # Source: LLL
    # {
    #   [[ 0 ]] (sha3 2048 1)
    # }
    pre[callee_14] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=Op.SHA3(offset=0x800, size=0x1)) + Op.STOP
        ),
    )
    # Source: LLL
    # {
    #   [[ 0 ]] (sha3 1024 0)
    # }
    pre[callee_15] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=Op.SHA3(offset=0x400, size=0x0)) + Op.STOP
        ),
    )
    pre[callee_16] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=Op.SHA3(offset=0x7E0, size=0x20))
            + Op.STOP
        ),
    )
    pre[sender] = Account(balance=0x100000000000, nonce=0)
    # Source: LLL
    # {
    #     (call (- 0 1) (+ 0x1000 $4) 0
    #        0x0F 0x10   ; arg offset and length to get the 0x1234...f0 value
    #        0x20 0x40)  ; return offset and length
    # }
    pre[contract] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.CALL(
                gas=Op.SUB(0x0, 0x1),
                address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
                value=0x0,
                args_offset=0xF,
                args_size=0x10,
                ret_offset=0x20,
                ret_size=0x40,
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
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
