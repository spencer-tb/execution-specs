"""
Taken from https://github.com/ethereum/EIPs/blob/master/EIPS/eip-145.md.

Ported from:
tests/static/state_tests/stShift/shr_-1_1Filler.json
"""

import pytest
from execution_testing import (
    EOA,
    Account,
    Address,
    Alloc,
    Environment,
    StateTestFiller,
    Transaction,
)
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


@pytest.mark.ported_from(
    ["tests/static/state_tests/stShift/shr_-1_1Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_shr_1_1(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Taken from..."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = EOA(
        key=0xB1F4CBC3A50042184425A6F9E996D0910F7BA879457CE5DAC5C71E498AD3C005
    )
    contract = Address("0x3610b43ff3bab81bd5772e01915ac9cbb67782b9")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)
    # Source: raw bytecode
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.SSTORE(
                key=0x0,
                value=Op.SHR(
                    0x1,
                    0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                ),
            )
        ),
        storage={0x0: 0x3},
    )

    tx = Transaction(
        sender=sender,
        to=contract,
        data=b"",
        gas_limit=400000,
        gas_price=10,
        nonce=0,
        value=100000,
    )

    post = {
        contract: Account(
            storage={
                0: 0x7FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
            },
            code=(
                Op.SSTORE(
                    key=0x0,
                    value=Op.SHR(
                        0x1,
                        0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                    ),
                )
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
