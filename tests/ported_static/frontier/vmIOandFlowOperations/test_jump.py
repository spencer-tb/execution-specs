"""
Verify JUMP destination validation: only JUMPDEST opcode bytes outside push
data are valid targets, and an invalid jump reverts the whole frame.

Ported from:
state_tests/VMTests/vmIOandFlowOperations/jumpFiller.yml

@manually-enhanced: Do not overwrite. The DELEGATECALL dispatcher (calldata
indexed, hardcoded addresses, near-cap gas limit) was dropped; each case is
called directly with a sentinel in the stored slot so a reverted frame is
distinguishable from a successful store. The memory-sourced jump case was
restored to its lll source's intent (jump to MLOAD of -1).
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
# The value a successful jump path stores, and the sentinel it replaces.
STORED = 0x600D
SENTINEL = 0xBAD
# Budget above the intrinsic cost so the endless-loop case runs out of gas
# quickly instead of consuming a maxed-out transaction budget.
LOOP_GAS_BUDGET = 0x10000

store_marker = Op.SSTORE(key=STORED_SLOT, value=STORED)


@pytest.mark.ported_from(
    ["state_tests/VMTests/vmIOandFlowOperations/jumpFiller.yml"],
)
@pytest.mark.valid_from("Frontier")
@pytest.mark.parametrize(
    "case",
    [
        "jump_hyperspace_computed_mul",
        "jumpi_hyperspace_computed_mul",
        "jump_over_stop",
        "jump_hyperspace_0xfffffff",
        "jump_to_push_opcode",
        "endless_loop",
        "jump_over_push_data",
        "jump_forward_and_back",
        "jump_computed_add",
        "jump_to_push_data_jumpdest_byte",
        "jump_to_push_data",
        "jump_to_gas_after_jumpdest",
        "jump_to_gas_before_jumpdest",
        "jump_hyperspace_2pow64",
        "jump_hyperspace_2pow32",
        "jump_hyperspace_from_memory",
        "jump_into_jumpdest_list",
    ],
)
def test_jump(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    case: str,
) -> None:
    """Run one JUMP scenario and check whether its store landed."""
    code: Bytecode
    stores: bool
    if case == "jump_hyperspace_computed_mul":
        # Source: lll
        # { [[0]] 0x600D (asm 0x10 0x20 mul jump jumpdest) }
        code = (
            store_marker
            + Op.JUMP(pc=Op.MUL(0x20, 0x10))
            + Op.JUMPDEST
            + Op.STOP
        )
        stores = False
    elif case == "jumpi_hyperspace_computed_mul":
        # Source: lll
        # { [[0]] 0x600D (asm 0x01 0x10 0x20 mul jumpi jumpdest) }
        code = (
            store_marker
            + Op.JUMPI(pc=Op.MUL(0x20, 0x10), condition=0x1)
            + Op.JUMPDEST
            + Op.STOP
        )
        stores = False
    elif case == "jump_over_stop":
        # Source: raw
        # 0x600456005B61600D60005500
        code = Op.JUMP(pc=0x4) + Op.STOP + Op.JUMPDEST + store_marker + Op.STOP
        stores = True
    elif case == "jump_hyperspace_0xfffffff":
        # Source: lll
        # { [[0]] 0x600D (asm 0x0fffffff jump) }
        code = store_marker + Op.JUMP(pc=0xFFFFFFF) + Op.STOP
        stores = False
    elif case == "jump_to_push_opcode":
        # Source: raw (jump lands on the PUSH1 opcode byte at pc 8)
        # 0x602360085660015b600255
        code = (
            Op.PUSH1[0x23]
            + Op.JUMP(pc=0x8)
            + Op.PUSH1[0x1]
            + Op.JUMPDEST
            + Op.PUSH1[0x2]
            + Op.SSTORE
        )
        stores = False
    elif case == "endless_loop":
        # Source: raw
        # 0x61600D6000555B600656
        code = store_marker + Op.JUMPDEST + Op.JUMP(pc=0x6)
        stores = False
    elif case == "jump_over_push_data":
        # Source: raw
        # 0x61600D60085660FF5B600055
        code = (
            Op.PUSH2[STORED]
            + Op.JUMP(pc=0x8)
            + Op.PUSH1[0xFF]
            + Op.JUMPDEST
            + Op.PUSH1[STORED_SLOT]
            + Op.SSTORE
        )
        stores = True
    elif case == "jump_forward_and_back":
        # Source: raw
        # 0x600B565B61600D600055005B600356
        code = (
            Op.JUMP(pc=0xB)
            + Op.JUMPDEST
            + store_marker
            + Op.STOP
            + Op.JUMPDEST
            + Op.JUMP(pc=0x3)
        )
        stores = True
    elif case == "jump_computed_add":
        # Source: raw
        # 0x600260050156005B61600D600055
        code = Op.JUMP(pc=Op.ADD(0x5, 0x2)) + Op.STOP + Op.JUMPDEST
        code += store_marker
        stores = True
    elif case == "jump_to_push_data_jumpdest_byte":
        # Source: raw (pc 5 is a 0x5B byte, but inside PUSH1's data)
        # 0x60055600605B61600D600055
        code = Op.JUMP(pc=0x5) + Op.STOP + Op.PUSH1[0x5B] + store_marker
        stores = False
    elif case == "jump_to_push_data":
        # Source: raw
        # 0x60055600600161600D600055
        code = Op.JUMP(pc=0x5) + Op.STOP + Op.PUSH1[0x1] + store_marker
        stores = False
    elif case == "jump_to_gas_after_jumpdest":
        # Source: raw (pc 0xB is a GAS opcode, one byte past the JUMPDEST)
        # 0x61600D600055600B565A5B5A600155
        code = (
            store_marker
            + Op.JUMP(pc=0xB)
            + Op.GAS
            + Op.JUMPDEST
            + Op.SSTORE(key=0x1, value=Op.GAS)
        )
        stores = False
    elif case == "jump_to_gas_before_jumpdest":
        # Source: raw (pc 0x9 is the GAS opcode before the JUMPDEST)
        # 0x61600D6000556009565A5B5A600155
        code = (
            store_marker
            + Op.JUMP(pc=0x9)
            + Op.GAS
            + Op.JUMPDEST
            + Op.SSTORE(key=0x1, value=Op.GAS)
        )
        stores = False
    elif case == "jump_hyperspace_2pow64":
        # Source: raw
        # 0x6801000000000000000b565b5b6001600155
        code = (
            Op.JUMP(pc=0x1000000000000000B)
            + Op.JUMPDEST * 2
            + Op.SSTORE(key=0x1, value=0x1)
        )
        stores = False
    elif case == "jump_hyperspace_2pow32":
        # Source: raw
        # 0x640100000007565b5b6001600155
        code = (
            Op.JUMP(pc=0x100000007)
            + Op.JUMPDEST * 2
            + Op.SSTORE(key=0x1, value=0x1)
        )
        stores = False
    elif case == "jump_hyperspace_from_memory":
        # Source: lll
        # { @0 (- 0 1) (asm 0 mload jump 0x600D 0x00 sstore) }
        code = (
            Op.MSTORE(offset=0x0, value=Op.SUB(0x0, 0x1))
            + Op.JUMP(pc=Op.MLOAD(offset=0x0))
            + store_marker
            + Op.STOP
        )
        stores = False
    else:  # jump_into_jumpdest_list
        # Source: raw
        # 0x600E565B5B5B5B5B5B5B5B5B5B5B5B5B5B5B5B61600D600055
        code = Op.JUMP(pc=0xE) + Op.JUMPDEST * 16 + store_marker
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
