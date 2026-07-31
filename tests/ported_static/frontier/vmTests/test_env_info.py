"""
Verify environment-info opcodes as seen by a called contract.

Ported from:
state_tests/VMTests/vmTests/envInfoFiller.yml

@manually-enhanced: Do not overwrite. Hardcoded addresses and the
calldata-indexed dispatch were dropped; each case deploys its own target
and caller pair and derives the expectation (own code bytes, code size,
caller address, gas price) instead of pinning constants. Zero-result
CODECOPY and CALLDATASIZE cases store result + 1 so a zero read is
distinguishable from a skipped store.
"""

import pytest
from execution_testing import (
    Account,
    Alloc,
    Bytecode,
    Bytes,
    Fork,
    Hash,
    StateTestFiller,
    Transaction,
)
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"

VALUE_SLOT = 0x0
CALL_VALUE = 0x10
GAS_PRICE = 0x1234
# Explicit sub-call budget: asking for more gas than is available would
# abort the CALL on pre-EIP-150 forks, so the caller must not forward all.
DISPATCH_GAS = 100_000
CODECOPY_SIZE = 0x7
# Offset so high it would wrap around if treated as a signed/modular
# index (-6 mod 2**256).
HUGE_OFFSET = 2**256 - 6


@pytest.mark.ported_from(
    ["state_tests/VMTests/vmTests/envInfoFiller.yml"],
)
@pytest.mark.valid_from("Frontier")
@pytest.mark.parametrize(
    "case",
    [
        "address",
        "codecopy",
        "codecopy_len0",
        "codecopy_neg_offset",
        "caller",
        "callvalue",
        "codesize",
        "gasprice",
        "origin",
        "calldatasize",
    ],
)
def test_env_info(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    case: str,
) -> None:
    """Store one environment-info observable in the called contract."""
    code: Bytecode
    if case == "address":
        code = Op.SSTORE(key=VALUE_SLOT, value=Op.ADDRESS) + Op.STOP
    elif case == "codecopy":
        # Copy the contract's own first bytes to memory, then to storage.
        code = (
            Op.CODECOPY(dest_offset=0x0, offset=0x0, size=CODECOPY_SIZE)
            + Op.SSTORE(key=VALUE_SLOT, value=Op.MLOAD(offset=0x0))
            + Op.STOP
        )
    elif case == "codecopy_len0":
        code = (
            Op.CODECOPY(dest_offset=0x0, offset=0x0, size=0x0)
            + Op.SSTORE(key=VALUE_SLOT, value=Op.ADD(Op.MLOAD(offset=0x0), 1))
            + Op.STOP
        )
    elif case == "codecopy_neg_offset":
        code = (
            Op.CODECOPY(dest_offset=0x0, offset=HUGE_OFFSET, size=0x8)
            + Op.SSTORE(key=VALUE_SLOT, value=Op.ADD(Op.MLOAD(offset=0x0), 1))
            + Op.STOP
        )
    elif case == "caller":
        code = Op.SSTORE(key=VALUE_SLOT, value=Op.CALLER) + Op.STOP
    elif case == "callvalue":
        code = Op.SSTORE(key=VALUE_SLOT, value=Op.CALLVALUE) + Op.STOP
    elif case == "codesize":
        code = Op.SSTORE(key=VALUE_SLOT, value=Op.CODESIZE) + Op.STOP
    elif case == "gasprice":
        code = Op.SSTORE(key=VALUE_SLOT, value=Op.GASPRICE) + Op.STOP
    elif case == "origin":
        code = Op.SSTORE(key=VALUE_SLOT, value=Op.ORIGIN) + Op.STOP
    else:  # calldatasize
        # The caller forwards no calldata, unlike the transaction itself.
        code = (
            Op.SSTORE(key=VALUE_SLOT, value=Op.ADD(Op.CALLDATASIZE, 1))
            + Op.STOP
        )

    target = pre.deploy_contract(code=code)
    caller = pre.deploy_contract(
        code=Op.CALL(gas=DISPATCH_GAS, address=target, value=CALL_VALUE)
        + Op.STOP,
        balance=CALL_VALUE,
    )
    sender = pre.fund_eoa()

    tx = Transaction(
        protected=fork.supports_protected_txs(),
        sender=sender,
        to=caller,
        # Non-empty tx calldata, so the empty forwarded calldata observed
        # by the target (calldatasize case) is a real truncation.
        data=Bytes("693c6139"),
        gas_price=GAS_PRICE,
    )

    expected: int | bytes
    if case == "address":
        expected = target
    elif case == "codecopy":
        expected = Hash(bytes(code)[:CODECOPY_SIZE].ljust(32, b"\x00"))
    elif case in ("codecopy_len0", "codecopy_neg_offset", "calldatasize"):
        expected = 1
    elif case == "caller":
        expected = caller
    elif case == "callvalue":
        expected = CALL_VALUE
    elif case == "codesize":
        expected = len(bytes(code))
    elif case == "gasprice":
        expected = GAS_PRICE
    else:  # origin
        expected = sender

    post = {target: Account(storage={VALUE_SLOT: expected})}

    state_test(pre=pre, post=post, tx=tx)
