"""
Ori Pomerantz qbzzt1@gmail.com

Ported from:
tests/static/state_tests/stEIP2930/coinbaseT01Filler.yml
"""

import pytest
from execution_testing import (
    AccessList,
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
    ["tests/static/state_tests/stEIP2930/coinbaseT01Filler.yml"],
)
@pytest.mark.valid_from("Cancun")
@pytest.mark.parametrize(
    "tx_access_list",
    [
        None,
        [AccessList(address=Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"), storage_keys=[])],
        [AccessList(address=Address("0x000000000000000000000000000000000000ba5a"), storage_keys=[])],
    ],
    ids=['case0', 'case1', 'case2'],
)
def test_coinbase_t01(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_access_list,
) -> None:
    """Ori Pomerantz qbzzt1@gmail.com."""
    coinbase = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    sender = Address("0x8a0a19589531694250d570040a0c4b74576919b8")
    contract = Address("0x1000000000000000000000000000000000001000")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=100,
        gas_limit=71794957647893862,
    )

    pre[contract] = Account(
        balance=0xde0b6b3a7640000,
        nonce=1,
        code=(
        Op.GAS + Op.PUSH1[0x0] + Op.MSTORE + Op.PUSH1[0x0] + Op.DUP1 + Op.DUP1
        + Op.DUP1 + Op.PUSH3[0xf4240]
        + Op.PUSH20[0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b] + Op.GAS + Op.CALL
        + Op.POP + Op.GAS + Op.PUSH1[0x20] + Op.MSTORE + Op.PUSH1[0x21]
        + Op.PUSH1[0x20] + Op.MLOAD + Op.PUSH1[0x0] + Op.MLOAD + Op.SUB + Op.SUB
        + Op.PUSH1[0x0] + Op.SSTORE + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0xde0b6b3a7640000, nonce=1)
    pre[coinbase] = Account(balance=0, nonce=1)

    tx = Transaction(
        secret_key=Hash(
            "0x9e7645d0cfd9c3a04eb7a9db59a4eb7d359f2e75c9164a9d6b9a7d54e1b6a36f"
        ),
        to=contract,
        data=bytes.fromhex("693c61390000000000000000000000000000000000000000000000000000000000000000"),
        gas_limit=16777216,
        gas_price=1000,
        nonce=1,
        value=0,
        access_list=tx_access_list,
    )

    post = {}

    state_test(env=env, pre=pre, post=post, tx=tx)
