"""
Ori Pomerantz   qbzzt1@gmail.com.

Ported from:
tests/static/state_tests/stCreateTest/createFailResultFiller.yml
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
    ["tests/static/state_tests/stCreateTest/createFailResultFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000000ee0000000000000000000000000000000000000000000000000000000000000bad",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000bad"): Account(
                    code=bytes.fromhex("650bad0bad0bad60005260206000fd")
                ),
                Address("0x000000000000000000000000000000000000600d"): Account(
                    code=bytes.fromhex("61600d60005260206000f3")
                ),
                Address("0x000000000000000000000000000000000000da7a"): Account(
                    code=bytes.fromhex(
                        "63deadbeef6000526160a760205260406000f3"
                    )
                ),
                Address("0x0000000000000000000000000000000000c0deee"): Account(
                    storage={16: 1, 17: 64, 18: 0xDEADBEEF, 19: 24743},
                    code=bytes.fromhex(
                        "60406101006000808061da7a5af16010553d60115561010051601255610120516013556000803581813b9283923c600080f06000553d6001553d60006102003e610200516002556102205160035500"  # noqa: E501
                    ),
                ),
                Address("0x0000000000000000000000000000000000c0def0"): Account(
                    code=bytes.fromhex(
                        "60406101006000808061da7a5af16010553d60115561010051601255610120516013556000803581813b9283923c600080f06000553d6001553d60006102003e610200516002556102205160035500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000c0def5"): Account(
                    code=bytes.fromhex(
                        "60406101006000808061da7a5af16010553d6011556101005160125561012051601355615a176000803581813b9283923c600080f56000553d6001553d60006102003e610200516002556102205160035500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000c0deff"): Account(
                    code=bytes.fromhex(
                        "60406101006000808061da7a5af16010553d601155610100516012556101205160135563bad05a176000803581813b9283923c600080f56000553d6001553d60006102003e610200516002556102205160035500"  # noqa: E501
                    )
                ),
                Address("0x13c950f8740ffaea1869a88d70b029e8b0c9a8da"): Account(
                    code=bytes.fromhex("600100")
                ),
                Address("0xbb0237ab04970e3cf3e813c02064662adc89336b"): Account(
                    code=bytes.fromhex("600100")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 1, 16: 1, 17: 64, 18: 0xDEADBEEF, 19: 24743},
                    code=bytes.fromhex(
                        "60206102008160008062c0de0060043501602435604061010084808061da7a5af16010553d60115561010051601255610120516013555a90600681146052575b8352f16000553d60015561020051600255005b6201ce809150603f56"  # noqa: E501
                    ),
                ),
                Address("0xf9d1ea8eab6963659ee85b3e0b4d8a57e7edba2b"): Account(
                    code=bytes.fromhex("600100")
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000000f00000000000000000000000000000000000000000000000000000000000000bad",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000bad"): Account(
                    code=bytes.fromhex("650bad0bad0bad60005260206000fd")
                ),
                Address("0x000000000000000000000000000000000000600d"): Account(
                    code=bytes.fromhex("61600d60005260206000f3")
                ),
                Address("0x000000000000000000000000000000000000da7a"): Account(
                    code=bytes.fromhex(
                        "63deadbeef6000526160a760205260406000f3"
                    )
                ),
                Address("0x0000000000000000000000000000000000c0deee"): Account(
                    code=bytes.fromhex(
                        "60406101006000808061da7a5af16010553d60115561010051601255610120516013556000803581813b9283923c600080f06000553d6001553d60006102003e610200516002556102205160035500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000c0def0"): Account(
                    storage={
                        1: 32,
                        2: 0xBAD0BAD0BAD,
                        16: 1,
                        17: 64,
                        18: 0xDEADBEEF,
                        19: 24743,
                    },
                    code=bytes.fromhex(
                        "60406101006000808061da7a5af16010553d60115561010051601255610120516013556000803581813b9283923c600080f06000553d6001553d60006102003e610200516002556102205160035500"  # noqa: E501
                    ),
                ),
                Address("0x0000000000000000000000000000000000c0def5"): Account(
                    code=bytes.fromhex(
                        "60406101006000808061da7a5af16010553d6011556101005160125561012051601355615a176000803581813b9283923c600080f56000553d6001553d60006102003e610200516002556102205160035500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000c0deff"): Account(
                    code=bytes.fromhex(
                        "60406101006000808061da7a5af16010553d601155610100516012556101205160135563bad05a176000803581813b9283923c600080f56000553d6001553d60006102003e610200516002556102205160035500"  # noqa: E501
                    )
                ),
                Address("0x13c950f8740ffaea1869a88d70b029e8b0c9a8da"): Account(
                    code=bytes.fromhex("600100")
                ),
                Address("0xbb0237ab04970e3cf3e813c02064662adc89336b"): Account(
                    code=bytes.fromhex("600100")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 1, 16: 1, 17: 64, 18: 0xDEADBEEF, 19: 24743},
                    code=bytes.fromhex(
                        "60206102008160008062c0de0060043501602435604061010084808061da7a5af16010553d60115561010051601255610120516013555a90600681146052575b8352f16000553d60015561020051600255005b6201ce809150603f56"  # noqa: E501
                    ),
                ),
                Address("0xf9d1ea8eab6963659ee85b3e0b4d8a57e7edba2b"): Account(
                    code=bytes.fromhex("600100")
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000000ee000000000000000000000000000000000000000000000000000000000000600d",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000bad"): Account(
                    code=bytes.fromhex("650bad0bad0bad60005260206000fd")
                ),
                Address("0x000000000000000000000000000000000000600d"): Account(
                    code=bytes.fromhex("61600d60005260206000f3")
                ),
                Address("0x000000000000000000000000000000000000da7a"): Account(
                    code=bytes.fromhex(
                        "63deadbeef6000526160a760205260406000f3"
                    )
                ),
                Address("0x0000000000000000000000000000000000c0deee"): Account(
                    storage={16: 1, 17: 64, 18: 0xDEADBEEF, 19: 24743},
                    code=bytes.fromhex(
                        "60406101006000808061da7a5af16010553d60115561010051601255610120516013556000803581813b9283923c600080f06000553d6001553d60006102003e610200516002556102205160035500"  # noqa: E501
                    ),
                ),
                Address("0x0000000000000000000000000000000000c0def0"): Account(
                    code=bytes.fromhex(
                        "60406101006000808061da7a5af16010553d60115561010051601255610120516013556000803581813b9283923c600080f06000553d6001553d60006102003e610200516002556102205160035500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000c0def5"): Account(
                    code=bytes.fromhex(
                        "60406101006000808061da7a5af16010553d6011556101005160125561012051601355615a176000803581813b9283923c600080f56000553d6001553d60006102003e610200516002556102205160035500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000c0deff"): Account(
                    code=bytes.fromhex(
                        "60406101006000808061da7a5af16010553d601155610100516012556101205160135563bad05a176000803581813b9283923c600080f56000553d6001553d60006102003e610200516002556102205160035500"  # noqa: E501
                    )
                ),
                Address("0x13c950f8740ffaea1869a88d70b029e8b0c9a8da"): Account(
                    code=bytes.fromhex("600100")
                ),
                Address("0xbb0237ab04970e3cf3e813c02064662adc89336b"): Account(
                    code=bytes.fromhex("600100")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 1, 16: 1, 17: 64, 18: 0xDEADBEEF, 19: 24743},
                    code=bytes.fromhex(
                        "60206102008160008062c0de0060043501602435604061010084808061da7a5af16010553d60115561010051601255610120516013555a90600681146052575b8352f16000553d60015561020051600255005b6201ce809150603f56"  # noqa: E501
                    ),
                ),
                Address("0xf9d1ea8eab6963659ee85b3e0b4d8a57e7edba2b"): Account(
                    code=bytes.fromhex("600100")
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000000f0000000000000000000000000000000000000000000000000000000000000600d",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000bad"): Account(
                    code=bytes.fromhex("650bad0bad0bad60005260206000fd")
                ),
                Address("0x000000000000000000000000000000000000600d"): Account(
                    code=bytes.fromhex("61600d60005260206000f3")
                ),
                Address("0x000000000000000000000000000000000000da7a"): Account(
                    code=bytes.fromhex(
                        "63deadbeef6000526160a760205260406000f3"
                    )
                ),
                Address("0x0000000000000000000000000000000000c0deee"): Account(
                    code=bytes.fromhex(
                        "60406101006000808061da7a5af16010553d60115561010051601255610120516013556000803581813b9283923c600080f06000553d6001553d60006102003e610200516002556102205160035500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000c0def0"): Account(
                    storage={
                        0: 0xB44F2C88D3D4283CD1E54E418C4FF7E6A6C73202,
                        16: 1,
                        17: 64,
                        18: 0xDEADBEEF,
                        19: 24743,
                    },
                    code=bytes.fromhex(
                        "60406101006000808061da7a5af16010553d60115561010051601255610120516013556000803581813b9283923c600080f06000553d6001553d60006102003e610200516002556102205160035500"  # noqa: E501
                    ),
                ),
                Address("0x0000000000000000000000000000000000c0def5"): Account(
                    code=bytes.fromhex(
                        "60406101006000808061da7a5af16010553d6011556101005160125561012051601355615a176000803581813b9283923c600080f56000553d6001553d60006102003e610200516002556102205160035500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000c0deff"): Account(
                    code=bytes.fromhex(
                        "60406101006000808061da7a5af16010553d601155610100516012556101205160135563bad05a176000803581813b9283923c600080f56000553d6001553d60006102003e610200516002556102205160035500"  # noqa: E501
                    )
                ),
                Address("0x13c950f8740ffaea1869a88d70b029e8b0c9a8da"): Account(
                    code=bytes.fromhex("600100")
                ),
                Address("0xb44f2c88d3d4283cd1e54e418c4ff7e6a6c73202"): Account(
                    code=bytes.fromhex(
                        "000000000000000000000000000000000000000000000000000000000000600d"  # noqa: E501
                    )
                ),
                Address("0xbb0237ab04970e3cf3e813c02064662adc89336b"): Account(
                    code=bytes.fromhex("600100")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 1, 16: 1, 17: 64, 18: 0xDEADBEEF, 19: 24743},
                    code=bytes.fromhex(
                        "60206102008160008062c0de0060043501602435604061010084808061da7a5af16010553d60115561010051601255610120516013555a90600681146052575b8352f16000553d60015561020051600255005b6201ce809150603f56"  # noqa: E501
                    ),
                ),
                Address("0xf9d1ea8eab6963659ee85b3e0b4d8a57e7edba2b"): Account(
                    code=bytes.fromhex("600100")
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000000f00000000000000000000000000000000000000000000000000000000000000006",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000bad"): Account(
                    code=bytes.fromhex("650bad0bad0bad60005260206000fd")
                ),
                Address("0x000000000000000000000000000000000000600d"): Account(
                    code=bytes.fromhex("61600d60005260206000f3")
                ),
                Address("0x000000000000000000000000000000000000da7a"): Account(
                    code=bytes.fromhex(
                        "63deadbeef6000526160a760205260406000f3"
                    )
                ),
                Address("0x0000000000000000000000000000000000c0deee"): Account(
                    code=bytes.fromhex(
                        "60406101006000808061da7a5af16010553d60115561010051601255610120516013556000803581813b9283923c600080f06000553d6001553d60006102003e610200516002556102205160035500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000c0def0"): Account(
                    code=bytes.fromhex(
                        "60406101006000808061da7a5af16010553d60115561010051601255610120516013556000803581813b9283923c600080f06000553d6001553d60006102003e610200516002556102205160035500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000c0def5"): Account(
                    code=bytes.fromhex(
                        "60406101006000808061da7a5af16010553d6011556101005160125561012051601355615a176000803581813b9283923c600080f56000553d6001553d60006102003e610200516002556102205160035500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000c0deff"): Account(
                    code=bytes.fromhex(
                        "60406101006000808061da7a5af16010553d601155610100516012556101205160135563bad05a176000803581813b9283923c600080f56000553d6001553d60006102003e610200516002556102205160035500"  # noqa: E501
                    )
                ),
                Address("0x13c950f8740ffaea1869a88d70b029e8b0c9a8da"): Account(
                    code=bytes.fromhex("600100")
                ),
                Address("0xbb0237ab04970e3cf3e813c02064662adc89336b"): Account(
                    code=bytes.fromhex("600100")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={16: 1, 17: 64, 18: 0xDEADBEEF, 19: 24743},
                    code=bytes.fromhex(
                        "60206102008160008062c0de0060043501602435604061010084808061da7a5af16010553d60115561010051601255610120516013555a90600681146052575b8352f16000553d60015561020051600255005b6201ce809150603f56"  # noqa: E501
                    ),
                ),
                Address("0xf9d1ea8eab6963659ee85b3e0b4d8a57e7edba2b"): Account(
                    code=bytes.fromhex("600100")
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000000ff0000000000000000000000000000000000000000000000000000000000000bad",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000bad"): Account(
                    code=bytes.fromhex("650bad0bad0bad60005260206000fd")
                ),
                Address("0x000000000000000000000000000000000000600d"): Account(
                    code=bytes.fromhex("61600d60005260206000f3")
                ),
                Address("0x000000000000000000000000000000000000da7a"): Account(
                    code=bytes.fromhex(
                        "63deadbeef6000526160a760205260406000f3"
                    )
                ),
                Address("0x0000000000000000000000000000000000c0deee"): Account(
                    code=bytes.fromhex(
                        "60406101006000808061da7a5af16010553d60115561010051601255610120516013556000803581813b9283923c600080f06000553d6001553d60006102003e610200516002556102205160035500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000c0def0"): Account(
                    code=bytes.fromhex(
                        "60406101006000808061da7a5af16010553d60115561010051601255610120516013556000803581813b9283923c600080f06000553d6001553d60006102003e610200516002556102205160035500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000c0def5"): Account(
                    code=bytes.fromhex(
                        "60406101006000808061da7a5af16010553d6011556101005160125561012051601355615a176000803581813b9283923c600080f56000553d6001553d60006102003e610200516002556102205160035500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000c0deff"): Account(
                    storage={16: 1, 17: 64, 18: 0xDEADBEEF, 19: 24743},
                    code=bytes.fromhex(
                        "60406101006000808061da7a5af16010553d601155610100516012556101205160135563bad05a176000803581813b9283923c600080f56000553d6001553d60006102003e610200516002556102205160035500"  # noqa: E501
                    ),
                ),
                Address("0x13c950f8740ffaea1869a88d70b029e8b0c9a8da"): Account(
                    code=bytes.fromhex("600100")
                ),
                Address("0xbb0237ab04970e3cf3e813c02064662adc89336b"): Account(
                    code=bytes.fromhex("600100")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 1, 16: 1, 17: 64, 18: 0xDEADBEEF, 19: 24743},
                    code=bytes.fromhex(
                        "60206102008160008062c0de0060043501602435604061010084808061da7a5af16010553d60115561010051601255610120516013555a90600681146052575b8352f16000553d60015561020051600255005b6201ce809150603f56"  # noqa: E501
                    ),
                ),
                Address("0xf9d1ea8eab6963659ee85b3e0b4d8a57e7edba2b"): Account(
                    code=bytes.fromhex("600100")
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000000f50000000000000000000000000000000000000000000000000000000000000bad",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000bad"): Account(
                    code=bytes.fromhex("650bad0bad0bad60005260206000fd")
                ),
                Address("0x000000000000000000000000000000000000600d"): Account(
                    code=bytes.fromhex("61600d60005260206000f3")
                ),
                Address("0x000000000000000000000000000000000000da7a"): Account(
                    code=bytes.fromhex(
                        "63deadbeef6000526160a760205260406000f3"
                    )
                ),
                Address("0x0000000000000000000000000000000000c0deee"): Account(
                    code=bytes.fromhex(
                        "60406101006000808061da7a5af16010553d60115561010051601255610120516013556000803581813b9283923c600080f06000553d6001553d60006102003e610200516002556102205160035500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000c0def0"): Account(
                    code=bytes.fromhex(
                        "60406101006000808061da7a5af16010553d60115561010051601255610120516013556000803581813b9283923c600080f06000553d6001553d60006102003e610200516002556102205160035500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000c0def5"): Account(
                    storage={
                        1: 32,
                        2: 0xBAD0BAD0BAD,
                        16: 1,
                        17: 64,
                        18: 0xDEADBEEF,
                        19: 24743,
                    },
                    code=bytes.fromhex(
                        "60406101006000808061da7a5af16010553d6011556101005160125561012051601355615a176000803581813b9283923c600080f56000553d6001553d60006102003e610200516002556102205160035500"  # noqa: E501
                    ),
                ),
                Address("0x0000000000000000000000000000000000c0deff"): Account(
                    code=bytes.fromhex(
                        "60406101006000808061da7a5af16010553d601155610100516012556101205160135563bad05a176000803581813b9283923c600080f56000553d6001553d60006102003e610200516002556102205160035500"  # noqa: E501
                    )
                ),
                Address("0x13c950f8740ffaea1869a88d70b029e8b0c9a8da"): Account(
                    code=bytes.fromhex("600100")
                ),
                Address("0xbb0237ab04970e3cf3e813c02064662adc89336b"): Account(
                    code=bytes.fromhex("600100")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 1, 16: 1, 17: 64, 18: 0xDEADBEEF, 19: 24743},
                    code=bytes.fromhex(
                        "60206102008160008062c0de0060043501602435604061010084808061da7a5af16010553d60115561010051601255610120516013555a90600681146052575b8352f16000553d60015561020051600255005b6201ce809150603f56"  # noqa: E501
                    ),
                ),
                Address("0xf9d1ea8eab6963659ee85b3e0b4d8a57e7edba2b"): Account(
                    code=bytes.fromhex("600100")
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000000ff000000000000000000000000000000000000000000000000000000000000600d",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000bad"): Account(
                    code=bytes.fromhex("650bad0bad0bad60005260206000fd")
                ),
                Address("0x000000000000000000000000000000000000600d"): Account(
                    code=bytes.fromhex("61600d60005260206000f3")
                ),
                Address("0x000000000000000000000000000000000000da7a"): Account(
                    code=bytes.fromhex(
                        "63deadbeef6000526160a760205260406000f3"
                    )
                ),
                Address("0x0000000000000000000000000000000000c0deee"): Account(
                    code=bytes.fromhex(
                        "60406101006000808061da7a5af16010553d60115561010051601255610120516013556000803581813b9283923c600080f06000553d6001553d60006102003e610200516002556102205160035500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000c0def0"): Account(
                    code=bytes.fromhex(
                        "60406101006000808061da7a5af16010553d60115561010051601255610120516013556000803581813b9283923c600080f06000553d6001553d60006102003e610200516002556102205160035500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000c0def5"): Account(
                    code=bytes.fromhex(
                        "60406101006000808061da7a5af16010553d6011556101005160125561012051601355615a176000803581813b9283923c600080f56000553d6001553d60006102003e610200516002556102205160035500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000c0deff"): Account(
                    storage={16: 1, 17: 64, 18: 0xDEADBEEF, 19: 24743},
                    code=bytes.fromhex(
                        "60406101006000808061da7a5af16010553d601155610100516012556101205160135563bad05a176000803581813b9283923c600080f56000553d6001553d60006102003e610200516002556102205160035500"  # noqa: E501
                    ),
                ),
                Address("0x13c950f8740ffaea1869a88d70b029e8b0c9a8da"): Account(
                    code=bytes.fromhex("600100")
                ),
                Address("0xbb0237ab04970e3cf3e813c02064662adc89336b"): Account(
                    code=bytes.fromhex("600100")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 1, 16: 1, 17: 64, 18: 0xDEADBEEF, 19: 24743},
                    code=bytes.fromhex(
                        "60206102008160008062c0de0060043501602435604061010084808061da7a5af16010553d60115561010051601255610120516013555a90600681146052575b8352f16000553d60015561020051600255005b6201ce809150603f56"  # noqa: E501
                    ),
                ),
                Address("0xf9d1ea8eab6963659ee85b3e0b4d8a57e7edba2b"): Account(
                    code=bytes.fromhex("600100")
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000000f5000000000000000000000000000000000000000000000000000000000000600d",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000bad"): Account(
                    code=bytes.fromhex("650bad0bad0bad60005260206000fd")
                ),
                Address("0x000000000000000000000000000000000000600d"): Account(
                    code=bytes.fromhex("61600d60005260206000f3")
                ),
                Address("0x000000000000000000000000000000000000da7a"): Account(
                    code=bytes.fromhex(
                        "63deadbeef6000526160a760205260406000f3"
                    )
                ),
                Address("0x0000000000000000000000000000000000c0deee"): Account(
                    code=bytes.fromhex(
                        "60406101006000808061da7a5af16010553d60115561010051601255610120516013556000803581813b9283923c600080f06000553d6001553d60006102003e610200516002556102205160035500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000c0def0"): Account(
                    code=bytes.fromhex(
                        "60406101006000808061da7a5af16010553d60115561010051601255610120516013556000803581813b9283923c600080f06000553d6001553d60006102003e610200516002556102205160035500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000c0def5"): Account(
                    storage={
                        0: 0x65EE26A034447B6AC64ABDCA1CCCB7B747E4A231,
                        16: 1,
                        17: 64,
                        18: 0xDEADBEEF,
                        19: 24743,
                    },
                    code=bytes.fromhex(
                        "60406101006000808061da7a5af16010553d6011556101005160125561012051601355615a176000803581813b9283923c600080f56000553d6001553d60006102003e610200516002556102205160035500"  # noqa: E501
                    ),
                ),
                Address("0x0000000000000000000000000000000000c0deff"): Account(
                    code=bytes.fromhex(
                        "60406101006000808061da7a5af16010553d601155610100516012556101205160135563bad05a176000803581813b9283923c600080f56000553d6001553d60006102003e610200516002556102205160035500"  # noqa: E501
                    )
                ),
                Address("0x13c950f8740ffaea1869a88d70b029e8b0c9a8da"): Account(
                    code=bytes.fromhex("600100")
                ),
                Address("0x65ee26a034447b6ac64abdca1cccb7b747e4a231"): Account(
                    code=bytes.fromhex(
                        "000000000000000000000000000000000000000000000000000000000000600d"  # noqa: E501
                    )
                ),
                Address("0xbb0237ab04970e3cf3e813c02064662adc89336b"): Account(
                    code=bytes.fromhex("600100")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 1, 16: 1, 17: 64, 18: 0xDEADBEEF, 19: 24743},
                    code=bytes.fromhex(
                        "60206102008160008062c0de0060043501602435604061010084808061da7a5af16010553d60115561010051601255610120516013555a90600681146052575b8352f16000553d60015561020051600255005b6201ce809150603f56"  # noqa: E501
                    ),
                ),
                Address("0xf9d1ea8eab6963659ee85b3e0b4d8a57e7edba2b"): Account(
                    code=bytes.fromhex("600100")
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000000f50000000000000000000000000000000000000000000000000000000000000006",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000000bad"): Account(
                    code=bytes.fromhex("650bad0bad0bad60005260206000fd")
                ),
                Address("0x000000000000000000000000000000000000600d"): Account(
                    code=bytes.fromhex("61600d60005260206000f3")
                ),
                Address("0x000000000000000000000000000000000000da7a"): Account(
                    code=bytes.fromhex(
                        "63deadbeef6000526160a760205260406000f3"
                    )
                ),
                Address("0x0000000000000000000000000000000000c0deee"): Account(
                    code=bytes.fromhex(
                        "60406101006000808061da7a5af16010553d60115561010051601255610120516013556000803581813b9283923c600080f06000553d6001553d60006102003e610200516002556102205160035500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000c0def0"): Account(
                    code=bytes.fromhex(
                        "60406101006000808061da7a5af16010553d60115561010051601255610120516013556000803581813b9283923c600080f06000553d6001553d60006102003e610200516002556102205160035500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000c0def5"): Account(
                    code=bytes.fromhex(
                        "60406101006000808061da7a5af16010553d6011556101005160125561012051601355615a176000803581813b9283923c600080f56000553d6001553d60006102003e610200516002556102205160035500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000c0deff"): Account(
                    code=bytes.fromhex(
                        "60406101006000808061da7a5af16010553d601155610100516012556101205160135563bad05a176000803581813b9283923c600080f56000553d6001553d60006102003e610200516002556102205160035500"  # noqa: E501
                    )
                ),
                Address("0x13c950f8740ffaea1869a88d70b029e8b0c9a8da"): Account(
                    code=bytes.fromhex("600100")
                ),
                Address("0xbb0237ab04970e3cf3e813c02064662adc89336b"): Account(
                    code=bytes.fromhex("600100")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={16: 1, 17: 64, 18: 0xDEADBEEF, 19: 24743},
                    code=bytes.fromhex(
                        "60206102008160008062c0de0060043501602435604061010084808061da7a5af16010553d60115561010051601255610120516013555a90600681146052575b8352f16000553d60015561020051600255005b6201ce809150603f56"  # noqa: E501
                    ),
                ),
                Address("0xf9d1ea8eab6963659ee85b3e0b4d8a57e7edba2b"): Account(
                    code=bytes.fromhex("600100")
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
def test_create_fail_result(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Ori Pomerantz   qbzzt1@gmail.com."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xcccccccccccccccccccccccccccccccccccccccc")
    callee = Address("0x0000000000000000000000000000000000000bad")
    callee_1 = Address("0x000000000000000000000000000000000000600d")
    callee_2 = Address("0x000000000000000000000000000000000000da7a")
    callee_3 = Address("0x0000000000000000000000000000000000c0deee")
    callee_4 = Address("0x0000000000000000000000000000000000c0def0")
    callee_5 = Address("0x0000000000000000000000000000000000c0def5")
    callee_6 = Address("0x0000000000000000000000000000000000c0deff")
    callee_7 = Address("0x13c950f8740ffaea1869a88d70b029e8b0c9a8da")
    callee_8 = Address("0xbb0237ab04970e3cf3e813c02064662adc89336b")
    callee_9 = Address("0xf9d1ea8eab6963659ee85b3e0b4d8a57e7edba2b")

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
        code=bytes.fromhex("650bad0bad0bad60005260206000fd"),
    )
    pre[callee_1] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex("61600d60005260206000f3"),
    )
    pre[callee_2] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex("63deadbeef6000526160a760205260406000f3"),
    )
    pre[callee_3] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex(
            "60406101006000808061da7a5af16010553d601155610100516012556101205160135560"  # noqa: E501
            "00803581813b9283923c600080f06000553d6001553d60006102003e6102005160025561"  # noqa: E501
            "02205160035500"
        ),
    )
    pre[callee_4] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex(
            "60406101006000808061da7a5af16010553d601155610100516012556101205160135560"  # noqa: E501
            "00803581813b9283923c600080f06000553d6001553d60006102003e6102005160025561"  # noqa: E501
            "02205160035500"
        ),
    )
    pre[callee_5] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex(
            "60406101006000808061da7a5af16010553d601155610100516012556101205160135561"  # noqa: E501
            "5a176000803581813b9283923c600080f56000553d6001553d60006102003e6102005160"  # noqa: E501
            "02556102205160035500"
        ),
    )
    pre[callee_6] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex(
            "60406101006000808061da7a5af16010553d601155610100516012556101205160135563"  # noqa: E501
            "bad05a176000803581813b9283923c600080f56000553d6001553d60006102003e610200"  # noqa: E501
            "516002556102205160035500"
        ),
    )
    pre[callee_7] = Account(
        balance=0x600D,
        nonce=1,
        code=bytes.fromhex("600100"),
    )
    pre[sender] = Account(balance=0xBA1A9CE0BA1A9CE, nonce=1)
    pre[callee_8] = Account(
        balance=0x600D,
        nonce=1,
        code=bytes.fromhex("600100"),
    )
    pre[contract] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex(
            "60206102008160008062c0de0060043501602435604061010084808061da7a5af1601055"  # noqa: E501
            "3d60115561010051601255610120516013555a90600681146052575b8352f16000553d60"  # noqa: E501
            "015561020051600255005b6201ce809150603f56"
        ),
    )
    pre[callee_9] = Account(
        balance=0x600D,
        nonce=1,
        code=bytes.fromhex("600100"),
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
