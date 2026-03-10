"""
https://github.com/ethereum/tests/issues/558 (subcall/opcode return more...

Ported from:
tests/static/state_tests/stReturnDataTest
subcallReturnMoreThenExpectedFiller.yml
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
        "tests/static/state_tests/stReturnDataTest/subcallReturnMoreThenExpectedFiller.yml",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_subcall_return_more_then_expected(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Https://github.com/ethereum/tests/issues/558 (subcall/opcode..."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0xca70835d5e9b8c8e139a9693ab05705d291f86bb")
    callee = Address("0x028cdafc3d5d27d006ffb88e1ecf2fa4b412ee4f")
    callee_1 = Address("0xa8592f39b32943f9f464090497722b4f9c15f598")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[callee] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.MSTORE(
                offset=0x0,
                value=0x1122334455667788991011121314151617181920212223242526272829303132,  # noqa: E501
            )
            + Op.MSTORE(
                offset=0x20,
                value=0x3334353637383940414243444546474849505152535455565758596061626364,  # noqa: E501
            )
            + Op.REVERT(offset=0x0, size=0x40)
            + Op.STOP
        ),
    )
    pre[callee_1] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.MSTORE(
                offset=0x0,
                value=0x1122334455667788991011121314151617181920212223242526272829303132,  # noqa: E501
            )
            + Op.MSTORE(
                offset=0x20,
                value=0x3334353637383940414243444546474849505152535455565758596061626364,  # noqa: E501
            )
            + Op.RETURN(offset=0x0, size=0x40)
            + Op.STOP
        ),
    )
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.POP(
                Op.CALL(
                    gas=0x30D40,
                    address=0xA8592F39B32943F9F464090497722B4F9C15F598,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0xC,
                ),
            )
            + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
            + Op.MSTORE(offset=0x0, value=0x0)
            + Op.POP(
                Op.DELEGATECALL(
                    gas=0x30D40,
                    address=0xA8592F39B32943F9F464090497722B4F9C15F598,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0xC,
                ),
            )
            + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
            + Op.MSTORE(offset=0x0, value=0x0)
            + Op.POP(
                Op.STATICCALL(
                    gas=0x30D40,
                    address=0xA8592F39B32943F9F464090497722B4F9C15F598,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0xC,
                ),
            )
            + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
            + Op.MSTORE(offset=0x0, value=0x0)
            + Op.POP(
                Op.CALLCODE(
                    gas=0x30D40,
                    address=0xA8592F39B32943F9F464090497722B4F9C15F598,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0xC,
                ),
            )
            + Op.SSTORE(key=0x3, value=Op.MLOAD(offset=0x0))
            + Op.MSTORE(offset=0x0, value=0x0)
            + Op.POP(
                Op.CALL(
                    gas=0x30D40,
                    address=0x28CDAFC3D5D27D006FFB88E1ECF2FA4B412EE4F,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0xC,
                ),
            )
            + Op.SSTORE(key=0x4, value=Op.MLOAD(offset=0x0))
            + Op.MSTORE(offset=0x0, value=0x0)
            + Op.POP(
                Op.DELEGATECALL(
                    gas=0x30D40,
                    address=0x28CDAFC3D5D27D006FFB88E1ECF2FA4B412EE4F,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0xC,
                ),
            )
            + Op.SSTORE(key=0x5, value=Op.MLOAD(offset=0x0))
            + Op.MSTORE(offset=0x0, value=0x0)
            + Op.POP(
                Op.STATICCALL(
                    gas=0x30D40,
                    address=0x28CDAFC3D5D27D006FFB88E1ECF2FA4B412EE4F,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0xC,
                ),
            )
            + Op.SSTORE(key=0x6, value=Op.MLOAD(offset=0x0))
            + Op.MSTORE(offset=0x0, value=0x0)
            + Op.POP(
                Op.CALLCODE(
                    gas=0x30D40,
                    address=0x28CDAFC3D5D27D006FFB88E1ECF2FA4B412EE4F,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0xC,
                ),
            )
            + Op.SSTORE(key=0x7, value=Op.MLOAD(offset=0x0))
            + Op.STOP
        ),
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xe04d1ac7ddda0c98397d56a0b501e960d4cd325a39286919ac23c1a07009a869"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=400000,
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = {
        callee: Account(
            code=(
                Op.MSTORE(
                    offset=0x0,
                    value=0x1122334455667788991011121314151617181920212223242526272829303132,  # noqa: E501
                )
                + Op.MSTORE(
                    offset=0x20,
                    value=0x3334353637383940414243444546474849505152535455565758596061626364,  # noqa: E501
                )
                + Op.REVERT(offset=0x0, size=0x40)
                + Op.STOP
            ),
        ),
        callee_1: Account(
            code=(
                Op.MSTORE(
                    offset=0x0,
                    value=0x1122334455667788991011121314151617181920212223242526272829303132,  # noqa: E501
                )
                + Op.MSTORE(
                    offset=0x20,
                    value=0x3334353637383940414243444546474849505152535455565758596061626364,  # noqa: E501
                )
                + Op.RETURN(offset=0x0, size=0x40)
                + Op.STOP
            ),
        ),
        contract: Account(
            storage={
                0: 0x1122334455667788991011120000000000000000000000000000000000000000,  # noqa: E501
                1: 0x1122334455667788991011120000000000000000000000000000000000000000,  # noqa: E501
                2: 0x1122334455667788991011120000000000000000000000000000000000000000,  # noqa: E501
                3: 0x1122334455667788991011120000000000000000000000000000000000000000,  # noqa: E501
                4: 0x1122334455667788991011120000000000000000000000000000000000000000,  # noqa: E501
                5: 0x1122334455667788991011120000000000000000000000000000000000000000,  # noqa: E501
                6: 0x1122334455667788991011120000000000000000000000000000000000000000,  # noqa: E501
                7: 0x1122334455667788991011120000000000000000000000000000000000000000,  # noqa: E501
            },
            code=(
                Op.POP(
                    Op.CALL(
                        gas=0x30D40,
                        address=0xA8592F39B32943F9F464090497722B4F9C15F598,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0xC,
                    ),
                )
                + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                + Op.MSTORE(offset=0x0, value=0x0)
                + Op.POP(
                    Op.DELEGATECALL(
                        gas=0x30D40,
                        address=0xA8592F39B32943F9F464090497722B4F9C15F598,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0xC,
                    ),
                )
                + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                + Op.MSTORE(offset=0x0, value=0x0)
                + Op.POP(
                    Op.STATICCALL(
                        gas=0x30D40,
                        address=0xA8592F39B32943F9F464090497722B4F9C15F598,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0xC,
                    ),
                )
                + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                + Op.MSTORE(offset=0x0, value=0x0)
                + Op.POP(
                    Op.CALLCODE(
                        gas=0x30D40,
                        address=0xA8592F39B32943F9F464090497722B4F9C15F598,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0xC,
                    ),
                )
                + Op.SSTORE(key=0x3, value=Op.MLOAD(offset=0x0))
                + Op.MSTORE(offset=0x0, value=0x0)
                + Op.POP(
                    Op.CALL(
                        gas=0x30D40,
                        address=0x28CDAFC3D5D27D006FFB88E1ECF2FA4B412EE4F,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0xC,
                    ),
                )
                + Op.SSTORE(key=0x4, value=Op.MLOAD(offset=0x0))
                + Op.MSTORE(offset=0x0, value=0x0)
                + Op.POP(
                    Op.DELEGATECALL(
                        gas=0x30D40,
                        address=0x28CDAFC3D5D27D006FFB88E1ECF2FA4B412EE4F,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0xC,
                    ),
                )
                + Op.SSTORE(key=0x5, value=Op.MLOAD(offset=0x0))
                + Op.MSTORE(offset=0x0, value=0x0)
                + Op.POP(
                    Op.STATICCALL(
                        gas=0x30D40,
                        address=0x28CDAFC3D5D27D006FFB88E1ECF2FA4B412EE4F,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0xC,
                    ),
                )
                + Op.SSTORE(key=0x6, value=Op.MLOAD(offset=0x0))
                + Op.MSTORE(offset=0x0, value=0x0)
                + Op.POP(
                    Op.CALLCODE(
                        gas=0x30D40,
                        address=0x28CDAFC3D5D27D006FFB88E1ECF2FA4B412EE4F,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0xC,
                    ),
                )
                + Op.SSTORE(key=0x7, value=Op.MLOAD(offset=0x0))
                + Op.STOP
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
