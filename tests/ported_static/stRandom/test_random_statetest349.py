"""
Ported from:
tests/static/state_tests/stRandom/randomStatetest349Filler.json
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
    ["tests/static/state_tests/stRandom/randomStatetest349Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_random_statetest349(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x4f3f701464972e74606d6ea82d4d3080599a0e79")
    sender = Address("0x2e3d0156d2b99a6eacba540c55f423c8f5a33143")
    contract = Address("0x7ae95f23f4e7f70699a603a5b4cac5cdc841f96d")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[sender] = Account(balance=0xde0b6b3a7640000, nonce=0)
    pre[coinbase] = Account(
        balance=46,
        nonce=0,
        code=(
        Op.JUMPI(pc=0x9, condition=Op.ISZERO(Op.SLOAD(key=Op.CALLDATALOAD(offset=0x0))))
        + Op.STOP + Op.JUMPDEST
        + Op.SSTORE(key=Op.CALLDATALOAD(offset=0x0), value=Op.CALLDATALOAD(offset=0x20))
    ),
    )
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH32[0xffffffffffffffffffffffffffffffffffffffff]
        + Op.PUSH32[0xffffffffffffffffffffffffffffffffffffffff] + Op.PUSH32[0xc350]
        + Op.PUSH32[0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe]
        + Op.SSTORE(key=Op.TIMESTAMP, value=Op.DIV(0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe, Op.PUSH32[0xc350]))
        + Op.MLOAD(offset=0x0) + Op.SSTORE
    ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xb1f4cbc3a50042184425a6f9e996d0910f7ba879457ce5dac5c71e498ad3c005"
        ),
        to=contract,
        data=bytes.fromhex(
            "7f000000000000000000000000ffffffffffffffffffffffffffffffffffffffff7f0000"
            "00000000000000000000ffffffffffffffffffffffffffffffffffffffff7f0000000000"
            "00000000000000000000000000000000000000000000000000c3507fffffffffffffffff"
            "fffffffffffffffffffffffffffffffffffffffffffffffe7f0000000000000000000000"
            "00000000000000000000000000000000000000c3507fffffffffffffffffffffffffffff"
            "fffffffffffffffffffffffffffffffffffe0442"
        ),
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=201035010,
    )

    post = {
        coinbase: Account(
            code=Op.JUMPI(pc=0x9, condition=Op.ISZERO(Op.SLOAD(key=Op.CALLDATALOAD(offset=0x0)))) + Op.STOP + Op.JUMPDEST + Op.SSTORE(key=Op.CALLDATALOAD(offset=0x0), value=Op.CALLDATALOAD(offset=0x20)),
        ),
        contract: Account(
            storage={0: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe, 1000: 0x14f8b588e368f08461f9f01b866e43aa79bbadc0980b242070b8cfbfc6540},
            code=Op.PUSH32[0xffffffffffffffffffffffffffffffffffffffff] + Op.PUSH32[0xffffffffffffffffffffffffffffffffffffffff] + Op.PUSH32[0xc350] + Op.PUSH32[0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe] + Op.SSTORE(key=Op.TIMESTAMP, value=Op.DIV(0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe, Op.PUSH32[0xc350])) + Op.MLOAD(offset=0x0) + Op.SSTORE,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
