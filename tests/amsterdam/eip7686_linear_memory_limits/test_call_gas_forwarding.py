"""Sub-call gas grants shrink with the caller's memory footprint."""

import pytest
from execution_testing import (
    Account,
    Alloc,
    Bytecode,
    Fork,
    Op,
    Opcodes,
    StateTestFiller,
    Storage,
    Transaction,
    compute_create2_address,
    compute_create_address,
)

from .spec import Spec, ref_spec_7686

REFERENCE_SPEC_GIT_PATH = ref_spec_7686.git_path
REFERENCE_SPEC_VERSION = ref_spec_7686.version

# More gas than any sub-call can be given, so the forwarded amount is
# always decided by `max_call_gas`.
ALL_AVAILABLE_GAS = 2**30

EXECUTED = 1


def intrinsic_cost(fork: Fork) -> int:
    """Return the execution intrinsic cost of a plain call."""
    return fork.transaction_intrinsic_cost_calculator()(
        return_cost_deducted_prior_execution=True
    )


def gas_reporting_code() -> Bytecode:
    """
    Return code that returns the gas it started with.

    `GAS` runs first, so the reported value is the frame's gas grant
    minus the `GAS` opcode's own cost.
    """
    return Op.GAS + Op.PUSH0 + Op.MSTORE + Op.RETURN(0, 0x20)


@pytest.mark.valid_from("EIP7686")
@pytest.mark.with_all_call_opcodes
@pytest.mark.parametrize(
    "memory_size,tx_gas_headroom",
    [
        pytest.param(0, None, id="no_memory_64th_rule"),
        pytest.param(8_192, None, id="small_memory_64th_rule"),
        pytest.param(65_536, None, id="large_memory_dominates"),
        # A grant barely above the memory size: after paying for the
        # expansion the remaining gas is below the memory size, so
        # the sub-call grant clamps to zero.
        pytest.param(320_000, 25_000, id="memory_exceeds_remaining_gas"),
    ],
)
def test_call_gas_forwarding(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    call_opcode: Opcodes,
    memory_size: int,
    tx_gas_headroom: int | None,
) -> None:
    """
    A caller keeps the larger of one 64th of its remaining gas and
    one gas per byte of its memory. The child reports the gas it
    received; the caller stores the report.
    """
    child = pre.deploy_contract(code=gas_reporting_code())

    if memory_size > 0:
        mem_prefix = Op.MSTORE8(
            offset=memory_size - 1, value=1, new_memory_size=memory_size
        )
        call = call_opcode(gas=ALL_AVAILABLE_GAS, address=child, ret_size=0x20)
        memory_after_call = memory_size
    else:
        mem_prefix = Bytecode()
        # The return region is the only memory the call touches.
        call = call_opcode(
            gas=ALL_AVAILABLE_GAS,
            address=child,
            ret_size=0x20,
            new_memory_size=0x20,
        )
        memory_after_call = 0x20

    if tx_gas_headroom is None:
        tx_gas_limit = 1_000_000
    else:
        tx_gas_limit = intrinsic_cost(fork) + memory_size + tx_gas_headroom
    grant = tx_gas_limit - intrinsic_cost(fork)

    available = grant - mem_prefix.gas_cost(fork) - call.gas_cost(fork)
    forwarded = min(
        ALL_AVAILABLE_GAS, Spec.max_call_gas(available, memory_after_call)
    )
    child_ran = forwarded > gas_reporting_code().gas_cost(fork)
    reported_gas = forwarded - Op.GAS().gas_cost(fork) if child_ran else 0

    storage = Storage()
    parent = pre.deploy_contract(
        code=mem_prefix
        + Op.SSTORE(storage.store_next(1 if child_ran else 0), call)
        + Op.SSTORE(storage.store_next(reported_gas), Op.MLOAD(0))
        + Op.SSTORE(storage.store_next(EXECUTED), EXECUTED),
    )

    tx = Transaction(
        sender=pre.fund_eoa(),
        to=parent,
        gas_limit=tx_gas_limit,
    )

    state_test(
        pre=pre,
        post={parent: Account(storage=storage)},
        tx=tx,
    )


@pytest.mark.valid_from("EIP7686")
@pytest.mark.parametrize(
    "opcode",
    [
        pytest.param(Op.CREATE, id="create"),
        pytest.param(Op.CREATE2, id="create2"),
    ],
)
@pytest.mark.parametrize(
    "memory_size",
    [
        pytest.param(128, id="small_memory_64th_rule"),
        pytest.param(131_072, id="large_memory_dominates"),
    ],
)
def test_create_gas_forwarding(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    opcode: Op,
    memory_size: int,
) -> None:
    """
    `CREATE*` grants follow the same rule as calls: the creator keeps
    the larger of one 64th of its remaining gas and one gas per byte
    of its memory. The init code stores the gas it received in the
    new account.
    """
    tx_gas_limit = 1_000_000

    # Init code that stores its frame's gas grant at slot zero of the
    # newly created account.
    init_code = Op.GAS + Op.PUSH0 + Op.SSTORE + Op.STOP
    init_code_bytes = bytes(init_code)
    init_code_word = int.from_bytes(init_code_bytes.ljust(32, b"\x00"), "big")

    mem_prefix = Op.MSTORE(
        offset=0, value=init_code_word, new_memory_size=32
    ) + Op.MSTORE8(
        offset=memory_size - 1,
        value=1,
        new_memory_size=memory_size,
        old_memory_size=32,
    )

    if opcode == Op.CREATE2:
        create = opcode(
            value=0,
            offset=0,
            size=len(init_code_bytes),
            salt=0,
            init_code_size=len(init_code_bytes),
        )
    else:
        create = opcode(
            value=0,
            offset=0,
            size=len(init_code_bytes),
            init_code_size=len(init_code_bytes),
        )

    grant = tx_gas_limit - intrinsic_cost(fork)
    available = grant - mem_prefix.gas_cost(fork) - create.gas_cost(fork)
    child_grant = Spec.max_call_gas(available, memory_size)

    parent = pre.deploy_contract(
        code=mem_prefix + Op.SSTORE(0, create) + Op.SSTORE(1, EXECUTED),
    )

    if opcode == Op.CREATE2:
        created = compute_create2_address(parent, 0, init_code_bytes)
    else:
        created = compute_create_address(address=parent, nonce=1)

    tx = Transaction(
        sender=pre.fund_eoa(),
        to=parent,
        gas_limit=tx_gas_limit,
    )

    state_test(
        pre=pre,
        post={
            parent: Account(storage={0: created, 1: EXECUTED}),
            created: Account(
                storage={0: child_grant - Op.GAS().gas_cost(fork)}
            ),
        },
        tx=tx,
    )
