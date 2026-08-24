"""
Tests for the EIP-7971 transient storage repricing.

Covers the constant costs of `TLOAD` and `TSTORE`, the allocation
surcharge on the first write to a slot in a transaction, and the
`(address, key)` scope of slot allocations across frames.
"""

import pytest
from execution_testing import (
    Account,
    Alloc,
    Block,
    BlockchainTestFiller,
    Bytecode,
    CodeGasMeasure,
    Conditional,
    Fork,
    Op,
    StateTestFiller,
    Storage,
    Transaction,
)
from execution_testing.checklists import EIPChecklist

from .spec import ref_spec_7971

REFERENCE_SPEC_GIT_PATH = ref_spec_7971.git_path
REFERENCE_SPEC_VERSION = ref_spec_7971.version

pytestmark = pytest.mark.valid_from("EIP7971")


def measure(code: Bytecode, fork: Fork) -> CodeGasMeasure:
    """
    Measure the runtime gas of a bare `TSTORE` write, netting out the
    argument pushes of `code`.

    The push overhead is the difference between the sequence cost and
    the bare opcode's own map cost.
    """
    return CodeGasMeasure(
        code=code,
        overhead_cost=code.gas_cost(fork) - Op.TSTORE.gas_cost(fork),
    )


@EIPChecklist.GasCostChanges.Test.GasUpdatesMeasurement()
@pytest.mark.parametrize(
    "slot_written",
    [
        pytest.param(False, id="unwritten_slot"),
        pytest.param(True, id="written_slot"),
    ],
)
def test_tload_gas(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    slot_written: bool,
) -> None:
    """`TLOAD` costs the same whether or not the slot was written."""
    gas_costs = fork.gas_costs()
    setup = Op.TSTORE(1, 1) if slot_written else Bytecode()
    load = CodeGasMeasure(
        code=Op.TLOAD(1),
        overhead_cost=Op.TLOAD(1).gas_cost(fork) - gas_costs.OPCODE_TLOAD,
        extra_stack_items=1,
    )
    contract = pre.deploy_contract(setup + load)
    tx = Transaction(sender=pre.fund_eoa(), to=contract)
    post = {contract: Account(storage={0: gas_costs.OPCODE_TLOAD})}
    state_test(pre=pre, post=post, tx=tx)


@EIPChecklist.GasCostChanges.Test.GasUpdatesMeasurement()
@pytest.mark.parametrize(
    "setup,store_value,expects_allocation",
    [
        pytest.param(Bytecode(), 1, True, id="fresh_slot"),
        pytest.param(Bytecode(), 0, True, id="fresh_slot_zero_value"),
        pytest.param(Op.TSTORE(2, 1), 2, False, id="repeat_write"),
        pytest.param(Op.TSTORE(2, 0), 1, False, id="write_after_zero_write"),
        pytest.param(Op.TSTORE(1, 1), 1, True, id="only_other_slot_written"),
    ],
)
def test_tstore_gas(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    setup: Bytecode,
    store_value: int,
    expects_allocation: bool,
) -> None:
    """
    `TSTORE` pays the allocation surcharge exactly on the first write to
    a slot in the transaction, including a write that stores zero.
    """
    gas_costs = fork.gas_costs()
    store = measure(Op.TSTORE(2, store_value), fork)
    contract = pre.deploy_contract(setup + store)
    tx = Transaction(sender=pre.fund_eoa(), to=contract)
    expected = gas_costs.OPCODE_TSTORE
    if expects_allocation:
        expected += gas_costs.OPCODE_TSTORE_ALLOCATE
    post = {contract: Account(storage={0: expected})}
    state_test(pre=pre, post=post, tx=tx)


