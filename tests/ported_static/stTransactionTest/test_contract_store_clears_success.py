"""
Ported from:
tests/static/state_tests/stTransactionTest/ContractStoreClearsSuccessFiller.json
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
    ["tests/static/state_tests/stTransactionTest/ContractStoreClearsSuccessFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_contract_store_clears_success(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    sender = Address("0x631b0f7cad68edb43681740bde668eda6cd68abb")
    contract = Address("0xd61e0564fab2b0da5136f75db579b663bd9f2bd8")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[sender] = Account(balance=0x8583b00, nonce=0)
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.SSTORE(key=0x0, value=0x0) + Op.SSTORE(key=0x1, value=0x0)
        + Op.SSTORE(key=0x2, value=0x0) + Op.SSTORE(key=0x3, value=0x0)
        + Op.SSTORE(key=0x4, value=0x0) + Op.SSTORE(key=0x5, value=0x0)
        + Op.SSTORE(key=0x6, value=0x0) + Op.SSTORE(key=0x7, value=0x0)
        + Op.SSTORE(key=0x8, value=0x0) + Op.SSTORE(key=0x9, value=0x0) + Op.STOP
    ),
        storage={0x0: 0xc, 0x1: 0xc, 0x2: 0xc, 0x3: 0xc, 0x4: 0xc, 0x5: 0xc, 0x6: 0xc, 0x7: 0xc, 0x8: 0xc, 0x9: 0xc},
    )

    tx = Transaction(
        secret_key=Hash(
            "0xe624afc0dccead9a7c59f0007c5c5c3b3dd36eed1cfd8f309a68c9ba3d07769b"
        ),
        to=contract,
        data=b"",
        gas_limit=130000,
        gas_price=10,
        nonce=0,
        value=10,
    )

    post = {
        contract: Account(
            code=Op.SSTORE(key=0x0, value=0x0) + Op.SSTORE(key=0x1, value=0x0) + Op.SSTORE(key=0x2, value=0x0) + Op.SSTORE(key=0x3, value=0x0) + Op.SSTORE(key=0x4, value=0x0) + Op.SSTORE(key=0x5, value=0x0) + Op.SSTORE(key=0x6, value=0x0) + Op.SSTORE(key=0x7, value=0x0) + Op.SSTORE(key=0x8, value=0x0) + Op.SSTORE(key=0x9, value=0x0) + Op.STOP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
