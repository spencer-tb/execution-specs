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
                    code=bytes.fromhex("63deadbeef6000526101006000f3")
                ),
                Address("0x0000000000000000000000000000000000c0de20"): Account(
                    code=bytes.fromhex("61beef60002000")
                ),
                Address("0x0000000000000000000000000000000000c0de3b"): Account(
                    code=bytes.fromhex("61ca11600080823b923c00")
                ),
                Address("0x0000000000000000000000000000000000c0de51"): Account(
                    code=bytes.fromhex("61beef5100")
                ),
                Address("0x0000000000000000000000000000000000c0de52"): Account(
                    code=bytes.fromhex("60ff61beef5200")
                ),
                Address("0x0000000000000000000000000000000000c0de53"): Account(
                    code=bytes.fromhex("60ff61beef5300")
                ),
                Address("0x0000000000000000000000000000000000c0def0"): Account(
                    code=bytes.fromhex("610200600080f060005500")
                ),
                Address("0x0000000000000000000000000000000000c0def1"): Account(
                    code=bytes.fromhex("610100600081818061ca115af100")
                ),
                Address("0x0000000000000000000000000000000000c0def2"): Account(
                    code=bytes.fromhex("610100600081818061ca115af200")
                ),
                Address("0x0000000000000000000000000000000000c0def4"): Account(
                    code=bytes.fromhex("6101006000818161ca115af400")
                ),
                Address("0x0000000000000000000000000000000000c0def5"): Account(
                    code=bytes.fromhex("615a17610200600080f560005500")
                ),
                Address("0x0000000000000000000000000000000000c0defa"): Account(
                    code=bytes.fromhex("6101006000818161ca115afa00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 2700},
                    code=bytes.fromhex(
                        "60443560243562c0de00600435016000805b14601c575003600055005b60008381808080808789f1930192601156"  # noqa: E501
                    ),
                ),
            },
        ),
        (
            "048071d300000000000000000000000000000000000000000000000000000000000000f100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000064",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000ca11"): Account(
                    code=bytes.fromhex("63deadbeef6000526101006000f3")
                ),
                Address("0x0000000000000000000000000000000000c0de20"): Account(
                    code=bytes.fromhex("61beef60002000")
                ),
                Address("0x0000000000000000000000000000000000c0de3b"): Account(
                    code=bytes.fromhex("61ca11600080823b923c00")
                ),
                Address("0x0000000000000000000000000000000000c0de51"): Account(
                    code=bytes.fromhex("61beef5100")
                ),
                Address("0x0000000000000000000000000000000000c0de52"): Account(
                    code=bytes.fromhex("60ff61beef5200")
                ),
                Address("0x0000000000000000000000000000000000c0de53"): Account(
                    code=bytes.fromhex("60ff61beef5300")
                ),
                Address("0x0000000000000000000000000000000000c0def0"): Account(
                    code=bytes.fromhex("610200600080f060005500")
                ),
                Address("0x0000000000000000000000000000000000c0def1"): Account(
                    code=bytes.fromhex("610100600081818061ca115af100")
                ),
                Address("0x0000000000000000000000000000000000c0def2"): Account(
                    code=bytes.fromhex("610100600081818061ca115af200")
                ),
                Address("0x0000000000000000000000000000000000c0def4"): Account(
                    code=bytes.fromhex("6101006000818161ca115af400")
                ),
                Address("0x0000000000000000000000000000000000c0def5"): Account(
                    code=bytes.fromhex("615a17610200600080f560005500")
                ),
                Address("0x0000000000000000000000000000000000c0defa"): Account(
                    code=bytes.fromhex("6101006000818161ca115afa00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 2700},
                    code=bytes.fromhex(
                        "60443560243562c0de00600435016000805b14601c575003600055005b60008381808080808789f1930192601156"  # noqa: E501
                    ),
                ),
            },
        ),
        (
            "048071d300000000000000000000000000000000000000000000000000000000000000f500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000064",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000ca11"): Account(
                    code=bytes.fromhex("63deadbeef6000526101006000f3")
                ),
                Address("0x0000000000000000000000000000000000c0de20"): Account(
                    code=bytes.fromhex("61beef60002000")
                ),
                Address("0x0000000000000000000000000000000000c0de3b"): Account(
                    code=bytes.fromhex("61ca11600080823b923c00")
                ),
                Address("0x0000000000000000000000000000000000c0de51"): Account(
                    code=bytes.fromhex("61beef5100")
                ),
                Address("0x0000000000000000000000000000000000c0de52"): Account(
                    code=bytes.fromhex("60ff61beef5200")
                ),
                Address("0x0000000000000000000000000000000000c0de53"): Account(
                    code=bytes.fromhex("60ff61beef5300")
                ),
                Address("0x0000000000000000000000000000000000c0def0"): Account(
                    code=bytes.fromhex("610200600080f060005500")
                ),
                Address("0x0000000000000000000000000000000000c0def1"): Account(
                    code=bytes.fromhex("610100600081818061ca115af100")
                ),
                Address("0x0000000000000000000000000000000000c0def2"): Account(
                    code=bytes.fromhex("610100600081818061ca115af200")
                ),
                Address("0x0000000000000000000000000000000000c0def4"): Account(
                    code=bytes.fromhex("6101006000818161ca115af400")
                ),
                Address("0x0000000000000000000000000000000000c0def5"): Account(
                    storage={0: 0x1C1BD7A2F25CA2F4577AD12388656BC147F96DAB},
                    code=bytes.fromhex("615a17610200600080f560005500"),
                ),
                Address("0x0000000000000000000000000000000000c0defa"): Account(
                    code=bytes.fromhex("6101006000818161ca115afa00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 54300},
                    code=bytes.fromhex(
                        "60443560243562c0de00600435016000805b14601c575003600055005b60008381808080808789f1930192601156"  # noqa: E501
                    ),
                ),
            },
        ),
        (
            "048071d300000000000000000000000000000000000000000000000000000000000000f000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000064",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000ca11"): Account(
                    code=bytes.fromhex("63deadbeef6000526101006000f3")
                ),
                Address("0x0000000000000000000000000000000000c0de20"): Account(
                    code=bytes.fromhex("61beef60002000")
                ),
                Address("0x0000000000000000000000000000000000c0de3b"): Account(
                    code=bytes.fromhex("61ca11600080823b923c00")
                ),
                Address("0x0000000000000000000000000000000000c0de51"): Account(
                    code=bytes.fromhex("61beef5100")
                ),
                Address("0x0000000000000000000000000000000000c0de52"): Account(
                    code=bytes.fromhex("60ff61beef5200")
                ),
                Address("0x0000000000000000000000000000000000c0de53"): Account(
                    code=bytes.fromhex("60ff61beef5300")
                ),
                Address("0x0000000000000000000000000000000000c0def0"): Account(
                    storage={0: 0xB44F2C88D3D4283CD1E54E418C4FF7E6A6C73202},
                    code=bytes.fromhex("610200600080f060005500"),
                ),
                Address("0x0000000000000000000000000000000000c0def1"): Account(
                    code=bytes.fromhex("610100600081818061ca115af100")
                ),
                Address("0x0000000000000000000000000000000000c0def2"): Account(
                    code=bytes.fromhex("610100600081818061ca115af200")
                ),
                Address("0x0000000000000000000000000000000000c0def4"): Account(
                    code=bytes.fromhex("6101006000818161ca115af400")
                ),
                Address("0x0000000000000000000000000000000000c0def5"): Account(
                    code=bytes.fromhex("615a17610200600080f560005500")
                ),
                Address("0x0000000000000000000000000000000000c0defa"): Account(
                    code=bytes.fromhex("6101006000818161ca115afa00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 54200},
                    code=bytes.fromhex(
                        "60443560243562c0de00600435016000805b14601c575003600055005b60008381808080808789f1930192601156"  # noqa: E501
                    ),
                ),
            },
        ),
        (
            "048071d300000000000000000000000000000000000000000000000000000000000000f400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000064",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000ca11"): Account(
                    code=bytes.fromhex("63deadbeef6000526101006000f3")
                ),
                Address("0x0000000000000000000000000000000000c0de20"): Account(
                    code=bytes.fromhex("61beef60002000")
                ),
                Address("0x0000000000000000000000000000000000c0de3b"): Account(
                    code=bytes.fromhex("61ca11600080823b923c00")
                ),
                Address("0x0000000000000000000000000000000000c0de51"): Account(
                    code=bytes.fromhex("61beef5100")
                ),
                Address("0x0000000000000000000000000000000000c0de52"): Account(
                    code=bytes.fromhex("60ff61beef5200")
                ),
                Address("0x0000000000000000000000000000000000c0de53"): Account(
                    code=bytes.fromhex("60ff61beef5300")
                ),
                Address("0x0000000000000000000000000000000000c0def0"): Account(
                    code=bytes.fromhex("610200600080f060005500")
                ),
                Address("0x0000000000000000000000000000000000c0def1"): Account(
                    code=bytes.fromhex("610100600081818061ca115af100")
                ),
                Address("0x0000000000000000000000000000000000c0def2"): Account(
                    code=bytes.fromhex("610100600081818061ca115af200")
                ),
                Address("0x0000000000000000000000000000000000c0def4"): Account(
                    code=bytes.fromhex("6101006000818161ca115af400")
                ),
                Address("0x0000000000000000000000000000000000c0def5"): Account(
                    code=bytes.fromhex("615a17610200600080f560005500")
                ),
                Address("0x0000000000000000000000000000000000c0defa"): Account(
                    code=bytes.fromhex("6101006000818161ca115afa00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 2700},
                    code=bytes.fromhex(
                        "60443560243562c0de00600435016000805b14601c575003600055005b60008381808080808789f1930192601156"  # noqa: E501
                    ),
                ),
            },
        ),
        (
            "048071d3000000000000000000000000000000000000000000000000000000000000003b00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000064",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000ca11"): Account(
                    code=bytes.fromhex("63deadbeef6000526101006000f3")
                ),
                Address("0x0000000000000000000000000000000000c0de20"): Account(
                    code=bytes.fromhex("61beef60002000")
                ),
                Address("0x0000000000000000000000000000000000c0de3b"): Account(
                    code=bytes.fromhex("61ca11600080823b923c00")
                ),
                Address("0x0000000000000000000000000000000000c0de51"): Account(
                    code=bytes.fromhex("61beef5100")
                ),
                Address("0x0000000000000000000000000000000000c0de52"): Account(
                    code=bytes.fromhex("60ff61beef5200")
                ),
                Address("0x0000000000000000000000000000000000c0de53"): Account(
                    code=bytes.fromhex("60ff61beef5300")
                ),
                Address("0x0000000000000000000000000000000000c0def0"): Account(
                    code=bytes.fromhex("610200600080f060005500")
                ),
                Address("0x0000000000000000000000000000000000c0def1"): Account(
                    code=bytes.fromhex("610100600081818061ca115af100")
                ),
                Address("0x0000000000000000000000000000000000c0def2"): Account(
                    code=bytes.fromhex("610100600081818061ca115af200")
                ),
                Address("0x0000000000000000000000000000000000c0def4"): Account(
                    code=bytes.fromhex("6101006000818161ca115af400")
                ),
                Address("0x0000000000000000000000000000000000c0def5"): Account(
                    code=bytes.fromhex("615a17610200600080f560005500")
                ),
                Address("0x0000000000000000000000000000000000c0defa"): Account(
                    code=bytes.fromhex("6101006000818161ca115afa00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 2800},
                    code=bytes.fromhex(
                        "60443560243562c0de00600435016000805b14601c575003600055005b60008381808080808789f1930192601156"  # noqa: E501
                    ),
                ),
            },
        ),
        (
            "048071d3000000000000000000000000000000000000000000000000000000000000005100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000064",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000ca11"): Account(
                    code=bytes.fromhex("63deadbeef6000526101006000f3")
                ),
                Address("0x0000000000000000000000000000000000c0de20"): Account(
                    code=bytes.fromhex("61beef60002000")
                ),
                Address("0x0000000000000000000000000000000000c0de3b"): Account(
                    code=bytes.fromhex("61ca11600080823b923c00")
                ),
                Address("0x0000000000000000000000000000000000c0de51"): Account(
                    code=bytes.fromhex("61beef5100")
                ),
                Address("0x0000000000000000000000000000000000c0de52"): Account(
                    code=bytes.fromhex("60ff61beef5200")
                ),
                Address("0x0000000000000000000000000000000000c0de53"): Account(
                    code=bytes.fromhex("60ff61beef5300")
                ),
                Address("0x0000000000000000000000000000000000c0def0"): Account(
                    code=bytes.fromhex("610200600080f060005500")
                ),
                Address("0x0000000000000000000000000000000000c0def1"): Account(
                    code=bytes.fromhex("610100600081818061ca115af100")
                ),
                Address("0x0000000000000000000000000000000000c0def2"): Account(
                    code=bytes.fromhex("610100600081818061ca115af200")
                ),
                Address("0x0000000000000000000000000000000000c0def4"): Account(
                    code=bytes.fromhex("6101006000818161ca115af400")
                ),
                Address("0x0000000000000000000000000000000000c0def5"): Account(
                    code=bytes.fromhex("615a17610200600080f560005500")
                ),
                Address("0x0000000000000000000000000000000000c0defa"): Account(
                    code=bytes.fromhex("6101006000818161ca115afa00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 9200},
                    code=bytes.fromhex(
                        "60443560243562c0de00600435016000805b14601c575003600055005b60008381808080808789f1930192601156"  # noqa: E501
                    ),
                ),
            },
        ),
        (
            "048071d3000000000000000000000000000000000000000000000000000000000000005300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000064",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000ca11"): Account(
                    code=bytes.fromhex("63deadbeef6000526101006000f3")
                ),
                Address("0x0000000000000000000000000000000000c0de20"): Account(
                    code=bytes.fromhex("61beef60002000")
                ),
                Address("0x0000000000000000000000000000000000c0de3b"): Account(
                    code=bytes.fromhex("61ca11600080823b923c00")
                ),
                Address("0x0000000000000000000000000000000000c0de51"): Account(
                    code=bytes.fromhex("61beef5100")
                ),
                Address("0x0000000000000000000000000000000000c0de52"): Account(
                    code=bytes.fromhex("60ff61beef5200")
                ),
                Address("0x0000000000000000000000000000000000c0de53"): Account(
                    code=bytes.fromhex("60ff61beef5300")
                ),
                Address("0x0000000000000000000000000000000000c0def0"): Account(
                    code=bytes.fromhex("610200600080f060005500")
                ),
                Address("0x0000000000000000000000000000000000c0def1"): Account(
                    code=bytes.fromhex("610100600081818061ca115af100")
                ),
                Address("0x0000000000000000000000000000000000c0def2"): Account(
                    code=bytes.fromhex("610100600081818061ca115af200")
                ),
                Address("0x0000000000000000000000000000000000c0def4"): Account(
                    code=bytes.fromhex("6101006000818161ca115af400")
                ),
                Address("0x0000000000000000000000000000000000c0def5"): Account(
                    code=bytes.fromhex("615a17610200600080f560005500")
                ),
                Address("0x0000000000000000000000000000000000c0defa"): Account(
                    code=bytes.fromhex("6101006000818161ca115afa00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 9200},
                    code=bytes.fromhex(
                        "60443560243562c0de00600435016000805b14601c575003600055005b60008381808080808789f1930192601156"  # noqa: E501
                    ),
                ),
            },
        ),
        (
            "048071d3000000000000000000000000000000000000000000000000000000000000005200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000064",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000ca11"): Account(
                    code=bytes.fromhex("63deadbeef6000526101006000f3")
                ),
                Address("0x0000000000000000000000000000000000c0de20"): Account(
                    code=bytes.fromhex("61beef60002000")
                ),
                Address("0x0000000000000000000000000000000000c0de3b"): Account(
                    code=bytes.fromhex("61ca11600080823b923c00")
                ),
                Address("0x0000000000000000000000000000000000c0de51"): Account(
                    code=bytes.fromhex("61beef5100")
                ),
                Address("0x0000000000000000000000000000000000c0de52"): Account(
                    code=bytes.fromhex("60ff61beef5200")
                ),
                Address("0x0000000000000000000000000000000000c0de53"): Account(
                    code=bytes.fromhex("60ff61beef5300")
                ),
                Address("0x0000000000000000000000000000000000c0def0"): Account(
                    code=bytes.fromhex("610200600080f060005500")
                ),
                Address("0x0000000000000000000000000000000000c0def1"): Account(
                    code=bytes.fromhex("610100600081818061ca115af100")
                ),
                Address("0x0000000000000000000000000000000000c0def2"): Account(
                    code=bytes.fromhex("610100600081818061ca115af200")
                ),
                Address("0x0000000000000000000000000000000000c0def4"): Account(
                    code=bytes.fromhex("6101006000818161ca115af400")
                ),
                Address("0x0000000000000000000000000000000000c0def5"): Account(
                    code=bytes.fromhex("615a17610200600080f560005500")
                ),
                Address("0x0000000000000000000000000000000000c0defa"): Account(
                    code=bytes.fromhex("6101006000818161ca115afa00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 9200},
                    code=bytes.fromhex(
                        "60443560243562c0de00600435016000805b14601c575003600055005b60008381808080808789f1930192601156"  # noqa: E501
                    ),
                ),
            },
        ),
        (
            "048071d3000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000064",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000ca11"): Account(
                    code=bytes.fromhex("63deadbeef6000526101006000f3")
                ),
                Address("0x0000000000000000000000000000000000c0de20"): Account(
                    code=bytes.fromhex("61beef60002000")
                ),
                Address("0x0000000000000000000000000000000000c0de3b"): Account(
                    code=bytes.fromhex("61ca11600080823b923c00")
                ),
                Address("0x0000000000000000000000000000000000c0de51"): Account(
                    code=bytes.fromhex("61beef5100")
                ),
                Address("0x0000000000000000000000000000000000c0de52"): Account(
                    code=bytes.fromhex("60ff61beef5200")
                ),
                Address("0x0000000000000000000000000000000000c0de53"): Account(
                    code=bytes.fromhex("60ff61beef5300")
                ),
                Address("0x0000000000000000000000000000000000c0def0"): Account(
                    code=bytes.fromhex("610200600080f060005500")
                ),
                Address("0x0000000000000000000000000000000000c0def1"): Account(
                    code=bytes.fromhex("610100600081818061ca115af100")
                ),
                Address("0x0000000000000000000000000000000000c0def2"): Account(
                    code=bytes.fromhex("610100600081818061ca115af200")
                ),
                Address("0x0000000000000000000000000000000000c0def4"): Account(
                    code=bytes.fromhex("6101006000818161ca115af400")
                ),
                Address("0x0000000000000000000000000000000000c0def5"): Account(
                    code=bytes.fromhex("615a17610200600080f560005500")
                ),
                Address("0x0000000000000000000000000000000000c0defa"): Account(
                    code=bytes.fromhex("6101006000818161ca115afa00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 18400},
                    code=bytes.fromhex(
                        "60443560243562c0de00600435016000805b14601c575003600055005b60008381808080808789f1930192601156"  # noqa: E501
                    ),
                ),
            },
        ),
        (
            "048071d300000000000000000000000000000000000000000000000000000000000000fa00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000064",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000ca11"): Account(
                    code=bytes.fromhex("63deadbeef6000526101006000f3")
                ),
                Address("0x0000000000000000000000000000000000c0de20"): Account(
                    code=bytes.fromhex("61beef60002000")
                ),
                Address("0x0000000000000000000000000000000000c0de3b"): Account(
                    code=bytes.fromhex("61ca11600080823b923c00")
                ),
                Address("0x0000000000000000000000000000000000c0de51"): Account(
                    code=bytes.fromhex("61beef5100")
                ),
                Address("0x0000000000000000000000000000000000c0de52"): Account(
                    code=bytes.fromhex("60ff61beef5200")
                ),
                Address("0x0000000000000000000000000000000000c0de53"): Account(
                    code=bytes.fromhex("60ff61beef5300")
                ),
                Address("0x0000000000000000000000000000000000c0def0"): Account(
                    code=bytes.fromhex("610200600080f060005500")
                ),
                Address("0x0000000000000000000000000000000000c0def1"): Account(
                    code=bytes.fromhex("610100600081818061ca115af100")
                ),
                Address("0x0000000000000000000000000000000000c0def2"): Account(
                    code=bytes.fromhex("610100600081818061ca115af200")
                ),
                Address("0x0000000000000000000000000000000000c0def4"): Account(
                    code=bytes.fromhex("6101006000818161ca115af400")
                ),
                Address("0x0000000000000000000000000000000000c0def5"): Account(
                    code=bytes.fromhex("615a17610200600080f560005500")
                ),
                Address("0x0000000000000000000000000000000000c0defa"): Account(
                    code=bytes.fromhex("6101006000818161ca115afa00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 2700},
                    code=bytes.fromhex(
                        "60443560243562c0de00600435016000805b14601c575003600055005b60008381808080808789f1930192601156"  # noqa: E501
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

    pre[callee] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex("63deadbeef6000526101006000f3"),
    )
    pre[callee_1] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex("61beef60002000"),
    )
    pre[callee_2] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex("61ca11600080823b923c00"),
    )
    pre[callee_3] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex("61beef5100"),
    )
    pre[callee_4] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex("60ff61beef5200"),
    )
    pre[callee_5] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex("60ff61beef5300"),
    )
    pre[callee_6] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex("610200600080f060005500"),
    )
    pre[callee_7] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex("610100600081818061ca115af100"),
    )
    pre[callee_8] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex("610100600081818061ca115af200"),
    )
    pre[callee_9] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex("6101006000818161ca115af400"),
    )
    pre[callee_10] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex("615a17610200600080f560005500"),
    )
    pre[callee_11] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex("6101006000818161ca115afa00"),
    )
    pre[sender] = Account(balance=0xBA1A9CE0BA1A9CE, nonce=1)
    pre[contract] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex(
            "60443560243562c0de00600435016000805b14601c575003600055005b60008381808080"  # noqa: E501
            "808789f1930192601156"
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
