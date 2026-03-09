"""
Revert undoes the transient storage writes after a successful call.

Ported from:
tests/static/state_tests/Cancun/stEIP1153_transientStorage
10_revertUndoesStoreAfterReturnFiller.yml
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
    [
        "tests/static/state_tests/Cancun/stEIP1153_transientStorage/10_revertUndoesStoreAfterReturnFiller.yml",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_10_revert_undoes_store_after_return(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Revert undoes the transient storage writes after a successful call."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xcef5f3b33e31360216fab2c61046840df9bd788e")
    contract = Address("0xe42b9e92d5348b0fc6353d40e3d220c316d3c685")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=4503599627370496,
    )

    pre[sender] = Account(balance=0x3635C9ADC5DEA00000, nonce=0)
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "5f3560e01c806370ac643e14602f57806376b85d2314602b57634ccca55314602357005b"  # noqa: E501
            "60296076565b005b605c565b50602960055f5d5f5c5f556376b85d2360e01b5f5260205f"  # noqa: E501
            "818180305af16001555f516002555f5c600355565b634ccca55360e01b5f525f80602081"  # noqa: E501
            "80305af15f5260205ffd5b60065f5d56"
        ),
        storage={0x1: 0xFFFF},
    )

    tx = Transaction(
        secret_key=Hash(
            "0xbe0e7d5fea1604bf57e004b0b414df8de04816dbb1c8f8719b725d0d6619b531"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex("70ac643e"),
        gas_limit=400000,
        max_fee_per_gas=2000,
        max_priority_fee_per_gas=0,
        nonce=0,
        value=0,
        access_list=[],
    )

    post = {
        contract: Account(
            storage={0: 5, 2: 1, 3: 5},
            code=bytes.fromhex(
                "5f3560e01c806370ac643e14602f57806376b85d2314602b57634ccca55314602357005b60296076565b005b605c565b50602960055f5d5f5c5f556376b85d2360e01b5f5260205f818180305af16001555f516002555f5c600355565b634ccca55360e01b5f525f8060208180305af15f5260205ffd5b60065f5d56"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
