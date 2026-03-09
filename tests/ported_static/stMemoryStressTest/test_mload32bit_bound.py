"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stMemoryStressTest/mload32bitBoundFiller.json
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
    ["tests/static/state_tests/stMemoryStressTest/mload32bitBoundFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit, expected_post",
    [
        (
            150000,
            {
                Address("0x74639acdfe345f749d595381961dac48c3c5e56a"): Account(
                    code=bytes.fromhex("6401000000005160015500")
                )
            },
        ),
        (
            16777216,
            {
                Address("0x74639acdfe345f749d595381961dac48c3c5e56a"): Account(
                    code=bytes.fromhex("6401000000005160015500")
                )
            },
        ),
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_mload32bit_bound(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x41fc8ac27e10a2b0ce876766a5927e7493d487e0")
    contract = Address("0x74639acdfe345f749d595381961dac48c3c5e56a")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=17592320524892,
    )

    pre[sender] = Account(balance=0x3E801F4FA93760, nonce=0)
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex("6401000000005160015500"),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xa3a3360edacc183e5d6d28657fc0a09cd4819b2c73a02881b04471f81be35a5a"  # noqa: E501
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
