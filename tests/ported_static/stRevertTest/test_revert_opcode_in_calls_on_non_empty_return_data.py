"""
Test checks that the returndata buffer is changed when a subcall REVERTs. ...

Ported from:
tests/static/state_tests/stRevertTest
RevertOpcodeInCallsOnNonEmptyReturnDataFiller.json
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
    [
        "tests/static/state_tests/stRevertTest/RevertOpcodeInCallsOnNonEmptyReturnDataFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, tx_gas_limit, expected_post",
    [
        (
            "000000000000000000000000e73611b5b479b30c93ac377aeb3bfb199764f3c3",
            860000,
            {
                Address("0x127eaf7e31d691a8393b7a2f84a6e94372190c01"): Account(
                    code=bytes.fromhex("600c60015260406000f300")
                ),
                Address("0x172a8f572404293aa810685dfdc6f740c300cc4b"): Account(
                    storage={10: 1},
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f150600060006000600060006000356203f7a0f1600a5500"  # noqa: E501
                    ),
                ),
                Address("0x6bacdfa8216dbb2a09819f8739e57ae3574c9fff"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f1506000600060006000600073ea519c47889074e6378b0d83747f2c3ea0b9cbc9620186a0f16000553d60025500"  # noqa: E501
                    )
                ),
                Address("0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b"): Account(
                    code=bytes.fromhex("600c60015560016000fd600d60035500")
                ),
                Address("0xc9da6cd8413f64323f12cd44c99671f280f15e1c"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f150600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f26000553d60025500"  # noqa: E501
                    )
                ),
                Address("0xe73611b5b479b30c93ac377aeb3bfb199764f3c3"): Account(
                    storage={2: 1},
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f150600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f16000553d60025500"  # noqa: E501
                    ),
                ),
                Address("0xea519c47889074e6378b0d83747f2c3ea0b9cbc9"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f150600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f16004553d60055500"  # noqa: E501
                    )
                ),
                Address("0xf20ccaf271beaa36e7cf4c9ced2867fac9558f14"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f15060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f46000553d60025500"  # noqa: E501
                    )
                ),
            },
        ),
        (
            "000000000000000000000000e73611b5b479b30c93ac377aeb3bfb199764f3c3",
            28000,
            {
                Address("0x127eaf7e31d691a8393b7a2f84a6e94372190c01"): Account(
                    code=bytes.fromhex("600c60015260406000f300")
                ),
                Address("0x172a8f572404293aa810685dfdc6f740c300cc4b"): Account(
                    storage={10: 255},
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f150600060006000600060006000356203f7a0f1600a5500"  # noqa: E501
                    ),
                ),
                Address("0x6bacdfa8216dbb2a09819f8739e57ae3574c9fff"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f1506000600060006000600073ea519c47889074e6378b0d83747f2c3ea0b9cbc9620186a0f16000553d60025500"  # noqa: E501
                    )
                ),
                Address("0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b"): Account(
                    code=bytes.fromhex("600c60015560016000fd600d60035500")
                ),
                Address("0xc9da6cd8413f64323f12cd44c99671f280f15e1c"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f150600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f26000553d60025500"  # noqa: E501
                    )
                ),
                Address("0xe73611b5b479b30c93ac377aeb3bfb199764f3c3"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f150600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f16000553d60025500"  # noqa: E501
                    )
                ),
                Address("0xea519c47889074e6378b0d83747f2c3ea0b9cbc9"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f150600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f16004553d60055500"  # noqa: E501
                    )
                ),
                Address("0xf20ccaf271beaa36e7cf4c9ced2867fac9558f14"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f15060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f46000553d60025500"  # noqa: E501
                    )
                ),
            },
        ),
        (
            "000000000000000000000000c9da6cd8413f64323f12cd44c99671f280f15e1c",
            860000,
            {
                Address("0x127eaf7e31d691a8393b7a2f84a6e94372190c01"): Account(
                    code=bytes.fromhex("600c60015260406000f300")
                ),
                Address("0x172a8f572404293aa810685dfdc6f740c300cc4b"): Account(
                    storage={10: 1},
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f150600060006000600060006000356203f7a0f1600a5500"  # noqa: E501
                    ),
                ),
                Address("0x6bacdfa8216dbb2a09819f8739e57ae3574c9fff"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f1506000600060006000600073ea519c47889074e6378b0d83747f2c3ea0b9cbc9620186a0f16000553d60025500"  # noqa: E501
                    )
                ),
                Address("0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b"): Account(
                    code=bytes.fromhex("600c60015560016000fd600d60035500")
                ),
                Address("0xc9da6cd8413f64323f12cd44c99671f280f15e1c"): Account(
                    storage={2: 1},
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f150600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f26000553d60025500"  # noqa: E501
                    ),
                ),
                Address("0xe73611b5b479b30c93ac377aeb3bfb199764f3c3"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f150600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f16000553d60025500"  # noqa: E501
                    )
                ),
                Address("0xea519c47889074e6378b0d83747f2c3ea0b9cbc9"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f150600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f16004553d60055500"  # noqa: E501
                    )
                ),
                Address("0xf20ccaf271beaa36e7cf4c9ced2867fac9558f14"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f15060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f46000553d60025500"  # noqa: E501
                    )
                ),
            },
        ),
        (
            "000000000000000000000000c9da6cd8413f64323f12cd44c99671f280f15e1c",
            28000,
            {
                Address("0x127eaf7e31d691a8393b7a2f84a6e94372190c01"): Account(
                    code=bytes.fromhex("600c60015260406000f300")
                ),
                Address("0x172a8f572404293aa810685dfdc6f740c300cc4b"): Account(
                    storage={10: 255},
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f150600060006000600060006000356203f7a0f1600a5500"  # noqa: E501
                    ),
                ),
                Address("0x6bacdfa8216dbb2a09819f8739e57ae3574c9fff"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f1506000600060006000600073ea519c47889074e6378b0d83747f2c3ea0b9cbc9620186a0f16000553d60025500"  # noqa: E501
                    )
                ),
                Address("0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b"): Account(
                    code=bytes.fromhex("600c60015560016000fd600d60035500")
                ),
                Address("0xc9da6cd8413f64323f12cd44c99671f280f15e1c"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f150600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f26000553d60025500"  # noqa: E501
                    )
                ),
                Address("0xe73611b5b479b30c93ac377aeb3bfb199764f3c3"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f150600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f16000553d60025500"  # noqa: E501
                    )
                ),
                Address("0xea519c47889074e6378b0d83747f2c3ea0b9cbc9"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f150600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f16004553d60055500"  # noqa: E501
                    )
                ),
                Address("0xf20ccaf271beaa36e7cf4c9ced2867fac9558f14"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f15060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f46000553d60025500"  # noqa: E501
                    )
                ),
            },
        ),
        (
            "000000000000000000000000f20ccaf271beaa36e7cf4c9ced2867fac9558f14",
            860000,
            {
                Address("0x127eaf7e31d691a8393b7a2f84a6e94372190c01"): Account(
                    code=bytes.fromhex("600c60015260406000f300")
                ),
                Address("0x172a8f572404293aa810685dfdc6f740c300cc4b"): Account(
                    storage={10: 1},
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f150600060006000600060006000356203f7a0f1600a5500"  # noqa: E501
                    ),
                ),
                Address("0x6bacdfa8216dbb2a09819f8739e57ae3574c9fff"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f1506000600060006000600073ea519c47889074e6378b0d83747f2c3ea0b9cbc9620186a0f16000553d60025500"  # noqa: E501
                    )
                ),
                Address("0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b"): Account(
                    code=bytes.fromhex("600c60015560016000fd600d60035500")
                ),
                Address("0xc9da6cd8413f64323f12cd44c99671f280f15e1c"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f150600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f26000553d60025500"  # noqa: E501
                    )
                ),
                Address("0xe73611b5b479b30c93ac377aeb3bfb199764f3c3"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f150600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f16000553d60025500"  # noqa: E501
                    )
                ),
                Address("0xea519c47889074e6378b0d83747f2c3ea0b9cbc9"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f150600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f16004553d60055500"  # noqa: E501
                    )
                ),
                Address("0xf20ccaf271beaa36e7cf4c9ced2867fac9558f14"): Account(
                    storage={2: 1},
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f15060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f46000553d60025500"  # noqa: E501
                    ),
                ),
            },
        ),
        (
            "000000000000000000000000f20ccaf271beaa36e7cf4c9ced2867fac9558f14",
            28000,
            {
                Address("0x127eaf7e31d691a8393b7a2f84a6e94372190c01"): Account(
                    code=bytes.fromhex("600c60015260406000f300")
                ),
                Address("0x172a8f572404293aa810685dfdc6f740c300cc4b"): Account(
                    storage={10: 255},
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f150600060006000600060006000356203f7a0f1600a5500"  # noqa: E501
                    ),
                ),
                Address("0x6bacdfa8216dbb2a09819f8739e57ae3574c9fff"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f1506000600060006000600073ea519c47889074e6378b0d83747f2c3ea0b9cbc9620186a0f16000553d60025500"  # noqa: E501
                    )
                ),
                Address("0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b"): Account(
                    code=bytes.fromhex("600c60015560016000fd600d60035500")
                ),
                Address("0xc9da6cd8413f64323f12cd44c99671f280f15e1c"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f150600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f26000553d60025500"  # noqa: E501
                    )
                ),
                Address("0xe73611b5b479b30c93ac377aeb3bfb199764f3c3"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f150600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f16000553d60025500"  # noqa: E501
                    )
                ),
                Address("0xea519c47889074e6378b0d83747f2c3ea0b9cbc9"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f150600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f16004553d60055500"  # noqa: E501
                    )
                ),
                Address("0xf20ccaf271beaa36e7cf4c9ced2867fac9558f14"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f15060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f46000553d60025500"  # noqa: E501
                    )
                ),
            },
        ),
        (
            "0000000000000000000000006bacdfa8216dbb2a09819f8739e57ae3574c9fff",
            860000,
            {
                Address("0x127eaf7e31d691a8393b7a2f84a6e94372190c01"): Account(
                    code=bytes.fromhex("600c60015260406000f300")
                ),
                Address("0x172a8f572404293aa810685dfdc6f740c300cc4b"): Account(
                    storage={10: 1},
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f150600060006000600060006000356203f7a0f1600a5500"  # noqa: E501
                    ),
                ),
                Address("0x6bacdfa8216dbb2a09819f8739e57ae3574c9fff"): Account(
                    storage={0: 1},
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f1506000600060006000600073ea519c47889074e6378b0d83747f2c3ea0b9cbc9620186a0f16000553d60025500"  # noqa: E501
                    ),
                ),
                Address("0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b"): Account(
                    code=bytes.fromhex("600c60015560016000fd600d60035500")
                ),
                Address("0xc9da6cd8413f64323f12cd44c99671f280f15e1c"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f150600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f26000553d60025500"  # noqa: E501
                    )
                ),
                Address("0xe73611b5b479b30c93ac377aeb3bfb199764f3c3"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f150600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f16000553d60025500"  # noqa: E501
                    )
                ),
                Address("0xea519c47889074e6378b0d83747f2c3ea0b9cbc9"): Account(
                    storage={5: 1},
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f150600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f16004553d60055500"  # noqa: E501
                    ),
                ),
                Address("0xf20ccaf271beaa36e7cf4c9ced2867fac9558f14"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f15060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f46000553d60025500"  # noqa: E501
                    )
                ),
            },
        ),
        (
            "0000000000000000000000006bacdfa8216dbb2a09819f8739e57ae3574c9fff",
            28000,
            {
                Address("0x127eaf7e31d691a8393b7a2f84a6e94372190c01"): Account(
                    code=bytes.fromhex("600c60015260406000f300")
                ),
                Address("0x172a8f572404293aa810685dfdc6f740c300cc4b"): Account(
                    storage={10: 255},
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f150600060006000600060006000356203f7a0f1600a5500"  # noqa: E501
                    ),
                ),
                Address("0x6bacdfa8216dbb2a09819f8739e57ae3574c9fff"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f1506000600060006000600073ea519c47889074e6378b0d83747f2c3ea0b9cbc9620186a0f16000553d60025500"  # noqa: E501
                    )
                ),
                Address("0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b"): Account(
                    code=bytes.fromhex("600c60015560016000fd600d60035500")
                ),
                Address("0xc9da6cd8413f64323f12cd44c99671f280f15e1c"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f150600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f26000553d60025500"  # noqa: E501
                    )
                ),
                Address("0xe73611b5b479b30c93ac377aeb3bfb199764f3c3"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f150600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f16000553d60025500"  # noqa: E501
                    )
                ),
                Address("0xea519c47889074e6378b0d83747f2c3ea0b9cbc9"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f150600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f16004553d60055500"  # noqa: E501
                    )
                ),
                Address("0xf20ccaf271beaa36e7cf4c9ced2867fac9558f14"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f15060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f46000553d60025500"  # noqa: E501
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
    ],
)
@pytest.mark.pre_alloc_mutable
def test_revert_opcode_in_calls_on_non_empty_return_data(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    tx_gas_limit: int,
    expected_post: dict,
) -> None:
    """Test checks that the returndata buffer is changed when a subcall..."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xfaa10b404ab607779993c016cd5da73ae1f29d7e")
    contract = Address("0x172a8f572404293aa810685dfdc6f740c300cc4b")
    callee = Address("0x127eaf7e31d691a8393b7a2f84a6e94372190c01")
    callee_1 = Address("0x6bacdfa8216dbb2a09819f8739e57ae3574c9fff")
    callee_2 = Address("0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b")
    callee_3 = Address("0xc9da6cd8413f64323f12cd44c99671f280f15e1c")
    callee_4 = Address("0xe73611b5b479b30c93ac377aeb3bfb199764f3c3")
    callee_5 = Address("0xea519c47889074e6378b0d83747f2c3ea0b9cbc9")
    callee_6 = Address("0xf20ccaf271beaa36e7cf4c9ced2867fac9558f14")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[callee] = Account(
        balance=1,
        nonce=0,
        code=bytes.fromhex("600c60015260406000f300"),
    )
    pre[contract] = Account(
        balance=1,
        nonce=0,
        code=bytes.fromhex(
            "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f15060"  # noqa: E501
            "0060006000600060006000356203f7a0f1600a5500"
        ),
        storage={0xA: 0xFF},
    )
    pre[callee_1] = Account(
        balance=1,
        nonce=0,
        code=bytes.fromhex(
            "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f15060"  # noqa: E501
            "00600060006000600073ea519c47889074e6378b0d83747f2c3ea0b9cbc9620186a0f160"  # noqa: E501
            "00553d60025500"
        ),
    )
    pre[callee_2] = Account(
        balance=1,
        nonce=0,
        code=bytes.fromhex("600c60015560016000fd600d60035500"),
    )
    pre[callee_3] = Account(
        balance=1,
        nonce=0,
        code=bytes.fromhex(
            "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f15060"  # noqa: E501
            "0060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f26000"  # noqa: E501
            "553d60025500"
        ),
    )
    pre[callee_4] = Account(
        balance=1,
        nonce=0,
        code=bytes.fromhex(
            "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f15060"  # noqa: E501
            "0060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f16000"  # noqa: E501
            "553d60025500"
        ),
    )
    pre[callee_5] = Account(
        balance=1,
        nonce=0,
        code=bytes.fromhex(
            "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f15060"  # noqa: E501
            "0060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f16004"  # noqa: E501
            "553d60055500"
        ),
    )
    pre[callee_6] = Account(
        balance=1,
        nonce=0,
        code=bytes.fromhex(
            "6000600060006000600073127eaf7e31d691a8393b7a2f84a6e94372190c016000f15060"  # noqa: E501
            "006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f46000553d"  # noqa: E501
            "60025500"
        ),
    )
    pre[sender] = Account(balance=0xE8D4A51000, nonce=0)

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x4f31b3206fbf0e0e598b9b1a7d8ac86302a0ff1d8930738f1bebae9b67173e52"  # noqa: E501
        ),
        to=contract,
        data=tx_data,
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
