"""
Verify a depth-two STATICCALL asking for more gas than its frame holds
is capped to all-but-one-64th and the chain still completes: the static
frames stay read-only, and only the writable depth-one frame records
its writes.

Ported from:
state_tests/stStaticCall/static_CallAskMoreGasOnDepth2ThenTransactionHasFiller.json

@manually-enhanced: Do not overwrite. The ported d0/d1 twin chains were
folded into one chain parametrized on the leaf behavior; addresses are
dynamic and the oversized ask is named and guarded.
"""

import pytest
from execution_testing import (
    Account,
    Alloc,
    Hash,
    StateTestFiller,
    Transaction,
)
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"

# The depth-one frame grants exactly this much to the depth-two frame.
DEPTH1_GAS_ASK = 0x30D40
# The depth-two frame asks for more than its whole grant, so the ask is
# capped to all-but-one-64th of what it has (guarded below).
DEPTH2_GAS_ASK = 0x927C0


@pytest.mark.ported_from(
    [
        "state_tests/stStaticCall/static_CallAskMoreGasOnDepth2ThenTransactionHasFiller.json"  # noqa: E501
    ],
)
@pytest.mark.valid_from("Byzantium")
@pytest.mark.parametrize("leaf_behavior", ["static_violation", "gas_snapshot"])
def test_static_call_ask_more_gas_on_depth2_then_transaction_has(
    state_test: StateTestFiller,
    pre: Alloc,
    leaf_behavior: str,
) -> None:
    """Cap an oversized depth-two gas ask and complete the call chain."""
    assert DEPTH2_GAS_ASK > DEPTH1_GAS_ASK, (
        "the depth-two ask must exceed the frame's whole grant"
    )
    if leaf_behavior == "static_violation":
        # Storage write inside the static context: the leaf frame halts
        # and forfeits its capped grant.
        leaf = pre.deploy_contract(
            code=Op.SSTORE(key=0x8, value=0x1) + Op.STOP
        )
    else:
        # Memory-only gas snapshot: the leaf frame succeeds.
        leaf = pre.deploy_contract(
            code=Op.MSTORE(offset=0x8, value=Op.GAS) + Op.STOP
        )
    depth2 = pre.deploy_contract(
        code=Op.MSTORE(offset=0x8, value=Op.GAS)
        + Op.MSTORE(
            offset=0x9,
            value=Op.STATICCALL(gas=DEPTH2_GAS_ASK, address=leaf),
        )
        + Op.STOP,
    )
    depth1 = pre.deploy_contract(
        code=Op.SSTORE(key=0x8, value=0x1)
        + Op.SSTORE(
            key=0x9,
            value=Op.STATICCALL(gas=DEPTH1_GAS_ASK, address=depth2),
        )
        + Op.STOP,
    )
    target = pre.deploy_contract(
        code=Op.SSTORE(
            key=0x0,
            value=Op.CALL(
                address=Op.CALLDATALOAD(offset=0x0), value=Op.CALLVALUE
            ),
        )
        + Op.SSTORE(key=0x1, value=0x1)
        + Op.STOP,
    )

    tx = Transaction(
        sender=pre.fund_eoa(),
        to=target,
        data=Hash(depth1, left_padding=True),
    )

    # The depth-two frame completes either way (its leaf's failure is
    # invisible to storage), so both writable frames record success.
    post = {
        leaf: Account(storage={}),
        depth2: Account(storage={}),
        depth1: Account(storage={8: 1, 9: 1}),
        target: Account(storage={0: 1, 1: 1}),
    }

    state_test(pre=pre, post=post, tx=tx)
