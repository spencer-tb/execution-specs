"""
The first test case required here.

https://github.com/ethereum/tests/issues/431#issue-306081539

Implements: SUC007.0, SUC007.1, SUC007.2, SUC007.3,
            SUC008.0, SUC008.1, SUC008.2, SUC008.3

Ported from:
tests/static/state_tests/stSystemOperationsTest
doubleSelfdestructTestFiller.yml
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
        "tests/static/state_tests/stSystemOperationsTest/doubleSelfdestructTestFiller.yml",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        (
            "f210011002",
            {
                Address("0x000000000000000000000000000000000000c0de"): Account(
                    code=bytes.fromhex(
                        "6002361160175760003560f01c36600214601557005bff5b60003560f81c60fa61ffff60003560e81c169160ff61ffff60003560d81c16818160081c166000531660015360f181146090575b60f28114607f575b60f48114606f575b14606157ff5b60008060028161c0de5afa50ff5b60008060028161c0de5af450605b565b6000806002818061c0de5af2506053565b6000806002818061c0de5af150604b56"  # noqa: E501
                    )
                )
            },
        ),
        (
            "f410011002",
            {
                Address("0x000000000000000000000000000000000000c0de"): Account(
                    code=bytes.fromhex(
                        "6002361160175760003560f01c36600214601557005bff5b60003560f81c60fa61ffff60003560e81c169160ff61ffff60003560d81c16818160081c166000531660015360f181146090575b60f28114607f575b60f48114606f575b14606157ff5b60008060028161c0de5afa50ff5b60008060028161c0de5af450605b565b6000806002818061c0de5af2506053565b6000806002818061c0de5af150604b56"  # noqa: E501
                    )
                )
            },
        ),
        (
            "f110011002",
            {
                Address("0x000000000000000000000000000000000000c0de"): Account(
                    code=bytes.fromhex(
                        "6002361160175760003560f01c36600214601557005bff5b60003560f81c60fa61ffff60003560e81c169160ff61ffff60003560d81c16818160081c166000531660015360f181146090575b60f28114607f575b60f48114606f575b14606157ff5b60008060028161c0de5afa50ff5b60008060028161c0de5af450605b565b6000806002818061c0de5af2506053565b6000806002818061c0de5af150604b56"  # noqa: E501
                    )
                )
            },
        ),
        (
            "fa1001c0de",
            {
                Address("0x000000000000000000000000000000000000c0de"): Account(
                    code=bytes.fromhex(
                        "6002361160175760003560f01c36600214601557005bff5b60003560f81c60fa61ffff60003560e81c169160ff61ffff60003560d81c16818160081c166000531660015360f181146090575b60f28114607f575b60f48114606f575b14606157ff5b60008060028161c0de5afa50ff5b60008060028161c0de5af450605b565b6000806002818061c0de5af2506053565b6000806002818061c0de5af150604b56"  # noqa: E501
                    )
                )
            },
        ),
        (
            "fa10011002",
            {
                Address("0x000000000000000000000000000000000000c0de"): Account(
                    code=bytes.fromhex(
                        "6002361160175760003560f01c36600214601557005bff5b60003560f81c60fa61ffff60003560e81c169160ff61ffff60003560d81c16818160081c166000531660015360f181146090575b60f28114607f575b60f48114606f575b14606157ff5b60008060028161c0de5afa50ff5b60008060028161c0de5af450605b565b6000806002818061c0de5af2506053565b6000806002818061c0de5af150604b56"  # noqa: E501
                    )
                )
            },
        ),
        (
            "f21001c0de",
            {
                Address("0x000000000000000000000000000000000000c0de"): Account(
                    code=bytes.fromhex(
                        "6002361160175760003560f01c36600214601557005bff5b60003560f81c60fa61ffff60003560e81c169160ff61ffff60003560d81c16818160081c166000531660015360f181146090575b60f28114607f575b60f48114606f575b14606157ff5b60008060028161c0de5afa50ff5b60008060028161c0de5af450605b565b6000806002818061c0de5af2506053565b6000806002818061c0de5af150604b56"  # noqa: E501
                    )
                )
            },
        ),
        (
            "f41001c0de",
            {
                Address("0x000000000000000000000000000000000000c0de"): Account(
                    code=bytes.fromhex(
                        "6002361160175760003560f01c36600214601557005bff5b60003560f81c60fa61ffff60003560e81c169160ff61ffff60003560d81c16818160081c166000531660015360f181146090575b60f28114607f575b60f48114606f575b14606157ff5b60008060028161c0de5afa50ff5b60008060028161c0de5af450605b565b6000806002818061c0de5af2506053565b6000806002818061c0de5af150604b56"  # noqa: E501
                    )
                )
            },
        ),
        (
            "f11001c0de",
            {
                Address("0x000000000000000000000000000000000000c0de"): Account(
                    code=bytes.fromhex(
                        "6002361160175760003560f01c36600214601557005bff5b60003560f81c60fa61ffff60003560e81c169160ff61ffff60003560d81c16818160081c166000531660015360f181146090575b60f28114607f575b60f48114606f575b14606157ff5b60008060028161c0de5afa50ff5b60008060028161c0de5af450605b565b6000806002818061c0de5af2506053565b6000806002818061c0de5af150604b56"  # noqa: E501
                    )
                )
            },
        ),
    ],
    ids=[
        "case0",
        "case1",
        "case2",
        "case3",
        "case4",
        "case5",
        "case6",
        "case7",
    ],
)
@pytest.mark.pre_alloc_mutable
def test_double_selfdestruct_test(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """The first test case required here."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x000000000000000000000000000000000000c0de")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000000,
    )

    pre[contract] = Account(
        balance=0xF4240,
        nonce=1,
        code=bytes.fromhex(
            "6002361160175760003560f01c36600214601557005bff5b60003560f81c60fa61ffff60"  # noqa: E501
            "003560e81c169160ff61ffff60003560d81c16818160081c166000531660015360f18114"  # noqa: E501
            "6090575b60f28114607f575b60f48114606f575b14606157ff5b60008060028161c0de5a"  # noqa: E501
            "fa50ff5b60008060028161c0de5af450605b565b6000806002818061c0de5af250605356"  # noqa: E501
            "5b6000806002818061c0de5af150604b56"
        ),
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=1)

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=tx_data,
        gas_limit=16777216,
        gas_price=10,
        nonce=1,
        value=1,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
