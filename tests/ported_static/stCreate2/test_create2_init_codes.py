"""
testing different byte opcodes inside create2 init code

Ported from:
tests/static/state_tests/stCreate2/create2InitCodesFiller.json
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

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


@pytest.mark.ported_from(
    ["tests/static/state_tests/stCreate2/create2InitCodesFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        ("60006000536000600160006000f560005500", {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(storage={0: 0x9ccb06046c674d1a423c968d7998235bc33d40c1})}),
        ("60566000536000600160006000f560005500", {}),
        ("60016000536000600160006000f560005500", {}),
        ("60f46000536000600160006000f560005500", {}),
        ("6a60016001556001546002556000526000600b60156000f560005500", {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(storage={0: 0xd46f8d2a93844fb23d8a2803a615f3d00849b8ab}), Address("0xd46f8d2a93844fb23d8a2803a615f3d00849b8ab"): Account(storage={1: 1, 2: 1})}),
        ("626001ff60005260006003601d6000f560005500", {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(storage={0: 0xadf52aafb61364f699f9b15ee605ef82dca7f53d})}),
        ("626001ff60005260006003601d6001f560005500", {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(storage={0: 0xadf52aafb61364f699f9b15ee605ef82dca7f53d})}),
        ("60006003601d6000f560005500", {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(storage={0: 0x52b620d9a3fd03486496061138825a08b4da501f})}),
        ("6160a960005260006002601e6001f560005500", {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(storage={0: 0x5210981ae8161a02a1b7e37452ae142aedc66ea3})}),
    ],
    ids=['case0', 'case1', 'case2', 'case3', 'case4', 'case5', 'case6', 'case7', 'case8'],
)
@pytest.mark.pre_alloc_mutable
def test_create2_init_codes(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """testing different byte opcodes inside create2 init code."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    pre[sender] = Account(balance=0xde0b6b3a7640000, nonce=0)

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=None,
        data=tx_data,
        gas_limit=800000,
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
