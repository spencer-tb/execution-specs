"""
`POST_TX_EXEMPT` frames (EIP-7906, ethereum/EIPs#12304): leading
execution-body frames whose state changes survive a failed `POST_TX`
frame while the rest of the body reverts.
"""

import pytest
from execution_testing import (
    Account,
    Alloc,
    BalAccountExpectation,
    BalNonceChange,
    BalStorageChange,
    BalStorageSlot,
    BlockAccessListExpectation,
    Bytecode,
    Fork,
    FrameReceipt,
    Header,
    Op,
    StateTestFiller,
    Transaction,
    TransactionReceipt,
)

from tests.bogota.eip8141_frame_transactions.helpers import (
    default_code_frame_gas,
    verify_frame,
)
from tests.bogota.eip8141_frame_transactions.spec import Spec as Spec8141

from .helpers import (
    BODY_EFFECTS,
    FEE_PER_GAS,
    FUNDS,
    SLOT_A,
    WORKER_STORAGE,
    BodyEffect,
    body_frame,
    expect_eq,
    frame_transaction_gas,
    post_tx_frame,
    reverted_body_receipts,
    settled_receipt,
)
from .spec import Spec, ref_spec_7906

REFERENCE_SPEC_GIT_PATH = ref_spec_7906.git_path
REFERENCE_SPEC_VERSION = ref_spec_7906.version

pytestmark = pytest.mark.valid_from("EIP7906")

EXEMPT = Spec.POST_TX_EXEMPT_FLAG


def writer_code() -> Bytecode:
    """Return code that sets `SLOT_A` and stops."""
    return Op.SSTORE(SLOT_A, 1) + Op.STOP


@pytest.mark.parametrize("effect", BODY_EFFECTS)
@pytest.mark.parametrize(
    "assertion_fails",
    [pytest.param(False, id="holds"), pytest.param(True, id="fails")],
)
def test_exempt_frame_settles_with_validation_prefix(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    effect: BodyEffect,
    assertion_fails: bool,
) -> None:
    """
    Keep an exempt frame's state gas, refund and event when the
    assertion fails, while the non-exempt frame after it loses all
    three.
    """
    sender = pre.fund_eoa(amount=FUNDS)
    exempt_worker = pre.deploy_contract(
        code=effect.code, storage=WORKER_STORAGE
    )
    body_worker = pre.deploy_contract(code=effect.code, storage=WORKER_STORAGE)
    assertion_code = Op.REVERT(0, 0) if assertion_fails else Op.STOP
    assertion = pre.deploy_contract(code=assertion_code)
    state_cost = effect.code.state_cost(fork)
    receipts = [
        FrameReceipt(
            status=Spec8141.STATUS_SUCCESS,
            gas_used=default_code_frame_gas(fork, target_warm=True),
            state_gas_used=0,
        ),
        settled_receipt(fork, exempt_worker, effect, kept=True),
        settled_receipt(fork, body_worker, effect, kept=not assertion_fails),
        FrameReceipt(
            status=Spec8141.STATUS_FAILURE
            if assertion_fails
            else Spec8141.STATUS_SUCCESS,
            gas_used=fork.frame_entry_gas_calculator()()
            + assertion_code.execution_cost(fork),
            state_gas_used=0,
        ),
    ]
    tx = Transaction(
        sender=sender,
        max_fee_per_gas=FEE_PER_GAS,
        max_priority_fee_per_gas=0,
        frames=[
            verify_frame(),
            body_frame(
                fork,
                target=exempt_worker,
                flags=EXEMPT,
                state_gas_limit=state_cost,
            ),
            body_frame(fork, target=body_worker, state_gas_limit=state_cost),
            post_tx_frame(fork, target=assertion),
        ],
    )
    refunding_workers = 1 if assertion_fails else 2
    payer_used, block_gas_used = frame_transaction_gas(
        fork,
        tx,
        receipts,
        refundable=refunding_workers * effect.code.refund(fork),
    )
    tx.expected_receipt = TransactionReceipt(
        payer=sender, cumulative_gas_used=payer_used, frame_receipts=receipts
    )
    state_test(
        pre=pre,
        tx=tx,
        post={
            sender: Account(nonce=1, balance=FUNDS - FEE_PER_GAS * payer_used),
            exempt_worker: Account(storage=effect.kept_storage),
            body_worker: Account(
                storage=WORKER_STORAGE
                if assertion_fails
                else effect.kept_storage
            ),
        },
        blockchain_test_header_verify=Header(gas_used=block_gas_used),
    )


