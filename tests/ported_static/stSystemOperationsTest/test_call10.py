"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stSystemOperationsTest/Call10Filler.json
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
    ["tests/static/state_tests/stSystemOperationsTest/Call10Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_call10(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    sender = Address("0x4768b5e50b0ebe91ae38d84a47e3179e615f9c40")
    contract = Address("0xfda03fa18cbda0970e18071f363bea4c9c90dfb6")
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
    pre[callee] = Account(balance=7000, nonce=0)
    pre[contract] = Account(
        balance=1000,
        nonce=0,
        code=(
            Op.JUMPDEST
            + Op.JUMPI(
                pc=0x42,
                condition=Op.ISZERO(Op.LT(Op.MLOAD(offset=0x80), 0xA)),
            )
            + Op.SSTORE(
                key=0x0,
                value=Op.CALL(
                    gas=0xFFFFFFFFFFF,
                    address=0xD9B97C712EBCE43F3C19179BBEF44B550F9E8BC0,
                    value=0x1,
                    args_offset=0x0,
                    args_size=0xC350,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.MSTORE(offset=0x80, value=Op.ADD(Op.MLOAD(offset=0x80), 0x1))
            + Op.JUMP(pc=0x0)
            + Op.JUMPDEST
            + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x80))
            + Op.STOP
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xe7c72b378297589acee4e0ba3272841bcfc5e220f86de253f890274cfee9e474"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=200000,
        gas_price=10,
        nonce=0,
        value=10,
    )

    post = {
        contract: Account(
            storage={0: 1, 1: 10},
            code=(
                Op.JUMPDEST
                + Op.JUMPI(
                    pc=0x42,
                    condition=Op.ISZERO(Op.LT(Op.MLOAD(offset=0x80), 0xA)),
                )
                + Op.SSTORE(
                    key=0x0,
                    value=Op.CALL(
                        gas=0xFFFFFFFFFFF,
                        address=0xD9B97C712EBCE43F3C19179BBEF44B550F9E8BC0,
                        value=0x1,
                        args_offset=0x0,
                        args_size=0xC350,
                        ret_offset=0x0,
                        ret_size=0x0,
                    ),
                )
                + Op.MSTORE(
                    offset=0x80, value=Op.ADD(Op.MLOAD(offset=0x80), 0x1)
                )
                + Op.JUMP(pc=0x0)
                + Op.JUMPDEST
                + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x80))
                + Op.STOP
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
