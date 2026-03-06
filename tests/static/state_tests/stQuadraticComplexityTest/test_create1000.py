"""
Gas analysis showed this test's gas can go as low as 21053, and still yield the same traces, which implies the test is broken

Ported from:
tests/static/state_tests/stQuadraticComplexityTest/Create1000Filler.json

contract code:
    jumpdest
    push2 0x03e8
    push1 0x80
    mload
    lt
    iszero
    push1 0x23
    jumpi
    push2 0xc350
    push1 0x00
    push1 0x01
    create
    push1 0x00
    sstore
    push1 0x01
    push1 0x80
    mload
    add
    push1 0x80
    mstore
    ... (8 more instructions)
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
    ["tests/static/state_tests/stQuadraticComplexityTest/Create1000Filler.json"],
)
@pytest.mark.valid_from("Cancun")
@pytest.mark.valid_until("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit",
    [
        150000,
        250000000,
    ],
    ids=['case0', 'case1'],
)
@pytest.mark.pre_alloc_mutable
def test_create1000(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
) -> None:
    """Gas analysis showed this test's gas can go as low as 21053, and still yield the same traces, which implies the test is broken."""
    coinbase = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xbbbf5374fce5edbc8e2a8697c15331677e6ebf0b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=8600000000,
    )

    pre[sender] = Account(balance=0xffffffffffffffffffffffffffffffff, nonce=0)
    pre[contract] = Account(
        balance=0xfffffffffffff,
        nonce=0,
        code=(
        Op.JUMPDEST + Op.PUSH2[0x3e8] + Op.PUSH1[0x80] + Op.MLOAD + Op.LT
        + Op.ISZERO + Op.PUSH1[0x23] + Op.JUMPI + Op.PUSH2[0xc350] + Op.PUSH1[0x0]
        + Op.PUSH1[0x1] + Op.CREATE + Op.PUSH1[0x0] + Op.SSTORE + Op.PUSH1[0x1]
        + Op.PUSH1[0x80] + Op.MLOAD + Op.ADD + Op.PUSH1[0x80] + Op.MSTORE
        + Op.PUSH1[0x0] + Op.JUMP + Op.JUMPDEST + Op.PUSH1[0x80] + Op.MLOAD
        + Op.PUSH1[0x1] + Op.SSTORE + Op.STOP
    ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=b"",
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=10,
    )

    post = {
        Address("0x010d8b0816e30ff51ba07678c64b272cdeddb807"): Account.NONEXISTENT,
        Address("0x014830fe159f418212e5c39b4b2e2ddc7b295395"): Account.NONEXISTENT,
        Address("0x0c6a8f1bf692cb9e4f9d9c5a2785d58edfd42457"): Account.NONEXISTENT,
        Address("0x198d23bedd1a9fdbd4adb5760930f6877f5d142f"): Account.NONEXISTENT,
        Address("0x266c09580d28c1c576e5c6b9adc926be1fecffb1"): Account.NONEXISTENT,
        contract: Account(storage={0: 0, 1: 0}, nonce=0),
        Address("0xe5dc2e5b40069a91f688e56ea8d12149c5480b42"): Account.NONEXISTENT,
        Address("0xfdbd2625737df76e194c99994be160c5f8248dad"): Account.NONEXISTENT,
        Address("0xfff043abcbf2b0972c1dca19b2ba3cd682f10e90"): Account.NONEXISTENT,
    }

    state_test(env=env, pre=pre, post=post, tx=tx)


@pytest.mark.ported_from(
    ["tests/static/state_tests/stQuadraticComplexityTest/Create1000ByzantiumFiller.json"],
)
@pytest.mark.valid_from("Cancun")
@pytest.mark.valid_until("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit",
    [
        150000,
        250000000,
    ],
    ids=['case0', 'case1'],
)
@pytest.mark.pre_alloc_mutable
def test_create1000_byzantium(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
) -> None:
    """Gas analysis showed this test's gas can go as low as 21053, and still yield the same traces, which implies the test is broken."""
    coinbase = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xbbbf5374fce5edbc8e2a8697c15331677e6ebf0b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=8600000000,
    )

    pre[sender] = Account(balance=0xffffffffffffffffffffffffffffffff, nonce=0)
    pre[contract] = Account(
        balance=0xfffffffffffff,
        nonce=0,
        code=(
        Op.JUMPDEST + Op.PUSH2[0x3e8] + Op.PUSH1[0x80] + Op.MLOAD + Op.LT
        + Op.ISZERO + Op.PUSH1[0x23] + Op.JUMPI + Op.PUSH2[0xc350] + Op.PUSH1[0x0]
        + Op.PUSH1[0x1] + Op.CREATE + Op.PUSH1[0x0] + Op.SSTORE + Op.PUSH1[0x1]
        + Op.PUSH1[0x80] + Op.MLOAD + Op.ADD + Op.PUSH1[0x80] + Op.MSTORE
        + Op.PUSH1[0x0] + Op.JUMP + Op.JUMPDEST + Op.PUSH1[0x80] + Op.MLOAD
        + Op.PUSH1[0x1] + Op.SSTORE + Op.STOP
    ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
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
