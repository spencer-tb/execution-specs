"""
Verify gas accounting when a contract calls itself twice and each inner
frame self-destructs with the contract as its own beneficiary: the balance
survives, and the sender pays the executed gas minus the capped refund.

Ported from:
state_tests/stRefundTest/refund_multimpleSuicideFiller.json

@manually-enhanced: Do not overwrite. The compiled Solidity dispatcher
(with its SUB(GAS, ...) forwarding and pinned sender balance) was rewritten
as a minimal calldata-dispatched double self-call; the sender balance,
refund cap and budget derive from fork composites and the post branches on
EIP-6780 for the contract's survival.
"""

import pytest
from execution_testing import (
    Account,
    Alloc,
    Bytes,
    Fork,
    StateTestFiller,
    Transaction,
)
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"

TARGET_BALANCE = 0xDE0B6B3A7640000
INITIAL_BALANCE = 10**18
GAS_PRICE = 10
FIRST_FLAG_SLOT = 0xA
SECOND_FLAG_SLOT = 0xB
# Any non-empty calldata selects the outer (double self-call) path.
RUN_SELECTOR = Bytes("c0406226")


@pytest.mark.ported_from(
    ["state_tests/stRefundTest/refund_multimpleSuicideFiller.json"],
)
@pytest.mark.valid_from("London")
def test_refund_multimple_suicide(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """Self-destruct to self twice; derive the gas accounting."""
    # The dispatch runs in all three frames: taken with calldata (outer),
    # not taken without (both inner). Both directions cost the same.
    kill_code = Op.SELFDESTRUCT(
        address=Op.CALLER, address_warm=True, account_new=False
    )
    run_pc = len(bytes(Op.JUMPI(pc=0, condition=Op.CALLDATASIZE))) + len(
        bytes(kill_code)
    )
    dispatch_code = Op.JUMPI(pc=run_pc, condition=Op.CALLDATASIZE)
    run_code = (
        Op.JUMPDEST
        + Op.SSTORE(
            key=FIRST_FLAG_SLOT,
            value=Op.CALL(address=Op.ADDRESS, address_warm=True),
            key_warm=False,
            original_value=0,
            new_value=1,
        )
        + Op.SSTORE(
            key=SECOND_FLAG_SLOT,
            value=Op.CALL(address=Op.ADDRESS, address_warm=True),
            key_warm=False,
            original_value=0,
            new_value=1,
        )
        + Op.STOP
    )
    target = pre.deploy_contract(
        code=dispatch_code + kill_code + run_code,
        balance=TARGET_BALANCE,
    )

    # The refund cap is a fifth of the gas actually deducted before
    # execution, which excludes the EIP-7623 calldata floor.
    intrinsic = fork.transaction_intrinsic_cost_calculator()(
        calldata=RUN_SELECTOR, return_cost_deducted_prior_execution=True
    )
    body_cost = (
        3 * dispatch_code.gas_cost(fork)
        + 2 * kill_code.gas_cost(fork)
        + run_code.gas_cost(fork)
    )
    executed = intrinsic + body_cost
    gas_limit = executed + 5_000

    sender = pre.fund_eoa(amount=INITIAL_BALANCE)
    tx = Transaction(
        protected=fork.supports_protected_txs(),
        sender=sender,
        to=target,
        data=RUN_SELECTOR,
        gas_limit=gas_limit,
        gas_price=GAS_PRICE,
    )

    # EIP-3529 caps the refund at a fifth of the executed gas. The
    # self-destruct refund (zero from London on) is counted once per
    # account, not once per SELFDESTRUCT.
    refund = min(kill_code.refund(fork), executed // 5)
    gas_used = executed - refund

    post = {
        # EIP-6780: the pre-existing contract survives its self-destructs
        # and, as its own beneficiary, keeps its balance. Before it, the
        # account is deleted and the self-sent balance burned with it.
        target: (
            Account(
                balance=TARGET_BALANCE,
                storage={FIRST_FLAG_SLOT: 1, SECOND_FLAG_SLOT: 1},
            )
            if fork.is_eip_enabled(6780)
            else Account.NONEXISTENT
        ),
        sender: Account(balance=INITIAL_BALANCE - gas_used * GAS_PRICE),
    }

    state_test(pre=pre, post=post, tx=tx)
