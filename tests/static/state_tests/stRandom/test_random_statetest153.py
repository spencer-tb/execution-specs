"""
Ported from:
tests/static/state_tests/stRandom/randomStatetest153Filler.json

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
    prevrandao
    timestamp
    signextend
    prevrandao
    timestamp
    number
    sha3
    sstore
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
    ["tests/static/state_tests/stRandom/randomStatetest153Filler.json"],
)
@pytest.mark.valid_from("Cancun")
@pytest.mark.pre_alloc_mutable
def test_random_statetest153(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x4f3f701464972e74606d6ea82d4d3080599a0e79")
    sender = Address("0x2e3d0156d2b99a6eacba540c55f423c8f5a33143")
    contract = Address("0x973aa64afc19eaeb66865746fc4938231bcf3312")

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
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=(
        Op.PREVRANDAO + Op.TIMESTAMP + Op.SIGNEXTEND + Op.PREVRANDAO + Op.TIMESTAMP
        + Op.NUMBER + Op.SHA3 + Op.SSTORE
    ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xb1f4cbc3a50042184425a6f9e996d0910f7ba879457ce5dac5c71e498ad3c005"
        ),
        to=contract,
        data=bytes.fromhex("42"),
        gas_limit=400000,
        gas_price=10,
        nonce=0,
        value=100000,
    )

    post = {
        Address("0x095e7baea6a6c7c4c2dfeb977efac326af552d87"): Account(
            storage={0xae72e2bf2302ebcd309e003e5be58830f96deddaf87bb89eeea159388bfe3ec1: 0x20000, 0xbc36789e7a1e281436464229828f817d6612f7b477d66591ff96a9e064bcc98a: 0},
            nonce=0,
            balance=0xde0b6b3a76586a0,
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
