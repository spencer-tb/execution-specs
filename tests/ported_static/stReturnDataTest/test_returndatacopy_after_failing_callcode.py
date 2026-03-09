"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stReturnDataTest
returndatacopy_after_failing_callcodeFiller.json
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
        "tests/static/state_tests/stReturnDataTest/returndatacopy_after_failing_callcodeFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_returndatacopy_after_failing_callcode(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xc102734f6a1e4747310179c0a0fc16e674aa901d")
    contract = Address("0x24878b81dd27c2d76258b421acddf26835bc1484")
    callee = Address("0x285d0814904bebb3b4add3b531a07647c2d08f59")
    callee_1 = Address("0x665521fd750490fd880ee369c267fca44ed8a078")

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
            "6000600060006000600073665521fd750490fd880ee369c267fca44ed8a0786000f25060"  # noqa: E501
            "20600060003e60005160005500"
        ),
        storage={0x0: 0xFFFFFFFFFFFF},
    )
    pre[callee] = Account(balance=0x10000000, nonce=0)
    pre[callee_1] = Account(
        balance=0x6400000000,
        nonce=0,
        code=bytes.fromhex("fd"),
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
            storage={0: 0xFFFFFFFFFFFF},
            code=bytes.fromhex(
                "6000600060006000600073665521fd750490fd880ee369c267fca44ed8a0786000f2506020600060003e60005160005500"  # noqa: E501
            ),
        ),
        callee_1: Account(code=bytes.fromhex("fd")),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
