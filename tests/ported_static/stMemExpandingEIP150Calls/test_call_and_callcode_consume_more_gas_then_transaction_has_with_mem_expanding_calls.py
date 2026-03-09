"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stMemExpandingEIP150Calls
CallAndCallcodeConsumeMoreGasThenTransactionHasWithMemExpandingCallsFiller.json
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
        "tests/static/state_tests/stMemExpandingEIP150Calls/CallAndCallcodeConsumeMoreGasThenTransactionHasWithMemExpandingCallsFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_call_and_callcode_consume_more_gas_then_transaction_has_with_mem_expanding_calls(  # noqa: E501
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x823066fb511f07f5e49cbd8ca9874e4bc6ee9e65")
    contract = Address("0x346e4c3e54a808e0cad66173de0d81ff4d06babf")
    callee = Address("0xa1f6e75a455896613053d45331763a07f4718969")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "5a60085560ff60ff60ff60ff600073a1f6e75a455896613053d45331763a07f471896962"  # noqa: E501
            "0927c0f160095560ff60ff60ff60ff600073a1f6e75a455896613053d45331763a07f471"  # noqa: E501
            "8969620927c0f2600a55"
        ),
    )
    pre[sender] = Account(balance=0xE8D4A51000, nonce=0)
    pre[callee] = Account(balance=0, nonce=0, code=bytes.fromhex("6012600055"))

    tx = Transaction(
        secret_key=Hash(
            "0x8d19f2b0d2f5689c1771fbca70476ca6e877a81ee15c3733de87fae38e5abcef"  # noqa: E501
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
            storage={0: 18, 8: 0x8D5B6, 9: 1, 10: 1},
            code=bytes.fromhex(
                "5a60085560ff60ff60ff60ff600073a1f6e75a455896613053d45331763a07f4718969620927c0f160095560ff60ff60ff60ff600073a1f6e75a455896613053d45331763a07f4718969620927c0f2600a55"  # noqa: E501
            ),
        ),
        callee: Account(storage={0: 18}, code=bytes.fromhex("6012600055")),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
