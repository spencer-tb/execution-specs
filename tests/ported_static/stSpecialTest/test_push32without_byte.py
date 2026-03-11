"""
push expect 32 bytes. but we have only 10 byte.

Ported from:
tests/static/state_tests/stSpecialTest/push32withoutByteFiller.json
"""

import pytest
from execution_testing import (
    Account,
    Address,
    Alloc,
    EOA,
    Environment,
    Hash,
    StateTestFiller,
    Transaction,
)

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


@pytest.mark.ported_from(
    ["tests/static/state_tests/stSpecialTest/push32withoutByteFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_push32without_byte(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Push expect 32 bytes. but we have only 10 byte."""
    coinbase = Address("0x68795c4aa09d6f4ed3e5deddf8c2ad3049a601da")
    sender = EOA(
        key=0x043F683FF58B5310699989DD19A4E1439E5333E2E3445374F7BC1446BAEDDD80
    )
    contract = Address("0xc46ea1c1ad6c8ee63711d0377ef63e51c05d38a0")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=3141592,
    )

    pre[sender] = Account(balance=0x8AC7230489E80000, nonce=1)
    # Source: raw bytecode
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("7f11223344556677889910"),
    )

    tx = Transaction(
        sender=sender,
        to=contract,
        data=b"",
        gas_limit=500000,
        gas_price=10,
        nonce=1,
        value=0,
    )

    post = {
        contract: Account(code=bytes.fromhex("7f11223344556677889910")),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
