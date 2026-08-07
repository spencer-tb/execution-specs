"""
Verify mutual A<->B recursion throttled by a per-level gas reserve.

Both contracts bump their own counter, then call the other side
forwarding everything but a 100,000-gas reserve (A sends one wei each
level; B sends nothing back). Nothing runs after the call, so a level
either completes -- keeping its bump and its transfer -- or dies of gas
and reverts both.

Ported from:
state_tests/stSystemOperationsTest/ABAcalls3Filler.json

@manually-enhanced: Do not overwrite. The ported test fixed the budget
and recorded the depth it reached, a golden value only a full replay of
the schedule can carry across forks. This fixes the depth and derives
the budget instead, which is a closed form because an access list
pre-warms every access, the budget stays far below 64 reserves so the
reserve rather than the EIP-150 clamp sets every grant, and it runs out
exactly at the chosen round so the chain dies at once. B reaches A as
its CALLER instead of a hardcoded address.
"""

import pytest
from execution_testing import (
    AccessList,
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


@pytest.mark.ported_from(
    ["state_tests/stSystemOperationsTest/ABAcalls3Filler.json"],
)
@pytest.mark.valid_from("Berlin")
def test_ab_acalls3(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """Pin how many rounds a reserve-throttled A<->B recursion runs."""
    counter_slot, counter_seed = 0, 1

    # Ported: each level holds this much back instead of forwarding it.
    gas_reserve = 100_000
    a_value = 1

    rounds = 8
    a_rounds, b_rounds = (rounds + 1) // 2, rounds // 2

    def bounce_code(call: Bytecode) -> Bytecode:
        """Bump the own-depth counter, then call the other side."""
        return (
            Op.SSTORE(
                key=counter_slot,
                value=Op.ADD(Op.SLOAD(key=counter_slot), 1),
            )
            + call
        )

    def reserve_call(address: Address | Opcode, value: int) -> Bytecode:
        """Return one side's call: forward all but the reserve."""
        return Op.CALL(
            gas=Op.SUB(Op.GAS, gas_reserve),
            address=address,
            value=value,
            # gas accounting
            address_warm=True,
            value_transfer=value > 0,
        )

    b_call = reserve_call(Op.CALLER, 0)
    contract_b = pre.deploy_contract(
        code=bounce_code(b_call),
        storage={counter_slot: counter_seed},
    )

    a_call = reserve_call(contract_b, a_value)
    contract_a = pre.deploy_contract(
        code=bounce_code(a_call),
        storage={counter_slot: counter_seed},
        balance=a_rounds * a_value,
    )

    # Pre-warm every account and slot the chain touches,
    # so no level pays a cold price.
    access_list = [
        AccessList(address=contract_a, storage_keys=[counter_slot]),
        AccessList(address=contract_b, storage_keys=[counter_slot]),
    ]

    stipend = fork.gas_costs().CALL_STIPEND
    statics = (
        Op.ADD(Op.SLOAD(key=counter_slot, key_warm=True), 1)
        + Op.PUSH1[counter_slot]
    ).gas_cost(fork)

    first_store = Op.SSTORE(
        key_warm=True,
        original_value=counter_seed,
        current_value=counter_seed,
        new_value=counter_seed + 1,
    ).gas_cost(fork)
    later_store = Op.SSTORE(
        key_warm=True,
        original_value=counter_seed,
        current_value=counter_seed + 1,
        new_value=counter_seed + 2,
    ).gas_cost(fork)

    def pushes_before_gas_read(call: Bytecode, sends_value: bool) -> int:
        """What the call charges before its GAS opcode reads."""
        upfront = Op.CALL(
            address_warm=True, value_transfer=sends_value
        ).gas_cost(fork)
        return call.gas_cost(fork) - upfront - Op.SUB.gas_cost(fork)

    chain_gas = (
        rounds * (gas_reserve + statics)
        + 2 * first_store
        + (rounds - 2) * later_store
        + a_rounds * (pushes_before_gas_read(a_call, True) - stipend)
        + b_rounds * pushes_before_gas_read(b_call, False)
    )
    # Above 64 reserves the EIP-150 clamp would set the grants instead,
    # and the sum above would stop describing the chain.
    assert chain_gas < 64 * gas_reserve, "the reserve must bind throughout"

    tx = Transaction(
        sender=pre.fund_eoa(),
        to=contract_a,
        access_list=access_list,
        gas_limit=(
            fork.transaction_intrinsic_cost_calculator()(
                access_list=access_list
            )
            + fork.transaction_top_frame_state_gas()
            + chain_gas
        ),
    )

    post = {
        contract_a: Account(
            storage={counter_slot: counter_seed + a_rounds},
            balance=0,
        ),
        contract_b: Account(
            storage={counter_slot: counter_seed + b_rounds},
            balance=a_rounds * a_value,
        ),
    }

    state_test(pre=pre, post=post, tx=tx)
