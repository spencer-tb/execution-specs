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
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_random_statetest310(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x4f3f701464972e74606d6ea82d4d3080599a0e79")
    sender = Address("0x2e3d0156d2b99a6eacba540c55f423c8f5a33143")
    contract = Address("0x6aba73f1d891c72c1b5730ac84067c1286ba693b")

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
        Op.JUMPI(pc=0x9, condition=Op.ISZERO(Op.SLOAD(key=Op.CALLDATALOAD(offset=0x0))))
        + Op.STOP + Op.JUMPDEST
        + Op.SSTORE(key=Op.CALLDATALOAD(offset=0x0), value=Op.CALLDATALOAD(offset=0x20))
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
        + Op.SSTORE(key=Op.MLOAD(offset=0x0), value=0x650645597c796e9c979555)
    ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xb1f4cbc3a50042184425a6f9e996d0910f7ba879457ce5dac5c71e498ad3c005"
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

    post = {
        coinbase: Account(
            code=Op.JUMPI(pc=0x9, condition=Op.ISZERO(Op.SLOAD(key=Op.CALLDATALOAD(offset=0x0)))) + Op.STOP + Op.JUMPDEST + Op.SSTORE(key=Op.CALLDATALOAD(offset=0x0), value=Op.CALLDATALOAD(offset=0x20)),
        ),
        contract: Account(
            storage={0x44587fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff: 0x650645597c796e9c979555},
            code=Op.PREVRANDAO + Op.PC + Op.PUSH32[0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff] + Op.PUSH32[0xc350] + Op.PUSH32[0xffffffffffffffffffffffffffffffffffffffff] + Op.MSIZE + Op.SWAP1 + Op.PUSH32[0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff] + Op.BYTE + Op.CALLDATACOPY + Op.AND + Op.SIGNEXTEND + Op.SSTORE(key=Op.MLOAD(offset=0x0), value=0x650645597c796e9c979555),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
