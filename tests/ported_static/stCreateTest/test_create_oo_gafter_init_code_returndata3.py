"""
Calls a contract that runs CREATE which deploy a code. then OOG happens...

Ported from:
tests/static/state_tests/stCreateTest
CreateOOGafterInitCodeReturndata3Filler.json
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

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


@pytest.mark.ported_from(
    [
        "tests/static/state_tests/stCreateTest/CreateOOGafterInitCodeReturndata3Filler.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_create_oo_gafter_init_code_returndata3(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Calls a contract that runs CREATE which deploy a code. then OOG..."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xc94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    callee = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[sender] = Account(balance=0xE8D4A51000, nonce=0)
    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "6d6460016001556000526005601bf3600052600e60126000f000"
        ),
    )
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "6020600060006000600073b94f5374fce5edbc8e2a8697c15331677e6ebf0b5af2506020"  # noqa: E501
            "600060003e60005160015500"
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=55000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        callee: Account(
            code=bytes.fromhex(
                "6d6460016001556000526005601bf3600052600e60126000f000"
            ),
        ),
        contract: Account(
            code=bytes.fromhex(
                "6020600060006000600073b94f5374fce5edbc8e2a8697c15331677e6ebf0b5af2506020600060003e60005160015500"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
