"""
Test where accnt has slot 1 value of '2', is cleared, then calls itself and...

Ported from:
tests/static/state_tests/stSStoreTest
SstoreCallToSelfSubRefundBelowZeroFiller.json
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
        "tests/static/state_tests/stSStoreTest/SstoreCallToSelfSubRefundBelowZeroFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_sstore_call_to_self_sub_refund_below_zero(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test where accnt has slot 1 value of '2', is cleared, then calls..."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x2c4b3807d1cb27f33e74c7cd5be5b0d6b176414e")
    contract = Address("0xb48023055b6c3d565a6f5488459d64efab79b6c7")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=68719476736,
    )

    pre[sender] = Account(balance=0xFFFFFFFFFFFFFFFF, nonce=0)
    # Source: raw bytecode
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.JUMPI(pc=0x15, condition=Op.EQ(Op.ADDRESS, Op.CALLER))
            + Op.SSTORE(key=0x1, value=0x0)
            + Op.CALL(
                gas=Op.GAS,
                address=Op.ADDRESS,
                value=Op.DUP1,
                args_offset=Op.DUP1,
                args_size=Op.DUP1,
                ret_offset=Op.DUP1,
                ret_size=0x0,
            )
            + Op.STOP
            + Op.JUMPDEST
            + Op.SSTORE(key=0x1, value=0x3)
            + Op.STOP
        ),
        storage={0x1: 0x2},
    )

    tx = Transaction(
        secret_key=Hash(
            "0xaf50993ba9fd52f2a61fcd1dc6d59a44e7af39f4289201cc19ea7d30e8e27e83"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=2367154,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            storage={1: 3},
            code=(
                Op.JUMPI(pc=0x15, condition=Op.EQ(Op.ADDRESS, Op.CALLER))
                + Op.SSTORE(key=0x1, value=0x0)
                + Op.CALL(
                    gas=Op.GAS,
                    address=Op.ADDRESS,
                    value=Op.DUP1,
                    args_offset=Op.DUP1,
                    args_size=Op.DUP1,
                    ret_offset=Op.DUP1,
                    ret_size=0x0,
                )
                + Op.STOP
                + Op.JUMPDEST
                + Op.SSTORE(key=0x1, value=0x3)
                + Op.STOP
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
