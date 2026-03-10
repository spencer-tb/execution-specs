"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stDelegatecallTestHomestead
Delegatecall1024OOGFiller.json
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
        "tests/static/state_tests/stDelegatecallTestHomestead/Delegatecall1024OOGFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_delegatecall1024_oog(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    sender = Address("0x4768b5e50b0ebe91ae38d84a47e3179e615f9c40")
    contract = Address("0x62c5c9278da01e6594d6fede061838cf5e597f2b")
    callee = Address("0xd9b97c712ebce43f3c19179bbef44b550f9e8bc0")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[sender] = Account(balance=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF, nonce=0)
    pre[contract] = Account(
        balance=1024,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=Op.ADD(Op.SLOAD(key=0x0), 0x1))
            + Op.SSTORE(
                key=0x1,
                value=Op.DELEGATECALL(
                    gas=Op.MUL(
                        Op.SUB(Op.GAS, 0x2710),
                        Op.SUB(0x1, Op.DIV(Op.SLOAD(key=0x0), 0x401)),
                    ),
                    address=0x62C5C9278DA01E6594D6FEDE061838CF5E597F2B,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.SSTORE(
                key=0x2,
                value=Op.ADD(0x1, Op.MUL(Op.SLOAD(key=0x0), 0x3E8)),
            )
            + Op.STOP
        ),
    )
    pre[callee] = Account(balance=7000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xe7c72b378297589acee4e0ba3272841bcfc5e220f86de253f890274cfee9e474"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=15720826,
        gas_price=10,
        nonce=0,
        value=10,
    )

    post = {
        contract: Account(
            storage={0: 146, 1: 1, 2: 0x23A51},
            code=(
                Op.SSTORE(key=0x0, value=Op.ADD(Op.SLOAD(key=0x0), 0x1))
                + Op.SSTORE(
                    key=0x1,
                    value=Op.DELEGATECALL(
                        gas=Op.MUL(
                            Op.SUB(Op.GAS, 0x2710),
                            Op.SUB(0x1, Op.DIV(Op.SLOAD(key=0x0), 0x401)),
                        ),
                        address=0x62C5C9278DA01E6594D6FEDE061838CF5E597F2B,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    ),
                )
                + Op.SSTORE(
                    key=0x2,
                    value=Op.ADD(0x1, Op.MUL(Op.SLOAD(key=0x0), 0x3E8)),
                )
                + Op.STOP
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
