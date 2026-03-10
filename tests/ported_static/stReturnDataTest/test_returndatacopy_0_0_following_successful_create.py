"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stReturnDataTest
returndatacopy_0_0_following_successful_createFiller.json
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
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


@pytest.mark.ported_from(
    [
        "tests/static/state_tests/stReturnDataTest/returndatacopy_0_0_following_successful_createFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_returndatacopy_0_0_following_successful_create(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x0f572e5295c57f15886f9b263e2f6d2d6c7b5ec6")

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
        code=(
            Op.PUSH1[0x7]
            + Op.CODECOPY(dest_offset=0x0, offset=0x1D, size=Op.DUP1)
            + Op.PUSH1[0x0]
            + Op.PUSH1[0x0]
            + Op.POP(Op.CREATE)
            + Op.RETURNDATACOPY(dest_offset=0x0, offset=0x0, size=0x0)
            + Op.SSTORE(key=0x0, value=0x0)
            + Op.STOP
            + Op.STOP
            + Op.INVALID
            + Op.SSTORE(key=0x0, value=0x1)
            + Op.STOP
            + Op.STOP
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
        contract: Account(
            code=(
                Op.PUSH1[0x7]
                + Op.CODECOPY(dest_offset=0x0, offset=0x1D, size=Op.DUP1)
                + Op.PUSH1[0x0]
                + Op.PUSH1[0x0]
                + Op.POP(Op.CREATE)
                + Op.RETURNDATACOPY(dest_offset=0x0, offset=0x0, size=0x0)
                + Op.SSTORE(key=0x0, value=0x0)
                + Op.STOP
                + Op.STOP
                + Op.INVALID
                + Op.SSTORE(key=0x0, value=0x1)
                + Op.STOP
                + Op.STOP
            ),
        ),
        Address("0x945304eb96065b2a98b57a48a06ae28d285a71b5"): Account(
            storage={0: 1},
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
