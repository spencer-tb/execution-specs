"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stPreCompiledContracts2
CALLCODEEcrecover0_completeReturnValueFiller.json
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
        "tests/static/state_tests/stPreCompiledContracts2/CALLCODEEcrecover0_completeReturnValueFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_callcode_ecrecover0_complete_return_value(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x095e7baea6a6c7c4c2dfeb977efac326af552d87")

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
            "4549606052602060806080600060006001610bb8f260025560805160005500"
        ),
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
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
            storage={
                0: 0xA94F5374FCE5EDBC8E2A8697C15331677E6EBF0B,
                2: 1,
            },
            code=bytes.fromhex(
                "7f18c547e4f7b0f325ad1e56f57e26c745b09a3e503d86e00e5255ff7f715d3d1c600052601c6020527f73b1693892219d736caba55bdb67216e485557ea6b6af75f37096c9aa6a5a75f6040527feeb940b1d03b21e36b0e47e79769f095fe2ab855bd91e3a38756b7d75a9c4549606052602060806080600060006001610bb8f260025560805160005500"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
