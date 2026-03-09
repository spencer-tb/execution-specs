"""
Ori Pomerantz qbzzt1@gmail.com.

Ported from:
tests/static/state_tests/stMemoryTest/memCopySelfFiller.yml
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

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


@pytest.mark.ported_from(
    ["tests/static/state_tests/stMemoryTest/memCopySelfFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_mem_copy_self(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Ori Pomerantz qbzzt1@gmail.com."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x485fd0fd5c1d0409d2b772a66e98a6ac867b9d8b")
    contract = Address("0xb595300ac049b84c5277c7ca68a96d74ae377b85")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000,
    )

    pre[sender] = Account(balance=0xBA1A9CE0BA1A9CE, nonce=1)
    pre[contract] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex(
            "600460005b600f8110603057600a60028160008086815182555af150600051600155600a"  # noqa: E501
            "600060203e602051600255005b806011600180930102815301600456"
        ),
        storage={0x0: 0x60A7},
    )

    tx = Transaction(
        secret_key=Hash(
            "0x48dc5a9f099caaaa557742ca3a990a94be45b9969126a1bc74e5e8be5a2b5b47"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=16777216,
        gas_price=10,
        nonce=1,
        value=0,
    )

    post = {
        contract: Account(
            storage={
                0: 0x112233445566778899AABBCCDDEEFF0000000000000000000000000000000000,  # noqa: E501
                1: 0x1122112233445566778899AADDEEFF0000000000000000000000000000000000,  # noqa: E501
                2: 0x112233445566778899AA00000000000000000000000000000000000000000000,  # noqa: E501
            },
            code=bytes.fromhex(
                "600460005b600f8110603057600a60028160008086815182555af150600051600155600a600060203e602051600255005b806011600180930102815301600456"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
