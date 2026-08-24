"""Fork-transition tests for EIP-8115 (batched priority fees)."""

import pytest
from execution_testing import (
    Account,
    Alloc,
    Block,
    BlockchainTestFiller,
    Environment,
    Fork,
    Op,
    Storage,
    Transaction,
)

from .spec import ref_spec_8115

REFERENCE_SPEC_GIT_PATH = ref_spec_8115.git_path
REFERENCE_SPEC_VERSION = ref_spec_8115.version

FORK_TIMESTAMP = 15_000


# TODO: Un-skip when a dedicated bogota fork module exists. Under the
#  pseudo-fork model both sides of the transition execute the same
#  amsterdam spec module, so the pre-fork block cannot exhibit the
#  per-transaction crediting this test pins.
@pytest.mark.skip(
    reason=(
        "requires a real post-Amsterdam spec fork; the Bogota pseudo-fork "
        "executes Amsterdam on both sides of the transition"
    )
)
@pytest.mark.valid_at_transition_to("EIP8115")
def test_priority_fee_batching_activates_at_transition(
    blockchain_test: BlockchainTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """
    Priority fees switch from per-transaction to end-of-block crediting
    at the fork boundary: an observer reading the fee recipient's
    balance after a tipping transaction sees the accrued fee before the
    fork and the untouched pre-block balance after it.
    """
    coinbase_initial_balance = 0x1000
    coinbase = pre.fund_eoa(amount=coinbase_initial_balance)
    bob = pre.fund_eoa(amount=1)

    tip_rate = 5
    value = 100

    pre_fork = fork.fork_at(timestamp=FORK_TIMESTAMP - 1_000)
    pre_fork_gas = pre_fork.transaction_intrinsic_cost_calculator()(
        calldata=b"",
        contract_creation=False,
        access_list=[],
        sends_value=True,
    )
    pre_fork_tip = pre_fork_gas * tip_rate

    observer_storage = Storage()
    pre_fork_observer = pre.deploy_contract(
        code=Op.SSTORE(
            # Before the fork the fee is already credited when the
            # observer runs.
            observer_storage.store_next(
                coinbase_initial_balance + pre_fork_tip
            ),
            Op.BALANCE(Op.COINBASE),
        )
    )
    post_fork_observer_storage = Storage()
    post_fork_observer = pre.deploy_contract(
        code=Op.SSTORE(
            # After the fork the accrued fee is invisible mid-block.
            post_fork_observer_storage.store_next(
                coinbase_initial_balance + pre_fork_tip
            ),
            Op.BALANCE(Op.COINBASE),
        )
    )

    alice = pre.fund_eoa()
    carol = pre.fund_eoa()
    dave = pre.fund_eoa()
    erin = pre.fund_eoa()

    def tipping_transfer(sender: object) -> Transaction:
        return Transaction(
            sender=sender,
            to=bob,
            value=value,
            max_fee_per_gas=10**10,
            max_priority_fee_per_gas=tip_rate,
        )

    blocks = [
        Block(
            timestamp=FORK_TIMESTAMP - 1_000,
            fee_recipient=coinbase,
            txs=[
                tipping_transfer(alice),
                Transaction(sender=carol, to=pre_fork_observer),
            ],
        ),
        Block(
            timestamp=FORK_TIMESTAMP,
            fee_recipient=coinbase,
            txs=[
                tipping_transfer(dave),
                Transaction(sender=erin, to=post_fork_observer),
            ],
        ),
    ]

    blockchain_test(
        pre=pre,
        blocks=blocks,
        genesis_environment=Environment(base_fee_per_gas=0x7),
        post={
            pre_fork_observer: Account(storage=observer_storage),
            post_fork_observer: Account(storage=post_fork_observer_storage),
        },
    )
