"""
Measure the gas cost of the memory-segment opcodes (SHA3, CALLDATACOPY,
CODECOPY, and LOG0-LOG4) as the touched segment grows
(by Ori Pomerantz qbzzt1@gmail.com).

Ported from:
state_tests/stEIP150singleCodeGasPrices/gasCostMemSegFiller.yml

@manually-enhanced: Do not overwrite. The legacy raw GAS-delta windows
are reframed as a CodeGasMeasure per (opcode, size) case over a
pre-expanded memory (so no expansion is charged), asserting the
fork-derived `measured_code.gas_cost(fork)`.
"""

from typing import Any

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
# MSTORE at this offset grows memory past every measured segment below,
# so the measured opcode never pays memory expansion.
PREEXPAND_OFFSET = 0x100
PREEXPANDED = PREEXPAND_OFFSET + 0x20

# Per-word-priced opcodes: sizes straddling the word boundaries.
SEGMENT_SIZES = [0x1, 0x20, 0x21, 0x40, 0x60, 0x80, 0xA0, 0xC0, 0xE0, 0x100]
# Per-byte-priced LOG data: one case per small byte count.
LOG_SIZES = [0x0, 0x1, 0x2, 0x3, 0x4]

CASES = [
    *[("sha3", size) for size in SEGMENT_SIZES],
    *[("calldatacopy", size) for size in SEGMENT_SIZES],
    *[("codecopy", size) for size in SEGMENT_SIZES],
    *[(f"log{topics}", size) for topics in range(5) for size in LOG_SIZES],
]


@pytest.mark.ported_from(
    ["state_tests/stEIP150singleCodeGasPrices/gasCostMemSegFiller.yml"],
)
@pytest.mark.valid_from("Frontier")
@pytest.mark.parametrize(
    "opcode, size", CASES, ids=[f"{op}_size_{size:#x}" for op, size in CASES]
)
def test_gas_cost_mem_seg(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    opcode: str,
    size: int,
) -> None:
    """Measure the gas each memory-segment opcode consumes per size."""
    memory_sizes: dict[str, Any] = {
        "old_memory_size": PREEXPANDED,
        "new_memory_size": PREEXPANDED,
    }
    extra_stack_items = 0
    measured: Bytecode
    if opcode == "sha3":
        measured = Op.SHA3(
            offset=0x0, size=size, data_size=size, **memory_sizes
        )
        extra_stack_items = 1
    elif opcode == "calldatacopy":
        measured = Op.CALLDATACOPY(
            dest_offset=0x0,
            offset=0x0,
            size=size,
            data_size=size,
            **memory_sizes,
        )
    elif opcode == "codecopy":
        measured = Op.CODECOPY(
            dest_offset=0x0,
            offset=0x0,
            size=size,
            data_size=size,
            **memory_sizes,
        )
    else:
        topics = int(opcode[-1])
        log_op = [Op.LOG0, Op.LOG1, Op.LOG2, Op.LOG3, Op.LOG4][topics]
        topic_args: dict[str, Any] = {
            f"topic_{i}": i for i in range(1, topics + 1)
        }
        measured = log_op(
            offset=0x0, size=size, data_size=size, **topic_args, **memory_sizes
        )

    contract = pre.deploy_contract(
        code=Op.MSTORE(offset=PREEXPAND_OFFSET, value=0x1)
        + CodeGasMeasure(
            code=measured,
            extra_stack_items=extra_stack_items,
            sstore_key=GAS_SLOT,
        ),
    )

    tx = Transaction(
        protected=fork.supports_protected_txs(),
        sender=pre.fund_eoa(),
        to=contract,
    )

    post = {contract: Account(storage={GAS_SLOT: measured.gas_cost(fork)})}

    state_test(pre=pre, post=post, tx=tx)
