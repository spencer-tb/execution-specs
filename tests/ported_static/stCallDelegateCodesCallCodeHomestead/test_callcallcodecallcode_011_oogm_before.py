"""
CALLCODE -> DELEGATE -> OOG DELEGATE -> CODE.

Ported from:
tests/static/state_tests/stCallDelegateCodesCallCodeHomestead
callcallcodecallcode_011_OOGMBeforeFiller.json
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
        "tests/static/state_tests/stCallDelegateCodesCallCodeHomestead/callcallcodecallcode_011_OOGMBeforeFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_callcallcodecallcode_011_oogm_before(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """CALLCODE -> DELEGATE -> OOG DELEGATE -> CODE."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0xa74ca10b765dcda3b60687f73f2881e2a56eda64")
    callee = Address("0xb126c622075b1189fb6c45e851641cfaddf65b36")
    callee_1 = Address("0xb5104f0f7758ce0caac73f593c6d63eb9a5ef905")
    callee_2 = Address("0xc176d297ff74c0f684b73d6cc8617e7f5ffe34fe")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=30000000,
    )

    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.SSTORE(
                key=0x0,
                value=Op.CALLCODE(
                    gas=0x249F0,
                    address=0xB5104F0F7758CE0CAAC73F593C6D63EB9A5EF905,
                    value=0x0,
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
        code=Op.SSTORE(key=0x3, value=0x1) + Op.STOP,
    )
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(
                key=0x1,
                value=Op.DELEGATECALL(
                    gas=0x9C90,
                    address=0xC176D297FF74C0F684B73D6CC8617E7F5FFE34FE,
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
    pre[callee_2] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.POP(Op.SHA3(offset=0x0, size=0x2FFFFF))
            + Op.SSTORE(
                key=0x2,
                value=Op.DELEGATECALL(
                    gas=0x4E34,
                    address=0xB126C622075B1189FB6C45E851641CFADDF65B36,
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
        gas_limit=172000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            storage={0: 1, 11: 1},
            code=(
                Op.SSTORE(
                    key=0x0,
                    value=Op.CALLCODE(
                        gas=0x249F0,
                        address=0xB5104F0F7758CE0CAAC73F593C6D63EB9A5EF905,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x40,
                        ret_offset=0x0,
                        ret_size=0x40,
                    ),
                )
                + Op.STOP
            ),
        ),
        callee: Account(code=Op.SSTORE(key=0x3, value=0x1) + Op.STOP),
        callee_1: Account(
            code=(
                Op.SSTORE(
                    key=0x1,
                    value=Op.DELEGATECALL(
                        gas=0x9C90,
                        address=0xC176D297FF74C0F684B73D6CC8617E7F5FFE34FE,
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
        callee_2: Account(
            code=(
                Op.POP(Op.SHA3(offset=0x0, size=0x2FFFFF))
                + Op.SSTORE(
                    key=0x2,
                    value=Op.DELEGATECALL(
                        gas=0x4E34,
                        address=0xB126C622075B1189FB6C45E851641CFADDF65B36,
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
