"""
Multi-transaction EIP-8250 cases: sequence progression, replay
independence, and the keyed writes' appearance in the EIP-7928 block
access list.
"""

import pytest
from execution_testing import (
    Account,
    Alloc,
    BalAccountExpectation,
    BalStorageChange,
    BalStorageSlot,
    Block,
    BlockAccessListExpectation,
    BlockchainTestFiller,
    Fork,
    Transaction,
    TransactionReceipt,
)

from ..eip8141_frame_transactions.helpers import verify_frame
from .spec import Spec, keyed_nonce_slot, ref_spec_8250
from .test_keyed_nonces import NONCE_KEY, OTHER_KEY, keyed_tx_gas_used

REFERENCE_SPEC_GIT_PATH = ref_spec_8250.git_path
REFERENCE_SPEC_VERSION = ref_spec_8250.version

pytestmark = pytest.mark.valid_from("EIP8250")


def test_sequence_progression(
    blockchain_test: BlockchainTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    A consumed key's next use carries the next sequence and pays no
    surcharge; the slot holds the sequence after the last use.
    """
    sender = pre.fund_eoa()
    txs = [
        Transaction(
            sender=sender,
            frames=[verify_frame()],
            nonce_keys=[NONCE_KEY],
            nonce_seq=seq,
        )
        for seq in (0, 1)
    ]
    first_gas = keyed_tx_gas_used(fork, txs[0], first_uses=1)
    second_gas = keyed_tx_gas_used(fork, txs[1], first_uses=0)
    txs[0].expected_receipt = TransactionReceipt(cumulative_gas_used=first_gas)
    txs[1].expected_receipt = TransactionReceipt(
        cumulative_gas_used=first_gas + second_gas
    )
    blockchain_test(
        pre=pre,
        blocks=[Block(txs=txs)],
        post={
            Spec.NONCE_MANAGER: Account(
                storage={keyed_nonce_slot(sender, NONCE_KEY): 2}
            ),
            sender: Account(nonce=0),
        },
    )


def test_disjoint_keys_replay_independent(
    blockchain_test: BlockchainTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    Two transactions from one sender on disjoint non-zero keys carry
    the same sequence and are both valid in one block.
    """
    sender = pre.fund_eoa()
    txs = [
        Transaction(
            sender=sender,
            frames=[verify_frame()],
            nonce_keys=[key],
            nonce_seq=0,
        )
        for key in (NONCE_KEY, OTHER_KEY)
    ]
    blockchain_test(
        pre=pre,
        blocks=[Block(txs=txs)],
        post={
            Spec.NONCE_MANAGER: Account(
                storage={
                    keyed_nonce_slot(sender, NONCE_KEY): 1,
                    keyed_nonce_slot(sender, OTHER_KEY): 1,
                }
            ),
            sender: Account(nonce=0),
        },
    )


def test_bal_records_keyed_consumption(
    blockchain_test: BlockchainTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    The consumed key's slot write lands in the block access list under
    the nonce manager, while the sender shows no nonce change — the
    keyed domains replace the legacy bump entirely.
    """
    sender = pre.fund_eoa()
    block = Block(
        txs=[
            Transaction(
                sender=sender,
                frames=[verify_frame()],
                nonce_keys=[NONCE_KEY],
                nonce_seq=0,
            )
        ],
        expected_block_access_list=BlockAccessListExpectation(
            account_expectations={
                Spec.NONCE_MANAGER: BalAccountExpectation(
                    storage_changes=[
                        BalStorageSlot(
                            slot=keyed_nonce_slot(sender, NONCE_KEY),
                            slot_changes=[
                                BalStorageChange(
                                    block_access_index=1, post_value=1
                                )
                            ],
                        )
                    ],
                ),
                sender: BalAccountExpectation(
                    nonce_changes=[],
                ),
            }
        ),
    )
    blockchain_test(pre=pre, blocks=[block], post={})
