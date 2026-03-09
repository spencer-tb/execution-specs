"""
Ported from:
tests/static/state_tests/Shanghai/stEIP3860_limitmeterinitcode/createInitCodeSizeLimitFiller.yml
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
    ["tests/static/state_tests/Shanghai/stEIP3860_limitmeterinitcode/createInitCodeSizeLimitFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        ("000000000000000000000000000000000000000000000000000000000000c001", {Address("0x000000000000000000000000000000000000c0de"): Account(code=Op.SHL(0xb0, 0x600a80600080396000f3) + Op.PUSH1[0x0] + Op.SWAP1 + Op.DUP2 + Op.MSTORE + Op.CALLDATALOAD + Op.GAS + Op.SWAP1 + Op.PUSH1[0x0] + Op.DUP1 + Op.CREATE + Op.SWAP1 + Op.GAS + Op.SWAP1 + Op.SSTORE(key=0xa, value=Op.SUB) + Op.PUSH1[0x0] + Op.SSTORE + Op.STOP), Address("0xbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"): Account(storage={1: 1}, code=Op.MSTORE(offset=0x0, value=Op.CALLDATALOAD(offset=0x0)) + Op.SSTORE(key=0x0, value=Op.CALL(gas=0x989680, address=0xc0de, value=Op.DUP1, args_offset=Op.DUP2, args_size=Op.CALLDATASIZE, ret_offset=Op.DUP1, ret_size=0x0)) + Op.SSTORE(key=Op.DUP1, value=0x1) + Op.STOP)}),
        ("000000000000000000000000000000000000000000000000000000000000c000", {Address("0x000000000000000000000000000000000000c0de"): Account(storage={0: 0x5f6baaeb5b7c97725f84d1569c4abc85135f4716, 10: 46323}, code=Op.SHL(0xb0, 0x600a80600080396000f3) + Op.PUSH1[0x0] + Op.SWAP1 + Op.DUP2 + Op.MSTORE + Op.CALLDATALOAD + Op.GAS + Op.SWAP1 + Op.PUSH1[0x0] + Op.DUP1 + Op.CREATE + Op.SWAP1 + Op.GAS + Op.SWAP1 + Op.SSTORE(key=0xa, value=Op.SUB) + Op.PUSH1[0x0] + Op.SSTORE + Op.STOP), Address("0x5f6baaeb5b7c97725f84d1569c4abc85135f4716"): Account(code=Op.PUSH1[0xa] + Op.CODECOPY(dest_offset=Op.DUP1, offset=0x0, size=Op.DUP1) + Op.PUSH1[0x0] + Op.RETURN), Address("0xbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"): Account(storage={0: 1, 1: 1}, code=Op.MSTORE(offset=0x0, value=Op.CALLDATALOAD(offset=0x0)) + Op.SSTORE(key=0x0, value=Op.CALL(gas=0x989680, address=0xc0de, value=Op.DUP1, args_offset=Op.DUP2, args_size=Op.CALLDATASIZE, ret_offset=Op.DUP1, ret_size=0x0)) + Op.SSTORE(key=Op.DUP1, value=0x1) + Op.STOP)}),
    ],
    ids=['case0', 'case1'],
)
@pytest.mark.pre_alloc_mutable
def test_create_init_code_size_limit(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
    callee = Address("0x000000000000000000000000000000000000c0de")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=20000000,
    )

    pre[callee] = Account(
        balance=0,
        nonce=1,
        code=(
        Op.SHL(0xb0, 0x600a80600080396000f3) + Op.PUSH1[0x0] + Op.SWAP1 + Op.DUP2
        + Op.MSTORE + Op.CALLDATALOAD + Op.GAS + Op.SWAP1 + Op.PUSH1[0x0] + Op.DUP1
        + Op.CREATE + Op.SWAP1 + Op.GAS + Op.SWAP1 + Op.SSTORE(key=0xa, value=Op.SUB)
        + Op.PUSH1[0x0] + Op.SSTORE + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0xbebc200, nonce=1)
    pre[contract] = Account(
        balance=0,
        nonce=1,
        code=(
        Op.MSTORE(offset=0x0, value=Op.CALLDATALOAD(offset=0x0))
        + Op.SSTORE(key=0x0, value=Op.CALL(gas=0x989680, address=0xc0de, value=Op.DUP1, args_offset=Op.DUP2, args_size=Op.CALLDATASIZE, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.SSTORE(key=Op.DUP1, value=0x1) + Op.STOP
    ),
    )

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=tx_data,
        gas_limit=15000000,
        gas_price=10,
        nonce=1,
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
