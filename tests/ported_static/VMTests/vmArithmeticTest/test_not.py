"""
Ori Pomerantz qbzzt1@gmail.com

Ported from:
tests/static/state_tests/VMTests/vmArithmeticTest/notFiller.yml
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
    ["tests/static/state_tests/VMTests/vmArithmeticTest/notFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_not(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Ori Pomerantz qbzzt1@gmail.com."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xcccccccccccccccccccccccccccccccccccccccc")
    callee = Address("0x0000000000000000000000000000000000001000")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000,
    )

    pre[callee] = Account(
        balance=0xba1a9ce0ba1a9ce,
        nonce=0,
        code=Op.SSTORE(key=0x0, value=Op.NOT(0x123456789abcdef)) + Op.STOP,
    )
    pre[sender] = Account(balance=0xba1a9ce0ba1a9ce, nonce=0)
    pre[contract] = Account(
        balance=0xba1a9ce0ba1a9ce,
        nonce=0,
        code=(
        Op.CALL(gas=0xffffff, address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)), value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)
        + Op.STOP
    ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=bytes.fromhex("693c61390000000000000000000000000000000000000000000000000000000000000000"),
        gas_limit=16777216,
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = {
        callee: Account(
            storage={0: 0xfffffffffffffffffffffffffffffffffffffffffffffffffedcba9876543210},
            code=Op.SSTORE(key=0x0, value=Op.NOT(0x123456789abcdef)) + Op.STOP,
        ),
        contract: Account(
            code=Op.CALL(gas=0xffffff, address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)), value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0) + Op.STOP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
