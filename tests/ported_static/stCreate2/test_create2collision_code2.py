"""
collision with the contract that already has the same init code that we are...

Ported from:
tests/static/state_tests/stCreate2/create2collisionCode2Filler.json
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
    ["tests/static/state_tests/stCreate2/create2collisionCode2Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex",
    [
        "6b620102036000526003601df36000526000600c60146000f500",
        "6b620102036000526003601df36000526000600c60146001f500",
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_create2collision_code2(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
) -> None:
    """Collision with the contract that already has the same init code..."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xfce41d047b4a1d4450382dcc29ec7e5fedc5f9a3")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)
    # Source: raw bytecode
    pre[contract] = Account(balance=0, nonce=1, code=Op.SUB(Op.MUL, Op.ADD))

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=None,
        data=tx_data,
        gas_limit=400000,
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = {
        contract: Account(code=Op.SUB(Op.MUL, Op.ADD)),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
