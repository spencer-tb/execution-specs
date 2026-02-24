"""
recursive call

Ported from:
tests/static/state_tests/stCallCreateCallCodeTest/CallcodeLoseGasOOGFiller.json
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
    ["tests/static/state_tests/stCallCreateCallCodeTest/CallcodeLoseGasOOGFiller.json"],
)
@pytest.mark.valid_from("Cancun")
@pytest.mark.parametrize(
    "tx_gas_limit",
    [
        166262,
        156262,
        170000,
    ],
    ids=['case0', 'case1', 'case2'],
)
def test_callcode_lose_gas_oog(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
) -> None:
    """recursive call."""
    coinbase = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    sender = Address("0x8a0a19589531694250d570040a0c4b74576919b8")
    contract = Address("0x1000000000000000000000000000000000001000")
    callee = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[contract] = Account(
        balance=1024,
        nonce=0,
        code=(
        Op.PUSH1[0x1] + Op.PUSH1[0x0] + Op.SLOAD + Op.ADD + Op.PUSH1[0x0]
        + Op.SSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH20[0x1000000000000000000000000000000000001000]
        + Op.PUSH3[0x186a0] + Op.PUSH1[0x0] + Op.SLOAD + Op.MUL + Op.PUSH1[0x1]
        + Op.ADD + Op.CALLCODE + Op.PUSH1[0x1] + Op.SSTORE + Op.PUSH2[0x3e8]
        + Op.PUSH1[0x0] + Op.SLOAD + Op.MUL + Op.PUSH1[0x1] + Op.ADD + Op.PUSH1[0x2]
        + Op.SSTORE + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0xffffffffffffffffffffffffffffffff, nonce=0)
    pre[callee] = Account(balance=7000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x9e7645d0cfd9c3a04eb7a9db59a4eb7d359f2e75c9164a9d6b9a7d54e1b6a36f"
        ),
        to=contract,
        data=b"",
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=10,
    )

    post = {}

    state_test(env=env, pre=pre, post=post, tx=tx)
