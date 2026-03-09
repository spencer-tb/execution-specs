"""
Transient storage can't be manipulated from nested staticcall.

Ported from:
tests/static/state_tests/Cancun/stEIP1153_transientStorage/14_revertAfterNestedStaticcallFiller.yml
"""

import pytest
from execution_testing import (
    AccessList,
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
    ["tests/static/state_tests/Cancun/stEIP1153_transientStorage/14_revertAfterNestedStaticcallFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_14_revert_after_nested_staticcall(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Transient storage can't be manipulated from nested staticcall.."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xcef5f3b33e31360216fab2c61046840df9bd788e")
    contract = Address("0x1150baff55fdcea5fd92b0995358ec0c416debe3")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=4503599627370496,
    )

    pre[contract] = Account(
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=(
        Op.SHR(0xe0, Op.CALLDATALOAD(offset=Op.PUSH0))
        + Op.JUMPI(pc=0x2f, condition=Op.EQ(0xf5f40590, Op.DUP1))
        + Op.JUMPI(pc=0x2b, condition=Op.EQ(0xf8dfc2d0, Op.DUP1))
        + Op.PUSH4[0x62fdb9be] + Op.JUMPI(pc=0x23, condition=Op.EQ) + Op.STOP
        + Op.JUMPDEST + Op.PUSH1[0x29] + Op.JUMP(pc=0x77) + Op.JUMPDEST + Op.STOP
        + Op.JUMPDEST + Op.JUMP(pc=0x5d) + Op.JUMPDEST + Op.POP + Op.PUSH1[0x29]
        + Op.TSTORE(key=Op.PUSH0, value=0xa)
        + Op.SSTORE(key=Op.PUSH0, value=Op.TLOAD(key=Op.PUSH0))
        + Op.MSTORE(offset=Op.PUSH0, value=Op.SHL(0xe4, 0xf8dfc2d))
        + Op.STATICCALL(gas=0xffff, address=Op.ADDRESS, args_offset=Op.DUP2, args_size=Op.DUP2, ret_offset=Op.PUSH0, ret_size=0x20)
        + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=Op.PUSH0)) + Op.PUSH1[0x2]
        + Op.SSTORE + Op.SSTORE(key=0x3, value=Op.TLOAD(key=Op.PUSH0)) + Op.JUMP
        + Op.JUMPDEST + Op.MSTORE(offset=Op.PUSH0, value=Op.SHL(0xe1, 0x317edcdf))
        + Op.MSTORE(offset=Op.PUSH0, value=Op.CALL(gas=Op.GAS, address=Op.ADDRESS, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=Op.PUSH0))
        + Op.RETURN(offset=Op.PUSH0, size=0x20) + Op.JUMPDEST
        + Op.TSTORE(key=Op.PUSH0, value=0xb) + Op.JUMP
    ),
        storage={0x1: 0xffff},
    )
    pre[sender] = Account(balance=0x3635c9adc5dea00000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xbe0e7d5fea1604bf57e004b0b414df8de04816dbb1c8f8719b725d0d6619b531"
        ),
        to=contract,
        data=bytes.fromhex("f5f40590"),
        gas_limit=400000,
        max_fee_per_gas=2000,
        max_priority_fee_per_gas=0,
        nonce=0,
        value=0,
        access_list=[],
    )

    post = {
        contract: Account(
            storage={0: 10, 2: 1, 3: 10},
            code=Op.SHR(0xe0, Op.CALLDATALOAD(offset=Op.PUSH0)) + Op.JUMPI(pc=0x2f, condition=Op.EQ(0xf5f40590, Op.DUP1)) + Op.JUMPI(pc=0x2b, condition=Op.EQ(0xf8dfc2d0, Op.DUP1)) + Op.PUSH4[0x62fdb9be] + Op.JUMPI(pc=0x23, condition=Op.EQ) + Op.STOP + Op.JUMPDEST + Op.PUSH1[0x29] + Op.JUMP(pc=0x77) + Op.JUMPDEST + Op.STOP + Op.JUMPDEST + Op.JUMP(pc=0x5d) + Op.JUMPDEST + Op.POP + Op.PUSH1[0x29] + Op.TSTORE(key=Op.PUSH0, value=0xa) + Op.SSTORE(key=Op.PUSH0, value=Op.TLOAD(key=Op.PUSH0)) + Op.MSTORE(offset=Op.PUSH0, value=Op.SHL(0xe4, 0xf8dfc2d)) + Op.STATICCALL(gas=0xffff, address=Op.ADDRESS, args_offset=Op.DUP2, args_size=Op.DUP2, ret_offset=Op.PUSH0, ret_size=0x20) + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=Op.PUSH0)) + Op.PUSH1[0x2] + Op.SSTORE + Op.SSTORE(key=0x3, value=Op.TLOAD(key=Op.PUSH0)) + Op.JUMP + Op.JUMPDEST + Op.MSTORE(offset=Op.PUSH0, value=Op.SHL(0xe1, 0x317edcdf)) + Op.MSTORE(offset=Op.PUSH0, value=Op.CALL(gas=Op.GAS, address=Op.ADDRESS, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=Op.PUSH0)) + Op.RETURN(offset=Op.PUSH0, size=0x20) + Op.JUMPDEST + Op.TSTORE(key=Op.PUSH0, value=0xb) + Op.JUMP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
