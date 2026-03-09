"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stPreCompiledContracts2/CallEcrecover3Filler.json
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
        "tests/static/state_tests/stPreCompiledContracts2/CallEcrecover3Filler.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_call_ecrecover3(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0x28d98d7cc227972a80fa4a16964272bf8738d792")

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
            "7f2f380a2dea7e778d81affc2443403b8fe4644db442ae4862ff5bb3732829cdb9600052"  # noqa: E501
            "601b6020527f6b65ccb0558806e9b097f27a396d08f964e37b8b7af6ceeb516ff86739fb"  # noqa: E501
            "ea0a6040527f37cbc8d883e129a4b1ef9d5f1df53c4f21a3ef147cf2a50a4ede0eb06ce0"  # noqa: E501
            "92d4606052602060806080600060006001620186a0f160025560a060020a608051066000"  # noqa: E501
            "55600054321460015500"
        ),
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
            storage={
                0: 0xE4319F4B631C6D0FCFC84045DBCB676865FE5E13,
                2: 1,
            },
            code=bytes.fromhex(
                "7f2f380a2dea7e778d81affc2443403b8fe4644db442ae4862ff5bb3732829cdb9600052601b6020527f6b65ccb0558806e9b097f27a396d08f964e37b8b7af6ceeb516ff86739fbea0a6040527f37cbc8d883e129a4b1ef9d5f1df53c4f21a3ef147cf2a50a4ede0eb06ce092d4606052602060806080600060006001620186a0f160025560a060020a60805106600055600054321460015500"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
