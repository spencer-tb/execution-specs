"""
Tests for [EIP-8279: Block access list byte floor](https://eips.ethereum.org/EIPS/eip-8279).

Each byte a transaction adds to the block access list raises its floor
gas, extending the EIP-7623 calldata floor; a transaction settles at the
floor when it exceeds the execution gas actually spent. Calldata-heavy
scaffold transactions make the floor bind so the metered bytes become
visible in the receipt's gas used.
"""

import pytest
from execution_testing import (
    Account,
    Alloc,
    AuthorizationTuple,
    Fork,
    Op,
    StateTestFiller,
    Transaction,
    TransactionReceipt,
)

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


def test_typical_transfer_unaffected(
    state_test: StateTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    A plain value transfer settles at its intrinsic cost; the byte
    floor adds nothing for a transaction that publishes no access data.
    """
    tx = Transaction(
        sender=pre.fund_eoa(),
        to=pre.fund_eoa(amount=1),
        value=1,
        expected_receipt=TransactionReceipt(
            cumulative_gas_used=fork.transaction_intrinsic_cost_calculator()(
                calldata=b"", sends_value=True
            )
        ),
    )
    state_test(pre=pre, post={}, tx=tx)


def test_floor_binds_cold_storage_read(
    state_test: StateTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    A floor-bound transaction that reads one cold storage slot settles
    exactly one storage-key's bytes above the calldata floor.
    """
    data = scaffold_data(fork, execution_headroom=STORAGE_KEY_FLOOR + 5_000)
    tx = Transaction(
        sender=pre.fund_eoa(),
        to=pre.deploy_contract(code=Op.SLOAD(COLD_SLOT)),
        data=data,
        expected_receipt=TransactionReceipt(
            cumulative_gas_used=fork.transaction_data_floor_cost_calculator()(
                data=data
            )
            + STORAGE_KEY_FLOOR
        ),
    )
    state_test(pre=pre, post={}, tx=tx)


@pytest.mark.parametrize("restore", [True, False])
def test_storage_restore_returns_value_bytes(
    state_test: StateTestFiller, pre: Alloc, fork: Fork, restore: bool
) -> None:
    """
    Writing a slot away from its original value adds the value's bytes;
    restoring it within the same transaction returns them, leaving only
    the key's bytes on the floor.
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
    value_bytes_floor = 0 if restore else STORAGE_VALUE_FLOOR
    tx = Transaction(
        sender=pre.fund_eoa(),
        to=contract,
        data=data,
        expected_receipt=TransactionReceipt(
            cumulative_gas_used=fork.transaction_data_floor_cost_calculator()(
                data=data
            )
            + STORAGE_KEY_FLOOR
            + value_bytes_floor
        ),
    )
    state_test(pre=pre, post={contract: Account(storage={slot: final})}, tx=tx)


def test_floor_meter_aborts_execution(
    state_test: StateTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    An access whose bytes would push the floor past the gas limit aborts
    the frame out-of-gas before the access happens; the transaction
    consumes its whole gas limit and reverts.
    """
    canary_slot = 0xC
    data = scaffold_data(fork, execution_headroom=STORAGE_KEY_FLOOR + 5_000)
    contract = pre.deploy_contract(
        code=Op.SLOAD(COLD_SLOT) + Op.SSTORE(canary_slot, 1)
    )
    # Room for less than the slot key's bytes above the initial floor.
    gas_limit = (
        fork.transaction_data_floor_cost_calculator()(data=data)
        + STORAGE_KEY_FLOOR // 2
    )
    tx = Transaction(
        sender=pre.fund_eoa(),
        to=contract,
        data=data,
        gas_limit=gas_limit,
        expected_receipt=TransactionReceipt(cumulative_gas_used=gas_limit),
    )
    state_test(pre=pre, post={contract: Account(storage={})}, tx=tx)


def test_reverted_frame_keeps_metered_bytes(
    state_test: StateTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    Bytes metered inside a frame survive its revert: the reverted
    accesses stay in the block access list, so the child's cold address
    and slot key remain on the caller's floor.
    """
    data = scaffold_data(
        fork,
        execution_headroom=ADDRESS_FLOOR + STORAGE_KEY_FLOOR + 10_000,
    )
    child = pre.deploy_contract(code=Op.SLOAD(COLD_SLOT) + Op.REVERT(0, 0))
    caller = pre.deploy_contract(code=Op.POP(Op.CALL(address=child)))
    tx = Transaction(
        sender=pre.fund_eoa(),
        to=caller,
        data=data,
        expected_receipt=TransactionReceipt(
            cumulative_gas_used=fork.transaction_data_floor_cost_calculator()(
                data=data
            )
            + ADDRESS_FLOOR
            + STORAGE_KEY_FLOOR
        ),
    )
    state_test(pre=pre, post={}, tx=tx)


def test_setcode_authorization_floor_seed(
    state_test: StateTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    Each authorization seeds the floor with the authority's address,
    delegation code, and nonce bytes before execution begins.
    """
    auth_floor = Spec.AUTHORIZATION_SEED_BYTES * Spec.FLOOR_PER_BYTE
    # An existing authority: a nonexistent one adds account-creation
    # state gas far above any reasonable floor scaffold.
    data = scaffold_data(fork, execution_headroom=auth_floor + 60_000)
    tx = Transaction(
        sender=pre.fund_eoa(),
        to=pre.deploy_contract(code=Op.STOP),
        data=data,
        authorization_list=[
            AuthorizationTuple(
                address=pre.deploy_contract(code=Op.STOP),
                nonce=0,
                signer=pre.fund_eoa(),
            )
        ],
        expected_receipt=TransactionReceipt(
            cumulative_gas_used=fork.transaction_data_floor_cost_calculator()(
                data=data
            )
            + auth_floor
        ),
    )
    state_test(pre=pre, post={}, tx=tx)
