"""
account already has storage X. create -> in init code change that account's...

Ported from:
tests/static/state_tests/stSStoreTest
sstore_changeFromExternalCallInInitCodeFiller.json
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
    [
        "tests/static/state_tests/stSStoreTest/sstore_changeFromExternalCallInInitCodeFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        (
            "6000600060006000600073bea0000000000000000000000000000000000000620186a0f100",  # noqa: E501
            {
                Address("0xbea0000000000000000000000000000000000000"): Account(
                    storage={0: 1, 1: 1},
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x0, value=0x1)
                    + Op.STOP,
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
            "6000602380601860003960006000f55060006000fd0000fe600060006000600073bea0000000000000000000000000000000000000620186a0f400",  # noqa: E501
            {
                Address("0xbea0000000000000000000000000000000000000"): Account(
                    storage={1: 1},
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x0, value=0x1)
                    + Op.STOP,
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
            "6000602380603860003960006000f5506000600060006000600073dea000000000000000000000000000000000000062030d40f1500000fe600060006000600073bea0000000000000000000000000000000000000620186a0f400",  # noqa: E501
            {
                Address("0xbea0000000000000000000000000000000000000"): Account(
                    storage={1: 1},
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x0, value=0x1)
                    + Op.STOP,
                ),
                Address("0xc07f1349a887643be65b34e234e1b3161f62dc30"): Account(
                    storage={0: 1, 1: 1}
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
            "600060006000600073bea0000000000000000000000000000000000000620186a0fa00",  # noqa: E501
            {
                Address("0xbea0000000000000000000000000000000000000"): Account(
                    storage={1: 1},
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x0, value=0x1)
                    + Op.STOP,
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
            "6000602380601360003960006000f5500000fe600060006000600073bea0000000000000000000000000000000000000620186a0fa00",  # noqa: E501
            {
                Address("0xbea0000000000000000000000000000000000000"): Account(
                    storage={1: 1},
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x0, value=0x1)
                    + Op.STOP,
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
            "6000602380601860003960006000f55060006000fd0000fe600060006000600073bea0000000000000000000000000000000000000620186a0fa00",  # noqa: E501
            {
                Address("0xbea0000000000000000000000000000000000000"): Account(
                    storage={1: 1},
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x0, value=0x1)
                    + Op.STOP,
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
            "6000602380603860003960006000f5506000600060006000600073dea000000000000000000000000000000000000062030d40f1500000fe600060006000600073bea0000000000000000000000000000000000000620186a0fa00",  # noqa: E501
            {
                Address("0xbea0000000000000000000000000000000000000"): Account(
                    storage={1: 1},
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x0, value=0x1)
                    + Op.STOP,
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
            "6000602580601360003960006000f5500000fe6000600060006000600073bea0000000000000000000000000000000000000620186a0f100",  # noqa: E501
            {
                Address("0xbea0000000000000000000000000000000000000"): Account(
                    storage={0: 1, 1: 1},
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x0, value=0x1)
                    + Op.STOP,
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
            "6000602580601860003960006000f55060006000fd0000fe6000600060006000600073bea0000000000000000000000000000000000000620186a0f100",  # noqa: E501
            {
                Address("0xbea0000000000000000000000000000000000000"): Account(
                    storage={1: 1},
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x0, value=0x1)
                    + Op.STOP,
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
            "6000602580603860003960006000f5506000600060006000600073dea000000000000000000000000000000000000062030d40f1500000fe6000600060006000600073bea0000000000000000000000000000000000000620186a0f100",  # noqa: E501
            {
                Address("0xbea0000000000000000000000000000000000000"): Account(
                    storage={0: 1, 1: 1},
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x0, value=0x1)
                    + Op.STOP,
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
            "6000600060006000600073bea0000000000000000000000000000000000000620186a0f200",  # noqa: E501
            {
                Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(
                    storage={0: 1, 1: 1}
                ),
                Address("0xbea0000000000000000000000000000000000000"): Account(
                    storage={1: 1},
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x0, value=0x1)
                    + Op.STOP,
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
            "6000602580601360003960006000f5500000fe6000600060006000600073bea0000000000000000000000000000000000000620186a0f200",  # noqa: E501
            {
                Address("0x0f446e1bd7a5da68b5e3a305c7030e3aa8efc293"): Account(
                    storage={0: 1, 1: 1}
                ),
                Address("0xbea0000000000000000000000000000000000000"): Account(
                    storage={1: 1},
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x0, value=0x1)
                    + Op.STOP,
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
            "6000602580601860003960006000f55060006000fd0000fe6000600060006000600073bea0000000000000000000000000000000000000620186a0f200",  # noqa: E501
            {
                Address("0xbea0000000000000000000000000000000000000"): Account(
                    storage={1: 1},
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x0, value=0x1)
                    + Op.STOP,
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
            "6000602580603860003960006000f5506000600060006000600073dea000000000000000000000000000000000000062030d40f1500000fe6000600060006000600073bea0000000000000000000000000000000000000620186a0f200",  # noqa: E501
            {
                Address("0x0f446e1bd7a5da68b5e3a305c7030e3aa8efc293"): Account(
                    storage={0: 1, 1: 1}
                ),
                Address("0xbea0000000000000000000000000000000000000"): Account(
                    storage={1: 1},
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x0, value=0x1)
                    + Op.STOP,
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
            "600060006000600073bea0000000000000000000000000000000000000620186a0f400",  # noqa: E501
            {
                Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(
                    storage={0: 1, 1: 1}
                ),
                Address("0xbea0000000000000000000000000000000000000"): Account(
                    storage={1: 1},
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x0, value=0x1)
                    + Op.STOP,
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
            "6000602380601360003960006000f5500000fe600060006000600073bea0000000000000000000000000000000000000620186a0f400",  # noqa: E501
            {
                Address("0xbea0000000000000000000000000000000000000"): Account(
                    storage={1: 1},
                    code=Op.SSTORE(key=0x1, value=0x0)
                    + Op.SSTORE(key=0x1, value=0x1)
                    + Op.SSTORE(key=0x0, value=0x1)
                    + Op.STOP,
                ),
                Address("0xc07f1349a887643be65b34e234e1b3161f62dc30"): Account(
                    storage={0: 1, 1: 1}
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
    ],
)
@pytest.mark.pre_alloc_mutable
def test_sstore_change_from_external_call_in_init_code(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Account already has storage X. create -> in init code change that..."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xbea0000000000000000000000000000000000000")
    callee_1 = Address("0xdea0000000000000000000000000000000000000")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[sender] = Account(balance=0xE8D4A51000, nonce=0)
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(key=0x1, value=0x0)
            + Op.SSTORE(key=0x1, value=0x1)
            + Op.SSTORE(key=0x0, value=0x1)
            + Op.STOP
        ),
        storage={0x1: 0x1},
    )
    pre[callee_1] = Account(
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
        gas_limit=200000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
