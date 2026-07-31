"""
Verify jumpdest analysis around push data: a 0x5B byte inside any PUSH1..
PUSH32 immediate is not a valid JUMP target, while the JUMPDEST right after
the push data is.

Ported from:
state_tests/VMTests/vmIOandFlowOperations/jumpToPushFiller.yml

@manually-enhanced: Do not overwrite. The 95 per-size contracts and the
DELEGATECALL dispatcher (with its SUB(GAS, ...) forwarding pin and near-cap
gas limit) were folded into one generator over push size and jump target;
duplicated filler cases were dropped, the first-data-byte variants the
filler deployed but never called are now exercised, and the codeless-target
dispatch case keeps its own test with the call's success flag stored.
"""

import pytest
from execution_testing import (
    Account,
    Alloc,
    Fork,
    StateTestFiller,
    Transaction,
)
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"

STORED_SLOT = 0x0
STORED = 0x1
SENTINEL = 0xBAD
FLAG_SLOT = 0x1
# Explicit sub-call budget: asking for more gas than is available would
# abort the call on pre-EIP-150 forks, so the caller must not forward all.
DISPATCH_GAS = 100_000

store_marker = Op.SSTORE(key=STORED_SLOT, value=STORED)
# Layout: <store_marker> <PUSH1 pc> <JUMP> <PUSHn 0x5B*n> <JUMPDEST>
PUSH_OPCODE_PC = len(bytes(store_marker)) + 3


@pytest.mark.ported_from(
    ["state_tests/VMTests/vmIOandFlowOperations/jumpToPushFiller.yml"],
)
@pytest.mark.valid_from("Frontier")
@pytest.mark.parametrize(
    "target", ["jumpdest", "push_data_first", "push_data_last"]
)
@pytest.mark.parametrize("push_size", range(1, 33), ids=lambda n: f"push{n}")
def test_jump_to_push(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    push_size: int,
    target: str,
) -> None:
    """Jump at, into, or past a push immediate made of 0x5B bytes."""
    if target == "jumpdest":
        target_pc = PUSH_OPCODE_PC + push_size + 1
        stores = True
    elif target == "push_data_first":
        target_pc = PUSH_OPCODE_PC + 1
        stores = False
    else:  # push_data_last
        target_pc = PUSH_OPCODE_PC + push_size
        stores = False
    assert target_pc <= 0xFF, "jump target must fit a PUSH1"

    push_op = getattr(Op, f"PUSH{push_size}")
    code = (
        store_marker
        + Op.JUMP(pc=target_pc)
        + push_op[int.from_bytes(b"\x5b" * push_size, byteorder="big")]
        + Op.JUMPDEST
    )
    contract = pre.deploy_contract(
        code=code,
        storage={STORED_SLOT: SENTINEL},
    )

    tx = Transaction(
        protected=fork.supports_protected_txs(),
        sender=pre.fund_eoa(),
        to=contract,
    )

    post = {
        contract: Account(
            storage={STORED_SLOT: STORED if stores else SENTINEL},
        ),
    }

    state_test(pre=pre, post=post, tx=tx)


@pytest.mark.ported_from(
    ["state_tests/VMTests/vmIOandFlowOperations/jumpToPushFiller.yml"],
)
@pytest.mark.valid_from("Homestead")
def test_jump_to_push_empty_target(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """The legacy dispatch to a codeless target succeeds, storing nothing."""
    target = pre.nonexistent_account()
    caller = pre.deploy_contract(
        code=Op.SSTORE(
            key=FLAG_SLOT,
            value=Op.DELEGATECALL(gas=DISPATCH_GAS, address=target),
        )
        + Op.STOP,
        storage={STORED_SLOT: SENTINEL},
    )

    tx = Transaction(
        protected=fork.supports_protected_txs(),
        sender=pre.fund_eoa(),
        to=caller,
    )

    post = {
        caller: Account(
            storage={STORED_SLOT: SENTINEL, FLAG_SLOT: 1},
        ),
    }

    state_test(pre=pre, post=post, tx=tx)
