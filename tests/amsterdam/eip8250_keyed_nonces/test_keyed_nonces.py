"""
Tests for [EIP-8250: Keyed Nonces for Frame Transactions](https://eips.ethereum.org/EIPS/eip-8250).

A frame transaction selects its replay domains through `nonce_keys`:
key zero aliases the sender's account nonce, non-zero keys live in the
`NONCE_MANAGER` system contract's protocol-managed storage and are
consumed atomically by the payment-scoped `APPROVE`.
"""

from typing import List

import pytest
from execution_testing import (
    Account,
    Alloc,
    Bytes,
    Fork,
    FrameReceipt,
    Op,
    StateTestFiller,
    Storage,
    Transaction,
    TransactionException,
    TransactionReceipt,
)

from ..eip8141_frame_transactions.helpers import (
    sender_frame,
    verify_frame,
)
from ..eip8141_frame_transactions.spec import Spec as Spec8141
from .spec import Spec, keyed_nonce_slot, nonce_keys_hash, ref_spec_8250

REFERENCE_SPEC_GIT_PATH = ref_spec_8250.git_path
REFERENCE_SPEC_VERSION = ref_spec_8250.version

pytestmark = pytest.mark.valid_from("EIP8250")

NONCE_KEY = 0xBEEF
OTHER_KEY = 0xCAFE

# A fresh SSTORE is charged state gas under EIP-8037 and a frame
# transaction holds no state gas reservoir, so a writing frame needs
# more than the default frame gas — sized by fresh slots written.
WRITE_FRAME_GAS = 200_000
INTROSPECTION_FRAME_GAS = 500_000


def keyed_tx_gas_used(fork: Fork, tx: Transaction, first_uses: int) -> int:
    """
    Return the gas a keyed transaction of default-code `VERIFY` frames
    settles at: the intrinsic cost of its frames, signature entries,
    and nonce encodings, plus the first-use surcharge — the default
    code itself consumes no gas.
    """
    tx.sign()
    assert tx.frames is not None and tx.signatures is not None
    assert tx.nonce_keys is not None and tx.nonce_seq is not None
    intrinsic = fork.frame_transaction_intrinsic_cost_calculator()(
        frames=tx.frames,
        signatures=tx.signatures,
        extra_charged_bytes=[
            fork.keyed_nonce_calldata(
                nonce_keys=[int(key) for key in tx.nonce_keys],
                nonce_seq=int(tx.nonce_seq),
            )
        ],
        return_cost_deducted_prior_execution=True,
    )
    floor = fork.frame_transaction_data_floor_cost_calculator()(
        frames=tx.frames,
        signatures=tx.signatures,
        extra_charged_bytes=[
            fork.keyed_nonce_calldata(
                nonce_keys=[int(key) for key in tx.nonce_keys],
                nonce_seq=int(tx.nonce_seq),
            )
        ],
    )
    surcharge = first_uses * fork.gas_costs().KEYED_NONCE_FIRST_USE
    return max(intrinsic + surcharge, floor)


