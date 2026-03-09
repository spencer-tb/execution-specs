"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stDelegatecallTestHomestead/callOutput3Filler.json
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
        "tests/static/state_tests/stDelegatecallTestHomestead/callOutput3Filler.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_call_output3(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x2e3d0156d2b99a6eacba540c55f423c8f5a33143")
    contract = Address("0x4e40004dedfdad4927c60de1289ab14535f5121a")
    callee = Address("0xbcc1197ccd23a97607f2f96d031f3432e0d16a02")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "7f5e20a0453cecd065ea59c37ac63e079ee08998b6045136a8ce6635c7912ec0b6600052"  # noqa: E501
            "602060006000600073bcc1197ccd23a97607f2f96d031f3432e0d16a0261c350f4506000"  # noqa: E501
            "5160005500"
        ),
    )
    pre[callee] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex("6001600101600055"),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xb1f4cbc3a50042184425a6f9e996d0910f7ba879457ce5dac5c71e498ad3c005"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=900000,
        gas_price=10,
        nonce=0,
        value=100000,
    )

    post = {
        contract: Account(
            storage={
                0: 0x5E20A0453CECD065EA59C37AC63E079EE08998B6045136A8CE6635C7912EC0B6,  # noqa: E501
            },
            code=bytes.fromhex(
                "7f5e20a0453cecd065ea59c37ac63e079ee08998b6045136a8ce6635c7912ec0b6600052602060006000600073bcc1197ccd23a97607f2f96d031f3432e0d16a0261c350f45060005160005500"  # noqa: E501
            ),
        ),
        callee: Account(code=bytes.fromhex("6001600101600055")),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
