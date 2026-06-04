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

from .helpers import DepositInteractionBase, DepositRequest


@pytest.fixture
def prepared_requests(
    pre: Alloc, requests: List[DepositInteractionBase]
) -> List[DepositInteractionBase]:
    """
    Allocate accounts/contracts for each request in `pre` and return copies
    with the allocated state populated. The parametrize value `requests` is
    not mutated, so it stays pristine across fixture format runs.
    """
    return [r.update_pre(pre) for r in requests]


@pytest.fixture
def txs(
    fork: Fork,
    prepared_requests: List[DepositInteractionBase],
) -> List[Transaction]:
    """List of transactions to include in the block."""
    txs = []
    for r in prepared_requests:
        txs += r.transactions()
    if not fork.is_eip_enabled(8037):
        return txs
    cap = fork.transaction_gas_limit_cap()
    current_calc = fork.transaction_intrinsic_cost_calculator()
    bumped: List[Transaction] = []
    for tx in txs:
        new_gas_limit = tx.gas_limit
        # EIP-7976 raises the calldata floor above the OOG fixtures' hardcoded
        # gas_limit. Lift to the new intrinsic so the tx still OOGs on its
        # first execution opcode (no deposits applied).
        if fork.is_eip_enabled(7976):
            new_gas_limit = max(new_gas_limit, current_calc(calldata=tx.data))
        # EIP-8037 draws state gas from the reservoir above the 7825 cap.
        # Fixtures pinned at the cap need headroom for the deposit state gas.
        if cap is not None and tx.gas_limit >= cap:
            new_gas_limit = max(new_gas_limit, 2 * cap)
        if new_gas_limit != tx.gas_limit:
            bumped.append(tx.copy(gas_limit=new_gas_limit))
        else:
            bumped.append(tx)
    return bumped


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
    prepared_requests: List[DepositInteractionBase],
) -> List[DepositRequest]:
    """
    Return the list of deposit requests that should be included in each block.
    """
    valid_requests: List[DepositRequest] = []

    for d in prepared_requests:
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
