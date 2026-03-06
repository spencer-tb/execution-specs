"""
CREATE2 suicide with/without value, CREATE2 suicide to itself   +  this cases during init of the CREATE2

Ported from:
tests/static/state_tests/stCreate2/CREATE2_SuicideFiller.json
"""

import pytest
from execution_testing.vm import Op
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
    ["tests/static/state_tests/stCreate2/CREATE2_SuicideFiller.json"],
)
@pytest.mark.valid_from("Cancun")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
    pytest.param(
        "626001ff60005260006003601d6000f500",
        {Address("0x0000000000000000000000000000000000000001"): Account.NONEXISTENT, Address("0x5649527a8464a86cae579719d347065f6eb27279"): Account.NONEXISTENT, Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=2)},
        id="case0",
    ),
    pytest.param(
        "6a6130ff6000526002601ef36000526000600b60156000f5506000600060006000736cd0e5133771823da00d4cb545ec8cdab0e38203620249f0fa00",
        {Address("0x0000000000000000000000000000000000000001"): Account.NONEXISTENT, Address("0x5649527a8464a86cae579719d347065f6eb27279"): Account.NONEXISTENT, Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=2)},
        id="case1",
    ),
    pytest.param(
        "6a6130ff6000526002601ef36000526000600b60156001f5506000600060006000736cd0e5133771823da00d4cb545ec8cdab0e38203620249f0fa00",
        {Address("0x0000000000000000000000000000000000000001"): Account(balance=1), Address("0x5649527a8464a86cae579719d347065f6eb27279"): Account.NONEXISTENT, Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=2)},
        id="case2",
    ),
    pytest.param(
        "6b626001ff6000526003601df36000526000600c60146000f55060006000600060006000735649527a8464a86cae579719d347065f6eb27279620249f0f100",
        {Address("0x0000000000000000000000000000000000000001"): Account(balance=1), Address("0x5649527a8464a86cae579719d347065f6eb27279"): Account.NONEXISTENT, Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=2)},
        id="case3",
    ),
    pytest.param(
        "626001ff60005260006003601d6001f500",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=2), Address("0x6cd0e5133771823da00d4cb545ec8cdab0e38203"): Account.NONEXISTENT},
        id="case4",
    ),
    pytest.param(
        "6b626001ff6000526003601df36000526000600c60146001f55060006000600060006000735649527a8464a86cae579719d347065f6eb27279620249f0f100",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=2), Address("0x6cd0e5133771823da00d4cb545ec8cdab0e38203"): Account.NONEXISTENT},
        id="case5",
    ),
    pytest.param(
        "6130ff60005260006002601e6000f500",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=2, balance=9), Address("0x6cd0e5133771823da00d4cb545ec8cdab0e38203"): Account.NONEXISTENT},
        id="case6",
    ),
    pytest.param(
        "6a6130ff6000526002601ef36000526000600b60156000f55060006000600060006000736cd0e5133771823da00d4cb545ec8cdab0e38203620249f0f100",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=2, balance=9), Address("0x6cd0e5133771823da00d4cb545ec8cdab0e38203"): Account.NONEXISTENT},
        id="case7",
    ),
    pytest.param(
        "6130ff60005260006002601e6001f500",
        {Address("0x5649527a8464a86cae579719d347065f6eb27279"): Account(code=Op.PUSH1[0x1] + Op.SELFDESTRUCT), Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=2)},
        id="case8",
    ),
    pytest.param(
        "6a6130ff6000526002601ef36000526000600b60156001f55060006000600060006000736cd0e5133771823da00d4cb545ec8cdab0e38203620249f0f100",
        {Address("0x5649527a8464a86cae579719d347065f6eb27279"): Account(code=Op.PUSH1[0x1] + Op.SELFDESTRUCT), Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=2)},
        id="case9",
    ),
    pytest.param(
        "6b626001ff6000526003601df36000526000600c60146000f5506000600060006000735649527a8464a86cae579719d347065f6eb27279620249f0fa00",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=2), Address("0x6cd0e5133771823da00d4cb545ec8cdab0e38203"): Account(code=Op.ADDRESS + Op.SELFDESTRUCT)},
        id="case10",
    ),
    pytest.param(
        "6b626001ff6000526003601df36000526000600c60146001f5506000600060006000735649527a8464a86cae579719d347065f6eb27279620249f0fa00",
        {Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(nonce=2), Address("0x6cd0e5133771823da00d4cb545ec8cdab0e38203"): Account(code=Op.ADDRESS + Op.SELFDESTRUCT)},
        id="case11",
    ),
    ],
)
@pytest.mark.pre_alloc_mutable
def test_create2_suicide(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """CREATE2 suicide with/without value, CREATE2 suicide to itself   +  this cases during init of the CREATE2."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[sender] = Account(balance=0xe8d4a51000, nonce=0)

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=None,
        data=tx_data,
        gas_limit=600000,
        gas_price=10,
        nonce=0,
        value=10,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
