"""
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
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


@pytest.mark.ported_from(
    ["tests/static/state_tests/stRandom/randomStatetest184Filler.json"],
)
@pytest.mark.valid_from("Cancun")
def test_random_statetest184(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x6d6e40885310545835a5b582dbc23ef026404bda")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x1000000000000000000000000000000000001000")
    callee = Address("0x8a0a19589531694250d570040a0c4b74576919b8")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=10000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=69449279085,
    )

    pre[contract] = Account(
        balance=0x70a217c02c8f2d4,
        nonce=117,
        code=(
        Op.PUSH16[0x823a02877cef7c1afb60663009def564] + Op.PUSH1[0x8c] + Op.SSTORE
        + Op.PUSH28[0xad2ae05769b991313726edbfa0881d9cc955b0f5154751da315696ea]
        + Op.PUSH29[0xe130184b64f2507582c502d450349ff24fb8aeb2a46146687b666bd7bd]
        + Op.SUB + Op.PUSH5[0x946cb720c7] + Op.PUSH14[0x483f5afea0049251fd9793c4b037]
        + Op.PUSH11[0xfbb4ebcdc42fdd42edcd4b] + Op.PUSH2[0x9cec]
        + Op.PUSH25[0x7638009cea26a1abe570e3186ab790b7dc7db36e4cda2570b0] + Op.DUP5
        + Op.PUSH27[0xdf6e39579c7c43a4ac976cd507d493cdfaebe09936078e31c71c46]
        + Op.PUSH6[0xd34a4b816b80] + Op.DIV
    ),
    )
    pre[callee] = Account(balance=0x9740421ff0ff3ae3, nonce=29)
    pre[sender] = Account(balance=0x10c1142f2b8e8eb058, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=bytes.fromhex("64dd3e4e84676723342c1dfaf9af4ef3"),
        gas_limit=100000,
        gas_price=28,
        nonce=0,
        value=1830670372,
    )

    post = {}

    state_test(env=env, pre=pre, post=post, tx=tx)
