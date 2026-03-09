"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stEIP150Specific
ExecuteCallThatAskForeGasThenTrabsactionHasFiller.json
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
        "tests/static/state_tests/stEIP150Specific/ExecuteCallThatAskForeGasThenTrabsactionHasFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_execute_call_that_ask_fore_gas_then_trabsaction_has(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x7f3f285918d9b5e764174551e10b7539b97bbb27")
    contract = Address("0x1819cf5bff62f0d379f146b85baaf9bd18239832")
    callee = Address("0xbfdd294028701b119d416c68eff7dd9f7effd249")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "6000600060006000600073bfdd294028701b119d416c68eff7dd9f7effd249620927c0f1"  # noqa: E501
            "60015500"
        ),
    )
    pre[sender] = Account(balance=0x5F5E100, nonce=0)
    pre[callee] = Account(
        balance=0x186A0,
        nonce=0,
        code=bytes.fromhex("600c60015500"),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xa2333eef5630066b928dea5fd85a239f511b5b067d1441ee7ac290d0122b917b"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            storage={1: 1},
            code=bytes.fromhex(
                "6000600060006000600073bfdd294028701b119d416c68eff7dd9f7effd249620927c0f160015500"  # noqa: E501
            ),
        ),
        callee: Account(storage={1: 12}, code=bytes.fromhex("600c60015500")),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
