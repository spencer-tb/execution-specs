"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stInitCodeTest
CallContractToCreateContractNoCashFiller.json
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
    [
        "tests/static/state_tests/stInitCodeTest/CallContractToCreateContractNoCashFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_call_contract_to_create_contract_no_cash(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = EOA(
        key=0xF79127A3004ABDE26A4CBD80C428CB10F829FA11B54D36E7B326F4F4A5927ACF
    )
    contract = Address("0x985aca92559c5b1b9cd7897fec0f7c7993ad0d60")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000,
    )

    # Source: LLL
    # {(MSTORE 0 0x600c60005566602060406000f060205260076039f3)[[0]](CREATE 100000 11 21)}  # noqa: E501
    pre[contract] = Account(
        balance=0x2710,
        nonce=0,
        code=(
            Op.MSTORE(
                offset=0x0,
                value=0x600C60005566602060406000F060205260076039F3,
            )
            + Op.SSTORE(
                key=0x0,
                value=Op.CREATE(value=0x186A0, offset=0xB, size=0x15),
            )
            + Op.STOP
        ),
    )
    pre[sender] = Account(balance=0x3B9ACA00, nonce=0)

    tx = Transaction(
        sender=sender,
        to=contract,
        data=bytes.fromhex("00"),
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            code=(
                Op.MSTORE(
                    offset=0x0,
                    value=0x600C60005566602060406000F060205260076039F3,
                )
                + Op.SSTORE(
                    key=0x0,
                    value=Op.CREATE(value=0x186A0, offset=0xB, size=0x15),
                )
                + Op.STOP
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
