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
from execution_testing.vm import Op

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
        code=(
            Op.SSTORE(key=0x8, value=Op.GAS)
            + Op.SSTORE(
                key=0x9,
                value=Op.CALL(
                    gas=0x927C0,
                    address=0xA1F6E75A455896613053D45331763A07F4718969,
                    value=0x0,
                    args_offset=0xFF,
                    args_size=0xFF,
                    ret_offset=0xFF,
                    ret_size=0xFF,
                ),
            )
            + Op.SSTORE(
                key=0xA,
                value=Op.CALLCODE(
                    gas=0x927C0,
                    address=0xA1F6E75A455896613053D45331763A07F4718969,
                    value=0x0,
                    args_offset=0xFF,
                    args_size=0xFF,
                    ret_offset=0xFF,
                    ret_size=0xFF,
                ),
            )
        ),
    )
    pre[sender] = Account(balance=0xE8D4A51000, nonce=0)
    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=Op.SSTORE(key=0x0, value=0x12),
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
            storage={0: 18, 8: 0x8D5B6, 9: 1, 10: 1},
            code=(
                Op.SSTORE(key=0x8, value=Op.GAS)
                + Op.SSTORE(
                    key=0x9,
                    value=Op.CALL(
                        gas=0x927C0,
                        address=0xA1F6E75A455896613053D45331763A07F4718969,
                        value=0x0,
                        args_offset=0xFF,
                        args_size=0xFF,
                        ret_offset=0xFF,
                        ret_size=0xFF,
                    ),
                )
                + Op.SSTORE(
                    key=0xA,
                    value=Op.CALLCODE(
                        gas=0x927C0,
                        address=0xA1F6E75A455896613053D45331763A07F4718969,
                        value=0x0,
                        args_offset=0xFF,
                        args_size=0xFF,
                        ret_offset=0xFF,
                        ret_size=0xFF,
                    ),
                )
            ),
        ),
        callee: Account(storage={0: 18}, code=Op.SSTORE(key=0x0, value=0x12)),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
