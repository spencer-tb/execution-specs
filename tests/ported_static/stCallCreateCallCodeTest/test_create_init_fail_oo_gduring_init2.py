"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stCallCreateCallCodeTest
createInitFail_OOGduringInit2Filler.json
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
        "tests/static/state_tests/stCallCreateCallCodeTest/createInitFail_OOGduringInit2Filler.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_create_init_fail_oo_gduring_init2(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x095e7baea6a6c7c4c2dfeb977efac326af552d87")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    # Source: LLL
    # { (CREATE 1 0  (lll(seq [[1]] 1 (KECCAK256 0x00 0x2fffff) )0))   }
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.PUSH1[0xD]
            + Op.CODECOPY(dest_offset=0x0, offset=0xF, size=Op.DUP1)
            + Op.PUSH1[0x0]
            + Op.PUSH1[0x1]
            + Op.CREATE
            + Op.STOP
            + Op.INVALID
            + Op.SSTORE(key=0x1, value=0x1)
            + Op.SHA3(offset=0x0, size=0x2FFFFF)
            + Op.STOP
        ),
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=1000000,
        gas_price=10,
        nonce=0,
        value=100000,
    )

    post = {
        contract: Account(
            code=(
                Op.PUSH1[0xD]
                + Op.CODECOPY(dest_offset=0x0, offset=0xF, size=Op.DUP1)
                + Op.PUSH1[0x0]
                + Op.PUSH1[0x1]
                + Op.CREATE
                + Op.STOP
                + Op.INVALID
                + Op.SSTORE(key=0x1, value=0x1)
                + Op.SHA3(offset=0x0, size=0x2FFFFF)
                + Op.STOP
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
