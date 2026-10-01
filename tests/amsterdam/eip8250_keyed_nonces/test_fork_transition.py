"""
Tests for the EIP-8250 fork transition.

The fork initializes the nonce manager at `Spec.NONCE_MANAGER` when it
activates: the runtime code is installed and the nonce raised to one,
keeping a higher nonce and any balance the account already had. Every
other EIP-8250 test starts at a fork where the account is already in
the genesis allocation, so these tests are the only ones exercising the
initialization itself.

As with the EIP-8141 transition tests, the pre-fork blocks contain
nothing the pseudo-fork's shared spec module disagrees on across the
boundary — plain transfers and `EXTCODESIZE` probes — since the
transition tool runs every block with the EIP enabled. The keyed
payload switch itself, a pre-fork frame transaction being rejected
from the boundary on, has to wait for a dedicated `bogota` spec
package.
"""

import pytest
from execution_testing import (
    Account,
    Alloc,
    BalAccountExpectation,
    BalCodeChange,
    BalNonceChange,
    Block,
    BlockAccessListExpectation,
    BlockchainTestFiller,
    Op,
    Transaction,
    TransactionException,
)

from ..eip8141_frame_transactions.helpers import verify_frame
from .helpers import NONCE_KEY
from .spec import Spec, keyed_nonce_slot, ref_spec_8250

REFERENCE_SPEC_GIT_PATH = ref_spec_8250.git_path
REFERENCE_SPEC_VERSION = ref_spec_8250.version

pytestmark = pytest.mark.valid_at_transition_to("EIP8250")

FORK_TIMESTAMP = 15_000
"""Timestamp at which the transition fork activates EIP-8250."""

NONCE_MANAGER_UNTOUCHED = BlockAccessListExpectation(
    account_expectations={
        Spec.NONCE_MANAGER: BalAccountExpectation(
            nonce_changes=[], code_changes=[], storage_changes=[]
        ),
    }
)
"""
The nonce manager is in the block access list, read by a probe, and
records no code, nonce or storage change: outside the fork block the
initialization does not run.
"""


def nonce_manager_installed(
    pre_fork_nonce: int | None,
) -> BlockAccessListExpectation:
    """
    Return the fork block's expectation: the initialization recorded at
    block access index 0 (EIP-7928's pre-execution index) as the code
    change and, when the nonce moves, the nonce change to one; an
    account that already had a higher nonce records no nonce change.
    """
    nonce_changes = []
    if (pre_fork_nonce or 0) < Spec.NONCE_MANAGER_NONCE:
        nonce_changes = [
            BalNonceChange(
                block_access_index=0, post_nonce=Spec.NONCE_MANAGER_NONCE
            )
        ]
    return BlockAccessListExpectation(
        account_expectations={
            Spec.NONCE_MANAGER: BalAccountExpectation(
                nonce_changes=nonce_changes,
                code_changes=[
                    BalCodeChange(
                        block_access_index=0,
                        new_code=Spec.NONCE_MANAGER_CODE,
                    )
                ],
                storage_changes=[],
            ),
        }
    )


@pytest.mark.pre_alloc_mutable
@pytest.mark.parametrize(
    "pre_fork_nonce,pre_fork_balance",
    [
        pytest.param(None, None, id="absent_before_fork"),
        pytest.param(0, 1, id="balance_before_fork"),
        pytest.param(7, 1, id="nonce_and_balance_before_fork"),
    ],
)
def test_nonce_manager_initialized_at_fork_transition(
    blockchain_test: BlockchainTestFiller,
    pre: Alloc,
    pre_fork_nonce: int | None,
    pre_fork_balance: int | None,
) -> None:
    """
    Initialize the nonce manager at the fork block and nothing else.

    A probe contract records `EXTCODESIZE` of the nonce manager keyed
    by block number, so each block's view is visible in the post-state:
    no code before the fork, the runtime code from the fork block on.
    The post-state pins the nonce at one for an account that did not
    exist or had a zero nonce, at its own value for one with a higher
    nonce, and the balance as it was — including a pre-fork transfer.
    The fork block's access list records the initialization at block
    access index 0, and no other block records a change.
    """
    sender = pre.fund_eoa()
    probe = pre.deploy_contract(
        Op.SSTORE(Op.NUMBER, Op.EXTCODESIZE(Spec.NONCE_MANAGER)) + Op.STOP
    )
    if pre_fork_nonce is not None and pre_fork_balance is not None:
        pre[Spec.NONCE_MANAGER] = Account(
            nonce=pre_fork_nonce, balance=pre_fork_balance
        )

    blocks = [
        Block(
            timestamp=FORK_TIMESTAMP - 1,
            txs=[
                Transaction(sender=sender, to=probe),
                # Before the fork there is no code at the address: the
                # call is a plain transfer.
                Transaction(sender=sender, to=Spec.NONCE_MANAGER, value=1),
            ],
            expected_block_access_list=NONCE_MANAGER_UNTOUCHED,
        ),
        Block(
            timestamp=FORK_TIMESTAMP,
            txs=[Transaction(sender=sender, to=probe)],
            expected_block_access_list=nonce_manager_installed(pre_fork_nonce),
        ),
        Block(
            timestamp=FORK_TIMESTAMP + 1,
            txs=[Transaction(sender=sender, to=probe)],
            expected_block_access_list=NONCE_MANAGER_UNTOUCHED,
        ),
    ]

    code_size = len(Spec.NONCE_MANAGER_CODE)
    post = {
        probe: Account(storage={1: 0, 2: code_size, 3: code_size}),
        Spec.NONCE_MANAGER: Account(
            nonce=max(pre_fork_nonce or 0, Spec.NONCE_MANAGER_NONCE),
            balance=(pre_fork_balance or 0) + 1,
            code=Spec.NONCE_MANAGER_CODE,
            storage={},
        ),
    }

    blockchain_test(pre=pre, blocks=blocks, post=post)


