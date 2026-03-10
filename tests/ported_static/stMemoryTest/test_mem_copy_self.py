"""
Ori Pomerantz qbzzt1@gmail.com.

Ported from:
tests/static/state_tests/stMemoryTest/memCopySelfFiller.yml
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
    ["tests/static/state_tests/stMemoryTest/memCopySelfFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_mem_copy_self(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Ori Pomerantz qbzzt1@gmail.com."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x485fd0fd5c1d0409d2b772a66e98a6ac867b9d8b")
    contract = Address("0xb595300ac049b84c5277c7ca68a96d74ae377b85")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000,
    )

    pre[sender] = Account(balance=0xBA1A9CE0BA1A9CE, nonce=1)
    pre[contract] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=(
            Op.PUSH1[0x4]
            + Op.PUSH1[0x0]
            + Op.JUMPDEST
            + Op.JUMPI(pc=0x30, condition=Op.LT(Op.DUP2, 0xF))
            + Op.PUSH1[0xA]
            + Op.PUSH1[0x2]
            + Op.DUP2
            + Op.PUSH1[0x0]
            + Op.DUP1
            + Op.DUP7
            + Op.SSTORE(key=Op.DUP3, value=Op.MLOAD(offset=Op.DUP2))
            + Op.GAS
            + Op.POP(Op.CALL)
            + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
            + Op.RETURNDATACOPY(dest_offset=0x20, offset=0x0, size=0xA)
            + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x20))
            + Op.STOP
            + Op.JUMPDEST
            + Op.DUP1
            + Op.PUSH1[0x11]
            + Op.PUSH1[0x1]
            + Op.DUP1
            + Op.SWAP4
            + Op.ADD
            + Op.MSTORE8(offset=Op.DUP2, value=Op.MUL)
            + Op.ADD
            + Op.JUMP(pc=0x4)
        ),
        storage={0x0: 0x60A7},
    )

    tx = Transaction(
        secret_key=Hash(
            "0x48dc5a9f099caaaa557742ca3a990a94be45b9969126a1bc74e5e8be5a2b5b47"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=16777216,
        gas_price=10,
        nonce=1,
        value=0,
    )

    post = {
        contract: Account(
            storage={
                0: 0x112233445566778899AABBCCDDEEFF0000000000000000000000000000000000,  # noqa: E501
                1: 0x1122112233445566778899AADDEEFF0000000000000000000000000000000000,  # noqa: E501
                2: 0x112233445566778899AA00000000000000000000000000000000000000000000,  # noqa: E501
            },
            code=(
                Op.PUSH1[0x4]
                + Op.PUSH1[0x0]
                + Op.JUMPDEST
                + Op.JUMPI(pc=0x30, condition=Op.LT(Op.DUP2, 0xF))
                + Op.PUSH1[0xA]
                + Op.PUSH1[0x2]
                + Op.DUP2
                + Op.PUSH1[0x0]
                + Op.DUP1
                + Op.DUP7
                + Op.SSTORE(key=Op.DUP3, value=Op.MLOAD(offset=Op.DUP2))
                + Op.GAS
                + Op.POP(Op.CALL)
                + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                + Op.RETURNDATACOPY(dest_offset=0x20, offset=0x0, size=0xA)
                + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x20))
                + Op.STOP
                + Op.JUMPDEST
                + Op.DUP1
                + Op.PUSH1[0x11]
                + Op.PUSH1[0x1]
                + Op.DUP1
                + Op.SWAP4
                + Op.ADD
                + Op.MSTORE8(offset=Op.DUP2, value=Op.MUL)
                + Op.ADD
                + Op.JUMP(pc=0x4)
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
