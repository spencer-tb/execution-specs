"""
Fork transition coverage for EIP-7906.

`POST_TX` is a new frame mode, so a frame transaction carrying one is
invalid before the fork and valid at it. Under the pseudo-fork model the
`amsterdam` spec module carries EIP-7906 on both sides of the boundary,
so the pre-fork rejection cannot execute yet.
"""

import pytest
from execution_testing import (
    Account,
    Alloc,
    Block,
    BlockchainTestFiller,
    Op,
    Transaction,
    TransactionException,
)

from tests.amsterdam.eip8141_frame_transactions.helpers import verify_frame

from .helpers import assertion_transaction, body_frame, post_tx_frame
from .spec import ref_spec_7906

REFERENCE_SPEC_GIT_PATH = ref_spec_7906.git_path
REFERENCE_SPEC_VERSION = ref_spec_7906.version

SLOT_A = 0x0A


# TODO: Enable when a real post-Amsterdam fork can execute both sides
#  of the activation boundary with distinct spec modules.
@pytest.mark.skip(reason="requires a real post-Amsterdam fork boundary")
@pytest.mark.valid_at_transition_to("EIP7906")
def test_post_tx_frame_across_transition(
    blockchain_test: BlockchainTestFiller,
    pre: Alloc,
) -> None:
    """
    Reject a `POST_TX` frame before the fork and accept it at the fork
    block: the same transaction shape is a malformed frame list under
    EIP-8141 alone and a valid assertion once EIP-7906 activates.
    """
    sender = pre.fund_eoa()
    writer = pre.deploy_contract(code=Op.SSTORE(SLOT_A, 1) + Op.STOP)
    assertion = pre.deploy_contract(code=Op.STOP)

    pre_fork_tx = Transaction(
        sender=sender,
        frames=[verify_frame(), post_tx_frame(target=assertion)],
        error=TransactionException.TYPE_6_INVALID_FRAME_FORMAT,
    )
    post_fork_tx = assertion_transaction(
        sender,
        body=[body_frame(target=writer)],
        assertion=assertion,
    )

    blockchain_test(
        pre=pre,
        blocks=[
            Block(
                txs=[pre_fork_tx],
                timestamp=14_999,
                exception=pre_fork_tx.error,
            ),
            Block(txs=[post_fork_tx], timestamp=15_000),
        ],
        post={
            sender: Account(nonce=1),
            writer: Account(storage={SLOT_A: 1}),
        },
    )
