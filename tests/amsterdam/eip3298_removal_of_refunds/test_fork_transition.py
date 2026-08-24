"""
Tests for EIP-3298 fork transition behavior.

Before the fork, clearing a non-zero-original slot grants the
storage-clearing refund (capped by the EIP-3529 quotient); from the fork
on, the same transaction pays gross gas in full.
"""

import pytest
from execution_testing import (
    Account,
    Alloc,
    Block,
    BlockchainTestFiller,
    Fork,
    Op,
    Transaction,
    TransactionReceipt,
)

from .spec import ref_spec_3298

REFERENCE_SPEC_GIT_PATH = ref_spec_3298.git_path
REFERENCE_SPEC_VERSION = ref_spec_3298.version


# TODO: Re-enable when a real post-Amsterdam fork module and transition
#  fork exist. The pseudo-fork shares the Amsterdam spec module, so it
#  cannot execute both sides of this behavior-changing boundary.
@pytest.mark.skip(reason="requires a real post-Amsterdam fork module")
@pytest.mark.valid_at_transition_to("EIP3298")
def test_clear_refund_across_transition(
    blockchain_test: BlockchainTestFiller, fork: Fork, pre: Alloc
) -> None:
    """
    Clear one slot on each side of the fork boundary.

    The pre-fork receipt reflects the capped clearing refund; the
    post-fork receipt reports gross gas with no refund.
    """
    code = Op.SSTORE.with_metadata(
        key_warm=False,
        original_value=1,
        current_value=1,
        new_value=0,
    )(0, 0)
    pre_fork_contract = pre.deploy_contract(code=code, storage={0: 1})
    post_fork_contract = pre.deploy_contract(code=code, storage={0: 1})
    sender = pre.fund_eoa()

    blocks = []
    expected_gas_used = []
    for timestamp, contract in (
        (14_999, pre_fork_contract),
        (15_000, post_fork_contract),
    ):
        sub_fork = fork.fork_at(timestamp=timestamp)
        intrinsic = sub_fork.transaction_intrinsic_cost_calculator()(
            return_cost_deducted_prior_execution=True
        )
        gross = (
            intrinsic
            + code.execution_cost(sub_fork)
            + code.state_cost(sub_fork)
        )
        accrued_refund = code.refund(sub_fork)
        applied_refund = min(
            accrued_refund,
            gross // sub_fork.max_refund_quotient(),
        )
        floor = sub_fork.transaction_data_floor_cost_calculator()(data=b"")
        cumulative_gas_used = max(gross - applied_refund, floor)
        expected_gas_used.append(cumulative_gas_used)

        blocks.append(
            Block(
                timestamp=timestamp,
                txs=[
                    Transaction(
                        to=contract,
                        sender=sender,
                        expected_receipt=TransactionReceipt(
                            cumulative_gas_used=cumulative_gas_used
                        ),
                    )
                ],
            )
        )

    pre_fork = fork.fork_at(timestamp=14_999)
    post_fork = fork.fork_at(timestamp=15_000)
    assert code.refund(pre_fork) > 0
    assert code.refund(post_fork) == 0
    assert expected_gas_used[0] < expected_gas_used[1]

    blockchain_test(
        pre=pre,
        blocks=blocks,
        post={
            pre_fork_contract: Account(storage={0: 0}),
            post_fork_contract: Account(storage={0: 0}),
        },
    )
