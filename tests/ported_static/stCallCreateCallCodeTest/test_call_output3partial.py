"""
check the output memory after call

Ported from:
tests/static/state_tests/stCallCreateCallCodeTest/callOutput3partialFiller.json
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
    ["tests/static/state_tests/stCallCreateCallCodeTest/callOutput3partialFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_call_output3partial(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """check the output memory after call."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x2e3d0156d2b99a6eacba540c55f423c8f5a33143")
    contract = Address("0x24bc72d274ab8e9445bb449bbea2ccd492f6a2bf")
    callee = Address("0xbcc1197ccd23a97607f2f96d031f3432e0d16a02")

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
        Op.MSTORE(offset=0x0, value=0x5e20a0453cecd065ea59c37ac63e079ee08998b6045136a8ce6635c7912ec0b6)
        + Op.POP(Op.CALL(gas=0x249f0, address=0xbcc1197ccd23a97607f2f96d031f3432e0d16a02, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0xa))
        + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0)) + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0xde0b6b3a7640000, nonce=0)
    pre[callee] = Account(
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=Op.SSTORE(key=0x0, value=Op.ADD(0x1, 0x1)),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xb1f4cbc3a50042184425a6f9e996d0910f7ba879457ce5dac5c71e498ad3c005"
        ),
        to=contract,
        data=b"",
        gas_limit=1000000,
        gas_price=10,
        nonce=0,
        value=100000,
    )

    post = {
        contract: Account(
            storage={0: 0x5e20a0453cecd065ea59c37ac63e079ee08998b6045136a8ce6635c7912ec0b6},
            code=Op.MSTORE(offset=0x0, value=0x5e20a0453cecd065ea59c37ac63e079ee08998b6045136a8ce6635c7912ec0b6) + Op.POP(Op.CALL(gas=0x249f0, address=0xbcc1197ccd23a97607f2f96d031f3432e0d16a02, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0xa)) + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0)) + Op.STOP,
        ),
        callee: Account(storage={0: 2}, code=Op.SSTORE(key=0x0, value=Op.ADD(0x1, 0x1))),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
