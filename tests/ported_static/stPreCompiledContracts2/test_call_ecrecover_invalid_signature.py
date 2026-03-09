"""
CALL to ECREC precompile with input which is a completely invalid signature...

Ported from:
tests/static/state_tests/stPreCompiledContracts2
CallEcrecoverInvalidSignatureFiller.json
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
        "tests/static/state_tests/stPreCompiledContracts2/CallEcrecoverInvalidSignatureFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_call_ecrecover_invalid_signature(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """CALL to ECREC precompile with input which is a completely invalid..."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0x2b8fd4adb0602fe9ee5823b0576f619daefbd369")

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
            "7f1122334455667788991011121314151617181920212223242526272829303132608052"  # noqa: E501
            "602060806080600060006001620493e0f15060805160005500"
        ),
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xe04d1ac7ddda0c98397d56a0b501e960d4cd325a39286919ac23c1a07009a869"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=3652240,
        gas_price=10,
        nonce=0,
        value=100000,
    )

    post = {
        contract: Account(
            storage={
                0: 0x1122334455667788991011121314151617181920212223242526272829303132,  # noqa: E501
            },
            code=bytes.fromhex(
                "7f1122334455667788991011121314151617181920212223242526272829303132608052602060806080600060006001620493e0f15060805160005500"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
