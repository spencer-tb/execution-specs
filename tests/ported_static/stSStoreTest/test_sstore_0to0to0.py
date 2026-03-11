"""
change 0 -> 0 -> 0.

Ported from:
tests/static/state_tests/stSStoreTest/sstore_0to0to0Filler.json
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
    ["tests/static/state_tests/stSStoreTest/sstore_0to0to0Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, tx_gas_limit, expected_post",
    [
        (
            "6000600060006000600073b000000000000000000000000000000000000000620493e0f1506000600060006000600073dea0000000000000000000000000000000000000620927c0f100",  # noqa: E501
            1000000,
            {
                Address("0xb000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.STOP
                ),
                Address("0xc000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.STOP
                ),
                Address("0xdea0000000000000000000000000000000000000"): Account(
                    storage={1: 1},
                    code=Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x2, value=0x1)
                    + Op.SSTORE(key=0x2, value=0x0)
                    + Op.SSTORE(key=0x3, value=0x1)
                    + Op.SSTORE(key=0x3, value=0x0)
                    + Op.SSTORE(key=0x4, value=0x1)
                    + Op.SSTORE(key=0x4, value=0x0)
                    + Op.SSTORE(key=0x5, value=0x1)
                    + Op.SSTORE(key=0x5, value=0x0)
                    + Op.SSTORE(key=0x6, value=0x1)
                    + Op.SSTORE(key=0x6, value=0x0)
                    + Op.SSTORE(key=0x7, value=0x1)
                    + Op.SSTORE(key=0x7, value=0x0)
                    + Op.SSTORE(key=0x8, value=0x1)
                    + Op.SSTORE(key=0x8, value=0x0)
                    + Op.SSTORE(key=0x9, value=0x1)
                    + Op.SSTORE(key=0x9, value=0x0)
                    + Op.SSTORE(key=0xA, value=0x1)
                    + Op.SSTORE(key=0xA, value=0x0)
                    + Op.SSTORE(key=0xB, value=0x1)
                    + Op.SSTORE(key=0xB, value=0x0)
                    + Op.SSTORE(key=0xC, value=0x1)
                    + Op.SSTORE(key=0xC, value=0x0)
                    + Op.SSTORE(key=0xD, value=0x1)
                    + Op.SSTORE(key=0xD, value=0x0)
                    + Op.SSTORE(key=0xE, value=0x1)
                    + Op.SSTORE(key=0xE, value=0x0)
                    + Op.SSTORE(key=0xF, value=0x1)
                    + Op.SSTORE(key=0xF, value=0x0)
                    + Op.SSTORE(key=0x10, value=0x1)
                    + Op.SSTORE(key=0x10, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.STOP,
                ),
            },
        ),
        (
            "6000600060006000600073b000000000000000000000000000000000000000620493e0f1506000600060006000600073dea0000000000000000000000000000000000000620927c0f100",  # noqa: E501
            400000,
            {
                Address("0xb000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.STOP
                ),
                Address("0xc000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.STOP
                ),
                Address("0xdea0000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x2, value=0x1)
                    + Op.SSTORE(key=0x2, value=0x0)
                    + Op.SSTORE(key=0x3, value=0x1)
                    + Op.SSTORE(key=0x3, value=0x0)
                    + Op.SSTORE(key=0x4, value=0x1)
                    + Op.SSTORE(key=0x4, value=0x0)
                    + Op.SSTORE(key=0x5, value=0x1)
                    + Op.SSTORE(key=0x5, value=0x0)
                    + Op.SSTORE(key=0x6, value=0x1)
                    + Op.SSTORE(key=0x6, value=0x0)
                    + Op.SSTORE(key=0x7, value=0x1)
                    + Op.SSTORE(key=0x7, value=0x0)
                    + Op.SSTORE(key=0x8, value=0x1)
                    + Op.SSTORE(key=0x8, value=0x0)
                    + Op.SSTORE(key=0x9, value=0x1)
                    + Op.SSTORE(key=0x9, value=0x0)
                    + Op.SSTORE(key=0xA, value=0x1)
                    + Op.SSTORE(key=0xA, value=0x0)
                    + Op.SSTORE(key=0xB, value=0x1)
                    + Op.SSTORE(key=0xB, value=0x0)
                    + Op.SSTORE(key=0xC, value=0x1)
                    + Op.SSTORE(key=0xC, value=0x0)
                    + Op.SSTORE(key=0xD, value=0x1)
                    + Op.SSTORE(key=0xD, value=0x0)
                    + Op.SSTORE(key=0xE, value=0x1)
                    + Op.SSTORE(key=0xE, value=0x0)
                    + Op.SSTORE(key=0xF, value=0x1)
                    + Op.SSTORE(key=0xF, value=0x0)
                    + Op.SSTORE(key=0x10, value=0x1)
                    + Op.SSTORE(key=0x10, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.STOP
                ),
            },
        ),
        (
            "6000600060006000600073b000000000000000000000000000000000000000620493e0f2506000600060006000600073dea0000000000000000000000000000000000000620927c0f100",  # noqa: E501
            1000000,
            {
                Address("0xb000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.STOP
                ),
                Address("0xc000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.STOP
                ),
                Address("0xdea0000000000000000000000000000000000000"): Account(
                    storage={1: 1},
                    code=Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x2, value=0x1)
                    + Op.SSTORE(key=0x2, value=0x0)
                    + Op.SSTORE(key=0x3, value=0x1)
                    + Op.SSTORE(key=0x3, value=0x0)
                    + Op.SSTORE(key=0x4, value=0x1)
                    + Op.SSTORE(key=0x4, value=0x0)
                    + Op.SSTORE(key=0x5, value=0x1)
                    + Op.SSTORE(key=0x5, value=0x0)
                    + Op.SSTORE(key=0x6, value=0x1)
                    + Op.SSTORE(key=0x6, value=0x0)
                    + Op.SSTORE(key=0x7, value=0x1)
                    + Op.SSTORE(key=0x7, value=0x0)
                    + Op.SSTORE(key=0x8, value=0x1)
                    + Op.SSTORE(key=0x8, value=0x0)
                    + Op.SSTORE(key=0x9, value=0x1)
                    + Op.SSTORE(key=0x9, value=0x0)
                    + Op.SSTORE(key=0xA, value=0x1)
                    + Op.SSTORE(key=0xA, value=0x0)
                    + Op.SSTORE(key=0xB, value=0x1)
                    + Op.SSTORE(key=0xB, value=0x0)
                    + Op.SSTORE(key=0xC, value=0x1)
                    + Op.SSTORE(key=0xC, value=0x0)
                    + Op.SSTORE(key=0xD, value=0x1)
                    + Op.SSTORE(key=0xD, value=0x0)
                    + Op.SSTORE(key=0xE, value=0x1)
                    + Op.SSTORE(key=0xE, value=0x0)
                    + Op.SSTORE(key=0xF, value=0x1)
                    + Op.SSTORE(key=0xF, value=0x0)
                    + Op.SSTORE(key=0x10, value=0x1)
                    + Op.SSTORE(key=0x10, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.STOP,
                ),
            },
        ),
        (
            "6000600060006000600073b000000000000000000000000000000000000000620493e0f2506000600060006000600073dea0000000000000000000000000000000000000620927c0f100",  # noqa: E501
            400000,
            {
                Address("0xb000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.STOP
                ),
                Address("0xc000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.STOP
                ),
                Address("0xdea0000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x2, value=0x1)
                    + Op.SSTORE(key=0x2, value=0x0)
                    + Op.SSTORE(key=0x3, value=0x1)
                    + Op.SSTORE(key=0x3, value=0x0)
                    + Op.SSTORE(key=0x4, value=0x1)
                    + Op.SSTORE(key=0x4, value=0x0)
                    + Op.SSTORE(key=0x5, value=0x1)
                    + Op.SSTORE(key=0x5, value=0x0)
                    + Op.SSTORE(key=0x6, value=0x1)
                    + Op.SSTORE(key=0x6, value=0x0)
                    + Op.SSTORE(key=0x7, value=0x1)
                    + Op.SSTORE(key=0x7, value=0x0)
                    + Op.SSTORE(key=0x8, value=0x1)
                    + Op.SSTORE(key=0x8, value=0x0)
                    + Op.SSTORE(key=0x9, value=0x1)
                    + Op.SSTORE(key=0x9, value=0x0)
                    + Op.SSTORE(key=0xA, value=0x1)
                    + Op.SSTORE(key=0xA, value=0x0)
                    + Op.SSTORE(key=0xB, value=0x1)
                    + Op.SSTORE(key=0xB, value=0x0)
                    + Op.SSTORE(key=0xC, value=0x1)
                    + Op.SSTORE(key=0xC, value=0x0)
                    + Op.SSTORE(key=0xD, value=0x1)
                    + Op.SSTORE(key=0xD, value=0x0)
                    + Op.SSTORE(key=0xE, value=0x1)
                    + Op.SSTORE(key=0xE, value=0x0)
                    + Op.SSTORE(key=0xF, value=0x1)
                    + Op.SSTORE(key=0xF, value=0x0)
                    + Op.SSTORE(key=0x10, value=0x1)
                    + Op.SSTORE(key=0x10, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.STOP
                ),
            },
        ),
        (
            "600060006000600073b000000000000000000000000000000000000000620493e0f4506000600060006000600073dea0000000000000000000000000000000000000620927c0f100",  # noqa: E501
            1000000,
            {
                Address("0xb000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.STOP
                ),
                Address("0xc000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.STOP
                ),
                Address("0xdea0000000000000000000000000000000000000"): Account(
                    storage={1: 1},
                    code=Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x2, value=0x1)
                    + Op.SSTORE(key=0x2, value=0x0)
                    + Op.SSTORE(key=0x3, value=0x1)
                    + Op.SSTORE(key=0x3, value=0x0)
                    + Op.SSTORE(key=0x4, value=0x1)
                    + Op.SSTORE(key=0x4, value=0x0)
                    + Op.SSTORE(key=0x5, value=0x1)
                    + Op.SSTORE(key=0x5, value=0x0)
                    + Op.SSTORE(key=0x6, value=0x1)
                    + Op.SSTORE(key=0x6, value=0x0)
                    + Op.SSTORE(key=0x7, value=0x1)
                    + Op.SSTORE(key=0x7, value=0x0)
                    + Op.SSTORE(key=0x8, value=0x1)
                    + Op.SSTORE(key=0x8, value=0x0)
                    + Op.SSTORE(key=0x9, value=0x1)
                    + Op.SSTORE(key=0x9, value=0x0)
                    + Op.SSTORE(key=0xA, value=0x1)
                    + Op.SSTORE(key=0xA, value=0x0)
                    + Op.SSTORE(key=0xB, value=0x1)
                    + Op.SSTORE(key=0xB, value=0x0)
                    + Op.SSTORE(key=0xC, value=0x1)
                    + Op.SSTORE(key=0xC, value=0x0)
                    + Op.SSTORE(key=0xD, value=0x1)
                    + Op.SSTORE(key=0xD, value=0x0)
                    + Op.SSTORE(key=0xE, value=0x1)
                    + Op.SSTORE(key=0xE, value=0x0)
                    + Op.SSTORE(key=0xF, value=0x1)
                    + Op.SSTORE(key=0xF, value=0x0)
                    + Op.SSTORE(key=0x10, value=0x1)
                    + Op.SSTORE(key=0x10, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.STOP,
                ),
            },
        ),
        (
            "600060006000600073b000000000000000000000000000000000000000620493e0f4506000600060006000600073dea0000000000000000000000000000000000000620927c0f100",  # noqa: E501
            400000,
            {
                Address("0xb000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.STOP
                ),
                Address("0xc000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.STOP
                ),
                Address("0xdea0000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x2, value=0x1)
                    + Op.SSTORE(key=0x2, value=0x0)
                    + Op.SSTORE(key=0x3, value=0x1)
                    + Op.SSTORE(key=0x3, value=0x0)
                    + Op.SSTORE(key=0x4, value=0x1)
                    + Op.SSTORE(key=0x4, value=0x0)
                    + Op.SSTORE(key=0x5, value=0x1)
                    + Op.SSTORE(key=0x5, value=0x0)
                    + Op.SSTORE(key=0x6, value=0x1)
                    + Op.SSTORE(key=0x6, value=0x0)
                    + Op.SSTORE(key=0x7, value=0x1)
                    + Op.SSTORE(key=0x7, value=0x0)
                    + Op.SSTORE(key=0x8, value=0x1)
                    + Op.SSTORE(key=0x8, value=0x0)
                    + Op.SSTORE(key=0x9, value=0x1)
                    + Op.SSTORE(key=0x9, value=0x0)
                    + Op.SSTORE(key=0xA, value=0x1)
                    + Op.SSTORE(key=0xA, value=0x0)
                    + Op.SSTORE(key=0xB, value=0x1)
                    + Op.SSTORE(key=0xB, value=0x0)
                    + Op.SSTORE(key=0xC, value=0x1)
                    + Op.SSTORE(key=0xC, value=0x0)
                    + Op.SSTORE(key=0xD, value=0x1)
                    + Op.SSTORE(key=0xD, value=0x0)
                    + Op.SSTORE(key=0xE, value=0x1)
                    + Op.SSTORE(key=0xE, value=0x0)
                    + Op.SSTORE(key=0xF, value=0x1)
                    + Op.SSTORE(key=0xF, value=0x0)
                    + Op.SSTORE(key=0x10, value=0x1)
                    + Op.SSTORE(key=0x10, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.STOP
                ),
            },
        ),
        (
            "600060006000600073c000000000000000000000000000000000000000620493e0fa506000600060006000600073dea0000000000000000000000000000000000000620927c0f100",  # noqa: E501
            1000000,
            {
                Address("0xb000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.STOP
                ),
                Address("0xc000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.STOP
                ),
                Address("0xdea0000000000000000000000000000000000000"): Account(
                    storage={1: 1},
                    code=Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x2, value=0x1)
                    + Op.SSTORE(key=0x2, value=0x0)
                    + Op.SSTORE(key=0x3, value=0x1)
                    + Op.SSTORE(key=0x3, value=0x0)
                    + Op.SSTORE(key=0x4, value=0x1)
                    + Op.SSTORE(key=0x4, value=0x0)
                    + Op.SSTORE(key=0x5, value=0x1)
                    + Op.SSTORE(key=0x5, value=0x0)
                    + Op.SSTORE(key=0x6, value=0x1)
                    + Op.SSTORE(key=0x6, value=0x0)
                    + Op.SSTORE(key=0x7, value=0x1)
                    + Op.SSTORE(key=0x7, value=0x0)
                    + Op.SSTORE(key=0x8, value=0x1)
                    + Op.SSTORE(key=0x8, value=0x0)
                    + Op.SSTORE(key=0x9, value=0x1)
                    + Op.SSTORE(key=0x9, value=0x0)
                    + Op.SSTORE(key=0xA, value=0x1)
                    + Op.SSTORE(key=0xA, value=0x0)
                    + Op.SSTORE(key=0xB, value=0x1)
                    + Op.SSTORE(key=0xB, value=0x0)
                    + Op.SSTORE(key=0xC, value=0x1)
                    + Op.SSTORE(key=0xC, value=0x0)
                    + Op.SSTORE(key=0xD, value=0x1)
                    + Op.SSTORE(key=0xD, value=0x0)
                    + Op.SSTORE(key=0xE, value=0x1)
                    + Op.SSTORE(key=0xE, value=0x0)
                    + Op.SSTORE(key=0xF, value=0x1)
                    + Op.SSTORE(key=0xF, value=0x0)
                    + Op.SSTORE(key=0x10, value=0x1)
                    + Op.SSTORE(key=0x10, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.STOP,
                ),
            },
        ),
        (
            "600060006000600073c000000000000000000000000000000000000000620493e0fa506000600060006000600073dea0000000000000000000000000000000000000620927c0f100",  # noqa: E501
            400000,
            {
                Address("0xb000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.STOP
                ),
                Address("0xc000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.STOP
                ),
                Address("0xdea0000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x2, value=0x1)
                    + Op.SSTORE(key=0x2, value=0x0)
                    + Op.SSTORE(key=0x3, value=0x1)
                    + Op.SSTORE(key=0x3, value=0x0)
                    + Op.SSTORE(key=0x4, value=0x1)
                    + Op.SSTORE(key=0x4, value=0x0)
                    + Op.SSTORE(key=0x5, value=0x1)
                    + Op.SSTORE(key=0x5, value=0x0)
                    + Op.SSTORE(key=0x6, value=0x1)
                    + Op.SSTORE(key=0x6, value=0x0)
                    + Op.SSTORE(key=0x7, value=0x1)
                    + Op.SSTORE(key=0x7, value=0x0)
                    + Op.SSTORE(key=0x8, value=0x1)
                    + Op.SSTORE(key=0x8, value=0x0)
                    + Op.SSTORE(key=0x9, value=0x1)
                    + Op.SSTORE(key=0x9, value=0x0)
                    + Op.SSTORE(key=0xA, value=0x1)
                    + Op.SSTORE(key=0xA, value=0x0)
                    + Op.SSTORE(key=0xB, value=0x1)
                    + Op.SSTORE(key=0xB, value=0x0)
                    + Op.SSTORE(key=0xC, value=0x1)
                    + Op.SSTORE(key=0xC, value=0x0)
                    + Op.SSTORE(key=0xD, value=0x1)
                    + Op.SSTORE(key=0xD, value=0x0)
                    + Op.SSTORE(key=0xE, value=0x1)
                    + Op.SSTORE(key=0xE, value=0x0)
                    + Op.SSTORE(key=0xF, value=0x1)
                    + Op.SSTORE(key=0xF, value=0x0)
                    + Op.SSTORE(key=0x10, value=0x1)
                    + Op.SSTORE(key=0x10, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.STOP
                ),
            },
        ),
        (
            "6000601080603860003960006000f5506000600060006000600073dea0000000000000000000000000000000000000620927c0f1500000fe60006000556000600055600160015500",  # noqa: E501
            1000000,
            {
                Address("0x0bdfb5bb25de41df5ef3e68904843c7a7b92d35f"): Account(
                    storage={1: 1}
                ),
                Address("0xb000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.STOP
                ),
                Address("0xc000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.STOP
                ),
                Address("0xdea0000000000000000000000000000000000000"): Account(
                    storage={1: 1},
                    code=Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x2, value=0x1)
                    + Op.SSTORE(key=0x2, value=0x0)
                    + Op.SSTORE(key=0x3, value=0x1)
                    + Op.SSTORE(key=0x3, value=0x0)
                    + Op.SSTORE(key=0x4, value=0x1)
                    + Op.SSTORE(key=0x4, value=0x0)
                    + Op.SSTORE(key=0x5, value=0x1)
                    + Op.SSTORE(key=0x5, value=0x0)
                    + Op.SSTORE(key=0x6, value=0x1)
                    + Op.SSTORE(key=0x6, value=0x0)
                    + Op.SSTORE(key=0x7, value=0x1)
                    + Op.SSTORE(key=0x7, value=0x0)
                    + Op.SSTORE(key=0x8, value=0x1)
                    + Op.SSTORE(key=0x8, value=0x0)
                    + Op.SSTORE(key=0x9, value=0x1)
                    + Op.SSTORE(key=0x9, value=0x0)
                    + Op.SSTORE(key=0xA, value=0x1)
                    + Op.SSTORE(key=0xA, value=0x0)
                    + Op.SSTORE(key=0xB, value=0x1)
                    + Op.SSTORE(key=0xB, value=0x0)
                    + Op.SSTORE(key=0xC, value=0x1)
                    + Op.SSTORE(key=0xC, value=0x0)
                    + Op.SSTORE(key=0xD, value=0x1)
                    + Op.SSTORE(key=0xD, value=0x0)
                    + Op.SSTORE(key=0xE, value=0x1)
                    + Op.SSTORE(key=0xE, value=0x0)
                    + Op.SSTORE(key=0xF, value=0x1)
                    + Op.SSTORE(key=0xF, value=0x0)
                    + Op.SSTORE(key=0x10, value=0x1)
                    + Op.SSTORE(key=0x10, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.STOP,
                ),
            },
        ),
        (
            "6000601080603860003960006000f5506000600060006000600073dea0000000000000000000000000000000000000620927c0f1500000fe60006000556000600055600160015500",  # noqa: E501
            400000,
            {
                Address("0x0bdfb5bb25de41df5ef3e68904843c7a7b92d35f"): Account(
                    storage={1: 1}
                ),
                Address("0xb000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.STOP
                ),
                Address("0xc000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.STOP
                ),
                Address("0xdea0000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x2, value=0x1)
                    + Op.SSTORE(key=0x2, value=0x0)
                    + Op.SSTORE(key=0x3, value=0x1)
                    + Op.SSTORE(key=0x3, value=0x0)
                    + Op.SSTORE(key=0x4, value=0x1)
                    + Op.SSTORE(key=0x4, value=0x0)
                    + Op.SSTORE(key=0x5, value=0x1)
                    + Op.SSTORE(key=0x5, value=0x0)
                    + Op.SSTORE(key=0x6, value=0x1)
                    + Op.SSTORE(key=0x6, value=0x0)
                    + Op.SSTORE(key=0x7, value=0x1)
                    + Op.SSTORE(key=0x7, value=0x0)
                    + Op.SSTORE(key=0x8, value=0x1)
                    + Op.SSTORE(key=0x8, value=0x0)
                    + Op.SSTORE(key=0x9, value=0x1)
                    + Op.SSTORE(key=0x9, value=0x0)
                    + Op.SSTORE(key=0xA, value=0x1)
                    + Op.SSTORE(key=0xA, value=0x0)
                    + Op.SSTORE(key=0xB, value=0x1)
                    + Op.SSTORE(key=0xB, value=0x0)
                    + Op.SSTORE(key=0xC, value=0x1)
                    + Op.SSTORE(key=0xC, value=0x0)
                    + Op.SSTORE(key=0xD, value=0x1)
                    + Op.SSTORE(key=0xD, value=0x0)
                    + Op.SSTORE(key=0xE, value=0x1)
                    + Op.SSTORE(key=0xE, value=0x0)
                    + Op.SSTORE(key=0xF, value=0x1)
                    + Op.SSTORE(key=0xF, value=0x0)
                    + Op.SSTORE(key=0x10, value=0x1)
                    + Op.SSTORE(key=0x10, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.STOP
                ),
            },
        ),
        (
            "6000600060006000600073b000000000000000000000000000000000000000620493e0f1506000600060006000600073dea0000000000000000000000000000000000000620927c0f15060206000fd00",  # noqa: E501
            1000000,
            {
                Address("0xb000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.STOP
                ),
                Address("0xc000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.STOP
                ),
                Address("0xdea0000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x2, value=0x1)
                    + Op.SSTORE(key=0x2, value=0x0)
                    + Op.SSTORE(key=0x3, value=0x1)
                    + Op.SSTORE(key=0x3, value=0x0)
                    + Op.SSTORE(key=0x4, value=0x1)
                    + Op.SSTORE(key=0x4, value=0x0)
                    + Op.SSTORE(key=0x5, value=0x1)
                    + Op.SSTORE(key=0x5, value=0x0)
                    + Op.SSTORE(key=0x6, value=0x1)
                    + Op.SSTORE(key=0x6, value=0x0)
                    + Op.SSTORE(key=0x7, value=0x1)
                    + Op.SSTORE(key=0x7, value=0x0)
                    + Op.SSTORE(key=0x8, value=0x1)
                    + Op.SSTORE(key=0x8, value=0x0)
                    + Op.SSTORE(key=0x9, value=0x1)
                    + Op.SSTORE(key=0x9, value=0x0)
                    + Op.SSTORE(key=0xA, value=0x1)
                    + Op.SSTORE(key=0xA, value=0x0)
                    + Op.SSTORE(key=0xB, value=0x1)
                    + Op.SSTORE(key=0xB, value=0x0)
                    + Op.SSTORE(key=0xC, value=0x1)
                    + Op.SSTORE(key=0xC, value=0x0)
                    + Op.SSTORE(key=0xD, value=0x1)
                    + Op.SSTORE(key=0xD, value=0x0)
                    + Op.SSTORE(key=0xE, value=0x1)
                    + Op.SSTORE(key=0xE, value=0x0)
                    + Op.SSTORE(key=0xF, value=0x1)
                    + Op.SSTORE(key=0xF, value=0x0)
                    + Op.SSTORE(key=0x10, value=0x1)
                    + Op.SSTORE(key=0x10, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.STOP
                ),
            },
        ),
        (
            "6000600060006000600073b000000000000000000000000000000000000000620493e0f1506000600060006000600073dea0000000000000000000000000000000000000620927c0f15060206000fd00",  # noqa: E501
            400000,
            {
                Address("0xb000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.STOP
                ),
                Address("0xc000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.STOP
                ),
                Address("0xdea0000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x2, value=0x1)
                    + Op.SSTORE(key=0x2, value=0x0)
                    + Op.SSTORE(key=0x3, value=0x1)
                    + Op.SSTORE(key=0x3, value=0x0)
                    + Op.SSTORE(key=0x4, value=0x1)
                    + Op.SSTORE(key=0x4, value=0x0)
                    + Op.SSTORE(key=0x5, value=0x1)
                    + Op.SSTORE(key=0x5, value=0x0)
                    + Op.SSTORE(key=0x6, value=0x1)
                    + Op.SSTORE(key=0x6, value=0x0)
                    + Op.SSTORE(key=0x7, value=0x1)
                    + Op.SSTORE(key=0x7, value=0x0)
                    + Op.SSTORE(key=0x8, value=0x1)
                    + Op.SSTORE(key=0x8, value=0x0)
                    + Op.SSTORE(key=0x9, value=0x1)
                    + Op.SSTORE(key=0x9, value=0x0)
                    + Op.SSTORE(key=0xA, value=0x1)
                    + Op.SSTORE(key=0xA, value=0x0)
                    + Op.SSTORE(key=0xB, value=0x1)
                    + Op.SSTORE(key=0xB, value=0x0)
                    + Op.SSTORE(key=0xC, value=0x1)
                    + Op.SSTORE(key=0xC, value=0x0)
                    + Op.SSTORE(key=0xD, value=0x1)
                    + Op.SSTORE(key=0xD, value=0x0)
                    + Op.SSTORE(key=0xE, value=0x1)
                    + Op.SSTORE(key=0xE, value=0x0)
                    + Op.SSTORE(key=0xF, value=0x1)
                    + Op.SSTORE(key=0xF, value=0x0)
                    + Op.SSTORE(key=0x10, value=0x1)
                    + Op.SSTORE(key=0x10, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.STOP
                ),
            },
        ),
        (
            "6000600060006000600073b000000000000000000000000000000000000000620493e0f2506000600060006000600073dea0000000000000000000000000000000000000620927c0f15060206000fd00",  # noqa: E501
            1000000,
            {
                Address("0xb000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.STOP
                ),
                Address("0xc000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.STOP
                ),
                Address("0xdea0000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x2, value=0x1)
                    + Op.SSTORE(key=0x2, value=0x0)
                    + Op.SSTORE(key=0x3, value=0x1)
                    + Op.SSTORE(key=0x3, value=0x0)
                    + Op.SSTORE(key=0x4, value=0x1)
                    + Op.SSTORE(key=0x4, value=0x0)
                    + Op.SSTORE(key=0x5, value=0x1)
                    + Op.SSTORE(key=0x5, value=0x0)
                    + Op.SSTORE(key=0x6, value=0x1)
                    + Op.SSTORE(key=0x6, value=0x0)
                    + Op.SSTORE(key=0x7, value=0x1)
                    + Op.SSTORE(key=0x7, value=0x0)
                    + Op.SSTORE(key=0x8, value=0x1)
                    + Op.SSTORE(key=0x8, value=0x0)
                    + Op.SSTORE(key=0x9, value=0x1)
                    + Op.SSTORE(key=0x9, value=0x0)
                    + Op.SSTORE(key=0xA, value=0x1)
                    + Op.SSTORE(key=0xA, value=0x0)
                    + Op.SSTORE(key=0xB, value=0x1)
                    + Op.SSTORE(key=0xB, value=0x0)
                    + Op.SSTORE(key=0xC, value=0x1)
                    + Op.SSTORE(key=0xC, value=0x0)
                    + Op.SSTORE(key=0xD, value=0x1)
                    + Op.SSTORE(key=0xD, value=0x0)
                    + Op.SSTORE(key=0xE, value=0x1)
                    + Op.SSTORE(key=0xE, value=0x0)
                    + Op.SSTORE(key=0xF, value=0x1)
                    + Op.SSTORE(key=0xF, value=0x0)
                    + Op.SSTORE(key=0x10, value=0x1)
                    + Op.SSTORE(key=0x10, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.STOP
                ),
            },
        ),
        (
            "6000600060006000600073b000000000000000000000000000000000000000620493e0f2506000600060006000600073dea0000000000000000000000000000000000000620927c0f15060206000fd00",  # noqa: E501
            400000,
            {
                Address("0xb000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.STOP
                ),
                Address("0xc000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.STOP
                ),
                Address("0xdea0000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x2, value=0x1)
                    + Op.SSTORE(key=0x2, value=0x0)
                    + Op.SSTORE(key=0x3, value=0x1)
                    + Op.SSTORE(key=0x3, value=0x0)
                    + Op.SSTORE(key=0x4, value=0x1)
                    + Op.SSTORE(key=0x4, value=0x0)
                    + Op.SSTORE(key=0x5, value=0x1)
                    + Op.SSTORE(key=0x5, value=0x0)
                    + Op.SSTORE(key=0x6, value=0x1)
                    + Op.SSTORE(key=0x6, value=0x0)
                    + Op.SSTORE(key=0x7, value=0x1)
                    + Op.SSTORE(key=0x7, value=0x0)
                    + Op.SSTORE(key=0x8, value=0x1)
                    + Op.SSTORE(key=0x8, value=0x0)
                    + Op.SSTORE(key=0x9, value=0x1)
                    + Op.SSTORE(key=0x9, value=0x0)
                    + Op.SSTORE(key=0xA, value=0x1)
                    + Op.SSTORE(key=0xA, value=0x0)
                    + Op.SSTORE(key=0xB, value=0x1)
                    + Op.SSTORE(key=0xB, value=0x0)
                    + Op.SSTORE(key=0xC, value=0x1)
                    + Op.SSTORE(key=0xC, value=0x0)
                    + Op.SSTORE(key=0xD, value=0x1)
                    + Op.SSTORE(key=0xD, value=0x0)
                    + Op.SSTORE(key=0xE, value=0x1)
                    + Op.SSTORE(key=0xE, value=0x0)
                    + Op.SSTORE(key=0xF, value=0x1)
                    + Op.SSTORE(key=0xF, value=0x0)
                    + Op.SSTORE(key=0x10, value=0x1)
                    + Op.SSTORE(key=0x10, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.STOP
                ),
            },
        ),
        (
            "600060006000600073b000000000000000000000000000000000000000620493e0f4506000600060006000600073dea0000000000000000000000000000000000000620927c0f15060206000fd00",  # noqa: E501
            1000000,
            {
                Address("0xb000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.STOP
                ),
                Address("0xc000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.STOP
                ),
                Address("0xdea0000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x2, value=0x1)
                    + Op.SSTORE(key=0x2, value=0x0)
                    + Op.SSTORE(key=0x3, value=0x1)
                    + Op.SSTORE(key=0x3, value=0x0)
                    + Op.SSTORE(key=0x4, value=0x1)
                    + Op.SSTORE(key=0x4, value=0x0)
                    + Op.SSTORE(key=0x5, value=0x1)
                    + Op.SSTORE(key=0x5, value=0x0)
                    + Op.SSTORE(key=0x6, value=0x1)
                    + Op.SSTORE(key=0x6, value=0x0)
                    + Op.SSTORE(key=0x7, value=0x1)
                    + Op.SSTORE(key=0x7, value=0x0)
                    + Op.SSTORE(key=0x8, value=0x1)
                    + Op.SSTORE(key=0x8, value=0x0)
                    + Op.SSTORE(key=0x9, value=0x1)
                    + Op.SSTORE(key=0x9, value=0x0)
                    + Op.SSTORE(key=0xA, value=0x1)
                    + Op.SSTORE(key=0xA, value=0x0)
                    + Op.SSTORE(key=0xB, value=0x1)
                    + Op.SSTORE(key=0xB, value=0x0)
                    + Op.SSTORE(key=0xC, value=0x1)
                    + Op.SSTORE(key=0xC, value=0x0)
                    + Op.SSTORE(key=0xD, value=0x1)
                    + Op.SSTORE(key=0xD, value=0x0)
                    + Op.SSTORE(key=0xE, value=0x1)
                    + Op.SSTORE(key=0xE, value=0x0)
                    + Op.SSTORE(key=0xF, value=0x1)
                    + Op.SSTORE(key=0xF, value=0x0)
                    + Op.SSTORE(key=0x10, value=0x1)
                    + Op.SSTORE(key=0x10, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.STOP
                ),
            },
        ),
        (
            "600060006000600073b000000000000000000000000000000000000000620493e0f4506000600060006000600073dea0000000000000000000000000000000000000620927c0f15060206000fd00",  # noqa: E501
            400000,
            {
                Address("0xb000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.STOP
                ),
                Address("0xc000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.STOP
                ),
                Address("0xdea0000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x2, value=0x1)
                    + Op.SSTORE(key=0x2, value=0x0)
                    + Op.SSTORE(key=0x3, value=0x1)
                    + Op.SSTORE(key=0x3, value=0x0)
                    + Op.SSTORE(key=0x4, value=0x1)
                    + Op.SSTORE(key=0x4, value=0x0)
                    + Op.SSTORE(key=0x5, value=0x1)
                    + Op.SSTORE(key=0x5, value=0x0)
                    + Op.SSTORE(key=0x6, value=0x1)
                    + Op.SSTORE(key=0x6, value=0x0)
                    + Op.SSTORE(key=0x7, value=0x1)
                    + Op.SSTORE(key=0x7, value=0x0)
                    + Op.SSTORE(key=0x8, value=0x1)
                    + Op.SSTORE(key=0x8, value=0x0)
                    + Op.SSTORE(key=0x9, value=0x1)
                    + Op.SSTORE(key=0x9, value=0x0)
                    + Op.SSTORE(key=0xA, value=0x1)
                    + Op.SSTORE(key=0xA, value=0x0)
                    + Op.SSTORE(key=0xB, value=0x1)
                    + Op.SSTORE(key=0xB, value=0x0)
                    + Op.SSTORE(key=0xC, value=0x1)
                    + Op.SSTORE(key=0xC, value=0x0)
                    + Op.SSTORE(key=0xD, value=0x1)
                    + Op.SSTORE(key=0xD, value=0x0)
                    + Op.SSTORE(key=0xE, value=0x1)
                    + Op.SSTORE(key=0xE, value=0x0)
                    + Op.SSTORE(key=0xF, value=0x1)
                    + Op.SSTORE(key=0xF, value=0x0)
                    + Op.SSTORE(key=0x10, value=0x1)
                    + Op.SSTORE(key=0x10, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.STOP
                ),
            },
        ),
        (
            "600060006000600073c000000000000000000000000000000000000000620493e0fa506000600060006000600073dea0000000000000000000000000000000000000620927c0f15060206000fd00",  # noqa: E501
            1000000,
            {
                Address("0xb000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.STOP
                ),
                Address("0xc000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.STOP
                ),
                Address("0xdea0000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x2, value=0x1)
                    + Op.SSTORE(key=0x2, value=0x0)
                    + Op.SSTORE(key=0x3, value=0x1)
                    + Op.SSTORE(key=0x3, value=0x0)
                    + Op.SSTORE(key=0x4, value=0x1)
                    + Op.SSTORE(key=0x4, value=0x0)
                    + Op.SSTORE(key=0x5, value=0x1)
                    + Op.SSTORE(key=0x5, value=0x0)
                    + Op.SSTORE(key=0x6, value=0x1)
                    + Op.SSTORE(key=0x6, value=0x0)
                    + Op.SSTORE(key=0x7, value=0x1)
                    + Op.SSTORE(key=0x7, value=0x0)
                    + Op.SSTORE(key=0x8, value=0x1)
                    + Op.SSTORE(key=0x8, value=0x0)
                    + Op.SSTORE(key=0x9, value=0x1)
                    + Op.SSTORE(key=0x9, value=0x0)
                    + Op.SSTORE(key=0xA, value=0x1)
                    + Op.SSTORE(key=0xA, value=0x0)
                    + Op.SSTORE(key=0xB, value=0x1)
                    + Op.SSTORE(key=0xB, value=0x0)
                    + Op.SSTORE(key=0xC, value=0x1)
                    + Op.SSTORE(key=0xC, value=0x0)
                    + Op.SSTORE(key=0xD, value=0x1)
                    + Op.SSTORE(key=0xD, value=0x0)
                    + Op.SSTORE(key=0xE, value=0x1)
                    + Op.SSTORE(key=0xE, value=0x0)
                    + Op.SSTORE(key=0xF, value=0x1)
                    + Op.SSTORE(key=0xF, value=0x0)
                    + Op.SSTORE(key=0x10, value=0x1)
                    + Op.SSTORE(key=0x10, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.STOP
                ),
            },
        ),
        (
            "600060006000600073c000000000000000000000000000000000000000620493e0fa506000600060006000600073dea0000000000000000000000000000000000000620927c0f15060206000fd00",  # noqa: E501
            400000,
            {
                Address("0xb000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.STOP
                ),
                Address("0xc000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.STOP
                ),
                Address("0xdea0000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x2, value=0x1)
                    + Op.SSTORE(key=0x2, value=0x0)
                    + Op.SSTORE(key=0x3, value=0x1)
                    + Op.SSTORE(key=0x3, value=0x0)
                    + Op.SSTORE(key=0x4, value=0x1)
                    + Op.SSTORE(key=0x4, value=0x0)
                    + Op.SSTORE(key=0x5, value=0x1)
                    + Op.SSTORE(key=0x5, value=0x0)
                    + Op.SSTORE(key=0x6, value=0x1)
                    + Op.SSTORE(key=0x6, value=0x0)
                    + Op.SSTORE(key=0x7, value=0x1)
                    + Op.SSTORE(key=0x7, value=0x0)
                    + Op.SSTORE(key=0x8, value=0x1)
                    + Op.SSTORE(key=0x8, value=0x0)
                    + Op.SSTORE(key=0x9, value=0x1)
                    + Op.SSTORE(key=0x9, value=0x0)
                    + Op.SSTORE(key=0xA, value=0x1)
                    + Op.SSTORE(key=0xA, value=0x0)
                    + Op.SSTORE(key=0xB, value=0x1)
                    + Op.SSTORE(key=0xB, value=0x0)
                    + Op.SSTORE(key=0xC, value=0x1)
                    + Op.SSTORE(key=0xC, value=0x0)
                    + Op.SSTORE(key=0xD, value=0x1)
                    + Op.SSTORE(key=0xD, value=0x0)
                    + Op.SSTORE(key=0xE, value=0x1)
                    + Op.SSTORE(key=0xE, value=0x0)
                    + Op.SSTORE(key=0xF, value=0x1)
                    + Op.SSTORE(key=0xF, value=0x0)
                    + Op.SSTORE(key=0x10, value=0x1)
                    + Op.SSTORE(key=0x10, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.STOP
                ),
            },
        ),
        (
            "6000601080603d60003960006000f5506000600060006000600073dea0000000000000000000000000000000000000620927c0f15060206000fd0000fe60006000556000600055600160015500",  # noqa: E501
            1000000,
            {
                Address("0xb000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.STOP
                ),
                Address("0xc000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.STOP
                ),
                Address("0xdea0000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x2, value=0x1)
                    + Op.SSTORE(key=0x2, value=0x0)
                    + Op.SSTORE(key=0x3, value=0x1)
                    + Op.SSTORE(key=0x3, value=0x0)
                    + Op.SSTORE(key=0x4, value=0x1)
                    + Op.SSTORE(key=0x4, value=0x0)
                    + Op.SSTORE(key=0x5, value=0x1)
                    + Op.SSTORE(key=0x5, value=0x0)
                    + Op.SSTORE(key=0x6, value=0x1)
                    + Op.SSTORE(key=0x6, value=0x0)
                    + Op.SSTORE(key=0x7, value=0x1)
                    + Op.SSTORE(key=0x7, value=0x0)
                    + Op.SSTORE(key=0x8, value=0x1)
                    + Op.SSTORE(key=0x8, value=0x0)
                    + Op.SSTORE(key=0x9, value=0x1)
                    + Op.SSTORE(key=0x9, value=0x0)
                    + Op.SSTORE(key=0xA, value=0x1)
                    + Op.SSTORE(key=0xA, value=0x0)
                    + Op.SSTORE(key=0xB, value=0x1)
                    + Op.SSTORE(key=0xB, value=0x0)
                    + Op.SSTORE(key=0xC, value=0x1)
                    + Op.SSTORE(key=0xC, value=0x0)
                    + Op.SSTORE(key=0xD, value=0x1)
                    + Op.SSTORE(key=0xD, value=0x0)
                    + Op.SSTORE(key=0xE, value=0x1)
                    + Op.SSTORE(key=0xE, value=0x0)
                    + Op.SSTORE(key=0xF, value=0x1)
                    + Op.SSTORE(key=0xF, value=0x0)
                    + Op.SSTORE(key=0x10, value=0x1)
                    + Op.SSTORE(key=0x10, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.STOP
                ),
            },
        ),
        (
            "6000601080603d60003960006000f5506000600060006000600073dea0000000000000000000000000000000000000620927c0f15060206000fd0000fe60006000556000600055600160015500",  # noqa: E501
            400000,
            {
                Address("0xb000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.STOP
                ),
                Address("0xc000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.STOP
                ),
                Address("0xdea0000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x2, value=0x1)
                    + Op.SSTORE(key=0x2, value=0x0)
                    + Op.SSTORE(key=0x3, value=0x1)
                    + Op.SSTORE(key=0x3, value=0x0)
                    + Op.SSTORE(key=0x4, value=0x1)
                    + Op.SSTORE(key=0x4, value=0x0)
                    + Op.SSTORE(key=0x5, value=0x1)
                    + Op.SSTORE(key=0x5, value=0x0)
                    + Op.SSTORE(key=0x6, value=0x1)
                    + Op.SSTORE(key=0x6, value=0x0)
                    + Op.SSTORE(key=0x7, value=0x1)
                    + Op.SSTORE(key=0x7, value=0x0)
                    + Op.SSTORE(key=0x8, value=0x1)
                    + Op.SSTORE(key=0x8, value=0x0)
                    + Op.SSTORE(key=0x9, value=0x1)
                    + Op.SSTORE(key=0x9, value=0x0)
                    + Op.SSTORE(key=0xA, value=0x1)
                    + Op.SSTORE(key=0xA, value=0x0)
                    + Op.SSTORE(key=0xB, value=0x1)
                    + Op.SSTORE(key=0xB, value=0x0)
                    + Op.SSTORE(key=0xC, value=0x1)
                    + Op.SSTORE(key=0xC, value=0x0)
                    + Op.SSTORE(key=0xD, value=0x1)
                    + Op.SSTORE(key=0xD, value=0x0)
                    + Op.SSTORE(key=0xE, value=0x1)
                    + Op.SSTORE(key=0xE, value=0x0)
                    + Op.SSTORE(key=0xF, value=0x1)
                    + Op.SSTORE(key=0xF, value=0x0)
                    + Op.SSTORE(key=0x10, value=0x1)
                    + Op.SSTORE(key=0x10, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x1)
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
    ],
)
@pytest.mark.pre_alloc_mutable
def test_sstore_0to0to0(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    tx_gas_limit: int,
    expected_post: dict,
) -> None:
    """Change 0 -> 0 -> 0."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xb000000000000000000000000000000000000000")
    callee_1 = Address("0xc000000000000000000000000000000000000000")
    callee_2 = Address("0xdea0000000000000000000000000000000000000")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[sender] = Account(balance=0xE8D4A51000, nonce=0)
    # Source: LLL
    # { [[1]] 0 [[1]] 0 }
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(key=0x1, value=0x0)
            + Op.SSTORE(key=0x1, value=0x0)
            + Op.STOP
        ),
    )
    # Source: LLL
    # { [[1]] 0 [[1]] 0 }
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(key=0x1, value=0x0)
            + Op.SSTORE(key=0x1, value=0x0)
            + Op.STOP
        ),
    )
    # Source: LLL
    # { [[1]] 1 [[1]] 0 [[2]] 1 [[2]] 0 [[3]] 1 [[3]] 0 [[4]] 1 [[4]] 0 [[5]] 1 [[5]] 0 [[6]] 1 [[6]] 0 [[7]] 1 [[7]] 0 [[8]] 1 [[8]] 0 [[9]] 1 [[9]] 0 [[10]] 1 [[10]] 0 [[11]] 1 [[11]] 0 [[12]] 1 [[12]] 0 [[13]] 1 [[13]] 0 [[14]] 1 [[14]] 0 [[15]] 1 [[15]] 0 [[16]] 1 [[16]] 0  [[1]] 1 }  # noqa: E501
    pre[callee_2] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(key=0x1, value=0x1)
            + Op.SSTORE(key=0x1, value=0x0)
            + Op.SSTORE(key=0x2, value=0x1)
            + Op.SSTORE(key=0x2, value=0x0)
            + Op.SSTORE(key=0x3, value=0x1)
            + Op.SSTORE(key=0x3, value=0x0)
            + Op.SSTORE(key=0x4, value=0x1)
            + Op.SSTORE(key=0x4, value=0x0)
            + Op.SSTORE(key=0x5, value=0x1)
            + Op.SSTORE(key=0x5, value=0x0)
            + Op.SSTORE(key=0x6, value=0x1)
            + Op.SSTORE(key=0x6, value=0x0)
            + Op.SSTORE(key=0x7, value=0x1)
            + Op.SSTORE(key=0x7, value=0x0)
            + Op.SSTORE(key=0x8, value=0x1)
            + Op.SSTORE(key=0x8, value=0x0)
            + Op.SSTORE(key=0x9, value=0x1)
            + Op.SSTORE(key=0x9, value=0x0)
            + Op.SSTORE(key=0xA, value=0x1)
            + Op.SSTORE(key=0xA, value=0x0)
            + Op.SSTORE(key=0xB, value=0x1)
            + Op.SSTORE(key=0xB, value=0x0)
            + Op.SSTORE(key=0xC, value=0x1)
            + Op.SSTORE(key=0xC, value=0x0)
            + Op.SSTORE(key=0xD, value=0x1)
            + Op.SSTORE(key=0xD, value=0x0)
            + Op.SSTORE(key=0xE, value=0x1)
            + Op.SSTORE(key=0xE, value=0x0)
            + Op.SSTORE(key=0xF, value=0x1)
            + Op.SSTORE(key=0xF, value=0x0)
            + Op.SSTORE(key=0x10, value=0x1)
            + Op.SSTORE(key=0x10, value=0x0)
            + Op.SSTORE(key=0x1, value=0x1)
            + Op.STOP
        ),
    )

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=None,
        data=tx_data,
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
