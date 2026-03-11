"""
Calls a contract that runs CREATE2 which deploy a code. then after...

Ported from:
tests/static/state_tests/stCreate2/Create2OOGafterInitCodeRevert2Filler.json
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
        "tests/static/state_tests/stCreate2/Create2OOGafterInitCodeRevert2Filler.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_create2_oo_gafter_init_code_revert2(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Calls a contract that runs CREATE2 which deploy a code. then..."""
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
    # Source: LLL
    # { (MSTORE 0 0x6460016001556000526005601bf3) (CREATE2 0 18 14 0) (REVERT 0 32) }  # noqa: E501
    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.MSTORE(offset=0x0, value=0x6460016001556000526005601BF3)
            + Op.POP(Op.CREATE2(value=0x0, offset=0x12, size=0xE, salt=0x0))
            + Op.REVERT(offset=0x0, size=0x20)
            + Op.STOP
        ),
    )
    # Source: LLL
    # { (CALL 33000 0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b 0 0 0 0 32) [[ 1 ]] (MLOAD 0) }  # noqa: E501
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.POP(
                Op.CALL(
                    gas=0x80E8,
                    address=0xB94F5374FCE5EDBC8E2A8697C15331677E6EBF0B,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x20,
                ),
            )
            + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
            + Op.STOP
        ),
        storage={0x1: 0x1},
    )

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=75000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        callee: Account(
            code=(
                Op.MSTORE(offset=0x0, value=0x6460016001556000526005601BF3)
                + Op.POP(
                    Op.CREATE2(value=0x0, offset=0x12, size=0xE, salt=0x0)
                )
                + Op.REVERT(offset=0x0, size=0x20)
                + Op.STOP
            ),
        ),
        contract: Account(
            storage={1: 0x6460016001556000526005601BF3},
            code=(
                Op.POP(
                    Op.CALL(
                        gas=0x80E8,
                        address=0xB94F5374FCE5EDBC8E2A8697C15331677E6EBF0B,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    ),
                )
                + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                + Op.STOP
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
