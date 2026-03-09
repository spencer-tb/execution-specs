"""
Ori Pomerantz qbzzt1@gmail.com.

Ported from:
tests/static/state_tests/VMTests/vmArithmeticTest/mulFiller.yml
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
    ["tests/static/state_tests/VMTests/vmArithmeticTest/mulFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000007",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("600360020260005500")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex(
                        "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("601760000260005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("600160170260005500")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex(
                        "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f80000000000000000000000000000000000000000000000000000000000000000260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex(
                        "7f80000000000000000000000000000000000000000000000000000000000000007f80000000000000000000000000000000000000000000000000000000000000000260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex(
                        "7f7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    storage={
                        0: 0x47D0817E4167B1EB4F9FC722B133EF9D7D9A6FB4C2C1C442D000107A5E419561  # noqa: E501
                    },
                    code=bytes.fromhex(
                        "7001234567890abcdef0fedcba09876543217001234567890abcdef0fedcba09876543217001234567890abcdef0fedcba0987654321020260005500"  # noqa: E501
                    ),
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600160005560010200")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "600060006000600060006004356110000162fffffff100"
                    )
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000002",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("600360020260005500")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex(
                        "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("601760000260005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("600160170260005500")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex(
                        "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f80000000000000000000000000000000000000000000000000000000000000000260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex(
                        "7f80000000000000000000000000000000000000000000000000000000000000007f80000000000000000000000000000000000000000000000000000000000000000260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex(
                        "7f7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex(
                        "7001234567890abcdef0fedcba09876543217001234567890abcdef0fedcba09876543217001234567890abcdef0fedcba0987654321020260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600160005560010200")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "600060006000600060006004356110000162fffffff100"
                    )
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000003",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("600360020260005500")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex(
                        "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("601760000260005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    storage={0: 23}, code=bytes.fromhex("600160170260005500")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex(
                        "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f80000000000000000000000000000000000000000000000000000000000000000260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex(
                        "7f80000000000000000000000000000000000000000000000000000000000000007f80000000000000000000000000000000000000000000000000000000000000000260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex(
                        "7f7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex(
                        "7001234567890abcdef0fedcba09876543217001234567890abcdef0fedcba09876543217001234567890abcdef0fedcba0987654321020260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600160005560010200")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "600060006000600060006004356110000162fffffff100"
                    )
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000000",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    storage={0: 6}, code=bytes.fromhex("600360020260005500")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex(
                        "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("601760000260005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("600160170260005500")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex(
                        "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f80000000000000000000000000000000000000000000000000000000000000000260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex(
                        "7f80000000000000000000000000000000000000000000000000000000000000007f80000000000000000000000000000000000000000000000000000000000000000260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex(
                        "7f7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex(
                        "7001234567890abcdef0fedcba09876543217001234567890abcdef0fedcba09876543217001234567890abcdef0fedcba0987654321020260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600160005560010200")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "600060006000600060006004356110000162fffffff100"
                    )
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000005",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("600360020260005500")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex(
                        "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("601760000260005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("600160170260005500")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex(
                        "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f80000000000000000000000000000000000000000000000000000000000000000260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex(
                        "7f80000000000000000000000000000000000000000000000000000000000000007f80000000000000000000000000000000000000000000000000000000000000000260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex(
                        "7f7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex(
                        "7001234567890abcdef0fedcba09876543217001234567890abcdef0fedcba09876543217001234567890abcdef0fedcba0987654321020260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600160005560010200")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "600060006000600060006004356110000162fffffff100"
                    )
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000004",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("600360020260005500")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex(
                        "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("601760000260005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("600160170260005500")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    storage={
                        0: 0x8000000000000000000000000000000000000000000000000000000000000000  # noqa: E501
                    },
                    code=bytes.fromhex(
                        "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f80000000000000000000000000000000000000000000000000000000000000000260005500"  # noqa: E501
                    ),
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex(
                        "7f80000000000000000000000000000000000000000000000000000000000000007f80000000000000000000000000000000000000000000000000000000000000000260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex(
                        "7f7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex(
                        "7001234567890abcdef0fedcba09876543217001234567890abcdef0fedcba09876543217001234567890abcdef0fedcba0987654321020260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600160005560010200")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "600060006000600060006004356110000162fffffff100"
                    )
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000006",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("600360020260005500")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex(
                        "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("601760000260005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("600160170260005500")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex(
                        "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f80000000000000000000000000000000000000000000000000000000000000000260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex(
                        "7f80000000000000000000000000000000000000000000000000000000000000007f80000000000000000000000000000000000000000000000000000000000000000260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    storage={0: 1},
                    code=bytes.fromhex(
                        "7f7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0260005500"  # noqa: E501
                    ),
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex(
                        "7001234567890abcdef0fedcba09876543217001234567890abcdef0fedcba09876543217001234567890abcdef0fedcba0987654321020260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600160005560010200")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "600060006000600060006004356110000162fffffff100"
                    )
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000001",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("600360020260005500")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    storage={0: 1},
                    code=bytes.fromhex(
                        "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0260005500"  # noqa: E501
                    ),
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("601760000260005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("600160170260005500")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex(
                        "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f80000000000000000000000000000000000000000000000000000000000000000260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex(
                        "7f80000000000000000000000000000000000000000000000000000000000000007f80000000000000000000000000000000000000000000000000000000000000000260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex(
                        "7f7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex(
                        "7001234567890abcdef0fedcba09876543217001234567890abcdef0fedcba09876543217001234567890abcdef0fedcba0987654321020260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600160005560010200")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "600060006000600060006004356110000162fffffff100"
                    )
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000008",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("600360020260005500")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex(
                        "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("601760000260005500")
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex("600160170260005500")
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex(
                        "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f80000000000000000000000000000000000000000000000000000000000000000260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=bytes.fromhex(
                        "7f80000000000000000000000000000000000000000000000000000000000000007f80000000000000000000000000000000000000000000000000000000000000000260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001006"): Account(
                    code=bytes.fromhex(
                        "7f7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001007"): Account(
                    code=bytes.fromhex(
                        "7001234567890abcdef0fedcba09876543217001234567890abcdef0fedcba09876543217001234567890abcdef0fedcba0987654321020260005500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001008"): Account(
                    code=bytes.fromhex("600160005560010200")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "600060006000600060006004356110000162fffffff100"
                    )
                ),
            },
        ),
    ],
    ids=[
        "case0",
        "case1",
        "case2",
        "case3",
        "case4",
        "case5",
        "case6",
        "case7",
        "case8",
    ],
)
@pytest.mark.pre_alloc_mutable
def test_mul(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Ori Pomerantz qbzzt1@gmail.com."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xcccccccccccccccccccccccccccccccccccccccc")
    callee = Address("0x0000000000000000000000000000000000001000")
    callee_1 = Address("0x0000000000000000000000000000000000001001")
    callee_2 = Address("0x0000000000000000000000000000000000001002")
    callee_3 = Address("0x0000000000000000000000000000000000001003")
    callee_4 = Address("0x0000000000000000000000000000000000001004")
    callee_5 = Address("0x0000000000000000000000000000000000001005")
    callee_6 = Address("0x0000000000000000000000000000000000001006")
    callee_7 = Address("0x0000000000000000000000000000000000001007")
    callee_8 = Address("0x0000000000000000000000000000000000001008")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000,
    )

    pre[callee] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("600360020260005500"),
    )
    pre[callee_1] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex(
            "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0260005500"  # noqa: E501
        ),
    )
    pre[callee_2] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("601760000260005500"),
    )
    pre[callee_3] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("600160170260005500"),
    )
    pre[callee_4] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex(
            "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f8000"  # noqa: E501
            "0000000000000000000000000000000000000000000000000000000000000260005500"  # noqa: E501
        ),
    )
    pre[callee_5] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex(
            "7f80000000000000000000000000000000000000000000000000000000000000007f8000"  # noqa: E501
            "0000000000000000000000000000000000000000000000000000000000000260005500"  # noqa: E501
        ),
    )
    pre[callee_6] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex(
            "7f7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f7fff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0260005500"  # noqa: E501
        ),
    )
    pre[callee_7] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex(
            "7001234567890abcdef0fedcba09876543217001234567890abcdef0fedcba0987654321"  # noqa: E501
            "7001234567890abcdef0fedcba0987654321020260005500"
        ),
    )
    pre[callee_8] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("600160005560010200"),
    )
    pre[sender] = Account(balance=0xBA1A9CE0BA1A9CE, nonce=0)
    pre[contract] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("600060006000600060006004356110000162fffffff100"),
    )

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=tx_data,
        gas_limit=16777216,
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
