"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stReturnDataTest
returndatasize_after_successful_delegatecallFiller.json
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
        "tests/static/state_tests/stReturnDataTest/returndatasize_after_successful_delegatecallFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_returndatasize_after_successful_delegatecall(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xc102734f6a1e4747310179c0a0fc16e674aa901d")
    contract = Address("0x1c7cce7753e67952a031524e6505e53f170520be")
    callee = Address("0x7c17dbbfa29dc8391bfa19022ecb4fda54fc826a")

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
            "6000600060006000737c17dbbfa29dc8391bfa19022ecb4fda54fc826a61ea60f4503d60"  # noqa: E501
            "005500"
        ),
        storage={
            0x0: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
        },
    )
    pre[callee] = Account(
        balance=0x6400000000,
        nonce=0,
        code=bytes.fromhex("3360005260146000f300"),
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
            storage={0: 20},
            code=bytes.fromhex(
                "6000600060006000737c17dbbfa29dc8391bfa19022ecb4fda54fc826a61ea60f4503d60005500"  # noqa: E501
            ),
        ),
        callee: Account(code=bytes.fromhex("3360005260146000f300")),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
