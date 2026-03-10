"""
Ori Pomerantz qbzzt1@gmail.com.

Ported from:
tests/static/state_tests/VMTests/vmArithmeticTest/expPower2Filler.yml
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
    ["tests/static/state_tests/VMTests/vmArithmeticTest/expPower2Filler.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_exp_power2(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Ori Pomerantz qbzzt1@gmail.com."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x56724d001b4f2a2888a81971a64aad37cd43f881")
    contract = Address("0x5a18b275908ad6766155191a40654188fe012dc6")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000,
    )

    pre[sender] = Account(balance=0xBA1A9CE0BA1A9CE, nonce=0)
    pre[contract] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.SSTORE(
                key=Op.MUL(0x10, 0x1), value=Op.EXP(0x2, Op.EXP(0x2, 0x1))
            )
            + Op.SSTORE(
                key=Op.ADD(Op.MUL(0x10, 0x1), 0x1),
                value=Op.EXP(0x2, Op.SUB(Op.EXP(0x2, 0x1), 0x1)),
            )
            + Op.SSTORE(
                key=Op.ADD(Op.MUL(0x10, 0x1), 0x2),
                value=Op.EXP(0x2, Op.ADD(Op.EXP(0x2, 0x1), 0x1)),
            )
            + Op.SSTORE(
                key=Op.MUL(0x10, 0x2), value=Op.EXP(0x2, Op.EXP(0x2, 0x2))
            )
            + Op.SSTORE(
                key=Op.ADD(Op.MUL(0x10, 0x2), 0x1),
                value=Op.EXP(0x2, Op.SUB(Op.EXP(0x2, 0x2), 0x1)),
            )
            + Op.SSTORE(
                key=Op.ADD(Op.MUL(0x10, 0x2), 0x2),
                value=Op.EXP(0x2, Op.ADD(Op.EXP(0x2, 0x2), 0x1)),
            )
            + Op.SSTORE(
                key=Op.MUL(0x10, 0x3), value=Op.EXP(0x2, Op.EXP(0x2, 0x3))
            )
            + Op.SSTORE(
                key=Op.ADD(Op.MUL(0x10, 0x3), 0x1),
                value=Op.EXP(0x2, Op.SUB(Op.EXP(0x2, 0x3), 0x1)),
            )
            + Op.SSTORE(
                key=Op.ADD(Op.MUL(0x10, 0x3), 0x2),
                value=Op.EXP(0x2, Op.ADD(Op.EXP(0x2, 0x3), 0x1)),
            )
            + Op.SSTORE(
                key=Op.MUL(0x10, 0x4), value=Op.EXP(0x2, Op.EXP(0x2, 0x4))
            )
            + Op.SSTORE(
                key=Op.ADD(Op.MUL(0x10, 0x4), 0x1),
                value=Op.EXP(0x2, Op.SUB(Op.EXP(0x2, 0x4), 0x1)),
            )
            + Op.SSTORE(
                key=Op.ADD(Op.MUL(0x10, 0x4), 0x2),
                value=Op.EXP(0x2, Op.ADD(Op.EXP(0x2, 0x4), 0x1)),
            )
            + Op.SSTORE(
                key=Op.MUL(0x10, 0x5), value=Op.EXP(0x2, Op.EXP(0x2, 0x5))
            )
            + Op.SSTORE(
                key=Op.ADD(Op.MUL(0x10, 0x5), 0x1),
                value=Op.EXP(0x2, Op.SUB(Op.EXP(0x2, 0x5), 0x1)),
            )
            + Op.SSTORE(
                key=Op.ADD(Op.MUL(0x10, 0x5), 0x2),
                value=Op.EXP(0x2, Op.ADD(Op.EXP(0x2, 0x5), 0x1)),
            )
            + Op.SSTORE(
                key=Op.MUL(0x10, 0x6), value=Op.EXP(0x2, Op.EXP(0x2, 0x6))
            )
            + Op.SSTORE(
                key=Op.ADD(Op.MUL(0x10, 0x6), 0x1),
                value=Op.EXP(0x2, Op.SUB(Op.EXP(0x2, 0x6), 0x1)),
            )
            + Op.SSTORE(
                key=Op.ADD(Op.MUL(0x10, 0x6), 0x2),
                value=Op.EXP(0x2, Op.ADD(Op.EXP(0x2, 0x6), 0x1)),
            )
            + Op.SSTORE(
                key=Op.MUL(0x10, 0x7), value=Op.EXP(0x2, Op.EXP(0x2, 0x7))
            )
            + Op.SSTORE(
                key=Op.ADD(Op.MUL(0x10, 0x7), 0x1),
                value=Op.EXP(0x2, Op.SUB(Op.EXP(0x2, 0x7), 0x1)),
            )
            + Op.SSTORE(
                key=Op.ADD(Op.MUL(0x10, 0x7), 0x2),
                value=Op.EXP(0x2, Op.ADD(Op.EXP(0x2, 0x7), 0x1)),
            )
            + Op.SSTORE(
                key=Op.MUL(0x10, 0x8), value=Op.EXP(0x2, Op.EXP(0x2, 0x8))
            )
            + Op.SSTORE(
                key=Op.ADD(Op.MUL(0x10, 0x8), 0x1),
                value=Op.EXP(0x2, Op.SUB(Op.EXP(0x2, 0x8), 0x1)),
            )
            + Op.SSTORE(
                key=Op.ADD(Op.MUL(0x10, 0x8), 0x2),
                value=Op.EXP(0x2, Op.ADD(Op.EXP(0x2, 0x8), 0x1)),
            )
            + Op.STOP
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0x40ac0fc28c27e961ee46ec43355a094de205856edbd4654cf2577c2608d4ec1e"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex(
            "693c61390000000000000000000000000000000000000000000000000000000000000000"  # noqa: E501
        ),
        gas_limit=16777216,
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = {
        contract: Account(
            storage={
                16: 4,
                17: 2,
                18: 8,
                32: 16,
                33: 8,
                34: 32,
                48: 256,
                49: 128,
                50: 512,
                64: 0x10000,
                65: 32768,
                66: 0x20000,
                80: 0x100000000,
                81: 0x80000000,
                82: 0x200000000,
                96: 0x10000000000000000,
                97: 0x8000000000000000,
                98: 0x20000000000000000,
                112: 0x100000000000000000000000000000000,
                113: 0x80000000000000000000000000000000,
                114: 0x200000000000000000000000000000000,
                129: 0x8000000000000000000000000000000000000000000000000000000000000000,  # noqa: E501
            },
            code=(
                Op.SSTORE(
                    key=Op.MUL(0x10, 0x1),
                    value=Op.EXP(0x2, Op.EXP(0x2, 0x1)),
                )
                + Op.SSTORE(
                    key=Op.ADD(Op.MUL(0x10, 0x1), 0x1),
                    value=Op.EXP(0x2, Op.SUB(Op.EXP(0x2, 0x1), 0x1)),
                )
                + Op.SSTORE(
                    key=Op.ADD(Op.MUL(0x10, 0x1), 0x2),
                    value=Op.EXP(0x2, Op.ADD(Op.EXP(0x2, 0x1), 0x1)),
                )
                + Op.SSTORE(
                    key=Op.MUL(0x10, 0x2),
                    value=Op.EXP(0x2, Op.EXP(0x2, 0x2)),
                )
                + Op.SSTORE(
                    key=Op.ADD(Op.MUL(0x10, 0x2), 0x1),
                    value=Op.EXP(0x2, Op.SUB(Op.EXP(0x2, 0x2), 0x1)),
                )
                + Op.SSTORE(
                    key=Op.ADD(Op.MUL(0x10, 0x2), 0x2),
                    value=Op.EXP(0x2, Op.ADD(Op.EXP(0x2, 0x2), 0x1)),
                )
                + Op.SSTORE(
                    key=Op.MUL(0x10, 0x3),
                    value=Op.EXP(0x2, Op.EXP(0x2, 0x3)),
                )
                + Op.SSTORE(
                    key=Op.ADD(Op.MUL(0x10, 0x3), 0x1),
                    value=Op.EXP(0x2, Op.SUB(Op.EXP(0x2, 0x3), 0x1)),
                )
                + Op.SSTORE(
                    key=Op.ADD(Op.MUL(0x10, 0x3), 0x2),
                    value=Op.EXP(0x2, Op.ADD(Op.EXP(0x2, 0x3), 0x1)),
                )
                + Op.SSTORE(
                    key=Op.MUL(0x10, 0x4),
                    value=Op.EXP(0x2, Op.EXP(0x2, 0x4)),
                )
                + Op.SSTORE(
                    key=Op.ADD(Op.MUL(0x10, 0x4), 0x1),
                    value=Op.EXP(0x2, Op.SUB(Op.EXP(0x2, 0x4), 0x1)),
                )
                + Op.SSTORE(
                    key=Op.ADD(Op.MUL(0x10, 0x4), 0x2),
                    value=Op.EXP(0x2, Op.ADD(Op.EXP(0x2, 0x4), 0x1)),
                )
                + Op.SSTORE(
                    key=Op.MUL(0x10, 0x5),
                    value=Op.EXP(0x2, Op.EXP(0x2, 0x5)),
                )
                + Op.SSTORE(
                    key=Op.ADD(Op.MUL(0x10, 0x5), 0x1),
                    value=Op.EXP(0x2, Op.SUB(Op.EXP(0x2, 0x5), 0x1)),
                )
                + Op.SSTORE(
                    key=Op.ADD(Op.MUL(0x10, 0x5), 0x2),
                    value=Op.EXP(0x2, Op.ADD(Op.EXP(0x2, 0x5), 0x1)),
                )
                + Op.SSTORE(
                    key=Op.MUL(0x10, 0x6),
                    value=Op.EXP(0x2, Op.EXP(0x2, 0x6)),
                )
                + Op.SSTORE(
                    key=Op.ADD(Op.MUL(0x10, 0x6), 0x1),
                    value=Op.EXP(0x2, Op.SUB(Op.EXP(0x2, 0x6), 0x1)),
                )
                + Op.SSTORE(
                    key=Op.ADD(Op.MUL(0x10, 0x6), 0x2),
                    value=Op.EXP(0x2, Op.ADD(Op.EXP(0x2, 0x6), 0x1)),
                )
                + Op.SSTORE(
                    key=Op.MUL(0x10, 0x7),
                    value=Op.EXP(0x2, Op.EXP(0x2, 0x7)),
                )
                + Op.SSTORE(
                    key=Op.ADD(Op.MUL(0x10, 0x7), 0x1),
                    value=Op.EXP(0x2, Op.SUB(Op.EXP(0x2, 0x7), 0x1)),
                )
                + Op.SSTORE(
                    key=Op.ADD(Op.MUL(0x10, 0x7), 0x2),
                    value=Op.EXP(0x2, Op.ADD(Op.EXP(0x2, 0x7), 0x1)),
                )
                + Op.SSTORE(
                    key=Op.MUL(0x10, 0x8),
                    value=Op.EXP(0x2, Op.EXP(0x2, 0x8)),
                )
                + Op.SSTORE(
                    key=Op.ADD(Op.MUL(0x10, 0x8), 0x1),
                    value=Op.EXP(0x2, Op.SUB(Op.EXP(0x2, 0x8), 0x1)),
                )
                + Op.SSTORE(
                    key=Op.ADD(Op.MUL(0x10, 0x8), 0x2),
                    value=Op.EXP(0x2, Op.ADD(Op.EXP(0x2, 0x8), 0x1)),
                )
                + Op.STOP
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
