"""
Ori Pomerantz   qbzzt1@gmail.com.

Ported from:
tests/static/state_tests/stRefundTest/refundFFFiller.yml
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
    ["tests/static/state_tests/stRefundTest/refundFFFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_refund_ff(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Ori Pomerantz   qbzzt1@gmail.com."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x5ea6a5f170e37eeaddffc85d982d261bf4b4fc7a")
    contract = Address("0xa45b53c7b70adf8ea2e910d0e826df8d895b2b49")
    callee = Address("0x7704d8a022a1ba8f3539fc82c7d7fb065abc0df3")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=1000,
        gas_limit=16777216,
    )

    pre[sender] = Account(balance=0xE8D6599218, nonce=1)
    pre[callee] = Account(balance=0, nonce=1)
    # Source: Yul
    # {
    #    selfdestruct(<eoa:0xdddddddddddddddddddddddddddddddddddddddd>)
    # }
    pre[contract] = Account(
        balance=0,
        nonce=1,
        code=(
            Op.SELFDESTRUCT(address=0x7704D8A022A1BA8F3539FC82C7D7FB065ABC0DF3)
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xd6b0676afde099a078f9d00f24d2c1cb4278546e1734927015023db0980a92c5"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex("00"),
        gas_limit=2601000,
        gas_price=1000,
        nonce=1,
        value=0,
        access_list=[],
    )

    post = {
        contract: Account(
            code=(
                Op.SELFDESTRUCT(
                    address=0x7704D8A022A1BA8F3539FC82C7D7FB065ABC0DF3,
                )
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
