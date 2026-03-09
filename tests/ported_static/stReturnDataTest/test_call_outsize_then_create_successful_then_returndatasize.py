"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stReturnDataTest
call_outsize_then_create_successful_then_returndatasizeFiller.json
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
        "tests/static/state_tests/stReturnDataTest/call_outsize_then_create_successful_then_returndatasizeFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_call_outsize_then_create_successful_then_returndatasize(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xc102734f6a1e4747310179c0a0fc16e674aa901d")
    contract = Address("0x3875f9536b829cb75f84cdcb2f72b000b5a41855")
    callee = Address("0x24b406508240d6f2783499d1fd65fedd0feeef37")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=111669149696,
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
            "602060006000600060007324b406508240d6f2783499d1fd65fedd0feeef376409000000"  # noqa: E501
            "00f150600e80603c60003960006000f0503d6000550000fe6211223360005260206000f3"  # noqa: E501
            "0000"
        ),
        storage={0x0: 0x1},
    )
    pre[sender] = Account(balance=0x6400000000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x834185262e53584684bf2b72c64e510013c235d0f45e462db65900455df45a35"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        Address("0x21b8ee56b69b18aaa96ccc9d1e92dd73f5c0f613"): Account(
            code=bytes.fromhex(
                "0000000000000000000000000000000000000000000000000000000000112233"  # noqa: E501
            ),
        ),
        callee: Account(
            code=bytes.fromhex(
                "7d111122223333444455556666777788889999aaaabbbbccccddddeeeeffff60005260206000f30000"  # noqa: E501
            ),
        ),
        contract: Account(
            code=bytes.fromhex(
                "602060006000600060007324b406508240d6f2783499d1fd65fedd0feeef37640900000000f150600e80603c60003960006000f0503d6000550000fe6211223360005260206000f30000"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
