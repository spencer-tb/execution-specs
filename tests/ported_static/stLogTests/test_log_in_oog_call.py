"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stLogTests/logInOOG_CallFiller.json
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
    ["tests/static/state_tests/stLogTests/logInOOG_CallFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_log_in_oog_call(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0x825dcc9fbf5cff44e688bae15b79e8e11951be2a")
    callee = Address("0x69b6134b97e638b919a7089df82af74961e71ff8")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    pre[callee] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex("60206000a067ffffffffffffffff5100"),
    )
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "600060006000600060177369b6134b97e638b919a7089df82af74961e71ff8620186a0f1"  # noqa: E501
            "60005500"
        ),
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xe04d1ac7ddda0c98397d56a0b501e960d4cd325a39286919ac23c1a07009a869"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=210000,
        gas_price=10,
        nonce=0,
        value=100000,
    )

    post = {
        callee: Account(
            code=bytes.fromhex("60206000a067ffffffffffffffff5100"),
        ),
        contract: Account(
            code=bytes.fromhex(
                "600060006000600060177369b6134b97e638b919a7089df82af74961e71ff8620186a0f160005500"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