@pytest.mark.parametrize(
    "batch_fails",
    [
        pytest.param(False, id="batch_holds"),
        pytest.param(True, id="batch_fails"),
    ],
)
def test_exempt_atomic_batch(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    batch_fails: bool,
) -> None:
    """
    Keep an exempt atomic batch when the assertion fails, or keep its
    unrolled state when the batch itself failed, and revert the
    non-exempt frame after it either way.
    """
    sender = pre.fund_eoa()
    first = pre.deploy_contract(code=writer_code())
    second = pre.deploy_contract(
        code=Op.REVERT(0, 0) if batch_fails else writer_code()
    )
    body_writer = pre.deploy_contract(code=writer_code())
    assertion = pre.deploy_contract(code=Op.REVERT(0, 0))
    batch_receipts = (
        [
            FrameReceipt(status=Spec8141.STATUS_SUCCESS, logs=[]),
            FrameReceipt(status=Spec8141.STATUS_FAILURE),
        ]
        if batch_fails
        else [
            FrameReceipt(status=Spec8141.STATUS_SUCCESS),
            FrameReceipt(status=Spec8141.STATUS_SUCCESS),
        ]
    )
    tx = Transaction(
        sender=sender,
        frames=[
            verify_frame(),
            body_frame(
                fork, target=first, flags=Spec8141.ATOMIC_BATCH_FLAG | EXEMPT
            ),
            body_frame(fork, target=second, flags=EXEMPT),
            body_frame(fork, target=body_writer),
            post_tx_frame(fork, target=assertion),
        ],
        expected_receipt=TransactionReceipt(
            payer=sender,
            frame_receipts=[
                FrameReceipt(status=Spec8141.STATUS_SUCCESS),
                *batch_receipts,
                FrameReceipt(status=Spec8141.STATUS_SUCCESS, logs=[]),
                FrameReceipt(status=Spec8141.STATUS_FAILURE),
            ],
        ),
    )
    batch_slot = 0 if batch_fails else 1
    post = {
        sender: Account(nonce=1),
        first: Account(storage={SLOT_A: batch_slot}),
        body_writer: Account(storage={SLOT_A: 0}),
    }
    if not batch_fails:
        post[second] = Account(storage={SLOT_A: 1})
    state_test(pre=pre, tx=tx, post=post)


@pytest.mark.parametrize(
    "prefix_flags",
    [pytest.param(0, id="non_exempt"), pytest.param(EXEMPT, id="exempt")],
)
def test_frame_before_payment_approval_and_exemption(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    prefix_flags: int,
) -> None:
    """
    Treat a `SENDER` frame before the payment approval as validation
    prefix whatever its flag, so it neither changes the outcome nor
    breaks the ordering of the exempt frame in the body.
    """
    sender = pre.fund_eoa(amount=FUNDS)
    sponsor = pre.deploy_contract(
        code=Op.APPROVE(0, 0, Spec8141.APPROVE_PAYMENT), balance=FUNDS
    )
    prefix_writer = pre.deploy_contract(code=writer_code())
    exempt_writer = pre.deploy_contract(code=writer_code())
    body_writer = pre.deploy_contract(code=writer_code())
    assertion = pre.deploy_contract(code=Op.REVERT(0, 0))
    state_test(
        pre=pre,
        tx=Transaction(
            sender=sender,
            frames=[
                verify_frame(flags=Spec8141.APPROVE_EXECUTION),
                body_frame(fork, target=prefix_writer, flags=prefix_flags),
                verify_frame(target=sponsor, flags=Spec8141.APPROVE_PAYMENT),
                body_frame(fork, target=exempt_writer, flags=EXEMPT),
                body_frame(fork, target=body_writer),
                post_tx_frame(fork, target=assertion),
            ],
            expected_receipt=TransactionReceipt(
                payer=sponsor,
                frame_receipts=[
                    FrameReceipt(status=Spec8141.STATUS_SUCCESS),
                    FrameReceipt(status=Spec8141.STATUS_SUCCESS),
                    FrameReceipt(status=Spec8141.STATUS_SUCCESS),
                    FrameReceipt(status=Spec8141.STATUS_SUCCESS),
                    FrameReceipt(status=Spec8141.STATUS_SUCCESS, logs=[]),
                    FrameReceipt(status=Spec8141.STATUS_FAILURE),
                ],
            ),
        ),
        post={
            sender: Account(nonce=1, balance=FUNDS),
            prefix_writer: Account(storage={SLOT_A: 1}),
            exempt_writer: Account(storage={SLOT_A: 1}),
            body_writer: Account(storage={SLOT_A: 0}),
        },
    )


