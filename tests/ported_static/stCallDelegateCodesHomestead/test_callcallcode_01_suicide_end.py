"""
Ported from:
tests/static/state_tests/stCallDelegateCodesHomestead/callcallcode_01_SuicideEndFiller.json
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
    ["tests/static/state_tests/stCallDelegateCodesHomestead/callcallcode_01_SuicideEndFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_callcallcode_01_suicide_end(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0x4353e77718be108d4c149d88b34caceda42c5c66")
    callee = Address("0x1cca6e93108ec94304ae5eb121d323e6c317fe7a")
    callee_1 = Address("0x703b936fd4d674f0ff5d6957f61097152f8781b8")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=30000000,
    )

    pre[callee] = Account(
        balance=0x2540be400,
        nonce=0,
        code=(
        Op.SSTORE(key=0x1, value=Op.DELEGATECALL(gas=0xc350, address=0x703b936fd4d674f0ff5d6957f61097152f8781b8, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40))
        + Op.SELFDESTRUCT(address=0x4353e77718be108d4c149d88b34caceda42c5c66)
        + Op.STOP
    ),
    )
    pre[contract] = Account(
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=(
        Op.SSTORE(key=0x0, value=Op.CALL(gas=0x249f0, address=0x1cca6e93108ec94304ae5eb121d323e6c317fe7a, value=0x0, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40))
        + Op.STOP
    ),
    )
    pre[callee_1] = Account(
        balance=0x2540be400,
        nonce=0,
        code=Op.SSTORE(key=0x2, value=0x1) + Op.STOP,
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
        callee: Account(
            storage={1: 1, 2: 1},
            code=Op.SSTORE(key=0x1, value=Op.DELEGATECALL(gas=0xc350, address=0x703b936fd4d674f0ff5d6957f61097152f8781b8, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40)) + Op.SELFDESTRUCT(address=0x4353e77718be108d4c149d88b34caceda42c5c66) + Op.STOP,
        ),
        contract: Account(
            storage={0: 1},
            code=Op.SSTORE(key=0x0, value=Op.CALL(gas=0x249f0, address=0x1cca6e93108ec94304ae5eb121d323e6c317fe7a, value=0x0, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40)) + Op.STOP,
        ),
        callee_1: Account(code=Op.SSTORE(key=0x2, value=0x1) + Op.STOP),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