def test_keyed_nonce_consumption(
    state_test: StateTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    Consuming a fresh non-zero nonce key writes sequence one to its
    `NONCE_MANAGER` slot, charges the first-use surcharge, and leaves
    the sender's account nonce untouched.
    """
    sender = pre.fund_eoa()
    tx = Transaction(
        sender=sender,
        frames=[verify_frame()],
        nonce_keys=[NONCE_KEY],
        nonce_seq=0,
    )
    tx.expected_receipt = TransactionReceipt(
        cumulative_gas_used=keyed_tx_gas_used(fork, tx, first_uses=1)
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


def test_legacy_alias_key(
    state_test: StateTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    The explicit `[0]` key set aliases the legacy account nonce: the
    sender's nonce increments, no surcharge is charged, and the nonce
    manager's storage stays empty.
    """
    sender = pre.fund_eoa()
    tx = Transaction(
        sender=sender,
        frames=[verify_frame()],
        nonce_keys=[0],
        nonce_seq=0,
    )
    tx.expected_receipt = TransactionReceipt(
        cumulative_gas_used=keyed_tx_gas_used(fork, tx, first_uses=0)
    )
    state_test(
        pre=pre,
        tx=tx,
        post={
            Spec.NONCE_MANAGER: Account(storage={}),
            sender: Account(nonce=1),
        },
    )


def test_multi_key_consumption(
    state_test: StateTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    A multi-key set advances every selected domain to the same next
    sequence and pays the surcharge once per first-use key.
    """
    keys = [1, NONCE_KEY, 2**256 - 1]
    sender = pre.fund_eoa()
    tx = Transaction(
        sender=sender,
        frames=[verify_frame()],
        nonce_keys=keys,
        nonce_seq=0,
    )
    tx.expected_receipt = TransactionReceipt(
        cumulative_gas_used=keyed_tx_gas_used(fork, tx, first_uses=len(keys))
    )
    state_test(
        pre=pre,
        tx=tx,
        post={
            Spec.NONCE_MANAGER: Account(
                storage={keyed_nonce_slot(sender, key): 1 for key in keys}
            ),
            sender: Account(nonce=0),
        },
    )


@pytest.mark.parametrize(
    "nonce_keys,nonce_seq,sender_nonce,error",
    [
        pytest.param(
            [NONCE_KEY],
            1,
            0,
            TransactionException.NONCE_MISMATCH_TOO_HIGH,
            id="fresh_key_nonzero_seq",
            marks=pytest.mark.exception_test,
        ),
        pytest.param(
            [0],
            1,
            0,
            TransactionException.NONCE_MISMATCH_TOO_HIGH,
            id="legacy_alias_seq_too_high",
            marks=pytest.mark.exception_test,
        ),
        pytest.param(
            [0],
            0,
            1,
            TransactionException.NONCE_MISMATCH_TOO_LOW,
            id="legacy_alias_seq_too_low",
            marks=pytest.mark.exception_test,
        ),
    ],
)
@pytest.mark.pre_alloc_mutable
def test_stateful_validity(
    state_test: StateTestFiller,
    pre: Alloc,
    nonce_keys: List[int],
    nonce_seq: int,
    sender_nonce: int,
    error: TransactionException,
) -> None:
    """
    A transaction whose sequence does not match the current sequence
    of every selected key is statefully invalid.
    """
    sender = pre.fund_eoa(nonce=sender_nonce)
    tx = Transaction(
        sender=sender,
        nonce=sender_nonce,
        frames=[verify_frame()],
        nonce_keys=nonce_keys,
        nonce_seq=nonce_seq,
        error=error,
    )
    state_test(pre=pre, tx=tx, post={})


@pytest.mark.parametrize(
    "nonce_keys,nonce_seq,error",
    [
        pytest.param(
            [],
            0,
            TransactionException.TYPE_6_INVALID_FRAME_FORMAT,
            id="empty_key_set",
        ),
        pytest.param(
            list(range(1, Spec.MAX_NONCE_KEYS + 2)),
            0,
            TransactionException.TYPE_6_INVALID_FRAME_FORMAT,
            id="too_many_keys",
        ),
        pytest.param(
            [2, 1],
            0,
            TransactionException.TYPE_6_INVALID_FRAME_FORMAT,
            id="decreasing_keys",
        ),
        pytest.param(
            [1, 1],
            0,
            TransactionException.TYPE_6_INVALID_FRAME_FORMAT,
            id="duplicate_keys",
        ),
        pytest.param(
            [0, 1],
            0,
            TransactionException.TYPE_6_INVALID_FRAME_FORMAT,
            id="zero_key_in_multi_key_set",
        ),
        pytest.param(
            [NONCE_KEY],
            Spec.MAX_NONCE_SEQ,
            TransactionException.NONCE_IS_MAX,
            id="seq_at_exhaustion_bound",
        ),
    ],
)
@pytest.mark.exception_test
def test_static_validity(
    state_test: StateTestFiller,
    pre: Alloc,
    nonce_keys: List[int],
    nonce_seq: int,
    error: TransactionException,
) -> None:
    """
    Key sets violating the structural rules — empty, oversized, not
    strictly increasing, or mixing zero with other keys — and an
    exhausted sequence are invalid regardless of state.
    """
    sender = pre.fund_eoa()
    tx = Transaction(
        sender=sender,
        frames=[verify_frame()],
        nonce_keys=nonce_keys,
        nonce_seq=nonce_seq,
        error=error,
    )
    state_test(pre=pre, tx=tx, post={})


@pytest.mark.pre_alloc_mutable
def test_txparam_introspection(
    state_test: StateTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    The four introspection indices expose the pre-state legacy nonce,
    the key count, the canonical key-set hash, and the first key;
    `TXPARAM(0x01)` returns the keyed sequence.
    """
    keys = [5, 9]
    storage = Storage()
    reader = pre.deploy_contract(
        code=Op.SSTORE(storage.store_next(0), Op.TXPARAM(0x01))
        + Op.SSTORE(
            storage.store_next(3), Op.TXPARAM(Spec.TXPARAM_LEGACY_NONCE)
        )
        + Op.SSTORE(
            storage.store_next(len(keys)),
            Op.TXPARAM(Spec.TXPARAM_NONCE_KEY_COUNT),
        )
        + Op.SSTORE(
            storage.store_next(nonce_keys_hash(keys)),
            Op.TXPARAM(Spec.TXPARAM_NONCE_KEYS_HASH),
        )
        + Op.SSTORE(
            storage.store_next(keys[0]),
            Op.TXPARAM(Spec.TXPARAM_NONCE_KEY_0),
        )
    )
    sender = pre.fund_eoa(nonce=3)
    tx = Transaction(
        sender=sender,
        nonce=3,
        frames=[
            verify_frame(),
            sender_frame(target=reader, gas_limit=INTROSPECTION_FRAME_GAS),
        ],
        nonce_keys=keys,
        nonce_seq=0,
    )
    state_test(
        pre=pre,
        tx=tx,
        post={
            reader: Account(storage=storage),
            sender: Account(nonce=3),
        },
    )


def test_consumption_survives_frame_revert(
    state_test: StateTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    Nonce consumption is an approval effect: a later frame's revert
    leaves the consumed key's slot advanced.
    """
    reverter = pre.deploy_contract(code=Op.REVERT(0, 0))
    sender = pre.fund_eoa()
    tx = Transaction(
        sender=sender,
        frames=[verify_frame(), sender_frame(target=reverter)],
        nonce_keys=[NONCE_KEY],
        nonce_seq=0,
        expected_receipt=TransactionReceipt(
            frame_receipts=[
                FrameReceipt(status=Spec8141.STATUS_SUCCESS),
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
    Payment approved inside an atomic batch keeps its payer and its
    consumed nonce set when a batch frame fails and the batch unrolls.
    """
    reverter = pre.deploy_contract(code=Op.REVERT(0, 0))
    # A contract sender whose code approves whatever scope the current
    # frame allows: execution from the leading `VERIFY` frame, payment
    # from the atomic batch frame — a `VERIFY` frame cannot carry the
    # atomic flag, and a `SENDER` frame cannot approve execution.
    sender = pre.deploy_contract(
        code=Op.APPROVE(
            0,
            0,
            Op.FRAMEPARAM(
                Op.TXPARAM(Spec8141.TXPARAM_FRAME_INDEX),
                Spec8141.FRAMEPARAM_ALLOWED_SCOPE,
            ),
        ),
        balance=10**18,
    )
    tx = Transaction(
        sender=sender,
        nonce=1,
        frames=[
            verify_frame(flags=Spec8141.APPROVE_EXECUTION),
            sender_frame(
                flags=Spec8141.ATOMIC_BATCH_FLAG | Spec8141.APPROVE_PAYMENT,
            ),
            sender_frame(target=reverter),
        ],
        nonce_keys=[NONCE_KEY],
        nonce_seq=0,
        expected_receipt=TransactionReceipt(
            payer=sender,
            frame_receipts=[
                FrameReceipt(status=Spec8141.STATUS_SUCCESS),
                FrameReceipt(status=Spec8141.STATUS_SUCCESS),
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
            sender: Account(nonce=1),
        },
    )


def test_first_use_surcharge_boundary(
    state_test: StateTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    The default `VERIFY` code's payment approval charges the first-use
    surcharge from the frame's gas: exactly covering it succeeds.
    """
    surcharge = fork.gas_costs().KEYED_NONCE_FIRST_USE
    sender = pre.fund_eoa()
    tx = Transaction(
        sender=sender,
        frames=[verify_frame(gas_limit=surcharge)],
        nonce_keys=[NONCE_KEY],
        nonce_seq=0,
    )
    state_test(
        pre=pre,
        tx=tx,
        post={
            Spec.NONCE_MANAGER: Account(
                storage={keyed_nonce_slot(sender, NONCE_KEY): 1}
            ),
        },
    )


@pytest.mark.exception_test
def test_first_use_surcharge_out_of_gas(
    state_test: StateTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    A frame whose gas falls one short of the first-use surcharge fails
    its approval, invalidating the transaction with no key consumed.
    """
    surcharge = fork.gas_costs().KEYED_NONCE_FIRST_USE
    sender = pre.fund_eoa()
    tx = Transaction(
        sender=sender,
        frames=[verify_frame(gas_limit=surcharge - 1)],
        nonce_keys=[NONCE_KEY],
        nonce_seq=0,
        error=TransactionException.TYPE_6_INVALID_FRAME_EXECUTION,
    )
    state_test(pre=pre, tx=tx, post={})


def test_nonce_manager_direct_call_reverts(
    state_test: StateTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    An ordinary call to the nonce manager reverts with empty
    returndata; only the protocol writes its slots.
    """
    storage = Storage()
    caller = pre.deploy_contract(
        code=Op.SSTORE(
            storage.store_next(1),
            Op.ADD(1, Op.CALL(address=Spec.NONCE_MANAGER)),
        )
        + Op.SSTORE(storage.store_next(0), Op.RETURNDATASIZE)
    )
    sender = pre.fund_eoa()
    tx = Transaction(
        sender=sender,
        frames=[
            verify_frame(),
            sender_frame(target=caller, gas_limit=WRITE_FRAME_GAS),
        ],
        nonce_keys=[0],
        nonce_seq=0,
    )
    state_test(
        pre=pre,
        tx=tx,
        post={
            caller: Account(storage=storage),
            Spec.NONCE_MANAGER: Account(
                code=Bytes(Spec.NONCE_MANAGER_CODE), storage={}
            ),
        },
    )
