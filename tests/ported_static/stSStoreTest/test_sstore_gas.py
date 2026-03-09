"""
Ori Pomerantz qbzzt1@gmail.com.

Ported from:
tests/static/state_tests/stSStoreTest/sstoreGasFiller.yml
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
    ["tests/static/state_tests/stSStoreTest/sstoreGasFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_sstore_gas(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Ori Pomerantz qbzzt1@gmail.com."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x485fd0fd5c1d0409d2b772a66e98a6ac867b9d8b")
    contract = Address("0x84e1dc6705b8b9b7ffaca256c9266792bdd0943b")

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
            "600160088180808080808080611000895a61beef6000555a900303815501885a63deadbe"  # noqa: E501
            "ef6000555a900303815501875a600080555a900303815501865a600080555a9003038155"  # noqa: E501
            "01855a6112346000555a900303815501845a600084555a900303815501835a6160a76002"  # noqa: E501
            "555a900303815501825a60006003555a900303815501905a6160a76003555a9003038155"  # noqa: E501
            "50506000805560006001556000600255600060035500"
        ),
        storage={0x0: 0x60A7, 0x1: 0x60A7},
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
                4096: 5000,
                4097: 100,
                4098: 100,
                4099: 100,
                4100: 100,
                4101: 5000,
                4102: 22100,
                4103: 2200,
                4104: 20000,
            },
            code=bytes.fromhex(
                "600160088180808080808080611000895a61beef6000555a900303815501885a63deadbeef6000555a900303815501875a600080555a900303815501865a600080555a900303815501855a6112346000555a900303815501845a600084555a900303815501835a6160a76002555a900303815501825a60006003555a900303815501905a6160a76003555a900303815550506000805560006001556000600255600060035500"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
