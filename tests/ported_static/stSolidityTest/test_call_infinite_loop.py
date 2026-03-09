"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stSolidityTest/CallInfiniteLoopFiller.json
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
    ["tests/static/state_tests/stSolidityTest/CallInfiniteLoopFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_call_infinite_loop(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0xeb201d2887816e041f6e807e804f64f3a7a226fe")
    sender = Address("0x01a87dcc756f6a6bd9e586598a5c1a44a1c6d945")
    contract = Address("0xf9b9ccb6160ce3574df5d096ca9fd12ba81d97ee")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000,
    )

    pre[sender] = Account(balance=0x1DCD6500, nonce=0)
    pre[coinbase] = Account(balance=0, nonce=1)
    pre[contract] = Account(
        balance=0x186A0,
        nonce=0,
        code=bytes.fromhex(
            "60003560e060020a90048063296df0df1460295780634893d88a146035578063981a3165"  # noqa: E501
            "14604157005b602f604d565b60006000f35b603b6062565b60006000f35b6047605a565b"  # noqa: E501
            "60006000f35b5b600115605857604e565b565b60606062565b565b6068605a565b56"  # noqa: E501
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0x96c07046493ec8728482079ab999d2994420d9cf4d3491dfd06871b106d9d87b"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex("296df0df"),
        gas_limit=300000,
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = {
        contract: Account(
            code=bytes.fromhex(
                "60003560e060020a90048063296df0df1460295780634893d88a146035578063981a316514604157005b602f604d565b60006000f35b603b6062565b60006000f35b6047605a565b60006000f35b5b600115605857604e565b565b60606062565b565b6068605a565b56"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
