"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stMemoryStressTest/SSTORE_BoundsFiller.json
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
    ["tests/static/state_tests/stMemoryStressTest/SSTORE_BoundsFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit, expected_post",
    [
        (
            150000,
            {
                Address("0x1f2aee312c3c47bdeb27ff5275fddb33c543e394"): Account(
                    code=bytes.fromhex(
                        "600163ffffffff55600167ffffffffffffffff5560016fffffffffffffffffffffffffffffffff5560017fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff5563ffffffff60205567ffffffffffffffff6040556fffffffffffffffffffffffffffffffff6080557fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff6101005500"  # noqa: E501
                    )
                )
            },
        ),
        (
            16777216,
            {
                Address("0x1f2aee312c3c47bdeb27ff5275fddb33c543e394"): Account(
                    storage={
                        32: 0xFFFFFFFF,
                        64: 0xFFFFFFFFFFFFFFFF,
                        128: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                        256: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                        0xFFFFFFFF: 1,
                        0xFFFFFFFFFFFFFFFF: 1,
                        0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF: 1,
                        0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF: 1,  # noqa: E501
                    },
                    code=bytes.fromhex(
                        "600163ffffffff55600167ffffffffffffffff5560016fffffffffffffffffffffffffffffffff5560017fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff5563ffffffff60205567ffffffffffffffff6040556fffffffffffffffffffffffffffffffff6080557fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff6101005500"  # noqa: E501
                    ),
                )
            },
        ),
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_sstore_bounds(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xd468b4c11201f7d9c35fe33e663dba4f904e4748")
    contract = Address("0x1f2aee312c3c47bdeb27ff5275fddb33c543e394")

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
            "600163ffffffff55600167ffffffffffffffff5560016fffffffffffffffffffffffffff"  # noqa: E501
            "ffffff5560017fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"  # noqa: E501
            "ffffff5563ffffffff60205567ffffffffffffffff6040556fffffffffffffffffffffff"  # noqa: E501
            "ffffffffff6080557fffffffffffffffffffffffffffffffffffffffffffffffffffffff"  # noqa: E501
            "ffffffffff6101005500"
        ),
    )
    pre[sender] = Account(balance=0x7FFFFFFFFFFFFFFFFFF, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xfe5be118ad5955e30e0ffc4e1f1bbdcaa7f5a67cb1426c4ac19e32c80eccdc06"  # noqa: E501
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
