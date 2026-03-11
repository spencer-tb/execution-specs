"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRefundTest/refund_getEtherBackFiller.json
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
    ["tests/static/state_tests/stRefundTest/refund_getEtherBackFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_refund_get_ether_back(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0xeb201d2887816e041f6e807e804f64f3a7a226fe")
    sender = EOA(
        key=0x29268B0C3308094249E9A06C02739F688D492D6325CA24B36EF949E5FC20AF27
    )
    contract = Address("0xf4c9fc42faeda49049e3b8e2b97a17cc2fe95718")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=228500,
    )

    pre[sender] = Account(balance=0x3CF773D0, nonce=0)
    pre[coinbase] = Account(balance=0, nonce=1)
    # Source: LLL
    # { [[ 1 ]] 0 }
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=Op.SSTORE(key=0x1, value=0x0) + Op.STOP,
        storage={0x1: 0x1},
    )

    tx = Transaction(
        sender=sender,
        to=contract,
        data=b"",
        gas_limit=228500,
        gas_price=10,
        nonce=0,
        value=10,
    )

    post = {
        contract: Account(code=Op.SSTORE(key=0x1, value=0x0) + Op.STOP),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
