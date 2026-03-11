"""
Malicious bytecode found by fuzztest tool: returndatacopy(0,-1).

Ported from:
tests/static/state_tests/stRandom2/randomStatetest647Filler.json
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
    ["tests/static/state_tests/stRandom2/randomStatetest647Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_random_statetest647(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Malicious bytecode found by fuzztest tool: returndatacopy(0,-1)."""
    coinbase = Address("0xd94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    sender = Address("0xcfff6235759a3209f2cb8e3e2dd6ea4c2b96e325")
    contract = Address("0x782b7c65205e1c08192df7357e2fe778c81256a9")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=18857228215205537,
    )

    # Source: raw bytecode
    pre[contract] = Account(
        balance=0,
        nonce=7,
        code=(
            Op.RETURNDATACOPY(
                dest_offset=0x0, offset=Op.SUB(0x0, 0x1), size=0x1
            )
            + Op.STOP
        ),
    )
    pre[sender] = Account(balance=0x174876E800, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x5b7b8efb6d003cd481e408d8759a25adc79955092f1a380d8f8b57346c1d1342"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=5786929,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            code=(
                Op.RETURNDATACOPY(
                    dest_offset=0x0,
                    offset=Op.SUB(0x0, 0x1),
                    size=0x1,
                )
                + Op.STOP
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
