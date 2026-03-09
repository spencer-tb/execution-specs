"""
Uses EXTCODECOPY to copy 32 bytes of code into a 64 byte range of memory...

Ported from:
tests/static/state_tests/stCodeCopyTest
ExtCodeCopyTargetRangeLongerThanCodeTestsFiller.json
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
        "tests/static/state_tests/stCodeCopyTest/ExtCodeCopyTargetRangeLongerThanCodeTestsFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_ext_code_copy_target_range_longer_than_code_tests(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Uses EXTCODECOPY to copy 32 bytes of code into a 64 byte range of..."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x4768b5e50b0ebe91ae38d84a47e3179e615f9c40")
    contract = Address("0x48d8f710ab8cb48f77b602d24696926e31787a17")
    callee = Address("0x7ac02e797f450c7ea62753383f618e1903cd6bba")

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
            "611234602052604060006000737ac02e797f450c7ea62753383f618e1903cd6bba3c6000"  # noqa: E501
            "51600055602051600155615678606052604060006040734768b5e50b0ebe91ae38d84a47"  # noqa: E501
            "e3179e615f9c403c60405160025560605160035500"
        ),
    )
    pre[callee] = Account(
        balance=0,
        nonce=1,
        code=bytes.fromhex(
            "1122334455667788991011121314151617181920212223242526272829303132"
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xe7c72b378297589acee4e0ba3272841bcfc5e220f86de253f890274cfee9e474"  # noqa: E501
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
                0: 0x1122334455667788991011121314151617181920212223242526272829303132,  # noqa: E501
            },
            code=bytes.fromhex(
                "611234602052604060006000737ac02e797f450c7ea62753383f618e1903cd6bba3c600051600055602051600155615678606052604060006040734768b5e50b0ebe91ae38d84a47e3179e615f9c403c60405160025560605160035500"  # noqa: E501
            ),
        ),
        callee: Account(
            code=bytes.fromhex(
                "1122334455667788991011121314151617181920212223242526272829303132"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
