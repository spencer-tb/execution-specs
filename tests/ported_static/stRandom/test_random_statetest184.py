"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRandom/randomStatetest184Filler.json
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
    ["tests/static/state_tests/stRandom/randomStatetest184Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_random_statetest184(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x6d6e40885310545835a5b582dbc23ef026404bda")
    sender = Address("0xd48af89ccc2cd5a8a6e6f6d3110a36c85f95185e")
    contract = Address("0x898207f2d9b9fb11cec9647a70e9390711732daa")
    callee = Address("0xf377657e450772b703a269e12bb487ff421a5c6d")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=10000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=69449279085,
    )

    pre[contract] = Account(
        balance=0x70A217C02C8F2D4,
        nonce=117,
        code=bytes.fromhex(
            "6f823a02877cef7c1afb60663009def564608c557bad2ae05769b991313726edbfa0881d"  # noqa: E501
            "9cc955b0f5154751da315696ea7ce130184b64f2507582c502d450349ff24fb8aeb2a461"  # noqa: E501
            "46687b666bd7bd0364946cb720c76d483f5afea0049251fd9793c4b0376afbb4ebcdc42f"  # noqa: E501
            "dd42edcd4b619cec787638009cea26a1abe570e3186ab790b7dc7db36e4cda2570b0847a"  # noqa: E501
            "df6e39579c7c43a4ac976cd507d493cdfaebe09936078e31c71c4665d34a4b816b8004"  # noqa: E501
        ),
    )
    pre[sender] = Account(balance=0x10C1142F2B8E8EB058, nonce=0)
    pre[callee] = Account(balance=0x9740421FF0FF3AE3, nonce=29)

    tx = Transaction(
        secret_key=Hash(
            "0x382acd382cc7a37bb6a57c4a171f216ef77ef04ebd5e6c0744ee5c90b0d962ef"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex("64dd3e4e84676723342c1dfaf9af4ef3"),
        gas_limit=100000,
        gas_price=28,
        nonce=0,
        value=1830670372,
    )

    post = {
        contract: Account(
            storage={140: 0x823A02877CEF7C1AFB60663009DEF564},
            code=bytes.fromhex(
                "6f823a02877cef7c1afb60663009def564608c557bad2ae05769b991313726edbfa0881d9cc955b0f5154751da315696ea7ce130184b64f2507582c502d450349ff24fb8aeb2a46146687b666bd7bd0364946cb720c76d483f5afea0049251fd9793c4b0376afbb4ebcdc42fdd42edcd4b619cec787638009cea26a1abe570e3186ab790b7dc7db36e4cda2570b0847adf6e39579c7c43a4ac976cd507d493cdfaebe09936078e31c71c4665d34a4b816b8004"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
