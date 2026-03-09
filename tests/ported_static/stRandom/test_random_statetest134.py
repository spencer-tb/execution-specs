"""
Ported from:
tests/static/state_tests/stRandom/randomStatetest134Filler.json
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
    ["tests/static/state_tests/stRandom/randomStatetest134Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_random_statetest134(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x4f3f701464972e74606d6ea82d4d3080599a0e79")
    sender = Address("0x2e3d0156d2b99a6eacba540c55f423c8f5a33143")
    contract = Address("0x955495cf3dc6d8b98b51e7c3f09c27a30c0e87f0")

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
        Op.COINBASE + Op.PUSH32[0x0]
        + Op.SSTORE(key=Op.PUSH32[0xffffffffffffffffffffffffffffffffffffffff], value=Op.PUSH32[0xffffffffffffffffffffffffffffffffffffffff])
        + Op.PUSH32[0x4f3f701464972e74606d6ea82d4d3080599a0e79]
        + Op.SSTORE(key=Op.PUSH32[0xffffffffffffffffffffffffffffffffffffffff], value=Op.PUSH32[0x0])
        + Op.DUP4
        + Op.SSTORE(key=Op.MLOAD(offset=0x0), value=0x636c9c395a07320145334055)
    ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xb1f4cbc3a50042184425a6f9e996d0910f7ba879457ce5dac5c71e498ad3c005"
        ),
        to=contract,
        data=bytes.fromhex(
            "417f00000000000000000000000000000000000000000000000000000000000000007f00"
            "0000000000000000000000ffffffffffffffffffffffffffffffffffffffff7f00000000"
            "0000000000000000ffffffffffffffffffffffffffffffffffffffff557f000000000000"
            "0000000000004f3f701464972e74606d6ea82d4d3080599a0e797f000000000000000000"
            "00000000000000000000000000000000000000000000007f000000000000000000000000"
            "ffffffffffffffffffffffffffffffffffffffff55836b636c9c395a073201453340"
        ),
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=65268053,
    )

    post = {
        coinbase: Account(
            code=Op.JUMPI(pc=0x9, condition=Op.ISZERO(Op.SLOAD(key=Op.CALLDATALOAD(offset=0x0)))) + Op.STOP + Op.JUMPDEST + Op.SSTORE(key=Op.CALLDATALOAD(offset=0x0), value=Op.CALLDATALOAD(offset=0x20)),
        ),
        contract: Account(
            code=Op.COINBASE + Op.PUSH32[0x0] + Op.SSTORE(key=Op.PUSH32[0xffffffffffffffffffffffffffffffffffffffff], value=Op.PUSH32[0xffffffffffffffffffffffffffffffffffffffff]) + Op.PUSH32[0x4f3f701464972e74606d6ea82d4d3080599a0e79] + Op.SSTORE(key=Op.PUSH32[0xffffffffffffffffffffffffffffffffffffffff], value=Op.PUSH32[0x0]) + Op.DUP4 + Op.SSTORE(key=Op.MLOAD(offset=0x0), value=0x636c9c395a07320145334055),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
