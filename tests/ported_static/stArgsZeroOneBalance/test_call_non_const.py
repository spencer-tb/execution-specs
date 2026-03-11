"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stArgsZeroOneBalance/callNonConstFiller.yml
"""

import pytest
from execution_testing import (
    Account,
    Address,
    Alloc,
    EOA,
    Environment,
    Hash,
    StateTestFiller,
    Transaction,
)
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


@pytest.mark.ported_from(
    ["tests/static/state_tests/stArgsZeroOneBalance/callNonConstFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_value, expected_post",
    [
        (
            0,
            {
                Address("0x7d7e1645af7df916da558f0695e9dedd23b1215e"): Account(
                    storage={0: 1},
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.CALL(
                            gas=Op.BALANCE(
                                address=0x7D7E1645AF7DF916DA558F0695E9DEDD23B1215E  # noqa: E501
                            ),
                            address=Op.BALANCE(
                                address=0x7D7E1645AF7DF916DA558F0695E9DEDD23B1215E  # noqa: E501
                            ),
                            value=Op.BALANCE(
                                address=0x7D7E1645AF7DF916DA558F0695E9DEDD23B1215E  # noqa: E501
                            ),
                            args_offset=Op.BALANCE(
                                address=0x7D7E1645AF7DF916DA558F0695E9DEDD23B1215E  # noqa: E501
                            ),
                            args_size=Op.BALANCE(
                                address=0x7D7E1645AF7DF916DA558F0695E9DEDD23B1215E  # noqa: E501
                            ),
                            ret_offset=Op.BALANCE(
                                address=0x7D7E1645AF7DF916DA558F0695E9DEDD23B1215E  # noqa: E501
                            ),
                            ret_size=Op.BALANCE(
                                address=0x7D7E1645AF7DF916DA558F0695E9DEDD23B1215E  # noqa: E501
                            ),
                        ),
                    )
                    + Op.STOP,
                )
            },
        ),
        (
            1,
            {
                Address("0x7d7e1645af7df916da558f0695e9dedd23b1215e"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.CALL(
                            gas=Op.BALANCE(
                                address=0x7D7E1645AF7DF916DA558F0695E9DEDD23B1215E  # noqa: E501
                            ),
                            address=Op.BALANCE(
                                address=0x7D7E1645AF7DF916DA558F0695E9DEDD23B1215E  # noqa: E501
                            ),
                            value=Op.BALANCE(
                                address=0x7D7E1645AF7DF916DA558F0695E9DEDD23B1215E  # noqa: E501
                            ),
                            args_offset=Op.BALANCE(
                                address=0x7D7E1645AF7DF916DA558F0695E9DEDD23B1215E  # noqa: E501
                            ),
                            args_size=Op.BALANCE(
                                address=0x7D7E1645AF7DF916DA558F0695E9DEDD23B1215E  # noqa: E501
                            ),
                            ret_offset=Op.BALANCE(
                                address=0x7D7E1645AF7DF916DA558F0695E9DEDD23B1215E  # noqa: E501
                            ),
                            ret_size=Op.BALANCE(
                                address=0x7D7E1645AF7DF916DA558F0695E9DEDD23B1215E  # noqa: E501
                            ),
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
def test_call_non_const(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_value: int,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = EOA(
        key=0xB1F4CBC3A50042184425A6F9E996D0910F7BA879457CE5DAC5C71E498AD3C005
    )
    contract = Address("0x7d7e1645af7df916da558f0695e9dedd23b1215e")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)
    # Source: LLL
    # { [[ 0 ]] (CALL (BALANCE <contract:target:0x095e7baea6a6c7c4c2dfeb977efac326af552d87>) (BALANCE <contract:target:0x095e7baea6a6c7c4c2dfeb977efac326af552d87>) (BALANCE <contract:target:0x095e7baea6a6c7c4c2dfeb977efac326af552d87>) (BALANCE <contract:target:0x095e7baea6a6c7c4c2dfeb977efac326af552d87>) (BALANCE <contract:target:0x095e7baea6a6c7c4c2dfeb977efac326af552d87>) (BALANCE <contract:target:0x095e7baea6a6c7c4c2dfeb977efac326af552d87>) (BALANCE <contract:target:0x095e7baea6a6c7c4c2dfeb977efac326af552d87>)) }  # noqa: E501
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(
                key=0x0,
                value=Op.CALL(
                    gas=Op.BALANCE(
                        address=0x7D7E1645AF7DF916DA558F0695E9DEDD23B1215E,
                    ),
                    address=Op.BALANCE(
                        address=0x7D7E1645AF7DF916DA558F0695E9DEDD23B1215E,
                    ),
                    value=Op.BALANCE(
                        address=0x7D7E1645AF7DF916DA558F0695E9DEDD23B1215E,
                    ),
                    args_offset=Op.BALANCE(
                        address=0x7D7E1645AF7DF916DA558F0695E9DEDD23B1215E,
                    ),
                    args_size=Op.BALANCE(
                        address=0x7D7E1645AF7DF916DA558F0695E9DEDD23B1215E,
                    ),
                    ret_offset=Op.BALANCE(
                        address=0x7D7E1645AF7DF916DA558F0695E9DEDD23B1215E,
                    ),
                    ret_size=Op.BALANCE(
                        address=0x7D7E1645AF7DF916DA558F0695E9DEDD23B1215E,
                    ),
                ),
            )
            + Op.STOP
        ),
    )

    tx = Transaction(
        sender=sender,
        to=contract,
        data=b"",
        gas_limit=400000,
        gas_price=10,
        nonce=0,
        value=tx_value,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
