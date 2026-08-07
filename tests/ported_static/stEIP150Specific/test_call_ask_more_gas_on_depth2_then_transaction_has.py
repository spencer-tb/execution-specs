"""
Verify the EIP-150 63/64 clamp at call depth 2: a first-level call receives
its exact (affordable) ask, and its own oversized ask is clamped to 63/64
of what remains in that frame.

Ported from:
state_tests/stEIP150Specific/CallAskMoreGasOnDepth2ThenTransactionHasFiller.json

@manually-enhanced: Do not overwrite. The lower frames return their
observed GAS up the stack instead of SSTORE-ing it (the ported lower-frame
gas snapshots are EIP-8037 state-gas traps), and both expectations are
derived from the fork: the depth-1 frame sees exactly its asked budget,
the depth-2 frame sees `base - base // 64` of the depth-1 remainder.
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


@pytest.mark.ported_from(
    [
        "state_tests/stEIP150Specific/CallAskMoreGasOnDepth2ThenTransactionHasFiller.json"  # noqa: E501
    ],
)
@pytest.mark.valid_from("Berlin")
def test_call_ask_more_gas_on_depth2_then_transaction_has(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """A depth-2 call asking above the frame budget gets 63/64 of it."""
    flag_slot = 0x0
    depth2_gas_slot = 0x1
    depth1_gas_slot = 0x2

    # According to EIP-150, forwarded = min(gas, available - available // 64)
    # On depth 1, gas (call_gas: 200_000) affordable, so ask_gas dominates.
    # On depth 2, gas (call_gas: 600_000) above depth-1 frame, clamp decides.
    caller_gas = 200_000
    ask_gas = 600_000

    # MEM[0x00:0x20] Depth 2 Gas Consumption
    # MEM[0x20:0x40] Depth 1 Gas Consumption

    # returns the gas it observed on depth 2.
    depth2_snapshot = pre.deploy_contract(
        code=Op.MSTORE(
            0,
            Op.GAS,
            # gas accounting
            old_memory_size=0x00,
            new_memory_size=0x20,
        )
        + Op.RETURN(0, 0x20),
    )

    # returns the gas it observed on depth 1.
    depth1_snapshot = Op.MSTORE(
        0x20,
        Op.GAS,
        # gas accounting
        old_memory_size=0x00,
        new_memory_size=0x40,
    )

    depth2_call = Op.CALL(
        gas=ask_gas,
        address=depth2_snapshot,
        ret_size=0x20,
        # gas accounting
        address_warm=False,
        account_new=False,
        new_memory_size=0x40,
        old_memory_size=0x40,
    )

    # Depth 1's ask is affordable, so it arrives whole;
    depth1 = pre.deploy_contract(
        code=depth1_snapshot + depth2_call + Op.RETURN(0, 0x40),
    )
    depth1_observed = caller_gas - Op.GAS.gas_cost(fork)

    # Depth 2's ask is not, so EIP-150 forwards all but 1/64 of whatever
    # the depth-1 frame still holds after the snapshot and the call.
    base = (
        caller_gas
        - depth1_snapshot.gas_cost(fork)
        - depth2_call.gas_cost(fork)
    )
    assert 0 < base < ask_gas, "the 63/64 clamp must apply at depth 2"
    forwarded = base - base // 64
    depth2_observed = forwarded - Op.GAS.gas_cost(fork)

    # Top frame: forwards the exact (affordable) depth-1 budget and stores
    # the success flag plus both returned readings.
    entry = pre.deploy_contract(
        code=Op.SSTORE(
            key=flag_slot,
            value=Op.CALL(gas=caller_gas, address=depth1, ret_size=0x40),
        )
        + Op.SSTORE(key=depth2_gas_slot, value=Op.MLOAD(0))
        + Op.SSTORE(key=depth1_gas_slot, value=Op.MLOAD(0x20)),
    )

    post = {
        entry: Account(
            storage={
                flag_slot: 1,
                depth2_gas_slot: depth2_observed,
                depth1_gas_slot: depth1_observed,
            },
        ),
    }

    tx = Transaction(
        sender=pre.fund_eoa(),
        to=entry,
        state_gas_reservoir=0,
    )

    state_test(pre=pre, post=post, tx=tx)
