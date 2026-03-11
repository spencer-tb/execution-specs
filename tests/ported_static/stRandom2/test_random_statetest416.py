"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRandom2/randomStatetest416Filler.json
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
    ["tests/static/state_tests/stRandom2/randomStatetest416Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_random_statetest416(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x4f3f701464972e74606d6ea82d4d3080599a0e79")
    sender = Address("0x2e3d0156d2b99a6eacba540c55f423c8f5a33143")
    contract = Address("0xd57defd369a62e5099d173d42772d3345138bede")

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
            Op.PUSH32[0x0]
            + Op.PUSH32[0x10000000000000000000000000000000000000000]
            + Op.PUSH32[0x0]
            + Op.PUSH32[0x1]
            + Op.PUSH32[0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF]
            + Op.TIMESTAMP
            + Op.SSTORE(
                key=Op.NUMBER,
                value=Op.PUSH32[0x4F3F701464972E74606D6EA82D4D3080599A0E79],
            )
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xb1f4cbc3a50042184425a6f9e996d0910f7ba879457ce5dac5c71e498ad3c005"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex(
            "7f00000000000000000000000000000000000000000000000000000000000000007f0000"  # noqa: E501
            "0000000000000000000100000000000000000000000000000000000000007f0000000000"  # noqa: E501
            "0000000000000000000000000000000000000000000000000000007f0000000000000000"  # noqa: E501
            "0000000000000000000000000000000000000000000000017f0000000000000000000000"  # noqa: E501
            "00ffffffffffffffffffffffffffffffffffffffff427f0000000000000000000000004f"  # noqa: E501
            "3f701464972e74606d6ea82d4d3080599a0e7943"
        ),
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=1331831824,
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
            storage={1: 0x4F3F701464972E74606D6EA82D4D3080599A0E79},
            code=(
                Op.PUSH32[0x0]
                + Op.PUSH32[0x10000000000000000000000000000000000000000]
                + Op.PUSH32[0x0]
                + Op.PUSH32[0x1]
                + Op.PUSH32[0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF]
                + Op.TIMESTAMP
                + Op.SSTORE(
                    key=Op.NUMBER,
                    value=Op.PUSH32[
                        0x4F3F701464972E74606D6EA82D4D3080599A0E79
                    ],
                )
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
