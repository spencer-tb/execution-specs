"""
Ori Pomerantz qbzzt1@gmail.com.

Ported from:
tests/static/state_tests/stEIP150singleCodeGasPrices/gasCostJumpFiller.yml
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
    [
        "tests/static/state_tests/stEIP150singleCodeGasPrices/gasCostJumpFiller.yml",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        (
            "c5b5a1ae00000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000004",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("600060005b5b00")
                ),
                Address("0x0000000000000000000000000000000000002000"): Account(
                    code=bytes.fromhex("60006005565b00")
                ),
                Address("0x0000000000000000000000000000000000003000"): Account(
                    code=bytes.fromhex("60016005575b00")
                ),
                Address("0x0000000000000000000000000000000000004000"): Account(
                    code=bytes.fromhex("60006005575b00")
                ),
                Address("0x095e7baea6a6c7c4c2dfeb977efac326af552d87"): Account(
                    code=bytes.fromhex(
                        "5a6000526000600060006000600061100062010000f1505a60005103602052600160043514602e57600050604e565b5a6000526000600060006000600061200062010000f1505a600051036040525b600260043514605e57600050607e565b5a6000526000600060006000600061300062010000f1505a600051036040525b600360043514608e5760005060ae565b5a6000526000600060006000600061400062010000f1505a600051036040525b602435602051604051030360005500"  # noqa: E501
                    )
                ),
            },
        ),
        (
            "c5b5a1ae00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000006",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("600060005b5b00")
                ),
                Address("0x0000000000000000000000000000000000002000"): Account(
                    code=bytes.fromhex("60006005565b00")
                ),
                Address("0x0000000000000000000000000000000000003000"): Account(
                    code=bytes.fromhex("60016005575b00")
                ),
                Address("0x0000000000000000000000000000000000004000"): Account(
                    code=bytes.fromhex("60006005575b00")
                ),
                Address("0x095e7baea6a6c7c4c2dfeb977efac326af552d87"): Account(
                    code=bytes.fromhex(
                        "5a6000526000600060006000600061100062010000f1505a60005103602052600160043514602e57600050604e565b5a6000526000600060006000600061200062010000f1505a600051036040525b600260043514605e57600050607e565b5a6000526000600060006000600061300062010000f1505a600051036040525b600360043514608e5760005060ae565b5a6000526000600060006000600061400062010000f1505a600051036040525b602435602051604051030360005500"  # noqa: E501
                    )
                ),
            },
        ),
        (
            "c5b5a1ae00000000000000000000000000000000000000000000000000000000000000030000000000000000000000000000000000000000000000000000000000000006",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("600060005b5b00")
                ),
                Address("0x0000000000000000000000000000000000002000"): Account(
                    code=bytes.fromhex("60006005565b00")
                ),
                Address("0x0000000000000000000000000000000000003000"): Account(
                    code=bytes.fromhex("60016005575b00")
                ),
                Address("0x0000000000000000000000000000000000004000"): Account(
                    code=bytes.fromhex("60006005575b00")
                ),
                Address("0x095e7baea6a6c7c4c2dfeb977efac326af552d87"): Account(
                    code=bytes.fromhex(
                        "5a6000526000600060006000600061100062010000f1505a60005103602052600160043514602e57600050604e565b5a6000526000600060006000600061200062010000f1505a600051036040525b600260043514605e57600050607e565b5a6000526000600060006000600061300062010000f1505a600051036040525b600360043514608e5760005060ae565b5a6000526000600060006000600061400062010000f1505a600051036040525b602435602051604051030360005500"  # noqa: E501
                    )
                ),
            },
        ),
    ],
    ids=["case0", "case1", "case2"],
)
@pytest.mark.pre_alloc_mutable
def test_gas_cost_jump(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Ori Pomerantz qbzzt1@gmail.com."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x095e7baea6a6c7c4c2dfeb977efac326af552d87")
    callee = Address("0x0000000000000000000000000000000000001000")
    callee_1 = Address("0x0000000000000000000000000000000000002000")
    callee_2 = Address("0x0000000000000000000000000000000000003000")
    callee_3 = Address("0x0000000000000000000000000000000000004000")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000,
    )

    pre[callee] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("600060005b5b00"),
    )
    pre[callee_1] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("60006005565b00"),
    )
    pre[callee_2] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("60016005575b00"),
    )
    pre[callee_3] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("60006005575b00"),
    )
    pre[contract] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex(
            "5a6000526000600060006000600061100062010000f1505a600051036020526001600435"  # noqa: E501
            "14602e57600050604e565b5a6000526000600060006000600061200062010000f1505a60"  # noqa: E501
            "0051036040525b600260043514605e57600050607e565b5a600052600060006000600060"  # noqa: E501
            "0061300062010000f1505a600051036040525b600360043514608e5760005060ae565b5a"  # noqa: E501
            "6000526000600060006000600061400062010000f1505a600051036040525b6024356020"  # noqa: E501
            "51604051030360005500"
        ),
        storage={0x0: 0x60A7},
    )
    pre[sender] = Account(balance=0xBA1A9CE0BA1A9CE, nonce=0)

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
        value=1,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
