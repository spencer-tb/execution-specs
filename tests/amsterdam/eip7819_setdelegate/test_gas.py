"""
Gas tests for [EIP-7819: SETDELEGATE instruction](https://eips.ethereum.org/EIPS/eip-7819).

SETDELEGATE uses the EIP-8037/8038 components: the access cost of the
written address, `ACCOUNT_WRITE` per invocation, `NEW_ACCOUNT` state gas
when the leaf does not exist, and net-metered `AUTH_BASE` state gas for
a designation created relative to transaction-start state.
"""

import pytest
from execution_testing import (
    AccessList,
    Account,
    Alloc,
    Fork,
    Op,
    StateTestFiller,
    Transaction,
    TransactionReceipt,
    compute_setdelegate_address,
)
from execution_testing.checklists import EIPChecklist

from .spec import Spec, ref_spec_7819

REFERENCE_SPEC_GIT_PATH = ref_spec_7819.git_path
REFERENCE_SPEC_VERSION = ref_spec_7819.version

pytestmark = pytest.mark.valid_from("EIP7819")

SALT = 0xC0FFEE


@EIPChecklist.Opcode.Test.GasUsage.Normal()
@pytest.mark.pre_alloc_mutable
@pytest.mark.parametrize(
    "location_pre",
    [
        pytest.param("nonexistent", id="nonexistent"),
        pytest.param("funded_eoa", id="funded_eoa"),
        pytest.param("existing_designation", id="existing_designation"),
    ],
)
def test_gas_single_write(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    location_pre: str,
) -> None:
    """
    A single SETDELEGATE pays for exactly the state it creates: an
    existing leaf skips `NEW_ACCOUNT` and an existing designation
    skips `AUTH_BASE`.
    """
    target = pre.fund_eoa(amount=0)
    account_new = location_pre == "nonexistent"
    designation_new = location_pre != "existing_designation"
    code = Op.POP(
        Op.SETDELEGATE(
            SALT,
            target,
            account_new=account_new,
            designation_new=designation_new,
        )
    )
    factory = pre.deploy_contract(code=code)
    location = compute_setdelegate_address(factory, SALT)

    expected_nonce = 1
    if location_pre == "funded_eoa":
        pre.fund_address(location, 1)
    elif location_pre == "existing_designation":
        old_target = pre.fund_eoa(amount=0)
        pre.deploy_contract(
            code=Spec.delegation_designation(old_target),
            address=location,
            nonce=2,
        )
        expected_nonce = 2

    intrinsic = fork.transaction_intrinsic_cost_calculator()()
    expected_gas_used = intrinsic + code.gas_cost(fork)

    tx = Transaction(
        to=factory,
        sender=pre.fund_eoa(),
        state_gas_reservoir=0,
        expected_receipt=TransactionReceipt(
            cumulative_gas_used=expected_gas_used,
        ),
    )

    post = {
        location: Account(
            code=Spec.delegation_designation(target),
            nonce=expected_nonce,
        ),
    }
    state_test(pre=pre, post=post, tx=tx)


