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
from execution_testing.vm import Op

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
    # Source: raw bytecode
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(key=0x8, value=Op.GAS)
            + Op.SSTORE(
                key=0x9,
                value=Op.CALL(
                    gas=0x30D40,
                    address=0xA229D9EFD075227ED1E0EA0427045B5EE24DC40A,
                    value=0x0,
                    args_offset=0xFF,
                    args_size=0xFF,
                    ret_offset=0xFF,
                    ret_size=0xFF,
                ),
            )
        ),
    )
    # Source: raw bytecode
    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=Op.SSTORE(key=0x8, value=Op.GAS),
    )
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(key=0x8, value=Op.GAS)
            + Op.SSTORE(
                key=0x9,
                value=Op.CALL(
                    gas=0x927C0,
                    address=0x9EDEFDFB5A11A6B30DBA1BFF8726F94F9D9E1232,
                    value=0x0,
                    args_offset=0xFF,
                    args_size=0xFF,
                    ret_offset=0xFF,
                    ret_size=0xFF,
                ),
            )
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
            code=(
                Op.SSTORE(key=0x8, value=Op.GAS)
                + Op.SSTORE(
                    key=0x9,
                    value=Op.CALL(
                        gas=0x30D40,
                        address=0xA229D9EFD075227ED1E0EA0427045B5EE24DC40A,
                        value=0x0,
                        args_offset=0xFF,
                        args_size=0xFF,
                        ret_offset=0xFF,
                        ret_size=0xFF,
                    ),
                )
            ),
        ),
        callee: Account(
            storage={8: 0x2A1C7},
            code=Op.SSTORE(key=0x8, value=Op.GAS),
        ),
        callee_1: Account(
            storage={8: 0x30D3E, 9: 1},
            code=(
                Op.SSTORE(key=0x8, value=Op.GAS)
                + Op.SSTORE(
                    key=0x9,
                    value=Op.CALL(
                        gas=0x927C0,
                        address=0x9EDEFDFB5A11A6B30DBA1BFF8726F94F9D9E1232,
                        value=0x0,
                        args_offset=0xFF,
                        args_size=0xFF,
                        ret_offset=0xFF,
                        ret_size=0xFF,
                    ),
                )
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
