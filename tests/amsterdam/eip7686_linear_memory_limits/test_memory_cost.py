"""Memory expansion is priced linearly under EIP-7686."""

import pytest
from execution_testing import (
    Account,
    Alloc,
    CodeGasMeasure,
    Fork,
    Op,
    StateTestFiller,
    Transaction,
)

from .spec import ref_spec_7686

REFERENCE_SPEC_GIT_PATH = ref_spec_7686.git_path
REFERENCE_SPEC_VERSION = ref_spec_7686.version


@pytest.mark.valid_from("EIP7686")
@pytest.mark.parametrize(
    "memory_size",
    [
        pytest.param(32, id="single_word"),
        pytest.param(1024, id="one_kilobyte"),
        pytest.param(32 * 1024, id="quadratic_term_visible"),
        pytest.param(1024 * 1024, id="one_mebibyte"),
    ],
)
@pytest.mark.parametrize(
    "expanding_op",
    [
        pytest.param(Op.MSTORE, id="mstore"),
        pytest.param(Op.MLOAD, id="mload"),
    ],
)
def test_linear_memory_expansion_cost(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    memory_size: int,
    expanding_op: Op,
) -> None:
    """
    Measure the gas a single memory-expanding opcode consumes and pin
    it to the fork's memory expansion calculator, which is linear from
    EIP-7686 onward.
    """
    offset = memory_size - 32
    if expanding_op == Op.MSTORE:
        measured_code = Op.MSTORE(
            offset=offset, value=1, new_memory_size=memory_size
        )
        bare_cost = Op.MSTORE(new_memory_size=memory_size).gas_cost(fork)
        extra_stack_items = 0
    else:
        measured_code = Op.MLOAD(offset=offset, new_memory_size=memory_size)
        bare_cost = Op.MLOAD(new_memory_size=memory_size).gas_cost(fork)
        extra_stack_items = 1

    overhead_cost = measured_code.gas_cost(fork) - bare_cost

    contract = pre.deploy_contract(
        code=CodeGasMeasure(
            code=measured_code,
            overhead_cost=overhead_cost,
            extra_stack_items=extra_stack_items,
        ),
    )

    tx = Transaction(sender=pre.fund_eoa(), to=contract)

    state_test(
        pre=pre,
        post={contract: Account(storage={0: bare_cost})},
        tx=tx,
    )
