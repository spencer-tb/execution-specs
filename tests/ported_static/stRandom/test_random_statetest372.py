"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRandom/randomStatetest372Filler.json
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
    ["tests/static/state_tests/stRandom/randomStatetest372Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_random_statetest372(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x945304eb96065b2a98b57a48a06ae28d285a71b5")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x095e7baea6a6c7c4c2dfeb977efac326af552d87")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    # Source: raw bytecode
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.PUSH32[0x1]
            + Op.PUSH32[
                0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE  # noqa: E501
            ]
            + Op.PUSH32[0x10000000000000000000000000000000000000000]
            + Op.PUSH32[0x10000000000000000000000000000000000000000]
            + Op.SSTORE(
                key=Op.MLOAD(offset=0x0),
                value=Op.ADDMOD(
                    Op.XOR(
                        Op.PUSH32[0x1],
                        Op.PUSH32[0x945304EB96065B2A98B57A48A06AE28D285A71B5],
                    ),
                    Op.PUSH32[0x945304EB96065B2A98B57A48A06AE28D285A71B5],
                    Op.PUSH32[0x945304EB96065B2A98B57A48A06AE28D285A71B5],
                ),
            )
        ),
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
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex(
            "7f00000000000000000000000000000000000000000000000000000000000000017fffff"  # noqa: E501
            "fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe7f0000000000"  # noqa: E501
            "0000000000000100000000000000000000000000000000000000007f0000000000000000"  # noqa: E501
            "0000000100000000000000000000000000000000000000007f0000000000000000000000"  # noqa: E501
            "00945304eb96065b2a98b57a48a06ae28d285a71b57f0000000000000000000000009453"  # noqa: E501
            "04eb96065b2a98b57a48a06ae28d285a71b57f000000000000000000000000945304eb96"  # noqa: E501
            "065b2a98b57a48a06ae28d285a71b57f0000000000000000000000000000000000000000"  # noqa: E501
            "0000000000000000000000011808"
        ),
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=1833691657,
    )

    post = {
        contract: Account(
            storage={0: 0x945304EB96065B2A98B57A48A06AE28D285A71B4},
            code=(
                Op.PUSH32[0x1]
                + Op.PUSH32[
                    0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE  # noqa: E501
                ]
                + Op.PUSH32[0x10000000000000000000000000000000000000000]
                + Op.PUSH32[0x10000000000000000000000000000000000000000]
                + Op.SSTORE(
                    key=Op.MLOAD(offset=0x0),
                    value=Op.ADDMOD(
                        Op.XOR(
                            Op.PUSH32[0x1],
                            Op.PUSH32[
                                0x945304EB96065B2A98B57A48A06AE28D285A71B5
                            ],
                        ),
                        Op.PUSH32[0x945304EB96065B2A98B57A48A06AE28D285A71B5],
                        Op.PUSH32[0x945304EB96065B2A98B57A48A06AE28D285A71B5],
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
