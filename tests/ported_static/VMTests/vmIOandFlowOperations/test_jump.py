"""
Ori Pomerantz qbzzt1@gmail.com.

Ported from:
tests/static/state_tests/VMTests/vmIOandFlowOperations/jumpFiller.yml
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
    ["tests/static/state_tests/VMTests/vmIOandFlowOperations/jumpFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000005",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("61600d6000556010602002565b00")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex("61600d60005560016010602002575b00")
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("600456005b61600d60005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("61600d600055630fffffff5600")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex("602360085660015b600255")
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex("61600d6000555b600656")
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex("61600d60085660ff5b600055")
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex("600b565b61600d600055005b600356")
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600260050156005b61600d600055")
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=bytes.fromhex("60055600605b61600d600055")
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=bytes.fromhex("60055600600161600d600055")
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=bytes.fromhex("61600d600055600b565a5b5a600155")
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=bytes.fromhex("61600d6000556009565a5b5a600155")
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=bytes.fromhex("6801000000000000000b565b5b6001600155")
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=bytes.fromhex("640100000007565b5b6001600155")
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=bytes.fromhex(
                        "600051506001600003506000515661600d60005500"
                    )
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=bytes.fromhex(
                        "600e565b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b61600d600055"
                    )
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 2989},
                    code=bytes.fromhex(
                        "60006000600060006004356110000162010000f400"
                    ),
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000000a",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("61600d6000556010602002565b00")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex("61600d60005560016010602002575b00")
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("600456005b61600d60005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("61600d600055630fffffff5600")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex("602360085660015b600255")
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex("61600d6000555b600656")
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex("61600d60085660ff5b600055")
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex("600b565b61600d600055005b600356")
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600260050156005b61600d600055")
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=bytes.fromhex("60055600605b61600d600055")
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=bytes.fromhex("60055600600161600d600055")
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=bytes.fromhex("61600d600055600b565a5b5a600155")
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=bytes.fromhex("61600d6000556009565a5b5a600155")
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=bytes.fromhex("6801000000000000000b565b5b6001600155")
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=bytes.fromhex("640100000007565b5b6001600155")
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=bytes.fromhex(
                        "600051506001600003506000515661600d60005500"
                    )
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=bytes.fromhex(
                        "600e565b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b61600d600055"
                    )
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 2989},
                    code=bytes.fromhex(
                        "60006000600060006004356110000162010000f400"
                    ),
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000009",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("61600d6000556010602002565b00")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex("61600d60005560016010602002575b00")
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("600456005b61600d60005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("61600d600055630fffffff5600")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex("602360085660015b600255")
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex("61600d6000555b600656")
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex("61600d60085660ff5b600055")
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex("600b565b61600d600055005b600356")
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600260050156005b61600d600055")
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=bytes.fromhex("60055600605b61600d600055")
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=bytes.fromhex("60055600600161600d600055")
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=bytes.fromhex("61600d600055600b565a5b5a600155")
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=bytes.fromhex("61600d6000556009565a5b5a600155")
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=bytes.fromhex("6801000000000000000b565b5b6001600155")
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=bytes.fromhex("640100000007565b5b6001600155")
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=bytes.fromhex(
                        "600051506001600003506000515661600d60005500"
                    )
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=bytes.fromhex(
                        "600e565b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b61600d600055"
                    )
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 2989},
                    code=bytes.fromhex(
                        "60006000600060006004356110000162010000f400"
                    ),
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000007",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("61600d6000556010602002565b00")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex("61600d60005560016010602002575b00")
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("600456005b61600d60005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("61600d600055630fffffff5600")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex("602360085660015b600255")
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex("61600d6000555b600656")
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex("61600d60085660ff5b600055")
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex("600b565b61600d600055005b600356")
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600260050156005b61600d600055")
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=bytes.fromhex("60055600605b61600d600055")
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=bytes.fromhex("60055600600161600d600055")
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=bytes.fromhex("61600d600055600b565a5b5a600155")
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=bytes.fromhex("61600d6000556009565a5b5a600155")
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=bytes.fromhex("6801000000000000000b565b5b6001600155")
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=bytes.fromhex("640100000007565b5b6001600155")
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=bytes.fromhex(
                        "600051506001600003506000515661600d60005500"
                    )
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=bytes.fromhex(
                        "600e565b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b61600d600055"
                    )
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 24589},
                    code=bytes.fromhex(
                        "60006000600060006004356110000162010000f400"
                    ),
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000006",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("61600d6000556010602002565b00")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex("61600d60005560016010602002575b00")
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("600456005b61600d60005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("61600d600055630fffffff5600")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex("602360085660015b600255")
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex("61600d6000555b600656")
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex("61600d60085660ff5b600055")
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex("600b565b61600d600055005b600356")
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600260050156005b61600d600055")
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=bytes.fromhex("60055600605b61600d600055")
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=bytes.fromhex("60055600600161600d600055")
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=bytes.fromhex("61600d600055600b565a5b5a600155")
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=bytes.fromhex("61600d6000556009565a5b5a600155")
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=bytes.fromhex("6801000000000000000b565b5b6001600155")
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=bytes.fromhex("640100000007565b5b6001600155")
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=bytes.fromhex(
                        "600051506001600003506000515661600d60005500"
                    )
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=bytes.fromhex(
                        "600e565b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b61600d600055"
                    )
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 24589},
                    code=bytes.fromhex(
                        "60006000600060006004356110000162010000f400"
                    ),
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000008",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("61600d6000556010602002565b00")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex("61600d60005560016010602002575b00")
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("600456005b61600d60005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("61600d600055630fffffff5600")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex("602360085660015b600255")
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex("61600d6000555b600656")
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex("61600d60085660ff5b600055")
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex("600b565b61600d600055005b600356")
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600260050156005b61600d600055")
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=bytes.fromhex("60055600605b61600d600055")
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=bytes.fromhex("60055600600161600d600055")
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=bytes.fromhex("61600d600055600b565a5b5a600155")
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=bytes.fromhex("61600d6000556009565a5b5a600155")
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=bytes.fromhex("6801000000000000000b565b5b6001600155")
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=bytes.fromhex("640100000007565b5b6001600155")
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=bytes.fromhex(
                        "600051506001600003506000515661600d60005500"
                    )
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=bytes.fromhex(
                        "600e565b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b61600d600055"
                    )
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 24589},
                    code=bytes.fromhex(
                        "60006000600060006004356110000162010000f400"
                    ),
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000001",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("61600d6000556010602002565b00")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex("61600d60005560016010602002575b00")
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("600456005b61600d60005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("61600d600055630fffffff5600")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex("602360085660015b600255")
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex("61600d6000555b600656")
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex("61600d60085660ff5b600055")
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex("600b565b61600d600055005b600356")
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600260050156005b61600d600055")
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=bytes.fromhex("60055600605b61600d600055")
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=bytes.fromhex("60055600600161600d600055")
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=bytes.fromhex("61600d600055600b565a5b5a600155")
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=bytes.fromhex("61600d6000556009565a5b5a600155")
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=bytes.fromhex("6801000000000000000b565b5b6001600155")
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=bytes.fromhex("640100000007565b5b6001600155")
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=bytes.fromhex(
                        "600051506001600003506000515661600d60005500"
                    )
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=bytes.fromhex(
                        "600e565b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b61600d600055"
                    )
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 2989},
                    code=bytes.fromhex(
                        "60006000600060006004356110000162010000f400"
                    ),
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000003",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("61600d6000556010602002565b00")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex("61600d60005560016010602002575b00")
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("600456005b61600d60005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("61600d600055630fffffff5600")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex("602360085660015b600255")
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex("61600d6000555b600656")
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex("61600d60085660ff5b600055")
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex("600b565b61600d600055005b600356")
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600260050156005b61600d600055")
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=bytes.fromhex("60055600605b61600d600055")
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=bytes.fromhex("60055600600161600d600055")
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=bytes.fromhex("61600d600055600b565a5b5a600155")
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=bytes.fromhex("61600d6000556009565a5b5a600155")
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=bytes.fromhex("6801000000000000000b565b5b6001600155")
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=bytes.fromhex("640100000007565b5b6001600155")
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=bytes.fromhex(
                        "600051506001600003506000515661600d60005500"
                    )
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=bytes.fromhex(
                        "600e565b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b61600d600055"
                    )
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 2989},
                    code=bytes.fromhex(
                        "60006000600060006004356110000162010000f400"
                    ),
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000000d",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("61600d6000556010602002565b00")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex("61600d60005560016010602002575b00")
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("600456005b61600d60005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("61600d600055630fffffff5600")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex("602360085660015b600255")
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex("61600d6000555b600656")
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex("61600d60085660ff5b600055")
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex("600b565b61600d600055005b600356")
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600260050156005b61600d600055")
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=bytes.fromhex("60055600605b61600d600055")
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=bytes.fromhex("60055600600161600d600055")
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=bytes.fromhex("61600d600055600b565a5b5a600155")
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=bytes.fromhex("61600d6000556009565a5b5a600155")
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=bytes.fromhex("6801000000000000000b565b5b6001600155")
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=bytes.fromhex("640100000007565b5b6001600155")
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=bytes.fromhex(
                        "600051506001600003506000515661600d60005500"
                    )
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=bytes.fromhex(
                        "600e565b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b61600d600055"
                    )
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 2989},
                    code=bytes.fromhex(
                        "60006000600060006004356110000162010000f400"
                    ),
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000000e",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("61600d6000556010602002565b00")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex("61600d60005560016010602002575b00")
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("600456005b61600d60005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("61600d600055630fffffff5600")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex("602360085660015b600255")
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex("61600d6000555b600656")
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex("61600d60085660ff5b600055")
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex("600b565b61600d600055005b600356")
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600260050156005b61600d600055")
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=bytes.fromhex("60055600605b61600d600055")
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=bytes.fromhex("60055600600161600d600055")
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=bytes.fromhex("61600d600055600b565a5b5a600155")
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=bytes.fromhex("61600d6000556009565a5b5a600155")
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=bytes.fromhex("6801000000000000000b565b5b6001600155")
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=bytes.fromhex("640100000007565b5b6001600155")
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=bytes.fromhex(
                        "600051506001600003506000515661600d60005500"
                    )
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=bytes.fromhex(
                        "600e565b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b61600d600055"
                    )
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 2989},
                    code=bytes.fromhex(
                        "60006000600060006004356110000162010000f400"
                    ),
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000000f",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("61600d6000556010602002565b00")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex("61600d60005560016010602002575b00")
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("600456005b61600d60005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("61600d600055630fffffff5600")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex("602360085660015b600255")
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex("61600d6000555b600656")
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex("61600d60085660ff5b600055")
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex("600b565b61600d600055005b600356")
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600260050156005b61600d600055")
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=bytes.fromhex("60055600605b61600d600055")
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=bytes.fromhex("60055600600161600d600055")
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=bytes.fromhex("61600d600055600b565a5b5a600155")
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=bytes.fromhex("61600d6000556009565a5b5a600155")
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=bytes.fromhex("6801000000000000000b565b5b6001600155")
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=bytes.fromhex("640100000007565b5b6001600155")
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=bytes.fromhex(
                        "600051506001600003506000515661600d60005500"
                    )
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=bytes.fromhex(
                        "600e565b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b61600d600055"
                    )
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 2989},
                    code=bytes.fromhex(
                        "60006000600060006004356110000162010000f400"
                    ),
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000000",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("61600d6000556010602002565b00")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex("61600d60005560016010602002575b00")
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("600456005b61600d60005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("61600d600055630fffffff5600")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex("602360085660015b600255")
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex("61600d6000555b600656")
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex("61600d60085660ff5b600055")
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex("600b565b61600d600055005b600356")
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600260050156005b61600d600055")
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=bytes.fromhex("60055600605b61600d600055")
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=bytes.fromhex("60055600600161600d600055")
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=bytes.fromhex("61600d600055600b565a5b5a600155")
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=bytes.fromhex("61600d6000556009565a5b5a600155")
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=bytes.fromhex("6801000000000000000b565b5b6001600155")
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=bytes.fromhex("640100000007565b5b6001600155")
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=bytes.fromhex(
                        "600051506001600003506000515661600d60005500"
                    )
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=bytes.fromhex(
                        "600e565b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b61600d600055"
                    )
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 2989},
                    code=bytes.fromhex(
                        "60006000600060006004356110000162010000f400"
                    ),
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000000b",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("61600d6000556010602002565b00")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex("61600d60005560016010602002575b00")
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("600456005b61600d60005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("61600d600055630fffffff5600")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex("602360085660015b600255")
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex("61600d6000555b600656")
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex("61600d60085660ff5b600055")
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex("600b565b61600d600055005b600356")
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600260050156005b61600d600055")
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=bytes.fromhex("60055600605b61600d600055")
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=bytes.fromhex("60055600600161600d600055")
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=bytes.fromhex("61600d600055600b565a5b5a600155")
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=bytes.fromhex("61600d6000556009565a5b5a600155")
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=bytes.fromhex("6801000000000000000b565b5b6001600155")
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=bytes.fromhex("640100000007565b5b6001600155")
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=bytes.fromhex(
                        "600051506001600003506000515661600d60005500"
                    )
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=bytes.fromhex(
                        "600e565b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b61600d600055"
                    )
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 2989},
                    code=bytes.fromhex(
                        "60006000600060006004356110000162010000f400"
                    ),
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000000c",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("61600d6000556010602002565b00")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex("61600d60005560016010602002575b00")
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("600456005b61600d60005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("61600d600055630fffffff5600")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex("602360085660015b600255")
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex("61600d6000555b600656")
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex("61600d60085660ff5b600055")
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex("600b565b61600d600055005b600356")
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600260050156005b61600d600055")
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=bytes.fromhex("60055600605b61600d600055")
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=bytes.fromhex("60055600600161600d600055")
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=bytes.fromhex("61600d600055600b565a5b5a600155")
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=bytes.fromhex("61600d6000556009565a5b5a600155")
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=bytes.fromhex("6801000000000000000b565b5b6001600155")
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=bytes.fromhex("640100000007565b5b6001600155")
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=bytes.fromhex(
                        "600051506001600003506000515661600d60005500"
                    )
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=bytes.fromhex(
                        "600e565b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b61600d600055"
                    )
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 2989},
                    code=bytes.fromhex(
                        "60006000600060006004356110000162010000f400"
                    ),
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000004",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("61600d6000556010602002565b00")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex("61600d60005560016010602002575b00")
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("600456005b61600d60005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("61600d600055630fffffff5600")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex("602360085660015b600255")
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex("61600d6000555b600656")
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex("61600d60085660ff5b600055")
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex("600b565b61600d600055005b600356")
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600260050156005b61600d600055")
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=bytes.fromhex("60055600605b61600d600055")
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=bytes.fromhex("60055600600161600d600055")
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=bytes.fromhex("61600d600055600b565a5b5a600155")
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=bytes.fromhex("61600d6000556009565a5b5a600155")
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=bytes.fromhex("6801000000000000000b565b5b6001600155")
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=bytes.fromhex("640100000007565b5b6001600155")
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=bytes.fromhex(
                        "600051506001600003506000515661600d60005500"
                    )
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=bytes.fromhex(
                        "600e565b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b61600d600055"
                    )
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 2989},
                    code=bytes.fromhex(
                        "60006000600060006004356110000162010000f400"
                    ),
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000002",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("61600d6000556010602002565b00")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex("61600d60005560016010602002575b00")
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("600456005b61600d60005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("61600d600055630fffffff5600")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex("602360085660015b600255")
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex("61600d6000555b600656")
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex("61600d60085660ff5b600055")
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex("600b565b61600d600055005b600356")
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600260050156005b61600d600055")
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=bytes.fromhex("60055600605b61600d600055")
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=bytes.fromhex("60055600600161600d600055")
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=bytes.fromhex("61600d600055600b565a5b5a600155")
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=bytes.fromhex("61600d6000556009565a5b5a600155")
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=bytes.fromhex("6801000000000000000b565b5b6001600155")
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=bytes.fromhex("640100000007565b5b6001600155")
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=bytes.fromhex(
                        "600051506001600003506000515661600d60005500"
                    )
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=bytes.fromhex(
                        "600e565b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b61600d600055"
                    )
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 24589},
                    code=bytes.fromhex(
                        "60006000600060006004356110000162010000f400"
                    ),
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000010",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("61600d6000556010602002565b00")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex("61600d60005560016010602002575b00")
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("600456005b61600d60005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("61600d600055630fffffff5600")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex("602360085660015b600255")
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex("61600d6000555b600656")
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex("61600d60085660ff5b600055")
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex("600b565b61600d600055005b600356")
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600260050156005b61600d600055")
                ),
                Address("0x0000000000000000000000000000000000001009"): Account(
                    code=bytes.fromhex("60055600605b61600d600055")
                ),
                Address("0x000000000000000000000000000000000000100a"): Account(
                    code=bytes.fromhex("60055600600161600d600055")
                ),
                Address("0x000000000000000000000000000000000000100b"): Account(
                    code=bytes.fromhex("61600d600055600b565a5b5a600155")
                ),
                Address("0x000000000000000000000000000000000000100c"): Account(
                    code=bytes.fromhex("61600d6000556009565a5b5a600155")
                ),
                Address("0x000000000000000000000000000000000000100d"): Account(
                    code=bytes.fromhex("6801000000000000000b565b5b6001600155")
                ),
                Address("0x000000000000000000000000000000000000100e"): Account(
                    code=bytes.fromhex("640100000007565b5b6001600155")
                ),
                Address("0x000000000000000000000000000000000000100f"): Account(
                    code=bytes.fromhex(
                        "600051506001600003506000515661600d60005500"
                    )
                ),
                Address("0x0000000000000000000000000000000000001010"): Account(
                    code=bytes.fromhex(
                        "600e565b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b61600d600055"
                    )
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 24589},
                    code=bytes.fromhex(
                        "60006000600060006004356110000162010000f400"
                    ),
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
def test_jump(
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
        code=bytes.fromhex("61600d6000556010602002565b00"),
    )
    pre[callee_1] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("61600d60005560016010602002575b00"),
    )
    pre[callee_2] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("600456005b61600d60005500"),
    )
    pre[callee_3] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("61600d600055630fffffff5600"),
    )
    pre[callee_4] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("602360085660015b600255"),
    )
    pre[callee_5] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("61600d6000555b600656"),
    )
    pre[callee_6] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("61600d60085660ff5b600055"),
    )
    pre[callee_7] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("600b565b61600d600055005b600356"),
    )
    pre[callee_8] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("600260050156005b61600d600055"),
    )
    pre[callee_9] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("60055600605b61600d600055"),
    )
    pre[callee_10] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("60055600600161600d600055"),
    )
    pre[callee_11] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("61600d600055600b565a5b5a600155"),
    )
    pre[callee_12] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("61600d6000556009565a5b5a600155"),
    )
    pre[callee_13] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("6801000000000000000b565b5b6001600155"),
    )
    pre[callee_14] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("640100000007565b5b6001600155"),
    )
    pre[callee_15] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("600051506001600003506000515661600d60005500"),
    )
    pre[callee_16] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex(
            "600e565b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b61600d600055"
        ),
    )
    pre[sender] = Account(balance=0x100000000000, nonce=0)
    pre[contract] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("60006000600060006004356110000162010000f400"),
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
