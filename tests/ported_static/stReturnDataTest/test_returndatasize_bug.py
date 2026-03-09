"""
RETURNDATASIZE after a failing CALL (due to insufficient balance) should return 0

Ported from:
tests/static/state_tests/stReturnDataTest/returndatasize_bugFiller.json
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
    ["tests/static/state_tests/stReturnDataTest/returndatasize_bugFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_returndatasize_bug(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """RETURNDATASIZE after a failing CALL (due to insufficient balance) should return 0."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xc102734f6a1e4747310179c0a0fc16e674aa901d")
    contract = Address("0x0d7bc2fbd330f7d4ec71764551a8b9cfb11619f5")
    callee = Address("0x0a6de4978faa392285cc6411dfe442872304deb1")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=111669149696,
    )

    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.POP(Op.CALL(gas=0xa, address=0x1, value=0xc350, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.SSTORE(key=0x1, value=0x1) + Op.STOP
    ),
    )
    pre[contract] = Account(
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=(
        Op.POP(Op.CALL(gas=0x1, address=0xa6de4978faa392285cc6411dfe442872304deb1, value=0xc350, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.SSTORE(key=0x0, value=Op.RETURNDATASIZE) + Op.STOP
    ),
        storage={0x0: 0x1},
    )
    pre[sender] = Account(balance=0x6400000000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x834185262e53584684bf2b72c64e510013c235d0f45e462db65900455df45a35"
        ),
        to=contract,
        data=b"",
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        callee: Account(
            code=Op.POP(Op.CALL(gas=0xa, address=0x1, value=0xc350, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x1, value=0x1) + Op.STOP,
        ),
        contract: Account(
            code=Op.POP(Op.CALL(gas=0x1, address=0xa6de4978faa392285cc6411dfe442872304deb1, value=0xc350, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x0, value=Op.RETURNDATASIZE) + Op.STOP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
