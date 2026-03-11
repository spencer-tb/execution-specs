"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stCreateTest/CreateOOGafterInitCodeFiller.json
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
        "tests/static/state_tests/stCreateTest/CreateOOGafterInitCodeFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit, expected_post",
    [
        (
            54000,
            {
                Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(
                    code=Op.MSTORE(
                        offset=0x0, value=0x6460016001556000526005601BF3
                    )
                    + Op.CREATE(value=0x0, offset=0x12, size=0xE)
                    + Op.STOP
                )
            },
        ),
        (
            55000,
            {
                Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(
                    code=Op.MSTORE(
                        offset=0x0, value=0x6460016001556000526005601BF3
                    )
                    + Op.CREATE(value=0x0, offset=0x12, size=0xE)
                    + Op.STOP
                ),
                Address("0xf1ecf98489fa9ed60a664fc4998db699cfa39d40"): Account(
                    code=Op.SSTORE(key=0x1, value=0x1)
                ),
            },
        ),
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_create_oo_gafter_init_code(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = EOA(
        key=0x45A915E4D060149EB4365960E6A7A45F334393093061116B197E3240065FF2D8
    )
    contract = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[sender] = Account(balance=0xE8D4A51000, nonce=0)
    # Source: LLL
    # { (MSTORE 0 0x6460016001556000526005601bf3) (CREATE 0 18 14) }
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.MSTORE(offset=0x0, value=0x6460016001556000526005601BF3)
            + Op.CREATE(value=0x0, offset=0x12, size=0xE)
            + Op.STOP
        ),
    )

    tx = Transaction(
        sender=sender,
        to=contract,
        data=b"",
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
