"""
Ported from:
tests/static/state_tests/stNonZeroCallsTest/NonZeroValue_CALLFiller.json
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
    ["tests/static/state_tests/stNonZeroCallsTest/NonZeroValue_CALLFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_non_zero_value_call(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[sender] = Account(balance=0xe8d4a51000, nonce=0)
    pre[contract] = Account(
        balance=100,
        nonce=0,
        code=(
        Op.MSTORE(offset=0x0, value=Op.GAS)
        + Op.SSTORE(key=0x1, value=Op.CALL(gas=0xea60, address=0xc94f5374fce5edbc8e2a8697c15331677e6ebf0b, value=0x1, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.SSTORE(key=0x64, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)) + Op.STOP
    ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=b"",
        gas_limit=600000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            storage={1: 1, 100: 56435},
            code=Op.MSTORE(offset=0x0, value=Op.GAS) + Op.SSTORE(key=0x1, value=Op.CALL(gas=0xea60, address=0xc94f5374fce5edbc8e2a8697c15331677e6ebf0b, value=0x1, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x64, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)) + Op.STOP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
