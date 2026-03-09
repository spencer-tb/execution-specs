"""
call with value and not enough value to send

Ported from:
tests/static/state_tests/stCallCreateCallCodeTest/callWithHighValueFiller.json
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
    ["tests/static/state_tests/stCallCreateCallCodeTest/callWithHighValueFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_call_with_high_value(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """call with value and not enough value to send."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0xccc6849cd07c3e5b61ab6d7e798d3c4007615284")
    callee = Address("0x9d8c3fed067968360493f6deb5b169a720dac8a2")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=30000000,
    )

    pre[callee] = Account(balance=23, nonce=0, code=Op.SSTORE(key=0x2, value=0x1) + Op.STOP)
    pre[contract] = Account(
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=(
        Op.SSTORE(key=0x0, value=Op.CALL(gas=0x249f0, address=0x9d8c3fed067968360493f6deb5b169a720dac8a2, value=0xde0b6b3a7640001, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x2))
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
        callee: Account(code=Op.SSTORE(key=0x2, value=0x1) + Op.STOP),
        contract: Account(
            code=Op.SSTORE(key=0x0, value=Op.CALL(gas=0x249f0, address=0x9d8c3fed067968360493f6deb5b169a720dac8a2, value=0xde0b6b3a7640001, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x2)) + Op.STOP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