@EIPChecklist.GasCostChanges.Test.GasUpdatesMeasurement()
def test_tstore_allocation_scoped_per_address(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """
    A slot is unique per `(address, key)`: a callee's first write to a
    key already written by the caller still pays the allocation cost.
    """
    gas_costs = fork.gas_costs()
    store = measure(Op.TSTORE(1, 1), fork)
    callee = pre.deploy_contract(store)
    caller_storage = Storage()
    caller = pre.deploy_contract(
        Op.TSTORE(1, 1)
        + Op.SSTORE(
            caller_storage.store_next(1),
            Op.CALL(Op.GAS, callee, 0, 0, 0, 0, 0),
        )
    )
    tx = Transaction(sender=pre.fund_eoa(), to=caller)
    expected = gas_costs.OPCODE_TSTORE + gas_costs.OPCODE_TSTORE_ALLOCATE
    post = {
        callee: Account(storage={0: expected}),
        caller: Account(storage=caller_storage),
    }
    state_test(pre=pre, post=post, tx=tx)


@EIPChecklist.GasCostChanges.Test.GasUpdatesMeasurement()
@pytest.mark.parametrize(
    "first_call_reverts",
    [
        pytest.param(True, id="reverted_write"),
        pytest.param(False, id="committed_write"),
    ],
)
def test_allocation_after_subcall(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    first_call_reverts: bool,
) -> None:
    """
    A reverted frame deallocates the slots it wrote, so a later write to
    the slot pays the allocation cost again; a committed write does not.
    """
    gas_costs = fork.gas_costs()
    write = Op.TSTORE(1, 1)
    if first_call_reverts:
        write += Op.REVERT(0, 0)
    callee = pre.deploy_contract(
        Conditional(
            condition=Op.CALLDATALOAD(0),
            if_true=measure(Op.TSTORE(1, 1), fork),
            if_false=write,
        )
    )
    caller_storage = Storage()
    caller = pre.deploy_contract(
        Op.MSTORE(0, 0)
        + Op.SSTORE(
            caller_storage.store_next(0 if first_call_reverts else 1),
            Op.CALL(Op.GAS, callee, 0, 0, 32, 0, 0),
        )
        + Op.MSTORE(0, 1)
        + Op.SSTORE(
            caller_storage.store_next(1),
            Op.CALL(Op.GAS, callee, 0, 0, 32, 0, 0),
        )
    )
    tx = Transaction(sender=pre.fund_eoa(), to=caller)
    expected = gas_costs.OPCODE_TSTORE
    if first_call_reverts:
        expected += gas_costs.OPCODE_TSTORE_ALLOCATE
    post = {
        callee: Account(storage={0: expected}),
        caller: Account(storage=caller_storage),
    }
    state_test(pre=pre, post=post, tx=tx)


@EIPChecklist.GasCostChanges.Test.GasUpdatesMeasurement()
def test_allocation_resets_between_transactions(
    blockchain_test: BlockchainTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """The first write in each transaction pays the allocation cost."""
    gas_costs = fork.gas_costs()
    contract = pre.deploy_contract(measure(Op.TSTORE(1, 1), fork))
    sender = pre.fund_eoa()
    txs = [
        Transaction(sender=sender, to=contract, nonce=0),
        Transaction(sender=sender, to=contract, nonce=1),
    ]
    expected = gas_costs.OPCODE_TSTORE + gas_costs.OPCODE_TSTORE_ALLOCATE
    blockchain_test(
        pre=pre,
        post={contract: Account(storage={0: expected})},
        blocks=[Block(txs=txs)],
    )


@EIPChecklist.GasCostChanges.Test.OutOfGas()
@EIPChecklist.Opcode.Test.GasUsage.OutOfGasExecution()
@pytest.mark.parametrize(
    "gas_delta,call_succeeds",
    [
        pytest.param(-1, False, id="one_below_cost"),
        pytest.param(0, True, id="exact_cost"),
    ],
)
def test_tstore_out_of_gas(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    gas_delta: int,
    call_succeeds: bool,
) -> None:
    """
    A first write halts out of gas one unit below the combined write and
    allocation cost, and succeeds at exactly that cost.
    """
    store = Op.TSTORE(0, 1)
    callee = pre.deploy_contract(store)
    # The opcode gas map prices a bare `TSTORE` as a first write, which
    # is exactly what the callee executes.
    callee_cost = store.gas_cost(fork)
    caller_storage = Storage()
    caller = pre.deploy_contract(
        Op.SSTORE(
            caller_storage.store_next(1 if call_succeeds else 0),
            Op.CALL(callee_cost + gas_delta, callee, 0, 0, 0, 0, 0),
        )
    )
    tx = Transaction(sender=pre.fund_eoa(), to=caller)
    post = {caller: Account(storage=caller_storage)}
    state_test(pre=pre, post=post, tx=tx)
