"""
Tests for [EIP-8372: Normalized state gas limit](https://eips.ethereum.org/EIPS/eip-8372).

Raw state gas answers to a scaled share of the block gas limit, and is
normalized back onto the block gas axis before the header's `gas_used`
takes the maximum of the two dimensions. Transaction-level accounting
stays raw, so receipts and the header expose the two scales side by
side.
"""

import pytest
from execution_testing import (
    Account,
    Alloc,
    Block,
    BlockchainTestFiller,
    Bytecode,
    Environment,
    Fork,
    Header,
    Op,
    Storage,
    Transaction,
    TransactionException,
    TransactionReceipt,
)

from .spec import ref_spec_8372

REFERENCE_SPEC_GIT_PATH = ref_spec_8372.git_path
REFERENCE_SPEC_VERSION = ref_spec_8372.version

pytestmark = pytest.mark.valid_from("EIP8372")


def sstore_tx_gas(fork: Fork, num_sstores: int) -> tuple[int, int]:
    """Return (execution, state) gas for a tx with N cold SSTOREs."""
    intrinsic_gas = fork.transaction_intrinsic_cost_calculator()()
    execution = intrinsic_gas + num_sstores * Op.SSTORE(0, 1).execution_cost(
        fork
    )
    state = num_sstores * Op.SSTORE(new_value=1).state_cost(fork)
    return execution, state


def sstore_tx(
    pre: Alloc, num_sstores: int, gas_limit: int
) -> tuple[Transaction, dict]:
    """Build a tx doing N zero-to-nonzero SSTOREs and its post."""
    storage = Storage()
    code = Bytecode(Op.STOP)
    for _ in range(num_sstores):
        code = Op.SSTORE(storage.store_next(1), 1) + code
    contract = pre.deploy_contract(code=code)
    tx = Transaction(to=contract, gas_limit=gas_limit, sender=pre.fund_eoa())
    return tx, {contract: Account(storage=storage)}


def test_header_gas_normalized_state_dominates(
    blockchain_test: BlockchainTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    State-heavy blocks settle the header at the normalized state gas —
    raw usage expressed back on the block gas axis — while each
    transaction's receipt keeps charging the raw amount.
    """
    num_sstores = 3
    execution, state = sstore_tx_gas(fork, num_sstores)
    tx, post = sstore_tx(pre, num_sstores, gas_limit=execution + state)
    tx.expected_receipt = TransactionReceipt(
        cumulative_gas_used=execution + state
    )
    normalized = fork.normalized_block_state_gas(state)
    assert normalized > execution, "state must dominate the header"
    blockchain_test(
        pre=pre,
        blocks=[Block(txs=[tx], header_verify=Header(gas_used=normalized))],
        post=post,
    )


def test_header_gas_execution_dominates(
    blockchain_test: BlockchainTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    A block without state growth settles the header at its execution
    gas; normalization has nothing to amplify.
    """
    data = b"\x01" * 4096
    intrinsic = fork.transaction_intrinsic_cost_calculator()
    execution = intrinsic(calldata=data)
    tx = Transaction(
        to=pre.deploy_contract(code=Op.STOP),
        data=data,
        gas_limit=execution,
        sender=pre.fund_eoa(),
    )
    blockchain_test(
        pre=pre,
        blocks=[Block(txs=[tx], header_verify=Header(gas_used=execution))],
        post={},
    )


def test_normalized_gas_invariant_under_calibration(
    blockchain_test: BlockchainTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    The proportional calibration preserves the normalized blockspace a
    state byte occupies: the header charge per fresh storage slot
    equals the slot's byte count priced at the baseline rate that maps
    the block gas limit to the unscaled 50% target.
    """
    execution, state = sstore_tx_gas(fork, 1)
    tx, post = sstore_tx(pre, 1, gas_limit=execution + state)
    # One fresh slot's bytes at the pre-calibration price: the raw
    # charge at the scaled price, undone by the same scale.
    normalized_slot = fork.normalized_block_state_gas(
        Op.SSTORE(new_value=1).state_cost(fork)
    )
    blockchain_test(
        pre=pre,
        blocks=[
            Block(txs=[tx], header_verify=Header(gas_used=normalized_slot))
        ],
        post=post,
    )


@pytest.mark.exception_test
def test_state_capacity_scaled(
    blockchain_test: BlockchainTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    A transaction whose gas limit exceeds the block's remaining scaled
    state-gas capacity is rejected, even though ample execution
    capacity remains.
    """
    block_gas_limit = 1_000_000
    state_capacity = fork.block_state_gas_limit(block_gas_limit)
    assert state_capacity < block_gas_limit, "scale must contract"

    # The first transaction's actual state usage brings the remaining
    # scaled capacity below a modest follow-up gas limit that the
    # unscaled limit would still admit.
    num_sstores = 7
    execution, state = sstore_tx_gas(fork, num_sstores)
    assert execution + state <= state_capacity, "the filler must be admissible"
    filler_tx, post = sstore_tx(pre, num_sstores, gas_limit=execution + state)

    remaining_state = state_capacity - state
    remaining_execution = block_gas_limit - execution
    rejected_gas_limit = remaining_state + 10_000
    assert rejected_gas_limit < remaining_execution, (
        "the rejection must come from the state ceiling"
    )
    rejected_tx = Transaction(
        to=pre.deploy_contract(code=Op.STOP),
        gas_limit=rejected_gas_limit,
        sender=pre.fund_eoa(),
        error=TransactionException.GAS_ALLOWANCE_EXCEEDED,
    )
    blockchain_test(
        genesis_environment=Environment(gas_limit=block_gas_limit),
        pre=pre,
        blocks=[
            Block(
                txs=[filler_tx, rejected_tx],
                gas_limit=block_gas_limit,
                exception=TransactionException.GAS_ALLOWANCE_EXCEEDED,
            )
        ],
        post={},
    )
