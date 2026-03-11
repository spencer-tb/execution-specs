"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stReturnDataTest
call_then_call_value_fail_then_returndatasizeFiller.json
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
        "tests/static/state_tests/stReturnDataTest/call_then_call_value_fail_then_returndatasizeFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_call_then_call_value_fail_then_returndatasize(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xc102734f6a1e4747310179c0a0fc16e674aa901d")
    contract = Address("0x0e496b29ad2f0e55adf292c08a6a9289cb163835")
    callee = Address("0x9898dd5e5c526b55ec49b1047e298705c13279f1")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=111669149696,
    )

    # Source: LLL
    # { (seq (CALL 0x0900000000 <contract:0x0aabbccdd5c57f15886f9b263e2f6d2d6c7b5ec6> 0 0 0 0 0x20) (CALL 0x0900000000 <contract:0x0aabbccdd5c57f15886f9b263e2f6d2d6c7b5ec6> 0xffffffffffff 0 0 0 0x20) (SSTORE 0 (RETURNDATASIZE)) )}  # noqa: E501
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.POP(
                Op.CALL(
                    gas=0x900000000,
                    address=0x9898DD5E5C526B55EC49B1047E298705C13279F1,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x20,
                ),
            )
            + Op.POP(
                Op.CALL(
                    gas=0x900000000,
                    address=0x9898DD5E5C526B55EC49B1047E298705C13279F1,
                    value=0xFFFFFFFFFFFF,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x20,
                ),
            )
            + Op.SSTORE(key=0x0, value=Op.RETURNDATASIZE)
            + Op.STOP
        ),
        storage={0x0: 0x1},
    )
    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.MSTORE(
                offset=0x0,
                value=0x111122223333444455556666777788889999AAAABBBBCCCCDDDDEEEEFFFF,  # noqa: E501
            )
            + Op.RETURN(offset=0x0, size=0x20)
            + Op.STOP
        ),
    )
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
            code=(
                Op.POP(
                    Op.CALL(
                        gas=0x900000000,
                        address=0x9898DD5E5C526B55EC49B1047E298705C13279F1,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    ),
                )
                + Op.POP(
                    Op.CALL(
                        gas=0x900000000,
                        address=0x9898DD5E5C526B55EC49B1047E298705C13279F1,
                        value=0xFFFFFFFFFFFF,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    ),
                )
                + Op.SSTORE(key=0x0, value=Op.RETURNDATASIZE)
                + Op.STOP
            ),
        ),
        callee: Account(
            code=(
                Op.MSTORE(
                    offset=0x0,
                    value=0x111122223333444455556666777788889999AAAABBBBCCCCDDDDEEEEFFFF,  # noqa: E501
                )
                + Op.RETURN(offset=0x0, size=0x20)
                + Op.STOP
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
