"""
Ported from:
tests/static/state_tests/stEIP150singleCodeGasPrices/RawCallCodeGasFiller.json
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
    ["tests/static/state_tests/stEIP150singleCodeGasPrices/RawCallCodeGasFiller.json"],
)
@pytest.mark.valid_from("Cancun")
def test_raw_call_code_gas(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x1000000000000000000000000000000000001100")
    callee = Address("0x1000000000000000000000000000000000001000")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[callee] = Account(balance=0, nonce=0, code=Op.GAS + Op.PUSH1[0x2] + Op.SSTORE + Op.STOP)
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.GAS + Op.PUSH1[0x0] + Op.MSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH20[0x1000000000000000000000000000000000001000] + Op.PUSH2[0x7530]
        + Op.CALLCODE + Op.POP + Op.GAS + Op.PUSH1[0x0] + Op.MLOAD + Op.SUB
        + Op.PUSH1[0x1] + Op.SSTORE + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0xe8d4a51000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=b"",
        gas_limit=500000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {}

    state_test(env=env, pre=pre, post=post, tx=tx)
