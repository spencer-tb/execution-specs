"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRefundTest/refund50_1Filler.json
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
    ["tests/static/state_tests/stRefundTest/refund50_1Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_refund50_1(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0xeb201d2887816e041f6e807e804f64f3a7a226fe")
    sender = Address("0xabbef90b4b6d86caa8d6d6cd7f673a15a8de2d61")
    contract = Address("0x6737eac10f0b6ff19a1c903cafc30b26752a5af4")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    # Source: LLL
    # { [[ 1 ]] 0 [[ 2 ]] 0 [[ 3 ]] 0 [[ 4 ]] 0 [[ 5 ]] 0 }
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.SSTORE(key=0x1, value=0x0)
            + Op.SSTORE(key=0x2, value=0x0)
            + Op.SSTORE(key=0x3, value=0x0)
            + Op.SSTORE(key=0x4, value=0x0)
            + Op.SSTORE(key=0x5, value=0x0)
            + Op.STOP
        ),
        storage={0x1: 0x1, 0x2: 0x1, 0x3: 0x1, 0x4: 0x1, 0x5: 0x1},
    )
    pre[sender] = Account(balance=0x989680, nonce=0)
    pre[coinbase] = Account(balance=0, nonce=1)

    tx = Transaction(
        secret_key=Hash(
            "0xdc4efa209aecdd4c2d5201a419ea27506151b4ec687f14a613229e310932491b"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            code=(
                Op.SSTORE(key=0x1, value=0x0)
                + Op.SSTORE(key=0x2, value=0x0)
                + Op.SSTORE(key=0x3, value=0x0)
                + Op.SSTORE(key=0x4, value=0x0)
                + Op.SSTORE(key=0x5, value=0x0)
                + Op.STOP
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
