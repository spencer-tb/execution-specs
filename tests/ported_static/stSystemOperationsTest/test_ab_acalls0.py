"""
Ported from:
tests/static/state_tests/stSystemOperationsTest/ABAcalls0Filler.json
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
    ["tests/static/state_tests/stSystemOperationsTest/ABAcalls0Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_ab_acalls0(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0xd6cd6ec9adca299f2bbfd754ff8bcf6a4b9aae40")
    callee = Address("0x44eb1162303b6a60f2f8882d43d661787b3011e6")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[callee] = Account(
        balance=23,
        nonce=0,
        code=(
        Op.SSTORE(key=Op.PC, value=Op.ADD(0x1, Op.CALL(gas=0xc350, address=0xd6cd6ec9adca299f2bbfd754ff8bcf6a4b9aae40, value=0x17, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)))
        + Op.STOP
    ),
    )
    pre[contract] = Account(
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=(
        Op.SSTORE(key=Op.PC, value=Op.CALL(gas=0x186a0, address=0x44eb1162303b6a60f2f8882d43d661787b3011e6, value=0x18, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
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
        gas_limit=1000000,
        gas_price=10,
        nonce=0,
        value=100000,
    )

    post = {
        callee: Account(
            storage={38: 1},
            code=Op.SSTORE(key=Op.PC, value=Op.ADD(0x1, Op.CALL(gas=0xc350, address=0xd6cd6ec9adca299f2bbfd754ff8bcf6a4b9aae40, value=0x17, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))) + Op.STOP,
        ),
        contract: Account(
            storage={36: 1},
            code=Op.SSTORE(key=Op.PC, value=Op.CALL(gas=0x186a0, address=0x44eb1162303b6a60f2f8882d43d661787b3011e6, value=0x18, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.STOP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
