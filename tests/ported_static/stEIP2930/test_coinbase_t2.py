"""
Ori Pomerantz qbzzt1@gmail.com.

Ported from:
tests/static/state_tests/stEIP2930/coinbaseT2Filler.yml
"""

import pytest
from execution_testing import (
    AccessList,
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
    ["tests/static/state_tests/stEIP2930/coinbaseT2Filler.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_access_list",
    [
        [
            AccessList(
                address=Address("0x7704d8a022a1ba8f3539fc82c7d7fb065abc0df3"),
                storage_keys=[],
            )
        ],
        [
            AccessList(
                address=Address("0x000000000000000000000000000000000000ba5a"),
                storage_keys=[],
            )
        ],
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_coinbase_t2(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_access_list: list | None,
) -> None:
    """Ori Pomerantz qbzzt1@gmail.com."""
    coinbase = Address("0x7704d8a022a1ba8f3539fc82c7d7fb065abc0df3")
    sender = Address("0x8dab845a8398167a1c204f0e79540d619be8b473")
    contract = Address("0x30873f83c35401e315e6e5994c012f1ee8119585")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=100,
        gas_limit=71794957647893862,
    )

    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=1,
        code=bytes.fromhex(
            "5a6000526000808080620f4240737704d8a022a1ba8f3539fc82c7d7fb065abc0df35af1"  # noqa: E501
            "505a6020526021602051600051030360005500"
        ),
    )
    pre[coinbase] = Account(balance=0, nonce=1)
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=1)

    tx = Transaction(
        secret_key=Hash(
            "0xde0c95357363da5c1c5a73bd7c2781ca5c9fecc1014103b5e1d1e990ae8208ec"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex(
            "693c61390000000000000000000000000000000000000000000000000000000000000000"  # noqa: E501
        ),
        gas_limit=16777216,
        max_fee_per_gas=10000,
        max_priority_fee_per_gas=100,
        nonce=1,
        value=0,
        access_list=tx_access_list,
    )

    post = {
        contract: Account(
            storage={0: 6800},
            code=bytes.fromhex(
                "5a6000526000808080620f4240737704d8a022a1ba8f3539fc82c7d7fb065abc0df35af1505a6020526021602051600051030360005500"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
