"""
Ported from:
tests/static/state_tests/stCreateTest/CreateOOGFromCallRefundsFiller.yml
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
    ["tests/static/state_tests/stCreateTest/CreateOOGFromCallRefundsFiller.yml"],
)
@pytest.mark.valid_from("Cancun")
@pytest.mark.parametrize(
    "tx_data_hex",
    [
        "693c6139000000000000000000000000000000000000000000000000000000000000006a",
        "693c6139000000000000000000000000000000000000000000000000000000000000006c",
        "693c6139000000000000000000000000000000000000000000000000000000000000006b",
        "693c6139000000000000000000000000000000000000000000000000000000000000008a",
        "693c6139000000000000000000000000000000000000000000000000000000000000008c",
        "693c6139000000000000000000000000000000000000000000000000000000000000008b",
        "693c6139000000000000000000000000000000000000000000000000000000000000007a",
        "693c6139000000000000000000000000000000000000000000000000000000000000007c",
        "693c6139000000000000000000000000000000000000000000000000000000000000007b",
        "693c6139000000000000000000000000000000000000000000000000000000000000002a",
        "693c6139000000000000000000000000000000000000000000000000000000000000003a",
        "693c6139000000000000000000000000000000000000000000000000000000000000004a",
        "693c6139000000000000000000000000000000000000000000000000000000000000001a",
        "693c6139000000000000000000000000000000000000000000000000000000000000001c",
        "693c6139000000000000000000000000000000000000000000000000000000000000002b",
        "693c6139000000000000000000000000000000000000000000000000000000000000002c",
        "693c6139000000000000000000000000000000000000000000000000000000000000003b",
        "693c6139000000000000000000000000000000000000000000000000000000000000003c",
        "693c6139000000000000000000000000000000000000000000000000000000000000004b",
        "693c6139000000000000000000000000000000000000000000000000000000000000004c",
        "693c6139000000000000000000000000000000000000000000000000000000000000001b",
        "693c6139000000000000000000000000000000000000000000000000000000000000005a",
        "693c6139000000000000000000000000000000000000000000000000000000000000005c",
        "693c6139000000000000000000000000000000000000000000000000000000000000005b",
    ],
    ids=['case0', 'case1', 'case2', 'case3', 'case4', 'case5', 'case6', 'case7', 'case8', 'case9', 'case10', 'case11', 'case12', 'case13', 'case14', 'case15', 'case16', 'case17', 'case18', 'case19', 'case20', 'case21', 'case22', 'case23'],
)
def test_create_oog_from_call_refunds(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    callee = Address("0x000000000000000000000000000000000000001a")
    callee_1 = Address("0x000000000000000000000000000000000000001b")
    callee_2 = Address("0x000000000000000000000000000000000000001c")
    callee_3 = Address("0x000000000000000000000000000000000000002a")
    callee_4 = Address("0x000000000000000000000000000000000000002b")
    callee_5 = Address("0x000000000000000000000000000000000000002c")
    callee_6 = Address("0x000000000000000000000000000000000000003a")
    callee_7 = Address("0x000000000000000000000000000000000000003b")
    callee_8 = Address("0x000000000000000000000000000000000000003c")
    callee_9 = Address("0x000000000000000000000000000000000000004a")
    callee_10 = Address("0x000000000000000000000000000000000000004b")
    callee_11 = Address("0x000000000000000000000000000000000000004c")
    callee_12 = Address("0x000000000000000000000000000000000000005a")
    callee_13 = Address("0x000000000000000000000000000000000000005b")
    callee_14 = Address("0x000000000000000000000000000000000000005c")
    callee_15 = Address("0x000000000000000000000000000000000000006a")
    callee_16 = Address("0x000000000000000000000000000000000000006b")
    callee_17 = Address("0x000000000000000000000000000000000000006c")
    callee_18 = Address("0x000000000000000000000000000000000000007a")
    callee_19 = Address("0x000000000000000000000000000000000000007b")
    callee_20 = Address("0x000000000000000000000000000000000000007c")
    callee_21 = Address("0x000000000000000000000000000000000000008a")
    callee_22 = Address("0x000000000000000000000000000000000000008b")
    callee_23 = Address("0x000000000000000000000000000000000000008c")
    callee_24 = Address("0x00000000000000000000000000000000000c0de0")
    callee_25 = Address("0x00000000000000000000000000000000000c0de1")
    callee_26 = Address("0x00000000000000000000000000000000000c0dea")
    callee_27 = Address("0x00000000000000000000000000000000000c0ded")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=4294967296,
    )

    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH1[0x1] + Op.PUSH1[0x0] + Op.DUP2 + Op.DUP2 + Op.SSTORE + Op.DUP1
        + Op.DUP3 + Op.SSTORE + Op.RETURN
    ),
    )
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH1[0x1] + Op.PUSH1[0x0] + Op.SSTORE + Op.PUSH1[0x1] + Op.DUP1
        + Op.SSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x1] + Op.SSTORE + Op.PUSH2[0x1388]
        + Op.PUSH1[0x0] + Op.RETURN
    ),
    )
    pre[callee_2] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH1[0x1] + Op.PUSH1[0x0] + Op.DUP2 + Op.DUP2 + Op.SSTORE + Op.SWAP1
        + Op.SSTORE + Op.INVALID
    ),
    )
    pre[callee_3] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH1[0x1] + Op.PUSH1[0x0] + Op.SSTORE + Op.PUSH1[0x0] + Op.DUP1
        + Op.DUP1 + Op.DUP1 + Op.DUP1 + Op.PUSH3[0xc0dea] + Op.GAS + Op.CALL
        + Op.PUSH1[0x1] + Op.PUSH1[0x0] + Op.RETURN
    ),
    )
    pre[callee_4] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH1[0x1] + Op.PUSH1[0x0] + Op.SSTORE + Op.PUSH1[0x0] + Op.DUP1
        + Op.DUP1 + Op.DUP1 + Op.DUP1 + Op.PUSH3[0xc0dea] + Op.GAS + Op.CALL
        + Op.PUSH2[0x1388] + Op.PUSH1[0x0] + Op.RETURN
    ),
    )
    pre[callee_5] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH1[0x1] + Op.PUSH1[0x0] + Op.SSTORE + Op.PUSH1[0x0] + Op.DUP1
        + Op.DUP1 + Op.DUP1 + Op.DUP1 + Op.PUSH3[0xc0dea] + Op.GAS + Op.CALL + Op.POP
        + Op.INVALID
    ),
    )
    pre[callee_6] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH1[0x1] + Op.PUSH1[0x0] + Op.SSTORE + Op.PUSH1[0x1] + Op.DUP1
        + Op.SSTORE + Op.PUSH1[0x0] + Op.DUP1 + Op.DUP1 + Op.DUP1 + Op.PUSH3[0xc0dea]
        + Op.GAS + Op.DELEGATECALL + Op.PUSH1[0x1] + Op.PUSH1[0x0] + Op.RETURN
    ),
    )
    pre[callee_7] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH1[0x1] + Op.PUSH1[0x0] + Op.SSTORE + Op.PUSH1[0x1] + Op.DUP1
        + Op.SSTORE + Op.PUSH1[0x0] + Op.DUP1 + Op.DUP1 + Op.DUP1 + Op.PUSH3[0xc0dea]
        + Op.GAS + Op.DELEGATECALL + Op.PUSH2[0x1388] + Op.PUSH1[0x0] + Op.RETURN
    ),
    )
    pre[callee_8] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH1[0x1] + Op.PUSH1[0x0] + Op.SSTORE + Op.PUSH1[0x1] + Op.DUP1
        + Op.SSTORE + Op.PUSH1[0x0] + Op.DUP1 + Op.DUP1 + Op.DUP1 + Op.PUSH3[0xc0dea]
        + Op.GAS + Op.DELEGATECALL + Op.POP + Op.INVALID
    ),
    )
    pre[callee_9] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH1[0x1] + Op.PUSH1[0x0] + Op.SSTORE + Op.PUSH1[0x1] + Op.DUP1
        + Op.SSTORE + Op.PUSH1[0x0] + Op.DUP1 + Op.DUP1 + Op.DUP1 + Op.DUP1
        + Op.PUSH3[0xc0dea] + Op.GAS + Op.CALLCODE + Op.PUSH1[0x1] + Op.PUSH1[0x0]
        + Op.RETURN
    ),
    )
    pre[callee_10] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH1[0x1] + Op.PUSH1[0x0] + Op.SSTORE + Op.PUSH1[0x1] + Op.DUP1
        + Op.SSTORE + Op.PUSH1[0x0] + Op.DUP1 + Op.DUP1 + Op.DUP1 + Op.DUP1
        + Op.PUSH3[0xc0dea] + Op.GAS + Op.CALLCODE + Op.PUSH2[0x1388] + Op.PUSH1[0x0]
        + Op.RETURN
    ),
    )
    pre[callee_11] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH1[0x1] + Op.PUSH1[0x0] + Op.SSTORE + Op.PUSH1[0x1] + Op.DUP1
        + Op.SSTORE + Op.PUSH1[0x0] + Op.DUP1 + Op.DUP1 + Op.DUP1 + Op.DUP1
        + Op.PUSH3[0xc0dea] + Op.GAS + Op.CALLCODE + Op.POP + Op.INVALID
    ),
    )
    pre[callee_12] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH1[0x1] + Op.PUSH1[0x0] + Op.SSTORE + Op.PUSH1[0x0] + Op.DUP1
        + Op.DUP1 + Op.DUP1 + Op.DUP1 + Op.PUSH3[0xc0ded] + Op.GAS + Op.CALL
        + Op.PUSH1[0x1] + Op.PUSH1[0x0] + Op.RETURN
    ),
    )
    pre[callee_13] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH1[0x1] + Op.PUSH1[0x0] + Op.SSTORE + Op.PUSH1[0x0] + Op.DUP1
        + Op.DUP1 + Op.DUP1 + Op.DUP1 + Op.PUSH3[0xc0ded] + Op.GAS + Op.CALL
        + Op.PUSH2[0x1388] + Op.PUSH1[0x0] + Op.RETURN
    ),
    )
    pre[callee_14] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH1[0x1] + Op.PUSH1[0x0] + Op.SSTORE + Op.PUSH1[0x0] + Op.DUP1
        + Op.DUP1 + Op.DUP1 + Op.DUP1 + Op.PUSH3[0xc0ded] + Op.GAS + Op.CALL + Op.POP
        + Op.INVALID
    ),
    )
    pre[callee_15] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH1[0x1] + Op.PUSH1[0x0] + Op.SSTORE + Op.PUSH1[0x0] + Op.DUP1
        + Op.DUP1 + Op.DUP1 + Op.DUP1 + Op.PUSH3[0xc0de0] + Op.GAS + Op.CALL
        + Op.PUSH1[0x1] + Op.PUSH1[0x0] + Op.RETURN
    ),
    )
    pre[callee_16] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH1[0x1] + Op.PUSH1[0x0] + Op.SSTORE + Op.PUSH1[0x0] + Op.DUP1
        + Op.DUP1 + Op.DUP1 + Op.DUP1 + Op.PUSH3[0xc0de0] + Op.GAS + Op.CALL
        + Op.PUSH2[0x1388] + Op.PUSH1[0x0] + Op.RETURN
    ),
    )
    pre[callee_17] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH1[0x1] + Op.PUSH1[0x0] + Op.SSTORE + Op.PUSH1[0x0] + Op.DUP1
        + Op.DUP1 + Op.DUP1 + Op.DUP1 + Op.PUSH3[0xc0de0] + Op.GAS + Op.CALL + Op.POP
        + Op.INVALID
    ),
    )
    pre[callee_18] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH1[0x1] + Op.PUSH1[0x0] + Op.DUP2 + Op.DUP2 + Op.SSTORE + Op.DUP1
        + Op.DUP3 + Op.SSTORE + Op.DUP2 + Op.SWAP1 + Op.PUSH3[0xc0de1] + Op.DUP1
        + Op.EXTCODESIZE + Op.SWAP2 + Op.DUP3 + Op.SWAP2 + Op.DUP2 + Op.SWAP1
        + Op.EXTCODECOPY + Op.DUP1 + Op.PUSH1[0x0] + Op.DUP1 + Op.CREATE + Op.POP
        + Op.ADD + Op.RETURN
    ),
    )
    pre[callee_19] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH1[0x1] + Op.PUSH1[0x0] + Op.SSTORE + Op.PUSH1[0x1] + Op.DUP1
        + Op.SSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x1] + Op.SSTORE + Op.PUSH2[0x1388]
        + Op.PUSH1[0x1] + Op.PUSH1[0x0] + Op.PUSH3[0xc0de1] + Op.DUP2 + Op.DUP2
        + Op.EXTCODESIZE + Op.SWAP3 + Op.DUP4 + Op.SWAP3 + Op.EXTCODECOPY + Op.DUP1
        + Op.PUSH1[0x0] + Op.DUP1 + Op.CREATE + Op.POP + Op.ADD + Op.RETURN
    ),
    )
    pre[callee_20] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH1[0x1] + Op.PUSH1[0x0] + Op.SSTORE + Op.PUSH1[0x1] + Op.DUP1
        + Op.SSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x1] + Op.SSTORE + Op.PUSH1[0x0]
        + Op.PUSH3[0xc0de1] + Op.DUP2 + Op.DUP2 + Op.EXTCODESIZE + Op.SWAP3 + Op.DUP4
        + Op.SWAP3 + Op.EXTCODECOPY + Op.PUSH1[0x0] + Op.DUP1 + Op.CREATE + Op.POP
        + Op.INVALID
    ),
    )
    pre[callee_21] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH1[0x1] + Op.PUSH1[0x0] + Op.DUP2 + Op.DUP2 + Op.SSTORE + Op.DUP1
        + Op.DUP3 + Op.SSTORE
        + Op.PUSH32[0x6001600055600060005560016000f30000000000000000000000000000000000]
        + Op.DUP2 + Op.MSTORE + Op.DUP2 + Op.SWAP1 + Op.PUSH1[0xf] + Op.SWAP1
        + Op.DUP2 + Op.DUP2 + Op.DUP1 + Op.CREATE2 + Op.POP + Op.ADD + Op.RETURN
    ),
    )
    pre[callee_22] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH1[0x1] + Op.PUSH1[0x0] + Op.SSTORE + Op.PUSH1[0x1] + Op.DUP1
        + Op.SSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x1] + Op.SSTORE + Op.PUSH2[0x1388]
        + Op.PUSH1[0x1] + Op.PUSH1[0x0] + Op.PUSH3[0xc0de1] + Op.DUP2 + Op.DUP2
        + Op.EXTCODESIZE + Op.SWAP3 + Op.DUP4 + Op.SWAP3 + Op.EXTCODECOPY
        + Op.PUSH1[0x0] + Op.DUP2 + Op.DUP2 + Op.DUP1 + Op.CREATE2 + Op.POP + Op.ADD
        + Op.RETURN
    ),
    )
    pre[callee_23] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH1[0x1] + Op.PUSH1[0x0] + Op.SSTORE + Op.PUSH1[0x1] + Op.DUP1
        + Op.SSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x1] + Op.SSTORE + Op.PUSH1[0x0]
        + Op.DUP1 + Op.PUSH3[0xc0de1] + Op.DUP2 + Op.DUP2 + Op.EXTCODESIZE + Op.SWAP3
        + Op.DUP4 + Op.SWAP3 + Op.EXTCODECOPY + Op.DUP2 + Op.DUP1 + Op.CREATE2
        + Op.POP + Op.INVALID
    ),
    )
    pre[callee_24] = Account(
        balance=0,
        nonce=1,
        code=(
        Op.PUSH1[0xff] + Op.PUSH1[0x0] + Op.MSTORE + Op.PUSH1[0x20] + Op.PUSH1[0x0]
        + Op.LOG0 + Op.PUSH1[0xfa] + Op.PUSH1[0x20] + Op.PUSH1[0x0] + Op.LOG1
        + Op.PUSH1[0xfb] + Op.PUSH1[0xfa] + Op.PUSH1[0x20] + Op.PUSH1[0x0] + Op.LOG2
        + Op.PUSH1[0xfc] + Op.PUSH1[0xfb] + Op.PUSH1[0xfa] + Op.PUSH1[0x20]
        + Op.PUSH1[0x0] + Op.LOG3 + Op.PUSH1[0xfd] + Op.PUSH1[0xfc] + Op.PUSH1[0xfb]
        + Op.PUSH1[0xfa] + Op.PUSH1[0x20] + Op.PUSH1[0x0] + Op.LOG4 + Op.STOP
    ),
        storage={0x1: 0x1},
    )
    pre[callee_25] = Account(
        balance=0,
        nonce=1,
        code=(
        Op.PUSH1[0x0] + Op.DUP1 + Op.DUP1 + Op.SSTORE + Op.PUSH1[0x1] + Op.SWAP1
        + Op.RETURN
    ),
    )
    pre[callee_26] = Account(
        balance=0,
        nonce=1,
        code=Op.PUSH1[0x0] + Op.PUSH1[0x1] + Op.SSTORE + Op.STOP,
        storage={0x1: 0x1},
    )
    pre[callee_27] = Account(
        balance=0,
        nonce=1,
        code=Op.ORIGIN + Op.SELFDESTRUCT,
        storage={0x1: 0x1},
    )
    pre[sender] = Account(balance=0x3d0900, nonce=1)
    pre[contract] = Account(
        balance=0,
        nonce=1,
        code=(
        Op.PUSH1[0x0] + Op.DUP1 + Op.PUSH1[0x4] + Op.CALLDATALOAD + Op.DUP2
        + Op.DUP2 + Op.EXTCODESIZE + Op.SWAP3 + Op.DUP4 + Op.SWAP3 + Op.EXTCODECOPY
        + Op.DUP2 + Op.DUP1 + Op.CREATE + Op.EQ + Op.PUSH1[0x15] + Op.JUMPI + Op.STOP
        + Op.JUMPDEST + Op.INVALID
    ),
    )

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=tx_data,
        gas_limit=400000,
        gas_price=10,
        nonce=1,
        value=0,
    )

    post = {}

    state_test(env=env, pre=pre, post=post, tx=tx)
