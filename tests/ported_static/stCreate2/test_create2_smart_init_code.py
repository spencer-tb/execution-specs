"""
create2SmartInitCode. create2 works different each time you call it

Ported from:
tests/static/state_tests/stCreate2/create2SmartInitCodeFiller.json
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
    ["tests/static/state_tests/stCreate2/create2SmartInitCodeFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        ("0000000000000000000000000f572e5295c57f15886f9b263e2f6d2d6c7b5ec6", {Address("0x0f572e5295c57f15886f9b263e2f6d2d6c7b5ec6"): Account(storage={1: 0xf6510583d425cfcf94b99f8b073b44f60d1912b}, code=Op.MSTORE(offset=0x0, value=0x600060015414601157600a6000f3601a565b60016001556001ff5b) + Op.SSTORE(key=0x1, value=Op.CREATE2(value=0x1, offset=0x5, size=0x1b, salt=0x0)) + Op.SSTORE(key=0x2, value=Op.CREATE2(value=0x1, offset=0x5, size=0x1b, salt=0x0)) + Op.STOP), Address("0x1f572e5295c57f15886f9b263e2f6d2d6c7b5ec6"): Account(code=Op.MSTORE(offset=0x0, value=0x600060015414601157600a6000f3601c565b6001600155600a6000f35b) + Op.SSTORE(key=0x1, value=Op.CREATE2(value=0x1, offset=0x3, size=0x1d, salt=0x0)) + Op.SSTORE(key=0x2, value=Op.CREATE2(value=0x1, offset=0x5, size=0x1b, salt=0x0)) + Op.STOP), Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(code=Op.CALL(gas=Op.GAS, address=Op.CALLDATALOAD(offset=0x0), value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0) + Op.STOP)}),
        ("0000000000000000000000001f572e5295c57f15886f9b263e2f6d2d6c7b5ec6", {Address("0x0f572e5295c57f15886f9b263e2f6d2d6c7b5ec6"): Account(code=Op.MSTORE(offset=0x0, value=0x600060015414601157600a6000f3601a565b60016001556001ff5b) + Op.SSTORE(key=0x1, value=Op.CREATE2(value=0x1, offset=0x5, size=0x1b, salt=0x0)) + Op.SSTORE(key=0x2, value=Op.CREATE2(value=0x1, offset=0x5, size=0x1b, salt=0x0)) + Op.STOP), Address("0x1f572e5295c57f15886f9b263e2f6d2d6c7b5ec6"): Account(storage={1: 0xd27e800c69122409ac5609fe4df903745f3988a0}, code=Op.MSTORE(offset=0x0, value=0x600060015414601157600a6000f3601c565b6001600155600a6000f35b) + Op.SSTORE(key=0x1, value=Op.CREATE2(value=0x1, offset=0x3, size=0x1d, salt=0x0)) + Op.SSTORE(key=0x2, value=Op.CREATE2(value=0x1, offset=0x5, size=0x1b, salt=0x0)) + Op.STOP), Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(code=Op.CALL(gas=Op.GAS, address=Op.CALLDATALOAD(offset=0x0), value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0) + Op.STOP), Address("0xd27e800c69122409ac5609fe4df903745f3988a0"): Account(storage={1: 1}, code=Op.STOP + Op.STOP + Op.STOP + Op.STOP + Op.STOP + Op.STOP + Op.STOP + Op.STOP + Op.STOP + Op.STOP)}),
    ],
    ids=['case0', 'case1'],
)
@pytest.mark.pre_alloc_mutable
def test_create2_smart_init_code(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """create2SmartInitCode. create2 works different each time you call it."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    callee = Address("0x0f572e5295c57f15886f9b263e2f6d2d6c7b5ec6")
    callee_1 = Address("0x1f572e5295c57f15886f9b263e2f6d2d6c7b5ec6")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=47244640256,
    )

    pre[callee] = Account(
        balance=100,
        nonce=0,
        code=(
        Op.MSTORE(offset=0x0, value=0x600060015414601157600a6000f3601a565b60016001556001ff5b)
        + Op.SSTORE(key=0x1, value=Op.CREATE2(value=0x1, offset=0x5, size=0x1b, salt=0x0))
        + Op.SSTORE(key=0x2, value=Op.CREATE2(value=0x1, offset=0x5, size=0x1b, salt=0x0))
        + Op.STOP
    ),
    )
    pre[callee_1] = Account(
        balance=100,
        nonce=0,
        code=(
        Op.MSTORE(offset=0x0, value=0x600060015414601157600a6000f3601c565b6001600155600a6000f35b)
        + Op.SSTORE(key=0x1, value=Op.CREATE2(value=0x1, offset=0x3, size=0x1d, salt=0x0))
        + Op.SSTORE(key=0x2, value=Op.CREATE2(value=0x1, offset=0x5, size=0x1b, salt=0x0))
        + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0x6400000000, nonce=0)
    pre[contract] = Account(
        balance=0x6400000000,
        nonce=0,
        code=(
        Op.CALL(gas=Op.GAS, address=Op.CALLDATALOAD(offset=0x0), value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)
        + Op.STOP
    ),
    )

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=tx_data,
        gas_limit=400000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
