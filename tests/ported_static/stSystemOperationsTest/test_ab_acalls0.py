"""
Verify mutual A<->B recursion with value transfers and fixed gas asks.

Contracts A and B call each other with a fixed gas ask and a value
transfer, each storing the result only after its call returns. A frame
too poor for that store halts, rolling back both the store and the
transfer that funded it.

Ported from:
state_tests/stSystemOperationsTest/ABAcalls0Filler.json

@manually-enhanced: Do not overwrite. The post state follows from a
single decision -- whether B's frame can still afford its store --
because the fixed asks pin every grant below the top frame; the third
frame's death is asserted from the fork's schedule rather than
assumed. B reaches A as its CALLER instead of a hardcoded address, and
both contracts store into a fixed slot rather than the filler's
PC-derived one, whose number tracked nothing but code length.
"""

import pytest
from execution_testing import (
    Account,
    Address,
    Alloc,
    Bytecode,
    Fork,
    StateTestFiller,
    Transaction,
)
from execution_testing.vm import Op, Opcode

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


def chain_call(gas: int, address: Address | Opcode, value: int) -> Bytecode:
    """
    Return the value-bearing CALL that carries the chain one frame on.

    The warmth metadata describes the frames costed in the test, not
    the cold top-level call; it does not change the bytecode.
    """
    return Op.CALL(
        gas=gas,
        address=address,
        value=value,
        address_warm=True,
        value_transfer=True,
    )


@pytest.mark.ported_from(
    ["state_tests/stSystemOperationsTest/ABAcalls0Filler.json"],
)
@pytest.mark.valid_from("Berlin")
def test_ab_acalls0(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """Pin how deep a value-bearing A<->B recursion reaches."""
    result_slot = 0

    b_gas, b_value = 50_000, 23
    b_call_code = chain_call(b_gas, Op.CALLER, b_value)
    # Split out because the gas check below costs exactly this tail.
    b_code_after_call = (
        Op.PUSH1[1]
        + Op.ADD
        + Op.PUSH1[result_slot]
        + Op.SSTORE(
            key_warm=False, original_value=0, current_value=0, new_value=1
        )
    )
    contract_b = pre.deploy_contract(
        code=b_call_code + b_code_after_call + Op.STOP,
        balance=b_value,  # one return payment, before any income
    )

    a_gas, a_value = 100_000, 24
    a_call_code = chain_call(a_gas, contract_b, a_value)
    a_initial_balance = a_value * 1024  # the call-depth ceiling
    contract_a = pre.deploy_contract(
        code=Op.SSTORE(key=result_slot, value=a_call_code),
        balance=a_initial_balance,
    )

    # Fixed call gas pins every grant below the top frame, so three
    # frames settle the chain: the first always stores, the third never
    # can, and B is the only one a repricing flips.
    stipend = fork.gas_costs().CALL_STIPEND
    third_frame_gas = b_gas + stipend - a_call_code.gas_cost(fork)
    assert third_frame_gas < a_gas, "the third frame must be clamped"
    assert third_frame_gas // 64 <= stipend, (
        "a clamped frame must fall short of the SSTORE gas gate"
    )

    # B does fund its call, so it keeps the whole remainder, not a 64th.
    b_gas_kept = a_gas + stipend - b_call_code.gas_cost(fork) - b_gas
    b_stores = (
        b_gas_kept > stipend and b_gas_kept >= b_code_after_call.gas_cost(fork)
    )

    # B stores `1 + 0`: its own call back to A always dies.
    a_stored, b_stored, wei_moved = (1, 1, a_value) if b_stores else (0, 0, 0)
    tx = Transaction(
        sender=pre.fund_eoa(),
        to=contract_a,
        # Only keeps the top frame alive; the call gas sets the depth.
        gas_limit=1_000_000,
    )
    post = {
        contract_a: Account(
            storage={result_slot: a_stored},
            balance=a_initial_balance - wei_moved,
        ),
        contract_b: Account(
            storage={result_slot: b_stored},
            balance=b_value + wei_moved,
        ),
    }

    state_test(pre=pre, post=post, tx=tx)
