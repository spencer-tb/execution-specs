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
from execution_testing.vm import Op

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

    # Source: LLL
    # { (KECCAK256 0x00 0x2fffff) }
    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=Op.SHA3(offset=0x0, size=0x2FFFFF) + Op.STOP,
    )
    pre[sender] = Account(balance=0xE8D4A51000, nonce=0)
    # Source: LLL
    # { (MSTORE 0 0x6460016001556000526005601bf3) (CREATE 0 18 14) (CALLCODE 10000 0x094f5374fce5edbc8e2a8697c15331677e6ebf0b 0 0 0 0 0) (REVERT 0 32) }  # noqa: E501
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.MSTORE(offset=0x0, value=0x6460016001556000526005601BF3)
            + Op.POP(Op.CREATE(value=0x0, offset=0x12, size=0xE))
            + Op.POP(
                Op.CALLCODE(
                    gas=0x2710,
                    address=0x94F5374FCE5EDBC8E2A8697C15331677E6EBF0B,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.REVERT(offset=0x0, size=0x20)
            + Op.STOP
        ),
    )
    # Source: LLL
    # { (CALL (GAS) 0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b 0 0 0 0 32) [[ 1 ]] (MLOAD 0) }  # noqa: E501
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.POP(
                Op.CALL(
                    gas=Op.GAS,
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
        callee: Account(code=Op.SHA3(offset=0x0, size=0x2FFFFF) + Op.STOP),
        callee_1: Account(
            code=(
                Op.MSTORE(offset=0x0, value=0x6460016001556000526005601BF3)
                + Op.POP(Op.CREATE(value=0x0, offset=0x12, size=0xE))
                + Op.POP(
                    Op.CALLCODE(
                        gas=0x2710,
                        address=0x94F5374FCE5EDBC8E2A8697C15331677E6EBF0B,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    ),
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
                        gas=Op.GAS,
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
