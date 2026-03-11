"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stSelfBalance/selfBalanceFiller.json
"""

import pytest
from execution_testing import (
    Account,
    Address,
    Alloc,
    EOA,
    Environment,
    Hash,
    StateTestFiller,
    Transaction,
)
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


@pytest.mark.ported_from(
    ["tests/static/state_tests/stSelfBalance/selfBalanceFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_self_balance(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = EOA(
        key=0x897B12D02D588D8A4FE16FF831CBD4459C6F62F8C845B0CCDD31CAF068C84A26
    )
    contract = Address("0xc4686d898faa85a20d23378b84956c9e10295db5")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000000,
    )

    # Source: LLL
    # { [[ 1 ]] (SELFBALANCE) }
    pre[contract] = Account(
        balance=500,
        nonce=0,
        code=Op.SSTORE(key=0x1, value=Op.SELFBALANCE) + Op.STOP,
    )
    pre[sender] = Account(balance=0x3635C9ADC5DEA00000, nonce=0)

    tx = Transaction(
        sender=sender,
        to=contract,
        data=b"",
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            storage={1: 500},
            code=Op.SSTORE(key=0x1, value=Op.SELFBALANCE) + Op.STOP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
