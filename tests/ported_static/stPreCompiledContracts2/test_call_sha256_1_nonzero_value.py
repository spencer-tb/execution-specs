"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stPreCompiledContracts2
CallSha256_1_nonzeroValueFiller.json
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
        "tests/static/state_tests/stPreCompiledContracts2/CallSha256_1_nonzeroValueFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_call_sha256_1_nonzero_value(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0x39baf944bd1b21e643d8d207a7073ee34a5d2116")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000,
    )

    pre[contract] = Account(
        balance=0xBEBC200,
        nonce=0,
        code=bytes.fromhex(
            "60206000600060006013600262030d40f160025560005160005500"
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
                0: 0xE3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855,  # noqa: E501
                2: 1,
            },
            code=bytes.fromhex(
                "60206000600060006013600262030d40f160025560005160005500"
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
