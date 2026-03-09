"""
Ori Pomerantz qbzzt1@gmail.com

Ported from:
tests/static/state_tests/VMTests/vmIOandFlowOperations/popFiller.yml
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
    ["tests/static/state_tests/VMTests/vmIOandFlowOperations/popFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        ("693c61390000000000000000000000000000000000000000000000000000000000000000", {Address("0x0000000000000000000000000000000000001000"): Account(code=Op.PUSH1[0x2] + Op.PUSH1[0x3] + Op.POP(0x4) + Op.SSTORE), Address("0x0000000000000000000000000000000000001001"): Account(code=Op.POP + Op.PUSH1[0x2] + Op.SSTORE(key=0x4, value=0x3)), Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(storage={3: 2}, code=Op.DELEGATECALL(gas=Op.GAS, address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)), args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0) + Op.STOP)}),
        ("693c61390000000000000000000000000000000000000000000000000000000000000001", {Address("0x0000000000000000000000000000000000001000"): Account(code=Op.PUSH1[0x2] + Op.PUSH1[0x3] + Op.POP(0x4) + Op.SSTORE), Address("0x0000000000000000000000000000000000001001"): Account(code=Op.POP + Op.PUSH1[0x2] + Op.SSTORE(key=0x4, value=0x3)), Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(code=Op.DELEGATECALL(gas=Op.GAS, address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)), args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0) + Op.STOP)}),
    ],
    ids=['case0', 'case1'],
)
@pytest.mark.pre_alloc_mutable
def test_pop(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Ori Pomerantz qbzzt1@gmail.com."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xcccccccccccccccccccccccccccccccccccccccc")
    callee = Address("0x0000000000000000000000000000000000001000")
    callee_1 = Address("0x0000000000000000000000000000000000001001")

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
        code=Op.PUSH1[0x2] + Op.PUSH1[0x3] + Op.POP(0x4) + Op.SSTORE,
    )
    pre[callee_1] = Account(
        balance=0xba1a9ce0ba1a9ce,
        nonce=0,
        code=Op.POP + Op.PUSH1[0x2] + Op.SSTORE(key=0x4, value=0x3),
    )
    pre[sender] = Account(balance=0x100000000000, nonce=0)
    pre[contract] = Account(
        balance=0xba1a9ce0ba1a9ce,
        nonce=0,
        code=(
        Op.DELEGATECALL(gas=Op.GAS, address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)), args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)
        + Op.STOP
    ),
    )

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=tx_data,
        gas_limit=16777216,
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
