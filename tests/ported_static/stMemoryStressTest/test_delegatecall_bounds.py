"""
Ported from:
tests/static/state_tests/stMemoryStressTest/DELEGATECALL_BoundsFiller.json
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
    ["tests/static/state_tests/stMemoryStressTest/DELEGATECALL_BoundsFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit, expected_post",
    [
        (150000, {Address("0x75bc6dcef9bdda4e2eb511e92ed4815699f32b4f"): Account(code=Op.POP(Op.DELEGATECALL(gas=0x7ffffffffffffff, address=0x849f53126ade5f72469029537296f2b6644d4d41, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.POP(Op.DELEGATECALL(gas=0x7ffffffffffffff, address=0x849f53126ade5f72469029537296f2b6644d4d41, args_offset=0x0, args_size=0xfffffff, ret_offset=0x0, ret_size=0xfffffff)) + Op.POP(Op.DELEGATECALL(gas=0x7ffffffffffffff, address=0x849f53126ade5f72469029537296f2b6644d4d41, args_offset=0x0, args_size=0xffffffff, ret_offset=0x0, ret_size=0xffffffff)) + Op.POP(Op.DELEGATECALL(gas=0x7ffffffffffffff, address=0x849f53126ade5f72469029537296f2b6644d4d41, args_offset=0xfffffff, args_size=0x0, ret_offset=0xfffffff, ret_size=0x0)) + Op.POP(Op.DELEGATECALL(gas=0x7ffffffffffffff, address=0x849f53126ade5f72469029537296f2b6644d4d41, args_offset=0xffffffff, args_size=0x0, ret_offset=0xffffffff, ret_size=0x0)) + Op.POP(Op.DELEGATECALL(gas=0x7ffffffffffffff, address=0x849f53126ade5f72469029537296f2b6644d4d41, args_offset=0xffffffffffffffff, args_size=0x0, ret_offset=0xffffffffffffffff, ret_size=0x0)) + Op.POP(Op.DELEGATECALL(gas=0x7ffffffffffffff, address=0x849f53126ade5f72469029537296f2b6644d4d41, args_offset=0xffffffffffffffffffffffffffffffff, args_size=0x0, ret_offset=0xffffffffffffffffffffffffffffffff, ret_size=0x0)) + Op.POP(Op.DELEGATECALL(gas=0x7ffffffffffffff, address=0x849f53126ade5f72469029537296f2b6644d4d41, args_offset=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff, args_size=0x0, ret_offset=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff, ret_size=0x0)) + Op.DELEGATECALL(gas=0x7ffffffffffffff, address=0x849f53126ade5f72469029537296f2b6644d4d41, args_offset=0xfffffff, args_size=0xfffffff, ret_offset=0xfffffff, ret_size=0xfffffff) + Op.STOP), Address("0x849f53126ade5f72469029537296f2b6644d4d41"): Account(code=Op.SSTORE(key=0x0, value=Op.ADD(0x1, Op.SLOAD(key=0x0))) + Op.STOP)}),
        (16777216, {Address("0x75bc6dcef9bdda4e2eb511e92ed4815699f32b4f"): Account(code=Op.POP(Op.DELEGATECALL(gas=0x7ffffffffffffff, address=0x849f53126ade5f72469029537296f2b6644d4d41, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.POP(Op.DELEGATECALL(gas=0x7ffffffffffffff, address=0x849f53126ade5f72469029537296f2b6644d4d41, args_offset=0x0, args_size=0xfffffff, ret_offset=0x0, ret_size=0xfffffff)) + Op.POP(Op.DELEGATECALL(gas=0x7ffffffffffffff, address=0x849f53126ade5f72469029537296f2b6644d4d41, args_offset=0x0, args_size=0xffffffff, ret_offset=0x0, ret_size=0xffffffff)) + Op.POP(Op.DELEGATECALL(gas=0x7ffffffffffffff, address=0x849f53126ade5f72469029537296f2b6644d4d41, args_offset=0xfffffff, args_size=0x0, ret_offset=0xfffffff, ret_size=0x0)) + Op.POP(Op.DELEGATECALL(gas=0x7ffffffffffffff, address=0x849f53126ade5f72469029537296f2b6644d4d41, args_offset=0xffffffff, args_size=0x0, ret_offset=0xffffffff, ret_size=0x0)) + Op.POP(Op.DELEGATECALL(gas=0x7ffffffffffffff, address=0x849f53126ade5f72469029537296f2b6644d4d41, args_offset=0xffffffffffffffff, args_size=0x0, ret_offset=0xffffffffffffffff, ret_size=0x0)) + Op.POP(Op.DELEGATECALL(gas=0x7ffffffffffffff, address=0x849f53126ade5f72469029537296f2b6644d4d41, args_offset=0xffffffffffffffffffffffffffffffff, args_size=0x0, ret_offset=0xffffffffffffffffffffffffffffffff, ret_size=0x0)) + Op.POP(Op.DELEGATECALL(gas=0x7ffffffffffffff, address=0x849f53126ade5f72469029537296f2b6644d4d41, args_offset=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff, args_size=0x0, ret_offset=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff, ret_size=0x0)) + Op.DELEGATECALL(gas=0x7ffffffffffffff, address=0x849f53126ade5f72469029537296f2b6644d4d41, args_offset=0xfffffff, args_size=0xfffffff, ret_offset=0xfffffff, ret_size=0xfffffff) + Op.STOP), Address("0x849f53126ade5f72469029537296f2b6644d4d41"): Account(code=Op.SSTORE(key=0x0, value=Op.ADD(0x1, Op.SLOAD(key=0x0))) + Op.STOP)}),
    ],
    ids=['case0', 'case1'],
)
@pytest.mark.pre_alloc_mutable
def test_delegatecall_bounds(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa99635038e8d9ab237a31179dd5c9087713f723a")
    contract = Address("0x75bc6dcef9bdda4e2eb511e92ed4815699f32b4f")
    callee = Address("0x849f53126ade5f72469029537296f2b6644d4d41")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.POP(Op.DELEGATECALL(gas=0x7ffffffffffffff, address=0x849f53126ade5f72469029537296f2b6644d4d41, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.POP(Op.DELEGATECALL(gas=0x7ffffffffffffff, address=0x849f53126ade5f72469029537296f2b6644d4d41, args_offset=0x0, args_size=0xfffffff, ret_offset=0x0, ret_size=0xfffffff))
        + Op.POP(Op.DELEGATECALL(gas=0x7ffffffffffffff, address=0x849f53126ade5f72469029537296f2b6644d4d41, args_offset=0x0, args_size=0xffffffff, ret_offset=0x0, ret_size=0xffffffff))
        + Op.POP(Op.DELEGATECALL(gas=0x7ffffffffffffff, address=0x849f53126ade5f72469029537296f2b6644d4d41, args_offset=0xfffffff, args_size=0x0, ret_offset=0xfffffff, ret_size=0x0))
        + Op.POP(Op.DELEGATECALL(gas=0x7ffffffffffffff, address=0x849f53126ade5f72469029537296f2b6644d4d41, args_offset=0xffffffff, args_size=0x0, ret_offset=0xffffffff, ret_size=0x0))
        + Op.POP(Op.DELEGATECALL(gas=0x7ffffffffffffff, address=0x849f53126ade5f72469029537296f2b6644d4d41, args_offset=0xffffffffffffffff, args_size=0x0, ret_offset=0xffffffffffffffff, ret_size=0x0))
        + Op.POP(Op.DELEGATECALL(gas=0x7ffffffffffffff, address=0x849f53126ade5f72469029537296f2b6644d4d41, args_offset=0xffffffffffffffffffffffffffffffff, args_size=0x0, ret_offset=0xffffffffffffffffffffffffffffffff, ret_size=0x0))
        + Op.POP(Op.DELEGATECALL(gas=0x7ffffffffffffff, address=0x849f53126ade5f72469029537296f2b6644d4d41, args_offset=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff, args_size=0x0, ret_offset=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff, ret_size=0x0))
        + Op.DELEGATECALL(gas=0x7ffffffffffffff, address=0x849f53126ade5f72469029537296f2b6644d4d41, args_offset=0xfffffff, args_size=0xfffffff, ret_offset=0xfffffff, ret_size=0xfffffff)
        + Op.STOP
    ),
    )
    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=Op.SSTORE(key=0x0, value=Op.ADD(0x1, Op.SLOAD(key=0x0))) + Op.STOP,
    )
    pre[sender] = Account(
        balance=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff,
        nonce=0,
    )

    tx = Transaction(
        secret_key=Hash(
            "0x50eadfb1030587ab3a993a6ecc073041fc3b45e119daa31a13d78c7e209631a5"
        ),
        to=contract,
        data=b"",
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
