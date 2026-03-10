"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRandom2/randomStatetest414Filler.json
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
    ["tests/static/state_tests/stRandom2/randomStatetest414Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_random_statetest414(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x4f3f701464972e74606d6ea82d4d3080599a0e79")
    sender = Address("0x2e3d0156d2b99a6eacba540c55f423c8f5a33143")
    contract = Address("0x16000b6b36a20d3093a8b71a9fd8292c8a641002")

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
            Op.PUSH32[
                0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF  # noqa: E501
            ]
            + Op.PUSH3[0x51437F]
            + Op.STOP
            + Op.STOP
            + Op.STOP
            + Op.STOP
            + Op.STOP
            + Op.STOP
            + Op.STOP
            + Op.STOP
            + Op.STOP
            + Op.STOP
            + Op.STOP
            + Op.ADD
            + Op.STOP
            + Op.STOP
            + Op.STOP
            + Op.STOP
            + Op.STOP
            + Op.STOP
            + Op.STOP
            + Op.STOP
            + Op.STOP
            + Op.STOP
            + Op.STOP
            + Op.STOP
            + Op.STOP
            + Op.STOP
            + Op.STOP
            + Op.STOP
            + Op.STOP
            + Op.STOP
            + Op.STOP
            + Op.STOP
            + Op.NUMBER
            + Op.SSTORE(
                key=Op.MLOAD(offset=0x0),
                value=Op.EQ(
                    Op.CALL,
                    Op.PUSH32[0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF],
                ),
            )
        ),
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)
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

    tx = Transaction(
        secret_key=Hash(
            "0xb1f4cbc3a50042184425a6f9e996d0910f7ba879457ce5dac5c71e498ad3c005"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex(
            "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff625143"  # noqa: E501
            "7f0000000000000000000000010000000000000000000000000000000000000000437f00"  # noqa: E501
            "0000000000000000000000fffffffffffffffffffffffffffffffffffffffff114"  # noqa: E501
        ),
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=1088932905,
    )

    post = {
        contract: Account(
            code=(
                Op.PUSH32[
                    0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF  # noqa: E501
                ]
                + Op.PUSH3[0x51437F]
                + Op.STOP
                + Op.STOP
                + Op.STOP
                + Op.STOP
                + Op.STOP
                + Op.STOP
                + Op.STOP
                + Op.STOP
                + Op.STOP
                + Op.STOP
                + Op.STOP
                + Op.ADD
                + Op.STOP
                + Op.STOP
                + Op.STOP
                + Op.STOP
                + Op.STOP
                + Op.STOP
                + Op.STOP
                + Op.STOP
                + Op.STOP
                + Op.STOP
                + Op.STOP
                + Op.STOP
                + Op.STOP
                + Op.STOP
                + Op.STOP
                + Op.STOP
                + Op.STOP
                + Op.STOP
                + Op.STOP
                + Op.STOP
                + Op.NUMBER
                + Op.SSTORE(
                    key=Op.MLOAD(offset=0x0),
                    value=Op.EQ(
                        Op.CALL,
                        Op.PUSH32[0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF],
                    ),
                )
            ),
        ),
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
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
