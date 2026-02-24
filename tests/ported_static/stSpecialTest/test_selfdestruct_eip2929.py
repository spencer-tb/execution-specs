"""
Martin: @tkstanczak requested a state-test regarding selfdestructs in relation to EIP-2929. I made one, which tests different variants of hot/cold accounts, and even precompile beneficiaries. https://github.com/holiman/goevmlab/blob/selfdestruct_2929/examples/selfdestruct_2929/main.go#L94

Ported from:
tests/static/state_tests/stSpecialTest/selfdestructEIP2929Filler.json
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
    ["tests/static/state_tests/stSpecialTest/selfdestructEIP2929Filler.json"],
)
@pytest.mark.valid_from("Cancun")
def test_selfdestruct_eip2929(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Martin: @tkstanczak requested a state-test regarding selfdestructs in relation to EIP-2929. I made one, which tests different variants of hot/cold accounts, and even precompile beneficiaries. https://github.com/holiman/goevmlab/blob/selfdestruct_2929/examples/selfdestruct_2929/main.go#L94."""
    coinbase = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x1000000000000000000000000000000000001100")
    callee = Address("0x1000000000000000000000000000000000001000")
    callee_1 = Address("0x6389e7f33ce3b1e94e4325ef02829cd12297ef71")
    callee_2 = Address("0x8a0a19589531694250d570040a0c4b74576919b8")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10944489199640098,
    )

    pre[callee] = Account(
        balance=1,
        nonce=1,
        code=(
        Op.PUSH1[0x0] + Op.CALLDATALOAD
        + Op.PUSH21[0xffffffffffffffffffffffffffffffffffffffffff] + Op.AND
        + Op.SELFDESTRUCT
    ),
    )
    pre[contract] = Account(
        balance=1,
        nonce=1,
        code=(
        Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH1[0xcc] + Op.PUSH1[0x0] + Op.CALL + Op.POP
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH1[0xdd] + Op.PUSH1[0x0] + Op.CALL + Op.POP
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH1[0x3] + Op.PUSH1[0x0] + Op.CALL + Op.POP
        + Op.PUSH1[0xaa] + Op.PUSH1[0x0] + Op.MSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x20] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH2[0xdead] + Op.GAS
        + Op.CALL + Op.POP + Op.PUSH1[0xaa] + Op.PUSH1[0x0] + Op.MSTORE
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x20] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH2[0xdead] + Op.GAS + Op.CALL + Op.POP
        + Op.PUSH1[0xbb] + Op.PUSH1[0x0] + Op.MSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x20] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH2[0xdead] + Op.GAS
        + Op.CALL + Op.POP + Op.PUSH1[0xbb] + Op.PUSH1[0x0] + Op.MSTORE
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x20] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH2[0xdead] + Op.GAS + Op.CALL + Op.POP
        + Op.PUSH1[0xcc] + Op.PUSH1[0x0] + Op.MSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x20] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH2[0xdead] + Op.GAS
        + Op.CALL + Op.POP + Op.PUSH1[0xcc] + Op.PUSH1[0x0] + Op.MSTORE
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x20] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH2[0xdead] + Op.GAS + Op.CALL + Op.POP
        + Op.PUSH1[0xdd] + Op.PUSH1[0x0] + Op.MSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x20] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH2[0xdead] + Op.GAS
        + Op.CALL + Op.POP + Op.PUSH1[0xdd] + Op.PUSH1[0x0] + Op.MSTORE
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x20] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH2[0xdead] + Op.GAS + Op.CALL + Op.POP + Op.PUSH1[0x1]
        + Op.PUSH1[0x0] + Op.MSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x20]
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH2[0xdead] + Op.GAS + Op.CALL + Op.POP
        + Op.PUSH1[0x1] + Op.PUSH1[0x0] + Op.MSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x20] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH2[0xdead] + Op.GAS
        + Op.CALL + Op.POP + Op.PUSH1[0x2] + Op.PUSH1[0x0] + Op.MSTORE + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH1[0x20] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH2[0xdead] + Op.GAS + Op.CALL + Op.POP + Op.PUSH1[0x2] + Op.PUSH1[0x0]
        + Op.MSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x20] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH2[0xdead] + Op.GAS + Op.CALL + Op.POP + Op.PUSH1[0x3]
        + Op.PUSH1[0x0] + Op.MSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x20]
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH2[0xdead] + Op.GAS + Op.CALL + Op.POP
        + Op.PUSH1[0x1] + Op.PUSH1[0x1] + Op.SSTORE
    ),
    )
    pre[callee_1] = Account(balance=0, nonce=1)
    pre[callee_2] = Account(balance=0, nonce=1)
    pre[sender] = Account(balance=0xde0b6b3a7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=b"",
        gas_limit=8000000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {}

    state_test(env=env, pre=pre, post=post, tx=tx)
