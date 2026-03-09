"""
Ported from:
tests/static/state_tests/stLogTests/log4_CallerFiller.json
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
    ["tests/static/state_tests/stLogTests/log4_CallerFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_log4_caller(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0x1e5597b6168fe79952cb2de7af91c3449bc95bd4")
    callee = Address("0x3aac40e63f4e85b4f222671fb5691c8a4fdfb3de")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    pre[contract] = Account(
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=(
        Op.SSTORE(key=0x0, value=Op.CALL(gas=0x3e8, address=0x3aac40e63f4e85b4f222671fb5691c8a4fdfb3de, value=0x17, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.STOP
    ),
    )
    pre[callee] = Account(
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=(
        Op.MSTORE8(offset=0x0, value=0xff)
        + Op.LOG4(offset=0x0, size=0x20, topic_1=0x0, topic_2=0x0, topic_3=0x0, topic_4=Op.CALLER)
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
        gas_limit=210000,
        gas_price=10,
        nonce=0,
        value=100000,
    )

    post = {
        contract: Account(
            storage={0: 1},
            code=Op.SSTORE(key=0x0, value=Op.CALL(gas=0x3e8, address=0x3aac40e63f4e85b4f222671fb5691c8a4fdfb3de, value=0x17, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.STOP,
        ),
        callee: Account(
            code=Op.MSTORE8(offset=0x0, value=0xff) + Op.LOG4(offset=0x0, size=0x20, topic_1=0x0, topic_2=0x0, topic_3=0x0, topic_4=Op.CALLER) + Op.STOP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
