"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRefundTest/refundSuicide50procentCapFiller.json
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
        "tests/static/state_tests/stRefundTest/refundSuicide50procentCapFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        (
            "00000000000000000000000000000000000000000000000000000000000001f4",
            {
                Address("0x4ff65047ce9c85f968689e4369c10003026a41a9"): Account(
                    code=bytes.fromhex(
                        "73a6cc2ca5611255d50118601aa8ece6f124fc4c45ff00"
                    )
                ),
                Address("0xa6cc2ca5611255d50118601aa8ece6f124fc4c45"): Account(
                    storage={10: 1, 23: 0x107A7},
                    code=bytes.fromhex(
                        "5a6016526001600a5560006000600060006000734ff65047ce9c85f968689e4369c10003026a41a9600035f1600b55600060015560006002556000600355600060045560006005556000600655600060075560006008555a6016510360175500"  # noqa: E501
                    ),
                ),
            },
        ),
        (
            "0000000000000000000000000000000000000000000000000000000000010000",
            {
                Address("0x4ff65047ce9c85f968689e4369c10003026a41a9"): Account(
                    code=bytes.fromhex(
                        "73a6cc2ca5611255d50118601aa8ece6f124fc4c45ff00"
                    )
                ),
                Address("0xa6cc2ca5611255d50118601aa8ece6f124fc4c45"): Account(
                    storage={10: 1, 11: 1, 23: 0x166FA},
                    code=bytes.fromhex(
                        "5a6016526001600a5560006000600060006000734ff65047ce9c85f968689e4369c10003026a41a9600035f1600b55600060015560006002556000600355600060045560006005556000600655600060075560006008555a6016510360175500"  # noqa: E501
                    ),
                ),
            },
        ),
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_refund_suicide50procent_cap(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0xeb201d2887816e041f6e807e804f64f3a7a226fe")
    sender = Address("0xc4a2ca1058df329e5da4755f9921ddaf05cbaa06")
    contract = Address("0xa6cc2ca5611255d50118601aa8ece6f124fc4c45")
    callee = Address("0x4ff65047ce9c85f968689e4369c10003026a41a9")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000,
    )

    pre[callee] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex("73a6cc2ca5611255d50118601aa8ece6f124fc4c45ff00"),
    )
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "5a6016526001600a5560006000600060006000734ff65047ce9c85f968689e4369c10003"  # noqa: E501
            "026a41a9600035f1600b5560006001556000600255600060035560006004556000600555"  # noqa: E501
            "6000600655600060075560006008555a6016510360175500"
        ),
        storage={
            0x1: 0x1,
            0x2: 0x1,
            0x3: 0x1,
            0x4: 0x1,
            0x5: 0x1,
            0x6: 0x1,
            0x7: 0x1,
            0x8: 0x1,
        },
    )
    pre[sender] = Account(balance=0x3B9ACA00, nonce=0)
    pre[coinbase] = Account(balance=0, nonce=1)

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0xf79127a3004abde26a4cbd80c428cb10f829fa11b54d36e7b326f4f4a5927acf"  # noqa: E501
        ),
        to=contract,
        data=tx_data,
        gas_limit=10000000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
