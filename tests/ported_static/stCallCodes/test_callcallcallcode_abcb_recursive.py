"""
call -> call  <-> callcode.

Ported from:
tests/static/state_tests/stCallCodes/callcallcallcode_ABCB_RECURSIVEFiller.json
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
        "tests/static/state_tests/stCallCodes/callcallcallcode_ABCB_RECURSIVEFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_callcallcallcode_abcb_recursive(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Call -> call  <-> callcode."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0x039f3900e280b9c74d46e825b0b3814df4d705ac")
    callee = Address("0x66c0d9f841a86866465e6385c3827be02b580020")
    callee_1 = Address("0xa71333d8c0291cfd6da54bec5a3957563ab16c1c")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=3000000000,
    )

    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "604060006040600060007366c0d9f841a86866465e6385c3827be02b58002063017d7840"  # noqa: E501
            "f160005500"
        ),
    )
    pre[callee] = Account(
        balance=0x2540BE400,
        nonce=0,
        code=bytes.fromhex(
            "6040600060406000600073a71333d8c0291cfd6da54bec5a3957563ab16c1c620f4240f1"  # noqa: E501
            "60015500"
        ),
    )
    pre[callee_1] = Account(
        balance=0x2540BE400,
        nonce=0,
        code=bytes.fromhex(
            "604060006040600060007366c0d9f841a86866465e6385c3827be02b5800206207a120f2"  # noqa: E501
            "60025500"
        ),
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xe04d1ac7ddda0c98397d56a0b501e960d4cd325a39286919ac23c1a07009a869"  # noqa: E501
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
            storage={0: 1},
            code=bytes.fromhex(
                "604060006040600060007366c0d9f841a86866465e6385c3827be02b58002063017d7840f160005500"  # noqa: E501
            ),
        ),
        callee: Account(
            storage={1: 1},
            code=bytes.fromhex(
                "6040600060406000600073a71333d8c0291cfd6da54bec5a3957563ab16c1c620f4240f160015500"  # noqa: E501
            ),
        ),
        callee_1: Account(
            code=bytes.fromhex(
                "604060006040600060007366c0d9f841a86866465e6385c3827be02b5800206207a120f260025500"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
