"""
Verify JUMPI destination validation and conditional behavior: a taken jump
needs a JUMPDEST outside push data, and an untaken one falls through.

Ported from:
state_tests/VMTests/vmIOandFlowOperations/jumpiFiller.yml

@manually-enhanced: Do not overwrite. The DELEGATECALL dispatcher (calldata
addressed, hardcoded addresses, near-cap gas limit) was dropped; each case
is called directly with a sentinel in the stored slot so a reverted frame
is distinguishable from a successful store. Two byte-identical duplicated
filler cases were folded, and the memory-sourced jump cases were restored
to their lll source's intent (jump to MLOAD of -1).
"""

import pytest
from execution_testing import (
    Account,
    Alloc,
    Bytecode,
    Fork,
    StateTestFiller,
    Transaction,
)
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"

STORED_SLOT = 0x0
# The value a successful path stores, and the sentinel it replaces.
STORED = 0x600D
SENTINEL = 0xBAD
# Budget above the intrinsic cost so the endless-loop case runs out of gas
# quickly instead of consuming a maxed-out transaction budget.
LOOP_GAS_BUDGET = 0x10000

store_marker = Op.SSTORE(key=STORED_SLOT, value=STORED)


@pytest.mark.ported_from(
    ["state_tests/VMTests/vmIOandFlowOperations/jumpiFiller.yml"],
)
@pytest.mark.valid_from("Frontier")
@pytest.mark.parametrize(
    "case",
    [
        "jumpi_hyperspace_computed_mul",
        "jumpi_not_taken_hyperspace_computed_mul",
        "jumpi_over_stop",
        "jumpi_not_taken_to_stop",
        "jumpi_hyperspace_0xfffffff",
        "jumpi_not_taken_hyperspace",
        "jumpi_to_push_opcode",
        "endless_loop",
        "jumpi_over_push_data",
        "jump_then_jumpi_back",
        "jumpi_computed_add",
        "jumpi_not_taken_computed_add",
        "jumpi_to_push_data_jumpdest_byte",
        "jumpi_to_push_data",
        "jumpi_to_gas_after_jumpdest",
        "jumpi_to_gas_before_jumpdest",
        "jumpi_hyperspace_2pow64",
        "jumpi_not_taken_2pow64",
        "jumpi_hyperspace_2pow32",
        "jumpi_not_taken_2pow32",
        "jumpi_hyperspace_from_memory",
        "jumpi_not_taken_from_memory",
        "jumpi_into_jumpdest_list",
        "countdown_loop",
    ],
)
def test_jumpi(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    case: str,
) -> None:
    """Run one JUMPI scenario and check whether its store landed."""
    code: Bytecode
    stores: bool
    if case == "jumpi_hyperspace_computed_mul":
        # Source: lll
        # { [[0]] 0x600D (asm 0x01 0x10 0x20 mul jumpi jumpdest) }
        code = (
            store_marker
            + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
            + Op.JUMPDEST
            + Op.STOP
        )
        stores = False
    elif case == "jumpi_not_taken_hyperspace_computed_mul":
        # Source: lll
        # { [[0]] 0x600D (asm 0x00 0x10 0x20 mul jumpi jumpdest) }
        code = (
            store_marker
            + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x0)
            + Op.JUMPDEST
            + Op.STOP
        )
        stores = True
    elif case == "jumpi_over_stop":
        # Source: raw
        # 0x6001600657005B61600D60005500
        code = (
            Op.JUMPI(pc=0x6, condition=0x1)
            + Op.STOP
            + Op.JUMPDEST
            + store_marker
            + Op.STOP
        )
        stores = True
    elif case == "jumpi_not_taken_to_stop":
        # Source: raw (the untaken jump falls through to STOP; no store)
        # 0x6000600657005B61600D60005500
        code = (
            Op.JUMPI(pc=0x6, condition=0x0)
            + Op.STOP
            + Op.JUMPDEST
            + store_marker
            + Op.STOP
        )
        stores = False
    elif case == "jumpi_hyperspace_0xfffffff":
        # Source: lll
        # { [[0]] 0x600D (asm 0xff 0x0fffffff jumpi) }
        code = store_marker + Op.JUMPI(pc=0xFFFFFFF, condition=0xFF) + Op.STOP
        stores = False
    elif case == "jumpi_not_taken_hyperspace":
        # Source: lll
        # { [[0]] 0x600D (asm 0x00 0x0fffffff jumpi) }
        code = store_marker + Op.JUMPI(pc=0xFFFFFFF, condition=0x0) + Op.STOP
        stores = True
    elif case == "jumpi_to_push_opcode":
        # Source: raw (jump lands on a PUSH1 opcode byte)
        # 0x6023600160085760015b600255
        code = (
            Op.PUSH1[0x23]
            + Op.JUMPI(pc=0x8, condition=0x1)
            + Op.PUSH1[0x1]
            + Op.JUMPDEST
            + Op.PUSH1[0x2]
            + Op.SSTORE
        )
        stores = False
    elif case == "endless_loop":
        # Source: raw
        # 0x61600D6000555B6006600657
        code = store_marker + Op.JUMPDEST + Op.JUMPI(pc=0x6, condition=0x6)
        stores = False
    elif case == "jumpi_over_push_data":
        # Source: raw
        # 0x61600D6001600A5760FF5B600055
        code = (
            Op.PUSH2[STORED]
            + Op.JUMPI(pc=0xA, condition=0x1)
            + Op.PUSH1[0xFF]
            + Op.JUMPDEST
            + Op.PUSH1[STORED_SLOT]
            + Op.SSTORE
        )
        stores = True
    elif case == "jump_then_jumpi_back":
        # Source: raw
        # 0x600B565B61600D600055005B6001600357
        code = (
            Op.JUMP(pc=0xB)
            + Op.JUMPDEST
            + store_marker
            + Op.STOP
            + Op.JUMPDEST
            + Op.JUMPI(pc=0x3, condition=0x1)
        )
        stores = True
    elif case == "jumpi_computed_add":
        # Source: raw
        # 0x6001600460050157005B61600D600055
        code = (
            Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x1)
            + Op.STOP
            + Op.JUMPDEST
            + store_marker
        )
        stores = True
    elif case == "jumpi_not_taken_computed_add":
        # Source: raw (the untaken jump falls through to STOP; no store)
        # 0x6000600460050157005B61600D600055
        code = (
            Op.JUMPI(pc=Op.ADD(0x5, 0x4), condition=0x0)
            + Op.STOP
            + Op.JUMPDEST
            + store_marker
        )
        stores = False
    elif case == "jumpi_to_push_data_jumpdest_byte":
        # Source: raw (pc 7 is a 0x5B byte, but inside PUSH1's data)
        # 0x600160075700605B61600D600055
        code = (
            Op.JUMPI(pc=0x7, condition=0x1)
            + Op.STOP
            + Op.PUSH1[0x5B]
            + store_marker
        )
        stores = False
    elif case == "jumpi_to_push_data":
        # Source: raw
        # 0x600160075700600161600D600055
        code = (
            Op.JUMPI(pc=0x7, condition=0x1)
            + Op.STOP
            + Op.PUSH1[0x1]
            + store_marker
        )
        stores = False
    elif case == "jumpi_to_gas_after_jumpdest":
        # Source: raw (pc 0xD is a GAS opcode, one byte past the JUMPDEST)
        # 0x61600D6000556001600D575A5B5A600155
        code = (
            store_marker
            + Op.JUMPI(pc=0xD, condition=0x1)
            + Op.GAS
            + Op.JUMPDEST
            + Op.SSTORE(key=0x1, value=Op.GAS)
        )
        stores = False
    elif case == "jumpi_to_gas_before_jumpdest":
        # Source: raw (pc 0xB is the GAS opcode before the JUMPDEST)
        # 0x61600D6000556001600B575A5B5A600155
        code = (
            store_marker
            + Op.JUMPI(pc=0xB, condition=0x1)
            + Op.GAS
            + Op.JUMPDEST
            + Op.SSTORE(key=0x1, value=Op.GAS)
        )
        stores = False
    elif case == "jumpi_hyperspace_2pow64":
        # Source: raw
        # 0x60116801000000000000000D575b5b61600D600055
        code = (
            Op.JUMPI(pc=0x1000000000000000D, condition=0x11)
            + Op.JUMPDEST * 2
            + store_marker
        )
        stores = False
    elif case == "jumpi_not_taken_2pow64":
        # Source: raw
        # 0x60006801000000000000000D575b5b61600D600055
        code = (
            Op.JUMPI(pc=0x1000000000000000D, condition=0x0)
            + Op.JUMPDEST * 2
            + store_marker
        )
        stores = True
    elif case == "jumpi_hyperspace_2pow32":
        # Source: raw
        # 0x6011640100000009575b5b61600D600055
        code = (
            Op.JUMPI(pc=0x100000009, condition=0x11)
            + Op.JUMPDEST * 2
            + store_marker
        )
        stores = False
    elif case == "jumpi_not_taken_2pow32":
        # Source: raw
        # 0x6000640100000009575b5b61600D600055
        code = (
            Op.JUMPI(pc=0x100000009, condition=0x0)
            + Op.JUMPDEST * 2
            + store_marker
        )
        stores = True
    elif case == "jumpi_hyperspace_from_memory":
        # Source: lll
        # { @0 (- 0 1) (asm 1 0 mload jumpi 0x600D 0x00 sstore) }
        code = (
            Op.MSTORE(offset=0x0, value=Op.SUB(0x0, 0x1))
            + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x1)
            + store_marker
            + Op.STOP
        )
        stores = False
    elif case == "jumpi_not_taken_from_memory":
        # Source: lll
        # { @0 (- 0 1) (asm 0 0 mload jumpi 0x600D 0x00 sstore) }
        code = (
            Op.MSTORE(offset=0x0, value=Op.SUB(0x0, 0x1))
            + Op.JUMPI(pc=Op.MLOAD(offset=0x0), condition=0x0)
            + store_marker
            + Op.STOP
        )
        stores = True
    elif case == "jumpi_into_jumpdest_list":
        # Source: raw
        # 0x6001600E575B5B5B5B5B5B5B5B5B5B5B5B5B5B5B5B61600D600055
        code = (
            Op.JUMPI(pc=0xE, condition=0x1) + Op.JUMPDEST * 16 + store_marker
        )
        stores = True
    else:  # countdown_loop
        # Source: raw (counts memory word 0 down from 0x10 to zero)
        # 0x61600D60005560106000525B60016000510380600052600B57
        code = (
            store_marker
            + Op.MSTORE(offset=0x0, value=0x10)
            + Op.JUMPDEST
            + Op.SUB(Op.MLOAD(offset=0x0), 0x1)
            + Op.MSTORE(offset=0x0, value=Op.DUP1)
            + Op.PUSH1[0xB]
            + Op.JUMPI
        )
        stores = True

    contract = pre.deploy_contract(
        code=code,
        storage={STORED_SLOT: SENTINEL},
    )

    tx = Transaction(
        protected=fork.supports_protected_txs(),
        sender=pre.fund_eoa(),
        to=contract,
        # The endless loop must run out of gas: give it a small bounded
        # budget instead of a maxed-out one.
        gas_limit=(
            fork.transaction_intrinsic_cost_calculator()() + LOOP_GAS_BUDGET
            if case == "endless_loop"
            else None
        ),
    )

    post = {
        contract: Account(
            storage={STORED_SLOT: STORED if stores else SENTINEL},
        ),
    }

    state_test(pre=pre, post=post, tx=tx)
