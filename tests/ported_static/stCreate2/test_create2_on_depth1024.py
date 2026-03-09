"""
Create2OnDepth1024, 0x0400 indicates 1022 level.

Ported from:
tests/static/state_tests/stCreate2/Create2OnDepth1024Filler.json
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
    ["tests/static/state_tests/stCreate2/Create2OnDepth1024Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.valid_until("Prague")
@pytest.mark.pre_alloc_mutable
def test_create2_on_depth1024(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Create2OnDepth1024, 0x0400 indicates 1022 level.."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    callee = Address("0xc94f5374fce5edbc8e2a8697c15331677e6ebf0b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[sender] = Account(
        balance=0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff,
        nonce=0,
    )
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.MSTORE(offset=0x0, value=Op.CALLDATALOAD(offset=0x0))
        + Op.MSTORE(offset=0x0, value=Op.ADD(0x2, Op.MLOAD(offset=0x0)))
        + Op.JUMPI(pc=0x43, condition=Op.EQ(Op.MLOAD(offset=0x0), 0x400))
        + Op.POP(Op.CALL(gas=Op.GAS, address=0xc94f5374fce5edbc8e2a8697c15331677e6ebf0b, value=Op.EQ(Op.MLOAD(offset=0x0), 0x400), args_offset=0x0, args_size=0x20, ret_offset=0x0, ret_size=0x0))
        + Op.JUMP(pc=0x6d) + Op.JUMPDEST
        + Op.MSTORE(offset=0x20, value=0x686000600060006000f56000526000600960176000f5600155)
        + Op.SSTORE(key=0x1, value=Op.CREATE2(value=0x0, offset=0x27, size=0x19, salt=0x0))
        + Op.JUMPDEST + Op.STOP
    ),
    )
    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.MSTORE(offset=0x0, value=Op.CALLDATALOAD(offset=0x0))
        + Op.CALL(gas=Op.GAS, address=0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b, value=0x0, args_offset=0x0, args_size=0x20, ret_offset=0x0, ret_size=0x0)
        + Op.STOP
    ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=b"",
        gas_limit=9151314442816847871,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        Address("0xb250d8cdad4a7a81323be508f4ac44584dd27597"): Account(
            storage={1: 0x436b8f99e8d953cdaf8f9472116add83ccd82a65},
        ),
        contract: Account(
            storage={1: 0xb250d8cdad4a7a81323be508f4ac44584dd27597},
            code=Op.MSTORE(offset=0x0, value=Op.CALLDATALOAD(offset=0x0)) + Op.MSTORE(offset=0x0, value=Op.ADD(0x2, Op.MLOAD(offset=0x0))) + Op.JUMPI(pc=0x43, condition=Op.EQ(Op.MLOAD(offset=0x0), 0x400)) + Op.POP(Op.CALL(gas=Op.GAS, address=0xc94f5374fce5edbc8e2a8697c15331677e6ebf0b, value=Op.EQ(Op.MLOAD(offset=0x0), 0x400), args_offset=0x0, args_size=0x20, ret_offset=0x0, ret_size=0x0)) + Op.JUMP(pc=0x6d) + Op.JUMPDEST + Op.MSTORE(offset=0x20, value=0x686000600060006000f56000526000600960176000f5600155) + Op.SSTORE(key=0x1, value=Op.CREATE2(value=0x0, offset=0x27, size=0x19, salt=0x0)) + Op.JUMPDEST + Op.STOP,
        ),
        callee: Account(
            code=Op.MSTORE(offset=0x0, value=Op.CALLDATALOAD(offset=0x0)) + Op.CALL(gas=Op.GAS, address=0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b, value=0x0, args_offset=0x0, args_size=0x20, ret_offset=0x0, ret_size=0x0) + Op.STOP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
