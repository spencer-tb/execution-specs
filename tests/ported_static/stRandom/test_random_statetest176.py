"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRandom/randomStatetest176Filler.json
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
    ["tests/static/state_tests/stRandom/randomStatetest176Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_random_statetest176(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x4f3f701464972e74606d6ea82d4d3080599a0e79")
    sender = EOA(
        key=0xB1F4CBC3A50042184425A6F9E996D0910F7BA879457CE5DAC5C71E498AD3C005
    )
    contract = Address("0x6520f3aed37c7b3960ec53119d5b0cedd39fe2f6")

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
        code=bytes.fromhex(
            "327fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f00"  # noqa: E501
            "0000000000000000000000000000000000000000000000000000000000c350427f000000"  # noqa: E501
            "000000000000000000000000000000000000000000000000000000c3507f000000000000"  # noqa: E501
            "0000000000004f3f701464972e74606d6ea82d4d3080599a0e797f000000000000000000"  # noqa: E501
            "00000000000000000000000000000000000000000000017fffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffffff041469988517f6889d92799e74664160"  # noqa: E501
            "005155"
        ),
    )

    tx = Transaction(
        sender=sender,
        to=contract,
        data=bytes.fromhex(
            "327fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f00"  # noqa: E501
            "0000000000000000000000000000000000000000000000000000000000c350427f000000"  # noqa: E501
            "000000000000000000000000000000000000000000000000000000c3507f000000000000"  # noqa: E501
            "0000000000004f3f701464972e74606d6ea82d4d3080599a0e797f000000000000000000"  # noqa: E501
            "00000000000000000000000000000000000000000000017fffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffffff041469988517f6889d92799e746641"  # noqa: E501
        ),
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=242920391,
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
            code=bytes.fromhex(
                "327fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f000000000000000000000000000000000000000000000000000000000000c350427f000000000000000000000000000000000000000000000000000000000000c3507f0000000000000000000000004f3f701464972e74606d6ea82d4d3080599a0e797f00000000000000000000000000000000000000000000000000000000000000017fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff041469988517f6889d92799e74664160005155"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
