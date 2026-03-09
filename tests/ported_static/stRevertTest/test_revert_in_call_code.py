"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRevertTest/RevertInCallCodeFiller.json
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
    ["tests/static/state_tests/stRevertTest/RevertInCallCodeFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_revert_in_call_code(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x7f3f285918d9b5e764174551e10b7539b97bbb27")
    contract = Address("0x5e1d76d7badbad41710e47410dba9226c255d229")
    callee = Address("0x26bc42b8191ccb142cb8cbc3490bd3bdce465591")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("61223260005260206000fd00"),
    )
    pre[contract] = Account(
        balance=1000,
        nonce=0,
        code=bytes.fromhex(
            "60406000604060006103e87326bc42b8191ccb142cb8cbc3490bd3bdce46559161c350f2"  # noqa: E501
            "6000553d6001556020600060403e60405160025500"
        ),
    )
    pre[sender] = Account(balance=0x5F5E100, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xa2333eef5630066b928dea5fd85a239f511b5b067d1441ee7ac290d0122b917b"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=105044,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        callee: Account(code=bytes.fromhex("61223260005260206000fd00")),
        contract: Account(
            storage={1: 32, 2: 8754},
            code=bytes.fromhex(
                "60406000604060006103e87326bc42b8191ccb142cb8cbc3490bd3bdce46559161c350f26000553d6001556020600060403e60405160025500"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
