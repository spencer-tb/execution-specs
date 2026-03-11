"""
Ori Pomerantz qbzzt1@gmail.com.

Ported from:
tests/static/state_tests/VMTests/vmArithmeticTest/arithFiller.yml
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
    ["tests/static/state_tests/VMTests/vmArithmeticTest/arithFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_arith(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Ori Pomerantz qbzzt1@gmail.com."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x56724d001b4f2a2888a81971a64aad37cd43f881")
    contract = Address("0x14814d06e93efb1102a15d5881432c9ff6c91362")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000,
    )

    # Source: raw bytecode
    pre[contract] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.PUSH1[0x1]
            + Op.PUSH1[0x1]
            + Op.SWAP1
            + Op.ADD(0x5, Op.MUL(0x7, Op.ADD))
            + Op.PUSH1[0x2]
            + Op.SWAP1
            + Op.DIV
            + Op.PUSH1[0x4]
            + Op.SWAP1
            + Op.PUSH1[0x21]
            + Op.SWAP1
            + Op.MUL(0x3, Op.ADD(0x17, Op.SDIV))
            + Op.PUSH1[0x5]
            + Op.SWAP1
            + Op.SUB(0x3, Op.SMOD)
            + Op.SSTORE(key=0x0, value=Op.EXP(0x11, 0x9))
            + Op.RETURN(offset=0x0, size=0x8)
        ),
    )
    pre[sender] = Account(balance=0xBA1A9CE0BA1A9CE, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x40ac0fc28c27e961ee46ec43355a094de205856edbd4654cf2577c2608d4ec1e"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex("00"),
        gas_limit=16777216,
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = {
        contract: Account(
            storage={0: 0x1B9C636491},
            code=(
                Op.PUSH1[0x1]
                + Op.PUSH1[0x1]
                + Op.SWAP1
                + Op.ADD(0x5, Op.MUL(0x7, Op.ADD))
                + Op.PUSH1[0x2]
                + Op.SWAP1
                + Op.DIV
                + Op.PUSH1[0x4]
                + Op.SWAP1
                + Op.PUSH1[0x21]
                + Op.SWAP1
                + Op.MUL(0x3, Op.ADD(0x17, Op.SDIV))
                + Op.PUSH1[0x5]
                + Op.SWAP1
                + Op.SUB(0x3, Op.SMOD)
                + Op.SSTORE(key=0x0, value=Op.EXP(0x11, 0x9))
                + Op.RETURN(offset=0x0, size=0x8)
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
