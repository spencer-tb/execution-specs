"""
Ported from:
tests/static/state_tests/stSolidityTest/TestOverflowFiller.json
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
    ["tests/static/state_tests/stSolidityTest/TestOverflowFiller.json"],
)
@pytest.mark.valid_from("Cancun")
def test_test_overflow(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x1000000000000000000000000000000000001000")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[contract] = Account(
        balance=0x186a0,
        nonce=0,
        code=(
        Op.PUSH1[0x0] + Op.CALLDATALOAD
        + Op.PUSH29[0x100000000000000000000000000000000000000000000000000000000]
        + Op.SWAP1 + Op.DIV + Op.DUP1 + Op.PUSH4[0x8040cac4] + Op.EQ + Op.PUSH2[0x3a]
        + Op.JUMPI + Op.DUP1 + Op.PUSH4[0xc0406226] + Op.EQ + Op.PUSH2[0x4c]
        + Op.JUMPI + Op.STOP + Op.JUMPDEST + Op.PUSH2[0x42] + Op.PUSH2[0x99] + Op.JUMP
        + Op.JUMPDEST + Op.DUP1 + Op.PUSH1[0x0] + Op.MSTORE + Op.PUSH1[0x20]
        + Op.PUSH1[0x0] + Op.RETURN + Op.JUMPDEST + Op.PUSH2[0x54] + Op.PUSH2[0x5e]
        + Op.JUMP + Op.JUMPDEST + Op.DUP1 + Op.PUSH1[0x0] + Op.MSTORE + Op.PUSH1[0x20]
        + Op.PUSH1[0x0] + Op.RETURN + Op.JUMPDEST + Op.PUSH1[0x0] + Op.PUSH2[0x68]
        + Op.PUSH2[0x99] + Op.JUMP + Op.JUMPDEST + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH2[0x100] + Op.EXP + Op.DUP2 + Op.SLOAD + Op.DUP2 + Op.PUSH1[0xff]
        + Op.MUL + Op.NOT + Op.AND + Op.SWAP1 + Op.DUP4 + Op.MUL + Op.OR + Op.SWAP1
        + Op.SSTORE + Op.POP + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.SWAP1 + Op.SLOAD
        + Op.SWAP1 + Op.PUSH2[0x100] + Op.EXP + Op.SWAP1 + Op.DIV + Op.PUSH1[0xff]
        + Op.AND + Op.SWAP1 + Op.POP + Op.PUSH2[0x96] + Op.JUMP + Op.JUMPDEST
        + Op.SWAP1 + Op.JUMP + Op.JUMPDEST + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x1] + Op.SWAP4 + Op.POP + Op.DUP4
        + Op.POP
        + Op.PUSH32[0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff]
        + Op.SWAP3 + Op.POP + Op.PUSH1[0x0] + Op.PUSH1[0x1] + Op.DUP5 + Op.ADD + Op.EQ
        + Op.ISZERO + Op.PUSH2[0xdb] + Op.JUMPI + Op.PUSH2[0xe4] + Op.JUMP
        + Op.JUMPDEST + Op.PUSH1[0x0] + Op.SWAP4 + Op.POP + Op.PUSH2[0x13b] + Op.JUMP
        + Op.JUMPDEST + Op.PUSH4[0xffffffff] + Op.SWAP2 + Op.POP + Op.PUSH1[0x0]
        + Op.PUSH1[0x1] + Op.DUP4 + Op.ADD + Op.PUSH4[0xffffffff] + Op.AND + Op.EQ
        + Op.ISZERO + Op.PUSH2[0x102] + Op.JUMPI + Op.PUSH2[0x10b] + Op.JUMP
        + Op.JUMPDEST + Op.PUSH1[0x0] + Op.SWAP4 + Op.POP + Op.PUSH2[0x13b] + Op.JUMP
        + Op.JUMPDEST + Op.PUSH8[0xffffffffffffffff] + Op.SWAP1 + Op.POP
        + Op.PUSH1[0x0] + Op.PUSH1[0x1] + Op.DUP3 + Op.ADD
        + Op.PUSH8[0xffffffffffffffff] + Op.AND + Op.EQ + Op.ISZERO + Op.PUSH2[0x131]
        + Op.JUMPI + Op.PUSH2[0x13a] + Op.JUMP + Op.JUMPDEST + Op.PUSH1[0x0]
        + Op.SWAP4 + Op.POP + Op.PUSH2[0x13b] + Op.JUMP + Op.JUMPDEST + Op.JUMPDEST
        + Op.POP + Op.POP + Op.POP + Op.SWAP1 + Op.JUMP
    ),
    )
    pre[sender] = Account(balance=0x12a05f200, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=bytes.fromhex("c0406226"),
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {}

    state_test(env=env, pre=pre, post=post, tx=tx)
