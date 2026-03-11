"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stMemoryStressTest/JUMP_BoundsFiller.json
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
    ["tests/static/state_tests/stMemoryStressTest/JUMP_BoundsFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit, expected_post",
    [
        (
            150000,
            {
                Address("0xb2448deb71e9fd31ed854e3b856f729adbc0c288"): Account(
                    code=Op.JUMP(pc=0x0) + Op.STOP
                )
            },
        ),
        (
            16777216,
            {
                Address("0xb2448deb71e9fd31ed854e3b856f729adbc0c288"): Account(
                    code=Op.JUMP(pc=0x0) + Op.STOP
                )
            },
        ),
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_jump_bounds(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = EOA(
        key=0x31B5AF02B012484AE954B3A43943242EDE546A2E76FC0A6ACC17435107C385EB
    )
    contract = Address("0xb2448deb71e9fd31ed854e3b856f729adbc0c288")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    # Source: LLL
    # { (JUMP 0) }
    pre[contract] = Account(balance=0, nonce=0, code=Op.JUMP(pc=0x0) + Op.STOP)
    pre[sender] = Account(balance=0x7FFFFFFFFFFFFFFF, nonce=0)

    tx = Transaction(
        sender=sender,
        to=contract,
        data=b"",
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
