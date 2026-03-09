"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stMemoryStressTest/DELEGATECALL_Bounds2Filler.json
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
        "tests/static/state_tests/stMemoryStressTest/DELEGATECALL_Bounds2Filler.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit, expected_post",
    [
        (
            150000,
            {
                Address("0x7b7e1fed40d6cb2420c7f2718725badb76616d4d"): Account(
                    code=bytes.fromhex(
                        "63ffffffff63ffffffff63ffffffff63ffffffff73849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff400"  # noqa: E501
                    )
                ),
                Address("0x849f53126ade5f72469029537296f2b6644d4d41"): Account(
                    code=bytes.fromhex("60005460010160005500")
                ),
            },
        ),
        (
            16777216,
            {
                Address("0x7b7e1fed40d6cb2420c7f2718725badb76616d4d"): Account(
                    code=bytes.fromhex(
                        "63ffffffff63ffffffff63ffffffff63ffffffff73849f53126ade5f72469029537296f2b6644d4d416707fffffffffffffff400"  # noqa: E501
                    )
                ),
                Address("0x849f53126ade5f72469029537296f2b6644d4d41"): Account(
                    code=bytes.fromhex("60005460010160005500")
                ),
            },
        ),
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_delegatecall_bounds2(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa99635038e8d9ab237a31179dd5c9087713f723a")
    contract = Address("0x7b7e1fed40d6cb2420c7f2718725badb76616d4d")
    callee = Address("0x849f53126ade5f72469029537296f2b6644d4d41")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "63ffffffff63ffffffff63ffffffff63ffffffff73849f53126ade5f72469029537296f2"  # noqa: E501
            "b6644d4d416707fffffffffffffff400"
        ),
    )
    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("60005460010160005500"),
    )
    pre[sender] = Account(
        balance=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
        nonce=0,
    )

    tx = Transaction(
        secret_key=Hash(
            "0x50eadfb1030587ab3a993a6ecc073041fc3b45e119daa31a13d78c7e209631a5"  # noqa: E501
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
