"""
Tests for [EIP-8250: Keyed Nonces for Frame Transactions](https://eips.ethereum.org/EIPS/eip-8250).

A frame transaction selects its replay domains through `nonce_keys`:
the single key zero aliases the sender's account nonce, while every
other key selects an independent sequence kept in the `NONCE_MANAGER`
system contract's protocol-managed storage. The selected domains are
consumed atomically by the payment-scoped `APPROVE`, which charges one
storage set of state gas per keyed domain used for the first time.
"""  # noqa: E501

from typing import Dict, List, Optional

import pytest
from execution_testing import (
    Account,
    Alloc,
    Bytecode,
    Bytes,
    CodeGasMeasure,
    Conditional,
    Fork,
    Frame,
    FrameReceipt,
    FrameSignature,
    Op,
    StateTestFiller,
    Storage,
    Transaction,
    TransactionException,
    TransactionReceipt,
    TransactionTestFiller,
    compute_create_address,
)

from ..eip8141_frame_transactions.helpers import (
    default_code_frame_gas,
    default_frame,
    sender_frame,
    verify_frame,
)
from ..eip8141_frame_transactions.spec import Spec as Spec8141
from .helpers import (
    NONCE_KEY,
    OTHER_KEY,
    nonce_manager_with_slots,
    used_key_slots,
    verify_only_tx_gas_used,
)
from .spec import Spec, keyed_nonce_slot, nonce_keys_hash, ref_spec_8250

REFERENCE_SPEC_GIT_PATH = ref_spec_8250.git_path
REFERENCE_SPEC_VERSION = ref_spec_8250.version

pytestmark = pytest.mark.valid_from("EIP8250")

MAX_KEY = 2**256 - 1
"""The largest encodable nonce key."""

SLOT_RESULT = 0x01
"""Storage slot the probe contracts write what they read into."""

SLOT_LEGACY_NONCE = 0x02
"""Storage slot recording `TXPARAM` legacy nonce reads."""

SLOT_NONCE_SEQ = 0x03
"""Storage slot recording `TXPARAM` nonce sequence reads."""

SLOT_EXECUTED = 0x04
"""Storage slot a worker writes to record its execution."""

PROBE_FRAME_GAS = 500_000
"""Execution gas budget of the frames running probe contracts."""

PROBE_FRAME_STATE_GAS = 600_000
"""
State gas budget of the frames running probe contracts: a few fresh
slots, or an account creation plus fresh slots.
"""

WORKER_FRAME_GAS = 200_000
"""Execution gas budget of the frames running worker contracts."""


def delegated_sender_code(sender_work: Bytecode) -> Bytecode:
    """
    Return code for a sender that runs its frames through an EIP-7702
    delegation.

    A delegated sender has code, so its `VERIFY` frames run this code
    instead of the protocol default code: in a `VERIFY` frame it
    approves whatever scope the frame allows, while in a `SENDER`
    frame it runs `sender_work` — which decides its own ending.
    """
    frame_index = Op.TXPARAM(Spec8141.TXPARAM_FRAME_INDEX)
    return Conditional(
        condition=Op.EQ(
            Op.FRAMEPARAM(frame_index, Spec8141.FRAMEPARAM_MODE),
            Spec8141.MODE_SENDER,
        ),
        if_true=sender_work,
        if_false=Op.APPROVE(
            0,
            0,
            Op.FRAMEPARAM(frame_index, Spec8141.FRAMEPARAM_ALLOWED_SCOPE),
        ),
    )


def default_verify_receipt(fork: Fork, state_gas_used: int) -> FrameReceipt:
    """
    Return the receipt of a default-code `VERIFY` frame resolving to
    the sender: the warm sender access at entry, plus the given state
    gas of its nonce transition.
    """
    return FrameReceipt(
        status=Spec8141.STATUS_SUCCESS,
        gas_used=default_code_frame_gas(fork, target_warm=True),
        state_gas_used=state_gas_used,
    )


