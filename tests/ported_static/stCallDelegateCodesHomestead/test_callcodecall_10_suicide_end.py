"""
Ported from:
tests/static/state_tests/stCallDelegateCodesHomestead/callcodecall_10_SuicideEndFiller.json
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
    ["tests/static/state_tests/stCallDelegateCodesHomestead/callcodecall_10_SuicideEndFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_callcodecall_10_suicide_end(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0x2b30b637f37e3f5b8ca4ab846331d0779a3f4671")
    callee = Address("0x703b936fd4d674f0ff5d6957f61097152f8781b8")
    callee_1 = Address("0xf741cfee7b7fb1025dccef3db5a3cbc8ffb776f8")

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
        Op.SSTORE(key=0x0, value=Op.DELEGATECALL(gas=0x249f0, address=0xf741cfee7b7fb1025dccef3db5a3cbc8ffb776f8, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40))
        + Op.STOP
    ),
    )
    pre[callee] = Account(
        balance=0x2540be400,
        nonce=0,
        code=Op.SSTORE(key=0x2, value=0x1) + Op.STOP,
    )
    pre[sender] = Account(balance=0xde0b6b3a7640000, nonce=0)
    pre[callee_1] = Account(
        balance=0x2540be400,
        nonce=0,
        code=(
        Op.SSTORE(key=0x1, value=Op.CALL(gas=0xc350, address=0x703b936fd4d674f0ff5d6957f61097152f8781b8, value=0x0, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40))
        + Op.SELFDESTRUCT(address=0x2b30b637f37e3f5b8ca4ab846331d0779a3f4671)
        + Op.STOP
    ),
    )

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
            storage={0: 1, 1: 1},
            code=Op.SSTORE(key=0x0, value=Op.DELEGATECALL(gas=0x249f0, address=0xf741cfee7b7fb1025dccef3db5a3cbc8ffb776f8, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40)) + Op.STOP,
        ),
        callee: Account(storage={2: 1}, code=Op.SSTORE(key=0x2, value=0x1) + Op.STOP),
        callee_1: Account(
            code=Op.SSTORE(key=0x1, value=Op.CALL(gas=0xc350, address=0x703b936fd4d674f0ff5d6957f61097152f8781b8, value=0x0, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40)) + Op.SELFDESTRUCT(address=0x2b30b637f37e3f5b8ca4ab846331d0779a3f4671) + Op.STOP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
