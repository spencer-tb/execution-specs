"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stEIP158Specific/EXP_EmptyFiller.json
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
    ["tests/static/state_tests/stEIP158Specific/EXP_EmptyFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_exp_empty(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xfaa10b404ab607779993c016cd5da73ae1f29d7e")
    contract = Address("0x8a3c9879fc69c8c45c1201c27da63312e9e9f6fe")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "5a600052600c60000a6001555a600051036002555a6000526000600c0a6003555a600051"  # noqa: E501
            "036004555a60005267ffffffffffffffff60000a6005555a600051036006555a6000526f"  # noqa: E501
            "ffffffffffffffffffffffffffffffff60000a6007555a600051036008555a6000527fff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff60000a6009"  # noqa: E501
            "555a60005103600a555a600052600067ffffffffffffffff0a600b555a60005103600c55"  # noqa: E501
            "5a60005260006fffffffffffffffffffffffffffffffff0a600d555a60005103600e555a"  # noqa: E501
            "60005260007fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"  # noqa: E501
            "ffff0a600f555a6000510360645500"
        ),
    )
    pre[sender] = Account(balance=0xE8D4A51000, nonce=0)

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
        contract: Account(
            storage={
                2: 2280,
                3: 1,
                4: 22127,
                6: 2627,
                8: 3027,
                10: 3827,
                11: 1,
                12: 22127,
                13: 1,
                14: 22127,
                15: 1,
                100: 22127,
            },
            code=bytes.fromhex(
                "5a600052600c60000a6001555a600051036002555a6000526000600c0a6003555a600051036004555a60005267ffffffffffffffff60000a6005555a600051036006555a6000526fffffffffffffffffffffffffffffffff60000a6007555a600051036008555a6000527fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff60000a6009555a60005103600a555a600052600067ffffffffffffffff0a600b555a60005103600c555a60005260006fffffffffffffffffffffffffffffffff0a600d555a60005103600e555a60005260007fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0a600f555a6000510360645500"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
