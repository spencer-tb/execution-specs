"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stReturnDataTest
returndatacopy_after_failing_delegatecallFiller.json
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
        "tests/static/state_tests/stReturnDataTest/returndatacopy_after_failing_delegatecallFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_returndatacopy_after_failing_delegatecall(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xc102734f6a1e4747310179c0a0fc16e674aa901d")
    contract = Address("0x905c744acaf4d8f5436c9c5e91e0626d44add821")
    callee = Address("0x5242f2ad00427020024f504ae629e0576ca6a01a")
    callee_1 = Address("0x665521fd750490fd880ee369c267fca44ed8a078")

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
            "600060006000600073665521fd750490fd880ee369c267fca44ed8a078612710f4506020"  # noqa: E501
            "600060003e60005160005500"
        ),
        storage={
            0x0: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
        },
    )
    pre[callee_1] = Account(
        balance=0x6400000000,
        nonce=0,
        code=bytes.fromhex("fd"),
    )
    pre[contract] = Account(balance=0x100000, nonce=0)
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
        callee: Account(
            storage={
                0: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
            },
            code=bytes.fromhex(
                "600060006000600073665521fd750490fd880ee369c267fca44ed8a078612710f4506020600060003e60005160005500"  # noqa: E501
            ),
        ),
        callee_1: Account(code=bytes.fromhex("fd")),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
