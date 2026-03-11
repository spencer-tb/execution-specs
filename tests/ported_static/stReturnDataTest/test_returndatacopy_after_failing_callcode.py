"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stReturnDataTest
returndatacopy_after_failing_callcodeFiller.json
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
        "tests/static/state_tests/stReturnDataTest/returndatacopy_after_failing_callcodeFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_returndatacopy_after_failing_callcode(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xc102734f6a1e4747310179c0a0fc16e674aa901d")
    contract = Address("0x24878b81dd27c2d76258b421acddf26835bc1484")
    callee = Address("0x285d0814904bebb3b4add3b531a07647c2d08f59")
    callee_1 = Address("0x665521fd750490fd880ee369c267fca44ed8a078")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=111669149696,
    )

    # Source: LLL
    # {  (CALLCODE 0 <contract:0x1000000000000000000000000000000000000002> 0 0 0 0 0) (RETURNDATACOPY 0x0 0x0 32) (SSTORE 0 (MLOAD 0))}  # noqa: E501
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.POP(
                Op.CALLCODE(
                    gas=0x0,
                    address=0x665521FD750490FD880EE369C267FCA44ED8A078,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.RETURNDATACOPY(dest_offset=0x0, offset=0x0, size=0x20)
            + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
            + Op.STOP
        ),
        storage={0x0: 0xFFFFFFFFFFFF},
    )
    pre[callee] = Account(balance=0x10000000, nonce=0)
    # Source: raw bytecode
    pre[callee_1] = Account(balance=0x6400000000, nonce=0, code=Op.REVERT)
    pre[sender] = Account(balance=0x6400000000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x834185262e53584684bf2b72c64e510013c235d0f45e462db65900455df45a35"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            storage={0: 0xFFFFFFFFFFFF},
            code=(
                Op.POP(
                    Op.CALLCODE(
                        gas=0x0,
                        address=0x665521FD750490FD880EE369C267FCA44ED8A078,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    ),
                )
                + Op.RETURNDATACOPY(dest_offset=0x0, offset=0x0, size=0x20)
                + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                + Op.STOP
            ),
        ),
        callee_1: Account(code=Op.REVERT),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
