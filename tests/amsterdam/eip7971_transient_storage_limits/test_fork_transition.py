"""Test the transient storage repricing across the activation fork."""

import pytest
from execution_testing import (
    Account,
    Alloc,
    Block,
    BlockchainTestFiller,
    CodeGasMeasure,
    Fork,
    Op,
    Transaction,
)
from execution_testing.checklists import EIPChecklist

from .spec import ref_spec_7971

REFERENCE_SPEC_GIT_PATH = ref_spec_7971.git_path
REFERENCE_SPEC_VERSION = ref_spec_7971.version


# TODO: The pseudo-fork model executes both sides of the transition on
#  the amsterdam spec module, which already carries the EIP-7971
#  behavior. Enable when a dedicated bogota fork module exists.
@pytest.mark.skip(reason="requires a dedicated bogota fork module")
@EIPChecklist.GasCostChanges.Test.ForkTransition()
@pytest.mark.valid_at_transition_to("EIP7971")
def test_tstore_gas_across_transition(
    blockchain_test: BlockchainTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """
    A fresh `TSTORE` costs the warm access cost before the transition
    and the constant write cost plus allocation after it.
    """

    def measuring_contract(at_fork: Fork) -> tuple:
        gas_costs = at_fork.gas_costs()
        store = Op.TSTORE(1, 1)
        address = pre.deploy_contract(
            CodeGasMeasure(
                code=store,
                overhead_cost=store.gas_cost(at_fork)
                - Op.TSTORE.gas_cost(at_fork),
            )
        )
        expected = gas_costs.OPCODE_TSTORE + gas_costs.OPCODE_TSTORE_ALLOCATE
        return address, expected

    sender = pre.fund_eoa()
    before, expected_before = measuring_contract(
        fork.fork_at(timestamp=14_999)
    )
    after, expected_after = measuring_contract(fork.fork_at(timestamp=15_000))
    blocks = [
        Block(
            timestamp=14_999,
            txs=[Transaction(sender=sender, to=before)],
        ),
        Block(
            timestamp=15_000,
            txs=[Transaction(sender=sender, to=after)],
        ),
    ]
    post = {
        before: Account(storage={0: expected_before}),
        after: Account(storage={0: expected_after}),
    }
    blockchain_test(pre=pre, post=post, blocks=blocks)
