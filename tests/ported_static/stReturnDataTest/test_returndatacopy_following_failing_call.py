"""
Ported from:
tests/static/state_tests/stReturnDataTest/returndatacopy_following_failing_callFiller.json
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
    ["tests/static/state_tests/stReturnDataTest/returndatacopy_following_failing_callFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_returndatacopy_following_failing_call(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xc102734f6a1e4747310179c0a0fc16e674aa901d")
    contract = Address("0x71a277f82c43ff98682eb8d6db4a3ecd680407eb")
    callee = Address("0x3141bb954e8294e47a14ebd08229f30e6294ba83")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=111669149696,
    )

    pre[callee] = Account(balance=0, nonce=0, code=Op.REVERT)
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.POP(Op.CALL(gas=0x900000000, address=0x3141bb954e8294e47a14ebd08229f30e6294ba83, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.RETURNDATACOPY(dest_offset=0x0, offset=0x1, size=0x20)
        + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0)) + Op.STOP
    ),
        storage={0x0: 0x1},
    )
    pre[sender] = Account(balance=0x6400000000, nonce=0)

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
        callee: Account(code=Op.REVERT),
        contract: Account(
            storage={0: 1},
            code=Op.POP(Op.CALL(gas=0x900000000, address=0x3141bb954e8294e47a14ebd08229f30e6294ba83, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.RETURNDATACOPY(dest_offset=0x0, offset=0x1, size=0x20) + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0)) + Op.STOP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
