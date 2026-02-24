"""
Calls a contract that runs CREATE which deploy a code. then after deployment and exiting from CREATE a REVERT is called. check the REVERT data in this case equal to RETURN value of CREATE. CREATE fails due to the deployment cost.

Ported from:
tests/static/state_tests/stCreateTest/CreateOOGafterInitCodeRevert2Filler.json
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
    ["tests/static/state_tests/stCreateTest/CreateOOGafterInitCodeRevert2Filler.json"],
)
@pytest.mark.valid_from("Cancun")
@pytest.mark.parametrize(
    "tx_data_hex",
    [
        "000000000000000000000000c94f5374fce5edbc8e2a8697c15331677e6ebf0b",
        "000000000000000000000000d94f5374fce5edbc8e2a8697c15331677e6ebf0b",
    ],
    ids=['case0', 'case1'],
)
def test_create_oo_gafter_init_code_revert2(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
) -> None:
    """Calls a contract that runs CREATE which deploy a code. then after deployment and exiting from CREATE a REVERT is called. check the REVERT data in this case equal to RETURN value of CREATE. CREATE fails due to the deployment cost.."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x1000000000000000000000000000000000000000")
    callee = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    callee_1 = Address("0xc94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    callee_2 = Address("0xd94f5374fce5edbc8e2a8697c15331677e6ebf0b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[contract] = Account(
        balance=0xe8d4a51000,
        nonce=0,
        code=(
        Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.CALLDATALOAD + Op.GAS + Op.CALL + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0xe8d4a51000, nonce=0)
    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH14[0x6460016001556000526005601bf3] + Op.PUSH1[0x0] + Op.MSTORE
        + Op.PUSH1[0xe] + Op.PUSH1[0x12] + Op.PUSH1[0x0] + Op.CREATE + Op.POP
        + Op.PUSH1[0x20] + Op.PUSH1[0x0] + Op.REVERT + Op.STOP
    ),
    )
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH1[0x20] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH20[0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b]
        + Op.PUSH2[0x80e8] + Op.CALL + Op.POP + Op.PUSH1[0x0] + Op.MLOAD
        + Op.PUSH1[0x1] + Op.SSTORE + Op.STOP
    ),
        storage={0x1: 0xff},
    )
    pre[callee_2] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH1[0x20] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH20[0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b]
        + Op.PUSH2[0x59d8] + Op.CALL + Op.POP + Op.PUSH1[0x0] + Op.MLOAD
        + Op.PUSH1[0x1] + Op.SSTORE + Op.STOP
    ),
        storage={0x1: 0xff},
    )

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=tx_data,
        gas_limit=175000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {}

    state_test(env=env, pre=pre, post=post, tx=tx)
