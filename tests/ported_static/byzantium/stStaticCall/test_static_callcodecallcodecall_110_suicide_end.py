"""
Measure the gas consumed by a DELEGATECALL-DELEGATECALL-STATICCALL
chain that ends in a SELFDESTRUCT of the shared context account: under
EIP-6780 the pre-existing account survives, its balance moves to the
beneficiary, and the chain's cost is exactly the sum of each frame's
charges — independent of the transaction value, which delegate calls
carry without transferring.

Ported from:
state_tests/stStaticCall/static_callcodecallcodecall_110_SuicideEndFiller.json

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
        "state_tests/stStaticCall/static_callcodecallcodecall_110_SuicideEndFiller.json"  # noqa: E501
    ],
)
@pytest.mark.valid_from("Cancun")
@pytest.mark.parametrize("tx_value", [0, 1])
def test_static_callcodecallcodecall_110_suicide_end(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    tx_value: int,
) -> None:
    """Measure a nested DELEGATECALL chain ending in SELFDESTRUCT."""
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

    # Middle delegate (target's context): DELEGATECALL the innermost.
    mid_code = (
        Op.DELEGATECALL(
            address=inner,
            args_size=0x40,
            ret_size=0x40,
            new_memory_size=0x40,
        )
        + Op.STOP
    )
    mid = pre.deploy_contract(code=mid_code)

    # The measured window: flag-storing DELEGATECALL into the chain.
    # The SSTORE keeps the chain's success observable in the window.
    store_code = Op.SSTORE(
        FLAG_SLOT,
        Op.DELEGATECALL(
            address=mid,
            args_size=0x40,
            ret_size=0x40,
            new_memory_size=0x40,
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
    # frame's actual charges; delegate calls move no value, so nothing
    # here depends on the transaction value.
    expected_gas = (
        store_code.gas_cost(fork)
        + mid_code.gas_cost(fork)
        + inner_code.gas_cost(fork)
        + leaf_code.gas_cost(fork)
    )

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
