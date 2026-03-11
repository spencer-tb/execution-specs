"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stArgsZeroOneBalance/log2NonConstFiller.yml
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
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


@pytest.mark.ported_from(
    ["tests/static/state_tests/stArgsZeroOneBalance/log2NonConstFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_value, expected_post",
    [
        (
            0,
            {
                Address("0x007631bf0fc6669fe93c41401498b2612bbf41cf"): Account(
                    code=Op.LOG2(
                        offset=Op.BALANCE(
                            address=0x7631BF0FC6669FE93C41401498B2612BBF41CF
                        ),
                        size=Op.BALANCE(
                            address=0x7631BF0FC6669FE93C41401498B2612BBF41CF
                        ),
                        topic_1=Op.BALANCE(
                            address=0x7631BF0FC6669FE93C41401498B2612BBF41CF
                        ),
                        topic_2=Op.BALANCE(
                            address=0x7631BF0FC6669FE93C41401498B2612BBF41CF
                        ),
                    )
                    + Op.STOP
                )
            },
        ),
        (
            1,
            {
                Address("0x007631bf0fc6669fe93c41401498b2612bbf41cf"): Account(
                    code=Op.LOG2(
                        offset=Op.BALANCE(
                            address=0x7631BF0FC6669FE93C41401498B2612BBF41CF
                        ),
                        size=Op.BALANCE(
                            address=0x7631BF0FC6669FE93C41401498B2612BBF41CF
                        ),
                        topic_1=Op.BALANCE(
                            address=0x7631BF0FC6669FE93C41401498B2612BBF41CF
                        ),
                        topic_2=Op.BALANCE(
                            address=0x7631BF0FC6669FE93C41401498B2612BBF41CF
                        ),
                    )
                    + Op.STOP
                )
            },
        ),
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_log2_non_const(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_value: int,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x2e3d0156d2b99a6eacba540c55f423c8f5a33143")
    contract = Address("0x007631bf0fc6669fe93c41401498b2612bbf41cf")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    # Source: LLL
    # { (LOG2 (BALANCE <contract:target:0x095e7baea6a6c7c4c2dfeb977efac326af552d87>) (BALANCE <contract:target:0x095e7baea6a6c7c4c2dfeb977efac326af552d87>) (BALANCE <contract:target:0x095e7baea6a6c7c4c2dfeb977efac326af552d87>) (BALANCE <contract:target:0x095e7baea6a6c7c4c2dfeb977efac326af552d87>)) }  # noqa: E501
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.LOG2(
                offset=Op.BALANCE(
                    address=0x7631BF0FC6669FE93C41401498B2612BBF41CF,
                ),
                size=Op.BALANCE(
                    address=0x7631BF0FC6669FE93C41401498B2612BBF41CF
                ),
                topic_1=Op.BALANCE(
                    address=0x7631BF0FC6669FE93C41401498B2612BBF41CF,
                ),
                topic_2=Op.BALANCE(
                    address=0x7631BF0FC6669FE93C41401498B2612BBF41CF,
                ),
            )
            + Op.STOP
        ),
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xb1f4cbc3a50042184425a6f9e996d0910f7ba879457ce5dac5c71e498ad3c005"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=400000,
        gas_price=10,
        nonce=0,
        value=tx_value,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
