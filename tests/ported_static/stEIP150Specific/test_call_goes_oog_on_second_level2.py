"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stEIP150Specific/CallGoesOOGOnSecondLevel2Filler.json
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
    [
        "tests/static/state_tests/stEIP150Specific/CallGoesOOGOnSecondLevel2Filler.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_call_goes_oog_on_second_level2(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xfaa10b404ab607779993c016cd5da73ae1f29d7e")
    contract = Address("0x171742e7809e3b571e899f0d4d9d35cd5deeacf1")
    callee = Address("0xbfb2b65e4ef26a144a185b32c7baf39ef8e40b4b")
    callee_1 = Address("0xe1d370a0538366eaffbc9fcd571af7b1e80d377c")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    # Source: LLL
    # { (SSTORE 8 (GAS)) (SSTORE 9 (CALL 600000 <contract:0x1000000000000000000000000000000000000113> 0 0 0 0 0)) }  # noqa: E501
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(key=0x8, value=Op.GAS)
            + Op.SSTORE(
                key=0x9,
                value=Op.CALL(
                    gas=0x927C0,
                    address=0xE1D370A0538366EAFFBC9FCD571AF7B1E80D377C,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.STOP
        ),
    )
    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(key=0x8, value=Op.GAS)
            + Op.SHA3(offset=0x0, size=0x2FFFFF)
            + Op.STOP
        ),
    )
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(key=0x8, value=Op.GAS)
            + Op.SSTORE(
                key=0x9,
                value=Op.CALL(
                    gas=0x927C0,
                    address=0xBFB2B65E4EF26A144A185B32C7BAF39EF8E40B4B,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.STOP
        ),
    )
    pre[sender] = Account(balance=0xE8D4A51000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x4f31b3206fbf0e0e598b9b1a7d8ac86302a0ff1d8930738f1bebae9b67173e52"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=160000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            code=(
                Op.SSTORE(key=0x8, value=Op.GAS)
                + Op.SSTORE(
                    key=0x9,
                    value=Op.CALL(
                        gas=0x927C0,
                        address=0xE1D370A0538366EAFFBC9FCD571AF7B1E80D377C,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    ),
                )
                + Op.STOP
            ),
        ),
        callee: Account(
            code=(
                Op.SSTORE(key=0x8, value=Op.GAS)
                + Op.SHA3(offset=0x0, size=0x2FFFFF)
                + Op.STOP
            ),
        ),
        callee_1: Account(
            code=(
                Op.SSTORE(key=0x8, value=Op.GAS)
                + Op.SSTORE(
                    key=0x9,
                    value=Op.CALL(
                        gas=0x927C0,
                        address=0xBFB2B65E4EF26A144A185B32C7BAF39EF8E40B4B,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    ),
                )
                + Op.STOP
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
