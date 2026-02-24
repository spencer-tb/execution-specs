"""
Tstore arbitrary value in arbitrary slot costs 100 gas.

Ported from:
tests/static/state_tests/Cancun/stEIP1153_transientStorage/17_tstoreGasFiller.yml
"""

import pytest
from execution_testing import (
    AccessList,
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
    ["tests/static/state_tests/Cancun/stEIP1153_transientStorage/17_tstoreGasFiller.yml"],
)
@pytest.mark.valid_from("Cancun")
def test_17_tstore_gas(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Tstore arbitrary value in arbitrary slot costs 100 gas.."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x1000000000000000000000000000000000001000")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=4503599627370496,
    )

    pre[contract] = Account(
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=(
        Op.PUSH1[0x7] + Op.GAS + Op.PUSH1[0x3] + Op.PUSH0 + Op.TSTORE + Op.GAS
        + Op.SWAP1 + Op.SUB + Op.SUB + Op.PUSH1[0x1] + Op.SSTORE + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0x3635c9adc5dea00000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=b"",
        gas_limit=400000,
        max_fee_per_gas=2000,
        max_priority_fee_per_gas=0,
        nonce=0,
        value=0,
        access_list=[],
    )

    post = {}

    state_test(env=env, pre=pre, post=post, tx=tx)
