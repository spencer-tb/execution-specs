"""
Ported from:
tests/static/state_tests/stSystemOperationsTest/CallRecursiveBombLogFiller.json
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
    ["tests/static/state_tests/stSystemOperationsTest/CallRecursiveBombLogFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.valid_until("Prague")
@pytest.mark.pre_alloc_mutable
def test_call_recursive_bomb_log(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0xd2e8fbe36bd16b24a1d34e4c06ec0741bd71c452")
    callee = Address("0x5fe917d1ef791e524f7cb24cd012b5e5ec17000c")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000000,
    )

    pre[callee] = Account(
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=(
        Op.MSTORE(offset=0x0, value=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
        + Op.LOG0(offset=0x0, size=0x20)
        + Op.SSTORE(key=0x0, value=Op.ADD(Op.SLOAD(key=0x0), 0x1))
        + Op.SSTORE(key=0x1, value=Op.CALL(gas=Op.SUB(Op.GAS, 0x61a8), address=Op.ADDRESS, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.STOP
    ),
    )
    pre[contract] = Account(
        balance=0x1312d00,
        nonce=0,
        code=(
        Op.CALL(gas=0x5f5e100, address=0x5fe917d1ef791e524f7cb24cd012b5e5ec17000c, value=0x17, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)
        + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0xde0b6b3a7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xe04d1ac7ddda0c98397d56a0b501e960d4cd325a39286919ac23c1a07009a869"
        ),
        to=contract,
        data=b"",
        gas_limit=10000000000,
        gas_price=10,
        nonce=0,
        value=100000,
    )

    post = {
        callee: Account(
            storage={0: 321, 1: 1},
            code=Op.MSTORE(offset=0x0, value=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) + Op.LOG0(offset=0x0, size=0x20) + Op.SSTORE(key=0x0, value=Op.ADD(Op.SLOAD(key=0x0), 0x1)) + Op.SSTORE(key=0x1, value=Op.CALL(gas=Op.SUB(Op.GAS, 0x61a8), address=Op.ADDRESS, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.STOP,
        ),
        contract: Account(
            code=Op.CALL(gas=0x5f5e100, address=0x5fe917d1ef791e524f7cb24cd012b5e5ec17000c, value=0x17, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0) + Op.STOP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
