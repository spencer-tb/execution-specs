"""
Ported from:
tests/static/state_tests/stReturnDataTest/call_then_create_successful_then_returndatasizeFiller.json
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
    ["tests/static/state_tests/stReturnDataTest/call_then_create_successful_then_returndatasizeFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_call_then_create_successful_then_returndatasize(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xc102734f6a1e4747310179c0a0fc16e674aa901d")
    contract = Address("0xcc5fbabb1e86f7744ed4840b4153736d3c0ae2a2")
    callee = Address("0x24b406508240d6f2783499d1fd65fedd0feeef37")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=111669149696,
    )

    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.MSTORE(offset=0x0, value=0x111122223333444455556666777788889999aaaabbbbccccddddeeeeffff)
        + Op.RETURN(offset=0x0, size=0x20) + Op.STOP + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0x6400000000, nonce=0)
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.POP(Op.CALL(gas=0x900000000, address=0x24b406508240d6f2783499d1fd65fedd0feeef37, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.PUSH1[0xe] + Op.CODECOPY(dest_offset=0x0, offset=0x3c, size=Op.DUP1)
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.POP(Op.CREATE)
        + Op.SSTORE(key=0x0, value=Op.RETURNDATASIZE) + Op.STOP + Op.STOP + Op.INVALID
        + Op.MSTORE(offset=0x0, value=0x112233) + Op.RETURN(offset=0x0, size=0x20)
        + Op.STOP + Op.STOP
    ),
        storage={0x0: 0x1},
    )

    tx = Transaction(
        secret_key=Hash(
            "0x834185262e53584684bf2b72c64e510013c235d0f45e462db65900455df45a35"
        ),
        to=contract,
        data=b"",
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        callee: Account(
            code=Op.MSTORE(offset=0x0, value=0x111122223333444455556666777788889999aaaabbbbccccddddeeeeffff) + Op.RETURN(offset=0x0, size=0x20) + Op.STOP + Op.STOP,
        ),
        Address("0x9ad81872d43eab9c434b755513337c6b53ac1b0a"): Account(
            code=bytes.fromhex("0000000000000000000000000000000000000000000000000000000000112233"),
        ),
        contract: Account(
            code=Op.POP(Op.CALL(gas=0x900000000, address=0x24b406508240d6f2783499d1fd65fedd0feeef37, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.PUSH1[0xe] + Op.CODECOPY(dest_offset=0x0, offset=0x3c, size=Op.DUP1) + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.POP(Op.CREATE) + Op.SSTORE(key=0x0, value=Op.RETURNDATASIZE) + Op.STOP + Op.STOP + Op.INVALID + Op.MSTORE(offset=0x0, value=0x112233) + Op.RETURN(offset=0x0, size=0x20) + Op.STOP + Op.STOP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
