"""
`TXTRACE` and `EVENTDATACOPY` (EIP-7906): enumeration of the
transaction's balance, slot, deployment and event tables, the gas
payment parameters, the halting inputs, and the instructions' gas.
"""

import pytest
from execution_testing import (
    Account,
    Alloc,
    Bytecode,
    Fork,
    FrameReceipt,
    Initcode,
    Op,
    StateTestFiller,
    Storage,
    Transaction,
    TransactionReceipt,
    compute_create_address,
    keccak256,
)

from tests.amsterdam.eip7708_eth_transfer_logs.spec import Spec as Spec7708
from tests.amsterdam.eip8141_frame_transactions.helpers import verify_frame
from tests.amsterdam.eip8141_frame_transactions.spec import Spec as Spec8141

from .helpers import (
    as_int,
    assertion_transaction,
    body_frame,
    expect_eq,
    measured_gas,
    post_tx_frame,
    probe_overhead,
    reverted_body_receipts,
    success_receipts,
)
from .spec import Spec, ref_spec_7906

REFERENCE_SPEC_GIT_PATH = ref_spec_7906.git_path
REFERENCE_SPEC_VERSION = ref_spec_7906.version

pytestmark = pytest.mark.valid_from("EIP7906")

FUNDS = 10**18
"""The sender's funding, the payer's balance before the transaction."""

BOB_FUNDS = 1_000
VALUE = 7

KEY_A = 0xA1
KEY_B = 0xB2
KEY_C = 0xC3
KEY_U = 0xD4
"""A slot the body reads but never writes."""

WRITER_STORAGE: Storage.StorageDictType = {KEY_B: 5, KEY_U: 3}
"""Storage the writer contracts start with."""

WRITER_CODE = (
    Op.SSTORE(KEY_A, 1)
    + Op.SSTORE(KEY_B, 7)
    + Op.SSTORE(KEY_C, 9)
    + Op.SSTORE(KEY_C, 0)
    + Op.STOP
)
"""
Set an empty slot, update a set one, and write a third then restore it,
so only the first two appear in `slots_changed`.
"""

EVENT_DATA = bytes(range(1, 41))
"""Non-indexed data of the emitter's event: 40 bytes, over a word."""

TOPIC_1 = 0x1111111111111111111111111111111111111111111111111111111111111111
TOPIC_2 = 0x2222222222222222222222222222222222222222222222222222222222222222

EMITTER_CODE = (
    Op.MSTORE(0, int.from_bytes(EVENT_DATA[:32], "big"))
    + Op.MSTORE(32, int.from_bytes(EVENT_DATA[32:].ljust(32, b"\x00"), "big"))
    + Op.LOG2(0, len(EVENT_DATA), TOPIC_1, TOPIC_2)
    + Op.STOP
)
"""Emit one two-topic event carrying `EVENT_DATA`."""

SILENT_CODE = Op.LOG0(0, 0) + Op.STOP
"""Emit one topic-less, data-less event."""

DEPLOYED_RUNTIME = b"\x00"
"""Runtime code of the contract the factory deploys: a single `STOP`."""

INITCODE_DEPLOYING = Op.MSTORE8(0, 0) + Op.RETURN(0, 1)
INITCODE_EMPTY = Op.STOP


def initcode_word(initcode: Bytecode) -> int:
    """Return an initcode, at most a word long, left-aligned in a word."""
    raw = bytes(initcode)
    assert len(raw) <= 32
    return int.from_bytes(raw.ljust(32, b"\x00"), "big")


FACTORY_CODE = (
    Op.MSTORE(0, initcode_word(INITCODE_DEPLOYING))
    + Op.POP(Op.CREATE(0, 0, len(bytes(INITCODE_DEPLOYING))))
    + Op.MSTORE(0, initcode_word(INITCODE_EMPTY))
    + Op.POP(Op.CREATE(0, 0, len(bytes(INITCODE_EMPTY))))
    + Op.STOP
)
"""
Deploy one contract with runtime code and one whose initcode returns
nothing, so only the first appears in `contracts_deployed`.
"""

FACTORY_STATE_GAS = 1_000_000
"""State gas budget covering two account creations."""


