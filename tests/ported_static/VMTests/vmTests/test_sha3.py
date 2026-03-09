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
                    code=bytes.fromhex("600060002060005500")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex("600560042060005500")
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("600a600a2060005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("620fffff6103e82060005500")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex("6064640fffffffff2060005500")
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex("640fffffffff6127102060005500")
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex(
                        "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2060005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex(
                        "60027fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2060005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600263010000002060005500")
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=bytes.fromhex("60016103c02060005500")
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=bytes.fromhex("60016103e02060005500")
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=bytes.fromhex("60016104002060005500")
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=bytes.fromhex("60016107c02060005500")
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=bytes.fromhex("60016107e02060005500")
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=bytes.fromhex("60016108002060005500")
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=bytes.fromhex("60006104002060005500")
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=bytes.fromhex("60206107e02060005500")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "604060206010600f6000600435611000016001600003f100"
                    )
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000003",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("600060002060005500")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex("600560042060005500")
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("600a600a2060005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    storage={
                        0: 0xBE6F1B42B34644F918560A07F959D23E532DEA5338E4B9F63DB0CAEB608018FA  # noqa: E501
                    },
                    code=bytes.fromhex("620fffff6103e82060005500"),
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex("6064640fffffffff2060005500")
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex("640fffffffff6127102060005500")
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex(
                        "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2060005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex(
                        "60027fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2060005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600263010000002060005500")
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=bytes.fromhex("60016103c02060005500")
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=bytes.fromhex("60016103e02060005500")
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=bytes.fromhex("60016104002060005500")
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=bytes.fromhex("60016107c02060005500")
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=bytes.fromhex("60016107e02060005500")
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=bytes.fromhex("60016108002060005500")
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=bytes.fromhex("60006104002060005500")
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=bytes.fromhex("60206107e02060005500")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "604060206010600f6000600435611000016001600003f100"
                    )
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000000f",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("600060002060005500")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex("600560042060005500")
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("600a600a2060005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("620fffff6103e82060005500")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex("6064640fffffffff2060005500")
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex("640fffffffff6127102060005500")
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex(
                        "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2060005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex(
                        "60027fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2060005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600263010000002060005500")
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=bytes.fromhex("60016103c02060005500")
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=bytes.fromhex("60016103e02060005500")
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=bytes.fromhex("60016104002060005500")
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=bytes.fromhex("60016107c02060005500")
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=bytes.fromhex("60016107e02060005500")
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=bytes.fromhex("60016108002060005500")
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    storage={
                        0: 0xC5D2460186F7233C927E7DB2DCC703C0E500B653CA82273B7BFAD8045D85A470  # noqa: E501
                    },
                    code=bytes.fromhex("60006104002060005500"),
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=bytes.fromhex("60206107e02060005500")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "604060206010600f6000600435611000016001600003f100"
                    )
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000000b",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("600060002060005500")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex("600560042060005500")
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("600a600a2060005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("620fffff6103e82060005500")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex("6064640fffffffff2060005500")
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex("640fffffffff6127102060005500")
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex(
                        "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2060005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex(
                        "60027fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2060005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600263010000002060005500")
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=bytes.fromhex("60016103c02060005500")
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=bytes.fromhex("60016103e02060005500")
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    storage={
                        0: 0xBC36789E7A1E281436464229828F817D6612F7B477D66591FF96A9E064BCC98A  # noqa: E501
                    },
                    code=bytes.fromhex("60016104002060005500"),
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=bytes.fromhex("60016107c02060005500")
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=bytes.fromhex("60016107e02060005500")
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=bytes.fromhex("60016108002060005500")
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=bytes.fromhex("60006104002060005500")
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=bytes.fromhex("60206107e02060005500")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "604060206010600f6000600435611000016001600003f100"
                    )
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000000c",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("600060002060005500")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex("600560042060005500")
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("600a600a2060005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("620fffff6103e82060005500")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex("6064640fffffffff2060005500")
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex("640fffffffff6127102060005500")
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex(
                        "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2060005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex(
                        "60027fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2060005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600263010000002060005500")
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=bytes.fromhex("60016103c02060005500")
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=bytes.fromhex("60016103e02060005500")
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=bytes.fromhex("60016104002060005500")
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    storage={
                        0: 0xBC36789E7A1E281436464229828F817D6612F7B477D66591FF96A9E064BCC98A  # noqa: E501
                    },
                    code=bytes.fromhex("60016107c02060005500"),
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=bytes.fromhex("60016107e02060005500")
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=bytes.fromhex("60016108002060005500")
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=bytes.fromhex("60006104002060005500")
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=bytes.fromhex("60206107e02060005500")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "604060206010600f6000600435611000016001600003f100"
                    )
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000000d",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("600060002060005500")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex("600560042060005500")
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("600a600a2060005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("620fffff6103e82060005500")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex("6064640fffffffff2060005500")
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex("640fffffffff6127102060005500")
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex(
                        "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2060005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex(
                        "60027fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2060005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600263010000002060005500")
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=bytes.fromhex("60016103c02060005500")
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=bytes.fromhex("60016103e02060005500")
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=bytes.fromhex("60016104002060005500")
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=bytes.fromhex("60016107c02060005500")
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    storage={
                        0: 0xBC36789E7A1E281436464229828F817D6612F7B477D66591FF96A9E064BCC98A  # noqa: E501
                    },
                    code=bytes.fromhex("60016107e02060005500"),
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=bytes.fromhex("60016108002060005500")
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=bytes.fromhex("60006104002060005500")
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=bytes.fromhex("60206107e02060005500")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "604060206010600f6000600435611000016001600003f100"
                    )
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000010",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("600060002060005500")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex("600560042060005500")
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("600a600a2060005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("620fffff6103e82060005500")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex("6064640fffffffff2060005500")
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex("640fffffffff6127102060005500")
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex(
                        "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2060005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex(
                        "60027fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2060005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600263010000002060005500")
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=bytes.fromhex("60016103c02060005500")
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=bytes.fromhex("60016103e02060005500")
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=bytes.fromhex("60016104002060005500")
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=bytes.fromhex("60016107c02060005500")
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=bytes.fromhex("60016107e02060005500")
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=bytes.fromhex("60016108002060005500")
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=bytes.fromhex("60006104002060005500")
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    storage={
                        0: 0x290DECD9548B62A8D60345A988386FC84BA6BC95484008F6362F93160EF3E563  # noqa: E501
                    },
                    code=bytes.fromhex("60206107e02060005500"),
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "604060206010600f6000600435611000016001600003f100"
                    )
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000000e",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("600060002060005500")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex("600560042060005500")
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("600a600a2060005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("620fffff6103e82060005500")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex("6064640fffffffff2060005500")
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex("640fffffffff6127102060005500")
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex(
                        "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2060005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex(
                        "60027fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2060005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600263010000002060005500")
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=bytes.fromhex("60016103c02060005500")
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=bytes.fromhex("60016103e02060005500")
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=bytes.fromhex("60016104002060005500")
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=bytes.fromhex("60016107c02060005500")
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=bytes.fromhex("60016107e02060005500")
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    storage={
                        0: 0xBC36789E7A1E281436464229828F817D6612F7B477D66591FF96A9E064BCC98A  # noqa: E501
                    },
                    code=bytes.fromhex("60016108002060005500"),
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=bytes.fromhex("60006104002060005500")
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=bytes.fromhex("60206107e02060005500")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "604060206010600f6000600435611000016001600003f100"
                    )
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000009",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("600060002060005500")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex("600560042060005500")
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("600a600a2060005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("620fffff6103e82060005500")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex("6064640fffffffff2060005500")
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex("640fffffffff6127102060005500")
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex(
                        "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2060005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex(
                        "60027fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2060005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600263010000002060005500")
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    storage={
                        0: 0xBC36789E7A1E281436464229828F817D6612F7B477D66591FF96A9E064BCC98A  # noqa: E501
                    },
                    code=bytes.fromhex("60016103c02060005500"),
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=bytes.fromhex("60016103e02060005500")
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=bytes.fromhex("60016104002060005500")
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=bytes.fromhex("60016107c02060005500")
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=bytes.fromhex("60016107e02060005500")
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=bytes.fromhex("60016108002060005500")
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=bytes.fromhex("60006104002060005500")
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=bytes.fromhex("60206107e02060005500")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "604060206010600f6000600435611000016001600003f100"
                    )
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000000a",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("600060002060005500")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex("600560042060005500")
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("600a600a2060005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("620fffff6103e82060005500")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex("6064640fffffffff2060005500")
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex("640fffffffff6127102060005500")
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex(
                        "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2060005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex(
                        "60027fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2060005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600263010000002060005500")
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=bytes.fromhex("60016103c02060005500")
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    storage={
                        0: 0xBC36789E7A1E281436464229828F817D6612F7B477D66591FF96A9E064BCC98A  # noqa: E501
                    },
                    code=bytes.fromhex("60016103e02060005500"),
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=bytes.fromhex("60016104002060005500")
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=bytes.fromhex("60016107c02060005500")
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=bytes.fromhex("60016107e02060005500")
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=bytes.fromhex("60016108002060005500")
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=bytes.fromhex("60006104002060005500")
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=bytes.fromhex("60206107e02060005500")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "604060206010600f6000600435611000016001600003f100"
                    )
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000001",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("600060002060005500")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    storage={
                        0: 0xC41589E7559804EA4A2080DAD19D876A024CCB05117835447D72CE08C1D020EC  # noqa: E501
                    },
                    code=bytes.fromhex("600560042060005500"),
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("600a600a2060005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("620fffff6103e82060005500")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex("6064640fffffffff2060005500")
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex("640fffffffff6127102060005500")
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex(
                        "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2060005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex(
                        "60027fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2060005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600263010000002060005500")
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=bytes.fromhex("60016103c02060005500")
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=bytes.fromhex("60016103e02060005500")
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=bytes.fromhex("60016104002060005500")
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=bytes.fromhex("60016107c02060005500")
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=bytes.fromhex("60016107e02060005500")
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=bytes.fromhex("60016108002060005500")
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=bytes.fromhex("60006104002060005500")
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=bytes.fromhex("60206107e02060005500")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "604060206010600f6000600435611000016001600003f100"
                    )
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000004",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("600060002060005500")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex("600560042060005500")
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("600a600a2060005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("620fffff6103e82060005500")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex("6064640fffffffff2060005500")
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex("640fffffffff6127102060005500")
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex(
                        "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2060005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex(
                        "60027fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2060005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600263010000002060005500")
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=bytes.fromhex("60016103c02060005500")
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=bytes.fromhex("60016103e02060005500")
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=bytes.fromhex("60016104002060005500")
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=bytes.fromhex("60016107c02060005500")
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=bytes.fromhex("60016107e02060005500")
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=bytes.fromhex("60016108002060005500")
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=bytes.fromhex("60006104002060005500")
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=bytes.fromhex("60206107e02060005500")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "604060206010600f6000600435611000016001600003f100"
                    )
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000005",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("600060002060005500")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex("600560042060005500")
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("600a600a2060005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("620fffff6103e82060005500")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex("6064640fffffffff2060005500")
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex("640fffffffff6127102060005500")
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex(
                        "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2060005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex(
                        "60027fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2060005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600263010000002060005500")
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=bytes.fromhex("60016103c02060005500")
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=bytes.fromhex("60016103e02060005500")
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=bytes.fromhex("60016104002060005500")
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=bytes.fromhex("60016107c02060005500")
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=bytes.fromhex("60016107e02060005500")
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=bytes.fromhex("60016108002060005500")
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=bytes.fromhex("60006104002060005500")
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=bytes.fromhex("60206107e02060005500")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "604060206010600f6000600435611000016001600003f100"
                    )
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000007",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("600060002060005500")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex("600560042060005500")
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("600a600a2060005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("620fffff6103e82060005500")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex("6064640fffffffff2060005500")
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex("640fffffffff6127102060005500")
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex(
                        "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2060005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex(
                        "60027fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2060005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600263010000002060005500")
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=bytes.fromhex("60016103c02060005500")
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=bytes.fromhex("60016103e02060005500")
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=bytes.fromhex("60016104002060005500")
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=bytes.fromhex("60016107c02060005500")
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=bytes.fromhex("60016107e02060005500")
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=bytes.fromhex("60016108002060005500")
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=bytes.fromhex("60006104002060005500")
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=bytes.fromhex("60206107e02060005500")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "604060206010600f6000600435611000016001600003f100"
                    )
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000006",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("600060002060005500")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex("600560042060005500")
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("600a600a2060005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("620fffff6103e82060005500")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex("6064640fffffffff2060005500")
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex("640fffffffff6127102060005500")
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex(
                        "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2060005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex(
                        "60027fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2060005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600263010000002060005500")
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=bytes.fromhex("60016103c02060005500")
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=bytes.fromhex("60016103e02060005500")
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=bytes.fromhex("60016104002060005500")
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=bytes.fromhex("60016107c02060005500")
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=bytes.fromhex("60016107e02060005500")
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=bytes.fromhex("60016108002060005500")
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=bytes.fromhex("60006104002060005500")
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=bytes.fromhex("60206107e02060005500")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "604060206010600f6000600435611000016001600003f100"
                    )
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
                    code=bytes.fromhex("600060002060005500"),
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex("600560042060005500")
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("600a600a2060005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("620fffff6103e82060005500")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex("6064640fffffffff2060005500")
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex("640fffffffff6127102060005500")
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex(
                        "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2060005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex(
                        "60027fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2060005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600263010000002060005500")
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=bytes.fromhex("60016103c02060005500")
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=bytes.fromhex("60016103e02060005500")
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=bytes.fromhex("60016104002060005500")
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=bytes.fromhex("60016107c02060005500")
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=bytes.fromhex("60016107e02060005500")
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=bytes.fromhex("60016108002060005500")
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=bytes.fromhex("60006104002060005500")
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=bytes.fromhex("60206107e02060005500")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "604060206010600f6000600435611000016001600003f100"
                    )
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000002",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("600060002060005500")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex("600560042060005500")
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    storage={
                        0: 0x6BD2DD6BD408CBEE33429358BF24FDC64612FBF8B1B4DB604518F40FFD34B607  # noqa: E501
                    },
                    code=bytes.fromhex("600a600a2060005500"),
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("620fffff6103e82060005500")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex("6064640fffffffff2060005500")
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex("640fffffffff6127102060005500")
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex(
                        "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2060005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex(
                        "60027fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2060005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600263010000002060005500")
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=bytes.fromhex("60016103c02060005500")
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=bytes.fromhex("60016103e02060005500")
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=bytes.fromhex("60016104002060005500")
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=bytes.fromhex("60016107c02060005500")
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=bytes.fromhex("60016107e02060005500")
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=bytes.fromhex("60016108002060005500")
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=bytes.fromhex("60006104002060005500")
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=bytes.fromhex("60206107e02060005500")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "604060206010600f6000600435611000016001600003f100"
                    )
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
        code=bytes.fromhex("600060002060005500"),
    )
    pre[callee_1] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("600560042060005500"),
    )
    pre[callee_2] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("600a600a2060005500"),
    )
    pre[callee_3] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("620fffff6103e82060005500"),
    )
    pre[callee_4] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("6064640fffffffff2060005500"),
    )
    pre[callee_5] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("640fffffffff6127102060005500"),
    )
    pre[callee_6] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex(
            "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2060005500"  # noqa: E501
        ),
    )
    pre[callee_7] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex(
            "60027fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff20"  # noqa: E501
            "60005500"
        ),
    )
    pre[callee_8] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("600263010000002060005500"),
    )
    pre[callee_9] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("60016103c02060005500"),
    )
    pre[callee_10] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("60016103e02060005500"),
    )
    pre[callee_11] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("60016104002060005500"),
    )
    pre[callee_12] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("60016107c02060005500"),
    )
    pre[callee_13] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("60016107e02060005500"),
    )
    pre[callee_14] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("60016108002060005500"),
    )
    pre[callee_15] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("60006104002060005500"),
    )
    pre[callee_16] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("60206107e02060005500"),
    )
    pre[sender] = Account(balance=0x100000000000, nonce=0)
    pre[contract] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("604060206010600f6000600435611000016001600003f100"),
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
