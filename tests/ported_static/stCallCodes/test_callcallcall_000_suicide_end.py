"""
call -> call -> (call -> code) suicide

Ported from:
tests/static/state_tests/stCallCodes/callcallcall_000_SuicideEndFiller.json
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
    ["tests/static/state_tests/stCallCodes/callcallcall_000_SuicideEndFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_callcallcall_000_suicide_end(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """call -> call -> (call -> code) suicide."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0x4353e77718be108d4c149d88b34caceda42c5c66")
    callee = Address("0x77b749ffff7ec61d31c79ed104f230a7959b2879")
    callee_1 = Address("0xcb6497f0337b6cd0f7239a8819295ec7d1dafd34")
    callee_2 = Address("0xd957e143ad2c011bc6a2b142795f1a9ba70d0680")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=30000000,
    )

    pre[contract] = Account(
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=(
        Op.SSTORE(key=0x0, value=Op.CALL(gas=0x249f0, address=0x77b749ffff7ec61d31c79ed104f230a7959b2879, value=0x0, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40))
        + Op.STOP
    ),
    )
    pre[callee] = Account(
        balance=0x2540be400,
        nonce=0,
        code=(
        Op.SSTORE(key=0x1, value=Op.CALL(gas=0x186a0, address=0xd957e143ad2c011bc6a2b142795f1a9ba70d0680, value=0x0, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40))
        + Op.STOP
    ),
    )
    pre[callee_1] = Account(
        balance=0x2540be400,
        nonce=0,
        code=Op.SSTORE(key=0x3, value=0x1) + Op.STOP,
    )
    pre[callee_2] = Account(
        balance=0x2540be400,
        nonce=0,
        code=(
        Op.SSTORE(key=0x2, value=Op.CALL(gas=0xc350, address=0xcb6497f0337b6cd0f7239a8819295ec7d1dafd34, value=0x0, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40))
        + Op.SELFDESTRUCT(address=0x77b749ffff7ec61d31c79ed104f230a7959b2879)
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
        gas_limit=3000000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            storage={0: 1},
            code=Op.SSTORE(key=0x0, value=Op.CALL(gas=0x249f0, address=0x77b749ffff7ec61d31c79ed104f230a7959b2879, value=0x0, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40)) + Op.STOP,
        ),
        callee: Account(
            storage={1: 1},
            code=Op.SSTORE(key=0x1, value=Op.CALL(gas=0x186a0, address=0xd957e143ad2c011bc6a2b142795f1a9ba70d0680, value=0x0, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40)) + Op.STOP,
        ),
        callee_1: Account(storage={3: 1}, code=Op.SSTORE(key=0x3, value=0x1) + Op.STOP),
        callee_2: Account(
            storage={2: 1},
            code=Op.SSTORE(key=0x2, value=Op.CALL(gas=0xc350, address=0xcb6497f0337b6cd0f7239a8819295ec7d1dafd34, value=0x0, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40)) + Op.SELFDESTRUCT(address=0x77b749ffff7ec61d31c79ed104f230a7959b2879) + Op.STOP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
