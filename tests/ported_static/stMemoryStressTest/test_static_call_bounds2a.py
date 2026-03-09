"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stMemoryStressTest/static_CALL_Bounds2aFiller.json
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
        "tests/static/state_tests/stMemoryStressTest/static_CALL_Bounds2aFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit, expected_post",
    [
        (
            150000,
            {
                Address("0x849f53126ade5f72469029537296f2b6644d4d41"): Account(
                    code=bytes.fromhex("60005460010160005500")
                ),
                Address("0x9edf5834c8b457164c7d203e17df72d92d384dba"): Account(
                    code=bytes.fromhex(
                        "63ffffffff63ffffffff63ffffffff63ffffffff73849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffffa00"  # noqa: E501
                    )
                ),
            },
        ),
        (
            16777216,
            {
                Address("0x849f53126ade5f72469029537296f2b6644d4d41"): Account(
                    code=bytes.fromhex("60005460010160005500")
                ),
                Address("0x9edf5834c8b457164c7d203e17df72d92d384dba"): Account(
                    code=bytes.fromhex(
                        "63ffffffff63ffffffff63ffffffff63ffffffff73849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffffa00"  # noqa: E501
                    )
                ),
            },
        ),
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_static_call_bounds2a(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x4d2e21bbf9a40a8303787a066285648f8013129a")
    contract = Address("0x9edf5834c8b457164c7d203e17df72d92d384dba")
    callee = Address("0x849f53126ade5f72469029537296f2b6644d4d41")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[sender] = Account(
        balance=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
        nonce=0,
    )
    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("60005460010160005500"),
    )
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "63ffffffff63ffffffff63ffffffff63ffffffff73849f53126ade5f72469029537296f2"  # noqa: E501
            "b6644d4d416707fffffffffffffffa00"
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xef111bbdab3a1622936afdfc9bbec4b5bc05b4fa4b1ef0ce2a55cef552f7650e"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
