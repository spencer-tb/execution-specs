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
from execution_testing.vm import Op

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
                    code=Op.SSTORE(
                        key=0x0, value=Op.ADD(0x1, Op.SLOAD(key=0x0))
                    )
                    + Op.STOP
                ),
                Address("0x9edf5834c8b457164c7d203e17df72d92d384dba"): Account(
                    code=Op.STATICCALL(
                        gas=0x7FFFFFFFFFFFFFF,
                        address=0x849F53126ADE5F72469029537296F2B6644D4D41,
                        args_offset=0xFFFFFFFF,
                        args_size=0xFFFFFFFF,
                        ret_offset=0xFFFFFFFF,
                        ret_size=0xFFFFFFFF,
                    )
                    + Op.STOP
                ),
            },
        ),
        (
            16777216,
            {
                Address("0x849f53126ade5f72469029537296f2b6644d4d41"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.ADD(0x1, Op.SLOAD(key=0x0))
                    )
                    + Op.STOP
                ),
                Address("0x9edf5834c8b457164c7d203e17df72d92d384dba"): Account(
                    code=Op.STATICCALL(
                        gas=0x7FFFFFFFFFFFFFF,
                        address=0x849F53126ADE5F72469029537296F2B6644D4D41,
                        args_offset=0xFFFFFFFF,
                        args_size=0xFFFFFFFF,
                        ret_offset=0xFFFFFFFF,
                        ret_size=0xFFFFFFFF,
                    )
                    + Op.STOP
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
        code=(
            Op.SSTORE(key=0x0, value=Op.ADD(0x1, Op.SLOAD(key=0x0))) + Op.STOP
        ),
    )
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.STATICCALL(
                gas=0x7FFFFFFFFFFFFFF,
                address=0x849F53126ADE5F72469029537296F2B6644D4D41,
                args_offset=0xFFFFFFFF,
                args_size=0xFFFFFFFF,
                ret_offset=0xFFFFFFFF,
                ret_size=0xFFFFFFFF,
            )
            + Op.STOP
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
