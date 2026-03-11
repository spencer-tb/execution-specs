"""
call with value. call takes more gas then tx has, and more value than...

Ported from:
tests/static/state_tests/stCallCreateCallCodeTest
callWithHighValueAndGasOOGFiller.json
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
        "tests/static/state_tests/stCallCreateCallCodeTest/callWithHighValueAndGasOOGFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_value, expected_post",
    [
        (
            100000,
            {
                Address("0x0896f13e800125c0ccec44f3c434335f0a97bc1b"): Account(
                    code=Op.SSTORE(key=0x1, value=0x1)
                    + Op.MSTORE8(offset=0x0, value=0x37)
                    + Op.RETURN(offset=0x0, size=0x2)
                ),
                Address("0xdfad372452688759edd82c422bf3976eafc89c2b"): Account(
                    storage={
                        1: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF  # noqa: E501
                    },
                    code=Op.MSTORE(
                        offset=0x0,
                        value=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                    )
                    + Op.MSTORE(
                        offset=0x20,
                        value=0xAAFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFAA,  # noqa: E501
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.CALL(
                            gas=0xFFFFFFFFFFFFFFFFFFFFFFFF,
                            address=0x896F13E800125C0CCEC44F3C434335F0A97BC1B,
                            value=0x56BC75E2D63100000,
                            args_offset=0x0,
                            args_size=0x40,
                            ret_offset=0x0,
                            ret_size=0x2,
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
            },
        ),
        (
            100000000000000000000,
            {
                Address("0x0896f13e800125c0ccec44f3c434335f0a97bc1b"): Account(
                    storage={1: 1},
                    code=Op.SSTORE(key=0x1, value=0x1)
                    + Op.MSTORE8(offset=0x0, value=0x37)
                    + Op.RETURN(offset=0x0, size=0x2),
                ),
                Address("0xdfad372452688759edd82c422bf3976eafc89c2b"): Account(
                    storage={
                        0: 1,
                        1: 0x3700FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                    },
                    code=Op.MSTORE(
                        offset=0x0,
                        value=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                    )
                    + Op.MSTORE(
                        offset=0x20,
                        value=0xAAFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFAA,  # noqa: E501
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.CALL(
                            gas=0xFFFFFFFFFFFFFFFFFFFFFFFF,
                            address=0x896F13E800125C0CCEC44F3C434335F0A97BC1B,
                            value=0x56BC75E2D63100000,
                            args_offset=0x0,
                            args_size=0x40,
                            ret_offset=0x0,
                            ret_size=0x2,
                        ),
                    )
                    + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
            },
        ),
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_call_with_high_value_and_gas_oog(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_value: int,
    expected_post: dict,
) -> None:
    """Call with value. call takes more gas then tx has, and more value..."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xd187b36e8532efd7f15218fb1781d79330c0cda2")
    contract = Address("0xdfad372452688759edd82c422bf3976eafc89c2b")
    callee = Address("0x0896f13e800125c0ccec44f3c434335f0a97bc1b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=30000000,
    )

    # Source: raw bytecode
    pre[callee] = Account(
        balance=23,
        nonce=0,
        code=(
            Op.SSTORE(key=0x1, value=0x1)
            + Op.MSTORE8(offset=0x0, value=0x37)
            + Op.RETURN(offset=0x0, size=0x2)
        ),
    )
    pre[sender] = Account(balance=0x3635C9ADC5DEA00000, nonce=0)
    # Source: LLL
    # { (MSTORE 0 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) (MSTORE 32 0xaaffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffaa ) [[ 0 ]] (CALL 0xffffffffffffffffffffffff <contract:0x945304eb96065b2a98b57a48a06ae28d285a71b5> 100000000000000000000 0 64 0 2 ) [[1]] (MLOAD 0)}  # noqa: E501
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.MSTORE(
                offset=0x0,
                value=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
            )
            + Op.MSTORE(
                offset=0x20,
                value=0xAAFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFAA,  # noqa: E501
            )
            + Op.SSTORE(
                key=0x0,
                value=Op.CALL(
                    gas=0xFFFFFFFFFFFFFFFFFFFFFFFF,
                    address=0x896F13E800125C0CCEC44F3C434335F0A97BC1B,
                    value=0x56BC75E2D63100000,
                    args_offset=0x0,
                    args_size=0x40,
                    ret_offset=0x0,
                    ret_size=0x2,
                ),
            )
            + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x0))
            + Op.STOP
        ),
        storage={0x0: 0x5},
    )

    tx = Transaction(
        secret_key=Hash(
            "0x897b12d02d588d8a4fe16ff831cbd4459c6f62f8c845b0ccdd31caf068c84a26"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=6000000,
        gas_price=10,
        nonce=0,
        value=tx_value,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
