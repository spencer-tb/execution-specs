"""
CALLCODE -> CALLCODE -> OOG DELEGATE -> CODE

Ported from:
tests/static/state_tests/stCallDelegateCodesCallCodeHomestead/callcallcallcode_001_OOGMBeforeFiller.json
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
    ["tests/static/state_tests/stCallDelegateCodesCallCodeHomestead/callcallcallcode_001_OOGMBeforeFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_callcallcallcode_001_oogm_before(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """CALLCODE -> CALLCODE -> OOG DELEGATE -> CODE."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0x9e57433afaff8a546fbc43cf0330afb6561dc550")
    callee = Address("0x8e6e134402f2eeca8e910e8ec62b45b36ee31f30")
    callee_1 = Address("0xb126c622075b1189fb6c45e851641cfaddf65b36")
    callee_2 = Address("0xefe4727369c5f495aebf4ea778cc48d1155bf978")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=30000000,
    )

    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.SSTORE(key=0x1, value=Op.CALLCODE(gas=0x927c0, address=0xefe4727369c5f495aebf4ea778cc48d1155bf978, value=0x0, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40))
        + Op.SSTORE(key=0xb, value=0x1) + Op.STOP
    ),
    )
    pre[contract] = Account(
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=(
        Op.SSTORE(key=0x0, value=Op.CALLCODE(gas=0xc3500, address=0x8e6e134402f2eeca8e910e8ec62b45b36ee31f30, value=0x0, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40))
        + Op.STOP
    ),
    )
    pre[callee_1] = Account(balance=0, nonce=0, code=Op.SSTORE(key=0x3, value=0x1) + Op.STOP)
    pre[sender] = Account(balance=0xde0b6b3a7640000, nonce=0)
    pre[callee_2] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.POP(Op.SHA3(offset=0x0, size=0x2fffff))
        + Op.SSTORE(key=0x2, value=Op.DELEGATECALL(gas=0x61a80, address=0xb126c622075b1189fb6c45e851641cfaddf65b36, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40))
        + Op.STOP
    ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xe04d1ac7ddda0c98397d56a0b501e960d4cd325a39286919ac23c1a07009a869"
        ),
        to=contract,
        data=b"",
        gas_limit=1000000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        callee: Account(
            code=Op.SSTORE(key=0x1, value=Op.CALLCODE(gas=0x927c0, address=0xefe4727369c5f495aebf4ea778cc48d1155bf978, value=0x0, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40)) + Op.SSTORE(key=0xb, value=0x1) + Op.STOP,
        ),
        contract: Account(
            storage={0: 1, 11: 1},
            code=Op.SSTORE(key=0x0, value=Op.CALLCODE(gas=0xc3500, address=0x8e6e134402f2eeca8e910e8ec62b45b36ee31f30, value=0x0, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40)) + Op.STOP,
        ),
        callee_1: Account(code=Op.SSTORE(key=0x3, value=0x1) + Op.STOP),
        callee_2: Account(
            code=Op.POP(Op.SHA3(offset=0x0, size=0x2fffff)) + Op.SSTORE(key=0x2, value=Op.DELEGATECALL(gas=0x61a80, address=0xb126c622075b1189fb6c45e851641cfaddf65b36, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40)) + Op.STOP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
