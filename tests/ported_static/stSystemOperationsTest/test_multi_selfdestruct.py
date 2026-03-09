"""
Implements: SUC000, SUC001, SUC002, SUC003, SUC004, SUC005.

Ported from:
tests/static/state_tests/stSystemOperationsTest/multiSelfdestructFiller.yml
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
        "tests/static/state_tests/stSystemOperationsTest/multiSelfdestructFiller.yml",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        (
            "01",
            {
                Address("0x000000000000000000000000000000000000dead"): Account(
                    code=bytes.fromhex(
                        "60003560f81c61ffff60003560e81c166000821460345760ff821460325760008080809481945af114602d57005b600080fd5bff5b00"  # noqa: E501
                    )
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 1, 1: 3, 16: 1, 17: 3, 18: 2},
                    code=bytes.fromhex(
                        "60ff600053601060015360006002536000806003818061dead5af16000556110003160015561dead3160025560003560f81c8060011460ce578060021460bc578060031460a55780600414608a57600514605857600080fd5b60016000536001600253600080600381600261dead5af15b6010556110003160115561dead3160125561100131601355005b50600160005360016002536000806003818061dead5af16070565b506001600253600080600381600261dead5af16070565b50600080600381600261dead5af16070565b50600080600380600261dead5af1607056"  # noqa: E501
                    ),
                ),
            },
        ),
        (
            "02",
            {
                Address("0x000000000000000000000000000000000000dead"): Account(
                    code=bytes.fromhex(
                        "60003560f81c61ffff60003560e81c166000821460345760ff821460325760008080809481945af114602d57005b600080fd5bff5b00"  # noqa: E501
                    )
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 1, 1: 3, 16: 1, 17: 5},
                    code=bytes.fromhex(
                        "60ff600053601060015360006002536000806003818061dead5af16000556110003160015561dead3160025560003560f81c8060011460ce578060021460bc578060031460a55780600414608a57600514605857600080fd5b60016000536001600253600080600381600261dead5af15b6010556110003160115561dead3160125561100131601355005b50600160005360016002536000806003818061dead5af16070565b506001600253600080600381600261dead5af16070565b50600080600381600261dead5af16070565b50600080600380600261dead5af1607056"  # noqa: E501
                    ),
                ),
            },
        ),
        (
            "03",
            {
                Address("0x000000000000000000000000000000000000dead"): Account(
                    code=bytes.fromhex(
                        "60003560f81c61ffff60003560e81c166000821460345760ff821460325760008080809481945af114602d57005b600080fd5bff5b00"  # noqa: E501
                    )
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 1, 1: 3, 16: 1, 17: 3, 19: 2},
                    code=bytes.fromhex(
                        "60ff600053601060015360006002536000806003818061dead5af16000556110003160015561dead3160025560003560f81c8060011460ce578060021460bc578060031460a55780600414608a57600514605857600080fd5b60016000536001600253600080600381600261dead5af15b6010556110003160115561dead3160125561100131601355005b50600160005360016002536000806003818061dead5af16070565b506001600253600080600381600261dead5af16070565b50600080600381600261dead5af16070565b50600080600380600261dead5af1607056"  # noqa: E501
                    ),
                ),
            },
        ),
        (
            "04",
            {
                Address("0x000000000000000000000000000000000000dead"): Account(
                    code=bytes.fromhex(
                        "60003560f81c61ffff60003560e81c166000821460345760ff821460325760008080809481945af114602d57005b600080fd5bff5b00"  # noqa: E501
                    )
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 1, 1: 3, 17: 3},
                    code=bytes.fromhex(
                        "60ff600053601060015360006002536000806003818061dead5af16000556110003160015561dead3160025560003560f81c8060011460ce578060021460bc578060031460a55780600414608a57600514605857600080fd5b60016000536001600253600080600381600261dead5af15b6010556110003160115561dead3160125561100131601355005b50600160005360016002536000806003818061dead5af16070565b506001600253600080600381600261dead5af16070565b50600080600381600261dead5af16070565b50600080600380600261dead5af1607056"  # noqa: E501
                    ),
                ),
            },
        ),
        (
            "05",
            {
                Address("0x000000000000000000000000000000000000dead"): Account(
                    code=bytes.fromhex(
                        "60003560f81c61ffff60003560e81c166000821460345760ff821460325760008080809481945af114602d57005b600080fd5bff5b00"  # noqa: E501
                    )
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 1, 1: 3, 16: 1, 17: 3, 18: 1, 19: 1},
                    code=bytes.fromhex(
                        "60ff600053601060015360006002536000806003818061dead5af16000556110003160015561dead3160025560003560f81c8060011460ce578060021460bc578060031460a55780600414608a57600514605857600080fd5b60016000536001600253600080600381600261dead5af15b6010556110003160115561dead3160125561100131601355005b50600160005360016002536000806003818061dead5af16070565b506001600253600080600381600261dead5af16070565b50600080600381600261dead5af16070565b50600080600380600261dead5af1607056"  # noqa: E501
                    ),
                ),
            },
        ),
    ],
    ids=["case0", "case1", "case2", "case3", "case4"],
)
@pytest.mark.pre_alloc_mutable
def test_multi_selfdestruct(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Implements: SUC000, SUC001, SUC002, SUC003, SUC004, SUC005."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xcccccccccccccccccccccccccccccccccccccccc")
    callee = Address("0x000000000000000000000000000000000000dead")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=1000,
        gas_limit=71794957647893862,
    )

    pre[callee] = Account(
        balance=3,
        nonce=1,
        code=bytes.fromhex(
            "60003560f81c61ffff60003560e81c166000821460345760ff8214603257600080808094"  # noqa: E501
            "81945af114602d57005b600080fd5bff5b00"
        ),
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=1)
    pre[contract] = Account(
        balance=0x5F5E100,
        nonce=1,
        code=bytes.fromhex(
            "60ff600053601060015360006002536000806003818061dead5af1600055611000316001"  # noqa: E501
            "5561dead3160025560003560f81c8060011460ce578060021460bc578060031460a55780"  # noqa: E501
            "600414608a57600514605857600080fd5b60016000536001600253600080600381600261"  # noqa: E501
            "dead5af15b6010556110003160115561dead3160125561100131601355005b5060016000"  # noqa: E501
            "5360016002536000806003818061dead5af16070565b5060016002536000806003816002"  # noqa: E501
            "61dead5af16070565b50600080600381600261dead5af16070565b506000806003806002"  # noqa: E501
            "61dead5af1607056"
        ),
        storage={
            0x0: 0x60A7,
            0x1: 0x60A7,
            0x10: 0x60A7,
            0x11: 0x60A7,
            0x12: 0x60A7,
            0x13: 0x60A7,
        },
    )

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=tx_data,
        gas_limit=10000000,
        gas_price=1000,
        nonce=1,
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
