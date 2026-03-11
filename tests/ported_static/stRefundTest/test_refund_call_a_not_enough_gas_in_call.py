"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRefundTest
refund_CallA_notEnoughGasInCallFiller.json
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
        "tests/static/state_tests/stRefundTest/refund_CallA_notEnoughGasInCallFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_refund_call_a_not_enough_gas_in_call(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0xeb201d2887816e041f6e807e804f64f3a7a226fe")
    sender = Address("0xf32d3cb96b5451fbe912bbc8105bba4fc05afd1e")
    contract = Address("0x8329332ccfb6ae9df0412e842619fb1c989fbf48")
    callee = Address("0xf4c9fc42faeda49049e3b8e2b97a17cc2fe95718")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    # Source: LLL
    # { [[ 0 ]] (CALL 5005 <contract:0xaaae7baea6a6c7c4c2dfeb977efac326af552aaa> 0 0 0 0 0 )}  # noqa: E501
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.SSTORE(
                key=0x0,
                value=Op.CALL(
                    gas=0x138D,
                    address=0xF4C9FC42FAEDA49049E3B8E2B97A17CC2FE95718,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.STOP
        ),
        storage={0x1: 0x1},
    )
    pre[coinbase] = Account(balance=0, nonce=1)
    pre[sender] = Account(balance=0xF4240, nonce=0)
    pre[callee] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=Op.SSTORE(key=0x1, value=0x0) + Op.STOP,
        storage={0x1: 0x1},
    )

    tx = Transaction(
        secret_key=Hash(
            "0x07c857d62c76ce09f2e8ec3fa9277578c67b69c6547364568fddb841071e5bd7"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=85000,
        gas_price=10,
        nonce=0,
        value=10,
    )

    post = {
        contract: Account(
            storage={1: 1},
            code=(
                Op.SSTORE(
                    key=0x0,
                    value=Op.CALL(
                        gas=0x138D,
                        address=0xF4C9FC42FAEDA49049E3B8E2B97A17CC2FE95718,
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
            storage={1: 1},
            code=Op.SSTORE(key=0x1, value=0x0) + Op.STOP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
