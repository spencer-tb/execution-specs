"""
Consensus issue test produced by fuzz testing team 00000005-storagefuzz-1

Ported from:
tests/static/state_tests/stRandom2/randomStatetest648Filler.json
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
    ["tests/static/state_tests/stRandom2/randomStatetest648Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_random_statetest648(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Consensus issue test produced by fuzz testing team 00000005-storagefuzz-1."""
    coinbase = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    sender = Address("0x8c78e3e2ffedb0eb21426734400554a5185299de")
    contract = Address("0xca5c69fa03b9dff4d059971ac17edac7ef758725")
    callee = Address("0xa828265d4b2db08e65a1c68d2878f15368b5ae75")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10944489199640098,
    )

    pre[sender] = Account(balance=0xffffffff, nonce=0)
    pre[callee] = Account(balance=0, nonce=0, code=Op.POP(0x0))
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.POP(Op.DELEGATECALL(gas=Op.GAS, address=0xf1, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.PUSH1[0x0] + Op.POP(0x0) + Op.SELFDESTRUCT(address=0xf5) + Op.REVERT
    ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xff348633b687ec0f553647f4ddeed7590e90c7ea65b87c5bd399f4c869b9c9fc"
        ),
        to=contract,
        data=bytes.fromhex(
            "384c289327fda733f319011b605929b98b6cc52e4915c942369264c71a3ca70ebce56fef"
            "7e41103f1acc71e91f299bf6c5730b265d6f9d475936735ea60c58b9bb125a7817817178"
            "4759606d696e98f8522b52fe213edee397b3df6ca9f0c6"
        ),
        gas_limit=343469,
        gas_price=10,
        nonce=0,
        value=14361094,
    )

    post = {
        callee: Account(code=Op.POP(0x0)),
        contract: Account(
            code=Op.POP(Op.DELEGATECALL(gas=Op.GAS, address=0xf1, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.PUSH1[0x0] + Op.POP(0x0) + Op.SELFDESTRUCT(address=0xf5) + Op.REVERT,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
