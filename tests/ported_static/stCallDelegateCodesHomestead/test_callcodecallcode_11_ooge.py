"""
DELEGATE -> DELEGATE -> CODE OOG.

Ported from:
tests/static/state_tests/stCallDelegateCodesHomestead
callcodecallcode_11_OOGEFiller.json
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
        "tests/static/state_tests/stCallDelegateCodesHomestead/callcodecallcode_11_OOGEFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_callcodecallcode_11_ooge(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """DELEGATE -> DELEGATE -> CODE OOG."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0x0e7163a4a90126c4a13e52f48e84c74600e844da")
    callee = Address("0x766b2cf0691f51029181fc511395b7ab71353a88")
    callee_1 = Address("0xecb18a704984b0e051e46358d64ef7811f2945ba")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=30000000,
    )

    # Source: LLL
    # {  [[ 0 ]] (DELEGATECALL 800000 <contract:0x1000000000000000000000000000000000000001> 0 64 0 64 ) }  # noqa: E501
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.SSTORE(
                key=0x0,
                value=Op.DELEGATECALL(
                    gas=0xC3500,
                    address=0xECB18A704984B0E051E46358D64EF7811F2945BA,
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
        code=(
            Op.SSTORE(key=0x2, value=0x1)
            + Op.SHA3(offset=0x0, size=0x2FFFFF)
            + Op.STOP
        ),
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(
                key=0x1,
                value=Op.DELEGATECALL(
                    gas=0x927C0,
                    address=0x766B2CF0691F51029181FC511395B7AB71353A88,
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
        contract: Account(
            storage={0: 1, 11: 1},
            code=(
                Op.SSTORE(
                    key=0x0,
                    value=Op.DELEGATECALL(
                        gas=0xC3500,
                        address=0xECB18A704984B0E051E46358D64EF7811F2945BA,
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
                Op.SSTORE(key=0x2, value=0x1)
                + Op.SHA3(offset=0x0, size=0x2FFFFF)
                + Op.STOP
            ),
        ),
        callee_1: Account(
            code=(
                Op.SSTORE(
                    key=0x1,
                    value=Op.DELEGATECALL(
                        gas=0x927C0,
                        address=0x766B2CF0691F51029181FC511395B7AB71353A88,
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
