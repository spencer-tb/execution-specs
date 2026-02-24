"""
Ported from:
tests/static/state_tests/stMemoryStressTest/RETURN_BoundsFiller.json
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
    ["tests/static/state_tests/stMemoryStressTest/RETURN_BoundsFiller.json"],
)
@pytest.mark.valid_from("Cancun")
@pytest.mark.parametrize(
    "tx_gas_limit",
    [
        150000,
        500000,
        15000000,
    ],
    ids=['case0', 'case1', 'case2'],
)
def test_return_bounds(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x1000000000000000000000000000000000002000")
    callee = Address("0x1000000000000000000000000000000000001000")
    callee_1 = Address("0x1000000000000000000000000000000000001100")
    callee_2 = Address("0x1000000000000000000000000000000000001200")
    callee_3 = Address("0x1000000000000000000000000000000000001300")
    callee_4 = Address("0x1000000000000000000000000000000000001400")
    callee_5 = Address("0x1000000000000000000000000000000000001500")
    callee_6 = Address("0x1000000000000000000000000000000000001600")
    callee_7 = Address("0x1000000000000000000000000000000000001700")
    callee_8 = Address("0x1000000000000000000000000000000000001800")
    callee_9 = Address("0x1000000000000000000000000000000000001900")
    callee_10 = Address("0x1000000000000000000000000000000000001a00")
    callee_11 = Address("0x1000000000000000000000000000000000001b00")
    callee_12 = Address("0x1000000000000000000000000000000000001c00")
    callee_13 = Address("0x1000000000000000000000000000000000001d00")
    callee_14 = Address("0x1000000000000000000000000000000000001e00")
    callee_15 = Address("0x1000000000000000000000000000000000001f00")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH32[0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff]
        + Op.PUSH32[0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff]
        + Op.RETURN + Op.STOP
    ),
    )
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH14[0xfffffffffffffffffffffffffff]
        + Op.PUSH14[0xfffffffffffffffffffffffffff] + Op.RETURN + Op.STOP
    ),
    )
    pre[callee_2] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH8[0xffffffffffffffff] + Op.PUSH8[0xffffffffffffffff] + Op.RETURN
        + Op.STOP
    ),
    )
    pre[callee_3] = Account(
        balance=0,
        nonce=0,
        code=Op.PUSH4[0xffffffff] + Op.PUSH4[0xffffffff] + Op.RETURN + Op.STOP,
    )
    pre[callee_4] = Account(
        balance=0,
        nonce=0,
        code=Op.PUSH4[0xfffffff] + Op.PUSH4[0xfffffff] + Op.RETURN + Op.STOP,
    )
    pre[callee_5] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH32[0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff]
        + Op.PUSH1[0x0] + Op.RETURN + Op.STOP
    ),
    )
    pre[callee_6] = Account(
        balance=0,
        nonce=0,
        code=Op.PUSH14[0xfffffffffffffffffffffffffff] + Op.PUSH1[0x0] + Op.RETURN + Op.STOP,
    )
    pre[callee_7] = Account(
        balance=0,
        nonce=0,
        code=Op.PUSH8[0xffffffffffffffff] + Op.PUSH1[0x0] + Op.RETURN + Op.STOP,
    )
    pre[callee_8] = Account(
        balance=0,
        nonce=0,
        code=Op.PUSH4[0xffffffff] + Op.PUSH1[0x0] + Op.RETURN + Op.STOP,
    )
    pre[callee_9] = Account(
        balance=0,
        nonce=0,
        code=Op.PUSH4[0xfffffff] + Op.PUSH1[0x0] + Op.RETURN + Op.STOP,
    )
    pre[callee_10] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH1[0x0]
        + Op.PUSH32[0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff]
        + Op.RETURN + Op.STOP
    ),
    )
    pre[callee_11] = Account(
        balance=0,
        nonce=0,
        code=Op.PUSH1[0x0] + Op.PUSH14[0xfffffffffffffffffffffffffff] + Op.RETURN + Op.STOP,
    )
    pre[callee_12] = Account(
        balance=0,
        nonce=0,
        code=Op.PUSH1[0x0] + Op.PUSH8[0xffffffffffffffff] + Op.RETURN + Op.STOP,
    )
    pre[callee_13] = Account(
        balance=0,
        nonce=0,
        code=Op.PUSH1[0x0] + Op.PUSH4[0xffffffff] + Op.RETURN + Op.STOP,
    )
    pre[callee_14] = Account(
        balance=0,
        nonce=0,
        code=Op.PUSH1[0x0] + Op.PUSH4[0xfffffff] + Op.RETURN + Op.STOP,
    )
    pre[callee_15] = Account(
        balance=0,
        nonce=0,
        code=Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.RETURN + Op.STOP,
    )
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH20[0x1000000000000000000000000000000000001f00]
        + Op.PUSH8[0x7ffffffffffffff] + Op.CALL + Op.PUSH1[0x1] + Op.SSTORE
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH20[0x1000000000000000000000000000000000001e00]
        + Op.PUSH8[0x7ffffffffffffff] + Op.CALL + Op.PUSH1[0x2] + Op.SSTORE
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH20[0x1000000000000000000000000000000000001d00]
        + Op.PUSH8[0x7ffffffffffffff] + Op.CALL + Op.PUSH1[0x3] + Op.SSTORE
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH20[0x1000000000000000000000000000000000001c00]
        + Op.PUSH8[0x7ffffffffffffff] + Op.CALL + Op.PUSH1[0x4] + Op.SSTORE
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH20[0x1000000000000000000000000000000000001b00]
        + Op.PUSH8[0x7ffffffffffffff] + Op.CALL + Op.PUSH1[0x5] + Op.SSTORE
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH20[0x1000000000000000000000000000000000001a00]
        + Op.PUSH8[0x7ffffffffffffff] + Op.CALL + Op.PUSH1[0x6] + Op.SSTORE
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH20[0x1000000000000000000000000000000000001a00]
        + Op.PUSH8[0x7ffffffffffffff] + Op.CALL + Op.PUSH1[0x7] + Op.SSTORE
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH20[0x1000000000000000000000000000000000001a00]
        + Op.PUSH8[0x7ffffffffffffff] + Op.CALL + Op.PUSH1[0x8] + Op.SSTORE
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH20[0x1000000000000000000000000000000000001a00]
        + Op.PUSH8[0x7ffffffffffffff] + Op.CALL + Op.PUSH1[0x9] + Op.SSTORE
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH20[0x1000000000000000000000000000000000001a00]
        + Op.PUSH8[0x7ffffffffffffff] + Op.CALL + Op.PUSH1[0xa] + Op.SSTORE
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH20[0x1000000000000000000000000000000000001a00]
        + Op.PUSH8[0x7ffffffffffffff] + Op.CALL + Op.PUSH1[0xb] + Op.SSTORE
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH20[0x1000000000000000000000000000000000001a00]
        + Op.PUSH8[0x7ffffffffffffff] + Op.CALL + Op.PUSH1[0xc] + Op.SSTORE
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH20[0x1000000000000000000000000000000000001a00]
        + Op.PUSH8[0x7ffffffffffffff] + Op.CALL + Op.PUSH1[0xd] + Op.SSTORE
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH20[0x1000000000000000000000000000000000001a00]
        + Op.PUSH8[0x7ffffffffffffff] + Op.CALL + Op.PUSH1[0xe] + Op.SSTORE
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH20[0x1000000000000000000000000000000000001a00]
        + Op.PUSH8[0x7ffffffffffffff] + Op.CALL + Op.PUSH1[0xf] + Op.SSTORE
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH20[0x1000000000000000000000000000000000001a00]
        + Op.PUSH8[0x7ffffffffffffff] + Op.CALL + Op.PUSH1[0x10] + Op.SSTORE + Op.STOP
    ),
    )
    pre[sender] = Account(
        balance=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff,
        nonce=0,
    )

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=b"",
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = {}

    state_test(env=env, pre=pre, post=post, tx=tx)
