"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stMemoryStressTest/mload32bitBoundFiller.json
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
    ["tests/static/state_tests/stMemoryStressTest/mload32bitBoundFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit, expected_post",
    [
        (
            150000,
            {
                Address("0x74639acdfe345f749d595381961dac48c3c5e56a"): Account(
                    code=Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x100000000))
                    + Op.STOP
                )
            },
        ),
        (
            16777216,
            {
                Address("0x74639acdfe345f749d595381961dac48c3c5e56a"): Account(
                    code=Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x100000000))
                    + Op.STOP
                )
            },
        ),
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_mload32bit_bound(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = EOA(
        key=0xA3A3360EDACC183E5D6D28657FC0A09CD4819B2C73A02881B04471F81BE35A5A
    )
    contract = Address("0x74639acdfe345f749d595381961dac48c3c5e56a")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=17592320524892,
    )

    pre[sender] = Account(balance=0x3E801F4FA93760, nonce=0)
    # Source: LLL
    # { [[ 1 ]] (MLOAD 4294967296) }
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x100000000)) + Op.STOP,
    )

    tx = Transaction(
        sender=sender,
        to=contract,
        data=b"",
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=10,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
