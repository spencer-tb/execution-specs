"""
Ori Pomerantz qbzzt1@gmail.com.

Ported from:
tests/static/state_tests/stMemoryTest/oogFiller.yml
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
    ["tests/static/state_tests/stMemoryTest/oogFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000000a000000000000000000000000000000000000000000000000000000000000039d0",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    )
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000000a100000000000000000000000000000000000000000000000000000000000039d0",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    )
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000000a200000000000000000000000000000000000000000000000000000000000039d0",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    )
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000000a300000000000000000000000000000000000000000000000000000000000039d0",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    )
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000000a400000000000000000000000000000000000000000000000000000000000039d0",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    )
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000000f00000000000000000000000000000000000000000000000000000000000007d00",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    )
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000000f50000000000000000000000000000000000000000000000000000000000007d00",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    )
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000000f300000000000000000000000000000000000000000000000000000000000036b0",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    )
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000000f100000000000000000000000000000000000000000000000000000000000002bc",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    )
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000000f200000000000000000000000000000000000000000000000000000000000002bc",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    )
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000000f400000000000000000000000000000000000000000000000000000000000002bc",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    )
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000000fa00000000000000000000000000000000000000000000000000000000000002bc",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    )
                ),
            },
        ),
        (
            "1a8451e60000000000000000000000000000000000000000000000000000000000000037000000000000000000000000000000000000000000000000000000000000032a",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    )
                ),
            },
        ),
        (
            "1a8451e60000000000000000000000000000000000000000000000000000000000000039000000000000000000000000000000000000000000000000000000000000032a",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    )
                ),
            },
        ),
        (
            "1a8451e6000000000000000000000000000000000000000000000000000000000000003c00000000000000000000000000000000000000000000000000000000000002bc",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    )
                ),
            },
        ),
        (
            "1a8451e6000000000000000000000000000000000000000000000000000000000000003e00000000000000000000000000000000000000000000000000000000000007d0",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    )
                ),
            },
        ),
        (
            "1a8451e6000000000000000000000000000000000000000000000000000000000000003e0000000000000000000000000000000000000000000000000000000000000c01",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    )
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000000510000000000000000000000000000000000000000000000000000000000000190",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    )
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000000520000000000000000000000000000000000000000000000000000000000000190",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    )
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000000530000000000000000000000000000000000000000000000000000000000000190",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    )
                ),
            },
        ),
        (
            "1a8451e6000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000004ba",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    )
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000000a0000000000000000000000000000000000000000000000000000000000000ffff",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 1},
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    ),
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000000a1000000000000000000000000000000000000000000000000000000000000ffff",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 1},
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    ),
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000000a2000000000000000000000000000000000000000000000000000000000000ffff",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 1},
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    ),
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000000a3000000000000000000000000000000000000000000000000000000000000ffff",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 1},
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    ),
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000000a4000000000000000000000000000000000000000000000000000000000000ffff",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 1},
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    ),
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000000f0000000000000000000000000000000000000000000000000000000000000ffff",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 1},
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    ),
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000000f5000000000000000000000000000000000000000000000000000000000000ffff",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 1},
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    ),
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000000f3000000000000000000000000000000000000000000000000000000000000ffff",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 1},
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    ),
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000000f1000000000000000000000000000000000000000000000000000000000000ffff",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 1},
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    ),
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000000f2000000000000000000000000000000000000000000000000000000000000ffff",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 1},
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    ),
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000000f4000000000000000000000000000000000000000000000000000000000000ffff",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 1},
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    ),
                ),
            },
        ),
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000000fa000000000000000000000000000000000000000000000000000000000000ffff",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 1},
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    ),
                ),
            },
        ),
        (
            "1a8451e60000000000000000000000000000000000000000000000000000000000000037000000000000000000000000000000000000000000000000000000000000ffff",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 1},
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    ),
                ),
            },
        ),
        (
            "1a8451e60000000000000000000000000000000000000000000000000000000000000039000000000000000000000000000000000000000000000000000000000000ffff",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 1},
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    ),
                ),
            },
        ),
        (
            "1a8451e6000000000000000000000000000000000000000000000000000000000000003c000000000000000000000000000000000000000000000000000000000000ffff",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 1},
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    ),
                ),
            },
        ),
        (
            "1a8451e6000000000000000000000000000000000000000000000000000000000000003e000000000000000000000000000000000000000000000000000000000000ffff",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 1},
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    ),
                ),
            },
        ),
        (
            "1a8451e6000000000000000000000000000000000000000000000000000000000000003e0000000000000000000000000000000000000000000000000000000000000c02",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 1},
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    ),
                ),
            },
        ),
        (
            "1a8451e60000000000000000000000000000000000000000000000000000000000000051000000000000000000000000000000000000000000000000000000000000ffff",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 1},
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    ),
                ),
            },
        ),
        (
            "1a8451e60000000000000000000000000000000000000000000000000000000000000052000000000000000000000000000000000000000000000000000000000000ffff",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 1},
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    ),
                ),
            },
        ),
        (
            "1a8451e60000000000000000000000000000000000000000000000000000000000000053000000000000000000000000000000000000000000000000000000000000ffff",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 1},
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
                    ),
                ),
            },
        ),
        (
            "1a8451e60000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000ffff",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000010020"): Account(
                    code=bytes.fromhex("61100060002000")
                ),
                Address("0x0000000000000000000000000000000000010037"): Account(
                    code=bytes.fromhex("6110006000803700")
                ),
                Address("0x0000000000000000000000000000000000010039"): Account(
                    code=bytes.fromhex("6110006000803900")
                ),
                Address("0x000000000000000000000000000000000001003c"): Account(
                    code=bytes.fromhex("611000600080303c00")
                ),
                Address("0x000000000000000000000000000000000001003e"): Account(
                    code=bytes.fromhex(
                        "602060008181806201113e5af150601060006110003e00"
                    )
                ),
                Address("0x0000000000000000000000000000000000010051"): Account(
                    code=bytes.fromhex("6110005100")
                ),
                Address("0x0000000000000000000000000000000000010052"): Account(
                    code=bytes.fromhex("60ff6110005200")
                ),
                Address("0x0000000000000000000000000000000000010053"): Account(
                    code=bytes.fromhex("60ff6110005300")
                ),
                Address("0x00000000000000000000000000000000000100a0"): Account(
                    code=bytes.fromhex("602062010000a000")
                ),
                Address("0x00000000000000000000000000000000000100a1"): Account(
                    code=bytes.fromhex("6001602062010000a100")
                ),
                Address("0x00000000000000000000000000000000000100a2"): Account(
                    code=bytes.fromhex("60026001602062010000a200")
                ),
                Address("0x00000000000000000000000000000000000100a3"): Account(
                    code=bytes.fromhex("600360026001602062010000a300")
                ),
                Address("0x00000000000000000000000000000000000100a4"): Account(
                    code=bytes.fromhex("6004600360026001602062010000a400")
                ),
                Address("0x00000000000000000000000000000000000100f0"): Account(
                    code=bytes.fromhex("6020620100006000f000")
                ),
                Address("0x00000000000000000000000000000000000100f1"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af100")
                ),
                Address("0x00000000000000000000000000000000000100f2"): Account(
                    code=bytes.fromhex("600080806201000081620111f15af200")
                ),
                Address("0x00000000000000000000000000000000000100f3"): Account(
                    code=bytes.fromhex("602062010000f3")
                ),
                Address("0x00000000000000000000000000000000000100f4"): Account(
                    code=bytes.fromhex("6000808062010000620111f15af400")
                ),
                Address("0x00000000000000000000000000000000000100f5"): Account(
                    code=bytes.fromhex("615a176020620100006000f500")
                ),
                Address("0x00000000000000000000000000000000000100fa"): Account(
                    code=bytes.fromhex("6000808062010000620111f15afa00")
                ),
                Address("0x000000000000000000000000000000000001113e"): Account(
                    code=bytes.fromhex(
                        "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2060005260206000f3"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000111f1"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 1},
                    code=bytes.fromhex(
                        "6000808080806201000060043501602435f160005500"
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
        "case17",
        "case18",
        "case19",
        "case20",
        "case21",
        "case22",
        "case23",
        "case24",
        "case25",
        "case26",
        "case27",
        "case28",
        "case29",
        "case30",
        "case31",
        "case32",
        "case33",
        "case34",
        "case35",
        "case36",
        "case37",
        "case38",
        "case39",
        "case40",
        "case41",
    ],
)
@pytest.mark.pre_alloc_mutable
def test_oog(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Ori Pomerantz qbzzt1@gmail.com."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xcccccccccccccccccccccccccccccccccccccccc")
    callee = Address("0x0000000000000000000000000000000000010020")
    callee_1 = Address("0x0000000000000000000000000000000000010037")
    callee_2 = Address("0x0000000000000000000000000000000000010039")
    callee_3 = Address("0x000000000000000000000000000000000001003c")
    callee_4 = Address("0x000000000000000000000000000000000001003e")
    callee_5 = Address("0x0000000000000000000000000000000000010051")
    callee_6 = Address("0x0000000000000000000000000000000000010052")
    callee_7 = Address("0x0000000000000000000000000000000000010053")
    callee_8 = Address("0x00000000000000000000000000000000000100a0")
    callee_9 = Address("0x00000000000000000000000000000000000100a1")
    callee_10 = Address("0x00000000000000000000000000000000000100a2")
    callee_11 = Address("0x00000000000000000000000000000000000100a3")
    callee_12 = Address("0x00000000000000000000000000000000000100a4")
    callee_13 = Address("0x00000000000000000000000000000000000100f0")
    callee_14 = Address("0x00000000000000000000000000000000000100f1")
    callee_15 = Address("0x00000000000000000000000000000000000100f2")
    callee_16 = Address("0x00000000000000000000000000000000000100f3")
    callee_17 = Address("0x00000000000000000000000000000000000100f4")
    callee_18 = Address("0x00000000000000000000000000000000000100f5")
    callee_19 = Address("0x00000000000000000000000000000000000100fa")
    callee_20 = Address("0x000000000000000000000000000000000001113e")
    callee_21 = Address("0x00000000000000000000000000000000000111f1")

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
        code=bytes.fromhex("61100060002000"),
    )
    pre[callee_1] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex("6110006000803700"),
    )
    pre[callee_2] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex("6110006000803900"),
    )
    pre[callee_3] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex("611000600080303c00"),
    )
    pre[callee_4] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex("602060008181806201113e5af150601060006110003e00"),
    )
    pre[callee_5] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex("6110005100"),
    )
    pre[callee_6] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex("60ff6110005200"),
    )
    pre[callee_7] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex("60ff6110005300"),
    )
    pre[callee_8] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex("602062010000a000"),
    )
    pre[callee_9] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex("6001602062010000a100"),
    )
    pre[callee_10] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex("60026001602062010000a200"),
    )
    pre[callee_11] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex("600360026001602062010000a300"),
    )
    pre[callee_12] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex("6004600360026001602062010000a400"),
    )
    pre[callee_13] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex("6020620100006000f000"),
    )
    pre[callee_14] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex("600080806201000081620111f15af100"),
    )
    pre[callee_15] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex("600080806201000081620111f15af200"),
    )
    pre[callee_16] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex("602062010000f3"),
    )
    pre[callee_17] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex("6000808062010000620111f15af400"),
    )
    pre[callee_18] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex("615a176020620100006000f500"),
    )
    pre[callee_19] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex("6000808062010000620111f15afa00"),
    )
    pre[callee_20] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex(
            "7f0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f20600052"  # noqa: E501
            "60206000f3"
        ),
    )
    pre[callee_21] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex("00"),
    )
    pre[sender] = Account(balance=0xBA1A9CE0BA1A9CE, nonce=1)
    pre[contract] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex("6000808080806201000060043501602435f160005500"),
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
