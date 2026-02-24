"""
BLOB002

Ported from:
tests/static/state_tests/Cancun/stEIP4844_blobtransactions/createBlobhashTxFiller.yml
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
    TransactionException,
)
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


@pytest.mark.ported_from(
    ["tests/static/state_tests/Cancun/stEIP4844_blobtransactions/createBlobhashTxFiller.yml"],
)
@pytest.mark.valid_from("Cancun")
@pytest.mark.exception_test
def test_create_blobhash_tx(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """BLOB002."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x1000000000000000000000000000000000001000")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=7,
        gas_limit=68719476736,
    )

    pre[contract] = Account(
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=Op.PUSH1[0x0] + Op.BLOBHASH + Op.PUSH1[0x0] + Op.SSTORE + Op.STOP,
    )
    pre[sender] = Account(balance=0xde0b6b3a7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=None,
        data=bytes.fromhex("00"),
        gas_limit=4000000,
        max_fee_per_gas=5000000000,
        max_priority_fee_per_gas=2,
        max_fee_per_blob_gas=10,
        blob_versioned_hashes=[Hash("0x01a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8")],
        nonce=0,
        value=100000,
        access_list=[AccessList(address=Address("0x1000000000000000000000000000000000001000"), storage_keys=[Hash("0x0000000000000000000000000000000000000000000000000000000000000000"), Hash("0x0000000000000000000000000000000000000000000000000000000000000001")])],
        error=TransactionException.TYPE_3_TX_CONTRACT_CREATION,
    )

    post = {}

    state_test(env=env, pre=pre, post=post, tx=tx)
