"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRandom2/randomStatetest632Filler.json
"""

import pytest
from execution_testing import (
    Account,
    Address,
    Alloc,
    EOA,
    Environment,
    Hash,
    StateTestFiller,
    Transaction,
)
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


@pytest.mark.ported_from(
    ["tests/static/state_tests/stRandom2/randomStatetest632Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_random_statetest632(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x4f3f701464972e74606d6ea82d4d3080599a0e79")
    sender = EOA(
        key=0xB1F4CBC3A50042184425A6F9E996D0910F7BA879457CE5DAC5C71E498AD3C005
    )
    contract = Address("0xde14e9d6c6f9145c355fdf3100fe961632d4cf85")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)
    # Source: raw bytecode
    pre[coinbase] = Account(
        balance=46,
        nonce=0,
        code=(
            Op.JUMPI(
                pc=0x9,
                condition=Op.ISZERO(Op.SLOAD(key=Op.CALLDATALOAD(offset=0x0))),
            )
            + Op.STOP
            + Op.JUMPDEST
            + Op.SSTORE(
                key=Op.CALLDATALOAD(offset=0x0),
                value=Op.CALLDATALOAD(offset=0x20),
            )
        ),
    )
    # Source: raw bytecode
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.NUMBER
            + Op.TIMESTAMP
            + Op.NUMBER
            + Op.NUMBER
            + Op.PREVRANDAO
            + Op.PREVRANDAO
            + Op.TIMESTAMP
            + Op.POP(Op.NUMBER)
            + Op.EXP(Op.CALLCODE, Op.EQ(Op.CALLDATASIZE, Op.ADDRESS))
        ),
    )

    tx = Transaction(
        sender=sender,
        to=contract,
        data=bytes.fromhex("42"),
        gas_limit=400000,
        gas_price=10,
        nonce=0,
        value=100000,
    )

    post = {
        coinbase: Account(
            code=(
                Op.JUMPI(
                    pc=0x9,
                    condition=Op.ISZERO(
                        Op.SLOAD(key=Op.CALLDATALOAD(offset=0x0))
                    ),
                )
                + Op.STOP
                + Op.JUMPDEST
                + Op.SSTORE(
                    key=Op.CALLDATALOAD(offset=0x0),
                    value=Op.CALLDATALOAD(offset=0x20),
                )
            ),
        ),
        contract: Account(
            code=(
                Op.NUMBER
                + Op.TIMESTAMP
                + Op.NUMBER
                + Op.NUMBER
                + Op.PREVRANDAO
                + Op.PREVRANDAO
                + Op.TIMESTAMP
                + Op.POP(Op.NUMBER)
                + Op.EXP(Op.CALLCODE, Op.EQ(Op.CALLDATASIZE, Op.ADDRESS))
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
