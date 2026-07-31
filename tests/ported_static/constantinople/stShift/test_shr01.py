"""
Taken from https://github.com/ethereum/EIPs/blob/master/EIPS/eip-145.md.

Ported from:
state_tests/stShift/shr01Filler.json
"""

import pytest
from execution_testing import (
    Account,
    Address,
    Alloc,
    Bytes,
    Environment,
    Fork,
    StateTestFiller,
    Transaction,
)
from execution_testing.forks import Constantinople
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


@pytest.mark.ported_from(
    ["state_tests/stShift/shr01Filler.json"],
)
@pytest.mark.valid_from("Frontier")
@pytest.mark.pre_alloc_mutable
def test_shr01(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """Taken from https://github."""
    coinbase = Address(0x2ADC25665018AA1FE0E6BC666DAC8FC2697FF9BA)
    sender = pre.fund_eoa(amount=0xDE0B6B3A7640000)

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    # Source: raw
    # 0x600060011c600055
    target = pre.deploy_contract(  # noqa: F841
        code=Op.SSTORE(key=0x0, value=Op.SHR(0x1, 0x0)),
        storage={0: 3},
        balance=0xDE0B6B3A7640000,
        nonce=0,
    )

    tx = Transaction(
        protected=fork.supports_protected_txs(),
        sender=sender,
        to=target,
        data=Bytes(""),
        gas_limit=400000,
        value=0x186A0,
    )

    if fork >= Constantinople:
        post = {
            target: Account(storage={0: 0}, balance=0xDE0B6B3A76586A0),
            sender: Account(storage={}, code=b"", nonce=1),
        }
    else:
        # The subject opcode is undefined before Constantinople: the
        # frame fails, the value transfer unwinds, and the
        # pre-state storage persists.
        post = {
            target: Account(storage={0: 3}, balance=0xDE0B6B3A7640000),
            sender: Account(storage={}, code=b"", nonce=1),
        }

    state_test(env=env, pre=pre, post=post, tx=tx)
