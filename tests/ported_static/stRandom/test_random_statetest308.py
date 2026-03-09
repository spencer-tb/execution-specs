"""
Ported from:
tests/static/state_tests/stRandom/randomStatetest308Filler.json
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
    ["tests/static/state_tests/stRandom/randomStatetest308Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.valid_until("Prague")
@pytest.mark.pre_alloc_mutable
def test_random_statetest308(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x945304eb96065b2a98b57a48a06ae28d285a71b5")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x095e7baea6a6c7c4c2dfeb977efac326af552d87")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH32[0x945304eb96065b2a98b57a48a06ae28d285a71b5]
        + Op.CALLDATALOAD(offset=Op.PUSH32[0x945304eb96065b2a98b57a48a06ae28d285a71b5])
        + Op.SSTORE(key=0x30f38c9a600051, value=Op.MULMOD(Op.ADD(Op.GAS, Op.ADDMOD(Op.PUSH32[0x10000000000000000000000000000000000000000], Op.PUSH32[0xc350], Op.TIMESTAMP)), 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe, Op.PUSH32[0xffffffffffffffffffffffffffffffffffffffff]))
    ),
    )
    pre[coinbase] = Account(
        balance=46,
        nonce=0,
        code=(
        Op.JUMPI(pc=0x9, condition=Op.ISZERO(Op.SLOAD(key=Op.CALLDATALOAD(offset=0x0))))
        + Op.STOP + Op.JUMPDEST
        + Op.SSTORE(key=Op.CALLDATALOAD(offset=0x0), value=Op.CALLDATALOAD(offset=0x20))
    ),
    )
    pre[sender] = Account(balance=0xde0b6b3a7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=bytes.fromhex(
            "7f000000000000000000000000945304eb96065b2a98b57a48a06ae28d285a71b57f0000"
            "00000000000000000000945304eb96065b2a98b57a48a06ae28d285a71b5357f00000000"
            "0000000000000000ffffffffffffffffffffffffffffffffffffffff7fffffffffffffff"
            "fffffffffffffffffffffffffffffffffffffffffffffffffe427f000000000000000000"
            "000000000000000000000000000000000000000000c3507f000000000000000000000001"
            "0000000000000000000000000000000000000000085a01096630f38c9a"
        ),
        gas_limit=1559407972,
        gas_price=10,
        nonce=0,
        value=23682877,
    )

    post = {
        contract: Account(
            storage={0x30f38c9a600051: 0x5cf25686ffffffffffffffff461b52f2},
            code=Op.PUSH32[0x945304eb96065b2a98b57a48a06ae28d285a71b5] + Op.CALLDATALOAD(offset=Op.PUSH32[0x945304eb96065b2a98b57a48a06ae28d285a71b5]) + Op.SSTORE(key=0x30f38c9a600051, value=Op.MULMOD(Op.ADD(Op.GAS, Op.ADDMOD(Op.PUSH32[0x10000000000000000000000000000000000000000], Op.PUSH32[0xc350], Op.TIMESTAMP)), 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe, Op.PUSH32[0xffffffffffffffffffffffffffffffffffffffff])),
        ),
        coinbase: Account(
            code=Op.JUMPI(pc=0x9, condition=Op.ISZERO(Op.SLOAD(key=Op.CALLDATALOAD(offset=0x0)))) + Op.STOP + Op.JUMPDEST + Op.SSTORE(key=Op.CALLDATALOAD(offset=0x0), value=Op.CALLDATALOAD(offset=0x20)),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
