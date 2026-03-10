"""
DELEGATECALL -> DELEGATECALL2 -> CALL -> DELEGATECALL2 -> ...

Ported from:
tests/static/state_tests/stCallDelegateCodesHomestead
callcodecallcodecall_ABCB_RECURSIVEFiller.json
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
        "tests/static/state_tests/stCallDelegateCodesHomestead/callcodecallcodecall_ABCB_RECURSIVEFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_callcodecallcodecall_abcb_recursive(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """DELEGATECALL -> DELEGATECALL2 -> CALL -> DELEGATECALL2 -> ..."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0x15600a91a7af84b8c85782714b3391ed5d73f9a0")
    callee = Address("0x91a8703c1bef34c1e76e152c1f7fb8c336c3be24")
    callee_1 = Address("0xe0b280638526cecd3ec29969b517aeb3fcbb31fa")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=3000000000,
    )

    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.SSTORE(
                key=0x0,
                value=Op.DELEGATECALL(
                    gas=0x17D7840,
                    address=0xE0B280638526CECD3EC29969B517AEB3FCBB31FA,
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
        balance=0x2540BE400,
        nonce=0,
        code=(
            Op.SSTORE(
                key=0x2,
                value=Op.CALL(
                    gas=0x7A120,
                    address=0xE0B280638526CECD3EC29969B517AEB3FCBB31FA,
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
    pre[callee_1] = Account(
        balance=0x2540BE400,
        nonce=0,
        code=(
            Op.SSTORE(
                key=0x1,
                value=Op.DELEGATECALL(
                    gas=0xF4240,
                    address=0x91A8703C1BEF34C1E76E152C1F7FB8C336C3BE24,
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
        gas_limit=600000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            storage={0: 1, 1: 1},
            code=(
                Op.SSTORE(
                    key=0x0,
                    value=Op.DELEGATECALL(
                        gas=0x17D7840,
                        address=0xE0B280638526CECD3EC29969B517AEB3FCBB31FA,
                        args_offset=0x0,
                        args_size=0x40,
                        ret_offset=0x0,
                        ret_size=0x40,
                    ),
                )
                + Op.STOP
            ),
        ),
        callee: Account(
            code=(
                Op.SSTORE(
                    key=0x2,
                    value=Op.CALL(
                        gas=0x7A120,
                        address=0xE0B280638526CECD3EC29969B517AEB3FCBB31FA,
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
        callee_1: Account(
            code=(
                Op.SSTORE(
                    key=0x1,
                    value=Op.DELEGATECALL(
                        gas=0xF4240,
                        address=0x91A8703C1BEF34C1E76E152C1F7FB8C336C3BE24,
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
