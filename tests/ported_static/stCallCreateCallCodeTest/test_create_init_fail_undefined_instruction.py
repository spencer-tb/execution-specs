"""
create fails because init code has undefined opcode, trying to suicide to it

Ported from:
tests/static/state_tests/stCallCreateCallCodeTest/createInitFailUndefinedInstructionFiller.json
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
    ["tests/static/state_tests/stCallCreateCallCodeTest/createInitFailUndefinedInstructionFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_create_init_fail_undefined_instruction(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """create fails because init code has undefined opcode, trying to suicide to it."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0x73e58ff0ab0c422709d507efb9d4889740040144")
    callee = Address("0x0183feb7335d767d4d6ae41bbdea7afb27227860")
    callee_1 = Address("0x552f200b75457440ee6df9159d6b188e9d18c222")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000000,
    )

    pre[callee] = Account(
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=(
        Op.MSTORE8(offset=0x0, value=0xf9)
        + Op.SELFDESTRUCT(address=Op.CREATE2(value=0x1, offset=0x0, size=0x1, salt=0x0))
        + Op.STOP
    ),
    )
    pre[callee_1] = Account(
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=(
        Op.MSTORE8(offset=0x0, value=0xf9)
        + Op.SELFDESTRUCT(address=Op.CREATE(value=0x1, offset=0x0, size=0x1))
        + Op.STOP
    ),
    )
    pre[contract] = Account(
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=(
        Op.SSTORE(key=0x0, value=Op.CALL(gas=0x61a80, address=0x552f200b75457440ee6df9159d6b188e9d18c222, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.SSTORE(key=0x1, value=Op.CALL(gas=0x61a80, address=0x183feb7335d767d4d6ae41bbdea7afb27227860, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.SSTORE(key=0x2, value=0x1) + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0xde0b6b3a7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xe04d1ac7ddda0c98397d56a0b501e960d4cd325a39286919ac23c1a07009a869"
        ),
        to=contract,
        data=b"",
        gas_limit=900000,
        gas_price=10,
        nonce=0,
        value=100000,
    )

    post = {
        callee: Account(
            code=Op.MSTORE8(offset=0x0, value=0xf9) + Op.SELFDESTRUCT(address=Op.CREATE2(value=0x1, offset=0x0, size=0x1, salt=0x0)) + Op.STOP,
        ),
        callee_1: Account(
            code=Op.MSTORE8(offset=0x0, value=0xf9) + Op.SELFDESTRUCT(address=Op.CREATE(value=0x1, offset=0x0, size=0x1)) + Op.STOP,
        ),
        contract: Account(
            storage={2: 1},
            code=Op.SSTORE(key=0x0, value=Op.CALL(gas=0x61a80, address=0x552f200b75457440ee6df9159d6b188e9d18c222, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x1, value=Op.CALL(gas=0x61a80, address=0x183feb7335d767d4d6ae41bbdea7afb27227860, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x2, value=0x1) + Op.STOP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
