"""
Tests for the EIP-7971 transaction-global transient storage slot limit.

Covers the exact limit boundary, the transaction-global scope across
contracts, deallocation on frame revert, and the exceptional halt when
the limit is exceeded.
"""

import pytest
from execution_testing import (
    Account,
    Alloc,
    Bytecode,
    Fork,
    Op,
    StateTestFiller,
    Transaction,
    While,
)
from execution_testing.checklists import EIPChecklist

from .spec import ref_spec_7971

REFERENCE_SPEC_GIT_PATH = ref_spec_7971.git_path
REFERENCE_SPEC_VERSION = ref_spec_7971.version

pytestmark = pytest.mark.valid_from("EIP7971")

# Storage sentinel that halted executions must leave untouched.
HALT_CANARY = 0xC0DE


def write_transient_slots(count: int, zero_value: bool = False) -> Bytecode:
    """
    Write `count` unique transient slots with keys 0 to count - 1.

    The loop counter lives at memory offset 0 so the body and condition
    stay stack-neutral for `While`.
    """
    assert 0 < count <= 2**18, "unexpected slot count"
    value = Op.PUSH0 if zero_value else Op.MLOAD(0)
    return Op.MSTORE(0, 0) + While(
        body=(
            value
            + Op.MLOAD(0)
            + Op.TSTORE
            + Op.MSTORE(0, Op.ADD(Op.MLOAD(0), 1))
        ),
        condition=Op.GT(count, Op.MLOAD(0)),
    )


def read_transient_slots(count: int) -> Bytecode:
    """Read `count` distinct transient slots with keys 0 to count - 1."""
    assert 0 < count <= 2**18, "unexpected slot count"
    return Op.MSTORE(0, 0) + While(
        body=(
            Op.TLOAD(Op.MLOAD(0))
            + Op.POP
            + Op.MSTORE(0, Op.ADD(Op.MLOAD(0), 1))
        ),
        condition=Op.GT(count, Op.MLOAD(0)),
    )


@EIPChecklist.Opcode.Test.ExceptionalAbort()
@pytest.mark.parametrize(
    "extra_slots,zero_value",
    [
        pytest.param(0, False, id="exactly_max_slots"),
        pytest.param(1, False, id="one_above_max_slots"),
        pytest.param(0, True, id="exactly_max_slots_zero_values"),
        pytest.param(1, True, id="one_above_max_slots_zero_values"),
    ],
)
def test_slot_limit_boundary(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    extra_slots: int,
    zero_value: bool,
) -> None:
    """
    Writing exactly the slot limit succeeds and one slot more halts,
    whether the writes store values or zeros.
    """
    max_slots = fork.max_transient_storage_slots()
    assert max_slots is not None
    halts = extra_slots > 0
    contract = pre.deploy_contract(
        write_transient_slots(max_slots + extra_slots, zero_value)
        + Op.SSTORE(0, 1),
        storage={0: HALT_CANARY},
    )
    tx = Transaction(
        sender=pre.fund_eoa(),
        to=contract,
        gas_limit=fork.transaction_gas_limit_cap(),
    )
    post = {contract: Account(storage={0: HALT_CANARY if halts else 1})}
    state_test(pre=pre, post=post, tx=tx)


