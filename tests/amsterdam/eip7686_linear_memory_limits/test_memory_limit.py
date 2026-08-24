"""A frame's memory is capped at one byte per gas of its grant."""

import pytest
from execution_testing import (
    Account,
    Alloc,
    Fork,
    Op,
    StateTestFiller,
    Storage,
    Transaction,
    TransactionReceipt,
)

from .spec import Spec, ref_spec_7686

REFERENCE_SPEC_GIT_PATH = ref_spec_7686.git_path
REFERENCE_SPEC_VERSION = ref_spec_7686.version

TX_GAS_LIMIT = 1_000_000
NOT_EXECUTED = 2
EXECUTED = 1


def top_frame_gas_grant(fork: Fork, gas_limit: int) -> int:
    """Return the execution-gas grant of a transaction's top frame."""
    intrinsic = fork.transaction_intrinsic_cost_calculator()(
        return_cost_deducted_prior_execution=True
    )
    return gas_limit - intrinsic


@pytest.mark.valid_from("EIP7686")
@pytest.mark.parametrize(
    "within_limit",
    [
        pytest.param(True, id="at_limit"),
        pytest.param(False, id="beyond_limit"),
    ],
)
@pytest.mark.parametrize(
    "expanding_op",
    [
        pytest.param(Op.MSTORE8, id="mstore8"),
        pytest.param(Op.MLOAD, id="mload"),
    ],
)
def test_memory_limit_boundary(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    within_limit: bool,
    expanding_op: Op,
) -> None:
    """
    Expand memory to the last word at or the first word past the
    frame's limit. The limit is the frame's initial execution-gas
    grant, so it is unaffected by gas already spent when the
    expansion happens.
    """
    grant = top_frame_gas_grant(fork, TX_GAS_LIMIT)
    limit = Spec.memory_limit(grant)
    # Largest allowed memory size: the limit rounded down to a word.
    word_floor = (limit // 32) * 32

    if expanding_op == Op.MSTORE8:
        # Touch the last in-bounds byte, or the first byte beyond.
        offset = word_floor - 1 if within_limit else word_floor
        expansion = Op.MSTORE8(offset, 1)
    else:
        # Read the last in-bounds word, or one byte past it.
        offset = word_floor - 32 if within_limit else word_floor - 31
        expansion = Op.MLOAD(offset) + Op.POP

    storage = Storage()
    contract = pre.deploy_contract(
        code=expansion + Op.SSTORE(0, EXECUTED),
        storage={0: NOT_EXECUTED},
    )
    storage.store_next(EXECUTED if within_limit else NOT_EXECUTED)

    tx = Transaction(
        sender=pre.fund_eoa(),
        to=contract,
        gas_limit=TX_GAS_LIMIT,
        expected_receipt=None
        if within_limit
        # The halt consumes the transaction's entire gas limit.
        else TransactionReceipt(cumulative_gas_used=TX_GAS_LIMIT),
    )

    state_test(
        pre=pre,
        post={contract: Account(storage=storage)},
        tx=tx,
    )


@pytest.mark.valid_from("EIP7686")
@pytest.mark.parametrize(
    "within_limit",
    [
        pytest.param(True, id="at_limit"),
        pytest.param(False, id="beyond_limit"),
    ],
)
def test_memory_limit_child_frame(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    within_limit: bool,
) -> None:
    """
    A child frame's memory limit is its own gas grant, not the
    caller's. The child expands to the last word its grant allows, or
    one word further: the halt is contained in the child and the
    caller continues.
    """
    child_gas = 200_000
    limit = Spec.memory_limit(child_gas)
    word_floor = (limit // 32) * 32
    # The grant is an exact multiple of 32, so the in-bounds case
    # lands exactly on the limit, pinning "strictly exceeding".
    assert word_floor == limit

    offset = word_floor - 1 if within_limit else word_floor
    child = pre.deploy_contract(
        code=Op.MSTORE8(offset, 1) + Op.SSTORE(0, EXECUTED),
        storage={0: NOT_EXECUTED},
    )

    parent_storage = Storage()
    parent = pre.deploy_contract(
        code=Op.SSTORE(
            parent_storage.store_next(1 if within_limit else 0),
            Op.CALL(gas=child_gas, address=child),
        )
        + Op.SSTORE(parent_storage.store_next(EXECUTED), EXECUTED),
    )

    tx = Transaction(
        sender=pre.fund_eoa(),
        to=parent,
        gas_limit=TX_GAS_LIMIT,
    )

    state_test(
        pre=pre,
        post={
            parent: Account(storage=parent_storage),
            child: Account(
                storage={0: EXECUTED if within_limit else NOT_EXECUTED}
            ),
        },
        tx=tx,
    )


@pytest.mark.valid_from("EIP7686")
@pytest.mark.parametrize(
    "within_limit",
    [
        pytest.param(True, id="last_word_within_stipend"),
        pytest.param(False, id="first_word_beyond_stipend"),
    ],
)
def test_value_call_stipend_counts_toward_memory_limit(
    state_test: StateTestFiller,
    pre: Alloc,
    within_limit: bool,
) -> None:
    """
    A value-bearing call requested with zero gas still gives its child the
    2,300-gas stipend. That stipend is part of the child's initial gas grant,
    so it also provides memory headroom even though the caller did not
    withhold it from its own gas.

    Memory is word-rounded: a 2,300-byte cap permits 2,272 bytes, while the
    next word would allocate 2,304 bytes and exceptionally halt the child.
    """
    stipend = 2_300
    last_word_within_limit = (Spec.memory_limit(stipend) // 32) * 32
    offset = (
        last_word_within_limit - 1 if within_limit else last_word_within_limit
    )
    child = pre.deploy_contract(code=Op.MSTORE8(offset, 1) + Op.STOP)

    parent = pre.deploy_contract(
        code=Op.SSTORE(
            0,
            Op.CALL(gas=0, address=child, value=1),
        ),
        balance=1,
    )

    state_test(
        pre=pre,
        post={
            parent: Account(storage={0: 1 if within_limit else 0}),
            child: Account(balance=1 if within_limit else 0),
        },
        tx=Transaction(
            sender=pre.fund_eoa(),
            to=parent,
            gas_limit=TX_GAS_LIMIT,
        ),
    )


@pytest.mark.valid_from("EIP7686")
def test_memory_limit_excludes_state_gas_reservoir(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """
    The memory limit is the frame's execution-gas grant only: a
    transaction carrying a state gas reservoir above the execution
    cap gets no extra memory headroom from it.
    """
    reservoir = 1_000_000
    execution_cap = fork.transaction_gas_limit_cap()
    assert execution_cap is not None, "fork must cap transaction gas"
    gas_limit = execution_cap + reservoir
    grant = top_frame_gas_grant(fork, execution_cap)
    word_floor = (Spec.memory_limit(grant) // 32) * 32

    contract = pre.deploy_contract(
        code=Op.MSTORE8(word_floor, 1) + Op.SSTORE(0, EXECUTED),
        storage={0: NOT_EXECUTED},
    )

    tx = Transaction(
        sender=pre.fund_eoa(),
        to=contract,
        gas_limit=gas_limit,
        state_gas_reservoir=reservoir,
    )

    state_test(
        pre=pre,
        post={contract: Account(storage={0: NOT_EXECUTED})},
        tx=tx,
    )
