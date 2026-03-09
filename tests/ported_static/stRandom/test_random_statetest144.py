"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRandom/randomStatetest144Filler.json
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
    ["tests/static/state_tests/stRandom/randomStatetest144Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_random_statetest144(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0xb0085a57673c8f7d78fb870418f622e42fd686e4")
    sender = Address("0x094419ff21b7d5a0f465fd0fae324dc95c5a97e9")
    contract = Address("0xea1cd1b117b10ac33fd7bbf18889624625ede7d4")
    callee = Address("0x19bcdbcd094c63df253c825b4b8e6dffc45c21a4")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1545160903,
    )

    pre[sender] = Account(balance=0x71E90493E6EB4C59, nonce=0)
    pre[callee] = Account(balance=0x2401AC5958344E85, nonce=53)
    pre[contract] = Account(
        balance=0x3255F99DE856501,
        nonce=89,
        code=bytes.fromhex(
            "621da82575e942e4fd977abdb407069cf700116e02b4f9b25d866b6d13163fff2b8ef03c"  # noqa: E501
            "f8ab5d662afb7bb5c9e68462741090bc0976c9705b40411efe39e80c20b572c5e3d75f78"  # noqa: E501
            "8f9be2f0981672b8de37f9e2d1515046cb77cc3ee74646fb096eadce98908499b6fd5472"  # noqa: E501
            "5f3c6a725968761ba50494d1ecaf1e787db9a052952427c4f271c28d3e25728b2b76439a"  # noqa: E501
            "3166cd0ed37f30ec2421ed38ebd3b00b89ba9208391dc274e4eefa69161a37dfff711175"  # noqa: E501
            "6dd7971065f05aa9de4867609e7d847a290d0eeb08cde2ff294ae11dd16f8a3e32494d94"  # noqa: E501
            "3fa0622cc04cd7476b6d2a1008e4ad1e2c33e2928e707c797f2a1a586bbf78658189bf58"  # noqa: E501
            "172ff77130be2ffc9bbf7f171939be260b30eb65b46a6cf107be1c9ed5c92c99d69fe055"  # noqa: E501
            "9389600e6013601c60096016601260016001600c6017016d200351654b9773409608aaa7"  # noqa: E501
            "db1f67b518d025727bdc6e0463b2bc334b658536d84dadc47a2288da62c36b9a35bf8934"  # noqa: E501
            "e3781a4c44e91637ce5c6b2f916d76706529d728b6f5ee076013601e601960086005601c"  # noqa: E501
            "6013601d96423568ce21a850c04a77ceb9"
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0x102da5c19454baf64e4f417e04ac2551245f3f217ffe9197f0c1d80fc2b16cff"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex(
            "166e31b12700cdefa7a0591398d415023175d1e5a1eca036986533972cab6625e976572e"  # noqa: E501
            "e91c150c"
        ),
        gas_limit=100000,
        gas_price=232,
        nonce=0,
        value=1022194925,
    )

    post = {
        contract: Account(
            code=bytes.fromhex(
                "621da82575e942e4fd977abdb407069cf700116e02b4f9b25d866b6d13163fff2b8ef03cf8ab5d662afb7bb5c9e68462741090bc0976c9705b40411efe39e80c20b572c5e3d75f788f9be2f0981672b8de37f9e2d1515046cb77cc3ee74646fb096eadce98908499b6fd54725f3c6a725968761ba50494d1ecaf1e787db9a052952427c4f271c28d3e25728b2b76439a3166cd0ed37f30ec2421ed38ebd3b00b89ba9208391dc274e4eefa69161a37dfff7111756dd7971065f05aa9de4867609e7d847a290d0eeb08cde2ff294ae11dd16f8a3e32494d943fa0622cc04cd7476b6d2a1008e4ad1e2c33e2928e707c797f2a1a586bbf78658189bf58172ff77130be2ffc9bbf7f171939be260b30eb65b46a6cf107be1c9ed5c92c99d69fe0559389600e6013601c60096016601260016001600c6017016d200351654b9773409608aaa7db1f67b518d025727bdc6e0463b2bc334b658536d84dadc47a2288da62c36b9a35bf8934e3781a4c44e91637ce5c6b2f916d76706529d728b6f5ee076013601e601960086005601c6013601d96423568ce21a850c04a77ceb9"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
