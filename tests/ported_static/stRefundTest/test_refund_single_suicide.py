"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRefundTest/refund_singleSuicideFiller.json
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
    ["tests/static/state_tests/stRefundTest/refund_singleSuicideFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_refund_single_suicide(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0xeb201d2887816e041f6e807e804f64f3a7a226fe")
    sender = Address("0xdf2e264abeec114532b73774cfa1994aed66a9f6")
    contract = Address("0xfc2c9403120f755b844fd30d99c231483e701631")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    pre[sender] = Account(balance=0x1C9C380, nonce=0)
    pre[coinbase] = Account(balance=0, nonce=1)
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.MSTORE(offset=0x40, value=0x60)
            + Op.DIV(Op.CALLDATALOAD(offset=0x0), Op.EXP(0x2, 0xE0))
            + Op.JUMPI(pc=0x2E, condition=Op.EQ(Op.DUP2, 0x9E587A5))
            + Op.JUMPI(pc=0x49, condition=Op.EQ(0x2E4699ED, Op.DUP1))
            + Op.JUMPI(pc=0x9B, condition=Op.EQ(0xC0406226, Op.DUP1))
            + Op.JUMPDEST
            + Op.STOP
            + Op.JUMPDEST
            + Op.PUSH1[0x2C]
            + Op.SELFDESTRUCT(
                address=Op.AND(
                    0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                    Op.CALLER,
                ),
            )
            + Op.JUMPDEST
            + Op.PUSH1[0x2C]
            + Op.JUMPDEST
            + Op.PUSH1[0x0]
            + Op.ADDRESS
            + Op.SWAP1
            + Op.POP
            + Op.AND(0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF, Op.DUP1)
            + Op.PUSH4[0x9E587A5]
            + Op.MLOAD(offset=0x40)
            + Op.MSTORE(
                offset=Op.DUP2, value=Op.MUL(Op.EXP(0x2, 0xE0), Op.DUP2)
            )
            + Op.PUSH1[0x4]
            + Op.ADD
            + Op.DUP1
            + Op.SWAP1
            + Op.POP
            + Op.JUMPI(
                pc=0x2,
                condition=Op.ISZERO(
                    Op.CALL(
                        gas=Op.SUB(Op.GAS, 0x61DA),
                        address=Op.DUP8,
                        value=0x0,
                        args_offset=Op.DUP2,
                        args_size=Op.SUB(Op.DUP4, Op.DUP1),
                        ret_offset=Op.MLOAD(offset=0x40),
                        ret_size=0x0,
                    ),
                ),
            )
            + Op.POP
            + Op.POP
            + Op.POP
            + Op.POP
            + Op.JUMP
            + Op.JUMPDEST
            + Op.PUSH1[0xA5]
            + Op.PUSH1[0x0]
            + Op.PUSH1[0xB9]
            + Op.JUMP(pc=0x4C)
            + Op.JUMPDEST
            + Op.PUSH1[0x40]
            + Op.MLOAD(offset=Op.DUP1)
            + Op.SWAP2
            + Op.MSTORE(offset=Op.DUP3, value=Op.ISZERO(Op.ISZERO))
            + Op.MLOAD
            + Op.SWAP1
            + Op.DUP2
            + Op.SWAP1
            + Op.ADD(0x20, Op.SUB)
            + Op.SWAP1
            + Op.RETURN
            + Op.JUMPDEST
            + Op.POP
            + Op.PUSH1[0x1]
            + Op.SWAP1
            + Op.JUMP
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0x2b75d0c814eb07c075fccbdd9a036faf651d9c46d7477d6c4f30772cfca90d38"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex("c0406226"),
        gas_limit=300000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            code=(
                Op.MSTORE(offset=0x40, value=0x60)
                + Op.DIV(Op.CALLDATALOAD(offset=0x0), Op.EXP(0x2, 0xE0))
                + Op.JUMPI(pc=0x2E, condition=Op.EQ(Op.DUP2, 0x9E587A5))
                + Op.JUMPI(pc=0x49, condition=Op.EQ(0x2E4699ED, Op.DUP1))
                + Op.JUMPI(pc=0x9B, condition=Op.EQ(0xC0406226, Op.DUP1))
                + Op.JUMPDEST
                + Op.STOP
                + Op.JUMPDEST
                + Op.PUSH1[0x2C]
                + Op.SELFDESTRUCT(
                    address=Op.AND(
                        0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                        Op.CALLER,
                    ),
                )
                + Op.JUMPDEST
                + Op.PUSH1[0x2C]
                + Op.JUMPDEST
                + Op.PUSH1[0x0]
                + Op.ADDRESS
                + Op.SWAP1
                + Op.POP
                + Op.AND(0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF, Op.DUP1)
                + Op.PUSH4[0x9E587A5]
                + Op.MLOAD(offset=0x40)
                + Op.MSTORE(
                    offset=Op.DUP2,
                    value=Op.MUL(Op.EXP(0x2, 0xE0), Op.DUP2),
                )
                + Op.PUSH1[0x4]
                + Op.ADD
                + Op.DUP1
                + Op.SWAP1
                + Op.POP
                + Op.JUMPI(
                    pc=0x2,
                    condition=Op.ISZERO(
                        Op.CALL(
                            gas=Op.SUB(Op.GAS, 0x61DA),
                            address=Op.DUP8,
                            value=0x0,
                            args_offset=Op.DUP2,
                            args_size=Op.SUB(Op.DUP4, Op.DUP1),
                            ret_offset=Op.MLOAD(offset=0x40),
                            ret_size=0x0,
                        ),
                    ),
                )
                + Op.POP
                + Op.POP
                + Op.POP
                + Op.POP
                + Op.JUMP
                + Op.JUMPDEST
                + Op.PUSH1[0xA5]
                + Op.PUSH1[0x0]
                + Op.PUSH1[0xB9]
                + Op.JUMP(pc=0x4C)
                + Op.JUMPDEST
                + Op.PUSH1[0x40]
                + Op.MLOAD(offset=Op.DUP1)
                + Op.SWAP2
                + Op.MSTORE(offset=Op.DUP3, value=Op.ISZERO(Op.ISZERO))
                + Op.MLOAD
                + Op.SWAP1
                + Op.DUP2
                + Op.SWAP1
                + Op.ADD(0x20, Op.SUB)
                + Op.SWAP1
                + Op.RETURN
                + Op.JUMPDEST
                + Op.POP
                + Op.PUSH1[0x1]
                + Op.SWAP1
                + Op.JUMP
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
