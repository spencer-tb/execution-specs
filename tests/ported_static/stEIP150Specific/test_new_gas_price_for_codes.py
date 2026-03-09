"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stEIP150Specific/NewGasPriceForCodesFiller.json
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
        "tests/static/state_tests/stEIP150Specific/NewGasPriceForCodesFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_new_gas_price_for_codes(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xfaa10b404ab607779993c016cd5da73ae1f29d7e")
    contract = Address("0xfd9afc8315a88141164e2a753157ea3e0f72c707")
    callee = Address("0xad9d325b811cb0701839c07c6f139f3799476798")
    callee_1 = Address("0xc572a70afaab9d01d0a2afb855bfbafb47c8211b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("601160645500"),
    )
    pre[callee_1] = Account(
        balance=111,
        nonce=0,
        code=bytes.fromhex(
            "1122334455667788991011121314151617181920212223242526272829303132"
        ),
    )
    pre[sender] = Account(balance=0xE8D4A51000, nonce=0)
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "5a6103e75273c572a70afaab9d01d0a2afb855bfbafb47c8211b3b600155601460006000"  # noqa: E501
            "73c572a70afaab9d01d0a2afb855bfbafb47c8211b3c6000516002556000546004556000"  # noqa: E501
            "600060006000600173ad9d325b811cb0701839c07c6f139f3799476798617530f1600555"  # noqa: E501
            "6000600060006000600173ad9d325b811cb0701839c07c6f139f3799476798617530f260"  # noqa: E501
            "0655600060006000600073ad9d325b811cb0701839c07c6f139f3799476798617530f460"  # noqa: E501
            "075560006000600060006000731000000000000000000000000000000000000013617530"  # noqa: E501
            "f160085573faa10b404ab607779993c016cd5da73ae1f29d7e316003555a6103e7510360"  # noqa: E501
            "0a5500"
        ),
        storage={0x0: 0x12},
    )

    tx = Transaction(
        secret_key=Hash(
            "0x4f31b3206fbf0e0e598b9b1a7d8ac86302a0ff1d8930738f1bebae9b67173e52"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=600000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        callee: Account(code=bytes.fromhex("601160645500")),
        callee_1: Account(
            code=bytes.fromhex(
                "1122334455667788991011121314151617181920212223242526272829303132"  # noqa: E501
            ),
        ),
        contract: Account(
            storage={
                0: 18,
                1: 32,
                2: 0x1122334455667788991011121314151617181920000000000000000000000000,  # noqa: E501
                3: 0xE8D4498280,
                4: 18,
                7: 1,
                8: 1,
                10: 0x2CB0A,
                100: 17,
            },
            code=bytes.fromhex(
                "5a6103e75273c572a70afaab9d01d0a2afb855bfbafb47c8211b3b60015560146000600073c572a70afaab9d01d0a2afb855bfbafb47c8211b3c6000516002556000546004556000600060006000600173ad9d325b811cb0701839c07c6f139f3799476798617530f16005556000600060006000600173ad9d325b811cb0701839c07c6f139f3799476798617530f2600655600060006000600073ad9d325b811cb0701839c07c6f139f3799476798617530f460075560006000600060006000731000000000000000000000000000000000000013617530f160085573faa10b404ab607779993c016cd5da73ae1f29d7e316003555a6103e75103600a5500"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
