"""
CALLCODE -> CALL <-> CALL

Ported from:
tests/static/state_tests/stCallCodes/callcodecallcall_ABCB_RECURSIVEFiller.json
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
    ["tests/static/state_tests/stCallCodes/callcodecallcall_ABCB_RECURSIVEFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_callcodecallcall_abcb_recursive(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """CALLCODE -> CALL <-> CALL."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0x6d477a21d3906d4c0cd1edbfa7d272e6e21f1ca1")
    callee = Address("0x66c0d9f841a86866465e6385c3827be02b580020")
    callee_1 = Address("0x91a8703c1bef34c1e76e152c1f7fb8c336c3be24")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=3000000000,
    )

    pre[callee] = Account(
        balance=0x2540be400,
        nonce=0,
        code=(
        Op.SSTORE(key=0x1, value=Op.CALL(gas=0xf4240, address=0x91a8703c1bef34c1e76e152c1f7fb8c336c3be24, value=0x0, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40))
        + Op.STOP
    ),
    )
    pre[contract] = Account(
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=(
        Op.SSTORE(key=0x0, value=Op.CALLCODE(gas=0x17d7840, address=0x66c0d9f841a86866465e6385c3827be02b580020, value=0x0, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40))
        + Op.STOP
    ),
    )
    pre[callee_1] = Account(
        balance=0x2540be400,
        nonce=0,
        code=(
        Op.SSTORE(key=0x2, value=Op.CALL(gas=0x7a120, address=0x66c0d9f841a86866465e6385c3827be02b580020, value=0x0, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40))
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
        gas_limit=600000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        callee: Account(
            code=Op.SSTORE(key=0x1, value=Op.CALL(gas=0xf4240, address=0x91a8703c1bef34c1e76e152c1f7fb8c336c3be24, value=0x0, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40)) + Op.STOP,
        ),
        contract: Account(
            storage={0: 1, 1: 1},
            code=Op.SSTORE(key=0x0, value=Op.CALLCODE(gas=0x17d7840, address=0x66c0d9f841a86866465e6385c3827be02b580020, value=0x0, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40)) + Op.STOP,
        ),
        callee_1: Account(
            code=Op.SSTORE(key=0x2, value=Op.CALL(gas=0x7a120, address=0x66c0d9f841a86866465e6385c3827be02b580020, value=0x0, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40)) + Op.STOP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