@pytest.mark.parametrize("assertion_holds", [True, False])
def test_balances_changed(
    state_test: StateTestFiller,
    pre: Alloc,
    assertion_holds: bool,
) -> None:
    """
    Enumerate `balances_changed` after a value transfer: the payer's
    entry, whose delta bundles the gas pre-charge with the value sent,
    and the recipient's, in ascending address order, with the gas
    payment parameters isolating the pre-charge. The transfer's
    EIP-7708 log is the transaction's only event. The failing variant
    expects one entry too many, and the body's transfer is reverted.
    """
    sender = pre.fund_eoa(amount=FUNDS)
    bob = pre.fund_eoa(amount=BOB_FUNDS)

    checks = expect_eq(
        Op.TXTRACE(Spec.TXTRACE_BALANCES_CHANGED, 0),
        2 if assertion_holds else 3,
    )
    for index, address in enumerate(sorted([sender, bob], key=as_int)):
        checks += expect_eq(
            Op.TXTRACE(Spec.TXTRACE_BALANCE_ADDRESS, index), as_int(address)
        )
        if address == sender:
            checks += expect_eq(
                Op.TXTRACE(Spec.TXTRACE_BALANCE_BEFORE, index), FUNDS
            )
            # The payer's escrow is only refunded at settlement, so its
            # live balance is the after value.
            checks += expect_eq(
                Op.TXTRACE(Spec.TXTRACE_BALANCE_AFTER, index),
                Op.BALANCE(sender),
            )
        else:
            checks += expect_eq(
                Op.TXTRACE(Spec.TXTRACE_BALANCE_BEFORE, index), BOB_FUNDS
            )
            checks += expect_eq(
                Op.TXTRACE(Spec.TXTRACE_BALANCE_AFTER, index),
                BOB_FUNDS + VALUE,
            )
    checks += expect_eq(Op.TXTRACE(Spec.TXTRACE_GAS_PAYER, 0), as_int(sender))
    checks += expect_eq(
        Op.TXTRACE(Spec.TXTRACE_GAS_PRE_CHARGE, 0),
        Op.SUB(FUNDS - VALUE, Op.BALANCE(sender)),
    )
    checks += expect_eq(Op.TXTRACE(Spec.TXTRACE_SLOTS_CHANGED, 0), 0)
    checks += expect_eq(Op.TXTRACE(Spec.TXTRACE_CONTRACTS_DEPLOYED, 0), 0)
    # The body's transfer is the transaction's only event, the EIP-7708
    # transfer log; the payer's escrow emits none.
    checks += expect_eq(Op.TXTRACE(Spec.TXTRACE_EVENTS_COUNT, 0), 1)
    checks += expect_eq(
        Op.TXTRACE(Spec.TXTRACE_EVENT_ADDRESS, 0),
        as_int(Spec7708.SYSTEM_ADDRESS),
    )
    checks += expect_eq(Op.TXTRACE(Spec.TXTRACE_EVENT_TOPIC_COUNT, 0), 3)
    checks += expect_eq(
        Op.TXTRACE(Spec.TXTRACE_EVENT_TOPIC0, 0),
        int.from_bytes(Spec7708.TRANSFER_TOPIC, "big"),
    )
    checks += expect_eq(
        Op.TXTRACE(Spec.TXTRACE_EVENT_TOPIC1, 0), as_int(sender)
    )
    checks += expect_eq(Op.TXTRACE(Spec.TXTRACE_EVENT_TOPIC2, 0), as_int(bob))
    checks += expect_eq(Op.TXTRACE(Spec.TXTRACE_EVENT_DATA_LEN, 0), 32)
    checks += Op.EVENTDATACOPY(0, 0, 0, 32)
    checks += expect_eq(Op.MLOAD(0), VALUE)
    assertion = pre.deploy_contract(code=checks + Op.STOP)

    state_test(
        pre=pre,
        tx=assertion_transaction(
            sender,
            body=[body_frame(target=bob, value=VALUE)],
            assertion=assertion,
            frame_receipts=success_receipts(3)
            if assertion_holds
            else reverted_body_receipts(1),
        ),
        post={
            sender: Account(nonce=1),
            bob: Account(
                balance=BOB_FUNDS + VALUE if assertion_holds else BOB_FUNDS
            ),
        },
    )


