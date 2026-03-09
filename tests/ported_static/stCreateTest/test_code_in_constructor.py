"""
Ori Pomerantz qbzzt1@gmail.com.

Ported from:
tests/static/state_tests/stCreateTest/CodeInConstructorFiller.yml
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
    ["tests/static/state_tests/stCreateTest/CodeInConstructorFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        (
            "83c7d7580000000000000000000000000000000000000000000000000000000000000001",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000da7a"): Account(
                    storage={
                        0: 8,
                        1: 10,
                        2: 0x8AF6A7AF30D840BA137E8F3F34D54CFB8BEBA6E2,
                        3: 262,
                        5: 0x610100610100610100395861026052600060006020610260600061DA7A62FFFF,  # noqa: E501
                        7: 184,
                    },
                    code=bytes.fromhex("6000356000545560016000540160005500"),
                ),
                Address("0x8af6a7af30d840ba137e8f3f34d54cfb8beba6e2"): Account(
                    code=bytes.fromhex("000000000000")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "60068061004c610100396102005260db8061005260003961022052600160043514603757615a17610200516101000160006000f56045565b610200516101000160006000f05b6102405200fe60ff60005500610100610100610100395861026052600060006020610260600061da7a62fffffff1503061026052600060006020610260600061da7a62fffffff1503861026052600060006020610260600061da7a62fffffff150303b61026052600060006020610260600061da7a62fffffff15060206000610100396101005161026052600060006020610260600061da7a62fffffff15060206000610100303c6101005161026052600060006020610260600061da7a62fffffff1505861026052600060006020610260600061da7a62fffffff1506101003803610100f300"  # noqa: E501
                    )
                ),
            },
        ),
        (
            "83c7d7580000000000000000000000000000000000000000000000000000000000000002",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000da7a"): Account(
                    storage={
                        0: 8,
                        1: 10,
                        2: 0x33C409678A4289F0184C95C627BA09DA2DAEAA46,
                        3: 262,
                        5: 0x610100610100610100395861026052600060006020610260600061DA7A62FFFF,  # noqa: E501
                        7: 184,
                    },
                    code=bytes.fromhex("6000356000545560016000540160005500"),
                ),
                Address("0x33c409678a4289f0184c95c627ba09da2daeaa46"): Account(
                    code=bytes.fromhex("000000000000")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "60068061004c610100396102005260db8061005260003961022052600160043514603757615a17610200516101000160006000f56045565b610200516101000160006000f05b6102405200fe60ff60005500610100610100610100395861026052600060006020610260600061da7a62fffffff1503061026052600060006020610260600061da7a62fffffff1503861026052600060006020610260600061da7a62fffffff150303b61026052600060006020610260600061da7a62fffffff15060206000610100396101005161026052600060006020610260600061da7a62fffffff15060206000610100303c6101005161026052600060006020610260600061da7a62fffffff1505861026052600060006020610260600061da7a62fffffff1506101003803610100f300"  # noqa: E501
                    )
                ),
            },
        ),
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_code_in_constructor(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Ori Pomerantz qbzzt1@gmail.com."""
    coinbase = Address("0xba5e0000ba5e0000ba5e0000ba5e0000ba5e0000")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xcccccccccccccccccccccccccccccccccccccccc")
    callee = Address("0x000000000000000000000000000000000000da7a")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=4294967296,
    )

    pre[callee] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("6000356000545560016000540160005500"),
        storage={0x0: 0x1},
    )
    pre[sender] = Account(balance=0xBA1A9CE0BA1A9CE, nonce=0)
    pre[contract] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex(
            "60068061004c610100396102005260db8061005260003961022052600160043514603757"  # noqa: E501
            "615a17610200516101000160006000f56045565b610200516101000160006000f05b6102"  # noqa: E501
            "405200fe60ff600055006101006101006101003958610260526000600060206102606000"  # noqa: E501
            "61da7a62fffffff1503061026052600060006020610260600061da7a62fffffff1503861"  # noqa: E501
            "026052600060006020610260600061da7a62fffffff150303b6102605260006000602061"  # noqa: E501
            "0260600061da7a62fffffff1506020600061010039610100516102605260006000602061"  # noqa: E501
            "0260600061da7a62fffffff15060206000610100303c6101005161026052600060006020"  # noqa: E501
            "610260600061da7a62fffffff1505861026052600060006020610260600061da7a62ffff"  # noqa: E501
            "fff1506101003803610100f300"
        ),
    )

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=tx_data,
        gas_limit=9437184,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
