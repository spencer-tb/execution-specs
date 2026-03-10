"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stChainId/chainIdGasCostFiller.json
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
    ["tests/static/state_tests/stChainId/chainIdGasCostFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_chain_id_gas_cost(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xd187b36e8532efd7f15218fb1781d79330c0cda2")
    contract = Address("0x53f64910db5c1bbb54ccb272c0e28bd47249ba9b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000000,
    )

    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.GAS
            + Op.CHAINID
            + Op.GAS
            + Op.SWAP1
            + Op.POP
            + Op.SWAP1
            + Op.SUB
            + Op.PUSH1[0x2]
            + Op.SWAP1
            + Op.SSTORE(key=0x1, value=Op.SUB)
            + Op.STOP
        ),
    )
    pre[sender] = Account(balance=0x3635C9ADC5DEA00000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x897b12d02d588d8a4fe16ff831cbd4459c6f62f8c845b0ccdd31caf068c84a26"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            storage={1: 2},
            code=(
                Op.GAS
                + Op.CHAINID
                + Op.GAS
                + Op.SWAP1
                + Op.POP
                + Op.SWAP1
                + Op.SUB
                + Op.PUSH1[0x2]
                + Op.SWAP1
                + Op.SSTORE(key=0x1, value=Op.SUB)
                + Op.STOP
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
