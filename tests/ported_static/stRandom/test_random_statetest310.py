"""
Ported from:
tests/static/state_tests/stRandom/randomStatetest310Filler.json
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
    ["tests/static/state_tests/stRandom/randomStatetest310Filler.json"],
)
@pytest.mark.valid_from("Cancun")
def test_random_statetest310(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x1000000000000000000000000000000000001000")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x1000000000000000000000000000000000001100")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

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
        code=(
        Op.PREVRANDAO + Op.PC
        + Op.PUSH32[0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff]
        + Op.PUSH32[0xc350] + Op.PUSH32[0xffffffffffffffffffffffffffffffffffffffff]
        + Op.MSIZE + Op.SWAP1
        + Op.PUSH32[0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff]
        + Op.BYTE + Op.CALLDATACOPY + Op.AND + Op.SIGNEXTEND
        + Op.PUSH11[0x650645597c796e9c979555] + Op.PUSH1[0x0] + Op.MLOAD + Op.SSTORE
    ),
    )
    pre[sender] = Account(balance=0xde0b6b3a7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=bytes.fromhex(
            "44587fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f"
            "000000000000000000000000000000000000000000000000000000000000c3507f000000"
            "000000000000000000ffffffffffffffffffffffffffffffffffffffff59907fffffffff"
            "ffffffffffffffffffffffffffffffffffffffffffffffffffffffff1a37160b6a650645"
            "597c796e9c9795"
        ),
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=460778909,
    )

    post = {}

    state_test(env=env, pre=pre, post=post, tx=tx)
