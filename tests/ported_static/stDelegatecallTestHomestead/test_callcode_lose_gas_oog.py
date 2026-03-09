"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stDelegatecallTestHomestead
CallcodeLoseGasOOGFiller.json
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
        "tests/static/state_tests/stDelegatecallTestHomestead/CallcodeLoseGasOOGFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit, expected_post",
    [
        (
            166262,
            {
                Address("0xbe855315b63d137b74d5eed6be5cd9dde6e2478d"): Account(
                    code=bytes.fromhex(
                        "600160005401600055600060006000600073be855315b63d137b74d5eed6be5cd9dde6e2478d620186a060005402600101f46001556103e86000540260010160025500"  # noqa: E501
                    )
                )
            },
        ),
        (
            156262,
            {
                Address("0xbe855315b63d137b74d5eed6be5cd9dde6e2478d"): Account(
                    code=bytes.fromhex(
                        "600160005401600055600060006000600073be855315b63d137b74d5eed6be5cd9dde6e2478d620186a060005402600101f46001556103e86000540260010160025500"  # noqa: E501
                    )
                )
            },
        ),
        (
            600000,
            {
                Address("0xbe855315b63d137b74d5eed6be5cd9dde6e2478d"): Account(
                    storage={0: 1, 2: 1001},
                    code=bytes.fromhex(
                        "600160005401600055600060006000600073be855315b63d137b74d5eed6be5cd9dde6e2478d620186a060005402600101f46001556103e86000540260010160025500"  # noqa: E501
                    ),
                )
            },
        ),
    ],
    ids=["case0", "case1", "case2"],
)
@pytest.mark.pre_alloc_mutable
def test_callcode_lose_gas_oog(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    sender = Address("0x4768b5e50b0ebe91ae38d84a47e3179e615f9c40")
    contract = Address("0xbe855315b63d137b74d5eed6be5cd9dde6e2478d")
    callee = Address("0xd9b97c712ebce43f3c19179bbef44b550f9e8bc0")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[sender] = Account(balance=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF, nonce=0)
    pre[contract] = Account(
        balance=1024,
        nonce=0,
        code=bytes.fromhex(
            "600160005401600055600060006000600073be855315b63d137b74d5eed6be5cd9dde6e2"  # noqa: E501
            "478d620186a060005402600101f46001556103e86000540260010160025500"
        ),
    )
    pre[callee] = Account(balance=7000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xe7c72b378297589acee4e0ba3272841bcfc5e220f86de253f890274cfee9e474"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=10,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
