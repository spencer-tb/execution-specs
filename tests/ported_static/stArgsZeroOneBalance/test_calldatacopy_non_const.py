"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stArgsZeroOneBalance/calldatacopyNonConstFiller.yml
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
        "tests/static/state_tests/stArgsZeroOneBalance/calldatacopyNonConstFiller.yml",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, tx_value, expected_post",
    [
        (
            "",
            0,
            {
                Address("0x444c2681920e1105c9104fb32249ddbb41cba4a0"): Account(
                    code=bytes.fromhex(
                        "73444c2681920e1105c9104fb32249ddbb41cba4a03173444c2681920e1105c9104fb32249ddbb41cba4a03173444c2681920e1105c9104fb32249ddbb41cba4a0313700"  # noqa: E501
                    )
                )
            },
        ),
        (
            "",
            1,
            {
                Address("0x444c2681920e1105c9104fb32249ddbb41cba4a0"): Account(
                    code=bytes.fromhex(
                        "73444c2681920e1105c9104fb32249ddbb41cba4a03173444c2681920e1105c9104fb32249ddbb41cba4a03173444c2681920e1105c9104fb32249ddbb41cba4a0313700"  # noqa: E501
                    )
                )
            },
        ),
        (
            "11223344",
            0,
            {
                Address("0x444c2681920e1105c9104fb32249ddbb41cba4a0"): Account(
                    code=bytes.fromhex(
                        "73444c2681920e1105c9104fb32249ddbb41cba4a03173444c2681920e1105c9104fb32249ddbb41cba4a03173444c2681920e1105c9104fb32249ddbb41cba4a0313700"  # noqa: E501
                    )
                )
            },
        ),
        (
            "11223344",
            1,
            {
                Address("0x444c2681920e1105c9104fb32249ddbb41cba4a0"): Account(
                    code=bytes.fromhex(
                        "73444c2681920e1105c9104fb32249ddbb41cba4a03173444c2681920e1105c9104fb32249ddbb41cba4a03173444c2681920e1105c9104fb32249ddbb41cba4a0313700"  # noqa: E501
                    )
                )
            },
        ),
    ],
    ids=["case0", "case1", "case2", "case3"],
)
@pytest.mark.pre_alloc_mutable
def test_calldatacopy_non_const(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    tx_value: int,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x2e3d0156d2b99a6eacba540c55f423c8f5a33143")
    contract = Address("0x444c2681920e1105c9104fb32249ddbb41cba4a0")

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
            "73444c2681920e1105c9104fb32249ddbb41cba4a03173444c2681920e1105c9104fb322"  # noqa: E501
            "49ddbb41cba4a03173444c2681920e1105c9104fb32249ddbb41cba4a0313700"
        ),
    )

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0xb1f4cbc3a50042184425a6f9e996d0910f7ba879457ce5dac5c71e498ad3c005"  # noqa: E501
        ),
        to=contract,
        data=tx_data,
        gas_limit=400000,
        gas_price=10,
        nonce=0,
        value=tx_value,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
