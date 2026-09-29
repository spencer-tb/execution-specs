"""
Execution semantics of `POST_TX` frames (EIP-7906): read-only trailing
frames whose failure reverts the execution body without invalidating
the transaction, and the only context the diff instructions run in.
"""

import pytest
from execution_testing import (
    Account,
    Alloc,
    BalAccountExpectation,
    BalBalanceChange,
    BalNonceChange,
    BalStorageChange,
    BalStorageSlot,
    Block,
    BlockAccessListExpectation,
    BlockchainTestFiller,
    Bytecode,
    Fork,
    FrameReceipt,
    Header,
    Op,
    StateTestFiller,
    Transaction,
    TransactionException,
    TransactionReceipt,
)

from tests.amsterdam.eip8141_frame_transactions.helpers import (
    default_code_frame_gas,
    default_frame,
    sender_frame,
    verify_frame,
)
from tests.amsterdam.eip8141_frame_transactions.spec import Spec as Spec8141

from .helpers import (
    BODY_FRAME_GAS,
    MARKER,
    SLOT_MARKER,
    assertion_transaction,
    body_frame,
    expect_eq,
    post_tx_frame,
    reverted_body_receipts,
    success_receipts,
)
from .spec import Spec, ref_spec_7906

REFERENCE_SPEC_GIT_PATH = ref_spec_7906.git_path
REFERENCE_SPEC_VERSION = ref_spec_7906.version

pytestmark = pytest.mark.valid_from("EIP7906")

SLOT_A = 0x0A
SLOT_B = 0x0B

RECIPIENT_FUNDS = 1_000
VALUE = 7


