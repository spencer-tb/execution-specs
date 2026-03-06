"""
Ported from:
tests/static/state_tests/stTransactionTest/Opcodes_TransactionInitFiller.json

contract code:
    push2 0xffff
    pop
    push1 0x04
    push1 0x00
    return

callee_1 code:
    push1 0x01
    push1 0x00
    sstore
    stop
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
    ["tests/static/state_tests/stTransactionTest/Opcodes_TransactionInitFiller.json"],
)
@pytest.mark.valid_from("Cancun")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
    pytest.param(
        "0060016000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case0",
    ),
    pytest.param(
        "60ff60ff60ff9150505060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case1",
    ),
    pytest.param(
        "60ff60ff60ff60ff925050505060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case2",
    ),
    pytest.param(
        "60ff60ff60ff60ff60ff93505050505060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case3",
    ),
    pytest.param(
        "60ff60ff60ff60ff60ff60ff9450505050505060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case4",
    ),
    pytest.param(
        "60ff60ff60ff60ff60ff60ff60ff955050505050505060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case5",
    ),
    pytest.param(
        "60ff60ff60ff60ff60ff60ff60ff60ff96505050505050505060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case6",
    ),
    pytest.param(
        "600060ff60ff60ff60ff60ff60ff60ff60ff9750505050505050505060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case7",
    ),
    pytest.param(
        "600060ff60ff60ff60ff60ff60ff60ff60ff60ff985050505050505050505060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case8",
    ),
    pytest.param(
        "600060ff60ff60ff60ff60ff60ff60ff60ff60ff60ff99505050505050505050505060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case9",
    ),
    pytest.param(
        "600060ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff9a50505050505050505050505060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case10",
    ),
    pytest.param(
        "600160010a5060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case11",
    ),
    pytest.param(
        "600060ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff9b5050505050505050505050505060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case12",
    ),
    pytest.param(
        "600060ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff9c505050505050505050505050505060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case13",
    ),
    pytest.param(
        "600060ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff9d50505050505050505050505050505060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case14",
    ),
    pytest.param(
        "600060ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff9e5050505050505050505050505050505060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case15",
    ),
    pytest.param(
        "600060ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff9f505050505050505050505050505050505060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case16",
    ),
    pytest.param(
        "60006000a060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case17",
    ),
    pytest.param(
        "60ff60006000a160006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case18",
    ),
    pytest.param(
        "60ff60ff60006000a260006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case19",
    ),
    pytest.param(
        "60ff60ff60ff60006000a360006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case20",
    ),
    pytest.param(
        "60ff60ff60ff60ff60006000a460006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case21",
    ),
    pytest.param(
        "600160010b5060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case22",
    ),
    pytest.param(
        "6000600060fff05060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case23",
    ),
    pytest.param(
        "60006000600060006017730f572e5295c57f15886f9b263e2f6d2d6c7b5ec66064f15060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case24",
    ),
    pytest.param(
        "60006000600060006000730f572e5295c57f15886f9b263e2f6d2d6c7b5ec66064f25060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case25",
    ),
    pytest.param(
        "60006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case26",
    ),
    pytest.param(
        "6000600060006000730f572e5295c57f15886f9b263e2f6d2d6c7b5ec6620186a0f45060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case27",
    ),
    pytest.param(
        "6000600060006000730f572e5295c57f15886f9b263e2f6d2d6c7b5ec6612710fa5060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case28",
    ),
    pytest.param(
        "60006000fd60006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case29",
    ),
    pytest.param(
        "32ff",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case30",
    ),
    pytest.param(
        "60016001105060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case31",
    ),
    pytest.param(
        "60016001115060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case32",
    ),
    pytest.param(
        "60016001125060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(storage={0: 0x38600060013960015160005560006000f3000000000000000000000000000000}, nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case33",
    ),
    pytest.param(
        "60016001135060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case34",
    ),
    pytest.param(
        "60016001145060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case35",
    ),
    pytest.param(
        "6000155060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case36",
    ),
    pytest.param(
        "60006000165060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case37",
    ),
    pytest.param(
        "60006000175060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case38",
    ),
    pytest.param(
        "60016001015060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case39",
    ),
    pytest.param(
        "60006000185060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case40",
    ),
    pytest.param(
        "6000195060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case41",
    ),
    pytest.param(
        "67805020100804020160001a5060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case42",
    ),
    pytest.param(
        "600060002060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case43",
    ),
    pytest.param(
        "305060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case44",
    ),
    pytest.param(
        "6000315060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case45",
    ),
    pytest.param(
        "325060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case46",
    ),
    pytest.param(
        "335060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case47",
    ),
    pytest.param(
        "345060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case48",
    ),
    pytest.param(
        "6000355060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case49",
    ),
    pytest.param(
        "60016001025060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case50",
    ),
    pytest.param(
        "365060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case51",
    ),
    pytest.param(
        "6000600060003760006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case52",
    ),
    pytest.param(
        "385060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case53",
    ),
    pytest.param(
        "38600060013960015160005560006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case54",
    ),
    pytest.param(
        "3a5060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case55",
    ),
    pytest.param(
        "60003b5060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case56",
    ),
    pytest.param(
        "6014600060007310000000000000000000000000000000000000103c60006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case57",
    ),
    pytest.param(
        "3d5060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case58",
    ),
    pytest.param(
        "6000600060003e60006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case59",
    ),
    pytest.param(
        "60005060005060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case60",
    ),
    pytest.param(
        "60016001035060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case61",
    ),
    pytest.param(
        "6000515060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case62",
    ),
    pytest.param(
        "600060005260006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case63",
    ),
    pytest.param(
        "60ff60005360006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case64",
    ),
    pytest.param(
        "6000545060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case65",
    ),
    pytest.param(
        "600160015560006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case66",
    ),
    pytest.param(
        "600456005b60006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case67",
    ),
    pytest.param(
        "6001600657005b60006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case68",
    ),
    pytest.param(
        "585060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case69",
    ),
    pytest.param(
        "595060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case70",
    ),
    pytest.param(
        "5a5060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case71",
    ),
    pytest.param(
        "60016001045060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case72",
    ),
    pytest.param(
        "5b60006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case73",
    ),
    pytest.param(
        "60ff5060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case74",
    ),
    pytest.param(
        "61ffff5060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case75",
    ),
    pytest.param(
        "62ffffff5060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case76",
    ),
    pytest.param(
        "63ffffffff5060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case77",
    ),
    pytest.param(
        "64ffffffffff5060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case78",
    ),
    pytest.param(
        "65ffffffffffff5060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case79",
    ),
    pytest.param(
        "66ffffffffffffff5060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case80",
    ),
    pytest.param(
        "67ffffffffffffffff5060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case81",
    ),
    pytest.param(
        "68ffffffffffffffffff5060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case82",
    ),
    pytest.param(
        "60016001055060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case83",
    ),
    pytest.param(
        "69ffffffffffffffffffff5060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case84",
    ),
    pytest.param(
        "6affffffffffffffffffffff5060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case85",
    ),
    pytest.param(
        "6bffffffffffffffffffffffff5060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case86",
    ),
    pytest.param(
        "6cffffffffffffffffffffffffff5060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case87",
    ),
    pytest.param(
        "6dffffffffffffffffffffffffffff5060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case88",
    ),
    pytest.param(
        "6effffffffffffffffffffffffffffff5060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case89",
    ),
    pytest.param(
        "6fffffffffffffffffffffffffffffffff5060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case90",
    ),
    pytest.param(
        "70ffffffffffffffffffffffffffffffffff5060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case91",
    ),
    pytest.param(
        "71ffffffffffffffffffffffffffffffffffff5060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case92",
    ),
    pytest.param(
        "72ffffffffffffffffffffffffffffffffffffff5060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case93",
    ),
    pytest.param(
        "60016001065060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case94",
    ),
    pytest.param(
        "73ffffffffffffffffffffffffffffffffffffffff5060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case95",
    ),
    pytest.param(
        "74ffffffffffffffffffffffffffffffffffffffffff5060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case96",
    ),
    pytest.param(
        "75ffffffffffffffffffffffffffffffffffffffffffff5060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case97",
    ),
    pytest.param(
        "76ffffffffffffffffffffffffffffffffffffffffffffff5060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case98",
    ),
    pytest.param(
        "77ffffffffffffffffffffffffffffffffffffffffffffffff5060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case99",
    ),
    pytest.param(
        "78ffffffffffffffffffffffffffffffffffffffffffffffffff5060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case100",
    ),
    pytest.param(
        "79ffffffffffffffffffffffffffffffffffffffffffffffffffff5060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case101",
    ),
    pytest.param(
        "7affffffffffffffffffffffffffffffffffffffffffffffffffffff5060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case102",
    ),
    pytest.param(
        "7bffffffffffffffffffffffffffffffffffffffffffffffffffffffff5060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case103",
    ),
    pytest.param(
        "7cffffffffffffffffffffffffffffffffffffffffffffffffffffffffff5060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case104",
    ),
    pytest.param(
        "60016001075060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case105",
    ),
    pytest.param(
        "7dffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff5060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case106",
    ),
    pytest.param(
        "7effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff5060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case107",
    ),
    pytest.param(
        "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff5060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case108",
    ),
    pytest.param(
        "60ff80505060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case109",
    ),
    pytest.param(
        "60ff60ff8150505060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case110",
    ),
    pytest.param(
        "60ff60ff60ff825050505060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case111",
    ),
    pytest.param(
        "60ff60ff60ff60ff83505050505060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case112",
    ),
    pytest.param(
        "60ff60ff60ff60ff60ff8450505050505060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case113",
    ),
    pytest.param(
        "60ff60ff60ff60ff60ff60ff855050505050505060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case114",
    ),
    pytest.param(
        "60ff60ff60ff60ff60ff60ff60ff86505050505050505060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case115",
    ),
    pytest.param(
        "600160016001085060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case116",
    ),
    pytest.param(
        "60ff60ff60ff60ff60ff60ff60ff60ff8750505050505050505060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case117",
    ),
    pytest.param(
        "60ff60ff60ff60ff60ff60ff60ff60ff60ff885050505050505050505060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case118",
    ),
    pytest.param(
        "60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff89505050505050505050505060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case119",
    ),
    pytest.param(
        "60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff8a50505050505050505050505060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=2), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case120",
    ),
    pytest.param(
        "60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff8b5050505050505050505050505060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case121",
    ),
    pytest.param(
        "60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff8c505050505050505050505050505060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case122",
    ),
    pytest.param(
        "60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff8d50505050505050505050505050505060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case123",
    ),
    pytest.param(
        "60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff8e5050505050505050505050505050505060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case124",
    ),
    pytest.param(
        "60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff60ff8f505050505050505050505050505050505060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=1), Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case125",
    ),
    pytest.param(
        "60ff60ff90505060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account.NONEXISTENT, Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case126",
    ),
    pytest.param(
        "600160016001095060006000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account.NONEXISTENT, Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case127",
    ),
    pytest.param(
        "ef",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account.NONEXISTENT, Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case128",
    ),
    pytest.param(
        "60008080808073b94f5374fce5edbc8e2a8697c15331677e6ebf0b61c350f100",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account.NONEXISTENT, Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case129",
    ),
    pytest.param(
        "60008080808073b94f5374fce5edbc8e2a8697c15331677e6ebf0b61c350f150fe",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account.NONEXISTENT, Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case130",
    ),
    pytest.param(
        "60008080808073b94f5374fce5edbc8e2a8697c15331677e6ebf0b61c350f15060ef60005360016000f3",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account.NONEXISTENT, Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(nonce=1)},
        id="case131",
    ),
    ],
)
@pytest.mark.pre_alloc_mutable
def test_opcodes_transaction_init(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x0f572e5295c57f15886f9b263e2f6d2d6c7b5ec6")
    callee_1 = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    pre[contract] = Account(
        balance=0xde0b6b3a7640000,
        nonce=1,
        code=Op.PUSH2[0xffff] + Op.POP + Op.PUSH1[0x4] + Op.PUSH1[0x0] + Op.RETURN,
    )
    pre[sender] = Account(balance=0xde0b6b3a7640000, nonce=0, storage={0x0: 0x0})
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=Op.PUSH1[0x1] + Op.PUSH1[0x0] + Op.SSTORE + Op.STOP,
    )

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=None,
        data=tx_data,
        gas_limit=400000,
        gas_price=10,
        nonce=0,
        value=100000,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