def test_keyed_nonce_consumption(
    state_test: StateTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    Consume a fresh non-zero nonce key.

    The payment approval writes sequence one to the key's nonce manager
    slot, charges one storage set of state gas to the approving frame,
    and leaves the sender's account nonce untouched.
    """
    first_use = fork.gas_costs().KEYED_NONCE_FIRST_USE
    sender = pre.fund_eoa()
    tx = Transaction(
        sender=sender,
        frames=[verify_frame()],
        nonce_keys=[NONCE_KEY],
        nonce_seq=0,
    )
    tx.expected_receipt = TransactionReceipt(
        payer=sender,
        cumulative_gas_used=verify_only_tx_gas_used(fork, tx, first_uses=1),
        frame_receipts=[default_verify_receipt(fork, first_use)],
    )
    state_test(
        pre=pre,
        tx=tx,
        post={
            Spec.NONCE_MANAGER: Account(
                nonce=Spec.NONCE_MANAGER_NONCE,
                code=Spec.NONCE_MANAGER_CODE,
                storage={keyed_nonce_slot(sender, NONCE_KEY): 1},
            ),
            sender: Account(nonce=0),
        },
    )


@pytest.mark.parametrize(
    "explicit_fields",
    [
        pytest.param(True, id="explicit_legacy_key_set"),
        pytest.param(False, id="unset_nonce_fields"),
    ],
)
def test_legacy_alias_key(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    explicit_fields: bool,
) -> None:
    """
    Select the legacy account nonce through the key set `[0]`.

    The sender's nonce increments as under EIP-8141, no keyed state gas
    is charged, and the nonce manager's storage stays empty. The test
    framework encodes unset nonce fields as this legacy key set, so
    the two variants fill the same transaction.
    """
    sender = pre.fund_eoa()
    nonce_fields = dict(nonce_keys=[0], nonce_seq=0) if explicit_fields else {}
    tx = Transaction(
        sender=sender,
        frames=[verify_frame()],
        **nonce_fields,
    )
    tx.expected_receipt = TransactionReceipt(
        payer=sender,
        cumulative_gas_used=verify_only_tx_gas_used(fork, tx, first_uses=0),
        frame_receipts=[default_verify_receipt(fork, 0)],
    )
    state_test(
        pre=pre,
        tx=tx,
        post={
            Spec.NONCE_MANAGER: Account(
                nonce=Spec.NONCE_MANAGER_NONCE,
                code=Spec.NONCE_MANAGER_CODE,
                storage={},
            ),
            sender: Account(nonce=1),
        },
    )


@pytest.mark.parametrize(
    "nonce_keys",
    [
        pytest.param([1, NONCE_KEY, MAX_KEY], id="three_keys_spanning_range"),
        pytest.param(
            list(range(1, Spec.MAX_NONCE_KEYS + 1)), id="max_key_count"
        ),
    ],
)
def test_multi_key_consumption(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    nonce_keys: List[int],
) -> None:
    """
    Consume a multi-key set of fresh domains.

    Every selected slot advances to sequence one and the approving
    frame pays one storage set per key; a set at the maximum key count
    needs a state budget sized for it.
    """
    first_use = fork.gas_costs().KEYED_NONCE_FIRST_USE
    state_gas = first_use * len(nonce_keys)
    sender = pre.fund_eoa()
    tx = Transaction(
        sender=sender,
        frames=[verify_frame(state_gas_limit=state_gas)],
        nonce_keys=nonce_keys,
        nonce_seq=0,
    )
    tx.expected_receipt = TransactionReceipt(
        payer=sender,
        cumulative_gas_used=verify_only_tx_gas_used(
            fork, tx, first_uses=len(nonce_keys)
        ),
        frame_receipts=[default_verify_receipt(fork, state_gas)],
    )
    state_test(
        pre=pre,
        tx=tx,
        post={
            Spec.NONCE_MANAGER: Account(
                storage={
                    keyed_nonce_slot(sender, key): 1 for key in nonce_keys
                },
            ),
            sender: Account(nonce=0),
        },
    )


@pytest.mark.pre_alloc_mutable
@pytest.mark.parametrize(
    "current_seq",
    [
        pytest.param(1, id="second_use"),
        pytest.param(127, id="seq_before_rlp_prefix"),
        pytest.param(128, id="seq_with_rlp_prefix"),
        pytest.param(255, id="seq_last_one_byte"),
        pytest.param(256, id="seq_first_two_bytes"),
        pytest.param(Spec.MAX_NONCE_SEQ - 1, id="last_use_before_exhaustion"),
    ],
)
def test_used_key_pays_no_creation(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    current_seq: int,
) -> None:
    """
    Reuse a keyed domain whose slot already exists.

    The transaction carries the slot's current sequence, the approval
    advances it by one without any state gas — the slot is not created
    — and the sequence just below the maximum is the last one a key can
    be selected at, leaving the slot exhausted.
    """
    sender = pre.fund_eoa()
    nonce_manager_with_slots(
        pre, used_key_slots(sender, {NONCE_KEY: current_seq})
    )
    tx = Transaction(
        sender=sender,
        frames=[verify_frame()],
        nonce_keys=[NONCE_KEY],
        nonce_seq=current_seq,
    )
    tx.expected_receipt = TransactionReceipt(
        payer=sender,
        cumulative_gas_used=verify_only_tx_gas_used(fork, tx, first_uses=0),
        frame_receipts=[default_verify_receipt(fork, 0)],
    )
    state_test(
        pre=pre,
        tx=tx,
        post={
            Spec.NONCE_MANAGER: Account(
                storage={keyed_nonce_slot(sender, NONCE_KEY): current_seq + 1}
            ),
            sender: Account(nonce=0),
        },
    )


@pytest.mark.pre_alloc_mutable
@pytest.mark.parametrize(
    "nonce_keys,nonce_seq,sender_nonce,used_keys,error",
    [
        pytest.param(
            [NONCE_KEY],
            1,
            0,
            {},
            TransactionException.NONCE_MISMATCH_TOO_HIGH,
            id="fresh_key_nonzero_seq",
            marks=pytest.mark.exception_test,
        ),
        pytest.param(
            [0],
            1,
            0,
            {},
            TransactionException.NONCE_MISMATCH_TOO_HIGH,
            id="legacy_alias_seq_too_high",
            marks=pytest.mark.exception_test,
        ),
        pytest.param(
            [0],
            0,
            1,
            {},
            TransactionException.NONCE_MISMATCH_TOO_LOW,
            id="legacy_alias_seq_too_low",
            marks=pytest.mark.exception_test,
        ),
        pytest.param(
            [NONCE_KEY],
            2,
            0,
            {NONCE_KEY: 3},
            TransactionException.NONCE_MISMATCH_TOO_LOW,
            id="used_key_seq_too_low",
            marks=pytest.mark.exception_test,
        ),
        pytest.param(
            [NONCE_KEY],
            4,
            0,
            {NONCE_KEY: 3},
            TransactionException.NONCE_MISMATCH_TOO_HIGH,
            id="used_key_seq_too_high",
            marks=pytest.mark.exception_test,
        ),
        pytest.param(
            [NONCE_KEY],
            Spec.MAX_NONCE_SEQ - 1,
            0,
            {NONCE_KEY: Spec.MAX_NONCE_SEQ},
            TransactionException.NONCE_MISMATCH_TOO_LOW,
            id="exhausted_key",
            marks=pytest.mark.exception_test,
        ),
        pytest.param(
            [NONCE_KEY, OTHER_KEY],
            0,
            0,
            {NONCE_KEY: 1},
            TransactionException.NONCE_MISMATCH_TOO_LOW,
            id="mixed_set_seq_of_fresh_key",
            marks=pytest.mark.exception_test,
        ),
        pytest.param(
            [NONCE_KEY, OTHER_KEY],
            1,
            0,
            {NONCE_KEY: 1},
            TransactionException.NONCE_MISMATCH_TOO_HIGH,
            id="mixed_set_seq_of_used_key",
            marks=pytest.mark.exception_test,
        ),
        pytest.param(
            [NONCE_KEY],
            0,
            5,
            {},
            None,
            id="keyed_domain_ignores_account_nonce",
        ),
    ],
)
def test_stateful_validity(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    nonce_keys: List[int],
    nonce_seq: int,
    sender_nonce: int,
    used_keys: Dict[int, int],
    error: Optional[TransactionException],
) -> None:
    """
    Check the transaction's sequence against every selected domain.

    A sequence differing from any selected domain's current one is
    statefully invalid, too low or too high per the first mismatching
    key. A shared sequence also means a set mixing a used key with a
    fresh one can never be valid: the fresh key demands zero, the used
    key its current, non-zero sequence. A key at the maximum sequence
    is exhausted, since no transaction may carry that sequence. The
    account nonce, in turn, plays no part in a keyed domain's check.
    """
    sender = pre.fund_eoa(nonce=sender_nonce)
    if used_keys:
        nonce_manager_with_slots(pre, used_key_slots(sender, used_keys))
    tx = Transaction(
        sender=sender,
        nonce=sender_nonce,
        frames=[verify_frame()],
        nonce_keys=nonce_keys,
        nonce_seq=nonce_seq,
        error=error,
    )
    post = {}
    if error is None:
        post[Spec.NONCE_MANAGER] = Account(
            storage={keyed_nonce_slot(sender, NONCE_KEY): 1}
        )
        post[sender] = Account(nonce=sender_nonce)
    state_test(pre=pre, tx=tx, post=post)


KEY_SET_CASES = [
    pytest.param(
        [],
        0,
        TransactionException.TYPE_6_INVALID_FRAME_FORMAT,
        id="empty_key_set",
        marks=pytest.mark.exception_test,
    ),
    pytest.param(
        list(range(1, Spec.MAX_NONCE_KEYS + 2)),
        0,
        TransactionException.TYPE_6_INVALID_FRAME_FORMAT,
        id="key_count_above_max",
        marks=pytest.mark.exception_test,
    ),
    pytest.param(
        [2, 1],
        0,
        TransactionException.TYPE_6_INVALID_FRAME_FORMAT,
        id="decreasing_keys",
        marks=pytest.mark.exception_test,
    ),
    pytest.param(
        [1, 1],
        0,
        TransactionException.TYPE_6_INVALID_FRAME_FORMAT,
        id="duplicate_keys",
        marks=pytest.mark.exception_test,
    ),
    pytest.param(
        [0, 1],
        0,
        TransactionException.TYPE_6_INVALID_FRAME_FORMAT,
        id="zero_key_first_in_multi_key_set",
        marks=pytest.mark.exception_test,
    ),
    pytest.param(
        [0, 0],
        0,
        TransactionException.TYPE_6_INVALID_FRAME_FORMAT,
        id="zero_key_repeated",
        marks=pytest.mark.exception_test,
    ),
    pytest.param(
        [2**256],
        0,
        TransactionException.TYPE_6_INVALID_FRAME_FORMAT,
        id="key_beyond_width",
        marks=pytest.mark.exception_test,
    ),
    pytest.param(
        [NONCE_KEY],
        Spec.MAX_NONCE_SEQ,
        TransactionException.NONCE_IS_MAX,
        id="seq_at_max",
        marks=pytest.mark.exception_test,
    ),
    pytest.param(
        [NONCE_KEY],
        Spec.MAX_NONCE_SEQ + 1,
        TransactionException.TYPE_6_INVALID_FRAME_FORMAT,
        id="seq_beyond_width",
        marks=pytest.mark.exception_test,
    ),
]
"""
Key set and sequence variations rejected regardless of state: sets
that are empty, oversized, not strictly increasing, or mixing key zero
with other keys, values beyond their field widths — which never
decode — and the exhausted sequence.
"""


@pytest.mark.parametrize("nonce_keys,nonce_seq,error", KEY_SET_CASES)
def test_static_validity(
    state_test: StateTestFiller,
    pre: Alloc,
    nonce_keys: List[int],
    nonce_seq: int,
    error: TransactionException,
) -> None:
    """
    Reject a structurally invalid key set or sequence before any
    state is consulted, and check that nothing was consumed.
    """
    sender = pre.fund_eoa()
    tx = Transaction(
        sender=sender,
        frames=[verify_frame()],
        nonce_keys=nonce_keys,
        nonce_seq=nonce_seq,
        error=error,
    )
    state_test(
        pre=pre,
        tx=tx,
        post={
            Spec.NONCE_MANAGER: Account(storage={}),
            sender: Account(nonce=0),
        },
    )


@pytest.mark.parametrize("nonce_keys,nonce_seq,error", KEY_SET_CASES)
def test_static_validity_transaction(
    transaction_test: TransactionTestFiller,
    pre: Alloc,
    nonce_keys: List[int],
    nonce_seq: int,
    error: TransactionException,
) -> None:
    """
    Assert the same key set rules as `test_static_validity` on the
    transaction itself rather than on a block containing it.
    """
    sender = pre.fund_eoa()
    tx = Transaction(
        sender=sender,
        frames=[verify_frame()],
        nonce_keys=nonce_keys,
        nonce_seq=nonce_seq,
        error=error,
    )
    transaction_test(pre=pre, tx=tx)


@pytest.mark.pre_alloc_mutable
@pytest.mark.parametrize(
    "nonce_keys,nonce_seq",
    [
        pytest.param([5, 9], 0, id="keyed_set"),
        pytest.param([0], 3, id="legacy_key_set"),
    ],
)
def test_txparam_nonce_fields(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    nonce_keys: List[int],
    nonce_seq: int,
) -> None:
    """
    Read the nonce fields through `TXPARAM`.

    `0x01` returns the transaction's sequence, which equals the legacy
    nonce only for the legacy key set, while the four selectors this
    EIP adds expose the pre-state legacy nonce, the key count, the
    canonical key-set hash, and the first key.
    """
    sender_nonce = 3
    storage = Storage()
    probe = pre.deploy_contract(
        code=Op.SSTORE(
            storage.store_next(nonce_seq), Op.TXPARAM(Spec.TXPARAM_NONCE_SEQ)
        )
        + Op.SSTORE(
            storage.store_next(sender_nonce),
            Op.TXPARAM(Spec.TXPARAM_LEGACY_NONCE),
        )
        + Op.SSTORE(
            storage.store_next(len(nonce_keys)),
            Op.TXPARAM(Spec.TXPARAM_NONCE_KEY_COUNT),
        )
        + Op.SSTORE(
            storage.store_next(nonce_keys_hash(nonce_keys)),
            Op.TXPARAM(Spec.TXPARAM_NONCE_KEYS_HASH),
        )
        + Op.SSTORE(
            storage.store_next(nonce_keys[0]),
            Op.TXPARAM(Spec.TXPARAM_NONCE_KEY_0),
        )
        + Op.STOP
    )
    sender = pre.fund_eoa(nonce=sender_nonce)
    tx = Transaction(
        sender=sender,
        nonce=sender_nonce,
        frames=[
            verify_frame(),
            default_frame(
                target=probe,
                gas_limit=PROBE_FRAME_GAS,
                state_gas_limit=PROBE_FRAME_STATE_GAS,
            ),
        ],
        nonce_keys=nonce_keys,
        nonce_seq=nonce_seq,
    )
    state_test(
        pre=pre,
        tx=tx,
        post={
            probe: Account(storage=storage),
            sender: Account(
                nonce=sender_nonce + 1 if nonce_keys == [0] else sender_nonce
            ),
        },
    )


def test_txparam_first_undefined_selector_halts(
    state_test: StateTestFiller, pre: Alloc
) -> None:
    """
    Read the first `TXPARAM` selector past the ones this EIP adds.

    The probe writes a marker before the halting read, so a selector
    that returned zero instead of halting would leave the marker
    behind.
    """
    sender = pre.fund_eoa()
    probe = pre.deploy_contract(
        code=Op.SSTORE(SLOT_RESULT, 0xFF)
        + Op.POP(Op.TXPARAM(Spec.TXPARAM_FIRST_UNDEFINED))
        + Op.STOP
    )
    tx = Transaction(
        sender=sender,
        frames=[
            verify_frame(),
            default_frame(target=probe, gas_limit=PROBE_FRAME_GAS),
        ],
        nonce_keys=[NONCE_KEY],
        nonce_seq=0,
        expected_receipt=TransactionReceipt(
            payer=sender,
            frame_receipts=[
                FrameReceipt(status=Spec8141.STATUS_SUCCESS),
                FrameReceipt(
                    status=Spec8141.STATUS_FAILURE,
                    gas_used=PROBE_FRAME_GAS,
                ),
            ],
        ),
    )
    state_test(
        pre=pre,
        tx=tx,
        post={probe: Account(storage={SLOT_RESULT: 0})},
    )


@pytest.mark.pre_alloc_mutable
def test_legacy_nonce_txparam_stable_across_create(
    state_test: StateTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    Advance the sender's account nonce within the transaction.

    A keyed transaction leaves the account nonce to ordinary EVM rules:
    a `CREATE` executed as the sender bumps it, while `TXPARAM`'s legacy
    nonce keeps reporting the pre-state value and the sequence stays
    the keyed one. The sender runs its frames through a delegation,
    which approves in the `VERIFY` frame and creates in the `SENDER`
    frame.
    """
    sender_nonce = 3
    creator = pre.deploy_contract(
        code=delegated_sender_code(
            Op.POP(Op.CREATE(0, 0, 0))
            + Op.SSTORE(
                SLOT_LEGACY_NONCE, Op.TXPARAM(Spec.TXPARAM_LEGACY_NONCE)
            )
            + Op.SSTORE(SLOT_NONCE_SEQ, Op.TXPARAM(Spec.TXPARAM_NONCE_SEQ))
            + Op.STOP
        )
    )
    sender = pre.fund_eoa(nonce=sender_nonce, delegation=creator)
    tx = Transaction(
        sender=sender,
        nonce=sender_nonce,
        frames=[
            verify_frame(),
            sender_frame(
                gas_limit=PROBE_FRAME_GAS,
                state_gas_limit=PROBE_FRAME_STATE_GAS,
            ),
        ],
        nonce_keys=[NONCE_KEY],
        nonce_seq=0,
        expected_receipt=TransactionReceipt(
            payer=sender,
            frame_receipts=[
                FrameReceipt(
                    status=Spec8141.STATUS_SUCCESS,
                    state_gas_used=fork.gas_costs().KEYED_NONCE_FIRST_USE,
                ),
                FrameReceipt(status=Spec8141.STATUS_SUCCESS),
            ],
        ),
    )
    created = compute_create_address(address=sender, nonce=sender_nonce)
    state_test(
        pre=pre,
        tx=tx,
        post={
            sender: Account(
                nonce=sender_nonce + 1,
                storage={
                    SLOT_LEGACY_NONCE: sender_nonce,
                    SLOT_NONCE_SEQ: 0,
                },
            ),
            created: Account(nonce=1, code=b""),
            Spec.NONCE_MANAGER: Account(
                storage={keyed_nonce_slot(sender, NONCE_KEY): 1}
            ),
        },
    )


def test_consumption_survives_frame_revert(
    state_test: StateTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    Revert a frame after the keyed domain was consumed.

    Nonce consumption is an approval effect: a later frame's revert
    leaves the consumed key's slot advanced and the state gas charged.
    """
    first_use = fork.gas_costs().KEYED_NONCE_FIRST_USE
    reverter = pre.deploy_contract(code=Op.REVERT(0, 0))
    sender = pre.fund_eoa()
    tx = Transaction(
        sender=sender,
        frames=[
            verify_frame(),
            sender_frame(target=reverter, gas_limit=WORKER_FRAME_GAS),
        ],
        nonce_keys=[NONCE_KEY],
        nonce_seq=0,
        expected_receipt=TransactionReceipt(
            payer=sender,
            frame_receipts=[
                default_verify_receipt(fork, first_use),
                FrameReceipt(status=Spec8141.STATUS_FAILURE),
            ],
        ),
    )
    state_test(
        pre=pre,
        tx=tx,
        post={
            Spec.NONCE_MANAGER: Account(
                storage={keyed_nonce_slot(sender, NONCE_KEY): 1}
            ),
            sender: Account(nonce=0),
        },
    )


def test_consumption_survives_atomic_batch_unroll(
    state_test: StateTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    Unroll an atomic batch after the keyed domain was consumed.

    Approval scope is banned inside a batch, so the consumption always
    precedes it; unrolling the batch restores the batch frames' state
    changes and leaves the consumed slot, the payer, and the state gas
    charge in place.
    """
    first_use = fork.gas_costs().KEYED_NONCE_FIRST_USE
    writer = pre.deploy_contract(code=Op.SSTORE(SLOT_EXECUTED, 1) + Op.STOP)
    reverter = pre.deploy_contract(code=Op.REVERT(0, 0))
    sender = pre.fund_eoa()
    tx = Transaction(
        sender=sender,
        frames=[
            verify_frame(),
            sender_frame(
                target=writer,
                flags=Spec8141.ATOMIC_BATCH_FLAG,
                gas_limit=WORKER_FRAME_GAS,
            ),
            sender_frame(target=reverter, gas_limit=WORKER_FRAME_GAS),
        ],
        nonce_keys=[NONCE_KEY],
        nonce_seq=0,
        expected_receipt=TransactionReceipt(
            payer=sender,
            frame_receipts=[
                default_verify_receipt(fork, first_use),
                FrameReceipt(status=Spec8141.STATUS_SUCCESS, state_gas_used=0),
                FrameReceipt(status=Spec8141.STATUS_FAILURE),
            ],
        ),
    )
    state_test(
        pre=pre,
        tx=tx,
        post={
            Spec.NONCE_MANAGER: Account(
                storage={keyed_nonce_slot(sender, NONCE_KEY): 1}
            ),
            writer: Account(storage={SLOT_EXECUTED: 0}),
            sender: Account(nonce=0),
        },
    )


@pytest.mark.parametrize(
    "key_count",
    [pytest.param(1, id="one_key"), pytest.param(2, id="two_keys")],
)
def test_first_use_state_gas_exact_budget(
    state_test: StateTestFiller, pre: Alloc, fork: Fork, key_count: int
) -> None:
    """
    Budget the approving frame's state gas at exactly the first-use
    charge of its keyed domains: the approval succeeds with the pool
    drained.
    """
    state_gas = fork.gas_costs().KEYED_NONCE_FIRST_USE * key_count
    nonce_keys = [NONCE_KEY + index for index in range(key_count)]
    sender = pre.fund_eoa()
    tx = Transaction(
        sender=sender,
        frames=[verify_frame(state_gas_limit=state_gas)],
        nonce_keys=nonce_keys,
        nonce_seq=0,
        expected_receipt=TransactionReceipt(
            payer=sender,
            frame_receipts=[default_verify_receipt(fork, state_gas)],
        ),
    )
    state_test(
        pre=pre,
        tx=tx,
        post={
            Spec.NONCE_MANAGER: Account(
                storage={
                    keyed_nonce_slot(sender, key): 1 for key in nonce_keys
                }
            ),
        },
    )


@pytest.mark.exception_test
@pytest.mark.parametrize(
    "key_count",
    [pytest.param(1, id="one_key"), pytest.param(2, id="two_keys")],
)
def test_first_use_state_gas_short_budget_fails_verify(
    state_test: StateTestFiller, pre: Alloc, fork: Fork, key_count: int
) -> None:
    """
    Budget the approving `VERIFY` frame's state gas one below the
    first-use charge: the approval halts, the `VERIFY` frame fails, and
    the transaction is invalid with nothing consumed.
    """
    state_gas = fork.gas_costs().KEYED_NONCE_FIRST_USE * key_count
    nonce_keys = [NONCE_KEY + index for index in range(key_count)]
    sender = pre.fund_eoa()
    tx = Transaction(
        sender=sender,
        frames=[verify_frame(state_gas_limit=state_gas - 1)],
        nonce_keys=nonce_keys,
        nonce_seq=0,
        error=TransactionException.TYPE_6_INVALID_FRAME_EXECUTION,
    )
    state_test(pre=pre, tx=tx, post={})


def test_first_use_state_gas_halts_contract_approver(
    state_test: StateTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    Approve from the sender's own code with a state budget one below
    the first-use charge.

    The `APPROVE` halts the call frame exceptionally: the `DEFAULT`
    frame fails with its execution budget consumed and no state gas
    attributed, and it records no approval, so the following `VERIFY`
    frame — running the same delegated code with the default state
    budget — approves instead and consumes the domain.
    """
    first_use = fork.gas_costs().KEYED_NONCE_FIRST_USE
    approve = Op.APPROVE(0, 0, Spec8141.APPROVE_EXECUTION_AND_PAYMENT)
    approver = pre.deploy_contract(code=approve)
    # A delegated EOA starts at nonce one, having sent its authorization.
    sender = pre.fund_eoa(delegation=approver)
    tx = Transaction(
        sender=sender,
        frames=[
            Frame(
                mode=Spec8141.MODE_DEFAULT,
                flags=Spec8141.APPROVE_EXECUTION_AND_PAYMENT,
                target=sender,
                gas_limit=WORKER_FRAME_GAS,
                state_gas_limit=first_use - 1,
            ),
            verify_frame(),
        ],
        nonce_keys=[NONCE_KEY],
        nonce_seq=0,
        expected_receipt=TransactionReceipt(
            payer=sender,
            frame_receipts=[
                FrameReceipt(
                    status=Spec8141.STATUS_FAILURE,
                    gas_used=WORKER_FRAME_GAS,
                    state_gas_used=0,
                ),
                FrameReceipt(
                    status=Spec8141.STATUS_SUCCESS,
                    # The failed frame's accesses are discarded, so the
                    # delegate is cold again at the second entry.
                    gas_used=fork.frame_entry_gas_calculator()(
                        target_warm=True, delegated=True
                    )
                    + approve.execution_cost(fork),
                    state_gas_used=first_use,
                ),
            ],
        ),
    )
    state_test(
        pre=pre,
        tx=tx,
        post={
            Spec.NONCE_MANAGER: Account(
                storage={keyed_nonce_slot(sender, NONCE_KEY): 1}
            ),
            sender: Account(nonce=1),
        },
    )


def test_contract_approver_pays_first_use(
    state_test: StateTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    Approve from the sender's own code with the first-use charge
    covered: the approving `DEFAULT` frame's receipt attributes the
    state gas, and the domain is consumed.
    """
    first_use = fork.gas_costs().KEYED_NONCE_FIRST_USE
    approve = Op.APPROVE(0, 0, Spec8141.APPROVE_EXECUTION_AND_PAYMENT)
    approver = pre.deploy_contract(code=approve)
    # A delegated EOA starts at nonce one, having sent its authorization.
    sender = pre.fund_eoa(delegation=approver)
    tx = Transaction(
        sender=sender,
        frames=[
            Frame(
                mode=Spec8141.MODE_DEFAULT,
                flags=Spec8141.APPROVE_EXECUTION_AND_PAYMENT,
                target=sender,
                gas_limit=WORKER_FRAME_GAS,
                state_gas_limit=first_use,
            ),
        ],
        nonce_keys=[NONCE_KEY],
        nonce_seq=0,
        expected_receipt=TransactionReceipt(
            payer=sender,
            frame_receipts=[
                FrameReceipt(
                    status=Spec8141.STATUS_SUCCESS,
                    # The sender is warm at entry; resolving its
                    # delegation charges the delegate's cold access.
                    gas_used=fork.frame_entry_gas_calculator()(
                        target_warm=True, delegated=True
                    )
                    + approve.execution_cost(fork),
                    state_gas_used=first_use,
                ),
            ],
        ),
    )
    state_test(
        pre=pre,
        tx=tx,
        post={
            Spec.NONCE_MANAGER: Account(
                storage={keyed_nonce_slot(sender, NONCE_KEY): 1}
            ),
            sender: Account(nonce=1),
        },
    )


def test_sponsor_pays_first_use(
    state_test: StateTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    Sponsor a keyed transaction: the sender's `VERIFY` frame approves
    execution only and pays no state gas, while the payer's `VERIFY`
    frame approves payment and carries the first-use charge of the
    sender's keyed domain in its receipt.
    """
    first_use = fork.gas_costs().KEYED_NONCE_FIRST_USE
    sender = pre.fund_eoa()
    payer = pre.fund_eoa()
    tx = Transaction(
        sender=sender,
        frames=[
            verify_frame(flags=Spec8141.APPROVE_EXECUTION),
            verify_frame(flags=Spec8141.APPROVE_PAYMENT, target=payer),
        ],
        signatures=[
            FrameSignature(
                scheme=Spec8141.SCHEME_SECP256K1,
                signer=Bytes(sender),
            ),
            FrameSignature(
                scheme=Spec8141.SCHEME_SECP256K1,
                signer=Bytes(payer),
                secret_key=payer.key,
            ),
        ],
        nonce_keys=[NONCE_KEY],
        nonce_seq=0,
        expected_receipt=TransactionReceipt(
            payer=payer,
            frame_receipts=[
                default_verify_receipt(fork, 0),
                FrameReceipt(
                    status=Spec8141.STATUS_SUCCESS,
                    gas_used=default_code_frame_gas(fork, target_warm=False),
                    state_gas_used=first_use,
                ),
            ],
        ),
    )
    state_test(
        pre=pre,
        tx=tx,
        post={
            Spec.NONCE_MANAGER: Account(
                storage={keyed_nonce_slot(sender, NONCE_KEY): 1}
            ),
            sender: Account(nonce=0),
            payer: Account(nonce=0),
        },
    )


@pytest.mark.pre_alloc_mutable
def test_legacy_nonce_exhaustion_halts_approval(
    state_test: StateTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    Approve payment on the legacy key set when the increment would
    exceed the maximum sequence.

    The sender starts one below the last usable nonce, so the
    transaction is valid, and its `SENDER` frame executes a `CREATE`
    that consumes that last nonce before approving payment. The
    approval halts the call frame exceptionally — the frame fails with
    its execution budget consumed, undoing the `CREATE` with it — so
    the later `VERIFY` frame finds the original nonce and approves.
    The sender runs its frames through a delegation that approves the
    allowed scope in every frame and creates in the `SENDER` frame.
    """
    sender_nonce = Spec.MAX_NONCE_SEQ - 1
    frame_index = Op.TXPARAM(Spec8141.TXPARAM_FRAME_INDEX)
    exhauster = pre.deploy_contract(
        code=delegated_sender_code(
            Op.POP(Op.CREATE(0, 0, 0))
            + Op.APPROVE(
                0,
                0,
                Op.FRAMEPARAM(frame_index, Spec8141.FRAMEPARAM_ALLOWED_SCOPE),
            )
        )
    )
    sender = pre.fund_eoa(nonce=sender_nonce, delegation=exhauster)
    tx = Transaction(
        sender=sender,
        nonce=sender_nonce,
        frames=[
            verify_frame(flags=Spec8141.APPROVE_EXECUTION),
            sender_frame(
                flags=Spec8141.APPROVE_PAYMENT,
                gas_limit=PROBE_FRAME_GAS,
                state_gas_limit=PROBE_FRAME_STATE_GAS,
            ),
            verify_frame(flags=Spec8141.APPROVE_PAYMENT),
        ],
        nonce_keys=[0],
        nonce_seq=sender_nonce,
        expected_receipt=TransactionReceipt(
            payer=sender,
            frame_receipts=[
                FrameReceipt(status=Spec8141.STATUS_SUCCESS, state_gas_used=0),
                FrameReceipt(
                    status=Spec8141.STATUS_FAILURE,
                    gas_used=PROBE_FRAME_GAS,
                    state_gas_used=0,
                ),
                FrameReceipt(status=Spec8141.STATUS_SUCCESS, state_gas_used=0),
            ],
        ),
    )
    created = compute_create_address(address=sender, nonce=sender_nonce)
    state_test(
        pre=pre,
        tx=tx,
        post={
            sender: Account(nonce=Spec.MAX_NONCE_SEQ),
            created: Account.NONEXISTENT,
            Spec.NONCE_MANAGER: Account(storage={}),
        },
    )


def test_nonce_manager_direct_call_reverts(
    state_test: StateTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    Call the nonce manager directly, statically and not: both calls
    revert with empty return data, and the contract holds its runtime
    code; only the protocol writes its slots.
    """
    storage = Storage()
    caller = pre.deploy_contract(
        code=Op.SSTORE(
            storage.store_next(1),
            Op.ADD(1, Op.CALL(address=Spec.NONCE_MANAGER)),
        )
        + Op.SSTORE(storage.store_next(1), Op.ADD(1, Op.RETURNDATASIZE))
        + Op.SSTORE(
            storage.store_next(1),
            Op.ADD(1, Op.STATICCALL(address=Spec.NONCE_MANAGER)),
        )
        + Op.SSTORE(storage.store_next(1), Op.ADD(1, Op.RETURNDATASIZE))
        + Op.SSTORE(
            storage.store_next(len(Spec.NONCE_MANAGER_CODE)),
            Op.EXTCODESIZE(Spec.NONCE_MANAGER),
        )
        + Op.STOP
    )
    sender = pre.fund_eoa()
    tx = Transaction(
        sender=sender,
        frames=[
            verify_frame(),
            default_frame(
                target=caller,
                gas_limit=PROBE_FRAME_GAS,
                state_gas_limit=PROBE_FRAME_STATE_GAS,
            ),
        ],
        nonce_keys=[NONCE_KEY],
        nonce_seq=0,
    )
    state_test(
        pre=pre,
        tx=tx,
        post={
            caller: Account(storage=storage),
            Spec.NONCE_MANAGER: Account(
                nonce=Spec.NONCE_MANAGER_NONCE,
                code=Spec.NONCE_MANAGER_CODE,
                storage={keyed_nonce_slot(sender, NONCE_KEY): 1},
            ),
        },
    )


def test_nonce_manager_stays_cold(
    state_test: StateTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    Measure a `BALANCE` of the nonce manager from a `DEFAULT` frame
    after a keyed approval.

    The approval's slot read and write are protocol bookkeeping: they
    leave the nonce manager cold, so the access pays the cold cost.
    """
    first_use = fork.gas_costs().KEYED_NONCE_FIRST_USE
    measured = Op.BALANCE(address=Spec.NONCE_MANAGER, address_warm=False)
    access_gas = Op.BALANCE(address_warm=False).gas_cost(fork)
    probe_code = CodeGasMeasure(
        code=measured,
        overhead_cost=measured.gas_cost(fork) - access_gas,
        extra_stack_items=1,
        sstore_key=SLOT_RESULT,
    )
    probe = pre.deploy_contract(code=probe_code)
    sender = pre.fund_eoa()
    tx = Transaction(
        sender=sender,
        frames=[
            verify_frame(),
            default_frame(
                target=probe,
                gas_limit=PROBE_FRAME_GAS,
                state_gas_limit=PROBE_FRAME_STATE_GAS,
            ),
        ],
        nonce_keys=[NONCE_KEY],
        nonce_seq=0,
        expected_receipt=TransactionReceipt(
            payer=sender,
            frame_receipts=[
                default_verify_receipt(fork, first_use),
                FrameReceipt(
                    status=Spec8141.STATUS_SUCCESS,
                    gas_used=fork.gas_costs().COLD_ACCOUNT_ACCESS
                    + probe_code.execution_cost(fork),
                    state_gas_used=probe_code.state_cost(fork),
                ),
            ],
        ),
    )
    state_test(
        pre=pre,
        tx=tx,
        post={probe: Account(storage={SLOT_RESULT: access_gas})},
    )


@pytest.mark.pre_alloc_mutable
@pytest.mark.parametrize("changed_field", ["keys", "sequence"])
@pytest.mark.parametrize(
    "resign",
    [pytest.param(False, marks=pytest.mark.exception_test), True],
)
def test_signature_binds_nonce_fields(
    state_test: StateTestFiller,
    pre: Alloc,
    changed_field: str,
    resign: bool,
) -> None:
    """Reject changed nonce fields unless the sender signs them again."""
    sender = pre.fund_eoa()
    tx = Transaction(
        sender=sender,
        frames=[verify_frame()],
        nonce_keys=[NONCE_KEY],
        nonce_seq=0,
    )
    tx.sign()
    changed_keys = (
        [NONCE_KEY, OTHER_KEY] if changed_field == "keys" else [NONCE_KEY]
    )
    changed_seq = 1 if changed_field == "sequence" else 0
    slots = used_key_slots(sender, {NONCE_KEY: 1}) if changed_seq else {}
    if slots:
        nonce_manager_with_slots(pre, slots)
    tx = tx.copy(nonce_keys=changed_keys, nonce_seq=changed_seq)
    if resign:
        tx.signatures = None
    else:
        # Recovery on the changed digest no longer matches the signer.
        tx.error = TransactionException.TYPE_6_INVALID_FRAME_FORMAT
    if resign:
        slots = {
            keyed_nonce_slot(sender, key): changed_seq + 1
            for key in changed_keys
        }
    state_test(
        pre=pre,
        tx=tx,
        post={
            sender: Account(nonce=0),
            Spec.NONCE_MANAGER: Account(storage=slots),
        },
    )


@pytest.mark.parametrize("revert_outer", [False, True])
def test_nested_approval_follows_enclosing_frame(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    revert_outer: bool,
) -> None:
    """Commit a nested approval only when its enclosing frame succeeds."""
    first_use = fork.gas_costs().KEYED_NONCE_FIRST_USE
    approver = pre.deploy_contract(
        Conditional(
            condition=Op.CALLDATASIZE,
            if_true=Op.APPROVE(0, 0, Spec8141.APPROVE_EXECUTION_AND_PAYMENT),
            if_false=Op.POP(Op.CALL(address=Op.ADDRESS, args_size=1))
            + (Op.REVERT(0, 0) if revert_outer else Op.STOP),
        )
    )
    sender = pre.fund_eoa(delegation=approver)
    frames = [
        default_frame(
            target=sender,
            flags=Spec8141.APPROVE_EXECUTION_AND_PAYMENT,
            gas_limit=WORKER_FRAME_GAS,
            state_gas_limit=first_use,
        )
    ]
    receipts = [
        FrameReceipt(
            status=Spec8141.STATUS_FAILURE
            if revert_outer
            else Spec8141.STATUS_SUCCESS,
            state_gas_used=0 if revert_outer else first_use,
        )
    ]
    if revert_outer:
        frames.append(verify_frame(data=b"\x01", state_gas_limit=first_use))
        receipts.append(
            FrameReceipt(
                status=Spec8141.STATUS_SUCCESS, state_gas_used=first_use
            )
        )
    tx = Transaction(
        sender=sender,
        frames=frames,
        nonce_keys=[NONCE_KEY],
        nonce_seq=0,
        expected_receipt=TransactionReceipt(
            payer=sender, frame_receipts=receipts
        ),
    )
    state_test(
        pre=pre,
        tx=tx,
        post={
            sender: Account(nonce=1),
            Spec.NONCE_MANAGER: Account(
                storage={keyed_nonce_slot(sender, NONCE_KEY): 1}
            ),
        },
    )


@pytest.mark.pre_alloc_mutable
@pytest.mark.parametrize("sender_nonce", [3, Spec.MAX_NONCE_SEQ - 2])
def test_legacy_approval_increments_live_nonce(
    state_test: StateTestFiller, pre: Alloc, sender_nonce: int
) -> None:
    """Keep a successful CREATE nonce increment when payment is approved."""
    creator = pre.deploy_contract(
        delegated_sender_code(Op.POP(Op.CREATE(0, 0, 0)) + Op.STOP)
    )
    sender = pre.fund_eoa(nonce=sender_nonce, delegation=creator)
    tx = Transaction(
        sender=sender,
        nonce=sender_nonce,
        nonce_keys=[0],
        nonce_seq=sender_nonce,
        frames=[
            verify_frame(flags=Spec8141.APPROVE_EXECUTION),
            sender_frame(
                gas_limit=PROBE_FRAME_GAS,
                state_gas_limit=PROBE_FRAME_STATE_GAS,
            ),
            verify_frame(flags=Spec8141.APPROVE_PAYMENT),
        ],
        expected_receipt=TransactionReceipt(
            payer=sender,
            frame_receipts=[
                FrameReceipt(status=Spec8141.STATUS_SUCCESS) for _ in range(3)
            ],
        ),
    )
    state_test(
        pre=pre,
        tx=tx,
        post={
            sender: Account(nonce=sender_nonce + 2),
            compute_create_address(
                address=sender, nonce=sender_nonce
            ): Account(nonce=1),
            Spec.NONCE_MANAGER: Account(storage={}),
        },
    )
