"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stTransactionTest
SuicidesAndInternalCallSuicidesOOGFiller.json
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
    [
        "tests/static/state_tests/stTransactionTest/SuicidesAndInternalCallSuicidesOOGFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_suicides_and_internal_call_suicides_oog(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    sender = EOA(
        key=0xA2333EEF5630066B928DEA5FD85A239F511B5B067D1441EE7AC290D0122B917B
    )
    contract = Address("0x78f15ba0abc5cc1aaa5a0ac6add5d28dd9ab8e1e")
    callee = Address("0x5f0d8cd21c9026a32a4e8d15257b1801458989f3")

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
        code=Op.SELFDESTRUCT(address=0x1) + Op.STOP,
    )
    # Source: LLL
    # {(CALL 22000 <contract:0x0000000000000000000000000000000000000000> 1 0 0 0 0) (SELFDESTRUCT 0)}  # noqa: E501
    pre[contract] = Account(
        balance=10,
        nonce=0,
        code=(
            Op.POP(
                Op.CALL(
                    gas=0x55F0,
                    address=0x5F0D8CD21C9026A32A4E8D15257B1801458989F3,
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
    pre[sender] = Account(balance=0x5F5E100, nonce=0)

    tx = Transaction(
        sender=sender,
        to=contract,
        data=b"",
        gas_limit=50000,
        gas_price=10,
        nonce=0,
        value=10,
    )

    post = {
        callee: Account(code=Op.SELFDESTRUCT(address=0x1) + Op.STOP),
        contract: Account(
            code=(
                Op.POP(
                    Op.CALL(
                        gas=0x55F0,
                        address=0x5F0D8CD21C9026A32A4E8D15257B1801458989F3,
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
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
