"""
Ported from:
tests/static/state_tests/stRandom2/randomStatetest450Filler.json
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
    ["tests/static/state_tests/stRandom2/randomStatetest450Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_random_statetest450(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x4f3f701464972e74606d6ea82d4d3080599a0e79")
    sender = Address("0x86071df262f8102466c69a1b215be50d4965756b")
    contract = Address("0x4cda9e76f4ec620ca74c0321e2393998b84f4b99")

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
        Op.PUSH32[0x0] + Op.PUSH32[0x4f3f701464972e74606d6ea82d4d3080599a0e79]
        + Op.PUSH32[0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff]
        + Op.CALLDATALOAD(offset=Op.PUSH32[0x4f3f701464972e74606d6ea82d4d3080599a0e79])
        + Op.PUSH32[0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff]
        + Op.SUB(Op.PUSH32[0x10000000000000000000000000000000000000000], Op.PUSH32[0xc350])
        + Op.GASPRICE + Op.SSTORE(key=Op.MLOAD(offset=0x0), value=Op.DUP1)
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
    pre[sender] = Account(balance=0xde0b6b3a764000000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xec7c2de039694d1868a1956b3126454e8e17448344a219e03d859b64831b6af8"
        ),
        to=contract,
        data=bytes.fromhex(
            "7f00000000000000000000000000000000000000000000000000000000000000007f0000"
            "000000000000000000004f3f701464972e74606d6ea82d4d3080599a0e797fffffffffff"
            "ffffffffffffffffffffffffffffffffffffffffffffffffffffff7f0000000000000000"
            "000000004f3f701464972e74606d6ea82d4d3080599a0e79357fffffffffffffffffffff"
            "ffffffffffffffffffffffffffffffffffffffffffff7f00000000000000000000000000"
            "0000000000000000000000000000000000c3507f00000000000000000000000100000000"
            "00000000000000000000000000000000033a80"
        ),
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=1357943190,
    )

    post = {
        contract: Account(
            storage={0: 10},
            code=Op.PUSH32[0x0] + Op.PUSH32[0x4f3f701464972e74606d6ea82d4d3080599a0e79] + Op.PUSH32[0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff] + Op.CALLDATALOAD(offset=Op.PUSH32[0x4f3f701464972e74606d6ea82d4d3080599a0e79]) + Op.PUSH32[0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff] + Op.SUB(Op.PUSH32[0x10000000000000000000000000000000000000000], Op.PUSH32[0xc350]) + Op.GASPRICE + Op.SSTORE(key=Op.MLOAD(offset=0x0), value=Op.DUP1),
        ),
        coinbase: Account(
            code=Op.JUMPI(pc=0x9, condition=Op.ISZERO(Op.SLOAD(key=Op.CALLDATALOAD(offset=0x0)))) + Op.STOP + Op.JUMPDEST + Op.SSTORE(key=Op.CALLDATALOAD(offset=0x0), value=Op.CALLDATALOAD(offset=0x20)),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
