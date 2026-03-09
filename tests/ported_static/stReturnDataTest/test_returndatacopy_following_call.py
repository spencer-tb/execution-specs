"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stReturnDataTest
returndatacopy_following_callFiller.json
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
        "tests/static/state_tests/stReturnDataTest/returndatacopy_following_callFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_returndatacopy_following_call(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xc102734f6a1e4747310179c0a0fc16e674aa901d")
    contract = Address("0x2faf9d2a81304665c9a06a42935ddc42b24f488b")
    callee = Address("0x9898dd5e5c526b55ec49b1047e298705c13279f1")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=111669149696,
    )

    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "60006000600060006000739898dd5e5c526b55ec49b1047e298705c13279f16409000000"  # noqa: E501
            "00f1506020600060003e60005160005500"
        ),
        storage={0x0: 0x1},
    )
    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "7d111122223333444455556666777788889999aaaabbbbccccddddeeeeffff6000526020"  # noqa: E501
            "6000f300"
        ),
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
        contract: Account(
            storage={
                0: 0x111122223333444455556666777788889999AAAABBBBCCCCDDDDEEEEFFFF,  # noqa: E501
            },
            code=bytes.fromhex(
                "60006000600060006000739898dd5e5c526b55ec49b1047e298705c13279f1640900000000f1506020600060003e60005160005500"  # noqa: E501
            ),
        ),
        callee: Account(
            code=bytes.fromhex(
                "7d111122223333444455556666777788889999aaaabbbbccccddddeeeeffff60005260206000f300"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