def test_post_tx_success_commits_body(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """
    Commit the execution body when the trailing `POST_TX` frame
    succeeds: the assertion observes the body's single slot change and
    accepts it.
    """
    sender = pre.fund_eoa()
    writer = pre.deploy_contract(code=Op.SSTORE(SLOT_A, 1) + Op.STOP)
    assertion = pre.deploy_contract(
        code=expect_eq(Op.TXTRACE(Spec.TXTRACE_SLOTS_CHANGED, 0), 1) + Op.STOP
    )

    state_test(
        pre=pre,
        tx=assertion_transaction(
            sender,
            body=[body_frame(target=writer)],
            assertion=assertion,
            frame_receipts=success_receipts(3),
        ),
        post={
            sender: Account(nonce=1),
            writer: Account(storage={SLOT_A: 1}),
        },
    )


@pytest.mark.parametrize(
    "failure",
    [
        pytest.param(Op.REVERT(0, 0), id="revert"),
        pytest.param(Op.INVALID, id="invalid_opcode"),
        pytest.param(Op.JUMP(1), id="bad_jump"),
    ],
)
def test_post_tx_failure_reverts_body(
    state_test: StateTestFiller,
    pre: Alloc,
    failure: Bytecode,
) -> None:
    """
    Revert the execution body when the `POST_TX` frame reverts or halts
    exceptionally, keeping the transaction valid: the validation
    prefix's nonce bump stays, the body's slot write and log are
    discarded, and the assertion frame's receipt reports failure.
    """
    sender = pre.fund_eoa()
    writer = pre.deploy_contract(
        code=Op.SSTORE(SLOT_A, 1) + Op.LOG0(0, 0) + Op.STOP
    )
    assertion = pre.deploy_contract(code=failure)

    state_test(
        pre=pre,
        tx=assertion_transaction(
            sender,
            body=[body_frame(target=writer)],
            assertion=assertion,
            frame_receipts=reverted_body_receipts(1),
        ),
        post={
            sender: Account(nonce=1),
            writer: Account(storage={SLOT_A: 0}),
        },
    )


def test_post_tx_failure_overrides_atomic_batch(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """
    Revert a committed atomic batch together with the rest of the body
    when the `POST_TX` frame fails: the batch's own all-or-nothing rule
    is superseded by the unconditional body revert.
    """
    sender = pre.fund_eoa()
    writer_a = pre.deploy_contract(code=Op.SSTORE(SLOT_A, 1) + Op.STOP)
    writer_b = pre.deploy_contract(code=Op.SSTORE(SLOT_B, 1) + Op.STOP)
    assertion = pre.deploy_contract(code=Op.REVERT(0, 0))

    state_test(
        pre=pre,
        tx=assertion_transaction(
            sender,
            body=[
                body_frame(target=writer_a, flags=Spec8141.ATOMIC_BATCH_FLAG),
                body_frame(target=writer_b),
            ],
            assertion=assertion,
            frame_receipts=reverted_body_receipts(2),
        ),
        post={
            sender: Account(nonce=1),
            writer_a: Account(storage={SLOT_A: 0}),
            writer_b: Account(storage={SLOT_B: 0}),
        },
    )


@pytest.mark.parametrize("post_tx_fails", [False, True])
def test_post_tx_terminates_atomic_batch(
    state_test: StateTestFiller,
    pre: Alloc,
    post_tx_fails: bool,
) -> None:
    """
    Accept a `POST_TX` frame as the terminating frame of an atomic batch
    opened by the last body frame: EIP-8141 only bars `VERIFY` frames
    from batches and EIP-7906 adds no flag rule for `POST_TX` frames.
    The batch has no effect of its own: a passing assertion commits the
    body, and a failing one reverts it as it would unbatched.
    """
    sender = pre.fund_eoa()
    writer = pre.deploy_contract(code=Op.SSTORE(SLOT_A, 1) + Op.STOP)
    assertion = pre.deploy_contract(
        code=Op.REVERT(0, 0) if post_tx_fails else Op.STOP
    )

    state_test(
        pre=pre,
        tx=assertion_transaction(
            sender,
            body=[
                body_frame(target=writer, flags=Spec8141.ATOMIC_BATCH_FLAG),
            ],
            assertion=assertion,
            frame_receipts=reverted_body_receipts(1)
            if post_tx_fails
            else success_receipts(3),
        ),
        post={
            sender: Account(nonce=1),
            writer: Account(storage={SLOT_A: 0 if post_tx_fails else 1}),
        },
    )


@pytest.mark.parametrize(
    "post_tx_fails",
    [pytest.param(False, id="holds"), pytest.param(True, id="fails")],
)
def test_post_tx_block_access_list(
    blockchain_test: BlockchainTestFiller,
    pre: Alloc,
    post_tx_fails: bool,
) -> None:
    """
    Record the execution body's changes in the block access list only
    when the assertion holds. A failed `POST_TX` frame re-files the
    body's storage write as a bare access and leaves the transfer
    recipient as a touched account without changes, as an atomic batch
    unroll does; the sender's nonce bump in the validation prefix stays.
    """
    sender = pre.fund_eoa()
    recipient = pre.fund_eoa(amount=RECIPIENT_FUNDS)
    writer = pre.deploy_contract(code=Op.SSTORE(SLOT_A, 1) + Op.STOP)
    assertion = pre.deploy_contract(
        code=Op.REVERT(0, 0) if post_tx_fails else Op.STOP
    )

    tx = assertion_transaction(
        sender,
        body=[
            body_frame(target=writer),
            body_frame(target=recipient, value=VALUE),
        ],
        assertion=assertion,
        frame_receipts=reverted_body_receipts(2)
        if post_tx_fails
        else success_receipts(4),
    )

    if post_tx_fails:
        writer_expectation = BalAccountExpectation(
            storage_changes=[], storage_reads=[SLOT_A]
        )
        recipient_expectation = BalAccountExpectation.empty()
    else:
        writer_expectation = BalAccountExpectation(
            storage_changes=[
                BalStorageSlot(
                    slot=SLOT_A,
                    slot_changes=[
                        BalStorageChange(block_access_index=1, post_value=1)
                    ],
                )
            ]
        )
        recipient_expectation = BalAccountExpectation(
            balance_changes=[
                BalBalanceChange(
                    block_access_index=1,
                    post_balance=RECIPIENT_FUNDS + VALUE,
                )
            ]
        )

    blockchain_test(
        pre=pre,
        blocks=[
            Block(
                txs=[tx],
                expected_block_access_list=BlockAccessListExpectation(
                    account_expectations={
                        writer: writer_expectation,
                        recipient: recipient_expectation,
                        # The assertion only reads; it is touched either
                        # way.
                        assertion: BalAccountExpectation.empty(),
                        sender: BalAccountExpectation(
                            nonce_changes=[
                                BalNonceChange(
                                    block_access_index=1, post_nonce=1
                                )
                            ],
                        ),
                    },
                ),
            )
        ],
        post={
            sender: Account(nonce=1),
            writer: Account(storage={SLOT_A: 0 if post_tx_fails else 1}),
            recipient: Account(
                balance=RECIPIENT_FUNDS
                if post_tx_fails
                else RECIPIENT_FUNDS + VALUE
            ),
        },
    )


def test_post_tx_failure_skips_remaining_frames(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """
    Skip the `POST_TX` frames after a failed one: the body is already
    reverted, so the later assertion has nothing left to observe and
    reports the skipped status with no gas used.
    """
    sender = pre.fund_eoa()
    writer = pre.deploy_contract(code=Op.SSTORE(SLOT_A, 1) + Op.STOP)
    failing = pre.deploy_contract(code=Op.REVERT(0, 0))
    passing = pre.deploy_contract(code=Op.STOP)

    tx = assertion_transaction(
        sender,
        body=[body_frame(target=writer)],
        assertion=[failing, passing],
        frame_receipts=[
            *reverted_body_receipts(1),
            FrameReceipt(status=Spec8141.STATUS_SKIPPED, gas_used=0),
        ],
    )

    state_test(
        pre=pre,
        tx=tx,
        post={
            sender: Account(nonce=1),
            writer: Account(storage={SLOT_A: 0}),
        },
    )


@pytest.mark.parametrize("second_fails", [False, True])
def test_multiple_post_tx_frames(
    state_test: StateTestFiller,
    pre: Alloc,
    second_fails: bool,
) -> None:
    """
    Compose independent assertions: every `POST_TX` frame must pass for
    the body to commit, and a later one failing reverts the body even
    though an earlier one accepted it.
    """
    sender = pre.fund_eoa()
    writer = pre.deploy_contract(code=Op.SSTORE(SLOT_A, 1) + Op.STOP)
    first = pre.deploy_contract(
        code=expect_eq(Op.TXTRACE(Spec.TXTRACE_SLOTS_CHANGED, 0), 1) + Op.STOP
    )
    second = pre.deploy_contract(
        code=Op.REVERT(0, 0) if second_fails else Op.STOP
    )

    if second_fails:
        receipts = [
            FrameReceipt(status=Spec8141.STATUS_SUCCESS),
            FrameReceipt(status=Spec8141.STATUS_SUCCESS, logs=[]),
            FrameReceipt(status=Spec8141.STATUS_SUCCESS),
            FrameReceipt(status=Spec8141.STATUS_FAILURE),
        ]
    else:
        receipts = success_receipts(4)

    tx = assertion_transaction(
        sender,
        body=[body_frame(target=writer)],
        assertion=[first, second],
        frame_receipts=receipts,
    )

    state_test(
        pre=pre,
        tx=tx,
        post={
            sender: Account(nonce=1),
            writer: Account(storage={SLOT_A: 0 if second_fails else 1}),
        },
    )


@pytest.mark.parametrize(
    "violation",
    [
        pytest.param(Op.SSTORE(SLOT_B, 1), id="sstore"),
        pytest.param(Op.TSTORE(SLOT_B, 1), id="tstore"),
        pytest.param(Op.LOG0(0, 0), id="log"),
        pytest.param(Op.CREATE(0, 0, 0), id="create"),
        pytest.param(
            Op.APPROVE(0, 0, Spec8141.APPROVE_EXECUTION_AND_PAYMENT),
            id="approve",
        ),
    ],
)
def test_post_tx_is_static(
    state_test: StateTestFiller,
    pre: Alloc,
    violation: Bytecode,
) -> None:
    """
    Execute the `POST_TX` frame as a `STATICCALL`: any state-changing
    instruction halts it exceptionally, `APPROVE` included, since the
    `VERIFY` frames' approval exception is not granted here. The halt
    reverts the body like any other assertion failure.
    """
    sender = pre.fund_eoa()
    writer = pre.deploy_contract(code=Op.SSTORE(SLOT_A, 1) + Op.STOP)
    assertion = pre.deploy_contract(code=violation + Op.STOP)

    state_test(
        pre=pre,
        tx=assertion_transaction(
            sender,
            body=[body_frame(target=writer)],
            assertion=assertion,
            frame_receipts=reverted_body_receipts(1),
        ),
        post={
            sender: Account(nonce=1),
            writer: Account(storage={SLOT_A: 0}),
            assertion: Account(storage={SLOT_B: 0}),
        },
    )


def test_post_tx_caller_and_origin(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """
    Execute a `POST_TX` frame as `ENTRY_POINT`, like `DEFAULT` and
    `VERIFY` frames: both the caller and the origin the frame observes
    are the entry point, not the sender.
    """
    sender = pre.fund_eoa()
    writer = pre.deploy_contract(code=Op.SSTORE(SLOT_A, 1) + Op.STOP)
    assertion = pre.deploy_contract(
        code=expect_eq(Op.CALLER, Spec8141.ENTRY_POINT)
        + expect_eq(Op.ORIGIN, Spec8141.ENTRY_POINT)
        + Op.STOP
    )

    state_test(
        pre=pre,
        tx=assertion_transaction(
            sender,
            body=[body_frame(target=writer)],
            assertion=assertion,
            frame_receipts=success_receipts(3),
        ),
        post={
            sender: Account(nonce=1),
            writer: Account(storage={SLOT_A: 1}),
        },
    )


def test_post_tx_codeless_target(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """
    Run a `POST_TX` frame targeting an account without code like a
    `DEFAULT` frame would: the call has nothing to execute and
    succeeds, so the body commits.
    """
    sender = pre.fund_eoa()
    writer = pre.deploy_contract(code=Op.SSTORE(SLOT_A, 1) + Op.STOP)
    codeless = pre.fund_eoa(amount=0)

    state_test(
        pre=pre,
        tx=assertion_transaction(
            sender,
            body=[body_frame(target=writer)],
            assertion=codeless,
            frame_receipts=success_receipts(3),
        ),
        post={
            sender: Account(nonce=1),
            writer: Account(storage={SLOT_A: 1}),
        },
    )


def test_diff_instructions_in_subcall(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """
    Allow the diff instructions anywhere in a `POST_TX` frame's call
    subtree: a contract the assertion calls reads the diff on its
    behalf.
    """
    sender = pre.fund_eoa()
    writer = pre.deploy_contract(code=Op.SSTORE(SLOT_A, 1) + Op.STOP)
    reader = pre.deploy_contract(
        code=Op.MSTORE(0, Op.TXTRACE(Spec.TXTRACE_SLOTS_CHANGED, 0))
        + Op.RETURN(0, 32)
    )
    assertion = pre.deploy_contract(
        code=Op.STATICCALL(Op.GAS, reader, 0, 0, 0, 32)
        + expect_eq(Op.MLOAD(0), 1)
        + Op.STOP
    )

    state_test(
        pre=pre,
        tx=assertion_transaction(
            sender,
            body=[body_frame(target=writer)],
            assertion=assertion,
            frame_receipts=success_receipts(3),
        ),
        post={
            sender: Account(nonce=1),
            writer: Account(storage={SLOT_A: 1}),
        },
    )


@pytest.mark.parametrize(
    "instruction",
    [
        pytest.param(
            Op.TXTRACE(Spec.TXTRACE_BALANCES_CHANGED, 0), id="txtrace"
        ),
        pytest.param(
            Op.TXDIFF(Spec.TXDIFF_ADDRESS_SLOTS_COUNT, 0, 0), id="txdiff"
        ),
        pytest.param(Op.EVENTDATACOPY(0, 0, 0, 0), id="eventdatacopy"),
    ],
)
@pytest.mark.parametrize(
    "frame_builder",
    [
        pytest.param(sender_frame, id="sender_frame"),
        pytest.param(default_frame, id="default_frame"),
    ],
)
def test_diff_instructions_outside_post_tx(
    state_test: StateTestFiller,
    pre: Alloc,
    instruction: Bytecode,
    frame_builder: type,
) -> None:
    """
    Halt the diff instructions exceptionally in any frame mode other
    than `POST_TX`: the probe's marker write is discarded with the
    failed frame, which does not invalidate the transaction.
    """
    sender = pre.fund_eoa()
    probe = pre.deploy_contract(
        code=Op.SSTORE(SLOT_MARKER, MARKER) + instruction + Op.STOP
    )

    state_test(
        pre=pre,
        tx=Transaction(
            sender=sender,
            frames=[
                verify_frame(),
                frame_builder(target=probe, gas_limit=BODY_FRAME_GAS),
            ],
            expected_receipt=TransactionReceipt(
                payer=sender,
                frame_receipts=[
                    FrameReceipt(status=Spec8141.STATUS_SUCCESS),
                    FrameReceipt(status=Spec8141.STATUS_FAILURE),
                ],
            ),
        ),
        post={
            sender: Account(nonce=1),
            probe: Account(storage={SLOT_MARKER: 0}),
        },
    )


@pytest.mark.parametrize(
    "instruction",
    [
        pytest.param(
            Op.TXTRACE(Spec.TXTRACE_BALANCES_CHANGED, 0), id="txtrace"
        ),
        pytest.param(
            Op.TXDIFF(Spec.TXDIFF_ADDRESS_SLOTS_COUNT, 0, 0), id="txdiff"
        ),
        pytest.param(Op.EVENTDATACOPY(0, 0, 0, 0), id="eventdatacopy"),
    ],
)
@pytest.mark.frame_tx_incompatible
def test_diff_instructions_in_legacy_transaction(
    state_test: StateTestFiller,
    pre: Alloc,
    instruction: Bytecode,
) -> None:
    """
    Halt the diff instructions exceptionally in a transaction that is
    not a frame transaction: there is no `POST_TX` frame to run in.
    """
    sender = pre.fund_eoa()
    probe = pre.deploy_contract(
        code=Op.SSTORE(SLOT_MARKER, MARKER) + instruction + Op.STOP
    )

    state_test(
        pre=pre,
        tx=Transaction(sender=sender, to=probe, gas_limit=200_000),
        post={probe: Account(storage={SLOT_MARKER: 0})},
    )


@pytest.mark.exception_test
def test_post_tx_without_payment(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """
    Invalidate a transaction whose only frames are `POST_TX` frames:
    nothing approves payment, so the transaction fails the end-of-frames
    rule regardless of the assertion's outcome.
    """
    sender = pre.fund_eoa()
    assertion = pre.deploy_contract(code=Op.STOP)
    tx = Transaction(
        sender=sender,
        frames=[post_tx_frame(target=assertion)],
        error=TransactionException.TYPE_6_INVALID_FRAME_EXECUTION,
    )
    state_test(pre=pre, tx=tx, post={})


@pytest.mark.parametrize("second_assertion", [False, True])
def test_failed_batch_can_skip_post_tx_terminator(
    state_test: StateTestFiller,
    pre: Alloc,
    second_assertion: bool,
) -> None:
    """
    Pin the inherited batch skip rule at the assertion boundary.

    The EIP must decide whether this skip is allowed: a sole assertion
    can be bypassed while earlier, unbatched body changes survive.
    """
    sender = pre.fund_eoa()
    writer = pre.deploy_contract(code=Op.SSTORE(SLOT_A, 1))
    failure = pre.deploy_contract(code=Op.REVERT(0, 0))
    receipts = [
        FrameReceipt(status=Spec8141.STATUS_SUCCESS),
        FrameReceipt(status=Spec8141.STATUS_SUCCESS, logs=[]),
        FrameReceipt(status=Spec8141.STATUS_FAILURE, logs=[]),
        FrameReceipt(
            status=Spec8141.STATUS_SKIPPED, gas_used=0, state_gas_used=0
        ),
    ]
    if second_assertion:
        receipts.append(FrameReceipt(status=Spec8141.STATUS_FAILURE))
    state_test(
        pre=pre,
        tx=assertion_transaction(
            sender,
            body=[
                body_frame(target=writer),
                body_frame(target=failure, flags=Spec8141.ATOMIC_BATCH_FLAG),
            ],
            assertion=[failure, failure] if second_assertion else failure,
            frame_receipts=receipts,
        ),
        post={
            sender: Account(nonce=1),
            writer: Account(storage={SLOT_A: 0 if second_assertion else 1}),
        },
    )


@pytest.mark.parametrize("failure", ["none", "revert", "exception"])
def test_post_tx_gas_settlement(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    failure: str,
) -> None:
    """
    Settle assertion failure against exact receipts, payer balance and
    block gas, including refunded state gas and a discarded storage refund.
    """
    funds = 10**18
    fee = 7
    sender = pre.fund_eoa(amount=funds)
    worker_code = (
        Op.SSTORE(SLOT_A, 1, original_value=0, new_value=1)
        + Op.SSTORE(SLOT_B, 0, original_value=1, current_value=1, new_value=0)
        + Op.LOG0(0, 0)
        + Op.STOP
    )
    worker = pre.deploy_contract(code=worker_code, storage={SLOT_B: 1})
    assertion_code = {
        "none": Op.STOP,
        "revert": Op.REVERT(0, 0),
        "exception": Op.INVALID,
    }[failure]
    assertion = pre.deploy_contract(code=assertion_code)
    later = pre.deploy_contract(code=Op.STOP)
    entry = fork.frame_entry_gas_calculator()()
    state_cost = worker_code.state_cost(fork)
    worker_execution = entry + worker_code.execution_cost(fork)
    state_budget = state_cost
    assertion_budget = 10_000
    assertion_execution = (
        assertion_budget
        if failure == "exception"
        else entry + assertion_code.execution_cost(fork)
    )
    receipts = [
        FrameReceipt(
            status=Spec8141.STATUS_SUCCESS,
            gas_used=default_code_frame_gas(fork, target_warm=True),
            state_gas_used=0,
        ),
        FrameReceipt(
            status=Spec8141.STATUS_SUCCESS,
            gas_used=worker_execution,
            state_gas_used=min(state_cost, state_budget)
            if failure == "none"
            else 0,
            **({"logs": []} if failure != "none" else {}),
        ),
        FrameReceipt(
            status=Spec8141.STATUS_SUCCESS
            if failure == "none"
            else Spec8141.STATUS_FAILURE,
            gas_used=assertion_execution,
            state_gas_used=0,
        ),
        FrameReceipt(
            status=Spec8141.STATUS_SUCCESS
            if failure == "none"
            else Spec8141.STATUS_SKIPPED,
            gas_used=entry if failure == "none" else 0,
            state_gas_used=0,
        ),
    ]
    tx = Transaction(
        sender=sender,
        max_fee_per_gas=fee,
        max_priority_fee_per_gas=0,
        frames=[
            verify_frame(),
            body_frame(target=worker, state_gas_limit=state_budget),
            post_tx_frame(target=assertion, gas_limit=assertion_budget),
            post_tx_frame(target=later),
        ],
    )
    tx.sign()
    assert tx.frames is not None and tx.signatures is not None
    intrinsic = fork.frame_transaction_intrinsic_cost_calculator()(
        frames=tx.frames,
        signatures=tx.signatures,
        return_cost_deducted_prior_execution=True,
    )
    floor = fork.frame_transaction_data_floor_cost_calculator()(
        frames=tx.frames, signatures=tx.signatures
    )
    execution_used = intrinsic
    state_used = 0
    for receipt in receipts:
        assert receipt.gas_used is not None
        assert receipt.state_gas_used is not None
        execution_used += int(receipt.gas_used)
        state_used += int(receipt.state_gas_used)
    refund = (
        min(worker_code.refund(fork), (execution_used + state_used) // 5)
        if failure == "none"
        else 0
    )
    payer_used = max(execution_used - refund, floor) + state_used
    tx.expected_receipt = TransactionReceipt(
        payer=sender, cumulative_gas_used=payer_used, frame_receipts=receipts
    )
    state_test(
        pre=pre,
        tx=tx,
        post={
            sender: Account(nonce=1, balance=funds - fee * payer_used),
            worker: Account(
                storage={
                    SLOT_A: 1 if failure == "none" else 0,
                    SLOT_B: 0 if failure == "none" else 1,
                }
            ),
        },
        blockchain_test_header_verify=Header(
            gas_used=max(execution_used, floor, state_used)
        ),
    )
