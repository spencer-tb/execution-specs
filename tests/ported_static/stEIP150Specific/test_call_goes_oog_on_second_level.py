"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stEIP150Specific/CallGoesOOGOnSecondLevelFiller.json
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
        "tests/static/state_tests/stEIP150Specific/CallGoesOOGOnSecondLevelFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_call_goes_oog_on_second_level(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xfaa10b404ab607779993c016cd5da73ae1f29d7e")
    contract = Address("0x3c6dca5471c6305d0642c6210d39d4613b5ea30b")
    callee = Address("0x066f77b181e0e662e17d427c7320267adf2fd624")
    callee_1 = Address("0xccc0159bd2ef7118b5e7b8d958e72237f02493fe")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "5a6008556000600060006000600073ccc0159bd2ef7118b5e7b8d958e72237f02493fe62"  # noqa: E501
            "0493e0f16009556001600c5500"
        ),
    )
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "5a6008556000600060006000600073066f77b181e0e662e17d427c7320267adf2fd62462"  # noqa: E501
            "0927c0f160095500"
        ),
    )
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("5a600855622fffff600020505a6009555a600a5500"),
    )
    pre[sender] = Account(balance=0xE8D4A51000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x4f31b3206fbf0e0e598b9b1a7d8ac86302a0ff1d8930738f1bebae9b67173e52"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=2200000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        callee: Account(
            storage={8: 0x927BE, 12: 1},
            code=bytes.fromhex(
                "5a6008556000600060006000600073ccc0159bd2ef7118b5e7b8d958e72237f02493fe620493e0f16009556001600c5500"  # noqa: E501
            ),
        ),
        contract: Account(
            storage={8: 0x213FB6, 9: 1},
            code=bytes.fromhex(
                "5a6008556000600060006000600073066f77b181e0e662e17d427c7320267adf2fd624620927c0f160095500"  # noqa: E501
            ),
        ),
        callee_1: Account(
            code=bytes.fromhex("5a600855622fffff600020505a6009555a600a5500"),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