def test_slots_changed(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """
    Enumerate `slots_changed` across two contracts: entries ascend by
    address then by key, carry the prestate and final values, collapse
    to one entry per slot, and omit a slot written then restored.
    """
    sender = pre.fund_eoa()
    writers = sorted(
        [
            pre.deploy_contract(code=WRITER_CODE, storage=WRITER_STORAGE),
            pre.deploy_contract(code=WRITER_CODE, storage=WRITER_STORAGE),
        ],
        key=as_int,
    )
    expected = [
        (writer, key, before, after)
        for writer in writers
        for key, before, after in ((KEY_A, 0, 1), (KEY_B, 5, 7))
    ]

    checks = expect_eq(Op.TXTRACE(Spec.TXTRACE_SLOTS_CHANGED, 0), 4)
    for index, (writer, key, before, after) in enumerate(expected):
        checks += expect_eq(
            Op.TXTRACE(Spec.TXTRACE_SLOT_ADDRESS, index), as_int(writer)
        )
        checks += expect_eq(Op.TXTRACE(Spec.TXTRACE_SLOT_KEY, index), key)
        checks += expect_eq(
            Op.TXTRACE(Spec.TXTRACE_SLOT_BEFORE, index), before
        )
        checks += expect_eq(Op.TXTRACE(Spec.TXTRACE_SLOT_AFTER, index), after)
    # Only the payer's balance moved.
    checks += expect_eq(Op.TXTRACE(Spec.TXTRACE_BALANCES_CHANGED, 0), 1)
    assertion = pre.deploy_contract(code=checks + Op.STOP)

    state_test(
        pre=pre,
        tx=assertion_transaction(
            sender,
            body=[body_frame(target=writer) for writer in writers],
            assertion=assertion,
            frame_receipts=success_receipts(4),
        ),
        post={
            sender: Account(nonce=1),
            **{
                writer: Account(
                    storage={KEY_A: 1, KEY_B: 7, KEY_C: 0, KEY_U: 3}
                )
                for writer in writers
            },
        },
    )


def test_contracts_deployed(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """
    Enumerate `contracts_deployed`: a creation that installs runtime
    code is listed with its code hash, while a creation whose initcode
    returns nothing leaves the account without a code change.
    """
    sender = pre.fund_eoa()
    factory = pre.deploy_contract(code=FACTORY_CODE)
    deployed = compute_create_address(address=factory, nonce=1)
    empty = compute_create_address(address=factory, nonce=2)

    checks = expect_eq(Op.TXTRACE(Spec.TXTRACE_CONTRACTS_DEPLOYED, 0), 1)
    checks += expect_eq(
        Op.TXTRACE(Spec.TXTRACE_DEPLOYED_ADDRESS, 0), as_int(deployed)
    )
    checks += expect_eq(
        Op.TXTRACE(Spec.TXTRACE_DEPLOYED_CODEHASH, 0),
        int.from_bytes(keccak256(DEPLOYED_RUNTIME), "big"),
    )
    assertion = pre.deploy_contract(code=checks + Op.STOP)

    state_test(
        pre=pre,
        tx=assertion_transaction(
            sender,
            body=[
                body_frame(target=factory, state_gas_limit=FACTORY_STATE_GAS)
            ],
            assertion=assertion,
            frame_receipts=success_receipts(3),
        ),
        post={
            sender: Account(nonce=1),
            factory: Account(nonce=3),
            deployed: Account(nonce=1, code=DEPLOYED_RUNTIME),
            empty: Account(nonce=1, code=b""),
        },
    )


def test_events(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """
    Enumerate the event table in emission order — emitter, topic count,
    topics and data length — and copy an event's data into memory with
    `EVENTDATACOPY`, from the start and from an offset.
    """
    sender = pre.fund_eoa()
    emitter = pre.deploy_contract(code=EMITTER_CODE)
    silent = pre.deploy_contract(code=SILENT_CODE)

    checks = expect_eq(Op.TXTRACE(Spec.TXTRACE_EVENTS_COUNT, 0), 2)
    checks += expect_eq(
        Op.TXTRACE(Spec.TXTRACE_EVENT_ADDRESS, 0), as_int(emitter)
    )
    checks += expect_eq(Op.TXTRACE(Spec.TXTRACE_EVENT_TOPIC_COUNT, 0), 2)
    checks += expect_eq(Op.TXTRACE(Spec.TXTRACE_EVENT_TOPIC0, 0), TOPIC_1)
    checks += expect_eq(Op.TXTRACE(Spec.TXTRACE_EVENT_TOPIC1, 0), TOPIC_2)
    checks += expect_eq(
        Op.TXTRACE(Spec.TXTRACE_EVENT_DATA_LEN, 0), len(EVENT_DATA)
    )
    checks += expect_eq(
        Op.TXTRACE(Spec.TXTRACE_EVENT_ADDRESS, 1), as_int(silent)
    )
    checks += expect_eq(Op.TXTRACE(Spec.TXTRACE_EVENT_TOPIC_COUNT, 1), 0)
    checks += expect_eq(Op.TXTRACE(Spec.TXTRACE_EVENT_DATA_LEN, 1), 0)
    checks += Op.EVENTDATACOPY(0, 0, 0, 32)
    checks += expect_eq(Op.MLOAD(0), int.from_bytes(EVENT_DATA[:32], "big"))
    checks += Op.EVENTDATACOPY(0, 0, 8, 32)
    checks += expect_eq(Op.MLOAD(0), int.from_bytes(EVENT_DATA[8:40], "big"))
    # A zero-length copy at the end of the data is in range.
    checks += Op.EVENTDATACOPY(0, 0, len(EVENT_DATA), 0)
    checks += Op.EVENTDATACOPY(1, 0, 0, 0)
    assertion = pre.deploy_contract(code=checks + Op.STOP)

    state_test(
        pre=pre,
        tx=assertion_transaction(
            sender,
            body=[body_frame(target=emitter), body_frame(target=silent)],
            assertion=assertion,
            frame_receipts=success_receipts(4),
        ),
        post={sender: Account(nonce=1)},
    )


@pytest.mark.parametrize(
    "halting_read",
    [
        pytest.param(
            Op.TXTRACE(Spec.TXTRACE_BALANCES_CHANGED, 1),
            id="reserved_index_count",
        ),
        pytest.param(
            Op.TXTRACE(Spec.TXTRACE_GAS_PRE_CHARGE, 1),
            id="reserved_index_pre_charge",
        ),
        pytest.param(
            Op.TXTRACE(Spec.TXTRACE_GAS_PAYER, 1),
            id="reserved_index_payer",
        ),
        pytest.param(
            Op.TXTRACE(Spec.TXTRACE_UNDEFINED, 0), id="undefined_param"
        ),
        pytest.param(
            Op.TXTRACE(Spec.TXTRACE_BALANCE_ADDRESS, 1),
            id="balance_index_out_of_bounds",
        ),
        pytest.param(
            Op.TXTRACE(Spec.TXTRACE_SLOT_AFTER, 2),
            id="slot_index_out_of_bounds",
        ),
        pytest.param(
            Op.TXTRACE(Spec.TXTRACE_DEPLOYED_ADDRESS, 0),
            id="deployed_index_out_of_bounds",
        ),
        pytest.param(
            Op.TXTRACE(Spec.TXTRACE_EVENT_ADDRESS, 2),
            id="event_index_out_of_bounds",
        ),
        pytest.param(
            Op.TXTRACE(Spec.TXTRACE_EVENT_TOPIC2, 0),
            id="topic_beyond_count",
        ),
        pytest.param(
            Op.TXTRACE(Spec.TXTRACE_EVENT_TOPIC0, 1),
            id="topic_of_topicless_event",
        ),
        pytest.param(
            Op.EVENTDATACOPY(2, 0, 0, 0), id="copy_event_out_of_bounds"
        ),
        pytest.param(Op.EVENTDATACOPY(0, 0, 32, 32), id="copy_range_past_end"),
        pytest.param(
            Op.EVENTDATACOPY(0, 0, len(EVENT_DATA), 1),
            id="copy_one_byte_past_end",
        ),
        pytest.param(Op.EVENTDATACOPY(1, 0, 0, 1), id="copy_from_empty_data"),
    ],
)
def test_txtrace_halts(
    state_test: StateTestFiller,
    pre: Alloc,
    halting_read: Bytecode,
) -> None:
    """
    Halt `TXTRACE` and `EVENTDATACOPY` exceptionally on a non-zero
    reserved input, an undefined parameter, an index beyond a table, a
    topic beyond an event's topic count, and a data range past an
    event's data. The halt fails the assertion frame, reverting the
    body: one changed slot, the payer's balance, no deployment, and
    two events are the tables the probes index into.
    """
    sender = pre.fund_eoa()
    writer = pre.deploy_contract(code=Op.SSTORE(KEY_A, 1) + Op.STOP)
    emitter = pre.deploy_contract(code=EMITTER_CODE)
    silent = pre.deploy_contract(code=SILENT_CODE)
    assertion = pre.deploy_contract(code=halting_read + Op.STOP)

    state_test(
        pre=pre,
        tx=assertion_transaction(
            sender,
            body=[
                body_frame(target=writer),
                body_frame(target=emitter),
                body_frame(target=silent),
            ],
            assertion=assertion,
            frame_receipts=reverted_body_receipts(3),
        ),
        post={
            sender: Account(nonce=1),
            writer: Account(storage={KEY_A: 0}),
        },
    )


def test_txtrace_gas(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """
    Charge `TXTRACE` its flat cost whatever the parameter, and
    `EVENTDATACOPY` the `CALLDATACOPY` price: the base cost plus a
    per-word copy cost, with the memory already expanded.
    """
    sender = pre.fund_eoa()
    emitter = pre.deploy_contract(code=EMITTER_CODE)
    gas_costs = fork.gas_costs()

    checks = Bytecode()
    for param, index in (
        (Spec.TXTRACE_BALANCES_CHANGED, 0),
        (Spec.TXTRACE_EVENT_TOPIC1, 0),
        (Spec.TXTRACE_GAS_PRE_CHARGE, 0),
    ):
        checks += expect_eq(
            measured_gas(Op.TXTRACE(param, index)),
            gas_costs.OPCODE_TXTRACE + probe_overhead(gas_costs, 2),
        )
    # Expand the memory first so the copy's expansion cost is zero.
    checks += Op.MSTORE(32, 0)
    checks += expect_eq(
        measured_gas(Op.EVENTDATACOPY(0, 0, 0, 40), pushes_result=False),
        gas_costs.VERY_LOW
        + 2 * gas_costs.OPCODE_COPY_PER_WORD
        + probe_overhead(gas_costs, 4, pushes_result=False),
    )
    checks += expect_eq(
        measured_gas(Op.EVENTDATACOPY(0, 0, 0, 0), pushes_result=False),
        gas_costs.VERY_LOW + probe_overhead(gas_costs, 4, pushes_result=False),
    )
    assertion = pre.deploy_contract(code=checks + Op.STOP)

    state_test(
        pre=pre,
        tx=assertion_transaction(
            sender,
            body=[body_frame(target=emitter)],
            assertion=assertion,
            frame_receipts=success_receipts(3),
        ),
        post={sender: Account(nonce=1)},
    )


@pytest.mark.parametrize("shortfall", [0, 1])
@pytest.mark.parametrize("operation", ["trace", "copy", *range(6, 13)])
def test_diff_view_gas_boundary(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    shortfall: int,
    operation: str | int,
) -> None:
    """Charge exact gas for table views and copying across a word boundary."""
    sender = pre.fund_eoa()
    emitter = pre.deploy_contract(code=Op.SSTORE(KEY_A, 1) + EMITTER_CODE)
    if operation == "trace":
        probe = Op.TXTRACE(Spec.TXTRACE_SLOTS_CHANGED, 0)
    elif operation == "copy":
        probe = Op.EVENTDATACOPY(0, 1, 0, 40, data_size=40, new_memory_size=41)
    else:
        assert isinstance(operation, int)
        key = TOPIC_2 if operation >= 0x0B else emitter
        probe = Op.TXDIFF(operation, key, 0)
    code = probe + Op.STOP
    assertion = pre.deploy_contract(code=code)
    gas = fork.frame_entry_gas_calculator()() + code.execution_cost(fork)
    tx = Transaction(
        sender=sender,
        frames=[
            verify_frame(),
            body_frame(target=emitter),
            post_tx_frame(target=assertion, gas_limit=gas - shortfall),
        ],
        expected_receipt=TransactionReceipt(
            payer=sender,
            frame_receipts=[
                FrameReceipt(status=Spec8141.STATUS_SUCCESS),
                FrameReceipt(status=Spec8141.STATUS_SUCCESS),
                FrameReceipt(
                    status=Spec8141.STATUS_FAILURE
                    if shortfall
                    else Spec8141.STATUS_SUCCESS,
                    gas_used=gas - shortfall,
                ),
            ],
        ),
    )
    state_test(
        pre=pre,
        tx=tx,
        post={
            sender: Account(nonce=1),
            emitter: Account(storage={KEY_A: 0 if shortfall else 1}),
        },
    )


@pytest.mark.parametrize("blob_count", [0, 1])
def test_sponsored_gas_pre_charge(
    state_test: StateTestFiller,
    pre: Alloc,
    blob_count: int,
) -> None:
    """Expose a distinct payer and its entire escrow, including blob fees."""
    sender = pre.fund_eoa(amount=FUNDS)
    payer = pre.deploy_contract(
        code=Op.APPROVE(0, 0, Spec8141.APPROVE_PAYMENT), balance=FUNDS
    )
    assertion_code = (
        expect_eq(Op.TXTRACE(Spec.TXTRACE_GAS_PAYER, 0), payer)
        + expect_eq(
            Op.TXTRACE(Spec.TXTRACE_GAS_PRE_CHARGE, 0),
            Op.SUB(FUNDS, Op.BALANCE(payer, address_warm=True)),
        )
        + expect_eq(
            Op.TXDIFF(
                Spec.TXDIFF_BALANCE_BEFORE,
                payer,
                0,
                state_access="account",
                address_warm=True,
            ),
            FUNDS,
        )
        + Op.STOP
    )
    assertion = pre.deploy_contract(code=assertion_code)
    fee = 7
    tx = Transaction(
        sender=sender,
        max_fee_per_gas=fee,
        max_priority_fee_per_gas=0,
        max_fee_per_blob_gas=1 if blob_count else 0,
        blob_versioned_hashes=[bytes.fromhex("01" + "00" * 31)] * blob_count,
        frames=[
            verify_frame(flags=Spec8141.APPROVE_EXECUTION),
            verify_frame(target=payer, flags=Spec8141.APPROVE_PAYMENT),
            post_tx_frame(target=assertion),
        ],
        expected_receipt=TransactionReceipt(
            payer=payer, frame_receipts=success_receipts(3)
        ),
    )
    state_test(
        pre=pre,
        tx=tx,
        post={sender: Account(nonce=1, balance=FUNDS)},
    )


@pytest.mark.parametrize("assertion_fails", [False, True])
def test_diff_precedes_selfdestruct_cleanup(
    state_test: StateTestFiller,
    pre: Alloc,
    assertion_fails: bool,
) -> None:
    """
    Observe current code and storage before deferred SELFDESTRUCT cleanup.

    This pins the prototype's reading-time interpretation; the EIP's
    claim that this is the final outcome needs to distinguish cleanup.
    """
    sender = pre.fund_eoa()
    runtime = Op.SSTORE(KEY_A, 1) + Op.SELFDESTRUCT(0)
    initcode = Initcode(deploy_code=runtime)
    factory = pre.deploy_contract(
        code=Op.MSTORE(0, initcode_word(initcode))
        + Op.POP(Op.CREATE(0, 0, len(initcode)))
        + Op.STOP
    )
    created = compute_create_address(address=factory, nonce=1)
    checks = expect_eq(Op.TXTRACE(Spec.TXTRACE_CONTRACTS_DEPLOYED, 0), 1)
    checks += expect_eq(Op.TXTRACE(Spec.TXTRACE_SLOTS_CHANGED, 0), 1)
    checks += expect_eq(Op.TXDIFF(Spec.TXDIFF_SLOT_AFTER, created, KEY_A), 1)
    checks += expect_eq(
        Op.TXDIFF(Spec.TXDIFF_CODEHASH_AFTER, created, 0),
        int.from_bytes(keccak256(bytes(runtime)), "big"),
    )
    assertion = pre.deploy_contract(
        code=checks + (Op.REVERT(0, 0) if assertion_fails else Op.STOP)
    )
    state_test(
        pre=pre,
        tx=assertion_transaction(
            sender,
            body=[
                body_frame(target=factory, state_gas_limit=FACTORY_STATE_GAS),
                body_frame(target=created),
            ],
            assertion=assertion,
            frame_receipts=reverted_body_receipts(2)
            if assertion_fails
            else success_receipts(4),
        ),
        post={
            sender: Account(nonce=1),
            factory: Account(nonce=1 if assertion_fails else 2),
            created: Account.NONEXISTENT,
        },
    )
