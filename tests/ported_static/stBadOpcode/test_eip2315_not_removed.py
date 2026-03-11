"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stBadOpcode/eip2315NotRemovedFiller.json
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
    ["tests/static/state_tests/stBadOpcode/eip2315NotRemovedFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_eip2315_not_removed(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = EOA(
        key=0x31B5AF02B012484AE954B3A43943242EDE546A2E76FC0A6ACC17435107C385EB
    )
    contract = Address("0x147943601b1281618e4d824d11073025cd2ac623")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    # Source: raw bytecode
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.PUSH1[0x4]
            + Op.MCOPY
            + Op.STOP
            + Op.TLOAD
            + Op.SSTORE(key=0x0, value=0x1)
            + Op.TSTORE
        ),
    )
    pre[sender] = Account(balance=0x7FFFFFFFFFFFFFFF, nonce=0)

    tx = Transaction(
        sender=sender,
        to=contract,
        data=b"",
        gas_limit=400000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            code=(
                Op.PUSH1[0x4]
                + Op.MCOPY
                + Op.STOP
                + Op.TLOAD
                + Op.SSTORE(key=0x0, value=0x1)
                + Op.TSTORE
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
