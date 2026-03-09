"""
Ported from:
tests/static/state_tests/stRevertTest/RevertInDelegateCallFiller.json
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
    ["tests/static/state_tests/stRevertTest/RevertInDelegateCallFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_revert_in_delegate_call(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x7f3f285918d9b5e764174551e10b7539b97bbb27")
    contract = Address("0x23ea33dc3aa11f5a1da3643bb13956382b9b6767")
    callee = Address("0xc3ecfe24c185ad3c946ebff4624131e8af5220a2")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    pre[contract] = Account(
        balance=1000,
        nonce=0,
        code=(
        Op.SSTORE(key=0x0, value=Op.DELEGATECALL(gas=0xc350, address=0xc3ecfe24c185ad3c946ebff4624131e8af5220a2, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40))
        + Op.SSTORE(key=0x1, value=Op.RETURNDATASIZE)
        + Op.RETURNDATACOPY(dest_offset=0x3f, offset=0x0, size=0x20)
        + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x3f)) + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0x5f5e100, nonce=0)
    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=Op.MSTORE(offset=0x20, value=0xa) + Op.REVERT(offset=0x20, size=0x20) + Op.STOP,
    )

    tx = Transaction(
        secret_key=Hash(
            "0xa2333eef5630066b928dea5fd85a239f511b5b067d1441ee7ac290d0122b917b"
        ),
        to=contract,
        data=b"",
        gas_limit=105044,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            storage={1: 32, 2: 10},
            code=Op.SSTORE(key=0x0, value=Op.DELEGATECALL(gas=0xc350, address=0xc3ecfe24c185ad3c946ebff4624131e8af5220a2, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40)) + Op.SSTORE(key=0x1, value=Op.RETURNDATASIZE) + Op.RETURNDATACOPY(dest_offset=0x3f, offset=0x0, size=0x20) + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x3f)) + Op.STOP,
        ),
        callee: Account(
            code=Op.MSTORE(offset=0x20, value=0xa) + Op.REVERT(offset=0x20, size=0x20) + Op.STOP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
