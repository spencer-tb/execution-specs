"""
RevertOpcodeCreate for CREATE2.

Ported from:
tests/static/state_tests/stCreate2/RevertOpcodeCreateFiller.json
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
    ["tests/static/state_tests/stCreate2/RevertOpcodeCreateFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit, expected_post",
    [
        (
            460000,
            {
                Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(
                    storage={0: 12},
                    code=bytes.fromhex(
                        "6e600160005560016000fd60116001556000526000600f60116001f5600155600c60005500"  # noqa: E501
                    ),
                )
            },
        ),
        (
            70000,
            {
                Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(
                    code=bytes.fromhex(
                        "6e600160005560016000fd60116001556000526000600f60116001f5600155600c60005500"  # noqa: E501
                    )
                )
            },
        ),
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_revert_opcode_create(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
    expected_post: dict,
) -> None:
    """RevertOpcodeCreate for CREATE2."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[sender] = Account(balance=0xE8D4A51000, nonce=0)
    pre[contract] = Account(
        balance=1,
        nonce=0,
        code=bytes.fromhex(
            "6e600160005560016000fd60116001556000526000600f60116001f5600155600c600055"  # noqa: E501
            "00"
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex("600160005560016000fe6011600155"),
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
