"""
Tests for the EIP-8272 fork transition.

The fork initializes the recent root contract at `Spec.RECENT_ROOT_ADDRESS`
when it activates: a nonexistent account is created with the code and
nonce one; an existing account with empty code gets the code, its nonce
raised to at least one and its balance kept. Every other EIP-8272 test
starts at a fork where the contract is already in the genesis allocation,
so these tests are the only ones exercising the initialization itself.

Under the pseudo-fork model the transition tool runs every block of a
transition fixture with EIP-8272's spec module, the pre-fork blocks
included. These tests work because their pre-fork blocks contain nothing
the two sides disagree on: a plain transfer and an `EXTCODESIZE` probe.
The case where activation finds an occupied address, which the EIP makes
an invalid block, cannot be filled: fills apply the install through the
framework, not through the spec's `apply_fork`. Direct activation tests
in `tests/json_loader/test_recent_root_activation.py` cover rejection of
both nonempty code and nonempty storage.
"""

import pytest
from execution_testing import (
    Account,
    Alloc,
    BalAccountExpectation,
    Block,
    BlockAccessListExpectation,
    BlockchainTestFiller,
    Fork,
    Op,
    Transaction,
)

from ..eip8141_frame_transactions.helpers import sender_frame, verify_frame
from .helpers import recent_root_frame, write_frame
from .spec import (
    Spec,
    entry_hash,
    ref_spec_8272,
    source_id,
    storage_key,
    validation_tuple,
)

REFERENCE_SPEC_GIT_PATH = ref_spec_8272.git_path
REFERENCE_SPEC_VERSION = ref_spec_8272.version

pytestmark = pytest.mark.valid_at_transition_to("EIP8272")

FORK_TIMESTAMP = 15_000
"""Timestamp at which the transition fork activates EIP-8272."""

SLOT_EXECUTED = 0x01
"""Storage slot used by target contracts to record execution."""

FORK_SLOT = 500
"""Slot of the block activating the fork."""

SALT = bytes(32)

CONTRACT_WITHOUT_CODE_CHANGE = BlockAccessListExpectation(
    account_expectations={
        Spec.RECENT_ROOT_ADDRESS: BalAccountExpectation(code_changes=[]),
    }
)
"""
The contract's address is in the block access list, reached by a
transaction, and records no code change: the install is not a block-level
operation and never appears there, in the fork block included.
"""

CONTRACT_UNTOUCHED = BlockAccessListExpectation(
    account_expectations={
        Spec.RECENT_ROOT_ADDRESS: BalAccountExpectation.empty(),
    }
)
"""The contract's address is read by a transaction and records no change."""


@pytest.mark.pre_alloc_mutable
@pytest.mark.parametrize(
    "pre_fork_nonce,pre_fork_balance",
    [
        pytest.param(None, None, id="absent_before_fork"),
        pytest.param(0, 1, id="balance_before_fork"),
        pytest.param(7, 1, id="nonce_and_balance_before_fork"),
    ],
)
def test_recent_root_contract_initialized_at_fork_transition(
    blockchain_test: BlockchainTestFiller,
    pre: Alloc,
    fork: Fork,
    pre_fork_nonce: int | None,
    pre_fork_balance: int | None,
) -> None:
    """
    Initialize the recent root contract at the fork block and nothing
    else.

    A probe records `EXTCODESIZE` of the contract's address keyed by block
    number: no code before the fork, the runtime code from the fork block
    on. An address nobody touched ends with nonce one and a zero balance;
    an account that already existed keeps its balance and gets nonce one
    unless its nonce was already higher.
    """
    sender = pre.fund_eoa()
    probe = pre.deploy_contract(
        Op.SSTORE(Op.NUMBER, Op.EXTCODESIZE(Spec.RECENT_ROOT_ADDRESS))
        + Op.STOP
    )
    if pre_fork_nonce is not None and pre_fork_balance is not None:
        pre[Spec.RECENT_ROOT_ADDRESS] = Account(
            nonce=pre_fork_nonce, balance=pre_fork_balance
        )

    blocks = [
        Block(
            timestamp=FORK_TIMESTAMP - 1,
            slot_number=FORK_SLOT - 1,
            txs=[
                Transaction(sender=sender, to=probe),
                # Before the fork there is no code at the address: the
                # call is a plain transfer of nothing.
                Transaction(sender=sender, to=Spec.RECENT_ROOT_ADDRESS),
            ],
            expected_block_access_list=CONTRACT_WITHOUT_CODE_CHANGE,
        ),
        Block(
            timestamp=FORK_TIMESTAMP,
            slot_number=FORK_SLOT,
            txs=[Transaction(sender=sender, to=probe)],
            expected_block_access_list=CONTRACT_UNTOUCHED,
        ),
        Block(
            timestamp=FORK_TIMESTAMP + 1,
            slot_number=FORK_SLOT + 1,
            txs=[Transaction(sender=sender, to=probe)],
            expected_block_access_list=CONTRACT_UNTOUCHED,
        ),
    ]

    code_size = len(Spec.RECENT_ROOT_CODE)
    post = {
        probe: Account(storage={1: 0, 2: code_size, 3: code_size}),
        Spec.RECENT_ROOT_ADDRESS: Account(
            nonce=max(pre_fork_nonce or 0, Spec.RECENT_ROOT_NONCE),
            balance=pre_fork_balance or 0,
            code=Spec.RECENT_ROOT_CODE,
            storage={},
        ),
    }

    blockchain_test(pre=pre, blocks=blocks, post=post)


def test_publish_in_fork_block_and_verify_after(
    blockchain_test: BlockchainTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """
    Publish a root in the block that activates the fork and verify it in
    the next block.

    The contract is initialized before the fork block's transactions run,
    so a write in that block finds the code in place; a reference to the
    fork block's slot verifies from the following slot on. Storage is
    empty at activation, so nothing earlier could be referenced.
    """
    sender = pre.fund_eoa()
    target = pre.deploy_contract(code=Op.SSTORE(SLOT_EXECUTED, 1) + Op.STOP)
    source = source_id(sender, SALT)
    root = (0xF0).to_bytes(32, "big")
    key = storage_key(source, FORK_SLOT)

    blocks = [
        Block(timestamp=FORK_TIMESTAMP - 1, slot_number=FORK_SLOT - 1),
        Block(
            timestamp=FORK_TIMESTAMP,
            slot_number=FORK_SLOT,
            txs=[
                Transaction(
                    sender=sender,
                    frames=[verify_frame(), write_frame(SALT, root)],
                )
            ],
            expected_block_access_list=CONTRACT_WITHOUT_CODE_CHANGE,
        ),
        Block(
            timestamp=FORK_TIMESTAMP + 1,
            slot_number=FORK_SLOT + 1,
            txs=[
                Transaction(
                    sender=sender,
                    frames=[
                        recent_root_frame(
                            validation_tuple(source, FORK_SLOT, root)
                        ),
                        verify_frame(),
                        sender_frame(target=target),
                    ],
                )
            ],
        ),
    ]
    post = {
        Spec.RECENT_ROOT_ADDRESS: Account(
            nonce=Spec.RECENT_ROOT_NONCE,
            code=Spec.RECENT_ROOT_CODE,
            storage={
                key: int.from_bytes(entry_hash(source, FORK_SLOT, root), "big")
            },
        ),
        target: Account(storage={SLOT_EXECUTED: 1}),
    }

    blockchain_test(pre=pre, blocks=blocks, post=post)
