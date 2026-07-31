"""
Verify a failure deep inside a CALLCODE-DELEGATECALL chain — a gas
burner exhausting its grant after a static call, or a storage write
inside a static context — is absorbed where it happens: the enclosing
frames complete and the outer frame's constant stores overwrite the
delegated frame's records.

Ported from:
state_tests/stStaticCall/static_callcodecallcallcode_101_OOGMAfter_3Filler.json

@manually-enhanced: Do not overwrite. Dropped the pinned 172000 budget
and its EIP-8037 top-up for the maxed default (the failing frames are
bounded by their fixed asks, now named and guarded); the d0/d1 chains
share their common contracts; addresses are dynamic.
"""

import pytest
from execution_testing import (
    Account,
    Alloc,
    Fork,
    Hash,
    StateTestFiller,
    Transaction,
)
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"

# Grant to the delegated frame below the entry: bounds the gas burner.
DELEGATE_GAS_ASK = 0xEAF6
# Grant to the static frame in the middle of the chain.
STATIC_GAS_ASK = 0x9C90
# Grant to the innermost delegate call.
LEAF_GAS_ASK = 0x4E34
# The gas burner loops this many EXTCODESIZE probes.
BURNER_ITERATIONS = 0xC350


@pytest.mark.ported_from(
    [
        "state_tests/stStaticCall/static_callcodecallcallcode_101_OOGMAfter_3Filler.json"  # noqa: E501
    ],
)
@pytest.mark.valid_from("Byzantium")
@pytest.mark.parametrize(
    "failure_mode", ["oog_after_static", "static_violation"]
)
def test_static_callcodecallcallcode_101_oogm_after_3(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    failure_mode: str,
) -> None:
    """Absorb a deep frame failure and overwrite its context writes."""
    if failure_mode == "oog_after_static":
        # The leaf is memory-only, so the static branch succeeds; the
        # burner after it exhausts the delegated frame's whole grant.
        leaf = pre.deploy_contract(
            code=Op.MSTORE(offset=0x3, value=0x1) + Op.STOP
        )
    else:
        # The leaf is delegate-called inside a static context, so its
        # SSTORE is a violation that halts only the leaf frame.
        leaf = pre.deploy_contract(
            code=Op.SSTORE(key=0x3, value=0x1) + Op.STOP
        )
    static_callee = pre.deploy_contract(
        code=Op.POP(
            Op.DELEGATECALL(
                gas=LEAF_GAS_ASK,
                address=leaf,
                args_size=0x40,
                ret_size=0x40,
            )
        )
        + Op.MSTORE(offset=0x3, value=0x1)
        + Op.STOP,
    )
    if failure_mode == "oog_after_static":
        # Static call, then an EXTCODESIZE loop far exceeding the
        # frame's grant (guarded below): the delegated frame OOGs.
        delegated = pre.deploy_contract(
            code=Op.POP(
                Op.STATICCALL(
                    gas=STATIC_GAS_ASK,
                    address=static_callee,
                    args_size=0x40,
                    ret_size=0x40,
                )
            )
            + Op.JUMPDEST
            + Op.JUMPI(
                pc=0x3E,
                condition=Op.ISZERO(
                    Op.LT(Op.MLOAD(offset=0x80), BURNER_ITERATIONS)
                ),
            )
            + Op.POP(Op.EXTCODESIZE(address=0x1))
            + Op.MSTORE(offset=0x80, value=Op.ADD(Op.MLOAD(offset=0x80), 0x1))
            + Op.JUMP(pc=0x22)
            + Op.JUMPDEST
            + Op.STOP,
        )
    else:
        # The static call absorbs the leaf's violation; this frame
        # completes.
        delegated = pre.deploy_contract(
            code=Op.STATICCALL(
                gas=STATIC_GAS_ASK,
                address=static_callee,
                args_size=0x40,
                ret_size=0x40,
            )
            + Op.STOP,
        )
    burner_cost = BURNER_ITERATIONS * Op.EXTCODESIZE(address=0x1).gas_cost(
        fork
    )
    assert DELEGATE_GAS_ASK < burner_cost, "the burner must exhaust its grant"
    # Entry code, run in the target's context: records the delegated
    # call's result and a gas snapshot, both overwritten by the target.
    entry = pre.deploy_contract(
        code=Op.SSTORE(
            key=0x0,
            value=Op.DELEGATECALL(
                gas=DELEGATE_GAS_ASK,
                address=delegated,
                args_size=0x40,
                ret_size=0x40,
            ),
        )
        + Op.SSTORE(key=0x1, value=Op.GAS)
        + Op.STOP,
    )
    target = pre.deploy_contract(
        code=Op.SSTORE(
            key=0x0,
            value=Op.CALLCODE(address=Op.CALLDATALOAD(offset=0x0), value=0x0),
        )
        + Op.SSTORE(key=0x1, value=0x1)
        + Op.STOP,
    )

    tx = Transaction(
        sender=pre.fund_eoa(),
        to=target,
        data=Hash(entry, left_padding=True),
    )

    # Whatever the delegated chain recorded in the target's slots, the
    # outer frame's constant stores overwrite it.
    post = {
        leaf: Account(storage={}),
        static_callee: Account(storage={}),
        target: Account(storage={0: 1, 1: 1}),
    }

    state_test(pre=pre, post=post, tx=tx)
