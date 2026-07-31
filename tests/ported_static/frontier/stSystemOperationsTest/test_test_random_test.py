"""
Run a fuzzed nested-CREATE sequence (a create inside another create's
operand chain, funded with a raw GAS reading) and verify the survivors.

Ported from:
state_tests/stSystemOperationsTest/testRandomTestFiller.json

@manually-enhanced: Do not overwrite. Hardcoded addresses, the fixed
sender key, and the per-fork gas-limit band-aids were dropped; the stored
slot key derives from the creator's nonce and the stored value from the
block timestamp.
"""

import pytest
from execution_testing import (
    Account,
    Alloc,
    Environment,
    Fork,
    StateTestFiller,
    Transaction,
    compute_create_address,
)
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"

BLOCK_NUMBER = 1
TIMESTAMP = 1000
CONTRACT_BALANCE = 10**18


@pytest.mark.ported_from(
    ["state_tests/stSystemOperationsTest/testRandomTestFiller.json"],
)
@pytest.mark.valid_from("Frontier")
def test_test_random_test(
    state_test: StateTestFiller,
    fork: Fork,
    pre: Alloc,
) -> None:
    """Store the block timestamp under the second created address."""
    env = Environment(number=BLOCK_NUMBER, timestamp=TIMESTAMP)

    # Source: raw
    # 0x424443444243434383f0155af055
    # The leading block-info reads are fuzzer junk left on the stack; the
    # first CREATE deploys an empty one-byte-initcode contract, and the
    # second (funded with a raw GAS reading as wei) supplies the storage
    # key for the final SSTORE.
    contract = pre.deploy_contract(
        code=Op.TIMESTAMP
        + Op.PREVRANDAO
        + Op.NUMBER
        + Op.PREVRANDAO
        + Op.SSTORE(
            key=Op.CREATE(
                value=Op.GAS,
                offset=Op.ISZERO(
                    Op.CREATE(value=Op.DUP4, offset=Op.NUMBER, size=Op.NUMBER)
                ),
                size=Op.NUMBER,
            ),
            value=Op.TIMESTAMP,
        ),
        balance=CONTRACT_BALANCE,
    )

    tx = Transaction(
        protected=fork.supports_protected_txs(),
        sender=pre.fund_eoa(),
        to=contract,
    )

    # The deployed creator starts at nonce 1; the second CREATE uses 2.
    second_created = compute_create_address(address=contract, nonce=2)
    post = {
        contract: Account(
            storage={second_created: TIMESTAMP},
            nonce=3,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
