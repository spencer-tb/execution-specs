"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stMemoryStressTest/mload32bitBound_return2Filler.json
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
        "tests/static/state_tests/stMemoryStressTest/mload32bitBound_return2Filler.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit, expected_post",
    [
        (
            150000,
            {
                Address("0x48c46c265c6883f765eea264f561fe7637968b4e"): Account(
                    code=Op.MSTORE(offset=0x0, value=0x1)
                    + Op.RETURN(offset=0x0, size=0xFFFFFFFF)
                    + Op.STOP
                )
            },
        ),
        (
            16777216,
            {
                Address("0x48c46c265c6883f765eea264f561fe7637968b4e"): Account(
                    code=Op.MSTORE(offset=0x0, value=0x1)
                    + Op.RETURN(offset=0x0, size=0xFFFFFFFF)
                    + Op.STOP
                )
            },
        ),
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_mload32bit_bound_return2(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x3b6a01e6249f494f798b8ca3c0ecaf19a2187f54")
    contract = Address("0x48c46c265c6883f765eea264f561fe7637968b4e")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=175923205248920000,
    )

    pre[sender] = Account(balance=0x186A0C3B1E19A180, nonce=0)
    # Source: LLL
    # { [ 0 ] 1 (RETURN 0 4294967295) }
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.MSTORE(offset=0x0, value=0x1)
            + Op.RETURN(offset=0x0, size=0xFFFFFFFF)
            + Op.STOP
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0x7dd14755c573e37c1f649b0c53b9815f76aebd636df7ccfa97f4579f33ba59a0"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
