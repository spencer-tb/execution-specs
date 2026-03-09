"""
CALL -> CALL -> DELEGATE -> CODE OOG

Ported from:
tests/static/state_tests/stCallDelegateCodesHomestead/callcallcallcode_001_OOGEFiller.json
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
    ["tests/static/state_tests/stCallDelegateCodesHomestead/callcallcallcode_001_OOGEFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_callcallcallcode_001_ooge(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """CALL -> CALL -> DELEGATE -> CODE OOG."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0x335b558774699d81f685543cfbcde5c4e5407686")
    callee = Address("0x1dd747f92062bb53bb8e867ec2902792435f1748")
    callee_1 = Address("0x3e423a7b1fba04d0c3f9423a3ae2a180d2878d5b")
    callee_2 = Address("0xbbdce54b3c571b853032cb3a637e8f5b81dbaf0d")

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
        code=Op.SSTORE(key=0x3, value=0x1) + Op.SHA3(offset=0x0, size=0x2fffff) + Op.STOP,
    )
    pre[contract] = Account(
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=(
        Op.SSTORE(key=0x0, value=Op.CALL(gas=0xc3500, address=0xbbdce54b3c571b853032cb3a637e8f5b81dbaf0d, value=0x0, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40))
        + Op.STOP
    ),
    )
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.SSTORE(key=0x2, value=Op.DELEGATECALL(gas=0x61a80, address=0x1dd747f92062bb53bb8e867ec2902792435f1748, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40))
        + Op.SSTORE(key=0xb, value=0x1) + Op.STOP
    ),
    )
    pre[callee_2] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.SSTORE(key=0x1, value=Op.CALL(gas=0x927c0, address=0x3e423a7b1fba04d0c3f9423a3ae2a180d2878d5b, value=0x0, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40))
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
        value=0,
    )

    post = {
        callee: Account(
            code=Op.SSTORE(key=0x3, value=0x1) + Op.SHA3(offset=0x0, size=0x2fffff) + Op.STOP,
        ),
        contract: Account(
            storage={0: 1},
            code=Op.SSTORE(key=0x0, value=Op.CALL(gas=0xc3500, address=0xbbdce54b3c571b853032cb3a637e8f5b81dbaf0d, value=0x0, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40)) + Op.STOP,
        ),
        callee_1: Account(
            storage={11: 1},
            code=Op.SSTORE(key=0x2, value=Op.DELEGATECALL(gas=0x61a80, address=0x1dd747f92062bb53bb8e867ec2902792435f1748, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40)) + Op.SSTORE(key=0xb, value=0x1) + Op.STOP,
        ),
        callee_2: Account(
            storage={1: 1},
            code=Op.SSTORE(key=0x1, value=Op.CALL(gas=0x927c0, address=0x3e423a7b1fba04d0c3f9423a3ae2a180d2878d5b, value=0x0, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40)) + Op.STOP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
