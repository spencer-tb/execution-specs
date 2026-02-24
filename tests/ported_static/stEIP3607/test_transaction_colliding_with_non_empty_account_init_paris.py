"""
Account with non-empty code attempts to send tx to create a contract

Ported from:
tests/static/state_tests/stEIP3607/transactionCollidingWithNonEmptyAccount_init_ParisFiller.yml
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
    TransactionException,
)

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


@pytest.mark.ported_from(
    ["tests/static/state_tests/stEIP3607/transactionCollidingWithNonEmptyAccount_init_ParisFiller.yml"],
)
@pytest.mark.valid_from("Cancun")
@pytest.mark.parametrize(
    "tx_data_hex",
    [
        "00",
        "60206000f3",
        "60008080806127107310000000000000000000000000000000000010005af100",
        "60008080807310000000000000000000000000000000000010005af400",
    ],
    ids=['case0', 'case1', 'case2', 'case3'],
)
@pytest.mark.exception_test
def test_transaction_colliding_with_non_empty_account_init_paris(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
) -> None:
    """Account with non-empty code attempts to send tx to create a contract."""
    coinbase = Address("0x6389e7f33ce3b1e94e4325ef02829cd12297ef71")
    sender = Address("0x8a0a19589531694250d570040a0c4b74576919b8")
    contract = Address("0x1000000000000000000000000000000000001000")
    callee_1 = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=71794957647893862,
    )

    pre[contract] = Account(balance=10, nonce=0, code=bytes.fromhex("00"))
    pre[coinbase] = Account(balance=0, nonce=1)
    pre[sender] = Account(balance=0xde0b6b3a7640000, nonce=0, code=bytes.fromhex("00"))
    pre[callee_1] = Account(balance=10, nonce=0)

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x9e7645d0cfd9c3a04eb7a9db59a4eb7d359f2e75c9164a9d6b9a7d54e1b6a36f"
        ),
        to=None,
        data=tx_data,
        gas_limit=400000,
        gas_price=10,
        nonce=0,
        value=100000,
        error=TransactionException.SENDER_NOT_EOA,
    )

    post = {}

    state_test(env=env, pre=pre, post=post, tx=tx)
