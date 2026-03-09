"""
Ori Pomerantz qbzzt1@gmail.com.

Ported from:
tests/static/state_tests/VMTests/vmTests/suicideFiller.yml
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
    ["tests/static/state_tests/VMTests/vmTests/suicideFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        (
            "693c61390000000000000000000000000000000000000000000000000000000000001000",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("33ff00")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex("61deadff00")
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("30ff00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex("600060006000600060006004355af100")
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000001002",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("33ff00")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex("61deadff00")
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("30ff00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex("600060006000600060006004355af100")
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000001001",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("33ff00")
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex("61deadff00")
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex("30ff00")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex("600060006000600060006004355af100")
                ),
            },
        ),
    ],
    ids=["case0", "case1", "case2"],
)
@pytest.mark.pre_alloc_mutable
def test_suicide(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Ori Pomerantz qbzzt1@gmail.com."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xcccccccccccccccccccccccccccccccccccccccc")
    callee = Address("0x0000000000000000000000000000000000001000")
    callee_1 = Address("0x0000000000000000000000000000000000001001")
    callee_2 = Address("0x0000000000000000000000000000000000001002")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000,
    )

    pre[callee] = Account(
        balance=0xFF000000000000,
        nonce=0,
        code=bytes.fromhex("33ff00"),
    )
    pre[callee_1] = Account(
        balance=0x100000000000,
        nonce=0,
        code=bytes.fromhex("61deadff00"),
    )
    pre[callee_2] = Account(
        balance=0x100000000000,
        nonce=0,
        code=bytes.fromhex("30ff00"),
    )
    pre[sender] = Account(balance=0x5AF3107A4000, nonce=0)
    pre[contract] = Account(
        balance=0x100000000000,
        nonce=0,
        code=bytes.fromhex("600060006000600060006004355af100"),
    )

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=tx_data,
        gas_limit=16777216,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
