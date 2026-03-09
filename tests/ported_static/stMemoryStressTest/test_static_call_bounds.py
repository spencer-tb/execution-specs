"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stMemoryStressTest/static_CALL_BoundsFiller.json
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
        "tests/static/state_tests/stMemoryStressTest/static_CALL_BoundsFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit, expected_post",
    [
        (
            150000,
            {
                Address("0x7f91c742985ac295da40f3771a1be98f99f6a357"): Account(
                    code=bytes.fromhex(
                        "600060006000600073cc704d60c46b9c08aab4d15281184441ac7ed35c6707fffffffffffffffa50630fffffff6000630fffffff600073cc704d60c46b9c08aab4d15281184441ac7ed35c6707fffffffffffffffa5063ffffffff600063ffffffff600073cc704d60c46b9c08aab4d15281184441ac7ed35c6707fffffffffffffffa506000630fffffff6000630fffffff73cc704d60c46b9c08aab4d15281184441ac7ed35c6707fffffffffffffffa50600063ffffffff600063ffffffff73cc704d60c46b9c08aab4d15281184441ac7ed35c6707fffffffffffffffa50600067ffffffffffffffff600067ffffffffffffffff73cc704d60c46b9c08aab4d15281184441ac7ed35c6707fffffffffffffffa5060006fffffffffffffffffffffffffffffffff60006fffffffffffffffffffffffffffffffff73cc704d60c46b9c08aab4d15281184441ac7ed35c6707fffffffffffffffa5060007fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff60007fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff73cc704d60c46b9c08aab4d15281184441ac7ed35c6707fffffffffffffffa00"  # noqa: E501
                    )
                ),
                Address("0xcc704d60c46b9c08aab4d15281184441ac7ed35c"): Account(
                    code=bytes.fromhex("60005460010160005200")
                ),
            },
        ),
        (
            16777216,
            {
                Address("0x7f91c742985ac295da40f3771a1be98f99f6a357"): Account(
                    code=bytes.fromhex(
                        "600060006000600073cc704d60c46b9c08aab4d15281184441ac7ed35c6707fffffffffffffffa50630fffffff6000630fffffff600073cc704d60c46b9c08aab4d15281184441ac7ed35c6707fffffffffffffffa5063ffffffff600063ffffffff600073cc704d60c46b9c08aab4d15281184441ac7ed35c6707fffffffffffffffa506000630fffffff6000630fffffff73cc704d60c46b9c08aab4d15281184441ac7ed35c6707fffffffffffffffa50600063ffffffff600063ffffffff73cc704d60c46b9c08aab4d15281184441ac7ed35c6707fffffffffffffffa50600067ffffffffffffffff600067ffffffffffffffff73cc704d60c46b9c08aab4d15281184441ac7ed35c6707fffffffffffffffa5060006fffffffffffffffffffffffffffffffff60006fffffffffffffffffffffffffffffffff73cc704d60c46b9c08aab4d15281184441ac7ed35c6707fffffffffffffffa5060007fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff60007fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff73cc704d60c46b9c08aab4d15281184441ac7ed35c6707fffffffffffffffa00"  # noqa: E501
                    )
                ),
                Address("0xcc704d60c46b9c08aab4d15281184441ac7ed35c"): Account(
                    code=bytes.fromhex("60005460010160005200")
                ),
            },
        ),
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_static_call_bounds(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x4d2e21bbf9a40a8303787a066285648f8013129a")
    contract = Address("0x7f91c742985ac295da40f3771a1be98f99f6a357")
    callee = Address("0xcc704d60c46b9c08aab4d15281184441ac7ed35c")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[sender] = Account(
        balance=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
        nonce=0,
    )
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "600060006000600073cc704d60c46b9c08aab4d15281184441ac7ed35c6707ffffffffff"  # noqa: E501
            "fffffa50630fffffff6000630fffffff600073cc704d60c46b9c08aab4d15281184441ac"  # noqa: E501
            "7ed35c6707fffffffffffffffa5063ffffffff600063ffffffff600073cc704d60c46b9c"  # noqa: E501
            "08aab4d15281184441ac7ed35c6707fffffffffffffffa506000630fffffff6000630fff"  # noqa: E501
            "ffff73cc704d60c46b9c08aab4d15281184441ac7ed35c6707fffffffffffffffa506000"  # noqa: E501
            "63ffffffff600063ffffffff73cc704d60c46b9c08aab4d15281184441ac7ed35c6707ff"  # noqa: E501
            "fffffffffffffa50600067ffffffffffffffff600067ffffffffffffffff73cc704d60c4"  # noqa: E501
            "6b9c08aab4d15281184441ac7ed35c6707fffffffffffffffa5060006fffffffffffffff"  # noqa: E501
            "ffffffffffffffffff60006fffffffffffffffffffffffffffffffff73cc704d60c46b9c"  # noqa: E501
            "08aab4d15281184441ac7ed35c6707fffffffffffffffa5060007fffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffffffffffff60007fffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffffffffff73cc704d60c46b9c08aab4d15281"  # noqa: E501
            "184441ac7ed35c6707fffffffffffffffa00"
        ),
    )
    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("60005460010160005200"),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xef111bbdab3a1622936afdfc9bbec4b5bc05b4fa4b1ef0ce2a55cef552f7650e"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
