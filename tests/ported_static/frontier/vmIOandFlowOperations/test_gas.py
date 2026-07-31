"""
Verify the GAS opcode tracks consumption of the operations preceding it.

Ported from:
state_tests/VMTests/vmIOandFlowOperations/gasFiller.yml

@manually-enhanced: Do not overwrite. The ported filler stored absolute GAS
readings behind a DELEGATECALL dispatcher (fragile against intrinsic-cost
changes); reframed as CodeGasMeasure deltas asserting fork-derived costs.
"""

import pytest
from execution_testing import (
    Account,
    Alloc,
    Bytecode,
    CodeGasMeasure,
    Fork,
    StateTestFiller,
    Transaction,
)
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"

GAS_SLOT = 0x0
SECOND_MSTORE_OFFSET = 0x5A


@pytest.mark.ported_from(
    ["state_tests/VMTests/vmIOandFlowOperations/gasFiller.yml"],
)
@pytest.mark.valid_from("Frontier")
@pytest.mark.parametrize("measured", ["memory_writes", "gas_read"])
def test_gas(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    measured: str,
) -> None:
    """Measure a known window of operations with two GAS readings."""
    window: Bytecode
    extra_stack_items: int
    if measured == "memory_writes":
        # Two memory writes, the second expanding memory past the first.
        window = Op.MSTORE(
            offset=0x0, value=0xFFFFFFFFFF, new_memory_size=0x20
        ) + Op.MSTORE(
            offset=SECOND_MSTORE_OFFSET,
            value=0xEEEE,
            old_memory_size=0x20,
            new_memory_size=SECOND_MSTORE_OFFSET + 0x20,
        )
        extra_stack_items = 0
    else:
        # The GAS opcode itself, whose reading the legacy filler stored.
        window = Op.GAS
        extra_stack_items = 1
    contract = pre.deploy_contract(
        code=CodeGasMeasure(
            code=window,
            extra_stack_items=extra_stack_items,
            sstore_key=GAS_SLOT,
        ),
    )

    tx = Transaction(
        protected=fork.supports_protected_txs(),
        sender=pre.fund_eoa(),
        to=contract,
    )

    post = {contract: Account(storage={GAS_SLOT: window.gas_cost(fork)})}

    state_test(pre=pre, post=post, tx=tx)
