"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRefundTest/refund_CallToSuicideNoStorageFiller.json
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
        "tests/static/state_tests/stRefundTest/refund_CallToSuicideNoStorageFiller.json",  # noqa: E501
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
                        "735be4b33890f720eff72be0019b122e0ff75cb937ff00"
                    )
                ),
                Address("0x5be4b33890f720eff72be0019b122e0ff75cb937"): Account(
                    storage={1: 1},
                    code=bytes.fromhex(
                        "60006000600060006000734ff65047ce9c85f968689e4369c10003026a41a9600035f160005500"  # noqa: E501
                    ),
                ),
            },
        ),
        (
            "0000000000000000000000000000000000000000000000000000000000010000",
            {
                Address("0x4ff65047ce9c85f968689e4369c10003026a41a9"): Account(
                    code=bytes.fromhex(
                        "735be4b33890f720eff72be0019b122e0ff75cb937ff00"
                    )
                ),
                Address("0x5be4b33890f720eff72be0019b122e0ff75cb937"): Account(
                    storage={0: 1, 1: 1},
                    code=bytes.fromhex(
                        "60006000600060006000734ff65047ce9c85f968689e4369c10003026a41a9600035f160005500"  # noqa: E501
                    ),
                ),
            },
        ),
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_refund_call_to_suicide_no_storage(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xd96ed4431b417993ab4f4d4a656959d13c66e1dc")
    contract = Address("0x5be4b33890f720eff72be0019b122e0ff75cb937")
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
        code=bytes.fromhex("735be4b33890f720eff72be0019b122e0ff75cb937ff00"),
    )
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "60006000600060006000734ff65047ce9c85f968689e4369c10003026a41a9600035f160"  # noqa: E501
            "005500"
        ),
        storage={0x1: 0x1},
    )
    pre[sender] = Account(balance=0x2540BE400, nonce=0)

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x6f0117d3e9c684c7d6e1e6b79dc3880da2bebe77c765b171c062fdffd38a673f"  # noqa: E501
        ),
        to=contract,
        data=tx_data,
        gas_limit=10000000,
        gas_price=10,
        nonce=0,
        value=10,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
