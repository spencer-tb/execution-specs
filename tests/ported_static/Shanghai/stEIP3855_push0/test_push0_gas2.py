"""
Test ported from static filler.

Ported from:
tests/static/state_tests/Shanghai/stEIP3855_push0/push0Gas2Filler.yml
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
    ["tests/static/state_tests/Shanghai/stEIP3855_push0/push0Gas2Filler.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        (
            "0000000000000000000000000000000000001000",
            {
                Address("0x0000000000000000000000000000000000000200"): Account(
                    code=bytes.fromhex("5a60005a9091039055")
                ),
                Address("0x0000000000000000000000000000000000001000"): Account(
                    storage={0: 4}, code=bytes.fromhex("5a5f5a9091039055")
                ),
                Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(
                    storage={0: 1, 1: 1},
                    code=bytes.fromhex(
                        "600080808080803560601c620186a0f16000556001805500"
                    ),
                ),
            },
        ),
        (
            "0000000000000000000000000000000000000200",
            {
                Address("0x0000000000000000000000000000000000000200"): Account(
                    storage={0: 5}, code=bytes.fromhex("5a60005a9091039055")
                ),
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("5a5f5a9091039055")
                ),
                Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(
                    storage={0: 1, 1: 1},
                    code=bytes.fromhex(
                        "600080808080803560601c620186a0f16000556001805500"
                    ),
                ),
            },
        ),
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_push0_gas2(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    callee = Address("0x0000000000000000000000000000000000000200")
    callee_1 = Address("0x0000000000000000000000000000000000001000")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=89128960,
    )

    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("5a60005a9091039055"),
    )
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("5a5f5a9091039055"),
    )
    pre[sender] = Account(balance=0x989680, nonce=0)
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("600080808080803560601c620186a0f16000556001805500"),
    )

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=tx_data,
        gas_limit=300000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
