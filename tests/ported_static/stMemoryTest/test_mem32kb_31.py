"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stMemoryTest/mem32kb-31Filler.json
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
    ["tests/static/state_tests/stMemoryTest/mem32kb-31Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_mem32kb_31(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xc102734f6a1e4747310179c0a0fc16e674aa901d")
    contract = Address("0xb46476112be03a9d0ea0e5c2d87fd734ee2c2687")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=42949672960,
    )

    # Source: LLL
    # { (MSTORE 31937 42) [[ 1 ]] (MLOAD 31937) [[ 0 ]] (MSIZE) }
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.MSTORE(offset=0x7CC1, value=0x2A)
            + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x7CC1))
            + Op.SSTORE(key=0x0, value=Op.MSIZE)
            + Op.STOP
        ),
    )
    pre[sender] = Account(balance=0x6400000000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x834185262e53584684bf2b72c64e510013c235d0f45e462db65900455df45a35"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=10,
    )

    post = {
        contract: Account(
            storage={0: 32000, 1: 42},
            code=(
                Op.MSTORE(offset=0x7CC1, value=0x2A)
                + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x7CC1))
                + Op.SSTORE(key=0x0, value=Op.MSIZE)
                + Op.STOP
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
