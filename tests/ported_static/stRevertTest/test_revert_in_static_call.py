"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRevertTest/RevertInStaticCallFiller.json
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
    ["tests/static/state_tests/stRevertTest/RevertInStaticCallFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_revert_in_static_call(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x7f3f285918d9b5e764174551e10b7539b97bbb27")
    contract = Address("0x30f7398d20afe518491069c036185caf69d5aae9")
    callee = Address("0x33fcf0576ab8b4527c9426094e2e355a7ffc7e71")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    # Source: LLL
    # { [[ 0 ]] (STATICCALL 50000 <contract:0x945304eb96065b2a98b57a48a06ae28d285a71b5> 0 64 0 64 )}  # noqa: E501
    pre[contract] = Account(
        balance=1000,
        nonce=0,
        code=(
            Op.SSTORE(
                key=0x0,
                value=Op.STATICCALL(
                    gas=0xC350,
                    address=0x33FCF0576AB8B4527C9426094E2E355A7FFC7E71,
                    args_offset=0x0,
                    args_size=0x40,
                    ret_offset=0x0,
                    ret_size=0x40,
                ),
            )
            + Op.STOP
        ),
    )
    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=Op.REVERT(offset=0x0, size=0x0) + Op.STOP,
    )
    pre[sender] = Account(balance=0x5F5E100, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xa2333eef5630066b928dea5fd85a239f511b5b067d1441ee7ac290d0122b917b"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=105044,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            code=(
                Op.SSTORE(
                    key=0x0,
                    value=Op.STATICCALL(
                        gas=0xC350,
                        address=0x33FCF0576AB8B4527C9426094E2E355A7FFC7E71,
                        args_offset=0x0,
                        args_size=0x40,
                        ret_offset=0x0,
                        ret_size=0x40,
                    ),
                )
                + Op.STOP
            ),
        ),
        callee: Account(code=Op.REVERT(offset=0x0, size=0x0) + Op.STOP),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
