"""
Ported from:
tests/static/state_tests/stReturnDataTest/returndatacopy_initial_256Filler.json
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
    ["tests/static/state_tests/stReturnDataTest/returndatacopy_initial_256Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex",
    [
        "0000000000000000000000000000000000000000000000000000000000000064",
        "0000000000000000000000000000000000000000000000000000000000000063",
        "0000000000000000000000000000000000000000000000000000000000000065",
    ],
    ids=['case0', 'case1', 'case2'],
)
@pytest.mark.pre_alloc_mutable
def test_returndatacopy_initial_256(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xc102734f6a1e4747310179c0a0fc16e674aa901d")
    contract = Address("0x28f194b678152b435b5910dbdf69c091fa056347")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=111669149696,
    )

    pre[contract] = Account(
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=(
        Op.RETURNDATACOPY(dest_offset=Op.SUB(0x0, Op.CALLDATALOAD(offset=0x0)), offset=0x0, size=0x64)
        + Op.MSTORE(offset=0x0, value=0x112233445566778899aabbccddeeff)
        + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0)) + Op.STOP
    ),
        storage={0x0: 0x1},
    )
    pre[sender] = Account(balance=0x6400000000, nonce=0)

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x834185262e53584684bf2b72c64e510013c235d0f45e462db65900455df45a35"
        ),
        to=contract,
        data=tx_data,
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            storage={0: 1},
            code=Op.RETURNDATACOPY(dest_offset=Op.SUB(0x0, Op.CALLDATALOAD(offset=0x0)), offset=0x0, size=0x64) + Op.MSTORE(offset=0x0, value=0x112233445566778899aabbccddeeff) + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0)) + Op.STOP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