def test_exempt_flag_before_payment_approval_has_no_effect(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """
    Ignore the exempt flag on a frame before the payment approval: the
    frame is validation prefix and kept anyway, and the whole body after
    the approval reverts when the assertion fails.
    """
    sender = pre.fund_eoa(amount=FUNDS)
    sponsor = pre.deploy_contract(
        code=Op.APPROVE(0, 0, Spec8141.APPROVE_PAYMENT), balance=FUNDS
    )
    prefix_writer = pre.deploy_contract(code=writer_code())
    body_writer = pre.deploy_contract(code=writer_code())
    assertion = pre.deploy_contract(code=Op.REVERT(0, 0))
    state_test(
        pre=pre,
        tx=Transaction(
            sender=sender,
            frames=[
                verify_frame(flags=Spec8141.APPROVE_EXECUTION),
                body_frame(fork, target=prefix_writer, flags=EXEMPT),
                verify_frame(target=sponsor, flags=Spec8141.APPROVE_PAYMENT),
                body_frame(fork, target=body_writer),
                post_tx_frame(fork, target=assertion),
            ],
            expected_receipt=TransactionReceipt(
                payer=sponsor,
                frame_receipts=[
                    FrameReceipt(status=Spec8141.STATUS_SUCCESS),
                    FrameReceipt(status=Spec8141.STATUS_SUCCESS),
                    *reverted_body_receipts(fork, 1),
                ],
            ),
        ),
        post={
            sender: Account(nonce=1, balance=FUNDS),
            prefix_writer: Account(storage={SLOT_A: 1}),
            body_writer: Account(storage={SLOT_A: 0}),
        },
    )


def test_exempt_frames_after_verify_frame(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """
    Keep two consecutive exempt frames that follow a `VERIFY` frame
    after the payment approval. Only a non-exempt `DEFAULT` or `SENDER`
    frame ends the exempt run, so both writes survive the failed
    assertion while the rest of the body reverts.
    """
    sender = pre.fund_eoa()
    noop = pre.deploy_contract(code=Op.STOP)
    first_exempt = pre.deploy_contract(code=writer_code())
    second_exempt = pre.deploy_contract(code=writer_code())
    body_writer = pre.deploy_contract(code=writer_code())
    assertion = pre.deploy_contract(code=Op.REVERT(0, 0))
    state_test(
        pre=pre,
        tx=Transaction(
            sender=sender,
            frames=[
                verify_frame(),
                verify_frame(target=noop, flags=Spec8141.APPROVE_NONE),
                body_frame(fork, target=first_exempt, flags=EXEMPT),
                body_frame(fork, target=second_exempt, flags=EXEMPT),
                body_frame(fork, target=body_writer),
                post_tx_frame(fork, target=assertion),
            ],
            expected_receipt=TransactionReceipt(
                payer=sender,
                frame_receipts=[
                    FrameReceipt(status=Spec8141.STATUS_SUCCESS),
                    FrameReceipt(status=Spec8141.STATUS_SUCCESS),
                    FrameReceipt(status=Spec8141.STATUS_SUCCESS),
                    FrameReceipt(status=Spec8141.STATUS_SUCCESS),
                    FrameReceipt(status=Spec8141.STATUS_SUCCESS, logs=[]),
                    FrameReceipt(status=Spec8141.STATUS_FAILURE),
                ],
            ),
        ),
        post={
            sender: Account(nonce=1),
            first_exempt: Account(storage={SLOT_A: 1}),
            second_exempt: Account(storage={SLOT_A: 1}),
            body_writer: Account(storage={SLOT_A: 0}),
        },
    )


def test_exempt_frame_block_access_list(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """
    Record an exempt frame's write in the block access list after a
    failed assertion, while the non-exempt frame's write becomes a bare
    read.
    """
    sender = pre.fund_eoa()
    exempt_writer = pre.deploy_contract(code=writer_code())
    body_writer = pre.deploy_contract(code=writer_code())
    assertion = pre.deploy_contract(code=Op.REVERT(0, 0))
    tx = Transaction(
        sender=sender,
        frames=[
            verify_frame(),
            body_frame(fork, target=exempt_writer, flags=EXEMPT),
            body_frame(fork, target=body_writer),
            post_tx_frame(fork, target=assertion),
        ],
        expected_receipt=TransactionReceipt(
            payer=sender,
            frame_receipts=[
                FrameReceipt(status=Spec8141.STATUS_SUCCESS),
                FrameReceipt(status=Spec8141.STATUS_SUCCESS),
                *reverted_body_receipts(fork, 1)[1:],
            ],
        ),
    )
    state_test(
        pre=pre,
        tx=tx,
        expected_block_access_list=BlockAccessListExpectation(
            account_expectations={
                exempt_writer: BalAccountExpectation(
                    storage_changes=[
                        BalStorageSlot(
                            slot=SLOT_A,
                            slot_changes=[
                                BalStorageChange(
                                    block_access_index=1, post_value=1
                                )
                            ],
                        )
                    ]
                ),
                body_writer: BalAccountExpectation(
                    storage_changes=[], storage_reads=[SLOT_A]
                ),
                sender: BalAccountExpectation(
                    nonce_changes=[
                        BalNonceChange(block_access_index=1, post_nonce=1)
                    ],
                ),
            },
        ),
        post={
            sender: Account(nonce=1),
            exempt_writer: Account(storage={SLOT_A: 1}),
            body_writer: Account(storage={SLOT_A: 0}),
        },
    )


def test_assertions_read_unexempted_diff(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """
    Show every `POST_TX` frame the whole body's diff, exempt frames
    included, with the exempt frame's flag readable through `FRAMEPARAM`.
    Exemptions apply only once a later assertion fails.
    """
    sender = pre.fund_eoa()
    exempt_writer = pre.deploy_contract(code=writer_code())
    body_writer = pre.deploy_contract(code=writer_code())
    reader = pre.deploy_contract(
        code=expect_eq(Op.TXTRACE(Spec.TXTRACE_SLOTS_CHANGED, 0), 2)
        + expect_eq(Op.FRAMEPARAM(1, Spec8141.FRAMEPARAM_FLAGS), EXEMPT)
        + Op.STOP
    )
    failure = pre.deploy_contract(code=Op.REVERT(0, 0))
    tx = Transaction(
        sender=sender,
        frames=[
            verify_frame(),
            body_frame(fork, target=exempt_writer, flags=EXEMPT),
            body_frame(fork, target=body_writer),
            post_tx_frame(fork, target=reader),
            post_tx_frame(fork, target=failure),
        ],
        expected_receipt=TransactionReceipt(
            payer=sender,
            frame_receipts=[
                FrameReceipt(status=Spec8141.STATUS_SUCCESS),
                FrameReceipt(status=Spec8141.STATUS_SUCCESS),
                FrameReceipt(status=Spec8141.STATUS_SUCCESS, logs=[]),
                FrameReceipt(status=Spec8141.STATUS_SUCCESS),
                FrameReceipt(status=Spec8141.STATUS_FAILURE),
            ],
        ),
    )
    state_test(
        pre=pre,
        tx=tx,
        post={
            exempt_writer: Account(storage={SLOT_A: 1}),
            body_writer: Account(storage={SLOT_A: 0}),
        },
    )


def test_sponsor_checks_exempt_flag(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """
    Let a sponsor's `VERIFY` frame read a later frame's exempt flag
    through `FRAMEPARAM` before approving payment, so its repayment
    survives a failed assertion.
    """
    sender = pre.fund_eoa(amount=FUNDS)
    repayment_index = 2
    sponsor = pre.deploy_contract(
        code=expect_eq(
            Op.AND(
                Op.FRAMEPARAM(repayment_index, Spec8141.FRAMEPARAM_FLAGS),
                EXEMPT,
            ),
            EXEMPT,
        )
        + Op.APPROVE(0, 0, Spec8141.APPROVE_PAYMENT),
        balance=FUNDS,
    )
    repayment = pre.deploy_contract(code=writer_code())
    body_writer = pre.deploy_contract(code=writer_code())
    assertion = pre.deploy_contract(code=Op.REVERT(0, 0))
    state_test(
        pre=pre,
        tx=Transaction(
            sender=sender,
            frames=[
                verify_frame(flags=Spec8141.APPROVE_EXECUTION),
                verify_frame(target=sponsor, flags=Spec8141.APPROVE_PAYMENT),
                body_frame(fork, target=repayment, flags=EXEMPT),
                body_frame(fork, target=body_writer),
                post_tx_frame(fork, target=assertion),
            ],
            expected_receipt=TransactionReceipt(
                payer=sponsor,
                frame_receipts=[
                    FrameReceipt(status=Spec8141.STATUS_SUCCESS),
                    FrameReceipt(status=Spec8141.STATUS_SUCCESS),
                    FrameReceipt(status=Spec8141.STATUS_SUCCESS),
                    FrameReceipt(status=Spec8141.STATUS_SUCCESS, logs=[]),
                    FrameReceipt(status=Spec8141.STATUS_FAILURE),
                ],
            ),
        ),
        post={
            repayment: Account(storage={SLOT_A: 1}),
            body_writer: Account(storage={SLOT_A: 0}),
        },
    )
