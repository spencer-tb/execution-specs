"""
Verify environment-probing writes three static frames deep are rolled
back: the probe frame's SSTOREs violate the static context and halt
only that frame, while a memory-only probe succeeds; either way the
enclosing frames complete and record success.

Ported from:
state_tests/stStaticCall/static_callcallcall_000Filler.json

@manually-enhanced: Do not overwrite. The ported d0/d1 twin chains were
folded into one chain parametrized on the probe type; addresses are
dynamic and sub-calls forward all gas.
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


@pytest.mark.ported_from(
    ["state_tests/stStaticCall/static_callcallcall_000Filler.json"],
)
@pytest.mark.valid_from("Byzantium")
@pytest.mark.parametrize("probe_type", ["sstore_probes", "mstore_probe"])
def test_static_callcallcall_000(
    state_test: StateTestFiller,
    pre: Alloc,
    probe_type: str,
) -> None:
    """Roll back environment probes stored inside a static context."""
    if probe_type == "sstore_probes":
        # Every SSTORE violates the static context: the probe frame
        # halts and none of these values persist.
        probe = pre.deploy_contract(
            code=Op.SSTORE(key=0x3, value=0x1)
            + Op.SSTORE(key=0x4, value=Op.CALLER)
            + Op.SSTORE(key=0x7, value=Op.CALLVALUE)
            + Op.SSTORE(key=0x14A, value=Op.ADDRESS)
            + Op.SSTORE(key=0x14C, value=Op.ORIGIN)
            + Op.SSTORE(key=0x150, value=Op.CALLDATASIZE)
            + Op.SSTORE(key=0x152, value=Op.CODESIZE)
            + Op.SSTORE(key=0x154, value=Op.GASPRICE)
            + Op.STOP,
        )
    else:
        # A memory-only probe is legal in a static context.
        probe = pre.deploy_contract(
            code=Op.MSTORE(offset=0x3, value=0x1) + Op.STOP,
        )
    depth3 = pre.deploy_contract(
        code=Op.MSTORE(offset=0x3, value=0x1)
        + Op.POP(Op.STATICCALL(address=probe, args_size=0x40, ret_size=0x40))
        + Op.MSTORE(offset=0x20, value=0x1)
        + Op.STOP,
    )
    depth2 = pre.deploy_contract(
        code=Op.MSTORE(offset=0x3, value=0x1)
        + Op.POP(Op.STATICCALL(address=depth3, args_size=0x40, ret_size=0x40))
        + Op.MSTORE(offset=0x20, value=0x1)
        + Op.STOP,
    )
    depth1 = pre.deploy_contract(
        code=Op.SSTORE(
            key=0x0,
            value=Op.STATICCALL(address=depth2, args_size=0x40, ret_size=0x40),
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

    # The probe frame's failure is invisible one level up: the static
    # middle frames complete either way, so the writable frames record
    # success.
    post = {
        probe: Account(storage={}),
        depth3: Account(storage={}),
        depth2: Account(storage={}),
        depth1: Account(storage={0: 1}),
        target: Account(storage={0: 1, 1: 1}),
    }

    state_test(pre=pre, post=post, tx=tx)
