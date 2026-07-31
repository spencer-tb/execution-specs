"""
Verify a nested static frame that fails — by writing storage inside a
static context or by burning its whole grant — leaves the top frame's
1/64 retentions unable to fund its SSTORE, so the top frame runs out of
gas and every write reverts.

Ported from:
state_tests/stStaticCall/static_CallGoesOOGOnSecondLevel2Filler.json

@manually-enhanced: Do not overwrite. Gas budget guarded by fork-derived
asserts (was a pinned 160000); dynamic addresses; d0/d1 renamed to the
leaf behavior they select.
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

# Post-intrinsic execution budget. Small enough that the top frame's
# 1/64 retentions cannot fund an SSTORE (guarded below), large enough to
# reach the depth-three leaf.
GAS_BUDGET = 139_000


@pytest.mark.ported_from(
    ["state_tests/stStaticCall/static_CallGoesOOGOnSecondLevel2Filler.json"],
)
@pytest.mark.valid_from("Byzantium")
@pytest.mark.parametrize("leaf_behavior", ["static_violation", "gas_burner"])
def test_static_call_goes_oog_on_second_level2(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    leaf_behavior: str,
) -> None:
    """Run the top frame out of gas after a nested static frame fails."""
    if leaf_behavior == "static_violation":
        # Storage write inside a static context: exceptional halt that
        # consumes the leaf's whole grant.
        leaf = pre.deploy_contract(
            code=Op.SSTORE(key=0x1, value=0x1) + Op.STOP
        )
    else:
        # EXTCODESIZE loop needing far more gas than any grant here.
        leaf = pre.deploy_contract(
            code=Op.JUMPDEST
            + Op.JUMPI(
                pc=0x1C,
                condition=Op.ISZERO(Op.LT(Op.MLOAD(offset=0x80), 0xC350)),
            )
            + Op.POP(Op.EXTCODESIZE(address=0x1))
            + Op.MSTORE(offset=0x80, value=Op.ADD(Op.MLOAD(offset=0x80), 0x1))
            + Op.JUMP(pc=0x0)
            + Op.JUMPDEST
            + Op.STOP,
        )
    addr = pre.deploy_contract(
        code=Op.MSTORE(offset=0x8, value=Op.GAS)
        + Op.MSTORE(
            offset=0x9,
            value=Op.STATICCALL(address=Op.CALLDATALOAD(offset=0x0)),
        )
        + Op.STOP,
    )
    target = pre.deploy_contract(
        code=Op.MSTORE(offset=0x0, value=Op.CALLDATALOAD(offset=0x0))
        + Op.SSTORE(key=0x0, value=Op.STATICCALL(address=addr, args_size=0x20))
        + Op.SSTORE(key=0x1, value=0x1)
        + Op.STOP,
    )

    # The depth-three frame consumes its whole grant either way; the top
    # frame keeps only its own 1/64 plus the intermediate frame's
    # returned 1/64, which must not fund the first SSTORE.
    sstore_cost = Op.SSTORE(
        key_warm=False, original_value=0, new_value=1
    ).gas_cost(fork)
    assert GAS_BUDGET // 32 + 100 < sstore_cost, (
        "retained gas must not fund the top frame's SSTORE"
    )
    gas_limit = fork.transaction_intrinsic_cost_calculator()() + GAS_BUDGET

    tx = Transaction(
        sender=pre.fund_eoa(),
        to=target,
        data=Hash(leaf, left_padding=True),
        gas_limit=gas_limit,
    )

    post = {
        leaf: Account(storage={}),
        target: Account(storage={}),
    }

    state_test(pre=pre, post=post, tx=tx)
