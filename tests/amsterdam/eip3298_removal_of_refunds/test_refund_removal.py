"""
Tests for [EIP-3298: Removal of refunds](https://eips.ethereum.org/EIPS/eip-3298).

The storage-clearing refund and the EIP-3529 quotient cap are removed;
the EIP-8038 net-metered ``STORAGE_WRITE`` reversal survives and is now
applied in full. Block-level accounting stays pre-refund (EIP-7778).
"""

import pytest
from execution_testing import (
    Account,
    Alloc,
    Bytecode,
    Fork,
    Header,
    Op,
    StateTestFiller,
    Transaction,
    TransactionReceipt,
)
from execution_testing.checklists import EIPChecklist

from .spec import ref_spec_3298

REFERENCE_SPEC_GIT_PATH = ref_spec_3298.git_path
REFERENCE_SPEC_VERSION = ref_spec_3298.version

pytestmark = pytest.mark.valid_from("EIP3298")


def _write_reversal(slot: int, warm: bool = False) -> Bytecode:
    """Change a non-zero-original slot and restore it."""
    return Op.SSTORE.with_metadata(
        key_warm=warm,
        original_value=1,
        current_value=1,
        new_value=2,
    )(slot, 2) + Op.SSTORE.with_metadata(
        key_warm=True,
        original_value=1,
        current_value=2,
        new_value=1,
    )(slot, 1)


def _gross_gas(code: Bytecode, fork: Fork, data: bytes = b"") -> int:
    """Return the pre-refund gas of a transaction executing ``code``."""
    intrinsic = fork.transaction_intrinsic_cost_calculator()(
        calldata=data,
        return_cost_deducted_prior_execution=True,
    )
    return intrinsic + code.execution_cost(fork) + code.state_cost(fork)


def _expected_cumulative(code: Bytecode, fork: Fork, data: bytes = b"") -> int:
    """
    Return the receipt ``cumulative_gas_used`` under EIP-3298.

    The refund applies in full (no EIP-3529 quotient cap); the EIP-7623
    calldata floor still applies after refunds.
    """
    gross = _gross_gas(code, fork, data)
    floor = fork.transaction_data_floor_cost_calculator()(data=data)
    return max(gross - code.refund(fork), floor)


