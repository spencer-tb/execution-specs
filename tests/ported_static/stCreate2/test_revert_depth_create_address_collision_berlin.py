"""
copy of this test for CREATE2.

Ported from:
tests/static/state_tests/stCreate2
RevertDepthCreateAddressCollisionBerlinFiller.json
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
        "tests/static/state_tests/stCreate2/RevertDepthCreateAddressCollisionBerlinFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, tx_gas_limit, tx_value, expected_post",
    [
        (
            "000000000000000000000000000000000000000000000000000000000000ea60",
            110000,
            1,
            {
                Address("0x3e180b1862f9d158abb5e519a6d8605540c23682"): Account(
                    code=bytes.fromhex(
                        "60016000556000600060006000600073b000000000000000000000000000000000000000600035f1600155600c60045500"  # noqa: E501
                    )
                ),
                Address("0xb000000000000000000000000000000000000000"): Account(
                    code=bytes.fromhex(
                        "60086002556000600060006000f550600c60035500"
                    )
                ),
            },
        ),
        (
            "000000000000000000000000000000000000000000000000000000000000ea60",
            110000,
            0,
            {
                Address("0x3e180b1862f9d158abb5e519a6d8605540c23682"): Account(
                    code=bytes.fromhex(
                        "60016000556000600060006000600073b000000000000000000000000000000000000000600035f1600155600c60045500"  # noqa: E501
                    )
                ),
                Address("0xb000000000000000000000000000000000000000"): Account(
                    code=bytes.fromhex(
                        "60086002556000600060006000f550600c60035500"
                    )
                ),
            },
        ),
        (
            "000000000000000000000000000000000000000000000000000000000000ea60",
            170000,
            1,
            {
                Address("0x3e180b1862f9d158abb5e519a6d8605540c23682"): Account(
                    storage={0: 1, 4: 12},
                    code=bytes.fromhex(
                        "60016000556000600060006000600073b000000000000000000000000000000000000000600035f1600155600c60045500"  # noqa: E501
                    ),
                ),
                Address("0xb000000000000000000000000000000000000000"): Account(
                    code=bytes.fromhex(
                        "60086002556000600060006000f550600c60035500"
                    )
                ),
            },
        ),
        (
            "000000000000000000000000000000000000000000000000000000000000ea60",
            170000,
            0,
            {
                Address("0x3e180b1862f9d158abb5e519a6d8605540c23682"): Account(
                    storage={0: 1, 4: 12},
                    code=bytes.fromhex(
                        "60016000556000600060006000600073b000000000000000000000000000000000000000600035f1600155600c60045500"  # noqa: E501
                    ),
                ),
                Address("0xb000000000000000000000000000000000000000"): Account(
                    code=bytes.fromhex(
                        "60086002556000600060006000f550600c60035500"
                    )
                ),
            },
        ),
        (
            "000000000000000000000000000000000000000000000000000000000001ea60",
            110000,
            1,
            {
                Address("0x3e180b1862f9d158abb5e519a6d8605540c23682"): Account(
                    code=bytes.fromhex(
                        "60016000556000600060006000600073b000000000000000000000000000000000000000600035f1600155600c60045500"  # noqa: E501
                    )
                ),
                Address("0xb000000000000000000000000000000000000000"): Account(
                    code=bytes.fromhex(
                        "60086002556000600060006000f550600c60035500"
                    )
                ),
            },
        ),
        (
            "000000000000000000000000000000000000000000000000000000000001ea60",
            110000,
            0,
            {
                Address("0x3e180b1862f9d158abb5e519a6d8605540c23682"): Account(
                    code=bytes.fromhex(
                        "60016000556000600060006000600073b000000000000000000000000000000000000000600035f1600155600c60045500"  # noqa: E501
                    )
                ),
                Address("0xb000000000000000000000000000000000000000"): Account(
                    code=bytes.fromhex(
                        "60086002556000600060006000f550600c60035500"
                    )
                ),
            },
        ),
        (
            "000000000000000000000000000000000000000000000000000000000001ea60",
            170000,
            1,
            {
                Address("0x3e180b1862f9d158abb5e519a6d8605540c23682"): Account(
                    storage={0: 1, 1: 1, 4: 12},
                    code=bytes.fromhex(
                        "60016000556000600060006000600073b000000000000000000000000000000000000000600035f1600155600c60045500"  # noqa: E501
                    ),
                ),
                Address("0xb000000000000000000000000000000000000000"): Account(
                    storage={2: 8, 3: 12},
                    code=bytes.fromhex(
                        "60086002556000600060006000f550600c60035500"
                    ),
                ),
            },
        ),
        (
            "000000000000000000000000000000000000000000000000000000000001ea60",
            170000,
            0,
            {
                Address("0x3e180b1862f9d158abb5e519a6d8605540c23682"): Account(
                    storage={0: 1, 1: 1, 4: 12},
                    code=bytes.fromhex(
                        "60016000556000600060006000600073b000000000000000000000000000000000000000600035f1600155600c60045500"  # noqa: E501
                    ),
                ),
                Address("0xb000000000000000000000000000000000000000"): Account(
                    storage={2: 8, 3: 12},
                    code=bytes.fromhex(
                        "60086002556000600060006000f550600c60035500"
                    ),
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
    ],
)
@pytest.mark.pre_alloc_mutable
def test_revert_depth_create_address_collision_berlin(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    tx_gas_limit: int,
    tx_value: int,
    expected_post: dict,
) -> None:
    """Copy of this test for CREATE2."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x3e180b1862f9d158abb5e519a6d8605540c23682")
    callee = Address("0xb000000000000000000000000000000000000000")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[contract] = Account(
        balance=5,
        nonce=54,
        code=bytes.fromhex(
            "60016000556000600060006000600073b000000000000000000000000000000000000000"  # noqa: E501
            "600035f1600155600c60045500"
        ),
    )
    pre[sender] = Account(balance=0xE8D4A51000, nonce=0)
    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("60086002556000600060006000f550600c60035500"),
    )

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=tx_data,
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=tx_value,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