@EIPChecklist.Opcode.Test.ExceptionalAbort()
def test_repeated_writes_do_not_count_toward_limit(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """
    Rewriting an allocated slot does not consume limit capacity: repeat
    writes on top of exactly the limit of unique slots still succeed.
    """
    max_slots = fork.max_transient_storage_slots()
    assert max_slots is not None
    contract = pre.deploy_contract(
        Op.TSTORE(0, 1) * 3
        + write_transient_slots(max_slots)
        + Op.SSTORE(0, 1),
        storage={0: HALT_CANARY},
    )
    tx = Transaction(
        sender=pre.fund_eoa(),
        to=contract,
        gas_limit=fork.transaction_gas_limit_cap(),
    )
    post = {contract: Account(storage={0: 1})}
    state_test(pre=pre, post=post, tx=tx)


@EIPChecklist.Opcode.Test.ExceptionalAbort()
def test_reads_do_not_count_toward_limit(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """
    `TLOAD` does not allocate: reading more distinct unwritten slots
    than the limit leaves the full write capacity available.
    """
    max_slots = fork.max_transient_storage_slots()
    assert max_slots is not None
    contract = pre.deploy_contract(
        read_transient_slots(max_slots + 1)
        + Op.TSTORE(0, 1)
        + Op.SSTORE(0, 1),
        storage={0: HALT_CANARY},
    )
    tx = Transaction(
        sender=pre.fund_eoa(),
        to=contract,
        gas_limit=fork.transaction_gas_limit_cap(),
    )
    post = {contract: Account(storage={0: 1})}
    state_test(pre=pre, post=post, tx=tx)


@EIPChecklist.Opcode.Test.ExceptionalAbort()
@pytest.mark.parametrize(
    "exceed",
    [
        pytest.param(False, id="exactly_max_across_contracts"),
        pytest.param(True, id="one_above_max_in_callee"),
    ],
)
def test_limit_is_transaction_global(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    exceed: bool,
) -> None:
    """
    The limit counts slots across all contracts in the transaction, and
    exceeding it halts only the writing frame: the caller continues with
    the callee's allocations rolled back.
    """
    max_slots = fork.max_transient_storage_slots()
    assert max_slots is not None
    caller_slots = max_slots // 2
    callee_slots = max_slots - caller_slots + (1 if exceed else 0)
    callee = pre.deploy_contract(write_transient_slots(callee_slots))
    caller = pre.deploy_contract(
        write_transient_slots(caller_slots)
        + Op.SSTORE(0, Op.CALL(Op.GAS, callee, 0, 0, 0, 0, 0))
        + Op.TSTORE(0, 2)
        + Op.SSTORE(1, 1),
        storage={0: HALT_CANARY, 1: HALT_CANARY},
    )
    tx = Transaction(
        sender=pre.fund_eoa(),
        to=caller,
        gas_limit=fork.transaction_gas_limit_cap(),
    )
    post = {
        caller: Account(storage={0: 0 if exceed else 1, 1: 1}),
    }
    state_test(pre=pre, post=post, tx=tx)


@EIPChecklist.Opcode.Test.ExceptionalAbort()
@pytest.mark.parametrize("create_opcode", [Op.CREATE, Op.CREATE2])
@pytest.mark.parametrize(
    "exceed",
    [
        pytest.param(False, id="exactly_max_across_create"),
        pytest.param(True, id="one_above_max_in_initcode"),
    ],
)
def test_limit_is_shared_with_contract_creation(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    create_opcode: Op,
    exceed: bool,
) -> None:
    """CREATE and CREATE2 initcode share the transaction's slot limit."""
    max_slots = fork.max_transient_storage_slots()
    assert max_slots is not None
    factory_slots = max_slots // 2
    initcode_slots = max_slots - factory_slots + (1 if exceed else 0)
    initcode = write_transient_slots(initcode_slots)
    create = (
        Op.CREATE2(0, 0, len(initcode), 0)
        if create_opcode == Op.CREATE2
        else Op.CREATE(0, 0, len(initcode))
    )
    factory = pre.deploy_contract(
        write_transient_slots(factory_slots)
        + Op.CALLDATACOPY(0, 0, Op.CALLDATASIZE)
        + Op.SSTORE(0, Op.ISZERO(Op.ISZERO(create)))
        + Op.SSTORE(1, 1),
        storage={0: HALT_CANARY, 1: HALT_CANARY},
    )
    tx = Transaction(
        sender=pre.fund_eoa(),
        to=factory,
        data=bytes(initcode),
        gas_limit=fork.transaction_gas_limit_cap(),
    )
    post = {
        factory: Account(storage={0: 0 if exceed else 1, 1: 1}),
    }
    state_test(pre=pre, post=post, tx=tx)


@EIPChecklist.Opcode.Test.ExceptionalAbort()
@pytest.mark.parametrize(
    "callee_reverts",
    [
        pytest.param(True, id="reverted_slots_deallocated"),
        pytest.param(False, id="committed_slots_still_count"),
    ],
)
def test_subcall_revert_deallocates_slots(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    callee_reverts: bool,
) -> None:
    """
    Slots written by a reverted frame do not count toward the limit,
    while slots written by a frame that returns normally still do.
    """
    max_slots = fork.max_transient_storage_slots()
    assert max_slots is not None
    callee_slots = 3
    callee_code = write_transient_slots(callee_slots)
    if callee_reverts:
        callee_code += Op.REVERT(0, 0)
    callee = pre.deploy_contract(callee_code)
    caller = pre.deploy_contract(
        Op.SSTORE(0, Op.CALL(Op.GAS, callee, 0, 0, 0, 0, 0))
        + write_transient_slots(max_slots)
        + Op.SSTORE(1, 1),
        storage={0: HALT_CANARY, 1: HALT_CANARY},
    )
    tx = Transaction(
        sender=pre.fund_eoa(),
        to=caller,
        gas_limit=fork.transaction_gas_limit_cap(),
    )
    if callee_reverts:
        # The callee's writes were rolled back, so the caller's writes
        # end at exactly the limit and the transaction completes.
        storage = {0: 0, 1: 1}
    else:
        # The callee's writes persist, the caller's loop exceeds the
        # limit and halts, leaving the whole transaction unapplied.
        storage = {0: HALT_CANARY, 1: HALT_CANARY}
    post = {caller: Account(storage=storage)}
    state_test(pre=pre, post=post, tx=tx)
