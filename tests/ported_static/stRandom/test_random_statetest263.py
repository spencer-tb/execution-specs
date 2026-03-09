"""
Ported from:
tests/static/state_tests/stRandom/randomStatetest263Filler.json
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
    ["tests/static/state_tests/stRandom/randomStatetest263Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.valid_until("Prague")
@pytest.mark.pre_alloc_mutable
def test_random_statetest263(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x945304eb96065b2a98b57a48a06ae28d285a71b5")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x095e7baea6a6c7c4c2dfeb977efac326af552d87")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH32[0x945304eb96065b2a98b57a48a06ae28d285a71b5] + Op.DUP1
        + Op.PUSH32[0xc350]
        + Op.PUSH32[0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe]
        + Op.PUSH32[0x10000000000000000000000000000000000000000]
        + Op.SSTORE(key=Op.MLOAD(offset=0x556000), value=Op.XOR(Op.DIV(0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe, Op.PUSH32[0xc350]), Op.PUSH32[0x945304eb96065b2a98b57a48a06ae28d285a71b5]))
    ),
    )
    pre[coinbase] = Account(
        balance=46,
        nonce=0,
        code=(
        Op.JUMPI(pc=0x9, condition=Op.ISZERO(Op.SLOAD(key=Op.CALLDATALOAD(offset=0x0))))
        + Op.STOP + Op.JUMPDEST
        + Op.SSTORE(key=Op.CALLDATALOAD(offset=0x0), value=Op.CALLDATALOAD(offset=0x20))
    ),
    )
    pre[sender] = Account(balance=0xde0b6b3a7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=bytes.fromhex(
            "7f000000000000000000000000945304eb96065b2a98b57a48a06ae28d285a71b5807f00"
            "0000000000000000000000000000000000000000000000000000000000c3507fffffffff"
            "fffffffffffffffffffffffffffffffffffffffffffffffffffffffe7f00000000000000"
            "000000000100000000000000000000000000000000000000007f00000000000000000000"
            "0000945304eb96065b2a98b57a48a06ae28d285a71b57f00000000000000000000000000"
            "0000000000000000000000000000000000c3507fffffffffffffffffffffffffffffffff"
            "fffffffffffffffffffffffffffffffe041862"
        ),
        gas_limit=2038963641,
        gas_price=10,
        nonce=0,
        value=767067244,
    )

    post = {
        contract: Account(
            storage={0: 0x14f8b588e368f08461f9f95eb620faca1c09044bcfafae26de901d3a614f5},
            code=Op.PUSH32[0x945304eb96065b2a98b57a48a06ae28d285a71b5] + Op.DUP1 + Op.PUSH32[0xc350] + Op.PUSH32[0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe] + Op.PUSH32[0x10000000000000000000000000000000000000000] + Op.SSTORE(key=Op.MLOAD(offset=0x556000), value=Op.XOR(Op.DIV(0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe, Op.PUSH32[0xc350]), Op.PUSH32[0x945304eb96065b2a98b57a48a06ae28d285a71b5])),
        ),
        coinbase: Account(
            code=Op.JUMPI(pc=0x9, condition=Op.ISZERO(Op.SLOAD(key=Op.CALLDATALOAD(offset=0x0)))) + Op.STOP + Op.JUMPDEST + Op.SSTORE(key=Op.CALLDATALOAD(offset=0x0), value=Op.CALLDATALOAD(offset=0x20)),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
