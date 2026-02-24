"""
Ported from:
tests/static/state_tests/stStaticCall/static_CheckOpcodes5Filler.json
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
    ["tests/static/state_tests/stStaticCall/static_CheckOpcodes5Filler.json"],
)
@pytest.mark.valid_from("Cancun")
@pytest.mark.parametrize(
    "tx_data_hex, tx_gas_limit, tx_value",
    [
        ("0000000000000000000000001000000000000000000000000000000000001400", 50000, 0),
        ("0000000000000000000000001000000000000000000000000000000000001400", 50000, 100),
        ("0000000000000000000000001000000000000000000000000000000000001400", 335000, 0),
        ("0000000000000000000000001000000000000000000000000000000000001400", 335000, 100),
        ("0000000000000000000000001000000000000000000000000000000000001300", 50000, 0),
        ("0000000000000000000000001000000000000000000000000000000000001300", 50000, 100),
        ("0000000000000000000000001000000000000000000000000000000000001300", 335000, 0),
        ("0000000000000000000000001000000000000000000000000000000000001300", 335000, 100),
        ("0000000000000000000000001000000000000000000000000000000000001500", 50000, 0),
        ("0000000000000000000000001000000000000000000000000000000000001500", 50000, 100),
        ("0000000000000000000000001000000000000000000000000000000000001500", 335000, 0),
        ("0000000000000000000000001000000000000000000000000000000000001500", 335000, 100),
        ("0000000000000000000000001000000000000000000000000000000000001600", 50000, 0),
        ("0000000000000000000000001000000000000000000000000000000000001600", 50000, 100),
        ("0000000000000000000000001000000000000000000000000000000000001600", 335000, 0),
        ("0000000000000000000000001000000000000000000000000000000000001600", 335000, 100),
        ("0000000000000000000000001000000000000000000000000000000000001700", 50000, 0),
        ("0000000000000000000000001000000000000000000000000000000000001700", 50000, 100),
        ("0000000000000000000000001000000000000000000000000000000000001700", 335000, 0),
        ("0000000000000000000000001000000000000000000000000000000000001700", 335000, 100),
    ],
    ids=['case0', 'case1', 'case2', 'case3', 'case4', 'case5', 'case6', 'case7', 'case8', 'case9', 'case10', 'case11', 'case12', 'case13', 'case14', 'case15', 'case16', 'case17', 'case18', 'case19'],
)
def test_static_check_opcodes5(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    tx_gas_limit: int,
    tx_value: int,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x1000000000000000000000000000000000001100")
    callee = Address("0x1000000000000000000000000000000000001000")
    callee_1 = Address("0x1000000000000000000000000000000000001200")
    callee_2 = Address("0x1000000000000000000000000000000000001300")
    callee_3 = Address("0x1000000000000000000000000000000000001400")
    callee_4 = Address("0x1000000000000000000000000000000000001500")
    callee_5 = Address("0x1000000000000000000000000000000000001600")
    callee_6 = Address("0x1000000000000000000000000000000000001700")
    callee_7 = Address("0x1000000000000000000000000000000000001800")
    callee_8 = Address("0x1000000000000000000000000000000000001900")
    callee_9 = Address("0x1000000000000000000000000000000000001a00")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.CALLDATALOAD + Op.PUSH2[0xc350] + Op.STATICCALL
        + Op.PUSH1[0x0] + Op.SSTORE + Op.STOP
    ),
    )
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.CALLDATALOAD + Op.PUSH3[0x3d090]
        + Op.CALL + Op.PUSH1[0x1] + Op.SSTORE + Op.STOP
    ),
    )
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.ORIGIN + Op.PUSH20[0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b] + Op.EQ
        + Op.PUSH1[0x22] + Op.JUMPI + Op.PUSH1[0x2] + Op.PUSH1[0x1] + Op.SSTORE
        + Op.PUSH1[0x28] + Op.JUMP + Op.JUMPDEST + Op.PUSH1[0x1] + Op.PUSH1[0x1]
        + Op.MSTORE + Op.JUMPDEST + Op.CALLER
        + Op.PUSH20[0x1000000000000000000000000000000000001000] + Op.EQ
        + Op.PUSH1[0x4b] + Op.JUMPI + Op.PUSH1[0x2] + Op.PUSH1[0x1] + Op.SSTORE
        + Op.PUSH1[0x51] + Op.JUMP + Op.JUMPDEST + Op.PUSH1[0x1] + Op.PUSH1[0x1]
        + Op.MSTORE + Op.JUMPDEST + Op.ADDRESS
        + Op.PUSH20[0x1000000000000000000000000000000000001200] + Op.EQ
        + Op.PUSH1[0x74] + Op.JUMPI + Op.PUSH1[0x2] + Op.PUSH1[0x1] + Op.SSTORE
        + Op.PUSH1[0x7a] + Op.JUMP + Op.JUMPDEST + Op.PUSH1[0x1] + Op.PUSH1[0x1]
        + Op.MSTORE + Op.JUMPDEST + Op.CALLVALUE + Op.PUSH1[0x0] + Op.EQ
        + Op.PUSH1[0x8a] + Op.JUMPI + Op.PUSH1[0x2] + Op.PUSH1[0x1] + Op.SSTORE
        + Op.PUSH1[0x90] + Op.JUMP + Op.JUMPDEST + Op.PUSH1[0x1] + Op.PUSH1[0x1]
        + Op.MSTORE + Op.JUMPDEST + Op.STOP
    ),
    )
    pre[callee_2] = Account(
        balance=10,
        nonce=0,
        code=(
        Op.PUSH20[0x1000000000000000000000000000000000001200] + Op.PUSH1[0x0]
        + Op.MSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x20] + Op.PUSH1[0x0]
        + Op.PUSH1[0xa] + Op.PUSH20[0x1000000000000000000000000000000000001000]
        + Op.PUSH3[0x186a0] + Op.CALL + Op.STOP
    ),
    )
    pre[callee_3] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH20[0x1000000000000000000000000000000000001200] + Op.PUSH1[0x0]
        + Op.MSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x20] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH20[0x1000000000000000000000000000000000001000]
        + Op.PUSH3[0x186a0] + Op.CALL + Op.STOP
    ),
    )
    pre[callee_4] = Account(
        balance=10,
        nonce=0,
        code=(
        Op.PUSH20[0x1000000000000000000000000000000000001800] + Op.PUSH1[0x0]
        + Op.MSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x20] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH20[0x1000000000000000000000000000000000001000]
        + Op.PUSH3[0x186a0] + Op.CALLCODE + Op.STOP
    ),
    )
    pre[callee_5] = Account(
        balance=10,
        nonce=0,
        code=(
        Op.PUSH20[0x1000000000000000000000000000000000001900] + Op.PUSH1[0x0]
        + Op.MSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x20] + Op.PUSH1[0x0]
        + Op.PUSH1[0x1] + Op.PUSH20[0x1000000000000000000000000000000000001000]
        + Op.PUSH3[0x186a0] + Op.CALLCODE + Op.STOP
    ),
    )
    pre[callee_6] = Account(
        balance=10,
        nonce=0,
        code=(
        Op.PUSH20[0x1000000000000000000000000000000000001a00] + Op.PUSH1[0x0]
        + Op.MSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x20] + Op.PUSH1[0x0]
        + Op.PUSH20[0x1000000000000000000000000000000000001000] + Op.PUSH3[0x186a0]
        + Op.DELEGATECALL + Op.STOP
    ),
    )
    pre[callee_7] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.ORIGIN + Op.PUSH20[0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b] + Op.EQ
        + Op.PUSH1[0x22] + Op.JUMPI + Op.PUSH1[0x2] + Op.PUSH1[0x1] + Op.SSTORE
        + Op.PUSH1[0x28] + Op.JUMP + Op.JUMPDEST + Op.PUSH1[0x1] + Op.PUSH1[0x1]
        + Op.MSTORE + Op.JUMPDEST + Op.CALLER
        + Op.PUSH20[0x1000000000000000000000000000000000001500] + Op.EQ
        + Op.PUSH1[0x4b] + Op.JUMPI + Op.PUSH1[0x2] + Op.PUSH1[0x1] + Op.SSTORE
        + Op.PUSH1[0x51] + Op.JUMP + Op.JUMPDEST + Op.PUSH1[0x1] + Op.PUSH1[0x1]
        + Op.MSTORE + Op.JUMPDEST + Op.ADDRESS
        + Op.PUSH20[0x1000000000000000000000000000000000001800] + Op.EQ
        + Op.PUSH1[0x74] + Op.JUMPI + Op.PUSH1[0x2] + Op.PUSH1[0x1] + Op.SSTORE
        + Op.PUSH1[0x7a] + Op.JUMP + Op.JUMPDEST + Op.PUSH1[0x1] + Op.PUSH1[0x1]
        + Op.MSTORE + Op.JUMPDEST + Op.CALLVALUE + Op.PUSH1[0x0] + Op.EQ
        + Op.PUSH1[0x8a] + Op.JUMPI + Op.PUSH1[0x2] + Op.PUSH1[0x1] + Op.SSTORE
        + Op.PUSH1[0x90] + Op.JUMP + Op.JUMPDEST + Op.PUSH1[0x1] + Op.PUSH1[0x1]
        + Op.MSTORE + Op.JUMPDEST + Op.STOP
    ),
    )
    pre[callee_8] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.ORIGIN + Op.PUSH20[0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b] + Op.EQ
        + Op.PUSH1[0x22] + Op.JUMPI + Op.PUSH1[0x2] + Op.PUSH1[0x1] + Op.SSTORE
        + Op.PUSH1[0x28] + Op.JUMP + Op.JUMPDEST + Op.PUSH1[0x1] + Op.PUSH1[0x1]
        + Op.MSTORE + Op.JUMPDEST + Op.CALLER
        + Op.PUSH20[0x1000000000000000000000000000000000001600] + Op.EQ
        + Op.PUSH1[0x4b] + Op.JUMPI + Op.PUSH1[0x2] + Op.PUSH1[0x1] + Op.SSTORE
        + Op.PUSH1[0x51] + Op.JUMP + Op.JUMPDEST + Op.PUSH1[0x1] + Op.PUSH1[0x1]
        + Op.MSTORE + Op.JUMPDEST + Op.ADDRESS
        + Op.PUSH20[0x1000000000000000000000000000000000001900] + Op.EQ
        + Op.PUSH1[0x74] + Op.JUMPI + Op.PUSH1[0x2] + Op.PUSH1[0x1] + Op.SSTORE
        + Op.PUSH1[0x7a] + Op.JUMP + Op.JUMPDEST + Op.PUSH1[0x1] + Op.PUSH1[0x1]
        + Op.MSTORE + Op.JUMPDEST + Op.CALLVALUE + Op.PUSH1[0x0] + Op.EQ
        + Op.PUSH1[0x8a] + Op.JUMPI + Op.PUSH1[0x2] + Op.PUSH1[0x1] + Op.SSTORE
        + Op.PUSH1[0x90] + Op.JUMP + Op.JUMPDEST + Op.PUSH1[0x1] + Op.PUSH1[0x1]
        + Op.MSTORE + Op.JUMPDEST + Op.STOP
    ),
    )
    pre[callee_9] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.ORIGIN + Op.PUSH20[0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b] + Op.EQ
        + Op.PUSH1[0x22] + Op.JUMPI + Op.PUSH1[0x2] + Op.PUSH1[0x1] + Op.SSTORE
        + Op.PUSH1[0x28] + Op.JUMP + Op.JUMPDEST + Op.PUSH1[0x1] + Op.PUSH1[0x1]
        + Op.MSTORE + Op.JUMPDEST + Op.CALLER
        + Op.PUSH20[0x1000000000000000000000000000000000001700] + Op.EQ
        + Op.PUSH1[0x4b] + Op.JUMPI + Op.PUSH1[0x2] + Op.PUSH1[0x1] + Op.SSTORE
        + Op.PUSH1[0x51] + Op.JUMP + Op.JUMPDEST + Op.PUSH1[0x1] + Op.PUSH1[0x1]
        + Op.MSTORE + Op.JUMPDEST + Op.ADDRESS
        + Op.PUSH20[0x1000000000000000000000000000000000001a00] + Op.EQ
        + Op.PUSH1[0x74] + Op.JUMPI + Op.PUSH1[0x2] + Op.PUSH1[0x1] + Op.SSTORE
        + Op.PUSH1[0x7a] + Op.JUMP + Op.JUMPDEST + Op.PUSH1[0x1] + Op.PUSH1[0x1]
        + Op.MSTORE + Op.JUMPDEST + Op.CALLVALUE + Op.PUSH1[0x0] + Op.EQ
        + Op.PUSH1[0x8a] + Op.JUMPI + Op.PUSH1[0x2] + Op.PUSH1[0x1] + Op.SSTORE
        + Op.PUSH1[0x90] + Op.JUMP + Op.JUMPDEST + Op.PUSH1[0x1] + Op.PUSH1[0x1]
        + Op.MSTORE + Op.JUMPDEST + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0xe8d4a51000, nonce=0)

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=tx_data,
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=tx_value,
    )

    post = {}

    state_test(env=env, pre=pre, post=post, tx=tx)
