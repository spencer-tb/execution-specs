"""
Ported from:
tests/static/state_tests/stMemoryStressTest/SSTORE_BoundsFiller.json
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
    ["tests/static/state_tests/stMemoryStressTest/SSTORE_BoundsFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit, expected_post",
    [
        (150000, {Address("0x1f2aee312c3c47bdeb27ff5275fddb33c543e394"): Account(code=Op.SSTORE(key=0xffffffff, value=0x1) + Op.SSTORE(key=0xffffffffffffffff, value=0x1) + Op.SSTORE(key=0xffffffffffffffffffffffffffffffff, value=0x1) + Op.SSTORE(key=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff, value=0x1) + Op.SSTORE(key=0x20, value=0xffffffff) + Op.SSTORE(key=0x40, value=0xffffffffffffffff) + Op.SSTORE(key=0x80, value=0xffffffffffffffffffffffffffffffff) + Op.SSTORE(key=0x100, value=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) + Op.STOP)}),
        (16777216, {Address("0x1f2aee312c3c47bdeb27ff5275fddb33c543e394"): Account(storage={32: 0xffffffff, 64: 0xffffffffffffffff, 128: 0xffffffffffffffffffffffffffffffff, 256: 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff, 0xffffffff: 1, 0xffffffffffffffff: 1, 0xffffffffffffffffffffffffffffffff: 1, 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff: 1}, code=Op.SSTORE(key=0xffffffff, value=0x1) + Op.SSTORE(key=0xffffffffffffffff, value=0x1) + Op.SSTORE(key=0xffffffffffffffffffffffffffffffff, value=0x1) + Op.SSTORE(key=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff, value=0x1) + Op.SSTORE(key=0x20, value=0xffffffff) + Op.SSTORE(key=0x40, value=0xffffffffffffffff) + Op.SSTORE(key=0x80, value=0xffffffffffffffffffffffffffffffff) + Op.SSTORE(key=0x100, value=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) + Op.STOP)}),
    ],
    ids=['case0', 'case1'],
)
@pytest.mark.pre_alloc_mutable
def test_sstore_bounds(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xd468b4c11201f7d9c35fe33e663dba4f904e4748")
    contract = Address("0x1f2aee312c3c47bdeb27ff5275fddb33c543e394")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.SSTORE(key=0xffffffff, value=0x1)
        + Op.SSTORE(key=0xffffffffffffffff, value=0x1)
        + Op.SSTORE(key=0xffffffffffffffffffffffffffffffff, value=0x1)
        + Op.SSTORE(key=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff, value=0x1)
        + Op.SSTORE(key=0x20, value=0xffffffff)
        + Op.SSTORE(key=0x40, value=0xffffffffffffffff)
        + Op.SSTORE(key=0x80, value=0xffffffffffffffffffffffffffffffff)
        + Op.SSTORE(key=0x100, value=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)
        + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0x7ffffffffffffffffff, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xfe5be118ad5955e30e0ffc4e1f1bbdcaa7f5a67cb1426c4ac19e32c80eccdc06"
        ),
        to=contract,
        data=b"",
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
