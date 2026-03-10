"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stTransactionTest/ContractStoreClearsOOGFiller.json
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
    [
        "tests/static/state_tests/stTransactionTest/ContractStoreClearsOOGFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_contract_store_clears_oog(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    sender = Address("0xdf2e264abeec114532b73774cfa1994aed66a9f6")
    contract = Address("0xc9c8ce4628bda9f8bc4a2caaebb3616f83c4305d")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000,
    )

    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=0x0)
            + Op.SSTORE(key=0x1, value=0x0)
            + Op.SSTORE(key=0x2, value=0x0)
            + Op.SSTORE(key=0x3, value=0x0)
            + Op.SSTORE(key=0x4, value=0x0)
            + Op.SSTORE(key=0x5, value=0x0)
            + Op.SSTORE(key=0x6, value=0x0)
            + Op.SSTORE(key=0x7, value=0x0)
            + Op.SSTORE(key=0x8, value=0x0)
            + Op.SSTORE(key=0x9, value=0xC)
            + Op.STOP
        ),
        storage={
            0x0: 0xC,
            0x1: 0xC,
            0x2: 0xC,
            0x3: 0xC,
            0x4: 0xC,
            0x5: 0xC,
            0x6: 0xC,
            0x7: 0xC,
            0x8: 0xC,
            0x9: 0xC,
        },
    )
    pre[sender] = Account(balance=0x1C9C380, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x2b75d0c814eb07c075fccbdd9a036faf651d9c46d7477d6c4f30772cfca90d38"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=23000,
        gas_price=10,
        nonce=0,
        value=10,
    )

    post = {
        contract: Account(
            storage={
                0: 12,
                1: 12,
                2: 12,
                3: 12,
                4: 12,
                5: 12,
                6: 12,
                7: 12,
                8: 12,
                9: 12,
            },
            code=(
                Op.SSTORE(key=0x0, value=0x0)
                + Op.SSTORE(key=0x1, value=0x0)
                + Op.SSTORE(key=0x2, value=0x0)
                + Op.SSTORE(key=0x3, value=0x0)
                + Op.SSTORE(key=0x4, value=0x0)
                + Op.SSTORE(key=0x5, value=0x0)
                + Op.SSTORE(key=0x6, value=0x0)
                + Op.SSTORE(key=0x7, value=0x0)
                + Op.SSTORE(key=0x8, value=0x0)
                + Op.SSTORE(key=0x9, value=0xC)
                + Op.STOP
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
