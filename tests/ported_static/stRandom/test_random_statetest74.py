"""
Ported from:
tests/static/state_tests/stRandom/randomStatetest74Filler.json
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
    ["tests/static/state_tests/stRandom/randomStatetest74Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_random_statetest74(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x4f3f701464972e74606d6ea82d4d3080599a0e79")
    sender = Address("0x2e3d0156d2b99a6eacba540c55f423c8f5a33143")
    contract = Address("0x1388416097405b5998a7b07d85a1aaadf337e5da")

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
        Op.TIMESTAMP
        + Op.PUSH32[0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe]
        + Op.PUSH32[0x1] + Op.PUSH32[0xffffffffffffffffffffffffffffffffffffffff]
        + Op.GASPRICE + Op.PUSH32[0x4f3f701464972e74606d6ea82d4d3080599a0e79]
        + Op.PUSH32[0x0]
        + Op.SSTORE(key=Op.MLOAD(offset=0x0), value=0x141097788a7b5a72139c07076f184255)
    ),
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

    tx = Transaction(
        secret_key=Hash(
            "0xb1f4cbc3a50042184425a6f9e996d0910f7ba879457ce5dac5c71e498ad3c005"
        ),
        to=contract,
        data=bytes.fromhex(
            "427ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe7f00"
            "000000000000000000000000000000000000000000000000000000000000017f00000000"
            "0000000000000000ffffffffffffffffffffffffffffffffffffffff3a7f000000000000"
            "0000000000004f3f701464972e74606d6ea82d4d3080599a0e797f000000000000000000"
            "00000000000000000000000000000000000000000000006f141097788a7b5a72139c0707"
            "6f1842"
        ),
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=1223108496,
    )

    post = {
        contract: Account(
            storage={0: 0x141097788a7b5a72139c07076f184255},
            code=Op.TIMESTAMP + Op.PUSH32[0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe] + Op.PUSH32[0x1] + Op.PUSH32[0xffffffffffffffffffffffffffffffffffffffff] + Op.GASPRICE + Op.PUSH32[0x4f3f701464972e74606d6ea82d4d3080599a0e79] + Op.PUSH32[0x0] + Op.SSTORE(key=Op.MLOAD(offset=0x0), value=0x141097788a7b5a72139c07076f184255),
        ),
        coinbase: Account(
            code=Op.JUMPI(pc=0x9, condition=Op.ISZERO(Op.SLOAD(key=Op.CALLDATALOAD(offset=0x0)))) + Op.STOP + Op.JUMPDEST + Op.SSTORE(key=Op.CALLDATALOAD(offset=0x0), value=Op.CALLDATALOAD(offset=0x20)),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
