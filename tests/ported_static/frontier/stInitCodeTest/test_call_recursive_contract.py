"""
Test_call_recursive_contract.

Ported from:
state_tests/stInitCodeTest/CallRecursiveContractFiller.json

@manually-enhanced: Do not overwrite. This test has been manually
reviewed and enhanced. Per-era post: created contracts start at nonce
0 before EIP-161, shifting every address in the creation chain, and
without EIP-150's 63/64 attenuation the recursion affords one more
level, so the reached depth and chain nonces are pinned per era.
"""

from typing import Generator

import pytest
from execution_testing import (
    Account,
    Address,
    Alloc,
    Fork,
    StateTestFiller,
    Transaction,
    compute_create_address,
)
from execution_testing.forks import SpuriousDragon, TangerineWhistle
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


def recursive_create_calculator(
    contract: Address, first_nonce: int, child_nonce: int, depth: int
) -> Generator[Address, None, None]:
    """
    Calculate the resulting address of a contract creating contracts
    recursively.
    """
    nonce = first_nonce
    while depth > 0:
        contract = compute_create_address(address=contract, nonce=nonce)
        yield contract
        nonce = child_nonce
        depth -= 1


@pytest.mark.ported_from(
    ["state_tests/stInitCodeTest/CallRecursiveContractFiller.json"],
)
@pytest.mark.valid_from("Frontier")
def test_call_recursive_contract(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """Test_call_recursive_contract."""
    sender = pre.fund_eoa()
    # Source: lll
    # {[[ 2 ]](ADDRESS)(CODECOPY 0 0 32)(CREATE 0 0 32)}
    entry_contract = pre.deploy_contract(
        code=Op.SSTORE(key=0x2, value=Op.ADDRESS)
        + Op.CODECOPY(dest_offset=0x0, offset=0x0, size=0x20)
        + Op.CREATE(value=0x0, offset=0x0, size=0x20)
        + Op.STOP,
    )

    gas_limit = 400_000
    pre_fund_deploy_addresses = False
    if fork.is_eip_enabled(8037):
        gas_limit = 2_000_000
        # In 8037, the cost of creating an account is beared by the parent
        # creating it, so in order to not run out of gas when we return from
        # contract creation we pre-fund the accounts. This way they are
        # already in the trie and don't produce a cost.
        pre_fund_deploy_addresses = True

    tx = Transaction(
        protected=fork.supports_protected_txs(),
        sender=sender,
        to=entry_contract,
        gas_limit=gas_limit,
    )

    # EIP-161 starts created contracts at nonce 1 (0 before), moving
    # every address in the chain after the first hop; the entry
    # contract itself is deployed at nonce 1 on every fork.
    child_start_nonce = 1 if fork >= SpuriousDragon else 0
    # Without EIP-150's 63/64 attenuation the recursion affords one
    # more level before an init frame cannot pay for its store.
    expected_depth = 5 if fork >= TangerineWhistle else 6
    for i, contract in enumerate(
        recursive_create_calculator(
            entry_contract,
            first_nonce=1,
            child_nonce=child_start_nonce,
            depth=expected_depth + 1,
        )
    ):
        if pre_fund_deploy_addresses:
            pre.fund_address(contract, 1)
        if i == expected_depth - 1:
            last_expected_contract = contract
        elif i == expected_depth:
            first_unexpected_contract = contract

    first_unexpected_contract_account = Account.NONEXISTENT
    if pre_fund_deploy_addresses:
        first_unexpected_contract_account = Account(balance=1, code=b"")

    post = {
        entry_contract: Account(
            storage={2: entry_contract}, balance=0, nonce=2
        ),
        last_expected_contract: Account(
            storage={2: last_expected_contract},
            balance=1 if pre_fund_deploy_addresses else 0,
            nonce=child_start_nonce + 1,
        ),
        first_unexpected_contract: first_unexpected_contract_account,
    }

    state_test(pre=pre, post=post, tx=tx)
