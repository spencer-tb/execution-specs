"""
Ported from:
tests/static/state_tests/stArgsZeroOneBalance/sha3NonConstFiller.yml
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
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


@pytest.mark.ported_from(
    ["tests/static/state_tests/stArgsZeroOneBalance/sha3NonConstFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_value, expected_post",
    [
        (0, {Address("0x8f7eceea4b37c6f7faf5d64d64fbffbcd14b79a4"): Account(storage={0: 0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470}, code=Op.SSTORE(key=0x0, value=Op.SHA3(offset=Op.BALANCE(address=0x8f7eceea4b37c6f7faf5d64d64fbffbcd14b79a4), size=Op.BALANCE(address=0x8f7eceea4b37c6f7faf5d64d64fbffbcd14b79a4))) + Op.STOP)}),
        (1, {Address("0x8f7eceea4b37c6f7faf5d64d64fbffbcd14b79a4"): Account(storage={0: 0xbc36789e7a1e281436464229828f817d6612f7b477d66591ff96a9e064bcc98a}, code=Op.SSTORE(key=0x0, value=Op.SHA3(offset=Op.BALANCE(address=0x8f7eceea4b37c6f7faf5d64d64fbffbcd14b79a4), size=Op.BALANCE(address=0x8f7eceea4b37c6f7faf5d64d64fbffbcd14b79a4))) + Op.STOP)}),
    ],
    ids=['case0', 'case1'],
)
@pytest.mark.pre_alloc_mutable
def test_sha3_non_const(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_value: int,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x2e3d0156d2b99a6eacba540c55f423c8f5a33143")
    contract = Address("0x8f7eceea4b37c6f7faf5d64d64fbffbcd14b79a4")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    pre[sender] = Account(balance=0xde0b6b3a7640000, nonce=0)
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.SSTORE(key=0x0, value=Op.SHA3(offset=Op.BALANCE(address=0x8f7eceea4b37c6f7faf5d64d64fbffbcd14b79a4), size=Op.BALANCE(address=0x8f7eceea4b37c6f7faf5d64d64fbffbcd14b79a4)))
        + Op.STOP
    ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xb1f4cbc3a50042184425a6f9e996d0910f7ba879457ce5dac5c71e498ad3c005"
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
