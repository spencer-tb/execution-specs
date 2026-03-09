"""
Ported from:
tests/static/state_tests/stRandom/randomStatetest66Filler.json
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
    ["tests/static/state_tests/stRandom/randomStatetest66Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_random_statetest66(
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
        Op.GASLIMIT
        + Op.PUSH32[0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff]
        + Op.COINBASE
        + Op.SSTORE(key=Op.PUSH32[0x10000000000000000000000000000000000000000], value=Op.MULMOD(0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe, Op.PUSH32[0x945304eb96065b2a98b57a48a06ae28d285a71b5], 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff))
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
            "457fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff417f"
            "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f000000"
            "000000000000000000945304eb96065b2a98b57a48a06ae28d285a71b57fffffffffffff"
            "fffffffffffffffffffffffffffffffffffffffffffffffffffe097f0000000000000000"
            "000000010000000000000000000000000000000000000000"
        ),
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=794190030,
    )

    post = {
        contract: Account(
            storage={0x10000000000000000000000000000000000000000: 0xffffffffffffffffffffffff6bacfb1469f9a4d5674a85b75f951d72d7a58e4a},
            code=Op.GASLIMIT + Op.PUSH32[0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff] + Op.COINBASE + Op.SSTORE(key=Op.PUSH32[0x10000000000000000000000000000000000000000], value=Op.MULMOD(0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe, Op.PUSH32[0x945304eb96065b2a98b57a48a06ae28d285a71b5], 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)),
        ),
        coinbase: Account(
            code=Op.JUMPI(pc=0x9, condition=Op.ISZERO(Op.SLOAD(key=Op.CALLDATALOAD(offset=0x0)))) + Op.STOP + Op.JUMPDEST + Op.SSTORE(key=Op.CALLDATALOAD(offset=0x0), value=Op.CALLDATALOAD(offset=0x20)),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
