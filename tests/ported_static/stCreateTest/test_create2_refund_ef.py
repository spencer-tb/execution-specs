"""
Test combination of gas refund and EF-prefixed CREATE2 failure.

Ported from:
tests/static/state_tests/stCreateTest/CREATE2_RefundEFFiller.yml
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
    ["tests/static/state_tests/stCreateTest/CREATE2_RefundEFFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_create2_refund_ef(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test combination of gas refund and EF-prefixed CREATE2 failure."""
    coinbase = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x000000000000000000000000000000000c5ea705")
    callee = Address("0x00000000000000000000000000000000005ef94d")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=Op.SSTORE(key=Op.DUP1, value=0x0) + Op.STOP,
        storage={0x0: 0x1},
    )
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.PUSH1[0x0]
            + Op.PUSH1[0x19]
            + Op.CODECOPY(dest_offset=Op.DUP4, offset=0x11, size=Op.DUP1)
            + Op.DUP2
            + Op.DUP1
            + Op.SSTORE(key=0x0, value=Op.CREATE2)
            + Op.STOP
            + Op.INVALID
            + Op.POP(
                Op.CALL(
                    gas=0xC350,
                    address=0x5EF94D,
                    value=Op.DUP1,
                    args_offset=Op.DUP1,
                    args_size=Op.DUP1,
                    ret_offset=Op.DUP1,
                    ret_size=0x0,
                ),
            )
            + Op.MSTORE8(offset=0x0, value=0xEF)
            + Op.RETURN(offset=0x0, size=0x1)
        ),
    )
    pre[sender] = Account(balance=0x5AF3107A4000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        callee: Account(
            storage={0: 1},
            code=Op.SSTORE(key=Op.DUP1, value=0x0) + Op.STOP,
        ),
        contract: Account(
            code=(
                Op.PUSH1[0x0]
                + Op.PUSH1[0x19]
                + Op.CODECOPY(dest_offset=Op.DUP4, offset=0x11, size=Op.DUP1)
                + Op.DUP2
                + Op.DUP1
                + Op.SSTORE(key=0x0, value=Op.CREATE2)
                + Op.STOP
                + Op.INVALID
                + Op.POP(
                    Op.CALL(
                        gas=0xC350,
                        address=0x5EF94D,
                        value=Op.DUP1,
                        args_offset=Op.DUP1,
                        args_size=Op.DUP1,
                        ret_offset=Op.DUP1,
                        ret_size=0x0,
                    ),
                )
                + Op.MSTORE8(offset=0x0, value=0xEF)
                + Op.RETURN(offset=0x0, size=0x1)
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
