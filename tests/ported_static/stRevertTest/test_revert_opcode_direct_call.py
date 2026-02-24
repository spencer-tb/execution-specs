"""
Ported from:
tests/static/state_tests/stRevertTest/RevertOpcodeDirectCallFiller.json
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
    ["tests/static/state_tests/stRevertTest/RevertOpcodeDirectCallFiller.json"],
)
@pytest.mark.valid_from("Cancun")
@pytest.mark.parametrize(
    "tx_gas_limit",
    [
        460000,
        62912,
    ],
    ids=['case0', 'case1'],
)
def test_revert_opcode_direct_call(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x1000000000000000000000000000000000001100")
    callee = Address("0x1000000000000000000000000000000000001000")
    callee_1 = Address("0x1000000000000000000000000000000000001200")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[callee] = Account(
        balance=1,
        nonce=0,
        code=(
        Op.PUSH1[0xc] + Op.PUSH1[0x1] + Op.SSTORE + Op.PUSH1[0x1] + Op.PUSH1[0x0]
        + Op.REVERT + Op.PUSH1[0xd] + Op.PUSH1[0x3] + Op.SSTORE + Op.STOP
    ),
    )
    pre[contract] = Account(
        balance=1,
        nonce=0,
        code=(
        Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH20[0x1000000000000000000000000000000000001000]
        + Op.PUSH2[0xc350] + Op.CALL + Op.PUSH1[0x0] + Op.SSTORE + Op.PUSH1[0xe]
        + Op.PUSH1[0x2] + Op.SSTORE + Op.STOP
    ),
    )
    pre[callee_1] = Account(
        balance=1,
        nonce=0,
        code=(
        Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.CALLDATALOAD + Op.PUSH2[0xea60] + Op.CALL
        + Op.PUSH1[0xa] + Op.SSTORE + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0xe8d4a51000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=bytes.fromhex("0000000000000000000000001000000000000000000000000000000000001100"),
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {}

    state_test(env=env, pre=pre, post=post, tx=tx)
