"""
Ported from:
tests/static/state_tests/stRandom/randomStatetest383Filler.json

coinbase code:
    push1 0x00
    calldataload
    sload
    iszero
    push1 0x09
    jumpi
    stop
    jumpdest
    push1 0x20
    calldataload
    push1 0x00
    calldataload
    sstore

contract code:
    push32 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    push32 0x4f3f701464972e74606d6ea82d4d3080599a0e79
    push32 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    push32 0xffffffffffffffffffffffffffffffffffffffff
    push32 0x4f3f701464972e74606d6ea82d4d3080599a0e79
    push32 0xffffffffffffffffffffffffffffffffffffffff
    push32 0xffffffffffffffffffffffffffffffffffffffff
    push32 0xffffffffffffffffffffffffffffffffffffffff
    mulmod
    iszero
    mul
    sstore
    number
    push13 0x75107e
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
    ["tests/static/state_tests/stRandom/randomStatetest383Filler.json"],
)
@pytest.mark.valid_from("Cancun")
@pytest.mark.pre_alloc_mutable
def test_random_statetest383(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x4f3f701464972e74606d6ea82d4d3080599a0e79")
    sender = Address("0x2e3d0156d2b99a6eacba540c55f423c8f5a33143")
    contract = Address("0x9306b5e9e12f8e3524cb929c05e3f817fd403029")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[sender] = Account(balance=0xde0b6b3a7640000, nonce=0)
    pre[coinbase] = Account(
        balance=46,
        nonce=0,
        code=(
        Op.PUSH1[0x0] + Op.CALLDATALOAD + Op.SLOAD + Op.ISZERO + Op.PUSH1[0x9]
        + Op.JUMPI + Op.STOP + Op.JUMPDEST + Op.PUSH1[0x20] + Op.CALLDATALOAD
        + Op.PUSH1[0x0] + Op.CALLDATALOAD + Op.SSTORE
    ),
    )
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
        "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f0000"
        "000000000000000000004f3f701464972e74606d6ea82d4d3080599a0e797fffffffffff"
        "ffffffffffffffffffffffffffffffffffffffffffffffffffffff7f0000000000000000"
        "00000000ffffffffffffffffffffffffffffffffffffffff7f0000000000000000000000"
        "004f3f701464972e74606d6ea82d4d3080599a0e797f000000000000000000000000ffff"
        "ffffffffffffffffffffffffffffffffffff7f000000000000000000000000ffffffffff"
        "ffffffffffffffffffffffffffffff7f000000000000000000000000ffffffffffffffff"
        "ffffffffffffffffffffffff09150255436c75107e"
    ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xb1f4cbc3a50042184425a6f9e996d0910f7ba879457ce5dac5c71e498ad3c005"
        ),
        to=contract,
        data=bytes.fromhex(
            "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f0000"
            "000000000000000000004f3f701464972e74606d6ea82d4d3080599a0e797fffffffffff"
            "ffffffffffffffffffffffffffffffffffffffffffffffffffffff7f0000000000000000"
            "00000000ffffffffffffffffffffffffffffffffffffffff7f0000000000000000000000"
            "004f3f701464972e74606d6ea82d4d3080599a0e797f000000000000000000000000ffff"
            "ffffffffffffffffffffffffffffffffffff7f000000000000000000000000ffffffffff"
            "ffffffffffffffffffffffffffffff7f000000000000000000000000ffffffffffffffff"
            "ffffffffffffffffffffffff09150255436c75107e"
        ),
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=1668923511,
    )

    post = {
        Address("0x095e7baea6a6c7c4c2dfeb977efac326af552d87"): Account(
            storage={0x945304eb96065b2a98b57a48a06ae28d285a71b5: 0xffffffffffffffffffffffffffffffffffffffff},
            nonce=0,
            balance=0x6379c077,
        ),
        Address("0x<contract:0x945304eb96065b2a98b57a48a06ae28d285a71b5>"): Account(
            storage={},
            nonce=0,
        ),
        Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(
            storage={},
            nonce=1,
            code=b"",
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
