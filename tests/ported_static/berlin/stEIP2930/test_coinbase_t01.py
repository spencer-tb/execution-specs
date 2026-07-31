"""
Measure the gas cost of a value-transferring CALL to the coinbase from
type-0 and type-1 (EIP-2930 access list) transactions
(by Ori Pomerantz qbzzt1@gmail.com).

Ported from:
state_tests/stEIP2930/coinbaseT01Filler.yml

@manually-enhanced: Do not overwrite. The legacy raw GAS-delta window is
reframed as a CodeGasMeasure over the CALL, asserting the fork-derived
composite (minus the returned stipend); the coinbase is warm from an
access-list entry or EIP-3651 (Shanghai), cold otherwise.
"""

import pytest
from execution_testing import (
    AccessList,
    Account,
    Alloc,
    CodeGasMeasure,
    Environment,
    Fork,
    StateTestFiller,
    Transaction,
)
from execution_testing.forks import Shanghai
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"

GAS_SLOT = 0x0
TRANSFER_VALUE = 1_000_000


@pytest.mark.ported_from(
    ["state_tests/stEIP2930/coinbaseT01Filler.yml"],
)
@pytest.mark.valid_from("Berlin")
@pytest.mark.parametrize(
    "access_list_case",
    ["no_access_list", "coinbase_in_list", "coinbase_not_in_list"],
    ids=["T0", "T1baseInList", "T1baseNotInList"],
)
def test_coinbase_t01(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    access_list_case: str,
) -> None:
    """Measure a value CALL to the coinbase per access-list variant."""
    # The coinbase must exist and be alive, so the value transfer never
    # writes a new account.
    coinbase = pre.fund_eoa(amount=1)
    env = Environment(fee_recipient=coinbase)

    if access_list_case == "no_access_list":
        # A plain type-0 transaction.
        access_list = None
    elif access_list_case == "coinbase_in_list":
        access_list = [AccessList(address=coinbase, storage_keys=[])]
    else:
        # A type-1 transaction whose access list does not warm the
        # coinbase.
        access_list = [
            AccessList(address=pre.nonexistent_account(), storage_keys=[])
        ]

    # EIP-3651 (Shanghai) pre-warms the coinbase; before that it is only
    # warm when the access list names it.
    coinbase_warm = fork >= Shanghai or access_list_case == "coinbase_in_list"
    call_code = Op.CALL(
        address=coinbase,
        value=TRANSFER_VALUE,
        address_warm=coinbase_warm,
        value_transfer=True,
    )
    target = pre.deploy_contract(
        code=CodeGasMeasure(
            code=call_code,
            extra_stack_items=1,
            sstore_key=GAS_SLOT,
        ),
        balance=TRANSFER_VALUE,
    )

    tx = Transaction(
        sender=pre.fund_eoa(),
        to=target,
        access_list=access_list,
        state_gas_reservoir=0,
    )

    # The coinbase consumes nothing, so the stipend handed over with the
    # value comes back unused.
    measured_gas = call_code.gas_cost(fork) - fork.gas_costs().CALL_STIPEND

    post = {target: Account(storage={GAS_SLOT: measured_gas}, balance=0)}

    state_test(env=env, pre=pre, post=post, tx=tx)
