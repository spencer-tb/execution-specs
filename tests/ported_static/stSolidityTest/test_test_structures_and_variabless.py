"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stSolidityTest/TestStructuresAndVariablessFiller.json
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
        "tests/static/state_tests/stSolidityTest/TestStructuresAndVariablessFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_test_structures_and_variabless(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xd96ed4431b417993ab4f4d4a656959d13c66e1dc")
    contract = Address("0x53d3dbdfd3ae109712a4771f7f37a6b1cda7b864")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[contract] = Account(
        balance=0x186A0,
        nonce=0,
        code=bytes.fromhex(
            "7c010000000000000000000000000000000000000000000000000000000060003504632a"  # noqa: E501
            "9afb838114610039578063c04062261461004b57005b61004161005d565b806000526020"  # noqa: E501
            "6000f35b61005361016c565b8060005260206000f35b600160ff8154141561006e576100"  # noqa: E501
            "76565b506000610169565b60015460035414156100875761008f565b506000610169565b"  # noqa: E501
            "73d96ed4431b417993ab4f4d4a656959d13c66e1dc73ffffffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffff60016002540481161614156100cd576100d5565b506000610169565b7f67"  # noqa: E501
            "6c6f62616c2064617461203332206c656e67746820737472696e67000000006004541415"  # noqa: E501
            "6101045761010c565b506000610169565b60056000808152602001908152602001600020"  # noqa: E501
            "60009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673d96e"  # noqa: E501
            "d4431b417993ab4f4d4a656959d13c66e1dc141561016057610168565b50600061016956"  # noqa: E501
            "5b5b90565b600060ff806001555073d96ed4431b417993ab4f4d4a656959d13c66e1dc60"  # noqa: E501
            "02805473ffffffffffffffffffffffffffffffffffffffff1916821790555060ff806003"  # noqa: E501
            "55507f676c6f62616c2064617461203332206c656e67746820737472696e670000000080"  # noqa: E501
            "6004555073d96ed4431b417993ab4f4d4a656959d13c66e1dc6005600080815260200190"  # noqa: E501
            "815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffff"  # noqa: E501
            "ffff0219169083021790555061022f61005d565b600060006101000a81548160ff021916"  # noqa: E501
            "9083021790555060ff6001600054041690509056"
        ),
    )
    pre[sender] = Account(balance=0x2540BE400, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x6f0117d3e9c684c7d6e1e6b79dc3880da2bebe77c765b171c062fdffd38a673f"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex("c0406226"),
        gas_limit=350000,
        gas_price=10,
        nonce=0,
        value=100,
    )

    post = {
        contract: Account(
            storage={
                0: 1,
                1: 255,
                2: 0xD96ED4431B417993AB4F4D4A656959D13C66E1DC,
                3: 255,
                4: 0x676C6F62616C2064617461203332206C656E67746820737472696E6700000000,  # noqa: E501
                0x5B8CCBB9D4D8FB16EA74CE3C29A41F1B461FBDAFF4714A0D9A8EB05499746BC: 0xD96ED4431B417993AB4F4D4A656959D13C66E1DC,  # noqa: E501
            },
            code=bytes.fromhex(
                "7c010000000000000000000000000000000000000000000000000000000060003504632a9afb838114610039578063c04062261461004b57005b61004161005d565b8060005260206000f35b61005361016c565b8060005260206000f35b600160ff8154141561006e57610076565b506000610169565b60015460035414156100875761008f565b506000610169565b73d96ed4431b417993ab4f4d4a656959d13c66e1dc73ffffffffffffffffffffffffffffffffffffffff60016002540481161614156100cd576100d5565b506000610169565b7f676c6f62616c2064617461203332206c656e67746820737472696e670000000060045414156101045761010c565b506000610169565b6005600080815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673d96ed4431b417993ab4f4d4a656959d13c66e1dc141561016057610168565b506000610169565b5b90565b600060ff806001555073d96ed4431b417993ab4f4d4a656959d13c66e1dc6002805473ffffffffffffffffffffffffffffffffffffffff1916821790555060ff80600355507f676c6f62616c2064617461203332206c656e67746820737472696e6700000000806004555073d96ed4431b417993ab4f4d4a656959d13c66e1dc6005600080815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff0219169083021790555061022f61005d565b600060006101000a81548160ff0219169083021790555060ff6001600054041690509056"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
