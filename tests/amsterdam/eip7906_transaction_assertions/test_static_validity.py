"""
Static validity of frame transactions carrying `POST_TX` frames
(EIP-7906): the mode's suffix rule and its value restriction.

The first mode value beyond `POST_TX` is rejected by the EIP-8141
suite's `test_first_undefined_frame_mode`, which reads the boundary
from the fork.
"""

import pytest
from execution_testing import (
    Account,
    Alloc,
    Op,
    StateTestFiller,
    Transaction,
    TransactionException,
    TransactionReceipt,
)

from tests.amsterdam.eip8141_frame_transactions.helpers import (
    default_frame,
    sender_frame,
    verify_frame,
)

from .helpers import post_tx_frame, success_receipts
from .spec import ref_spec_7906

REFERENCE_SPEC_GIT_PATH = ref_spec_7906.git_path
REFERENCE_SPEC_VERSION = ref_spec_7906.version

pytestmark = pytest.mark.valid_from("EIP7906")


@pytest.mark.exception_test
@pytest.mark.parametrize(
    "trailing_frame",
    [
        pytest.param(sender_frame, id="sender_after_post_tx"),
        pytest.param(default_frame, id="default_after_post_tx"),
        pytest.param(verify_frame, id="verify_after_post_tx"),
    ],
)
def test_post_tx_suffix_rule(
    state_test: StateTestFiller,
    pre: Alloc,
    trailing_frame: type,
) -> None:
    """
    Reject a frame of any other mode after a `POST_TX` frame: `POST_TX`
    frames form a contiguous trailing suffix of the frame list.
    """
    sender = pre.fund_eoa()
    noop = pre.deploy_contract(code=Op.STOP)
    tx = Transaction(
        sender=sender,
        frames=[
            verify_frame(),
            post_tx_frame(target=noop),
            trailing_frame(target=noop),
        ],
        error=TransactionException.TYPE_6_INVALID_FRAME_FORMAT,
    )
    state_test(pre=pre, tx=tx, post={})


@pytest.mark.exception_test
def test_post_tx_value_rejected(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """
    Reject a `POST_TX` frame carrying value: only `SENDER` frames
    transfer value, and a `POST_TX` frame executes as `ENTRY_POINT`.
    """
    sender = pre.fund_eoa()
    noop = pre.deploy_contract(code=Op.STOP)
    tx = Transaction(
        sender=sender,
        frames=[
            verify_frame(),
            post_tx_frame(target=noop, value=1),
        ],
        error=TransactionException.TYPE_6_INVALID_FRAME_FORMAT,
    )
    state_test(pre=pre, tx=tx, post={})


def test_post_tx_suffix_valid(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """
    Accept several `POST_TX` frames as the trailing suffix of a
    transaction with an execution body.
    """
    sender = pre.fund_eoa()
    noop = pre.deploy_contract(code=Op.STOP)
    tx = Transaction(
        sender=sender,
        frames=[
            verify_frame(),
            sender_frame(target=noop),
            post_tx_frame(target=noop),
            post_tx_frame(target=noop),
        ],
        expected_receipt=TransactionReceipt(
            payer=sender, frame_receipts=success_receipts(4)
        ),
    )
    state_test(pre=pre, tx=tx, post={sender: Account(nonce=1)})
