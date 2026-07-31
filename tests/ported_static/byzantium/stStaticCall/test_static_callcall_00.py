"""
Verify environment-probing writes two static frames deep are rolled
back: the probe frame's SSTOREs violate the static context and halt
only that frame, while memory-only probes succeed; either way the
enclosing frames complete and record success.

Ported from:
state_tests/stStaticCall/static_callcall_00Filler.json

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
    ["state_tests/stStaticCall/static_callcall_00Filler.json"],
)
@pytest.mark.valid_from("Byzantium")
@pytest.mark.parametrize("probe_type", ["sstore_probes", "mstore_probes"])
def test_static_callcall_00(
    state_test: StateTestFiller,
    pre: Alloc,
    probe_type: str,
) -> None:
    """Roll back environment probes stored inside a static context."""
    if probe_type == "sstore_probes":
        # Every SSTORE violates the static context: the probe frame
        # halts and none of these values persist.
        probe = pre.deploy_contract(
            code=Op.SSTORE(key=0x2, value=0x1)
            + Op.SSTORE(key=0x4, value=Op.CALLER)
            + Op.SSTORE(key=0x7, value=Op.CALLVALUE)
            + Op.SSTORE(key=0xE6, value=Op.ADDRESS)
            + Op.SSTORE(key=0xE8, value=Op.ORIGIN)
            + Op.SSTORE(key=0xEC, value=Op.CALLDATASIZE)
            + Op.SSTORE(key=0xEE, value=Op.CODESIZE)
            + Op.SSTORE(key=0xF0, value=Op.GASPRICE)
            + Op.STOP,
        )
    else:
        # Memory-only probes are legal in a static context.
        probe = pre.deploy_contract(
            code=Op.MSTORE(offset=0x0, value=0x1)
            + Op.MSTORE(offset=0x20, value=Op.CALLER)
            + Op.MSTORE(offset=0x40, value=Op.CALLVALUE)
            + Op.MSTORE(offset=0x60, value=Op.ADDRESS)
            + Op.MSTORE(offset=0x80, value=Op.ORIGIN)
            + Op.MSTORE(offset=0xA0, value=Op.CALLDATASIZE)
            + Op.MSTORE(offset=0xC0, value=Op.CODESIZE)
            + Op.MSTORE(offset=0xE0, value=Op.GASPRICE)
            + Op.STOP,
        )
    depth2 = pre.deploy_contract(
        code=Op.STATICCALL(address=probe, args_size=0x40, ret_size=0x40)
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

    # The probe frame's failure is invisible one level up: depth2
    # completes either way, so the writable frames record success.
    post = {
        probe: Account(storage={}),
        depth2: Account(storage={}),
        depth1: Account(storage={0: 1}),
        target: Account(storage={0: 1, 1: 1}),
    }

    state_test(pre=pre, post=post, tx=tx)
