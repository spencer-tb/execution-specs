"""
`TXDIFF` (EIP-7906): keyed lookups into the transaction's state diff,
the per-address and per-topic views, the account change flags, the
EIP-2929 pricing and access recording of the live lookups, and the
halting inputs.
"""

import pytest
from execution_testing import (
    Account,
    Alloc,
    BalAccountExpectation,
    BalNonceChange,
    BalStorageChange,
    BalStorageSlot,
    Block,
    BlockAccessListExpectation,
    BlockchainTestFiller,
    Bytecode,
    Fork,
    FrameReceipt,
    Op,
    StateTestFiller,
    Transaction,
    TransactionReceipt,
    compute_create_address,
    keccak256,
)

from tests.amsterdam.eip8141_frame_transactions.helpers import verify_frame
from tests.amsterdam.eip8141_frame_transactions.spec import Spec as Spec8141

from .helpers import (
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
from .test_txtrace import (
    BOB_FUNDS,
    DEPLOYED_RUNTIME,
    FACTORY_CODE,
    FACTORY_STATE_GAS,
    FUNDS,
    KEY_A,
    KEY_B,
    KEY_C,
    KEY_U,
    TOPIC_1,
    TOPIC_2,
    VALUE,
    WRITER_CODE,
    WRITER_STORAGE,
)

REFERENCE_SPEC_GIT_PATH = ref_spec_7906.git_path
REFERENCE_SPEC_VERSION = ref_spec_7906.version

pytestmark = pytest.mark.valid_from("EIP7906")

TOPIC_3 = 0x3333333333333333333333333333333333333333333333333333333333333333
TOPIC_ABSENT = (
    0x9999999999999999999999999999999999999999999999999999999999999999
)

CAROL_FUNDS = 1
"""Funding of an account the body never touches."""


def test_txdiff_lookups(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """
    Look up slots, balances and code hashes before and after the
    transaction by key, including keys the transaction never wrote,
    which read the live value for both; summarize each account's net
    change in the flags bitmask; and map the per-address slot view onto
    the enumeration table.
    """
    sender = pre.fund_eoa(amount=FUNDS)
    bob = pre.fund_eoa(amount=BOB_FUNDS)
    carol = pre.fund_eoa(amount=CAROL_FUNDS)
    writer = pre.deploy_contract(code=WRITER_CODE, storage=WRITER_STORAGE)
    factory = pre.deploy_contract(code=FACTORY_CODE)
    deployed = compute_create_address(address=factory, nonce=1)
    deployed_code_hash = int.from_bytes(keccak256(DEPLOYED_RUNTIME), "big")

    def slot(param: int, key: int) -> Bytecode:
        return Op.TXDIFF(param, writer, key)

    checks = Bytecode()
    for key, before, after in (
        (KEY_A, 0, 1),
        (KEY_B, 5, 7),
        (KEY_C, 0, 0),
        (KEY_U, 3, 3),
    ):
        checks += expect_eq(slot(Spec.TXDIFF_SLOT_BEFORE, key), before)
        checks += expect_eq(slot(Spec.TXDIFF_SLOT_AFTER, key), after)

    checks += expect_eq(
        Op.TXDIFF(Spec.TXDIFF_BALANCE_BEFORE, bob, 0), BOB_FUNDS
    )
    checks += expect_eq(
        Op.TXDIFF(Spec.TXDIFF_BALANCE_AFTER, bob, 0), BOB_FUNDS + VALUE
    )
    checks += expect_eq(
        Op.TXDIFF(Spec.TXDIFF_BALANCE_BEFORE, carol, 0), CAROL_FUNDS
    )
    checks += expect_eq(
        Op.TXDIFF(Spec.TXDIFF_BALANCE_AFTER, carol, 0), CAROL_FUNDS
    )
    checks += expect_eq(
        Op.TXDIFF(Spec.TXDIFF_BALANCE_BEFORE, sender, 0), FUNDS
    )
    checks += expect_eq(
        Op.TXDIFF(Spec.TXDIFF_BALANCE_AFTER, sender, 0), Op.BALANCE(sender)
    )

    checks += expect_eq(
        Op.TXDIFF(Spec.TXDIFF_CODEHASH_BEFORE, deployed, 0),
        Spec.EMPTY_CODE_HASH,
    )
    checks += expect_eq(
        Op.TXDIFF(Spec.TXDIFF_CODEHASH_AFTER, deployed, 0),
        deployed_code_hash,
    )
    checks += expect_eq(
        Op.TXDIFF(Spec.TXDIFF_CODEHASH_BEFORE, bob, 0), Spec.EMPTY_CODE_HASH
    )
    checks += expect_eq(
        Op.TXDIFF(Spec.TXDIFF_CODEHASH_AFTER, bob, 0), Spec.EMPTY_CODE_HASH
    )
    checks += expect_eq(
        Op.TXDIFF(Spec.TXDIFF_CODEHASH_AFTER, writer, 0),
        int.from_bytes(keccak256(bytes(WRITER_CODE)), "big"),
    )

    for address, flags in (
        (sender, Spec.CHANGE_FLAG_NONCE | Spec.CHANGE_FLAG_BALANCE),
        (writer, Spec.CHANGE_FLAG_STORAGE),
        (bob, Spec.CHANGE_FLAG_BALANCE),
        (deployed, Spec.CHANGE_FLAG_NONCE | Spec.CHANGE_FLAG_CODE),
        (factory, Spec.CHANGE_FLAG_NONCE),
        (carol, 0),
    ):
        checks += expect_eq(
            Op.TXDIFF(Spec.TXDIFF_ACCOUNT_CHANGE_FLAGS, address, 0), flags
        )

    checks += expect_eq(
        Op.TXDIFF(Spec.TXDIFF_ADDRESS_SLOTS_COUNT, writer, 0), 2
    )
    checks += expect_eq(
        Op.TXDIFF(Spec.TXDIFF_ADDRESS_SLOT_INDEX, writer, 0), 0
    )
    checks += expect_eq(
        Op.TXDIFF(Spec.TXDIFF_ADDRESS_SLOT_INDEX, writer, 1), 1
    )
    checks += expect_eq(Op.TXDIFF(Spec.TXDIFF_ADDRESS_SLOTS_COUNT, bob, 0), 0)
    assertion = pre.deploy_contract(code=checks + Op.STOP)

    state_test(
        pre=pre,
        tx=assertion_transaction(
            sender,
            body=[
                body_frame(target=writer),
                body_frame(target=bob, value=VALUE),
                body_frame(target=factory, state_gas_limit=FACTORY_STATE_GAS),
            ],
            assertion=assertion,
            frame_receipts=success_receipts(5),
        ),
        post={
            sender: Account(nonce=1),
            writer: Account(storage={KEY_A: 1, KEY_B: 7, KEY_C: 0, KEY_U: 3}),
            bob: Account(balance=BOB_FUNDS + VALUE),
            carol: Account(balance=CAROL_FUNDS),
            factory: Account(nonce=3),
            deployed: Account(nonce=1, code=DEPLOYED_RUNTIME),
        },
    )


def test_txdiff_event_views(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """
    Map the per-address and per-topic event views onto the event table:
    counts and local-to-global indices keyed by emitter, and keyed by an
    indexed topic value in any position, excluding the signature topic.
    """
    sender = pre.fund_eoa()
    emitter_a = pre.deploy_contract(
        code=Op.LOG3(0, 0, TOPIC_1, TOPIC_3, TOPIC_2) + Op.STOP
    )
    emitter_b = pre.deploy_contract(code=Op.LOG1(0, 0, TOPIC_1) + Op.STOP)

    checks = expect_eq(Op.TXTRACE(Spec.TXTRACE_EVENTS_COUNT, 0), 3)
    checks += expect_eq(
        Op.TXDIFF(Spec.TXDIFF_ADDRESS_EVENTS_COUNT, emitter_a, 0), 2
    )
    checks += expect_eq(
        Op.TXDIFF(Spec.TXDIFF_ADDRESS_EVENT_INDEX, emitter_a, 0), 0
    )
    checks += expect_eq(
        Op.TXDIFF(Spec.TXDIFF_ADDRESS_EVENT_INDEX, emitter_a, 1), 2
    )
    checks += expect_eq(
        Op.TXDIFF(Spec.TXDIFF_ADDRESS_EVENTS_COUNT, emitter_b, 0), 1
    )
    checks += expect_eq(
        Op.TXDIFF(Spec.TXDIFF_ADDRESS_EVENT_INDEX, emitter_b, 0), 1
    )
    checks += expect_eq(
        Op.TXDIFF(Spec.TXDIFF_ADDRESS_EVENTS_COUNT, sender, 0), 0
    )
    # `TOPIC_2` sits in the third indexed position of both of A's events.
    checks += expect_eq(
        Op.TXDIFF(Spec.TXDIFF_TOPIC_EVENTS_COUNT, TOPIC_2, 0), 2
    )
    checks += expect_eq(
        Op.TXDIFF(Spec.TXDIFF_TOPIC_EVENT_INDEX, TOPIC_2, 0), 0
    )
    checks += expect_eq(
        Op.TXDIFF(Spec.TXDIFF_TOPIC_EVENT_INDEX, TOPIC_2, 1), 2
    )
    checks += expect_eq(
        Op.TXDIFF(Spec.TXDIFF_TOPIC_EVENTS_COUNT, TOPIC_3, 0), 2
    )
    # `TOPIC_1` only ever appears as the signature topic.
    checks += expect_eq(
        Op.TXDIFF(Spec.TXDIFF_TOPIC_EVENTS_COUNT, TOPIC_1, 0), 0
    )
    checks += expect_eq(
        Op.TXDIFF(Spec.TXDIFF_TOPIC_EVENTS_COUNT, TOPIC_ABSENT, 0), 0
    )
    assertion = pre.deploy_contract(code=checks + Op.STOP)

    state_test(
        pre=pre,
        tx=assertion_transaction(
            sender,
            body=[
                body_frame(target=emitter_a),
                body_frame(target=emitter_b),
                body_frame(target=emitter_a),
            ],
            assertion=assertion,
            frame_receipts=success_receipts(5),
        ),
        post={sender: Account(nonce=1)},
    )


def test_txdiff_gas_and_warmth(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """
    Price the live lookups per EIP-2929 — a cold slot or account on
    first access, warm on the next, the access warming the key for the
    rest of the frame — and the view and flags parameters at the flat
    `TXTRACE` cost.
    """
    sender = pre.fund_eoa()
    carol = pre.fund_eoa(amount=CAROL_FUNDS)
    writer = pre.deploy_contract(code=WRITER_CODE, storage=WRITER_STORAGE)
    gas_costs = fork.gas_costs()
    overhead = probe_overhead(gas_costs, 3)

    checks = Bytecode()
    for probe, cost in (
        (
            Op.TXDIFF(Spec.TXDIFF_SLOT_AFTER, writer, KEY_U),
            gas_costs.COLD_STORAGE_ACCESS,
        ),
        (
            Op.TXDIFF(Spec.TXDIFF_SLOT_BEFORE, writer, KEY_U),
            gas_costs.WARM_ACCESS,
        ),
        (
            Op.TXDIFF(Spec.TXDIFF_BALANCE_AFTER, carol, 0),
            gas_costs.COLD_ACCOUNT_ACCESS,
        ),
        (
            Op.TXDIFF(Spec.TXDIFF_CODEHASH_BEFORE, carol, 0),
            gas_costs.WARM_ACCESS,
        ),
        (
            Op.TXDIFF(Spec.TXDIFF_ADDRESS_SLOTS_COUNT, writer, 0),
            gas_costs.OPCODE_TXTRACE,
        ),
        (
            Op.TXDIFF(Spec.TXDIFF_ACCOUNT_CHANGE_FLAGS, carol, 0),
            gas_costs.OPCODE_TXTRACE,
        ),
        (
            Op.TXDIFF(Spec.TXDIFF_TOPIC_EVENTS_COUNT, TOPIC_1, 0),
            gas_costs.OPCODE_TXTRACE,
        ),
    ):
        checks += expect_eq(measured_gas(probe), cost + overhead)
    assertion = pre.deploy_contract(code=checks + Op.STOP)

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
            writer: Account(storage={KEY_A: 1, KEY_B: 7, KEY_C: 0, KEY_U: 3}),
        },
    )


def test_txdiff_records_accesses(
    blockchain_test: BlockchainTestFiller,
    pre: Alloc,
) -> None:
    """
    Record a live `TXDIFF` lookup in the block access list like any
    other state read: the unwritten slot the assertion reads is a
    storage read of the writer, and the untouched account it reads
    appears as a touched account without changes.
    """
    sender = pre.fund_eoa()
    carol = pre.fund_eoa(amount=CAROL_FUNDS)
    writer = pre.deploy_contract(
        code=Op.SSTORE(KEY_A, 1) + Op.STOP, storage={KEY_U: 3}
    )
    assertion = pre.deploy_contract(
        code=expect_eq(Op.TXDIFF(Spec.TXDIFF_SLOT_AFTER, writer, KEY_U), 3)
        + expect_eq(
            Op.TXDIFF(Spec.TXDIFF_BALANCE_AFTER, carol, 0), CAROL_FUNDS
        )
        + Op.STOP
    )

    tx = assertion_transaction(
        sender,
        body=[body_frame(target=writer)],
        assertion=assertion,
        frame_receipts=success_receipts(3),
    )

    blockchain_test(
        pre=pre,
        blocks=[
            Block(
                txs=[tx],
                expected_block_access_list=BlockAccessListExpectation(
                    account_expectations={
                        writer: BalAccountExpectation(
                            storage_changes=[
                                BalStorageSlot(
                                    slot=KEY_A,
                                    slot_changes=[
                                        BalStorageChange(
                                            block_access_index=1,
                                            post_value=1,
                                        )
                                    ],
                                )
                            ],
                            storage_reads=[KEY_U],
                        ),
                        carol: BalAccountExpectation.empty(),
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
            writer: Account(storage={KEY_A: 1, KEY_U: 3}),
            carol: Account(balance=CAROL_FUNDS),
        },
    )


@pytest.mark.parametrize(
    "halting_read",
    [
        pytest.param(
            Op.TXDIFF(Spec.TXDIFF_BALANCE_BEFORE, 0xBEEF, 1),
            id="reserved_index_balance",
        ),
        pytest.param(
            Op.TXDIFF(Spec.TXDIFF_CODEHASH_AFTER, 0xBEEF, 1),
            id="reserved_index_codehash",
        ),
        pytest.param(
            Op.TXDIFF(Spec.TXDIFF_ADDRESS_SLOTS_COUNT, 0xBEEF, 1),
            id="reserved_index_slots_count",
        ),
        pytest.param(
            Op.TXDIFF(Spec.TXDIFF_ADDRESS_EVENTS_COUNT, 0xBEEF, 1),
            id="reserved_index_events_count",
        ),
        pytest.param(
            Op.TXDIFF(Spec.TXDIFF_ACCOUNT_CHANGE_FLAGS, 0xBEEF, 1),
            id="reserved_index_flags",
        ),
        pytest.param(
            Op.TXDIFF(Spec.TXDIFF_TOPIC_EVENTS_COUNT, TOPIC_1, 1),
            id="reserved_index_topic_count",
        ),
        pytest.param(
            Op.TXDIFF(Spec.TXDIFF_UNDEFINED, 0, 0), id="undefined_param"
        ),
        pytest.param(
            Op.TXDIFF(Spec.TXDIFF_ADDRESS_EVENT_INDEX, 0xBEEF, 0),
            id="event_index_of_silent_address",
        ),
        pytest.param(
            Op.TXDIFF(Spec.TXDIFF_TOPIC_EVENT_INDEX, TOPIC_1, 0),
            id="topic_index_of_absent_topic",
        ),
    ],
)
def test_txdiff_halts(
    state_test: StateTestFiller,
    pre: Alloc,
    halting_read: Bytecode,
) -> None:
    """
    Halt `TXDIFF` exceptionally on a non-zero reserved input, an
    undefined parameter, and a per-address or per-topic index beyond
    the view's count; the halt fails the assertion frame and reverts
    the body.
    """
    sender = pre.fund_eoa()
    writer = pre.deploy_contract(code=Op.SSTORE(KEY_A, 1) + Op.STOP)
    assertion = pre.deploy_contract(code=halting_read + Op.STOP)

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
            writer: Account(storage={KEY_A: 0}),
        },
    )


def test_txdiff_slot_index_out_of_bounds(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """
    Halt the per-address slot view on a local index equal to the view's
    count: the writer changed exactly one slot.
    """
    sender = pre.fund_eoa()
    writer = pre.deploy_contract(code=Op.SSTORE(KEY_A, 1) + Op.STOP)
    assertion = pre.deploy_contract(
        code=expect_eq(Op.TXDIFF(Spec.TXDIFF_ADDRESS_SLOT_INDEX, writer, 0), 0)
        + Op.TXDIFF(Spec.TXDIFF_ADDRESS_SLOT_INDEX, writer, 1)
        + Op.STOP
    )

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
            writer: Account(storage={KEY_A: 0}),
        },
    )


@pytest.mark.pre_alloc_mutable
@pytest.mark.parametrize("creation_reverts", [False, True])
def test_storage_before_creation_collision(
    state_test: StateTestFiller,
    pre: Alloc,
    creation_reverts: bool,
) -> None:
    """
    Read the true transaction prestate after creation at a storage-only
    address, including when the creation is reverted.
    """
    sender = pre.fund_eoa()
    initcode = Op.SSTORE(KEY_A, 7) + (
        Op.REVERT(0, 0) if creation_reverts else Op.STOP
    )
    factory = pre.deploy_contract(
        code=Op.MSTORE(
            0, int.from_bytes(bytes(initcode).ljust(32, b"\x00"), "big")
        )
        + Op.POP(Op.CREATE(0, 0, len(initcode)))
        + Op.STOP
    )
    created = compute_create_address(address=factory, nonce=1)
    pre.deploy_contract(
        address=created, code=b"", nonce=0, storage={KEY_A: 5}, balance=1
    )
    checks = expect_eq(Op.TXDIFF(Spec.TXDIFF_SLOT_BEFORE, created, KEY_A), 5)
    checks += expect_eq(
        Op.TXDIFF(Spec.TXDIFF_SLOT_AFTER, created, KEY_A),
        5 if creation_reverts else 7,
    )
    checks += expect_eq(
        Op.TXTRACE(Spec.TXTRACE_SLOTS_CHANGED, 0),
        0 if creation_reverts else 1,
    )
    if not creation_reverts:
        checks += expect_eq(Op.TXTRACE(Spec.TXTRACE_SLOT_BEFORE, 0), 5)
        checks += expect_eq(Op.TXTRACE(Spec.TXTRACE_SLOT_AFTER, 0), 7)
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
            factory: Account(nonce=2),
            created: Account(
                nonce=0 if creation_reverts else 1,
                storage={KEY_A: 5 if creation_reverts else 7},
            ),
        },
    )


