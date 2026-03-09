"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stDelegatecallTestHomestead
CallRecursiveBombPreCallFiller.json
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
        "tests/static/state_tests/stDelegatecallTestHomestead/CallRecursiveBombPreCallFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.valid_until("Prague")
@pytest.mark.pre_alloc_mutable
def test_call_recursive_bomb_pre_call(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x9f583f1fdfa7e94974bff973b2abcd0ad513af0b")
    contract = Address("0x7a11b1b8911ecccfccb030a17f9cebde63a92190")
    callee = Address("0x3046257c307a51f1a8ae73f6f6360937dd21138e")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[callee] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "60016000540160005560006000600060006000733046257c307a51f1a8ae73f6f6360937"  # noqa: E501
            "dd21138e62036b005a03f160015500"
        ),
    )
    pre[contract] = Account(
        balance=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
        nonce=0,
        code=bytes.fromhex(
            "6000600060006000601773bad304eb96065b2a98b57a48a06ae28d285a71b5620186a0f1"  # noqa: E501
            "506000600060006000733046257c307a51f1a8ae73f6f6360937dd21138e6707ffffffff"  # noqa: E501
            "fffffff400"
        ),
    )
    pre[sender] = Account(balance=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x77f65b71f1f16a75476f469f7106d1b60bfec266ae25b8da16a9091d223aa24a"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=9214364837600034817,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        callee: Account(
            storage={0: 1023, 1: 1},
            code=bytes.fromhex(
                "60016000540160005560006000600060006000733046257c307a51f1a8ae73f6f6360937dd21138e62036b005a03f160015500"  # noqa: E501
            ),
        ),
        contract: Account(
            storage={0: 1, 1: 1},
            code=bytes.fromhex(
                "6000600060006000601773bad304eb96065b2a98b57a48a06ae28d285a71b5620186a0f1506000600060006000733046257c307a51f1a8ae73f6f6360937dd21138e6707fffffffffffffff400"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
