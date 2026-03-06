"""
account already has storage X. create -> in init code change that account's storage -> 0 -> change it to X again 

Ported from:
tests/static/state_tests/stSStoreTest/sstore_changeFromExternalCallInInitCodeFiller.json

contract code:
    push1 0x00
    push1 0x01
    sstore
    push1 0x01
    push1 0x01
    sstore
    push1 0x01
    push1 0x00
    sstore
    stop

callee_1 code:
    push1 0x01
    push1 0x01
    sstore
    push1 0x00
    push1 0x01
    sstore
    push1 0x01
    push1 0x02
    sstore
    push1 0x00
    push1 0x02
    sstore
    push1 0x01
    push1 0x03
    sstore
    push1 0x00
    push1 0x03
    sstore
    push1 0x01
    push1 0x04
    ... (80 more instructions)
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
    ["tests/static/state_tests/stSStoreTest/sstore_changeFromExternalCallInInitCodeFiller.json"],
)
@pytest.mark.valid_from("Cancun")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
    pytest.param(
        "6000600060006000600073bea0000000000000000000000000000000000000620186a0f100",
        {Address("0xbea0000000000000000000000000000000000000"): Account(storage={0: 1, 1: 1}, nonce=0)},
        id="case0",
    ),
    pytest.param(
        "6000602380601860003960006000f55060006000fd0000fe600060006000600073bea0000000000000000000000000000000000000620186a0f400",
        {Address("0xbea0000000000000000000000000000000000000"): Account(storage={0: 1, 1: 1}, nonce=0)},
        id="case1",
    ),
    pytest.param(
        "6000602380603860003960006000f5506000600060006000600073dea000000000000000000000000000000000000062030d40f1500000fe600060006000600073bea0000000000000000000000000000000000000620186a0f400",
        {Address("0x6602cfc925be62bf18470598a98f72812a1ebef2"): Account.NONEXISTENT, Address("0xbea0000000000000000000000000000000000000"): Account(storage={0: 0, 1: 1}, nonce=0)},
        id="case2",
    ),
    pytest.param(
        "600060006000600073bea0000000000000000000000000000000000000620186a0fa00",
        {Address("0xbea0000000000000000000000000000000000000"): Account(storage={0: 1, 1: 1}, nonce=0)},
        id="case3",
    ),
    pytest.param(
        "6000602380601360003960006000f5500000fe600060006000600073bea0000000000000000000000000000000000000620186a0fa00",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(storage={0: 1, 1: 1}, nonce=1), Address("0xbea0000000000000000000000000000000000000"): Account(storage={0: 0, 1: 1}, nonce=0)},
        id="case4",
    ),
    pytest.param(
        "6000602380601860003960006000f55060006000fd0000fe600060006000600073bea0000000000000000000000000000000000000620186a0fa00",
        {Address("0x0f446e1bd7a5da68b5e3a305c7030e3aa8efc293"): Account(storage={0: 1, 1: 1}, nonce=1), Address("0xbea0000000000000000000000000000000000000"): Account(storage={0: 0, 1: 1}, nonce=0)},
        id="case5",
    ),
    pytest.param(
        "6000602380603860003960006000f5506000600060006000600073dea000000000000000000000000000000000000062030d40f1500000fe600060006000600073bea0000000000000000000000000000000000000620186a0fa00",
        {Address("0x6602cfc925be62bf18470598a98f72812a1ebef2"): Account.NONEXISTENT, Address("0xbea0000000000000000000000000000000000000"): Account(storage={0: 0, 1: 1}, nonce=0)},
        id="case6",
    ),
    pytest.param(
        "6000602580601360003960006000f5500000fe6000600060006000600073bea0000000000000000000000000000000000000620186a0f100",
        {Address("0x0f446e1bd7a5da68b5e3a305c7030e3aa8efc293"): Account(storage={0: 1, 1: 1}, nonce=1), Address("0xbea0000000000000000000000000000000000000"): Account(storage={0: 0, 1: 1}, nonce=0)},
        id="case7",
    ),
    pytest.param(
        "6000602580601860003960006000f55060006000fd0000fe6000600060006000600073bea0000000000000000000000000000000000000620186a0f100",
        {Address("0x6602cfc925be62bf18470598a98f72812a1ebef2"): Account.NONEXISTENT, Address("0xbea0000000000000000000000000000000000000"): Account(storage={0: 0, 1: 1}, nonce=0)},
        id="case8",
    ),
    pytest.param(
        "6000602580603860003960006000f5506000600060006000600073dea000000000000000000000000000000000000062030d40f1500000fe6000600060006000600073bea0000000000000000000000000000000000000620186a0f100",
        {Address("0x6602cfc925be62bf18470598a98f72812a1ebef2"): Account.NONEXISTENT, Address("0xbea0000000000000000000000000000000000000"): Account(storage={0: 0, 1: 1}, nonce=0)},
        id="case9",
    ),
    pytest.param(
        "6000600060006000600073bea0000000000000000000000000000000000000620186a0f200",
        {Address("0x6602cfc925be62bf18470598a98f72812a1ebef2"): Account.NONEXISTENT, Address("0xbea0000000000000000000000000000000000000"): Account(storage={0: 0, 1: 1}, nonce=0)},
        id="case10",
    ),
    pytest.param(
        "6000602580601360003960006000f5500000fe6000600060006000600073bea0000000000000000000000000000000000000620186a0f200",
        {Address("0x6602cfc925be62bf18470598a98f72812a1ebef2"): Account.NONEXISTENT, Address("0xbea0000000000000000000000000000000000000"): Account(storage={0: 0, 1: 1}, nonce=0)},
        id="case11",
    ),
    pytest.param(
        "6000602580601860003960006000f55060006000fd0000fe6000600060006000600073bea0000000000000000000000000000000000000620186a0f200",
        {Address("0x6602cfc925be62bf18470598a98f72812a1ebef2"): Account.NONEXISTENT, Address("0xbea0000000000000000000000000000000000000"): Account(storage={0: 0, 1: 1}, nonce=0)},
        id="case12",
    ),
    pytest.param(
        "6000602580603860003960006000f5506000600060006000600073dea000000000000000000000000000000000000062030d40f1500000fe6000600060006000600073bea0000000000000000000000000000000000000620186a0f200",
        {Address("0x6602cfc925be62bf18470598a98f72812a1ebef2"): Account.NONEXISTENT, Address("0xbea0000000000000000000000000000000000000"): Account(storage={0: 0, 1: 1}, nonce=0)},
        id="case13",
    ),
    pytest.param(
        "600060006000600073bea0000000000000000000000000000000000000620186a0f400",
        {Address("0x6602cfc925be62bf18470598a98f72812a1ebef2"): Account.NONEXISTENT, Address("0xbea0000000000000000000000000000000000000"): Account(storage={0: 0, 1: 1}, nonce=0)},
        id="case14",
    ),
    pytest.param(
        "6000602380601360003960006000f5500000fe600060006000600073bea0000000000000000000000000000000000000620186a0f400",
        {Address("0x6602cfc925be62bf18470598a98f72812a1ebef2"): Account.NONEXISTENT, Address("0xbea0000000000000000000000000000000000000"): Account(storage={0: 0, 1: 1}, nonce=0)},
        id="case15",
    ),
    ],
)
@pytest.mark.pre_alloc_mutable
def test_sstore_change_from_external_call_in_init_code(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """account already has storage X. create -> in init code change that account's storage -> 0 -> change it to X again ."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xbea0000000000000000000000000000000000000")
    callee_1 = Address("0xdea0000000000000000000000000000000000000")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[sender] = Account(balance=0xe8d4a51000, nonce=0)
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH1[0x0] + Op.PUSH1[0x1] + Op.SSTORE + Op.PUSH1[0x1] + Op.PUSH1[0x1]
        + Op.SSTORE + Op.PUSH1[0x1] + Op.PUSH1[0x0] + Op.SSTORE + Op.STOP
    ),
        storage={0x1: 0x1},
    )
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH1[0x1] + Op.PUSH1[0x1] + Op.SSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x1]
        + Op.SSTORE + Op.PUSH1[0x1] + Op.PUSH1[0x2] + Op.SSTORE + Op.PUSH1[0x0]
        + Op.PUSH1[0x2] + Op.SSTORE + Op.PUSH1[0x1] + Op.PUSH1[0x3] + Op.SSTORE
        + Op.PUSH1[0x0] + Op.PUSH1[0x3] + Op.SSTORE + Op.PUSH1[0x1] + Op.PUSH1[0x4]
        + Op.SSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x4] + Op.SSTORE + Op.PUSH1[0x1]
        + Op.PUSH1[0x5] + Op.SSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x5] + Op.SSTORE
        + Op.PUSH1[0x1] + Op.PUSH1[0x6] + Op.SSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x6]
        + Op.SSTORE + Op.PUSH1[0x1] + Op.PUSH1[0x7] + Op.SSTORE + Op.PUSH1[0x0]
        + Op.PUSH1[0x7] + Op.SSTORE + Op.PUSH1[0x1] + Op.PUSH1[0x8] + Op.SSTORE
        + Op.PUSH1[0x0] + Op.PUSH1[0x8] + Op.SSTORE + Op.PUSH1[0x1] + Op.PUSH1[0x9]
        + Op.SSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x9] + Op.SSTORE + Op.PUSH1[0x1]
        + Op.PUSH1[0xa] + Op.SSTORE + Op.PUSH1[0x0] + Op.PUSH1[0xa] + Op.SSTORE
        + Op.PUSH1[0x1] + Op.PUSH1[0xb] + Op.SSTORE + Op.PUSH1[0x0] + Op.PUSH1[0xb]
        + Op.SSTORE + Op.PUSH1[0x1] + Op.PUSH1[0xc] + Op.SSTORE + Op.PUSH1[0x0]
        + Op.PUSH1[0xc] + Op.SSTORE + Op.PUSH1[0x1] + Op.PUSH1[0xd] + Op.SSTORE
        + Op.PUSH1[0x0] + Op.PUSH1[0xd] + Op.SSTORE + Op.PUSH1[0x1] + Op.PUSH1[0xe]
        + Op.SSTORE + Op.PUSH1[0x0] + Op.PUSH1[0xe] + Op.SSTORE + Op.PUSH1[0x1]
        + Op.PUSH1[0xf] + Op.SSTORE + Op.PUSH1[0x0] + Op.PUSH1[0xf] + Op.SSTORE
        + Op.PUSH1[0x1] + Op.PUSH1[0x10] + Op.SSTORE + Op.PUSH1[0x0] + Op.PUSH1[0x10]
        + Op.SSTORE + Op.PUSH1[0x1] + Op.PUSH1[0x1] + Op.SSTORE + Op.STOP
    ),
    )

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=None,
        data=tx_data,
        gas_limit=200000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
