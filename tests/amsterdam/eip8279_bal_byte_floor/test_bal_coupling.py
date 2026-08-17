"""
Tests coupling the EIP-8279 floor to the EIP-7928 block access list.

The byte floor is defined over the bytes the transaction contributes to
the block access list, so each test here pins both sides of the same
block: the list's contents and the floor-bound `gas_used` they imply.
"""

import pytest
from execution_testing import (
    Alloc,
    AuthorizationTuple,
    BalAccountExpectation,
    BalCodeChange,
    BalNonceChange,
    BalStorageChange,
    BalStorageSlot,
    Block,
    BlockAccessListExpectation,
    BlockchainTestFiller,
    Fork,
    Header,
    Op,
    Transaction,
)

from ...prague.eip7702_set_code_tx.spec import Spec as Spec7702
from .helpers import (
    ADDRESS_FLOOR,
    COLD_SLOT,
    STORAGE_KEY_FLOOR,
    STORAGE_VALUE_FLOOR,
    scaffold_data,
)
from .spec import Spec, ref_spec_8279

REFERENCE_SPEC_GIT_PATH = ref_spec_8279.git_path
REFERENCE_SPEC_VERSION = ref_spec_8279.version

pytestmark = pytest.mark.valid_from("EIP8279")


def test_bal_read_bytes_floor(
    blockchain_test: BlockchainTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    A cold storage read lands in the list as a storage read, and its
    key's bytes land on the floor.
    """
    data = scaffold_data(fork, execution_headroom=STORAGE_KEY_FLOOR + 5_000)
    reader = pre.deploy_contract(code=Op.SLOAD(COLD_SLOT))
    block = Block(
        txs=[Transaction(sender=pre.fund_eoa(), to=reader, data=data)],
        header_verify=Header(
            gas_used=fork.transaction_data_floor_cost_calculator()(data=data)
            + STORAGE_KEY_FLOOR
        ),
        expected_block_access_list=BlockAccessListExpectation(
            account_expectations={
                reader: BalAccountExpectation(
                    storage_reads=[COLD_SLOT],
                    storage_changes=[],
                ),
            }
        ),
    )
    blockchain_test(pre=pre, blocks=[block], post={})


@pytest.mark.parametrize("restore", [True, False])
def test_bal_write_demotion_returns_bytes(
    blockchain_test: BlockchainTestFiller,
    pre: Alloc,
    fork: Fork,
    restore: bool,
) -> None:
    """
    Restoring a slot demotes its entry to a read in the list and
    returns the value's bytes; a lasting write keeps both.
    """
    original, updated, other = 5, 7, 9
    slot = 0xB
    final = original if restore else other
    data = scaffold_data(
        fork,
        execution_headroom=STORAGE_KEY_FLOOR + STORAGE_VALUE_FLOOR + 30_000,
    )
    contract = pre.deploy_contract(
        code=Op.SSTORE(slot, updated) + Op.SSTORE(slot, final),
        storage={slot: original},
    )
    if restore:
        contract_expectation = BalAccountExpectation(
            storage_reads=[slot],
            storage_changes=[],
        )
        value_bytes_floor = 0
    else:
        contract_expectation = BalAccountExpectation(
            storage_reads=[],
            storage_changes=[
                BalStorageSlot(
                    slot=slot,
                    slot_changes=[
                        BalStorageChange(
                            block_access_index=1, post_value=final
                        )
                    ],
                )
            ],
        )
        value_bytes_floor = STORAGE_VALUE_FLOOR
    block = Block(
        txs=[Transaction(sender=pre.fund_eoa(), to=contract, data=data)],
        header_verify=Header(
            gas_used=fork.transaction_data_floor_cost_calculator()(data=data)
            + STORAGE_KEY_FLOOR
            + value_bytes_floor
        ),
        expected_block_access_list=BlockAccessListExpectation(
            account_expectations={contract: contract_expectation}
        ),
    )
    blockchain_test(pre=pre, blocks=[block], post={})


def test_bal_reverted_read_keeps_bytes(
    blockchain_test: BlockchainTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    A read inside a reverted frame stays in the list, so its bytes stay
    on the floor.
    """
    data = scaffold_data(
        fork,
        execution_headroom=ADDRESS_FLOOR + STORAGE_KEY_FLOOR + 10_000,
    )
    child = pre.deploy_contract(code=Op.SLOAD(COLD_SLOT) + Op.REVERT(0, 0))
    caller = pre.deploy_contract(code=Op.POP(Op.CALL(address=child)))
    block = Block(
        txs=[Transaction(sender=pre.fund_eoa(), to=caller, data=data)],
        header_verify=Header(
            gas_used=fork.transaction_data_floor_cost_calculator()(data=data)
            + ADDRESS_FLOOR
            + STORAGE_KEY_FLOOR
        ),
        expected_block_access_list=BlockAccessListExpectation(
            account_expectations={
                child: BalAccountExpectation(
                    storage_reads=[COLD_SLOT],
                    storage_changes=[],
                ),
                caller: BalAccountExpectation.empty(),
            }
        ),
    )
    blockchain_test(pre=pre, blocks=[block], post={})


def test_bal_authorization_seed_matches_designation(
    blockchain_test: BlockchainTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    An applied authorization publishes the authority's nonce and
    delegation code in the list; the static seed prices exactly those
    bytes plus the authority's address.
    """
    auth_floor = Spec.AUTHORIZATION_SEED_BYTES * Spec.FLOOR_PER_BYTE
    data = scaffold_data(fork, execution_headroom=auth_floor + 60_000)
    delegate = pre.deploy_contract(code=Op.STOP)
    authority = pre.fund_eoa()
    block = Block(
        txs=[
            Transaction(
                sender=pre.fund_eoa(),
                to=pre.deploy_contract(code=Op.STOP),
                data=data,
                authorization_list=[
                    AuthorizationTuple(
                        address=delegate, nonce=0, signer=authority
                    )
                ],
            )
        ],
        header_verify=Header(
            gas_used=fork.transaction_data_floor_cost_calculator()(data=data)
            + auth_floor
        ),
        expected_block_access_list=BlockAccessListExpectation(
            account_expectations={
                authority: BalAccountExpectation(
                    nonce_changes=[
                        BalNonceChange(block_access_index=1, post_nonce=1)
                    ],
                    code_changes=[
                        BalCodeChange(
                            block_access_index=1,
                            new_code=Spec7702.delegation_designation(delegate),
                        )
                    ],
                ),
            }
        ),
    )
    blockchain_test(pre=pre, blocks=[block], post={})