def test_keyed_transaction_in_first_post_fork_block(
    blockchain_test: BlockchainTestFiller,
    pre: Alloc,
) -> None:
    """
    Execute a keyed frame transaction in the block that activates the
    fork.

    The nonce manager is initialized before the block's transactions
    run, so the approval finds the account in place and writes the
    consumed key's slot into it.
    """
    sender = pre.fund_eoa()
    tx = Transaction(
        sender=sender,
        frames=[verify_frame()],
        nonce_keys=[NONCE_KEY],
        nonce_seq=0,
    )
    blocks = [
        Block(timestamp=FORK_TIMESTAMP - 1),
        Block(timestamp=FORK_TIMESTAMP, txs=[tx]),
    ]
    post = {
        Spec.NONCE_MANAGER: Account(
            nonce=Spec.NONCE_MANAGER_NONCE,
            code=Spec.NONCE_MANAGER_CODE,
            storage={keyed_nonce_slot(sender, NONCE_KEY): 1},
        ),
        sender: Account(nonce=0),
    }

    blockchain_test(pre=pre, blocks=blocks, post=post)


class PreKeyedFrameTransaction(Transaction):
    """Encode the EIP-8141 payload before keyed nonces activate."""

    def get_rlp_signing_fields(self) -> list[str]:
        """Use the scalar nonce in both the payload and signing envelope."""
        return [
            "chain_id",
            "nonce",
            "sender",
            "frames",
            "signing_signatures",
            "fees",
            "blob_versioned_hashes",
        ]


# TODO: Enable on a real post-Amsterdam fork with an EIP-8141 predecessor
# and fork-aware frame encoding. The pseudo-fork runs keyed rules on both
# sides of the boundary and cannot execute the pre-keyed transaction.
@pytest.mark.skip(
    reason="requires distinct pre/post-fork specs and frame payload encoding"
)
@pytest.mark.exception_test
def test_payload_switch_across_transition(
    blockchain_test: BlockchainTestFiller, pre: Alloc
) -> None:
    """Switch payloads at activation and reject a pre-fork authorization."""
    sender = pre.fund_eoa()
    before = PreKeyedFrameTransaction(
        sender=sender, nonce=0, frames=[verify_frame()]
    )
    old_authorization = PreKeyedFrameTransaction(
        sender=sender, nonce=1, frames=[verify_frame()]
    )
    old_authorization.sign()
    after = Transaction(
        sender=sender,
        nonce=1,
        nonce_keys=[0],
        nonce_seq=1,
        frames=[verify_frame()],
    )
    stale = after.copy(
        signatures=old_authorization.signatures,
        error=TransactionException.TYPE_6_INVALID_FRAME_FORMAT,
    )
    blockchain_test(
        pre=pre,
        blocks=[
            Block(timestamp=FORK_TIMESTAMP - 1, txs=[before]),
            Block(
                timestamp=FORK_TIMESTAMP,
                txs=[stale],
                exception=TransactionException.TYPE_6_INVALID_FRAME_FORMAT,
            ),
            # The invalid block does not become the parent: regenerated
            # authorization at the same boundary consumes nonce one.
            Block(timestamp=FORK_TIMESTAMP, txs=[after]),
        ],
        post={
            sender: Account(nonce=2),
            Spec.NONCE_MANAGER: Account(
                nonce=Spec.NONCE_MANAGER_NONCE,
                code=Spec.NONCE_MANAGER_CODE,
                storage={},
            ),
        },
    )