@EIPChecklist.Opcode.Test.GasUsage.Normal()
def test_gas_repeat_same_salt(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """
    A second SETDELEGATE on the same salt pays warm access and another
    `ACCOUNT_WRITE`, but no additional leaf or designation state gas.
    """
    first_target = pre.fund_eoa(amount=0)
    second_target = pre.fund_eoa(amount=0)
    code = Op.POP(Op.SETDELEGATE(SALT, first_target)) + Op.POP(
        Op.SETDELEGATE(
            SALT,
            second_target,
            address_warm=True,
            account_new=False,
            designation_new=False,
        )
    )
    factory = pre.deploy_contract(code=code)
    location = compute_setdelegate_address(factory, SALT)

    intrinsic = fork.transaction_intrinsic_cost_calculator()()
    expected_gas_used = intrinsic + code.gas_cost(fork)

    tx = Transaction(
        to=factory,
        sender=pre.fund_eoa(),
        state_gas_reservoir=0,
        expected_receipt=TransactionReceipt(
            cumulative_gas_used=expected_gas_used,
        ),
    )

    post = {
        location: Account(
            code=Spec.delegation_designation(second_target),
            nonce=1,
        ),
    }
    state_test(pre=pre, post=post, tx=tx)


@EIPChecklist.Opcode.Test.GasUsage.Normal()
def test_gas_set_clear_set(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """
    Clearing a designation created in the same transaction refills its
    state gas. Setting it again charges the state gas again, so the net
    transaction charge describes the designation that remains.
    """
    target = pre.fund_eoa(amount=0)
    code = (
        Op.POP(Op.SETDELEGATE(SALT, target))
        + Op.POP(
            Op.SETDELEGATE(
                SALT,
                0,
                address_warm=True,
                account_new=False,
                designation_new=False,
                designation_cleared=True,
            )
        )
        + Op.POP(
            Op.SETDELEGATE(
                SALT,
                target,
                address_warm=True,
                account_new=False,
            )
        )
    )
    factory = pre.deploy_contract(code=code)
    location = compute_setdelegate_address(factory, SALT)

    intrinsic = fork.transaction_intrinsic_cost_calculator()()
    expected_gas_used = (
        intrinsic + code.gas_cost(fork) - code.state_refund(fork)
    )

    tx = Transaction(
        to=factory,
        sender=pre.fund_eoa(),
        state_gas_reservoir=0,
        expected_receipt=TransactionReceipt(
            cumulative_gas_used=expected_gas_used,
        ),
    )

    post = {
        location: Account(
            code=Spec.delegation_designation(target),
            nonce=1,
        ),
    }
    state_test(pre=pre, post=post, tx=tx)


@EIPChecklist.Opcode.Test.GasUsage.Normal()
def test_gas_reverted_set_then_set(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """
    A reverted child SETDELEGATE refills its state gas. A later write to
    the same location pays both `ACCOUNT_WRITE` and designation state
    gas again, because neither exception is transaction-scoped for an
    opcode-level write.
    """
    target = pre.fund_eoa(amount=0)
    child_code = Op.POP(Op.SETDELEGATE(SALT, target)) + Op.REVERT(0, 0)
    writer = pre.deploy_contract(code=child_code)
    parent_code = Op.POP(Op.DELEGATECALL(address=writer)) + Op.POP(
        Op.SETDELEGATE(SALT, target)
    )
    factory = pre.deploy_contract(code=parent_code)
    location = compute_setdelegate_address(factory, SALT)

    intrinsic = fork.transaction_intrinsic_cost_calculator()()
    expected_gas_used = (
        intrinsic
        + parent_code.gas_cost(fork)
        + child_code.execution_cost(fork)
    )

    tx = Transaction(
        to=factory,
        sender=pre.fund_eoa(),
        state_gas_reservoir=0,
        expected_receipt=TransactionReceipt(
            cumulative_gas_used=expected_gas_used,
        ),
    )

    post = {
        location: Account(
            code=Spec.delegation_designation(target),
            nonce=1,
        ),
    }
    state_test(pre=pre, post=post, tx=tx)


@EIPChecklist.Opcode.Test.GasUsage.Normal()
def test_gas_clear_on_fresh_account(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """
    Clearing at a nonexistent address still creates the account leaf,
    so `NEW_ACCOUNT` is charged but no designation state gas is.
    """
    code = Op.POP(Op.SETDELEGATE(SALT, 0, designation_new=False))
    factory = pre.deploy_contract(code=code)
    location = compute_setdelegate_address(factory, SALT)

    intrinsic = fork.transaction_intrinsic_cost_calculator()()
    expected_gas_used = intrinsic + code.gas_cost(fork)

    tx = Transaction(
        to=factory,
        sender=pre.fund_eoa(),
        state_gas_reservoir=0,
        expected_receipt=TransactionReceipt(
            cumulative_gas_used=expected_gas_used,
        ),
    )

    post = {location: Account(code=b"", nonce=1)}
    state_test(pre=pre, post=post, tx=tx)


@EIPChecklist.Opcode.Test.GasUsage.Normal()
def test_gas_access_list_warm_location(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """
    A location warmed by the transaction access list pays the warm
    access cost.
    """
    target = pre.fund_eoa(amount=0)
    code = Op.POP(Op.SETDELEGATE(SALT, target, address_warm=True))
    factory = pre.deploy_contract(code=code)
    location = compute_setdelegate_address(factory, SALT)

    access_list = [AccessList(address=location, storage_keys=[])]
    intrinsic = fork.transaction_intrinsic_cost_calculator()(
        access_list=access_list
    )
    expected_gas_used = intrinsic + code.gas_cost(fork)

    tx = Transaction(
        to=factory,
        sender=pre.fund_eoa(),
        access_list=access_list,
        state_gas_reservoir=0,
        expected_receipt=TransactionReceipt(
            cumulative_gas_used=expected_gas_used,
        ),
    )

    post = {
        location: Account(code=Spec.delegation_designation(target), nonce=1),
    }
    state_test(pre=pre, post=post, tx=tx)


@EIPChecklist.Opcode.Test.GasUsage.OutOfGasExecution()
@pytest.mark.parametrize(
    "extra_gas,succeeds",
    [
        pytest.param(0, True, id="exact"),
        pytest.param(-1, False, id="exact_minus_one"),
    ],
)
def test_gas_exact_boundary(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    extra_gas: int,
    succeeds: bool,
) -> None:
    """
    The transaction succeeds with exactly enough gas for the write and
    exceptionally halts with one unit less, leaving no designation.
    """
    target = pre.fund_eoa(amount=0)
    code = Op.POP(Op.SETDELEGATE(SALT, target))
    factory = pre.deploy_contract(code=code)
    location = compute_setdelegate_address(factory, SALT)

    intrinsic = fork.transaction_intrinsic_cost_calculator()()
    gas_limit = intrinsic + code.gas_cost(fork) + extra_gas

    tx = Transaction(
        to=factory,
        sender=pre.fund_eoa(),
        gas_limit=gas_limit,
        state_gas_reservoir=0,
        expected_receipt=TransactionReceipt(
            cumulative_gas_used=gas_limit,
        ),
    )

    post: dict = {location: Account.NONEXISTENT}
    if succeeds:
        post = {
            location: Account(
                code=Spec.delegation_designation(target), nonce=1
            ),
        }
    state_test(pre=pre, post=post, tx=tx)
