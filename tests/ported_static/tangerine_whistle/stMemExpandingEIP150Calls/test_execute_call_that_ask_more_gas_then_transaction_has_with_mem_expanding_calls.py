"""
Test_execute_call_that_ask_more_gas_then_transaction_has_with_mem_expand...

Ported from:
state_tests/stMemExpandingEIP150Calls/ExecuteCallThatAskMoreGasThenTransactionHasWithMemExpandingCallsFiller.json

@manually-enhanced: Do not overwrite. Per-era post: pre-EIP-150
(Frontier/Homestead) there is no 63/64 cap, so the oversized gas ask
exceptionally halts the frame and all storage unwinds.
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
from execution_testing.forks import Amsterdam, TangerineWhistle
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


@pytest.mark.ported_from(
    [
        "state_tests/stMemExpandingEIP150Calls/ExecuteCallThatAskMoreGasThenTransactionHasWithMemExpandingCallsFiller.json"  # noqa: E501
    ],
)
@pytest.mark.valid_from("Frontier")
@pytest.mark.pre_alloc_mutable
def test_execute_call_that_ask_more_gas_then_transaction_has_with_mem_expanding_calls(  # noqa: E501
    state_test: StateTestFiller,
    fork: Fork,
    pre: Alloc,
) -> None:
    """Test_execute_call_that_ask_more_gas_then_transaction_has_with_mem_e..."""  # noqa: E501
    coinbase = Address(0x2ADC25665018AA1FE0E6BC666DAC8FC2697FF9BA)
    sender = pre.fund_eoa(amount=0x186A000)

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    # Source: hex
    # 0x600c600155
    addr = pre.deploy_contract(  # noqa: F841
        code=Op.SSTORE(key=0x1, value=0xC),
        balance=0x186A0,
        nonce=0,
    )
    # Source: hex
    # 0x60ff60ff60ff60ff600073<contract:0x1000000000000000000000000000000000000001>620927c0f1600155  # noqa: E501
    target = pre.deploy_contract(  # noqa: F841
        code=Op.SSTORE(
            key=0x1,
            value=Op.CALL(
                gas=0x927C0,
                address=addr,
                value=0x0,
                args_offset=0xFF,
                args_size=0xFF,
                ret_offset=0xFF,
                ret_size=0xFF,
            ),
        ),
        nonce=0,
    )

    tx = Transaction(
        protected=fork.supports_protected_txs(),
        sender=sender,
        to=target,
        data=Bytes(""),
        gas_limit=2100000 if fork >= Amsterdam else 100000,
    )

    if fork >= TangerineWhistle:
        # EIP-150: the oversized 0x927C0 gas ask is capped to 63/64 of
        # the remaining gas, so the call proceeds and succeeds.
        post = {
            sender: Account(nonce=1),
            target: Account(storage={1: 1}),
            addr: Account(storage={1: 12}, balance=0x186A0),
        }
    else:
        # Pre-EIP-150 there is no 63/64 cap: a call asking for more
        # gas than remains exceptionally halts the frame, unwinding
        # all storage writes.
        post = {
            sender: Account(nonce=1),
            target: Account(storage={}),
            addr: Account(storage={}, balance=0x186A0),
        }

    state_test(env=env, pre=pre, post=post, tx=tx)
