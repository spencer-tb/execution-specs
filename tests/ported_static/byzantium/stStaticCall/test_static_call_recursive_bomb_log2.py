"""
Verify a static context defuses a logging recursion bomb: the bomb's
LOG0 violates the static context and halts its frame at depth one, so
the caller observes failure and continues.

Ported from:
state_tests/stStaticCall/static_CallRecursiveBombLog2Filler.json

@manually-enhanced: Do not overwrite. Dropped the pinned 10B gas limit
(which capped validity at Prague) in favor of the maxed default; the
call result is stored +1 so the observed failure is a non-zero value.
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

# Gas each bomb level would keep for its LOG0 and MSTORE (never reached
# past depth one: the LOG0 halts the first static frame).
BOMB_GAS_RESERVE = 0x61A8
# Gas the top frame keeps for its two post-call SSTOREs (guarded below).
TARGET_GAS_RESERVE = 0x186A0


@pytest.mark.ported_from(
    ["state_tests/stStaticCall/static_CallRecursiveBombLog2Filler.json"],
)
@pytest.mark.valid_from("Byzantium")
def test_static_call_recursive_bomb_log2(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """Observe a LOG0 recursion bomb halt inside a static context."""
    addr = pre.deploy_contract(
        code=Op.MSTORE(offset=0x0, value=Op.GAS)
        + Op.LOG0(offset=0x0, size=0x20)
        + Op.STATICCALL(
            gas=Op.SUB(Op.GAS, BOMB_GAS_RESERVE), address=Op.ADDRESS
        )
        + Op.STOP,
    )
    # Store the bomb call's result plus one so the observed failure (a
    # stored 1) is distinguishable from a never-written slot.
    target = pre.deploy_contract(
        code=Op.SSTORE(
            key=0x0,
            value=Op.ADD(
                0x1,
                Op.STATICCALL(
                    gas=Op.SUB(Op.GAS, TARGET_GAS_RESERVE), address=addr
                ),
            ),
        )
        + Op.SSTORE(key=0x1, value=0x1)
        + Op.STOP,
    )

    # The failed bomb frame forfeits its whole grant; the reserve alone
    # must fund the two SSTOREs that record the outcome. Only their
    # execution cost draws on the frame's gas: the maxed transaction
    # (no explicit gas limit) covers any state gas from its reservoir.
    sstore_cost = Op.SSTORE(
        key_warm=False, original_value=0, new_value=1
    ).execution_cost(fork)
    assert TARGET_GAS_RESERVE > 2 * sstore_cost, (
        "the reserve must fund the outcome SSTOREs"
    )

    sender = pre.fund_eoa()
    tx = Transaction(sender=sender, to=target)

    post = {
        target: Account(storage={0: 1, 1: 1}),
        sender: Account(nonce=1),
    }

    state_test(pre=pre, post=post, tx=tx)
