"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stSolidityTest/ContractInheritanceFiller.json
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
    ["tests/static/state_tests/stSolidityTest/ContractInheritanceFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.valid_until("Prague")
@pytest.mark.pre_alloc_mutable
def test_contract_inheritance(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x73c241c3bc4fdf83b6ff3ae73735fddf7c9d711d")
    contract = Address("0x3809b123c157b2d0d3b998255f35b5f8b8ae4789")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[contract] = Account(
        balance=0x186A0,
        nonce=0,
        code=(
            Op.DIV(
                Op.CALLDATALOAD(offset=0x0),
                0x100000000000000000000000000000000000000000000000000000000,
            )
            + Op.JUMPI(pc=Op.PUSH2[0x39], condition=Op.EQ(Op.DUP2, 0x3E0BCA3B))
            + Op.JUMPI(pc=Op.PUSH2[0xA8], condition=Op.EQ(0xC0406226, Op.DUP1))
            + Op.STOP
            + Op.JUMPDEST
            + Op.PUSH2[0xB5]
            + Op.JUMPDEST
            + Op.PUSH1[0x1]
            + Op.PUSH1[0x0]
            + Op.DUP1
            + Op.CODECOPY(dest_offset=Op.DUP4, offset=0x1EC, size=0x45)
            + Op.CREATE(value=0x0, offset=0x0, size=0x45)
            + Op.SWAP2
            + Op.POP
            + Op.AND(0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF, Op.DUP2)
            + Op.PUSH4[0x81BDA09B]
            + Op.PUSH1[0x20]
            + Op.PUSH1[0x0]
            + Op.MSTORE(
                offset=0x0,
                value=Op.MUL(
                    0x100000000000000000000000000000000000000000000000000000000,  # noqa: E501
                    Op.DUP3,
                ),
            )
            + Op.PUSH1[0x4]
            + Op.PUSH1[0x0]
            + Op.PUSH1[0x0]
            + Op.DUP7
            + Op.SUB(Op.GAS, 0x61DA)
            + Op.JUMPI(pc=0x119, condition=Op.CALL)
            + Op.STOP
            + Op.JUMPDEST
            + Op.PUSH2[0xBF]
            + Op.PUSH1[0x0]
            + Op.PUSH2[0xC9]
            + Op.JUMP(pc=Op.PUSH2[0x3D])
            + Op.JUMPDEST
            + Op.MSTORE(offset=0x0, value=Op.DUP1)
            + Op.RETURN(offset=0x0, size=0x20)
            + Op.JUMPDEST
            + Op.MSTORE(offset=0x0, value=Op.DUP1)
            + Op.RETURN(offset=0x0, size=0x20)
            + Op.JUMPDEST
            + Op.PUSH1[0x0]
            + Op.AND(
                0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00,  # noqa: E501
                Op.SLOAD(key=Op.DUP1),
            )
            + Op.SWAP2
            + Op.SWAP1
            + Op.SWAP2
            + Op.OR
            + Op.SWAP1
            + Op.DUP2
            + Op.SWAP1
            + Op.SSTORE
            + Op.PUSH1[0xFF]
            + Op.AND
            + Op.SWAP2
            + Op.SWAP1
            + Op.POP
            + Op.JUMP
            + Op.JUMPDEST
            + Op.POP
            + Op.POP
            + Op.JUMPI(
                pc=0x19D,
                condition=Op.ISZERO(
                    Op.EQ(0x2, Op.AND(0xFFFFFFFF, Op.MLOAD(offset=0x0))),
                ),
            )
            + Op.JUMPDEST
            + Op.JUMPDEST
            + Op.POP
            + Op.POP
            + Op.SWAP1
            + Op.JUMP
            + Op.JUMPDEST
            + Op.POP
            + Op.POP
            + Op.JUMPI(
                pc=0x194,
                condition=Op.ISZERO(
                    Op.EQ(0x1, Op.AND(0xFFFFFFFF, Op.MLOAD(offset=0x0))),
                ),
            )
            + Op.JUMPDEST
            + Op.CODECOPY(dest_offset=0x0, offset=0x1A7, size=0x45)
            + Op.CREATE(value=0x0, offset=0x0, size=0x45)
            + Op.SWAP1
            + Op.POP
            + Op.AND(0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF, Op.DUP1)
            + Op.PUSH4[0x81BDA09B]
            + Op.PUSH1[0x20]
            + Op.PUSH1[0x0]
            + Op.MSTORE(
                offset=0x0,
                value=Op.MUL(
                    0x100000000000000000000000000000000000000000000000000000000,  # noqa: E501
                    Op.DUP3,
                ),
            )
            + Op.PUSH1[0x4]
            + Op.PUSH1[0x0]
            + Op.PUSH1[0x0]
            + Op.DUP7
            + Op.SUB(Op.GAS, 0x61DA)
            + Op.JUMPI(pc=Op.PUSH2[0xFF], condition=Op.CALL)
            + Op.STOP
            + Op.JUMPDEST
            + Op.PUSH1[0x0]
            + Op.SWAP3
            + Op.POP
            + Op.JUMP(pc=0x114)
            + Op.JUMPDEST
            + Op.PUSH1[0x0]
            + Op.SWAP3
            + Op.POP
            + Op.JUMP(pc=0x114)
            + Op.STOP
            + Op.PUSH1[0x39]
            + Op.CODECOPY(dest_offset=0x0, offset=0xC, size=Op.DUP1)
            + Op.PUSH1[0x0]
            + Op.RETURN
            + Op.STOP
            + Op.DIV(
                Op.CALLDATALOAD(offset=0x0),
                0x100000000000000000000000000000000000000000000000000000000,
            )
            + Op.JUMPI(pc=0x2D, condition=Op.EQ(Op.DUP2, 0x81BDA09B))
            + Op.STOP
            + Op.JUMPDEST
            + Op.PUSH1[0x2]
            + Op.PUSH1[0x0]
            + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2)
            + Op.PUSH1[0x20]
            + Op.SWAP1
            + Op.RETURN
            + Op.PUSH1[0x39]
            + Op.CODECOPY(dest_offset=0x0, offset=0xC, size=Op.DUP1)
            + Op.PUSH1[0x0]
            + Op.RETURN
            + Op.STOP
            + Op.DIV(
                Op.CALLDATALOAD(offset=0x0),
                0x100000000000000000000000000000000000000000000000000000000,
            )
            + Op.JUMPI(pc=0x2D, condition=Op.EQ(Op.DUP2, 0x81BDA09B))
            + Op.STOP
            + Op.JUMPDEST
            + Op.PUSH1[0x1]
            + Op.PUSH1[0x0]
            + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2)
            + Op.PUSH1[0x20]
            + Op.SWAP1
            + Op.RETURN
        ),
    )
    pre[sender] = Account(balance=0x12A05F200, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xa9ae12cb2700c0214f86b9796881bc03a1fd5605d0e76d2da2ca592e62d53e52"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex("c0406226"),
        gas_limit=35000000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        Address("0x1571f89d2292ae5e46b8c8fd8ebbec038506edea"): Account(
            code=(
                Op.DIV(
                    Op.CALLDATALOAD(offset=0x0),
                    0x100000000000000000000000000000000000000000000000000000000,  # noqa: E501
                )
                + Op.JUMPI(pc=0x2D, condition=Op.EQ(Op.DUP2, 0x81BDA09B))
                + Op.STOP
                + Op.JUMPDEST
                + Op.PUSH1[0x1]
                + Op.PUSH1[0x0]
                + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2)
                + Op.PUSH1[0x20]
                + Op.SWAP1
                + Op.RETURN
            ),
        ),
        contract: Account(
            storage={0: 1},
            code=(
                Op.DIV(
                    Op.CALLDATALOAD(offset=0x0),
                    0x100000000000000000000000000000000000000000000000000000000,  # noqa: E501
                )
                + Op.JUMPI(
                    pc=Op.PUSH2[0x39], condition=Op.EQ(Op.DUP2, 0x3E0BCA3B)
                )
                + Op.JUMPI(
                    pc=Op.PUSH2[0xA8], condition=Op.EQ(0xC0406226, Op.DUP1)
                )
                + Op.STOP
                + Op.JUMPDEST
                + Op.PUSH2[0xB5]
                + Op.JUMPDEST
                + Op.PUSH1[0x1]
                + Op.PUSH1[0x0]
                + Op.DUP1
                + Op.CODECOPY(dest_offset=Op.DUP4, offset=0x1EC, size=0x45)
                + Op.CREATE(value=0x0, offset=0x0, size=0x45)
                + Op.SWAP2
                + Op.POP
                + Op.AND(0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF, Op.DUP2)
                + Op.PUSH4[0x81BDA09B]
                + Op.PUSH1[0x20]
                + Op.PUSH1[0x0]
                + Op.MSTORE(
                    offset=0x0,
                    value=Op.MUL(
                        0x100000000000000000000000000000000000000000000000000000000,  # noqa: E501
                        Op.DUP3,
                    ),
                )
                + Op.PUSH1[0x4]
                + Op.PUSH1[0x0]
                + Op.PUSH1[0x0]
                + Op.DUP7
                + Op.SUB(Op.GAS, 0x61DA)
                + Op.JUMPI(pc=0x119, condition=Op.CALL)
                + Op.STOP
                + Op.JUMPDEST
                + Op.PUSH2[0xBF]
                + Op.PUSH1[0x0]
                + Op.PUSH2[0xC9]
                + Op.JUMP(pc=Op.PUSH2[0x3D])
                + Op.JUMPDEST
                + Op.MSTORE(offset=0x0, value=Op.DUP1)
                + Op.RETURN(offset=0x0, size=0x20)
                + Op.JUMPDEST
                + Op.MSTORE(offset=0x0, value=Op.DUP1)
                + Op.RETURN(offset=0x0, size=0x20)
                + Op.JUMPDEST
                + Op.PUSH1[0x0]
                + Op.AND(
                    0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00,  # noqa: E501
                    Op.SLOAD(key=Op.DUP1),
                )
                + Op.SWAP2
                + Op.SWAP1
                + Op.SWAP2
                + Op.OR
                + Op.SWAP1
                + Op.DUP2
                + Op.SWAP1
                + Op.SSTORE
                + Op.PUSH1[0xFF]
                + Op.AND
                + Op.SWAP2
                + Op.SWAP1
                + Op.POP
                + Op.JUMP
                + Op.JUMPDEST
                + Op.POP
                + Op.POP
                + Op.JUMPI(
                    pc=0x19D,
                    condition=Op.ISZERO(
                        Op.EQ(0x2, Op.AND(0xFFFFFFFF, Op.MLOAD(offset=0x0))),
                    ),
                )
                + Op.JUMPDEST
                + Op.JUMPDEST
                + Op.POP
                + Op.POP
                + Op.SWAP1
                + Op.JUMP
                + Op.JUMPDEST
                + Op.POP
                + Op.POP
                + Op.JUMPI(
                    pc=0x194,
                    condition=Op.ISZERO(
                        Op.EQ(0x1, Op.AND(0xFFFFFFFF, Op.MLOAD(offset=0x0))),
                    ),
                )
                + Op.JUMPDEST
                + Op.CODECOPY(dest_offset=0x0, offset=0x1A7, size=0x45)
                + Op.CREATE(value=0x0, offset=0x0, size=0x45)
                + Op.SWAP1
                + Op.POP
                + Op.AND(0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF, Op.DUP1)
                + Op.PUSH4[0x81BDA09B]
                + Op.PUSH1[0x20]
                + Op.PUSH1[0x0]
                + Op.MSTORE(
                    offset=0x0,
                    value=Op.MUL(
                        0x100000000000000000000000000000000000000000000000000000000,  # noqa: E501
                        Op.DUP3,
                    ),
                )
                + Op.PUSH1[0x4]
                + Op.PUSH1[0x0]
                + Op.PUSH1[0x0]
                + Op.DUP7
                + Op.SUB(Op.GAS, 0x61DA)
                + Op.JUMPI(pc=Op.PUSH2[0xFF], condition=Op.CALL)
                + Op.STOP
                + Op.JUMPDEST
                + Op.PUSH1[0x0]
                + Op.SWAP3
                + Op.POP
                + Op.JUMP(pc=0x114)
                + Op.JUMPDEST
                + Op.PUSH1[0x0]
                + Op.SWAP3
                + Op.POP
                + Op.JUMP(pc=0x114)
                + Op.STOP
                + Op.PUSH1[0x39]
                + Op.CODECOPY(dest_offset=0x0, offset=0xC, size=Op.DUP1)
                + Op.PUSH1[0x0]
                + Op.RETURN
                + Op.STOP
                + Op.DIV(
                    Op.CALLDATALOAD(offset=0x0),
                    0x100000000000000000000000000000000000000000000000000000000,  # noqa: E501
                )
                + Op.JUMPI(pc=0x2D, condition=Op.EQ(Op.DUP2, 0x81BDA09B))
                + Op.STOP
                + Op.JUMPDEST
                + Op.PUSH1[0x2]
                + Op.PUSH1[0x0]
                + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2)
                + Op.PUSH1[0x20]
                + Op.SWAP1
                + Op.RETURN
                + Op.PUSH1[0x39]
                + Op.CODECOPY(dest_offset=0x0, offset=0xC, size=Op.DUP1)
                + Op.PUSH1[0x0]
                + Op.RETURN
                + Op.STOP
                + Op.DIV(
                    Op.CALLDATALOAD(offset=0x0),
                    0x100000000000000000000000000000000000000000000000000000000,  # noqa: E501
                )
                + Op.JUMPI(pc=0x2D, condition=Op.EQ(Op.DUP2, 0x81BDA09B))
                + Op.STOP
                + Op.JUMPDEST
                + Op.PUSH1[0x1]
                + Op.PUSH1[0x0]
                + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2)
                + Op.PUSH1[0x20]
                + Op.SWAP1
                + Op.RETURN
            ),
        ),
        Address("0x4ea88aa7836fe10b497e4bb4984ec5b4346bd767"): Account(
            code=(
                Op.DIV(
                    Op.CALLDATALOAD(offset=0x0),
                    0x100000000000000000000000000000000000000000000000000000000,  # noqa: E501
                )
                + Op.JUMPI(pc=0x2D, condition=Op.EQ(Op.DUP2, 0x81BDA09B))
                + Op.STOP
                + Op.JUMPDEST
                + Op.PUSH1[0x2]
                + Op.PUSH1[0x0]
                + Op.MSTORE(offset=Op.DUP2, value=Op.DUP2)
                + Op.PUSH1[0x20]
                + Op.SWAP1
                + Op.RETURN
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
