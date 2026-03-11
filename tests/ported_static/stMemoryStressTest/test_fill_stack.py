"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stMemoryStressTest/FillStackFiller.json
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
    ["tests/static/state_tests/stMemoryStressTest/FillStackFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit, expected_post",
    [
        (
            3141592,
            {
                Address("0x4f3f701464972e74606d6ea82d4d3080599a0e79"): Account(
                    code=Op.JUMPI(
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
                Address("0x709ee68118ab00ce0bab659c9aa89744b35703fa"): Account(
                    code=Op.JUMPDEST
                    + Op.PUSH32[
                        0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF  # noqa: E501
                    ]
                    + Op.PUSH32[
                        0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE  # noqa: E501
                    ]
                    + Op.GASLIMIT
                    + Op.PUSH32[0x10000000000000000000000000000000000000000]
                    + Op.PUSH32[0x1]
                    + Op.JUMPI(pc=Op.NUMBER, condition=Op.PUSH32[0xC350])
                    + Op.ISZERO
                    + Op.MSTORE8
                    + Op.SHA3
                    + Op.DUP1
                    + Op.GASPRICE
                    + Op.SWAP8
                    + Op.SSTORE
                    + Op.MLOAD(offset=0x0)
                    + Op.SSTORE
                ),
            },
        ),
        (
            16777216,
            {
                Address("0x4f3f701464972e74606d6ea82d4d3080599a0e79"): Account(
                    code=Op.JUMPI(
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
                Address("0x709ee68118ab00ce0bab659c9aa89744b35703fa"): Account(
                    code=Op.JUMPDEST
                    + Op.PUSH32[
                        0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF  # noqa: E501
                    ]
                    + Op.PUSH32[
                        0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE  # noqa: E501
                    ]
                    + Op.GASLIMIT
                    + Op.PUSH32[0x10000000000000000000000000000000000000000]
                    + Op.PUSH32[0x1]
                    + Op.JUMPI(pc=Op.NUMBER, condition=Op.PUSH32[0xC350])
                    + Op.ISZERO
                    + Op.MSTORE8
                    + Op.SHA3
                    + Op.DUP1
                    + Op.GASPRICE
                    + Op.SWAP8
                    + Op.SSTORE
                    + Op.MLOAD(offset=0x0)
                    + Op.SSTORE
                ),
            },
        ),
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_fill_stack(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x4f3f701464972e74606d6ea82d4d3080599a0e79")
    sender = Address("0xded0d7993c3e6100a321e038900a8114c05ddf51")
    contract = Address("0x709ee68118ab00ce0bab659c9aa89744b35703fa")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

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
            Op.JUMPDEST
            + Op.PUSH32[
                0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF  # noqa: E501
            ]
            + Op.PUSH32[
                0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE  # noqa: E501
            ]
            + Op.GASLIMIT
            + Op.PUSH32[0x10000000000000000000000000000000000000000]
            + Op.PUSH32[0x1]
            + Op.JUMPI(pc=Op.NUMBER, condition=Op.PUSH32[0xC350])
            + Op.ISZERO
            + Op.MSTORE8
            + Op.SHA3
            + Op.DUP1
            + Op.GASPRICE
            + Op.SWAP8
            + Op.SSTORE
            + Op.MLOAD(offset=0x0)
            + Op.SSTORE
        ),
    )
    pre[sender] = Account(balance=0x152D02C7E14AF6800000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x23000fe3d08cdeba75eb2e2e2909f842dbf48aa0c566f49101e8285c8dec62d6"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex(
            "5b7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fff"  # noqa: E501
            "fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe457f000000"  # noqa: E501
            "00000000000000000100000000000000000000000000000000000000007f000000000000"  # noqa: E501
            "00000000000000000000000000000000000000000000000000017f000000000000000000"  # noqa: E501
            "000000000000000000000000000000000000000000c3504357155320803a97"
        ),
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=264050067,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
