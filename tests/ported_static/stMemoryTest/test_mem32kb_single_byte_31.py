"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stMemoryTest/mem32kb_singleByte-31Filler.json
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
    ["tests/static/state_tests/stMemoryTest/mem32kb_singleByte-31Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_mem32kb_single_byte_31(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = EOA(
        key=0x834185262E53584684BF2B72C64E510013C235D0F45E462DB65900455DF45A35
    )
    contract = Address("0xa66b4a1cc854f0b1ac130e79071ca4d277abb87d")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=42949672960,
    )

    # Source: LLL
    # { (MSTORE8 31968 42) [[ 0 ]] (MSIZE) }
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.MSTORE8(offset=0x7CE0, value=0x2A)
            + Op.SSTORE(key=0x0, value=Op.MSIZE)
            + Op.STOP
        ),
    )
    pre[sender] = Account(balance=0x6400000000, nonce=0)

    tx = Transaction(
        sender=sender,
        to=contract,
        data=b"",
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=10,
    )

    post = {
        contract: Account(
            storage={0: 32000},
            code=(
                Op.MSTORE8(offset=0x7CE0, value=0x2A)
                + Op.SSTORE(key=0x0, value=Op.MSIZE)
                + Op.STOP
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
