"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stCreate2/CREATE2_HighNonceFiller.yml
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
    ["tests/static/state_tests/stCreate2/CREATE2_HighNonceFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_create2_high_nonce(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=89128960,
    )

    pre[sender] = Account(balance=0x3B9ACA00, nonce=0)
    pre[contract] = Account(
        balance=0,
        nonce=18446744073709551615,
        code=(
            Op.SHL(0xD8, 0x60016000F3)
            + Op.PUSH1[0x0]
            + Op.SWAP1
            + Op.DUP2
            + Op.MSTORE
            + Op.PUSH1[0x5]
            + Op.DUP2
            + Op.DUP1
            + Op.SSTORE(key=0x0, value=Op.CREATE2)
            + Op.SSTORE(key=Op.DUP1, value=0x1)
            + Op.STOP
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=16777216,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            storage={1: 1},
            code=(
                Op.SHL(0xD8, 0x60016000F3)
                + Op.PUSH1[0x0]
                + Op.SWAP1
                + Op.DUP2
                + Op.MSTORE
                + Op.PUSH1[0x5]
                + Op.DUP2
                + Op.DUP1
                + Op.SSTORE(key=0x0, value=Op.CREATE2)
                + Op.SSTORE(key=Op.DUP1, value=0x1)
                + Op.STOP
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