@pytest.mark.parametrize("param", range(6))
@pytest.mark.parametrize("warm", [False, True])
@pytest.mark.parametrize("shortfall", [0, 1])
def test_txdiff_access_gas_boundary(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    param: int,
    warm: bool,
    shortfall: int,
) -> None:
    """
    Record live accesses only after the full opcode charge, at exact
    and one-short gas, for both cold and warm account and slot reads.
    """
    sender = pre.fund_eoa()
    target = pre.deploy_contract(code=Op.STOP, storage={KEY_U: 3})
    is_slot = param < 2
    key = KEY_U if is_slot else 0
    probe = Op.TXDIFF(
        param,
        target,
        key,
        state_access="slot" if is_slot else "account",
        key_warm=warm,
        address_warm=warm,
    )
    prelude = Bytecode()
    if warm:
        prelude = Op.POP(
            Op.TXDIFF(
                param,
                target,
                key,
                state_access="slot" if is_slot else "account",
            )
        )
    code = prelude + probe + Op.STOP
    assertion = pre.deploy_contract(code=code)
    gas = fork.frame_entry_gas_calculator()() + code.execution_cost(fork)
    accessed = warm or shortfall == 0
    expectation = (
        BalAccountExpectation(storage_reads=[KEY_U], storage_changes=[])
        if is_slot
        else BalAccountExpectation.empty()
    )
    state_test(
        pre=pre,
        tx=Transaction(
            sender=sender,
            frames=[
                verify_frame(),
                post_tx_frame(target=assertion, gas_limit=gas - shortfall),
            ],
            expected_receipt=TransactionReceipt(
                payer=sender,
                frame_receipts=[
                    FrameReceipt(status=Spec8141.STATUS_SUCCESS),
                    FrameReceipt(
                        status=Spec8141.STATUS_FAILURE
                        if shortfall
                        else Spec8141.STATUS_SUCCESS,
                        gas_used=gas - shortfall,
                    ),
                ],
            ),
        ),
        post={sender: Account(nonce=1), target: Account(storage={KEY_U: 3})},
        expected_block_access_list=BlockAccessListExpectation(
            account_expectations={target: expectation if accessed else None}
        ),
    )


@pytest.mark.parametrize("param", [0x06, 0x08, 0x0A, 0x0B])
def test_txdiff_empty_views_do_not_access_state(
    state_test: StateTestFiller,
    pre: Alloc,
    param: int,
) -> None:
    """Leave an untouched view key absent from the block access list."""
    sender = pre.fund_eoa()
    untouched = pre.deploy_contract(code=Op.STOP, storage={KEY_U: 3})
    assertion = pre.deploy_contract(
        code=expect_eq(Op.TXDIFF(param, untouched, 0), 0) + Op.STOP
    )
    state_test(
        pre=pre,
        tx=assertion_transaction(
            sender,
            body=[],
            assertion=assertion,
            frame_receipts=success_receipts(2),
        ),
        post={sender: Account(nonce=1)},
        expected_block_access_list=BlockAccessListExpectation(
            account_expectations={untouched: None}
        ),
    )
