"""
SELFBALANCE tests inside CALL, DELEGATECALL, and CALLCODE

Ported from:
tests/static/state_tests/stSelfBalance/selfBalanceCallTypesFiller.json
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
    ["tests/static/state_tests/stSelfBalance/selfBalanceCallTypesFiller.json"],
)
@pytest.mark.valid_from("Cancun")
@pytest.mark.parametrize(
    "tx_data_hex",
    [
        "0000000000000000000000000000000000000000000000000000000000000001",
        "0000000000000000000000000000000000000000000000000000000000000002",
        "0000000000000000000000000000000000000000000000000000000000000003",
    ],
    ids=['case0', 'case1', 'case2'],
)
def test_self_balance_call_types(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
) -> None:
    """SELFBALANCE tests inside CALL, DELEGATECALL, and CALLCODE."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x1000000000000000000000000000000000001400")
    callee = Address("0x1000000000000000000000000000000000001000")
    callee_1 = Address("0x1000000000000000000000000000000000001100")
    callee_2 = Address("0x1000000000000000000000000000000000001200")
    callee_3 = Address("0x1000000000000000000000000000000000001300")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000000,
    )

    pre[callee] = Account(
        balance=4864,
        nonce=0,
        code=(
        Op.SELFBALANCE + Op.DUP1 + Op.PUSH1[0x41] + Op.SSTORE + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x1]
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.CALL + Op.POP + Op.SELFBALANCE + Op.DUP1
        + Op.PUSH1[0x42] + Op.SSTORE + Op.SWAP1 + Op.SUB + Op.PUSH1[0x43] + Op.SSTORE
        + Op.STOP
    ),
    )
    pre[callee_1] = Account(
        balance=4608,
        nonce=0,
        code=(
        Op.GAS + Op.SELFBALANCE + Op.GAS + Op.SWAP1 + Op.POP + Op.SWAP1 + Op.SUB
        + Op.PUSH1[0x2] + Op.SWAP1 + Op.SUB + Op.PUSH1[0x31] + Op.SSTORE + Op.STOP
    ),
    )
    pre[callee_2] = Account(
        balance=4352,
        nonce=0,
        code=Op.SELFBALANCE + Op.PUSH1[0x21] + Op.SSTORE + Op.STOP,
    )
    pre[callee_3] = Account(
        balance=4096,
        nonce=0,
        code=(
        Op.ADDRESS + Op.BALANCE + Op.SELFBALANCE + Op.EQ + Op.PUSH1[0x11]
        + Op.SSTORE + Op.STOP
    ),
    )
    pre[contract] = Account(
        balance=8192,
        nonce=0,
        code=(
        Op.PUSH1[0x0] + Op.PUSH1[0x80] + Op.MSTORE + Op.JUMPDEST + Op.PUSH1[0x80]
        + Op.MLOAD + Op.SLOAD + Op.ISZERO + Op.PUSH1[0x75] + Op.JUMPI + Op.PUSH1[0x0]
        + Op.CALLDATALOAD + Op.PUSH1[0x1] + Op.EQ + Op.ISZERO + Op.PUSH1[0x2c]
        + Op.JUMPI + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH1[0x80] + Op.MLOAD + Op.SLOAD + Op.PUSH1[0x15]
        + Op.GAS + Op.SUB + Op.CALL + Op.POP + Op.JUMPDEST + Op.PUSH1[0x0]
        + Op.CALLDATALOAD + Op.PUSH1[0x2] + Op.EQ + Op.ISZERO + Op.PUSH1[0x49]
        + Op.JUMPI + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x80] + Op.MLOAD + Op.SLOAD + Op.PUSH1[0x15] + Op.GAS + Op.SUB
        + Op.DELEGATECALL + Op.POP + Op.JUMPDEST + Op.PUSH1[0x0] + Op.CALLDATALOAD
        + Op.PUSH1[0x3] + Op.EQ + Op.ISZERO + Op.PUSH1[0x68] + Op.JUMPI
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH1[0x80] + Op.MLOAD + Op.SLOAD + Op.PUSH1[0x15]
        + Op.GAS + Op.SUB + Op.CALLCODE + Op.POP + Op.JUMPDEST + Op.PUSH1[0x1]
        + Op.PUSH1[0x80] + Op.MLOAD + Op.ADD + Op.PUSH1[0x80] + Op.MSTORE
        + Op.PUSH1[0x5] + Op.JUMP + Op.JUMPDEST + Op.STOP
    ),
        storage={0x0: 0x1000000000000000000000000000000000001300, 0x1: 0x1000000000000000000000000000000000001200, 0x2: 0x1000000000000000000000000000000000001100, 0x3: 0x1000000000000000000000000000000000001000},
    )
    pre[sender] = Account(balance=0x3635c9adc5dea00000, nonce=0)

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=tx_data,
        gas_limit=1000000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {}

    state_test(env=env, pre=pre, post=post, tx=tx)
