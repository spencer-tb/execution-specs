"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stPreCompiledContracts/sec80Filler.json
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
    ["tests/static/state_tests/stPreCompiledContracts/sec80Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_sec80(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0x39c2fbd2d4e46fa75775649472ddb79e836160b0")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000,
    )

    pre[contract] = Account(
        balance=0x1312D00,
        nonce=0,
        code=bytes.fromhex(
            "601b565b6000555b005b630badf00d6003565b63c001f00d6003565b7319e7e376e7c213"  # noqa: E501
            "b7e7e7e46cc70a5dd086daff2a7f22ae6da6b482f9b1b19b0b897c3fd43884180a1c5ee3"  # noqa: E501
            "61e1107a1bc635649dda600052601b603f537f16433dce375ce6dc8151d3f0a22728bc4a"  # noqa: E501
            "1d9fd6ed39dfd18b4609331937367f6040527f306964c0cf5d74f04129fdc60b54d35b59"  # noqa: E501
            "6dde1bf89ad92cb4123318f4c0e40060605260206080607f60006000600161fffff21560"  # noqa: E501
            "075760805114601257600956"
        ),
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xe04d1ac7ddda0c98397d56a0b501e960d4cd325a39286919ac23c1a07009a869"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=10000000,
        gas_price=10,
        nonce=0,
        value=100000,
    )

    post = {
        contract: Account(
            storage={0: 0xC001F00D},
            code=bytes.fromhex(
                "601b565b6000555b005b630badf00d6003565b63c001f00d6003565b7319e7e376e7c213b7e7e7e46cc70a5dd086daff2a7f22ae6da6b482f9b1b19b0b897c3fd43884180a1c5ee361e1107a1bc635649dda600052601b603f537f16433dce375ce6dc8151d3f0a22728bc4a1d9fd6ed39dfd18b4609331937367f6040527f306964c0cf5d74f04129fdc60b54d35b596dde1bf89ad92cb4123318f4c0e40060605260206080607f60006000600161fffff21560075760805114601257600956"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
