"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stSystemOperationsTest/ABAcallsSuicide1Filler.json
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
        "tests/static/state_tests/stSystemOperationsTest/ABAcallsSuicide1Filler.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        (
            "00000000000000000000000000000000000000000000000000000000000186a0",
            {
                Address("0x095e7baea6a6c7c4c2dfeb977efac326af552d87"): Account(
                    code=bytes.fromhex(
                        "6000356000526000600060206000601873945304eb96065b2a98b57a48a06ae28d285a71b5600035f1585500"  # noqa: E501
                    )
                ),
                Address("0x945304eb96065b2a98b57a48a06ae28d285a71b5"): Account(
                    code=bytes.fromhex(
                        "6000356000526000600060206000601773095e7baea6a6c7c4c2dfeb977efac326af552d8761c35060003503f16001015855730f572e5295c57f15886f9b263e2f6d2d6c7b5ec6ff00"  # noqa: E501
                    )
                ),
            },
        ),
        (
            "00000000000000000000000000000000000000000000000000000000000486a0",
            {
                Address("0x095e7baea6a6c7c4c2dfeb977efac326af552d87"): Account(
                    code=bytes.fromhex(
                        "6000356000526000600060206000601873945304eb96065b2a98b57a48a06ae28d285a71b5600035f1585500"  # noqa: E501
                    )
                ),
                Address("0x945304eb96065b2a98b57a48a06ae28d285a71b5"): Account(
                    code=bytes.fromhex(
                        "6000356000526000600060206000601773095e7baea6a6c7c4c2dfeb977efac326af552d8761c35060003503f16001015855730f572e5295c57f15886f9b263e2f6d2d6c7b5ec6ff00"  # noqa: E501
                    )
                ),
            },
        ),
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_ab_acalls_suicide1(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x095e7baea6a6c7c4c2dfeb977efac326af552d87")
    callee = Address("0x945304eb96065b2a98b57a48a06ae28d285a71b5")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000,
    )

    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "6000356000526000600060206000601873945304eb96065b2a98b57a48a06ae28d285a71"  # noqa: E501
            "b5600035f1585500"
        ),
    )
    pre[callee] = Account(
        balance=23,
        nonce=0,
        code=bytes.fromhex(
            "6000356000526000600060206000601773095e7baea6a6c7c4c2dfeb977efac326af552d"  # noqa: E501
            "8761c35060003503f16001015855730f572e5295c57f15886f9b263e2f6d2d6c7b5ec6ff"  # noqa: E501
            "00"
        ),
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=tx_data,
        gas_limit=10000000,
        gas_price=10,
        nonce=0,
        value=100000,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
