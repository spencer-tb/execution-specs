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
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        ("000000000000000000000000c94f5374fce5edbc8e2a8697c15331677e6ebf0b", {Address("0x1000000000000000000000000000000000000000"): Account(code=Op.CALL(gas=Op.GAS, address=Op.CALLDATALOAD(offset=0x0), value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0) + Op.STOP), Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(code=Op.MSTORE(offset=0x0, value=0x6460016001556000526005601bf3) + Op.POP(Op.CREATE(value=0x0, offset=0x12, size=0xe)) + Op.REVERT(offset=0x0, size=0x20) + Op.STOP), Address("0xc94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(storage={1: 0x6460016001556000526005601bf3}, code=Op.POP(Op.CALL(gas=0x80e8, address=0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x20)) + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0)) + Op.STOP), Address("0xd94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(storage={1: 255}, code=Op.POP(Op.CALL(gas=0x59d8, address=0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x20)) + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0)) + Op.STOP)}),
        ("000000000000000000000000d94f5374fce5edbc8e2a8697c15331677e6ebf0b", {Address("0x1000000000000000000000000000000000000000"): Account(code=Op.CALL(gas=Op.GAS, address=Op.CALLDATALOAD(offset=0x0), value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0) + Op.STOP), Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(code=Op.MSTORE(offset=0x0, value=0x6460016001556000526005601bf3) + Op.POP(Op.CREATE(value=0x0, offset=0x12, size=0xe)) + Op.REVERT(offset=0x0, size=0x20) + Op.STOP), Address("0xc94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(storage={1: 255}, code=Op.POP(Op.CALL(gas=0x80e8, address=0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x20)) + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0)) + Op.STOP), Address("0xd94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(code=Op.POP(Op.CALL(gas=0x59d8, address=0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x20)) + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0)) + Op.STOP)}),
    ],
    ids=['case0', 'case1'],
)
@pytest.mark.pre_alloc_mutable
def test_create_oo_gafter_init_code_revert2(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
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
        Op.CALL(gas=Op.GAS, address=Op.CALLDATALOAD(offset=0x0), value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)
        + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0xe8d4a51000, nonce=0)
    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.MSTORE(offset=0x0, value=0x6460016001556000526005601bf3)
        + Op.POP(Op.CREATE(value=0x0, offset=0x12, size=0xe))
        + Op.REVERT(offset=0x0, size=0x20) + Op.STOP
    ),
    )
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.POP(Op.CALL(gas=0x80e8, address=0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x20))
        + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0)) + Op.STOP
    ),
        storage={0x1: 0xff},
    )
    pre[callee_2] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.POP(Op.CALL(gas=0x59d8, address=0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x20))
        + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0)) + Op.STOP
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

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
