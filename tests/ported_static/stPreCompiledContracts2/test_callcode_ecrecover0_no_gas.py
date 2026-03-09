"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stPreCompiledContracts2
CALLCODEEcrecover0_NoGasFiller.json
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
        "tests/static/state_tests/stPreCompiledContracts2/CALLCODEEcrecover0_NoGasFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_callcode_ecrecover0_no_gas(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0x642b4bc6fe2e1633caaf1ad06e473299adb5cfd2")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[contract] = Account(
        balance=0x1312D00,
        nonce=0,
        code=bytes.fromhex(
            "7f18c547e4f7b0f325ad1e56f57e26c745b09a3e503d86e00e5255ff7f715d3d1c600052"  # noqa: E501
            "601c6020527f73b1693892219d736caba55bdb67216e485557ea6b6af75f37096c9aa6a5"  # noqa: E501
            "a75f6040527feeb940b1d03b21e36b0e47e79769f095fe2ab855bd91e3a38756b7d75a9c"  # noqa: E501
            "45496060526020608060806000600160016000f260025560a060020a6080510660005560"  # noqa: E501
            "0054321460015500"
        ),
        storage={0x0: 0xC, 0x1: 0xC, 0x2: 0xC},
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xe04d1ac7ddda0c98397d56a0b501e960d4cd325a39286919ac23c1a07009a869"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=365224,
        gas_price=10,
        nonce=0,
        value=100000,
    )

    post = {
        contract: Account(
            code=bytes.fromhex(
                "7f18c547e4f7b0f325ad1e56f57e26c745b09a3e503d86e00e5255ff7f715d3d1c600052601c6020527f73b1693892219d736caba55bdb67216e485557ea6b6af75f37096c9aa6a5a75f6040527feeb940b1d03b21e36b0e47e79769f095fe2ab855bd91e3a38756b7d75a9c45496060526020608060806000600160016000f260025560a060020a60805106600055600054321460015500"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
