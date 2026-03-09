"""
Ported from:
tests/static/state_tests/stRandom2/randomStatetest601Filler.json
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
    ["tests/static/state_tests/stRandom2/randomStatetest601Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_random_statetest601(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x4f3f701464972e74606d6ea82d4d3080599a0e79")
    sender = Address("0x2e3d0156d2b99a6eacba540c55f423c8f5a33143")
    contract = Address("0x287d3f26febb148710a503235ebf7ac1f1b75838")

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
        code=bytes.fromhex(
        "7f000000000000000000000000ffffffffffffffffffffffffffffffffffffffff7fffff"
        "fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe7f0000000000"
        "00000000000000945304eb96065b2a98b57a48a06ae28d285a71b57f0000000000000000"
        "0000000000000000000000000000000000000000000000007f0000000000000000000000"
        "00000000000000000000000000000000000000c350377f00000000000000000000000000"
        "0000000000000000000000000000000000c3507f00000000000000000000000100000000"
        "000000000000000000000000000000000b3a09785b1084418866100af0868a3455"
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
            "7f000000000000000000000000ffffffffffffffffffffffffffffffffffffffff7fffff"
            "fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe7f0000000000"
            "00000000000000945304eb96065b2a98b57a48a06ae28d285a71b57f0000000000000000"
            "0000000000000000000000000000000000000000000000007f0000000000000000000000"
            "00000000000000000000000000000000000000c350377f00000000000000000000000000"
            "0000000000000000000000000000000000c3507f00000000000000000000000100000000"
            "000000000000000000000000000000000b3a09785b1084418866100af0868a34"
        ),
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=2056709657,
    )

    post = {
        contract: Account(
            code=bytes.fromhex("7f000000000000000000000000ffffffffffffffffffffffffffffffffffffffff7ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe7f000000000000000000000000945304eb96065b2a98b57a48a06ae28d285a71b57f00000000000000000000000000000000000000000000000000000000000000007f000000000000000000000000000000000000000000000000000000000000c350377f000000000000000000000000000000000000000000000000000000000000c3507f00000000000000000000000100000000000000000000000000000000000000000b3a09785b1084418866100af0868a3455"),
        ),
        coinbase: Account(
            code=Op.JUMPI(pc=0x9, condition=Op.ISZERO(Op.SLOAD(key=Op.CALLDATALOAD(offset=0x0)))) + Op.STOP + Op.JUMPDEST + Op.SSTORE(key=Op.CALLDATALOAD(offset=0x0), value=Op.CALLDATALOAD(offset=0x20)),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
