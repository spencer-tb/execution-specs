"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stCreate2
call_then_create2_successful_then_returndatasizeFiller.json
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
        "tests/static/state_tests/stCreate2/call_then_create2_successful_then_returndatasizeFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_call_then_create2_successful_then_returndatasize(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x0f572e5295c57f15886f9b263e2f6d2d6c7b5ec6")
    callee = Address("0x0aabbccdd5c57f15886f9b263e2f6d2d6c7b5ec6")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=47244640256,
    )

    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "7d111122223333444455556666777788889999aaaabbbbccccddddeeeeffff6000526020"  # noqa: E501
            "6000f30000"
        ),
    )
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "60006000600060006000730aabbccdd5c57f15886f9b263e2f6d2d6c7b5ec66409000000"  # noqa: E501
            "00f1506000600e80603e60003960006000f5503d6000550000fe62112233600052602060"  # noqa: E501
            "00f30000"
        ),
        storage={0x0: 0x1},
    )
    pre[sender] = Account(balance=0x6400000000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        callee: Account(
            code=bytes.fromhex(
                "7d111122223333444455556666777788889999aaaabbbbccccddddeeeeffff60005260206000f30000"  # noqa: E501
            ),
        ),
        contract: Account(
            code=bytes.fromhex(
                "60006000600060006000730aabbccdd5c57f15886f9b263e2f6d2d6c7b5ec6640900000000f1506000600e80603e60003960006000f5503d6000550000fe6211223360005260206000f30000"  # noqa: E501
            ),
        ),
        Address("0xc0c06666fad9e52251740536e21fc0f3db0e0fa0"): Account(
            code=bytes.fromhex(
                "0000000000000000000000000000000000000000000000000000000000112233"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
