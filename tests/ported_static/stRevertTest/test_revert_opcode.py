"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRevertTest/RevertOpcodeFiller.json
"""

import pytest
from execution_testing import (
    Account,
    Address,
    Alloc,
    EOA,
    Environment,
    Hash,
    StateTestFiller,
    Transaction,
)
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


@pytest.mark.ported_from(
    ["tests/static/state_tests/stRevertTest/RevertOpcodeFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit, tx_value, expected_post",
    [
        (
            800000,
            0,
            {
                Address("0xf5eaf70f313ab7c223ded96f5a804abc49bf804a"): Account(
                    code=Op.SSTORE(key=0x0, value=0x1)
                    + Op.REVERT(offset=0x0, size=0x1)
                    + Op.SSTORE(key=0x1, value=0x11)
                )
            },
        ),
        (
            800000,
            10,
            {
                Address("0xf5eaf70f313ab7c223ded96f5a804abc49bf804a"): Account(
                    code=Op.SSTORE(key=0x0, value=0x1)
                    + Op.REVERT(offset=0x0, size=0x1)
                    + Op.SSTORE(key=0x1, value=0x11)
                )
            },
        ),
        (
            30000,
            0,
            {
                Address("0xf5eaf70f313ab7c223ded96f5a804abc49bf804a"): Account(
                    code=Op.SSTORE(key=0x0, value=0x1)
                    + Op.REVERT(offset=0x0, size=0x1)
                    + Op.SSTORE(key=0x1, value=0x11)
                )
            },
        ),
        (
            30000,
            10,
            {
                Address("0xf5eaf70f313ab7c223ded96f5a804abc49bf804a"): Account(
                    code=Op.SSTORE(key=0x0, value=0x1)
                    + Op.REVERT(offset=0x0, size=0x1)
                    + Op.SSTORE(key=0x1, value=0x11)
                )
            },
        ),
    ],
    ids=["case0", "case1", "case2", "case3"],
)
@pytest.mark.pre_alloc_mutable
def test_revert_opcode(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
    tx_value: int,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = EOA(
        key=0x4F31B3206FBF0E0E598B9B1A7D8AC86302A0FF1D8930738F1BEBAE9B67173E52
    )
    contract = Address("0xf5eaf70f313ab7c223ded96f5a804abc49bf804a")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    # Source: raw bytecode
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=0x1)
            + Op.REVERT(offset=0x0, size=0x1)
            + Op.SSTORE(key=0x1, value=0x11)
        ),
    )
    pre[sender] = Account(balance=0xE8D4A51000, nonce=0)

    tx = Transaction(
        sender=sender,
        to=contract,
        data=b"",
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=tx_value,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
