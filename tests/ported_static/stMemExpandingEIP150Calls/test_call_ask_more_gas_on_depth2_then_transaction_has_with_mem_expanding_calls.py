"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stMemExpandingEIP150Calls
CallAskMoreGasOnDepth2ThenTransactionHasWithMemExpandingCallsFiller.json
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
        "tests/static/state_tests/stMemExpandingEIP150Calls/CallAskMoreGasOnDepth2ThenTransactionHasWithMemExpandingCallsFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_call_ask_more_gas_on_depth2_then_transaction_has_with_mem_expanding_calls(  # noqa: E501
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x823066fb511f07f5e49cbd8ca9874e4bc6ee9e65")
    contract = Address("0x97442da68a5f2b1be1728c655c0f395cffb999cf")
    callee = Address("0x9edefdfb5a11a6b30dba1bff8726f94f9d9e1232")
    callee_1 = Address("0xa229d9efd075227ed1e0ea0427045b5ee24dc40a")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[sender] = Account(balance=0xE8D4A51000, nonce=0)
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "5a60085560ff60ff60ff60ff600073a229d9efd075227ed1e0ea0427045b5ee24dc40a62"  # noqa: E501
            "030d40f1600955"
        ),
    )
    pre[callee] = Account(balance=0, nonce=0, code=bytes.fromhex("5a600855"))
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "5a60085560ff60ff60ff60ff6000739edefdfb5a11a6b30dba1bff8726f94f9d9e123262"  # noqa: E501
            "0927c0f1600955"
        ),
    )

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
            storage={8: 0x8D5B6, 9: 1},
            code=bytes.fromhex(
                "5a60085560ff60ff60ff60ff600073a229d9efd075227ed1e0ea0427045b5ee24dc40a62030d40f1600955"  # noqa: E501
            ),
        ),
        callee: Account(storage={8: 0x2A1C7}, code=bytes.fromhex("5a600855")),
        callee_1: Account(
            storage={8: 0x30D3E, 9: 1},
            code=bytes.fromhex(
                "5a60085560ff60ff60ff60ff6000739edefdfb5a11a6b30dba1bff8726f94f9d9e1232620927c0f1600955"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
