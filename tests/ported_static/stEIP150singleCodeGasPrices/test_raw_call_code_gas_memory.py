"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stEIP150singleCodeGasPrices
RawCallCodeGasMemoryFiller.json
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
        "tests/static/state_tests/stEIP150singleCodeGasPrices/RawCallCodeGasMemoryFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_raw_call_code_gas_memory(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xfaa10b404ab607779993c016cd5da73ae1f29d7e")
    contract = Address("0xefbb83cb8bb5ed4f8cbce07972c071d88020ea1f")
    callee = Address("0xe497cd0909c3691e0b6d2a42e26f36696fc27ba5")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[callee] = Account(balance=0, nonce=0, code=bytes.fromhex("5a60025500"))
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "5a600052611f406000611f406000600073e497cd0909c3691e0b6d2a42e26f36696fc27b"  # noqa: E501
            "a5617530f2505a6000510360015500"
        ),
    )
    pre[sender] = Account(balance=0xE8D4A51000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x4f31b3206fbf0e0e598b9b1a7d8ac86302a0ff1d8930738f1bebae9b67173e52"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=500000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        callee: Account(code=bytes.fromhex("5a60025500")),
        contract: Account(
            storage={1: 25608, 2: 29998},
            code=bytes.fromhex(
                "5a600052611f406000611f406000600073e497cd0909c3691e0b6d2a42e26f36696fc27ba5617530f2505a6000510360015500"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
