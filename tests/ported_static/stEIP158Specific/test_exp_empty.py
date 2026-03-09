"""
Ported from:
tests/static/state_tests/stEIP158Specific/EXP_EmptyFiller.json
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
    ["tests/static/state_tests/stEIP158Specific/EXP_EmptyFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_exp_empty(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xfaa10b404ab607779993c016cd5da73ae1f29d7e")
    contract = Address("0x8a3c9879fc69c8c45c1201c27da63312e9e9f6fe")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.MSTORE(offset=0x0, value=Op.GAS)
        + Op.SSTORE(key=0x1, value=Op.EXP(0x0, 0xc))
        + Op.SSTORE(key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS))
        + Op.MSTORE(offset=0x0, value=Op.GAS)
        + Op.SSTORE(key=0x3, value=Op.EXP(0xc, 0x0))
        + Op.SSTORE(key=0x4, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS))
        + Op.MSTORE(offset=0x0, value=Op.GAS)
        + Op.SSTORE(key=0x5, value=Op.EXP(0x0, 0xffffffffffffffff))
        + Op.SSTORE(key=0x6, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS))
        + Op.MSTORE(offset=0x0, value=Op.GAS)
        + Op.SSTORE(key=0x7, value=Op.EXP(0x0, 0xffffffffffffffffffffffffffffffff))
        + Op.SSTORE(key=0x8, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS))
        + Op.MSTORE(offset=0x0, value=Op.GAS)
        + Op.SSTORE(key=0x9, value=Op.EXP(0x0, 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff))
        + Op.SSTORE(key=0xa, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS))
        + Op.MSTORE(offset=0x0, value=Op.GAS)
        + Op.SSTORE(key=0xb, value=Op.EXP(0xffffffffffffffff, 0x0))
        + Op.SSTORE(key=0xc, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS))
        + Op.MSTORE(offset=0x0, value=Op.GAS)
        + Op.SSTORE(key=0xd, value=Op.EXP(0xffffffffffffffffffffffffffffffff, 0x0))
        + Op.SSTORE(key=0xe, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS))
        + Op.MSTORE(offset=0x0, value=Op.GAS)
        + Op.SSTORE(key=0xf, value=Op.EXP(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff, 0x0))
        + Op.SSTORE(key=0x64, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)) + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0xe8d4a51000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x4f31b3206fbf0e0e598b9b1a7d8ac86302a0ff1d8930738f1bebae9b67173e52"
        ),
        to=contract,
        data=b"",
        gas_limit=600000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            storage={2: 2280, 3: 1, 4: 22127, 6: 2627, 8: 3027, 10: 3827, 11: 1, 12: 22127, 13: 1, 14: 22127, 15: 1, 100: 22127},
            code=Op.MSTORE(offset=0x0, value=Op.GAS) + Op.SSTORE(key=0x1, value=Op.EXP(0x0, 0xc)) + Op.SSTORE(key=0x2, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)) + Op.MSTORE(offset=0x0, value=Op.GAS) + Op.SSTORE(key=0x3, value=Op.EXP(0xc, 0x0)) + Op.SSTORE(key=0x4, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)) + Op.MSTORE(offset=0x0, value=Op.GAS) + Op.SSTORE(key=0x5, value=Op.EXP(0x0, 0xffffffffffffffff)) + Op.SSTORE(key=0x6, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)) + Op.MSTORE(offset=0x0, value=Op.GAS) + Op.SSTORE(key=0x7, value=Op.EXP(0x0, 0xffffffffffffffffffffffffffffffff)) + Op.SSTORE(key=0x8, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)) + Op.MSTORE(offset=0x0, value=Op.GAS) + Op.SSTORE(key=0x9, value=Op.EXP(0x0, 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)) + Op.SSTORE(key=0xa, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)) + Op.MSTORE(offset=0x0, value=Op.GAS) + Op.SSTORE(key=0xb, value=Op.EXP(0xffffffffffffffff, 0x0)) + Op.SSTORE(key=0xc, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)) + Op.MSTORE(offset=0x0, value=Op.GAS) + Op.SSTORE(key=0xd, value=Op.EXP(0xffffffffffffffffffffffffffffffff, 0x0)) + Op.SSTORE(key=0xe, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)) + Op.MSTORE(offset=0x0, value=Op.GAS) + Op.SSTORE(key=0xf, value=Op.EXP(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff, 0x0)) + Op.SSTORE(key=0x64, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)) + Op.STOP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
