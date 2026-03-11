"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRevertTest
LoopDelegateCallsDepthThenRevertFiller.json
"""

import pytest
from execution_testing import (
    Account,
    Address,
    Alloc,
    Environment,
    Hash,
    StateTestFiller,
    Transaction,
)
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


@pytest.mark.ported_from(
    [
        "tests/static/state_tests/stRevertTest/LoopDelegateCallsDepthThenRevertFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_loop_delegate_calls_depth_then_revert(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xfaa10b404ab607779993c016cd5da73ae1f29d7e")
    contract = Address("0xb0923c4a632de291fcdac653e6c6cc2b4e4cdfa8")
    callee = Address("0xf798cb78490da31dfacdcd1f2b3fb1948bb2b228")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000,
    )

    # Source: LLL
    # { [[0]] (+ (SLOAD 0) 1) (DELEGATECALL (GAS) <contract:0xb000000000000000000000000000000000000000> 0 0 0 0) }  # noqa: E501
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=Op.ADD(Op.SLOAD(key=0x0), 0x1))
            + Op.DELEGATECALL(
                gas=Op.GAS,
                address=0xF798CB78490DA31DFACDCD1F2B3FB1948BB2B228,
                args_offset=0x0,
                args_size=0x0,
                ret_offset=0x0,
                ret_size=0x0,
            )
            + Op.STOP
        ),
    )
    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=Op.ADD(Op.SLOAD(key=0x0), 0x1))
            + Op.DELEGATECALL(
                gas=Op.GAS,
                address=0xB0923C4A632DE291FCDAC653E6C6CC2B4E4CDFA8,
                args_offset=0x0,
                args_size=0x0,
                ret_offset=0x0,
                ret_size=0x0,
            )
            + Op.STOP
        ),
    )
    pre[sender] = Account(balance=0xE8D4A51000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x4f31b3206fbf0e0e598b9b1a7d8ac86302a0ff1d8930738f1bebae9b67173e52"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=10000000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            storage={0: 386},
            code=(
                Op.SSTORE(key=0x0, value=Op.ADD(Op.SLOAD(key=0x0), 0x1))
                + Op.DELEGATECALL(
                    gas=Op.GAS,
                    address=0xF798CB78490DA31DFACDCD1F2B3FB1948BB2B228,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                )
                + Op.STOP
            ),
        ),
        callee: Account(
            code=(
                Op.SSTORE(key=0x0, value=Op.ADD(Op.SLOAD(key=0x0), 0x1))
                + Op.DELEGATECALL(
                    gas=Op.GAS,
                    address=0xB0923C4A632DE291FCDAC653E6C6CC2B4E4CDFA8,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                )
                + Op.STOP
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
