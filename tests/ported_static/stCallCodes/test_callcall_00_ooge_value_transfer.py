"""
call -> call -> code oog.

Ported from:
tests/static/state_tests/stCallCodes/callcall_00_OOGE_valueTransferFiller.json
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
        "tests/static/state_tests/stCallCodes/callcall_00_OOGE_valueTransferFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_callcall_00_ooge_value_transfer(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Call -> call -> code oog."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0xb06c4ff2e2503bb892cc3c9237a1ae465a759616")
    callee = Address("0x766b2cf0691f51029181fc511395b7ab71353a88")
    callee_1 = Address("0xa781ad010268e97d590d07e5b442975243b2f05b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=30000000,
    )

    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(key=0x2, value=0x1)
            + Op.SHA3(offset=0x0, size=0x2FFFFF)
            + Op.STOP
        ),
    )
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(
                key=0x1,
                value=Op.CALL(
                    gas=0x927C0,
                    address=0x766B2CF0691F51029181FC511395B7AB71353A88,
                    value=0xA,
                    args_offset=0x0,
                    args_size=0x40,
                    ret_offset=0x0,
                    ret_size=0x40,
                ),
            )
            + Op.SSTORE(key=0xB, value=0x1)
            + Op.STOP
        ),
    )
    # Source: LLL
    # {  [[ 0 ]] (CALL 800000 <contract:0x1000000000000000000000000000000000000001> 20 0 64 0 64 ) }  # noqa: E501
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.SSTORE(
                key=0x0,
                value=Op.CALL(
                    gas=0xC3500,
                    address=0xA781AD010268E97D590D07E5B442975243B2F05B,
                    value=0x14,
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
        gas_limit=1000000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        callee: Account(
            code=(
                Op.SSTORE(key=0x2, value=0x1)
                + Op.SHA3(offset=0x0, size=0x2FFFFF)
                + Op.STOP
            ),
        ),
        callee_1: Account(
            storage={11: 1},
            code=(
                Op.SSTORE(
                    key=0x1,
                    value=Op.CALL(
                        gas=0x927C0,
                        address=0x766B2CF0691F51029181FC511395B7AB71353A88,
                        value=0xA,
                        args_offset=0x0,
                        args_size=0x40,
                        ret_offset=0x0,
                        ret_size=0x40,
                    ),
                )
                + Op.SSTORE(key=0xB, value=0x1)
                + Op.STOP
            ),
        ),
        contract: Account(
            storage={0: 1},
            code=(
                Op.SSTORE(
                    key=0x0,
                    value=Op.CALL(
                        gas=0xC3500,
                        address=0xA781AD010268E97D590D07E5B442975243B2F05B,
                        value=0x14,
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
