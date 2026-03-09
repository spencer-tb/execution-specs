"""
call -> call -> code, params check.

Ported from:
tests/static/state_tests/stCallCodes/callcall_00Filler.json
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
    ["tests/static/state_tests/stCallCodes/callcall_00Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_callcall_00(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Call -> call -> code, params check."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0xeb09ff15547417853f6f4b240b8804769c37b0f1")
    callee = Address("0x33f368f0b54063613cf5944941e8e0e4eeb64697")
    callee_1 = Address("0xc3e151e887921d1edb46aae9b4a3ffc5b85e2a89")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=30000000,
    )

    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "600160025533600455346007553060e6553260e8553660ec553860ee553a60f05500"  # noqa: E501
        ),
    )
    pre[callee_1] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "604060006040600060027333f368f0b54063613cf5944941e8e0e4eeb646976203d090f1"  # noqa: E501
            "60015500"
        ),
    )
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "6040600060406000600173c3e151e887921d1edb46aae9b4a3ffc5b85e2a8962055730f1"  # noqa: E501
            "60005500"
        ),
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xe04d1ac7ddda0c98397d56a0b501e960d4cd325a39286919ac23c1a07009a869"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=3000000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        callee: Account(
            storage={
                2: 1,
                4: 0xC3E151E887921D1EDB46AAE9B4A3FFC5B85E2A89,
                7: 2,
                230: 0x33F368F0B54063613CF5944941E8E0E4EEB64697,
                232: 0xEBAF50DEBF10E08302FE4280C32DF010463CA297,
                236: 64,
                238: 34,
                240: 10,
            },
            code=bytes.fromhex(
                "600160025533600455346007553060e6553260e8553660ec553860ee553a60f05500"  # noqa: E501
            ),
        ),
        callee_1: Account(
            storage={1: 1},
            code=bytes.fromhex(
                "604060006040600060027333f368f0b54063613cf5944941e8e0e4eeb646976203d090f160015500"  # noqa: E501
            ),
        ),
        contract: Account(
            storage={0: 1},
            code=bytes.fromhex(
                "6040600060406000600173c3e151e887921d1edb46aae9b4a3ffc5b85e2a8962055730f160005500"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
