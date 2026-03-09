"""
Ported from:
tests/static/state_tests/stShift/sar_2^255-1_248Filler.json
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
    ["tests/static/state_tests/stShift/sar_2^255-1_248Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_sar_2_255_1_248(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x2e3d0156d2b99a6eacba540c55f423c8f5a33143")
    contract = Address("0xaca270ca7f9e766b84a13de48f52dafc92b80f8e")

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
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=(
        Op.SSTORE(key=0x0, value=Op.SAR(0xf8, 0x7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff))
    ),
        storage={0x0: 0x3},
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
        value=100000,
    )

    post = {
        contract: Account(
            storage={0: 127},
            code=Op.SSTORE(key=0x0, value=Op.SAR(0xf8, 0x7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
