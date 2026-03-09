"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stCodeCopyTest/ExtCodeCopyTestsParisFiller.json
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
        "tests/static/state_tests/stCodeCopyTest/ExtCodeCopyTestsParisFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_ext_code_copy_tests_paris(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xaaaf5374fce5edbc8e2a8697c15331677e6ebf0b")
    callee = Address("0xcccf5374fce5edbc8e2a8697c15331677e6ebf0b")
    callee_1 = Address("0xdddf5374fce5edbc8e2a8697c15331677e6ebf0b")
    callee_2 = Address("0xeeef5374fce5edbc8e2a8697c15331677e6ebf0b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[sender] = Account(balance=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF, nonce=0)
    pre[contract] = Account(
        balance=7000,
        nonce=0,
        code=bytes.fromhex(
            "6002600a600173bbbf5374fce5edbc8e2a8697c15331677e6ebf0b3c6000516002556002"  # noqa: E501
            "600a600173cccf5374fce5edbc8e2a8697c15331677e6ebf0b3c6000516003556002600a"  # noqa: E501
            "600173dddf5374fce5edbc8e2a8697c15331677e6ebf0b3c6000516004556002600a6001"  # noqa: E501
            "73eeef5374fce5edbc8e2a8697c15331677e6ebf0b3c60005160055560c8600a600173ee"  # noqa: E501
            "ef5374fce5edbc8e2a8697c15331677e6ebf0b3c60005160065500"
        ),
    )
    pre[callee] = Account(balance=10, nonce=0)
    pre[callee_1] = Account(balance=0, nonce=1)
    pre[callee_2] = Account(
        balance=0,
        nonce=1,
        code=bytes.fromhex(
            "1122334455667788991011121314151617181920212223242526272829303132"
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=400000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            storage={
                5: 0x11120000000000000000000000000000000000000000000000000000000000,  # noqa: E501
                6: 0x11121314151617181920212223242526272829303132000000000000000000,  # noqa: E501
            },
            code=bytes.fromhex(
                "6002600a600173bbbf5374fce5edbc8e2a8697c15331677e6ebf0b3c6000516002556002600a600173cccf5374fce5edbc8e2a8697c15331677e6ebf0b3c6000516003556002600a600173dddf5374fce5edbc8e2a8697c15331677e6ebf0b3c6000516004556002600a600173eeef5374fce5edbc8e2a8697c15331677e6ebf0b3c60005160055560c8600a600173eeef5374fce5edbc8e2a8697c15331677e6ebf0b3c60005160065500"  # noqa: E501
            ),
        ),
        callee_2: Account(
            code=bytes.fromhex(
                "1122334455667788991011121314151617181920212223242526272829303132"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
