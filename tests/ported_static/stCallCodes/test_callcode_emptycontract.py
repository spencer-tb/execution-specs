"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stCallCodes/callcodeEmptycontractFiller.json
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
    ["tests/static/state_tests/stCallCodes/callcodeEmptycontractFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_callcode_emptycontract(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x7f3f285918d9b5e764174551e10b7539b97bbb27")
    contract = Address("0x594f6a1a002fc9949ac40616cc146845680302e1")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[contract] = Account(
        balance=1000,
        nonce=0,
        code=bytes.fromhex(
            "60406000604060006103e873945304eb96065b2a98b57a48a06ae28d285a71b561c350f2"  # noqa: E501
            "60005500"
        ),
    )
    pre[sender] = Account(balance=0x5F5E100, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xa2333eef5630066b928dea5fd85a239f511b5b067d1441ee7ac290d0122b917b"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=1050440,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            storage={0: 1},
            code=bytes.fromhex(
                "60406000604060006103e873945304eb96065b2a98b57a48a06ae28d285a71b561c350f260005500"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
