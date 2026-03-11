"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stTransactionTest
SuicidesAndInternalCallSuicidesSuccessFiller.json
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
        "tests/static/state_tests/stTransactionTest/SuicidesAndInternalCallSuicidesSuccessFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        (
            "00000000000000000000000000000000000000000000000000000000000055f0",
            {
                Address("0x0000000000000000000000000000000000000000"): Account(
                    code=Op.SELFDESTRUCT(address=0x1) + Op.STOP
                ),
                Address("0xc94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.CALLDATALOAD(offset=0x0),
                            address=0x0,
                            value=0x1,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP
                ),
            },
        ),
        (
            "000000000000000000000000000000000000000000000000000000000000aaf0",
            {
                Address("0x0000000000000000000000000000000000000000"): Account(
                    code=Op.SELFDESTRUCT(address=0x1) + Op.STOP
                ),
                Address("0xc94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(
                    code=Op.POP(
                        Op.CALL(
                            gas=Op.CALLDATALOAD(offset=0x0),
                            address=0x0,
                            value=0x1,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        )
                    )
                    + Op.SELFDESTRUCT(address=0x0)
                    + Op.STOP
                ),
            },
        ),
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_suicides_and_internal_call_suicides_success(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xc94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    callee = Address("0x0000000000000000000000000000000000000000")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    # Source: LLL
    # {(SELFDESTRUCT 0x0000000000000000000000000000000000000001)}
    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=Op.SELFDESTRUCT(address=0x1) + Op.STOP,
    )
    pre[sender] = Account(balance=0xABA9500, nonce=0)
    # Source: LLL
    # {(CALL (CALLDATALOAD 0) 0x0000000000000000000000000000000000000000 1 0 0 0 0) (SELFDESTRUCT 0)}  # noqa: E501
    pre[contract] = Account(
        balance=1000,
        nonce=0,
        code=(
            Op.POP(
                Op.CALL(
                    gas=Op.CALLDATALOAD(offset=0x0),
                    address=0x0,
                    value=0x1,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.SELFDESTRUCT(address=0x0)
            + Op.STOP
        ),
    )

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=tx_data,
        gas_limit=150000,
        gas_price=10,
        nonce=0,
        value=10,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
