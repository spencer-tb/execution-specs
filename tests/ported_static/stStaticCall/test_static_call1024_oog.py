"""
Ported from:
tests/static/state_tests/stStaticCall/static_Call1024OOGFiller.json
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
    ["tests/static/state_tests/stStaticCall/static_Call1024OOGFiller.json"],
)
@pytest.mark.valid_from("Cancun")
@pytest.mark.parametrize(
    "tx_data_hex",
    [
        "0000000000000000000000001000000000000000000000000000000000001100",
        "0000000000000000000000001000000000000000000000000000000000001000",
    ],
    ids=['case0', 'case1'],
)
def test_static_call1024_oog(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    sender = Address("0x8a0a19589531694250d570040a0c4b74576919b8")
    contract = Address("0x1000000000000000000000000000000000001200")
    callee = Address("0x1000000000000000000000000000000000001000")
    callee_1 = Address("0x1000000000000000000000000000000000001100")
    callee_2 = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[callee] = Account(
        balance=1024,
        nonce=0,
        code=(
        Op.PUSH1[0x1] + Op.PUSH1[0x0] + Op.MLOAD + Op.ADD + Op.PUSH1[0x0]
        + Op.MSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH20[0x1000000000000000000000000000000000001000] + Op.PUSH2[0x401]
        + Op.PUSH1[0x0] + Op.MLOAD + Op.DIV + Op.PUSH1[0x1] + Op.SUB
        + Op.PUSH2[0x2710] + Op.GAS + Op.SUB + Op.MUL + Op.STATICCALL + Op.POP
        + Op.PUSH2[0x3e8] + Op.PUSH1[0x0] + Op.MLOAD + Op.MUL + Op.PUSH1[0x1] + Op.ADD
        + Op.PUSH1[0x20] + Op.MSTORE + Op.STOP
    ),
    )
    pre[callee_1] = Account(
        balance=1024,
        nonce=0,
        code=(
        Op.PUSH1[0x1] + Op.PUSH1[0x0] + Op.SLOAD + Op.ADD + Op.PUSH1[0x0]
        + Op.SSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH20[0x1000000000000000000000000000000000001100] + Op.PUSH2[0x401]
        + Op.PUSH1[0x0] + Op.SLOAD + Op.DIV + Op.PUSH1[0x1] + Op.SUB
        + Op.PUSH2[0x2710] + Op.GAS + Op.SUB + Op.MUL + Op.STATICCALL + Op.PUSH1[0x1]
        + Op.SSTORE + Op.PUSH2[0x3e8] + Op.PUSH1[0x0] + Op.SLOAD + Op.MUL
        + Op.PUSH1[0x1] + Op.ADD + Op.PUSH1[0x2] + Op.SSTORE + Op.STOP
    ),
    )
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.CALLVALUE
        + Op.PUSH1[0x0] + Op.CALLDATALOAD + Op.GAS + Op.CALL + Op.PUSH1[0x0]
        + Op.SSTORE + Op.PUSH1[0x1] + Op.PUSH1[0x1] + Op.SSTORE + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0xffffffffffffffffffffffffffffffff, nonce=0)
    pre[callee_2] = Account(balance=7000, nonce=0)

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x9e7645d0cfd9c3a04eb7a9db59a4eb7d359f2e75c9164a9d6b9a7d54e1b6a36f"
        ),
        to=contract,
        data=tx_data,
        gas_limit=15720826,
        gas_price=10,
        nonce=0,
        value=10,
    )

    post = {}

    state_test(env=env, pre=pre, post=post, tx=tx)
