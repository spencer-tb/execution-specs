"""
CALLCODE -> CALLCODE -> code, check parameters.

Ported from:
tests/static/state_tests/stCallCodes/callcodecallcode_11Filler.json
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
    ["tests/static/state_tests/stCallCodes/callcodecallcode_11Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_callcodecallcode_11(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """CALLCODE -> CALLCODE -> code, check parameters."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0xdb43306b16c521b9cc3667fbe7d1b697bb1f9605")
    callee = Address("0x69142b38329c92930601fe8da12dc5866cde11c3")
    callee_1 = Address("0xb096eca04cd5c92c88ba466f92627d4f04d53c95")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=30000000,
    )

    pre[callee] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.SSTORE(
                key=0x1,
                value=Op.CALLCODE(
                    gas=0x3D090,
                    address=0xB096ECA04CD5C92C88BA466F92627D4F04D53C95,
                    value=0x2,
                    args_offset=0x0,
                    args_size=0x40,
                    ret_offset=0x0,
                    ret_size=0x40,
                ),
            )
            + Op.STOP
        ),
    )
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(key=0x2, value=0x1)
            + Op.SSTORE(key=0x4, value=Op.CALLER)
            + Op.SSTORE(key=0x7, value=Op.CALLVALUE)
            + Op.SSTORE(key=0xE6, value=Op.ADDRESS)
            + Op.SSTORE(key=0xE8, value=Op.ORIGIN)
            + Op.SSTORE(key=0xEC, value=Op.CALLDATASIZE)
            + Op.SSTORE(key=0xEE, value=Op.CODESIZE)
            + Op.SSTORE(key=0xF0, value=Op.GASPRICE)
            + Op.STOP
        ),
    )
    # Source: LLL
    # {  [[ 0 ]] (CALLCODE 350000 <contract:0x1000000000000000000000000000000000000001> 1 0 64 0 64 ) }  # noqa: E501
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.SSTORE(
                key=0x0,
                value=Op.CALLCODE(
                    gas=0x55730,
                    address=0x69142B38329C92930601FE8DA12DC5866CDE11C3,
                    value=0x1,
                    args_offset=0x0,
                    args_size=0x40,
                    ret_offset=0x0,
                    ret_size=0x40,
                ),
            )
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
        gas_limit=3000000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        callee: Account(
            code=(
                Op.SSTORE(
                    key=0x1,
                    value=Op.CALLCODE(
                        gas=0x3D090,
                        address=0xB096ECA04CD5C92C88BA466F92627D4F04D53C95,
                        value=0x2,
                        args_offset=0x0,
                        args_size=0x40,
                        ret_offset=0x0,
                        ret_size=0x40,
                    ),
                )
                + Op.STOP
            ),
        ),
        callee_1: Account(
            code=(
                Op.SSTORE(key=0x2, value=0x1)
                + Op.SSTORE(key=0x4, value=Op.CALLER)
                + Op.SSTORE(key=0x7, value=Op.CALLVALUE)
                + Op.SSTORE(key=0xE6, value=Op.ADDRESS)
                + Op.SSTORE(key=0xE8, value=Op.ORIGIN)
                + Op.SSTORE(key=0xEC, value=Op.CALLDATASIZE)
                + Op.SSTORE(key=0xEE, value=Op.CODESIZE)
                + Op.SSTORE(key=0xF0, value=Op.GASPRICE)
                + Op.STOP
            ),
        ),
        contract: Account(
            storage={
                0: 1,
                1: 1,
                2: 1,
                4: 0xDB43306B16C521B9CC3667FBE7D1B697BB1F9605,
                7: 2,
                230: 0xDB43306B16C521B9CC3667FBE7D1B697BB1F9605,
                232: 0xEBAF50DEBF10E08302FE4280C32DF010463CA297,
                236: 64,
                238: 34,
                240: 10,
            },
            code=(
                Op.SSTORE(
                    key=0x0,
                    value=Op.CALLCODE(
                        gas=0x55730,
                        address=0x69142B38329C92930601FE8DA12DC5866CDE11C3,
                        value=0x1,
                        args_offset=0x0,
                        args_size=0x40,
                        ret_offset=0x0,
                        ret_size=0x40,
                    ),
                )
                + Op.STOP
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
