"""
Verify the EIP-150 "all but one 64th" rounding: a subcall asking for more
gas than the transaction holds receives `base - base // 64`, probed with a
base exactly divisible by 64 and one gas either side of it.

Ported from:
state_tests/stEIP150Specific/Transaction64Rule_d64e0Filler.json
state_tests/stEIP150Specific/Transaction64Rule_d64m1Filler.json
state_tests/stEIP150Specific/Transaction64Rule_d64p1Filler.json

@manually-enhanced: Do not overwrite. Three fillers folded into one
parametrize; the callee reports its observed GAS, so the exact forwarded
amount is asserted — `base * 63 // 64` is one gas short whenever the base
is not a multiple of 64, which the ported posts could not see. The gas
limit is fork-derived, so the base keeps its delta on every fork.
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


@pytest.mark.ported_from(
    [
        "state_tests/stEIP150Specific/Transaction64Rule_d64e0Filler.json",
        "state_tests/stEIP150Specific/Transaction64Rule_d64m1Filler.json",
        "state_tests/stEIP150Specific/Transaction64Rule_d64p1Filler.json",
    ],
)
@pytest.mark.valid_from("Berlin")
@pytest.mark.parametrize("delta", [0, -1, 1])
def test_transaction64_rule(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    delta: int,
) -> None:
    """A subcall asking above the tx budget receives `base - base // 64`."""
    gas_slot = 0x1
    oversized_gas_ask = 2**61

    gas_return_contract = pre.deploy_contract(
        code=Op.MSTORE(0, Op.GAS, new_memory_size=0x20) + Op.RETURN(0, 0x20),
    )

    call_code = Op.CALL(
        gas=oversized_gas_ask,
        address=gas_return_contract,
        ret_size=0x20,
        address_warm=False,
        account_new=False,
        new_memory_size=0x20,
    )
    # The only op after the call; the callee's returned surplus covers it.
    store_code = Op.SSTORE(
        key=gas_slot,
        value=Op.MLOAD(0),
        key_warm=False,
        original_value=0,
        new_value=1,
    )
    caller = pre.deploy_contract(code=call_code + store_code + Op.STOP)

    #   gas_limit = intrinsic + call_code + base
    #   base      = base // 64 (kept by the caller) + forwarded
    #
    # `delta` shifts base off a multiple of 64, where `base * 63 // 64`
    # would be one gas short. The +1024 margin covers the trailing store.
    intrinsic = fork.transaction_intrinsic_cost_calculator()()
    min_base = store_code.gas_cost(fork) + 1024
    base = -(-min_base // 64) * 64 + delta
    assert base < oversized_gas_ask, "the 63/64 clamp must apply"
    gas_limit = intrinsic + call_code.gas_cost(fork) + base

    tx = Transaction(
        sender=pre.fund_eoa(),
        to=caller,
        gas_limit=gas_limit,
    )

    # The callee reports the forwarded gas minus its own GAS opcode.
    forwarded = base - base // 64
    expected_gas = forwarded - Op.GAS.gas_cost(fork)

    post = {caller: Account(storage={gas_slot: expected_gas})}

    state_test(pre=pre, post=post, tx=tx)
