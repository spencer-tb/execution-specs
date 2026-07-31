"""
Measure the gas consumed by a CALLCODE-CALLCODE-STATICCALL chain that
ends in a SELFDESTRUCT of the shared context account: under EIP-6780
the pre-existing account survives, its balance moves to the
beneficiary, and the chain's cost is exactly the sum of each frame's
charges (minus the returned stipends when value is sent).

Ported from:
state_tests/stStaticCall/static_callcodecallcodecall_110_SuicideEnd2Filler.json

@manually-enhanced: Do not overwrite. The ported absolute GAS snapshot
(slot 1) became a CodeGasMeasure delta asserted against fork-derived
frame costs; the SELFDESTRUCT beneficiary is the (warm) static leaf so
every address is dynamic, and its balance is asserted.
"""

import pytest
from execution_testing import (
    Account,
    Alloc,
    CodeGasMeasure,
    Fork,
    StateTestFiller,
    Transaction,
)
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"

FLAG_SLOT = 0x0
GAS_SLOT = 0x1
TARGET_BALANCE = 10**18


@pytest.mark.ported_from(
    [
        "state_tests/stStaticCall/static_callcodecallcodecall_110_SuicideEnd2Filler.json"  # noqa: E501
    ],
)
@pytest.mark.valid_from("Cancun")
@pytest.mark.parametrize("tx_value", [0, 1])
def test_static_callcodecallcodecall_110_suicide_end2(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    tx_value: int,
) -> None:
    """Measure a nested CALLCODE chain ending in SELFDESTRUCT."""
    sends_value = tx_value > 0

    # Static leaf: memory-only, runs in its own frame.
    leaf_code = Op.MSTORE(offset=0x3, value=0x1, new_memory_size=0x23)
    leaf = pre.deploy_contract(code=leaf_code + Op.STOP)

    # Innermost delegate (target's context): static-call the leaf, then
    # self-destruct the context account. The beneficiary is the leaf —
    # warm from the call just made, and deployable without the address
    # circularity of the ported layout (which paid the same warm-access
    # cost for the mid-chain delegate).
    inner_code = Op.POP(
        Op.STATICCALL(
            address=leaf,
            args_size=0x40,
            ret_size=0x40,
            new_memory_size=0x40,
        )
    ) + Op.SELFDESTRUCT(address=leaf, address_warm=True)
    inner = pre.deploy_contract(code=inner_code)

    # Middle delegate (target's context): CALLCODE into the innermost.
    mid_code = (
        Op.CALLCODE(
            address=inner,
            value=Op.CALLVALUE,
            args_size=0x40,
            ret_size=0x40,
            new_memory_size=0x40,
            value_transfer=sends_value,
        )
        + Op.STOP
    )
    mid = pre.deploy_contract(code=mid_code)

    # The measured window: flag-storing CALLCODE into the chain. The
    # SSTORE keeps the chain's success observable inside the window.
    store_code = Op.SSTORE(
        FLAG_SLOT,
        Op.CALLCODE(
            address=mid,
            value=Op.CALLVALUE,
            args_size=0x40,
            ret_size=0x40,
            new_memory_size=0x40,
            value_transfer=sends_value,
        ),
        key_warm=False,
        original_value=0,
        new_value=1,
    )
    target = pre.deploy_contract(
        code=CodeGasMeasure(
            code=store_code,
            extra_stack_items=0,
            sstore_key=GAS_SLOT,
        ),
        balance=TARGET_BALANCE,
    )

    tx = Transaction(
        sender=pre.fund_eoa(),
        to=target,
        value=tx_value,
        state_gas_reservoir=0,
    )

    # Every frame succeeds, so the window measures the sum of each
    # frame's actual charges; each value-bearing hop's callee returns
    # its unused 2300 stipend, shaving it off the measurement.
    expected_gas = (
        store_code.gas_cost(fork)
        + mid_code.gas_cost(fork)
        + inner_code.gas_cost(fork)
        + leaf_code.gas_cost(fork)
    )
    if sends_value:
        expected_gas -= 2 * fork.gas_costs().CALL_STIPEND

    # EIP-6780: the pre-existing target survives its self-destruct; its
    # whole balance (including the transaction value) moved to the leaf.
    post = {
        target: Account(
            balance=0,
            storage={FLAG_SLOT: 1, GAS_SLOT: expected_gas},
        ),
        leaf: Account(
            balance=TARGET_BALANCE + tx_value,
            storage={},
        ),
    }

    state_test(pre=pre, post=post, tx=tx)
