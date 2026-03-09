"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stMemExpandingEIP150Calls
CallGoesOOGOnSecondLevel2WithMemExpandingCallsFiller.json
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

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


@pytest.mark.ported_from(
    [
        "tests/static/state_tests/stMemExpandingEIP150Calls/CallGoesOOGOnSecondLevel2WithMemExpandingCallsFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_call_goes_oog_on_second_level2_with_mem_expanding_calls(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xadc699577c950fccb53e02805bf25c44939cda20")
    contract = Address("0x0700bb425d7d4c412ac658014015bd6c98652dc4")
    callee = Address("0x96983de02bfbcb5d0f4e0ee98fdde6d6f0c75fe0")
    callee_1 = Address("0xc10a98222464b07008ceb5a0ec44ed49920addda")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000,
    )

    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "5a60085560ff60ff60ff60ff600073c10a98222464b07008ceb5a0ec44ed49920addda62"  # noqa: E501
            "0927c0f1600955"
        ),
    )
    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("5a6008555a6009555a600a55"),
    )
    pre[sender] = Account(balance=0xE8D4A510000, nonce=0)
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "5a60085560ff60ff60ff60ff60007396983de02bfbcb5d0f4e0ee98fdde6d6f0c75fe062"  # noqa: E501
            "0927c0f1600955"
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0x0b51075bb33d347a23b516e327e1b71c54f63faa192d1d94b62c76e0c26cf98a"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=160000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            code=bytes.fromhex(
                "5a60085560ff60ff60ff60ff600073c10a98222464b07008ceb5a0ec44ed49920addda620927c0f1600955"  # noqa: E501
            ),
        ),
        callee: Account(code=bytes.fromhex("5a6008555a6009555a600a55")),
        callee_1: Account(
            code=bytes.fromhex(
                "5a60085560ff60ff60ff60ff60007396983de02bfbcb5d0f4e0ee98fdde6d6f0c75fe0620927c0f1600955"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