@EIPChecklist.GasRefundsChanges.Test.RefundCalculation()
@EIPChecklist.GasRefundsChanges.Test.RefundCalculation.Over()
def test_clear_grants_no_refund(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """
    Clearing a non-zero-original slot grants no refund.

    The storage-clearing refund is removed from the gas schedule, so the
    receipt reports the gross gas in full.
    """
    code = Op.SSTORE.with_metadata(
        key_warm=False,
        original_value=1,
        current_value=1,
        new_value=0,
    )(0, 0)
    contract = pre.deploy_contract(code=code, storage={0: 1})

    assert code.refund(fork) == 0
    expected_cumulative = _expected_cumulative(code, fork)
    assert expected_cumulative == _gross_gas(code, fork)

    tx = Transaction(
        to=contract,
        sender=pre.fund_eoa(),
        expected_receipt=TransactionReceipt(
            cumulative_gas_used=expected_cumulative
        ),
    )

    post = {contract: Account(storage={0: 0})}
    state_test(pre=pre, post=post, tx=tx)


@EIPChecklist.GasRefundsChanges.Test.RefundCalculation()
@EIPChecklist.GasRefundsChanges.Test.RefundCalculation.Under()
def test_write_reversal_survives_uncapped(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """
    Restoring a changed slot still refunds ``STORAGE_WRITE``, in full.

    No filler gas is burned, so the refund exceeds one fifth of the
    gross gas: the removed EIP-3529 cap would have bound here, and the
    receipt observably reflects the full reversal instead.
    """
    code = _write_reversal(0)
    contract = pre.deploy_contract(code=code, storage={0: 1})

    reversal = code.refund(fork)
    assert reversal > 0
    gross = _gross_gas(code, fork)
    # The struck cap would have bound: the full refund is observable
    # only because EIP-3298 removed it.
    assert reversal > gross // 5
    expected_cumulative = _expected_cumulative(code, fork)
    assert expected_cumulative == gross - reversal

    tx = Transaction(
        to=contract,
        sender=pre.fund_eoa(),
        expected_receipt=TransactionReceipt(
            cumulative_gas_used=expected_cumulative
        ),
    )

    post = {contract: Account(storage={0: 1})}
    state_test(pre=pre, post=post, tx=tx)


@EIPChecklist.GasRefundsChanges.Test.RefundCalculation()
@EIPChecklist.GasRefundsChanges.Test.RefundCalculation.Under()
@pytest.mark.parametrize("num_slots", [8, 32])
def test_refund_uncapped_many_reversals(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    num_slots: int,
) -> None:
    """
    Accumulated reversals apply in full with no quotient cap.

    Each of ``num_slots`` non-zero-original slots is changed and
    restored, accruing one ``STORAGE_WRITE`` reversal per slot; the
    accrued refund far exceeds the struck ``gas_used // 5`` cap.
    """
    code = Bytecode()
    for slot in range(num_slots):
        code += _write_reversal(slot)

    contract = pre.deploy_contract(
        code=code,
        storage=dict.fromkeys(range(num_slots), 1),
    )

    accrued = code.refund(fork)
    gross = _gross_gas(code, fork)
    assert accrued > gross // 5
    expected_cumulative = _expected_cumulative(code, fork)
    assert expected_cumulative == gross - accrued

    tx = Transaction(
        to=contract,
        sender=pre.fund_eoa(),
        expected_receipt=TransactionReceipt(
            cumulative_gas_used=expected_cumulative
        ),
    )

    post = {contract: Account(storage=dict.fromkeys(range(num_slots), 1))}
    state_test(pre=pre, post=post, tx=tx)


@EIPChecklist.GasRefundsChanges.Test.RefundCalculation()
def test_clear_and_restore_refunds_write_only(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """
    Clearing then restoring a non-zero-original slot refunds only the
    write reversal.

    Both struck schedule entries participate in this round trip under
    EIP-8038 (the clear grant and its restoration reversal); with both
    removed, the surviving ``STORAGE_WRITE`` reversal alone remains.
    """
    code = Op.SSTORE.with_metadata(
        key_warm=False,
        original_value=1,
        current_value=1,
        new_value=0,
    )(0, 0) + Op.SSTORE.with_metadata(
        key_warm=True,
        original_value=1,
        current_value=0,
        new_value=1,
    )(0, 1)
    contract = pre.deploy_contract(code=code, storage={0: 1})

    reversal = _write_reversal(0).refund(fork)
    assert code.refund(fork) == reversal
    expected_cumulative = _expected_cumulative(code, fork)

    tx = Transaction(
        to=contract,
        sender=pre.fund_eoa(),
        expected_receipt=TransactionReceipt(
            cumulative_gas_used=expected_cumulative
        ),
    )

    post = {contract: Account(storage={0: 1})}
    state_test(pre=pre, post=post, tx=tx)


@EIPChecklist.GasRefundsChanges.Test.RefundCalculation()
def test_floor_applies_after_uncapped_refund(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """
    The calldata floor still binds after the refund is applied in full.

    A data-carrying transaction accrues write reversals that drive the
    post-refund usage below the EIP-7623 floor; the receipt reports the
    floor.
    """
    code = _write_reversal(0) + _write_reversal(1)
    contract = pre.deploy_contract(code=code, storage={0: 1, 1: 1})

    # Search for a data size that places the floor inside the
    # refund-wide window between the post-refund usage and the gross
    # gas. The floor grows faster per byte than the intrinsic data
    # cost, so the window is crossed within the bounded range; the
    # 25-byte step is far finer than the two-reversal window width.
    refund = code.refund(fork)
    floor_calc = fork.transaction_data_floor_cost_calculator()
    for size in range(0, 20_000, 25):
        data = b"\x00" * size
        gross = _gross_gas(code, fork, data)
        floor = floor_calc(data=data)
        if gross - refund < floor < gross:
            break
    else:
        raise AssertionError("no data size lands the floor in the window")

    tx = Transaction(
        to=contract,
        data=data,
        sender=pre.fund_eoa(),
        expected_receipt=TransactionReceipt(cumulative_gas_used=floor),
    )

    post = {contract: Account(storage={0: 1, 1: 1})}
    state_test(pre=pre, post=post, tx=tx)


@EIPChecklist.GasRefundsChanges.Test.RefundCalculation()
def test_block_gas_ignores_refunds(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """
    Block-level accounting stays pre-refund (EIP-7778 unchanged).

    The receipt reflects the fully applied reversal while the block
    header ``gas_used`` reports the pre-refund execution gas; the two
    observables diverge by exactly the refund.
    """
    code = _write_reversal(0)
    contract = pre.deploy_contract(code=code, storage={0: 1})

    gross = _gross_gas(code, fork)
    expected_cumulative = _expected_cumulative(code, fork)
    assert gross - expected_cumulative == code.refund(fork)

    tx = Transaction(
        to=contract,
        sender=pre.fund_eoa(),
        expected_receipt=TransactionReceipt(
            cumulative_gas_used=expected_cumulative
        ),
    )

    post = {contract: Account(storage={0: 1})}
    state_test(
        pre=pre,
        post=post,
        tx=tx,
        blockchain_test_header_verify=Header(gas_used=gross),
    )


@EIPChecklist.GasRefundsChanges.Test.RefundCalculation()
def test_reverted_frame_discards_reversal(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """
    A reverting frame's refund additions are discarded (unchanged
    journaling semantics).

    The callee accrues a write reversal and reverts; the receipt shows
    no refund applied.
    """
    callee_code = _write_reversal(0) + Op.REVERT(0, 0)
    callee = pre.deploy_contract(code=callee_code, storage={0: 1})

    caller_code = Op.POP(Op.CALL(address=callee, address_warm=False))
    caller = pre.deploy_contract(code=caller_code)

    intrinsic = fork.transaction_intrinsic_cost_calculator()(
        return_cost_deducted_prior_execution=True
    )
    gross = (
        intrinsic
        + caller_code.gas_cost(fork)
        + callee_code.execution_cost(fork)
    )

    tx = Transaction(
        to=caller,
        sender=pre.fund_eoa(),
        expected_receipt=TransactionReceipt(cumulative_gas_used=gross),
    )

    post = {callee: Account(storage={0: 1})}
    state_test(pre=pre, post=post, tx=tx)
