"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stArgsZeroOneBalance/callNonConstFiller.yml
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
    ["tests/static/state_tests/stArgsZeroOneBalance/callNonConstFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_value, expected_post",
    [
        (
            0,
            {
                Address("0x7d7e1645af7df916da558f0695e9dedd23b1215e"): Account(
                    storage={0: 1},
                    code=bytes.fromhex(
                        "737d7e1645af7df916da558f0695e9dedd23b1215e31737d7e1645af7df916da558f0695e9dedd23b1215e31737d7e1645af7df916da558f0695e9dedd23b1215e31737d7e1645af7df916da558f0695e9dedd23b1215e31737d7e1645af7df916da558f0695e9dedd23b1215e31737d7e1645af7df916da558f0695e9dedd23b1215e31737d7e1645af7df916da558f0695e9dedd23b1215e31f160005500"  # noqa: E501
                    ),
                )
            },
        ),
        (
            1,
            {
                Address("0x7d7e1645af7df916da558f0695e9dedd23b1215e"): Account(
                    code=bytes.fromhex(
                        "737d7e1645af7df916da558f0695e9dedd23b1215e31737d7e1645af7df916da558f0695e9dedd23b1215e31737d7e1645af7df916da558f0695e9dedd23b1215e31737d7e1645af7df916da558f0695e9dedd23b1215e31737d7e1645af7df916da558f0695e9dedd23b1215e31737d7e1645af7df916da558f0695e9dedd23b1215e31737d7e1645af7df916da558f0695e9dedd23b1215e31f160005500"  # noqa: E501
                    )
                )
            },
        ),
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_call_non_const(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_value: int,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x2e3d0156d2b99a6eacba540c55f423c8f5a33143")
    contract = Address("0x7d7e1645af7df916da558f0695e9dedd23b1215e")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "737d7e1645af7df916da558f0695e9dedd23b1215e31737d7e1645af7df916da558f0695"  # noqa: E501
            "e9dedd23b1215e31737d7e1645af7df916da558f0695e9dedd23b1215e31737d7e1645af"  # noqa: E501
            "7df916da558f0695e9dedd23b1215e31737d7e1645af7df916da558f0695e9dedd23b121"  # noqa: E501
            "5e31737d7e1645af7df916da558f0695e9dedd23b1215e31737d7e1645af7df916da558f"  # noqa: E501
            "0695e9dedd23b1215e31f160005500"
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xb1f4cbc3a50042184425a6f9e996d0910f7ba879457ce5dac5c71e498ad3c005"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=400000,
        gas_price=10,
        nonce=0,
        value=tx_value,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
