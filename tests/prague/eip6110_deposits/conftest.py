"""Fixtures for the EIP-6110 deposit tests."""

from typing import List

import pytest
from execution_testing import (
    Alloc,
    Block,
    BlockException,
    Fork,
    Header,
    Requests,
    Transaction,
)
from execution_testing.forks import Amsterdam

from .helpers import DepositContract, DepositInteractionBase, DepositRequest


@pytest.fixture
def update_pre(pre: Alloc, requests: List[DepositInteractionBase]) -> None:
    """
    Init state of the accounts. Every deposit transaction defines their own
    pre-state requirements, and this fixture aggregates them all.
    """
    for d in requests:
        d.update_pre(pre)


@pytest.fixture
def txs(
    fork: Fork,
    requests: List[DepositInteractionBase],
    update_pre: None,  # Fixture is used for its side effects
) -> List[Transaction]:
    """List of transactions to include in the block."""
    if fork >= Amsterdam:
        gas_costs = fork.gas_costs()
        for r in requests:
            if isinstance(r, DepositContract):
                valid_count = sum(1 for d in r.requests if d.valid)
                if valid_count > 0:
                    # Each deposit writes ~3 new storage slots in the beacon
                    # deposit contract (branch array, deposit count).
                    # At Amsterdam (EIP-8037), these SSTOREs incur state gas.
                    # Bump tx_gas_limit to provide a state gas reservoir so
                    # state gas does not consume regular execution gas.
                    r.tx_gas_limit += (
                        valid_count * 3 * gas_costs.G_STORAGE_SET
                    )
    txs = []
    for r in requests:
        txs += r.transactions()
    return txs


@pytest.fixture
def block_body_override_requests() -> List[DepositRequest] | None:
    """
    List of requests that overwrite the requests in the header. None by
    default.
    """
    return None


@pytest.fixture
def exception() -> BlockException | None:
    """Block exception expected by the tests. None by default."""
    return None


@pytest.fixture
def included_requests(
    requests: List[DepositInteractionBase],
) -> List[DepositRequest]:
    """
    Return the list of deposit requests that should be included in each block.
    """
    valid_requests: List[DepositRequest] = []

    for d in requests:
        valid_requests += d.valid_requests(10**18)

    return valid_requests


@pytest.fixture
def blocks(
    fork: Fork,
    included_requests: List[DepositRequest],
    block_body_override_requests: List[DepositRequest] | None,
    txs: List[Transaction],
    exception: BlockException | None,
) -> List[Block]:
    """List of blocks that comprise the test."""
    return [
        Block(
            txs=txs,
            header_verify=Header(
                requests_hash=Requests(
                    *included_requests,
                ),
            ),
            requests=Requests(
                *block_body_override_requests,
            ).requests_list
            if block_body_override_requests is not None
            else None,
            exception=exception,
        )
    ]
