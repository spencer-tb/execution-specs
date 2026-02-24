"""
Ported from:
tests/static/state_tests/stSolidityTest/CallLowLevelCreatesSolidityFiller.json
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
    ["tests/static/state_tests/stSolidityTest/CallLowLevelCreatesSolidityFiller.json"],
)
@pytest.mark.valid_from("Cancun")
def test_call_low_level_creates_solidity(
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
        gas_limit=100000000,
    )

    pre[contract] = Account(
        balance=0x186a0,
        nonce=0,
        code=(
        Op.PUSH1[0x0] + Op.CALLDATALOAD + Op.PUSH1[0xe0] + Op.PUSH1[0x2] + Op.EXP
        + Op.SWAP1 + Op.DIV + Op.DUP1 + Op.PUSH4[0x30debb42] + Op.EQ + Op.PUSH2[0x21]
        + Op.JUMPI + Op.DUP1 + Op.PUSH4[0xc0406226] + Op.EQ + Op.PUSH2[0x32]
        + Op.JUMPI + Op.STOP + Op.JUMPDEST + Op.PUSH2[0x2c] + Op.PUSH1[0x4]
        + Op.CALLDATALOAD + Op.PUSH2[0xc7] + Op.JUMP + Op.JUMPDEST + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.RETURN + Op.JUMPDEST + Op.PUSH2[0x3a] + Op.PUSH2[0x44]
        + Op.JUMP + Op.JUMPDEST + Op.DUP1 + Op.PUSH1[0x0] + Op.MSTORE + Op.PUSH1[0x20]
        + Op.PUSH1[0x0] + Op.RETURN + Op.JUMPDEST + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x1] + Op.PUSH1[0x0] + Op.DUP2 + Op.SWAP1 + Op.SSTORE + Op.POP
        + Op.PUSH20[0x1000000000000000000000000000000000001000] + Op.PUSH1[0x1]
        + Op.DUP2 + Op.SWAP1 + Op.SSTORE + Op.POP + Op.PUSH1[0x6a] + Op.PUSH2[0xd2]
        + Op.PUSH1[0x0] + Op.CODECOPY + Op.PUSH1[0x6a] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.CREATE + Op.SWAP1 + Op.POP + Op.DUP1 + Op.PUSH1[0x1] + Op.PUSH1[0xa0]
        + Op.PUSH1[0x2] + Op.EXP + Op.SUB + Op.AND + Op.PUSH4[0x19ab453c]
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.DUP3 + Op.PUSH1[0xe0] + Op.PUSH1[0x2]
        + Op.EXP + Op.MUL + Op.PUSH1[0x0] + Op.MSTORE + Op.PUSH1[0x4] + Op.PUSH1[0x1]
        + Op.SLOAD + Op.PUSH1[0x1] + Op.PUSH1[0xa0] + Op.PUSH1[0x2] + Op.EXP + Op.SUB
        + Op.AND + Op.DUP2 + Op.MSTORE + Op.PUSH1[0x20] + Op.ADD + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.DUP7 + Op.PUSH1[0x32] + Op.GAS + Op.SUB + Op.CALL
        + Op.PUSH2[0xbc] + Op.JUMPI + Op.STOP + Op.JUMPDEST + Op.POP + Op.POP
        + Op.PUSH1[0x0] + Op.SLOAD + Op.SWAP2 + Op.POP + Op.POP + Op.SWAP1 + Op.JUMP
        + Op.JUMPDEST + Op.DUP1 + Op.PUSH1[0x0] + Op.DUP2 + Op.SWAP1 + Op.SSTORE
        + Op.POP + Op.POP + Op.JUMP + Op.STOP + Op.PUSH1[0x5e] + Op.DUP1
        + Op.PUSH1[0xc] + Op.PUSH1[0x0] + Op.CODECOPY + Op.PUSH1[0x0] + Op.RETURN
        + Op.STOP + Op.PUSH1[0x0] + Op.CALLDATALOAD + Op.PUSH1[0xe0] + Op.PUSH1[0x2]
        + Op.EXP + Op.SWAP1 + Op.DIV + Op.DUP1 + Op.PUSH4[0x19ab453c] + Op.EQ
        + Op.PUSH1[0x15] + Op.JUMPI + Op.STOP + Op.JUMPDEST + Op.PUSH1[0x1e]
        + Op.PUSH1[0x4] + Op.CALLDATALOAD + Op.PUSH1[0x24] + Op.JUMP + Op.JUMPDEST
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.RETURN + Op.JUMPDEST + Op.DUP1
        + Op.PUSH1[0x1] + Op.PUSH1[0xa0] + Op.PUSH1[0x2] + Op.EXP + Op.SUB + Op.AND
        + Op.PUSH4[0x30debb42] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.DUP3
        + Op.PUSH1[0xe0] + Op.PUSH1[0x2] + Op.EXP + Op.MUL + Op.PUSH1[0x0] + Op.MSTORE
        + Op.PUSH1[0x4] + Op.PUSH1[0xe1] + Op.DUP2 + Op.MSTORE + Op.PUSH1[0x20]
        + Op.ADD + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.DUP7 + Op.PUSH1[0x32] + Op.GAS
        + Op.SUB + Op.CALL + Op.PUSH1[0x59] + Op.JUMPI + Op.STOP + Op.JUMPDEST
        + Op.POP + Op.POP + Op.POP + Op.JUMP
    ),
    )
    pre[sender] = Account(balance=0x5f5e100, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=bytes.fromhex("c0406226"),
        gas_limit=350000,
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = {}

    state_test(env=env, pre=pre, post=post, tx=tx)
