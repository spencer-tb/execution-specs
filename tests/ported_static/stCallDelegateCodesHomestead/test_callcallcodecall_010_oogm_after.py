"""
CALL -> (DELEGATE -> CALL -> CODE) OOG.

Ported from:
tests/static/state_tests/stCallDelegateCodesHomestead
callcallcodecall_010_OOGMAfterFiller.json
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
        "tests/static/state_tests/stCallDelegateCodesHomestead/callcallcodecall_010_OOGMAfterFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_callcallcodecall_010_oogm_after(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """CALL -> (DELEGATE -> CALL -> CODE) OOG."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0xe54ccfa5e33a84943997885f0ab9c19c587d8c4f")
    callee = Address("0x1adae71ad3aeec97978e38be04da2a1773dfc506")
    callee_1 = Address("0x8d7270785422b63a97d83bada6aac80bebc3a99d")
    callee_2 = Address("0xb126c622075b1189fb6c45e851641cfaddf65b36")

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
            Op.SSTORE(
                key=0x1,
                value=Op.DELEGATECALL(
                    gas=0x927C0,
                    address=0x8D7270785422B63A97D83BADA6AAC80BEBC3A99D,
                    args_offset=0x0,
                    args_size=0x40,
                    ret_offset=0x0,
                    ret_size=0x40,
                ),
            )
            + Op.SHA3(offset=0x0, size=0x2FFFFF)
            + Op.STOP
        ),
    )
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(
                key=0x2,
                value=Op.CALL(
                    gas=0x61A80,
                    address=0xB126C622075B1189FB6C45E851641CFADDF65B36,
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
    pre[callee_2] = Account(
        balance=0,
        nonce=0,
        code=Op.SSTORE(key=0x3, value=0x1) + Op.STOP,
    )
    # Source: LLL
    # {  [[ 0 ]] (CALL 800000 <contract:0x1000000000000000000000000000000000000001> 0 0 64 0 64 ) [[11]] 1 }  # noqa: E501
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.SSTORE(
                key=0x0,
                value=Op.CALL(
                    gas=0xC3500,
                    address=0x1ADAE71AD3AEEC97978E38BE04DA2A1773DFC506,
                    value=0x0,
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
                Op.SSTORE(
                    key=0x1,
                    value=Op.DELEGATECALL(
                        gas=0x927C0,
                        address=0x8D7270785422B63A97D83BADA6AAC80BEBC3A99D,
                        args_offset=0x0,
                        args_size=0x40,
                        ret_offset=0x0,
                        ret_size=0x40,
                    ),
                )
                + Op.SHA3(offset=0x0, size=0x2FFFFF)
                + Op.STOP
            ),
        ),
        callee_1: Account(
            code=(
                Op.SSTORE(
                    key=0x2,
                    value=Op.CALL(
                        gas=0x61A80,
                        address=0xB126C622075B1189FB6C45E851641CFADDF65B36,
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
        callee_2: Account(code=Op.SSTORE(key=0x3, value=0x1) + Op.STOP),
        contract: Account(
            storage={11: 1},
            code=(
                Op.SSTORE(
                    key=0x0,
                    value=Op.CALL(
                        gas=0xC3500,
                        address=0x1ADAE71AD3AEEC97978E38BE04DA2A1773DFC506,
                        value=0x0,
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
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
