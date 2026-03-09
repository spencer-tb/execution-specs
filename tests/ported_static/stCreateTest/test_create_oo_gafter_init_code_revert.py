"""
Calls a contract that runs CREATE which deploy a code. then after...

Ported from:
tests/static/state_tests/stCreateTest/CreateOOGafterInitCodeRevertFiller.json
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
        "tests/static/state_tests/stCreateTest/CreateOOGafterInitCodeRevertFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_create_oo_gafter_init_code_revert(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Calls a contract that runs CREATE which deploy a code. then after..."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xc94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    callee = Address("0x094f5374fce5edbc8e2a8697c15331677e6ebf0b")
    callee_1 = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("622fffff60002000"),
    )
    pre[sender] = Account(balance=0xE8D4A51000, nonce=0)
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "6d6460016001556000526005601bf3600052600e60126000f05060006000600060006000"  # noqa: E501
            "73094f5374fce5edbc8e2a8697c15331677e6ebf0b612710f25060206000fd00"
        ),
    )
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "6020600060006000600073b94f5374fce5edbc8e2a8697c15331677e6ebf0b5af1506000"  # noqa: E501
            "5160015500"
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=285000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        callee: Account(code=bytes.fromhex("622fffff60002000")),
        callee_1: Account(
            code=bytes.fromhex(
                "6d6460016001556000526005601bf3600052600e60126000f0506000600060006000600073094f5374fce5edbc8e2a8697c15331677e6ebf0b612710f25060206000fd00"  # noqa: E501
            ),
        ),
        contract: Account(
            storage={1: 0x6460016001556000526005601BF3},
            code=bytes.fromhex(
                "6020600060006000600073b94f5374fce5edbc8e2a8697c15331677e6ebf0b5af15060005160015500"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
