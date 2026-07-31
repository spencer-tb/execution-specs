"""
Verify SELFBALANCE inside CALL, DELEGATECALL, and CALLCODE contexts.

Ported from:
state_tests/stSelfBalance/selfBalanceCallTypesFiller.json

@manually-enhanced: Do not overwrite. The jump-table dispatcher is
replaced by a parametrize over the call opcode, the raw GAS-delta probe
by a CodeGasMeasure asserting `Op.SELFBALANCE.gas_cost(fork)`, and the
posts by relationships on the executing context's balance.
"""

import pytest
from execution_testing import (
    Account,
    Alloc,
    Bytecode,
    CodeGasMeasure,
    Fork,
    StateTestFiller,
    Transaction,
)
from execution_testing.vm import Op, Opcode

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"

# Storage slots written by the four probe contracts.
EQ_SLOT = 0x11
BALANCE_SLOT = 0x21
GAS_SLOT = 0x31
BEFORE_SLOT = 0x41
AFTER_SLOT = 0x42
DIFF_SLOT = 0x43

# Distinct balances so a probe reading the wrong context is visible.
EQ_PROBE_BALANCE = 4096
BALANCE_PROBE_BALANCE = 4352
GAS_PROBE_BALANCE = 4608
TRANSFER_PROBE_BALANCE = 4864
TARGET_BALANCE = 8192
# The transfer probe sends this from the executing context.
TRANSFER_VALUE = 1


@pytest.mark.ported_from(
    ["state_tests/stSelfBalance/selfBalanceCallTypesFiller.json"],
)
@pytest.mark.valid_from("Istanbul")
@pytest.mark.parametrize(
    "call_op",
    [Op.CALL, Op.DELEGATECALL, Op.CALLCODE],
    ids=["call", "delegatecall", "callcode"],
)
def test_self_balance_call_types(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    call_op: Opcode,
) -> None:
    """Verify SELFBALANCE reads the executing context in each call type."""
    # Probe 1: SELFBALANCE must equal BALANCE of the current address.
    eq_probe = pre.deploy_contract(
        code=Op.SSTORE(
            key=EQ_SLOT,
            value=Op.EQ(Op.SELFBALANCE, Op.BALANCE(address=Op.ADDRESS)),
        )
        + Op.STOP,
        balance=EQ_PROBE_BALANCE,
    )
    # Probe 2: store the raw SELFBALANCE reading.
    balance_probe = pre.deploy_contract(
        code=Op.SSTORE(key=BALANCE_SLOT, value=Op.SELFBALANCE) + Op.STOP,
        balance=BALANCE_PROBE_BALANCE,
    )
    # Probe 3: measure the gas SELFBALANCE consumes.
    gas_probe = pre.deploy_contract(
        code=CodeGasMeasure(
            code=Op.SELFBALANCE,
            extra_stack_items=1,
            sstore_key=GAS_SLOT,
        ),
        balance=GAS_PROBE_BALANCE,
    )
    # Probe 4: SELFBALANCE must track a value transfer out of the
    # executing context (a zero-gas CALL that sends one wei).
    transfer_probe = pre.deploy_contract(
        code=Op.SELFBALANCE
        + Op.SSTORE(key=BEFORE_SLOT, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x0, address=0x0, value=TRANSFER_VALUE))
        + Op.SELFBALANCE
        + Op.SSTORE(key=AFTER_SLOT, value=Op.DUP1)
        + Op.SWAP1
        + Op.SSTORE(key=DIFF_SLOT, value=Op.SUB)
        + Op.STOP,
        balance=TRANSFER_PROBE_BALANCE,
    )

    probes = [eq_probe, balance_probe, gas_probe, transfer_probe]
    target_code = Bytecode()
    for probe in probes:
        target_code += Op.POP(call_op(address=probe))
    target = pre.deploy_contract(
        code=target_code + Op.STOP,
        balance=TARGET_BALANCE,
    )

    tx = Transaction(sender=pre.fund_eoa(), to=target)

    # A plain CALL runs each probe in its own context; DELEGATECALL and
    # CALLCODE run the probe code in the target's context, so every slot
    # lands in the target's storage and SELFBALANCE reads its balance.
    selfbalance_gas = Op.SELFBALANCE.gas_cost(fork)
    if call_op == Op.CALL:
        post = {
            eq_probe: Account(balance=EQ_PROBE_BALANCE, storage={EQ_SLOT: 1}),
            balance_probe: Account(
                balance=BALANCE_PROBE_BALANCE,
                storage={BALANCE_SLOT: BALANCE_PROBE_BALANCE},
            ),
            gas_probe: Account(
                balance=GAS_PROBE_BALANCE,
                storage={GAS_SLOT: selfbalance_gas},
            ),
            transfer_probe: Account(
                balance=TRANSFER_PROBE_BALANCE - TRANSFER_VALUE,
                storage={
                    BEFORE_SLOT: TRANSFER_PROBE_BALANCE,
                    AFTER_SLOT: TRANSFER_PROBE_BALANCE - TRANSFER_VALUE,
                    DIFF_SLOT: TRANSFER_VALUE,
                },
            ),
            target: Account(balance=TARGET_BALANCE, storage={}),
        }
    else:
        post = {
            eq_probe: Account(balance=EQ_PROBE_BALANCE, storage={}),
            balance_probe: Account(balance=BALANCE_PROBE_BALANCE, storage={}),
            gas_probe: Account(balance=GAS_PROBE_BALANCE, storage={}),
            transfer_probe: Account(
                balance=TRANSFER_PROBE_BALANCE, storage={}
            ),
            target: Account(
                balance=TARGET_BALANCE - TRANSFER_VALUE,
                storage={
                    EQ_SLOT: 1,
                    BALANCE_SLOT: TARGET_BALANCE,
                    GAS_SLOT: selfbalance_gas,
                    BEFORE_SLOT: TARGET_BALANCE,
                    AFTER_SLOT: TARGET_BALANCE - TRANSFER_VALUE,
                    DIFF_SLOT: TRANSFER_VALUE,
                },
            ),
        }

    state_test(pre=pre, post=post, tx=tx)
