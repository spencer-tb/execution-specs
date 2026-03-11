"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRandom/randomStatetest171Filler.json
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
    ["tests/static/state_tests/stRandom/randomStatetest171Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_random_statetest171(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x4f3f701464972e74606d6ea82d4d3080599a0e79")
    sender = EOA(
        key=0xB1F4CBC3A50042184425A6F9E996D0910F7BA879457CE5DAC5C71E498AD3C005
    )
    contract = Address("0x698791d8a7c355091fa7bc3a0171cd426dbe2f51")

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
        balance=0,
        nonce=0,
        code=(
            Op.PUSH32[0xC350]
            + Op.NUMBER
            + Op.PUSH32[0x0]
            + Op.SSTORE(
                key=Op.MULMOD(
                    0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE,  # noqa: E501
                    Op.NOT(
                        Op.PUSH32[0x4F3F701464972E74606D6EA82D4D3080599A0E79]
                    ),
                    0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE,  # noqa: E501
                ),
                value=Op.PUSH32[0x1],
            )
            + Op.MLOAD(offset=0x0)
            + Op.SSTORE
        ),
    )

    tx = Transaction(
        sender=sender,
        to=contract,
        data=bytes.fromhex(
            "7f000000000000000000000000000000000000000000000000000000000000c350437f00"  # noqa: E501
            "000000000000000000000000000000000000000000000000000000000000007f00000000"  # noqa: E501
            "000000000000000000000000000000000000000000000000000000017fffffffffffffff"  # noqa: E501
            "fffffffffffffffffffffffffffffffffffffffffffffffffe7f00000000000000000000"  # noqa: E501
            "00004f3f701464972e74606d6ea82d4d3080599a0e79197fffffffffffffffffffffffff"  # noqa: E501
            "fffffffffffffffffffffffffffffffffffffffe09"
        ),
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=1726364132,
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
                Op.PUSH32[0xC350]
                + Op.NUMBER
                + Op.PUSH32[0x0]
                + Op.SSTORE(
                    key=Op.MULMOD(
                        0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE,  # noqa: E501
                        Op.NOT(
                            Op.PUSH32[
                                0x4F3F701464972E74606D6EA82D4D3080599A0E79
                            ],
                        ),
                        0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE,  # noqa: E501
                    ),
                    value=Op.PUSH32[0x1],
                )
                + Op.MLOAD(offset=0x0)
                + Op.SSTORE
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
