"""
Verify a transaction-level out-of-gas reverts storage increments made
two call depths down: the sub-frames' grants are sized to succeed, but
the top frame's budget is cut one gas short — at its final SSTORE or
already at its second call — so every write in the tree unwinds.

Ported from:
state_tests/stRevertTest/RevertDepth2Filler.json

@manually-enhanced: Do not overwrite. The two pinned budgets (170685 /
136685) and all sub-call grants are now derived from fork composites;
the cut point is parametrized. Undercounting slack (the shared leaf's
second, dirty write) only moves the OOG earlier, never past the cut.
Floors at Berlin: the framework prices opcode composites with the
EIP-2929 schedule, so earlier forks cannot be derived exactly.
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

# Slack added to every derived sub-call grant.
GRANT_HEADROOM = 500
# Constantinople/Petersburg charge 5000 for a dirty re-store where the
# framework composite prices 100; the leaf's second-call grant carries
# this explicitly.
DIRTY_SSTORE_HEADROOM = 5_000


def _increment() -> Bytecode:
    """
    Build the shared slot-0 increment used by every contract.

    The SLOAD pays the slot's cold access, so the SSTORE on the same
    slot is warm.
    """
    return Op.SSTORE(
        key=0x0,
        value=Op.ADD(0x1, Op.SLOAD(key=0x0)),
        key_warm=True,
        original_value=0,
        new_value=1,
    )


@pytest.mark.ported_from(
    ["state_tests/stRevertTest/RevertDepth2Filler.json"],
)
@pytest.mark.valid_from("Berlin")
@pytest.mark.parametrize("cut_point", ["final_sstore", "second_call"])
def test_revert_depth2(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    cut_point: str,
) -> None:
    """Unwind depth-two storage increments on a top-frame OOG."""
    # Leaf: increments its slot 0. Called once per chain; the second
    # call sees a warm address, a warm key, and a dirty slot.
    leaf_code = _increment() + Op.STOP
    leaf = pre.deploy_contract(code=leaf_code)
    leaf_first_consumed = leaf_code.gas_cost(fork)
    # The second call's consumption is undercounted (its dirty SSTORE
    # is priced differently across forks): undercounting keeps the
    # derived budget below the true total, which is the safe side.
    leaf_second_read = Op.ADD(0x1, Op.SLOAD(key=0x0, key_warm=True))
    leaf_second_consumed = leaf_second_read.gas_cost(fork)
    leaf_first_grant = leaf_first_consumed + GRANT_HEADROOM
    leaf_second_grant = (
        leaf_second_consumed + DIRTY_SSTORE_HEADROOM + GRANT_HEADROOM
    )

    # First chain: increment, then call the (cold) leaf.
    chain1_code = (
        _increment()
        + Op.SSTORE(
            key=0x1,
            value=Op.CALL(gas=leaf_first_grant, address=leaf),
            key_warm=False,
            original_value=0,
            new_value=1,
        )
        + Op.STOP
    )
    chain1 = pre.deploy_contract(code=chain1_code)
    chain1_consumed = chain1_code.gas_cost(fork) + leaf_first_consumed
    chain1_grant = chain1_code.gas_cost(fork) + leaf_first_grant

    # Second chain: increment, call the (now warm) leaf, snapshot GAS.
    chain2_code = (
        _increment()
        + Op.SSTORE(
            key=0x1,
            value=Op.CALL(
                gas=leaf_second_grant, address=leaf, address_warm=True
            ),
            key_warm=False,
            original_value=0,
            new_value=1,
        )
        + Op.SSTORE(
            key=0x2,
            value=Op.GAS,
            key_warm=False,
            original_value=0,
            new_value=1,
        )
        + Op.STOP
    )
    chain2 = pre.deploy_contract(code=chain2_code)
    chain2_consumed = chain2_code.gas_cost(fork) + leaf_second_consumed
    chain2_grant = (
        chain2_code.gas_cost(fork) + leaf_second_grant + GRANT_HEADROOM
    )

    target_code = (
        _increment()
        + Op.SSTORE(
            key=0x1,
            value=Op.CALL(gas=chain1_grant, address=chain1),
            key_warm=False,
            original_value=0,
            new_value=1,
        )
        + Op.SSTORE(
            key=0x2,
            value=Op.CALL(gas=chain2_grant, address=chain2),
            key_warm=False,
            original_value=0,
            new_value=1,
        )
        + Op.STOP
    )
    target = pre.deploy_contract(code=target_code)

    # One gas short of full completion: the OOG lands at the final
    # SSTORE, or — cutting the second chain's whole cost too — already
    # at the second call's machinery.
    total = (
        fork.transaction_intrinsic_cost_calculator()()
        + target_code.gas_cost(fork)
        + chain1_consumed
        + chain2_consumed
    )
    gas_limit = total - 1
    if cut_point == "second_call":
        final_sstore_cost = Op.SSTORE(
            key_warm=False, original_value=0, new_value=1
        ).gas_cost(fork)
        gas_limit -= chain2_consumed + final_sstore_cost

    sender = pre.fund_eoa()
    tx = Transaction(
        sender=sender,
        to=target,
        gas_limit=gas_limit,
    )

    post = {
        target: Account(storage={}),
        chain1: Account(storage={}),
        chain2: Account(storage={}),
        leaf: Account(storage={}),
        sender: Account(nonce=1),
    }

    state_test(pre=pre, post=post, tx=tx)
