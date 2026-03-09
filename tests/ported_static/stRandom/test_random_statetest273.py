"""
Ported from:
tests/static/state_tests/stRandom/randomStatetest273Filler.json
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
    ["tests/static/state_tests/stRandom/randomStatetest273Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_random_statetest273(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x4f3f701464972e74606d6ea82d4d3080599a0e79")
    sender = Address("0x2e3d0156d2b99a6eacba540c55f423c8f5a33143")
    contract = Address("0x5f82da708c6f5a1f5c2e84cd0239dad1edb623aa")

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
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=(
        Op.NUMBER + Op.TIMESTAMP + Op.TIMESTAMP + Op.NUMBER + Op.NUMBER
        + Op.TIMESTAMP + Op.JUMPDEST + Op.PREVRANDAO + Op.SWAP6 + Op.SELFDESTRUCT
        + Op.CREATE + Op.TIMESTAMP + Op.SSTORE(key=0x99, value=Op.DUP6)
    ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xb1f4cbc3a50042184425a6f9e996d0910f7ba879457ce5dac5c71e498ad3c005"
        ),
        to=contract,
        data=bytes.fromhex("42"),
        gas_limit=400000,
        gas_price=10,
        nonce=0,
        value=100000,
    )

    post = {
        coinbase: Account(
            code=Op.JUMPI(pc=0x9, condition=Op.ISZERO(Op.SLOAD(key=Op.CALLDATALOAD(offset=0x0)))) + Op.STOP + Op.JUMPDEST + Op.SSTORE(key=Op.CALLDATALOAD(offset=0x0), value=Op.CALLDATALOAD(offset=0x20)),
        ),
        contract: Account(
            code=Op.NUMBER + Op.TIMESTAMP + Op.TIMESTAMP + Op.NUMBER + Op.NUMBER + Op.TIMESTAMP + Op.JUMPDEST + Op.PREVRANDAO + Op.SWAP6 + Op.SELFDESTRUCT + Op.CREATE + Op.TIMESTAMP + Op.SSTORE(key=0x99, value=Op.DUP6),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
