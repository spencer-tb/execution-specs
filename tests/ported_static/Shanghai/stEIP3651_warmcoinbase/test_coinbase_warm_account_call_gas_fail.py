"""
Test ported from static filler.

Ported from:
tests/static/state_tests/Shanghai/stEIP3651_warmcoinbase
coinbaseWarmAccountCallGasFailFiller.yml
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
        "tests/static/state_tests/Shanghai/stEIP3651_warmcoinbase/coinbaseWarmAccountCallGasFailFiller.yml",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        (
            "693c61390000000000000000000000008ddf5d9a5251c41efd2949f53db0a464116c7c6e",  # noqa: E501
            {
                Address("0x0a92fc97bb4c47b3d5e9e96fbb1c3fc2f07dba81"): Account(
                    storage={0: 1},
                    code=bytes.fromhex(
                        "60008080808060043560648180738ddf5d9a5251c41efd2949f53db0a464116c7c6e146088578073498516b6b2f25cb6a8e011a7c37a617b77e7d5001460885780738873820bb96daa39db93ae64a9d6397e4c6a48d71460805773303b6790d019874a107418eb549e4e7766a64728146079575bf1600055005b6018016073565b506018016073565b50601b01607356"  # noqa: E501
                    ),
                ),
                Address("0x303b6790d019874a107418eb549e4e7766a64728"): Account(
                    code=bytes.fromhex("60008080804181fa00")
                ),
                Address("0x498516b6b2f25cb6a8e011a7c37a617b77e7d500"): Account(
                    code=bytes.fromhex("6000808080804181f200")
                ),
                Address("0x8873820bb96daa39db93ae64a9d6397e4c6a48d7"): Account(
                    code=bytes.fromhex("60008080804181f400")
                ),
                Address("0x8ddf5d9a5251c41efd2949f53db0a464116c7c6e"): Account(
                    code=bytes.fromhex("6000808080804181f100")
                ),
            },
        ),
        (
            "693c6139000000000000000000000000498516b6b2f25cb6a8e011a7c37a617b77e7d500",  # noqa: E501
            {
                Address("0x0a92fc97bb4c47b3d5e9e96fbb1c3fc2f07dba81"): Account(
                    storage={0: 1},
                    code=bytes.fromhex(
                        "60008080808060043560648180738ddf5d9a5251c41efd2949f53db0a464116c7c6e146088578073498516b6b2f25cb6a8e011a7c37a617b77e7d5001460885780738873820bb96daa39db93ae64a9d6397e4c6a48d71460805773303b6790d019874a107418eb549e4e7766a64728146079575bf1600055005b6018016073565b506018016073565b50601b01607356"  # noqa: E501
                    ),
                ),
                Address("0x303b6790d019874a107418eb549e4e7766a64728"): Account(
                    code=bytes.fromhex("60008080804181fa00")
                ),
                Address("0x498516b6b2f25cb6a8e011a7c37a617b77e7d500"): Account(
                    code=bytes.fromhex("6000808080804181f200")
                ),
                Address("0x8873820bb96daa39db93ae64a9d6397e4c6a48d7"): Account(
                    code=bytes.fromhex("60008080804181f400")
                ),
                Address("0x8ddf5d9a5251c41efd2949f53db0a464116c7c6e"): Account(
                    code=bytes.fromhex("6000808080804181f100")
                ),
            },
        ),
        (
            "693c61390000000000000000000000008873820bb96daa39db93ae64a9d6397e4c6a48d7",  # noqa: E501
            {
                Address("0x0a92fc97bb4c47b3d5e9e96fbb1c3fc2f07dba81"): Account(
                    storage={0: 1},
                    code=bytes.fromhex(
                        "60008080808060043560648180738ddf5d9a5251c41efd2949f53db0a464116c7c6e146088578073498516b6b2f25cb6a8e011a7c37a617b77e7d5001460885780738873820bb96daa39db93ae64a9d6397e4c6a48d71460805773303b6790d019874a107418eb549e4e7766a64728146079575bf1600055005b6018016073565b506018016073565b50601b01607356"  # noqa: E501
                    ),
                ),
                Address("0x303b6790d019874a107418eb549e4e7766a64728"): Account(
                    code=bytes.fromhex("60008080804181fa00")
                ),
                Address("0x498516b6b2f25cb6a8e011a7c37a617b77e7d500"): Account(
                    code=bytes.fromhex("6000808080804181f200")
                ),
                Address("0x8873820bb96daa39db93ae64a9d6397e4c6a48d7"): Account(
                    code=bytes.fromhex("60008080804181f400")
                ),
                Address("0x8ddf5d9a5251c41efd2949f53db0a464116c7c6e"): Account(
                    code=bytes.fromhex("6000808080804181f100")
                ),
            },
        ),
        (
            "693c6139000000000000000000000000303b6790d019874a107418eb549e4e7766a64728",  # noqa: E501
            {
                Address("0x0a92fc97bb4c47b3d5e9e96fbb1c3fc2f07dba81"): Account(
                    storage={0: 1},
                    code=bytes.fromhex(
                        "60008080808060043560648180738ddf5d9a5251c41efd2949f53db0a464116c7c6e146088578073498516b6b2f25cb6a8e011a7c37a617b77e7d5001460885780738873820bb96daa39db93ae64a9d6397e4c6a48d71460805773303b6790d019874a107418eb549e4e7766a64728146079575bf1600055005b6018016073565b506018016073565b50601b01607356"  # noqa: E501
                    ),
                ),
                Address("0x303b6790d019874a107418eb549e4e7766a64728"): Account(
                    code=bytes.fromhex("60008080804181fa00")
                ),
                Address("0x498516b6b2f25cb6a8e011a7c37a617b77e7d500"): Account(
                    code=bytes.fromhex("6000808080804181f200")
                ),
                Address("0x8873820bb96daa39db93ae64a9d6397e4c6a48d7"): Account(
                    code=bytes.fromhex("60008080804181f400")
                ),
                Address("0x8ddf5d9a5251c41efd2949f53db0a464116c7c6e"): Account(
                    code=bytes.fromhex("6000808080804181f100")
                ),
            },
        ),
    ],
    ids=["case0", "case1", "case2", "case3"],
)
@pytest.mark.pre_alloc_mutable
def test_coinbase_warm_account_call_gas_fail(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x50228c44ed92561d94511e8518a75aa463bd444b")
    sender = Address("0x485fd0fd5c1d0409d2b772a66e98a6ac867b9d8b")
    contract = Address("0x0a92fc97bb4c47b3d5e9e96fbb1c3fc2f07dba81")
    callee = Address("0x303b6790d019874a107418eb549e4e7766a64728")
    callee_1 = Address("0x498516b6b2f25cb6a8e011a7c37a617b77e7d500")
    callee_2 = Address("0x8873820bb96daa39db93ae64a9d6397e4c6a48d7")
    callee_3 = Address("0x8ddf5d9a5251c41efd2949f53db0a464116c7c6e")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000,
    )

    pre[contract] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex(
            "60008080808060043560648180738ddf5d9a5251c41efd2949f53db0a464116c7c6e1460"  # noqa: E501
            "88578073498516b6b2f25cb6a8e011a7c37a617b77e7d5001460885780738873820bb96d"  # noqa: E501
            "aa39db93ae64a9d6397e4c6a48d71460805773303b6790d019874a107418eb549e4e7766"  # noqa: E501
            "a64728146079575bf1600055005b6018016073565b506018016073565b50601b01607356"  # noqa: E501
        ),
    )
    pre[callee] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex("60008080804181fa00"),
    )
    pre[sender] = Account(balance=0xBA1A9CE0BA1A9CE, nonce=1)
    pre[callee_1] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex("6000808080804181f200"),
    )
    pre[coinbase] = Account(balance=0xBA1A9CE0BA1A9CE, nonce=1)
    pre[callee_2] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex("60008080804181f400"),
    )
    pre[callee_3] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=bytes.fromhex("6000808080804181f100"),
    )

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x48dc5a9f099caaaa557742ca3a990a94be45b9969126a1bc74e5e8be5a2b5b47"  # noqa: E501
        ),
        to=contract,
        data=tx_data,
        gas_limit=80000,
        gas_price=10,
        nonce=1,
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
