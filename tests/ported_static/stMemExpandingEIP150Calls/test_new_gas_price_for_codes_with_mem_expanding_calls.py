"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stMemExpandingEIP150Calls
NewGasPriceForCodesWithMemExpandingCallsFiller.json
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
        "tests/static/state_tests/stMemExpandingEIP150Calls/NewGasPriceForCodesWithMemExpandingCallsFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_new_gas_price_for_codes_with_mem_expanding_calls(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xf1100237a29f570cbf8b107ba3cb5bf2db42bd3f")
    contract = Address("0x23a2ec54f5f8589778da7c2199caf3b179a24cb9")
    callee = Address("0x6b6af3c6e1714081c8c3085acbac8c2b21fadf0b")
    callee_1 = Address("0x7b8c83e74cc8dfadb03138c2743c70588ace4222")

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
            "736b6af3c6e1714081c8c3085acbac8c2b21fadf0b3b600155601460006000736b6af3c6"  # noqa: E501
            "e1714081c8c3085acbac8c2b21fadf0b3c60005160025560005460045560ff60ff60ff60"  # noqa: E501
            "ff6001737b8c83e74cc8dfadb03138c2743c70588ace4222617530f160055560ff60ff60"  # noqa: E501
            "ff60ff6001737b8c83e74cc8dfadb03138c2743c70588ace4222617530f260065560ff60"  # noqa: E501
            "ff60ff60ff737b8c83e74cc8dfadb03138c2743c70588ace4222617530f460075560ff60"  # noqa: E501
            "ff60ff60ff6000731000000000000000000000000000000000000013617530f160085573"  # noqa: E501
            "f1100237a29f570cbf8b107ba3cb5bf2db42bd3f316003555a600a55"
        ),
        storage={0x0: 0x12},
    )
    pre[callee] = Account(
        balance=111,
        nonce=0,
        code=bytes.fromhex(
            "1122334455667788991011121314151617181920212223242526272829303132"
        ),
    )
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("6011606455"),
    )
    pre[sender] = Account(balance=0xE8D4A5100000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x03956fc06bd55836acdb92da0e38a15f2e568c088022cf2278180477f3f7702a"  # noqa: E501
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
            storage={
                0: 18,
                1: 32,
                2: 0x1122334455667788991011121314151617181920000000000000000000000000,  # noqa: E501
                3: 0xE8D4A4B47280,
                4: 18,
                7: 1,
                8: 1,
                10: 0x60AE9,
                100: 17,
            },
            code=bytes.fromhex(
                "736b6af3c6e1714081c8c3085acbac8c2b21fadf0b3b600155601460006000736b6af3c6e1714081c8c3085acbac8c2b21fadf0b3c60005160025560005460045560ff60ff60ff60ff6001737b8c83e74cc8dfadb03138c2743c70588ace4222617530f160055560ff60ff60ff60ff6001737b8c83e74cc8dfadb03138c2743c70588ace4222617530f260065560ff60ff60ff60ff737b8c83e74cc8dfadb03138c2743c70588ace4222617530f460075560ff60ff60ff60ff6000731000000000000000000000000000000000000013617530f160085573f1100237a29f570cbf8b107ba3cb5bf2db42bd3f316003555a600a55"  # noqa: E501
            ),
        ),
        callee: Account(
            code=bytes.fromhex(
                "1122334455667788991011121314151617181920212223242526272829303132"  # noqa: E501
            ),
        ),
        callee_1: Account(code=bytes.fromhex("6011606455")),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
