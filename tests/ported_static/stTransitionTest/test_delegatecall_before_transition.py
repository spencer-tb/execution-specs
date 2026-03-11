"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stTransitionTest
delegatecallBeforeTransitionFiller.json
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
        "tests/static/state_tests/stTransitionTest/delegatecallBeforeTransitionFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_delegatecall_before_transition(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0x55bb8a8658b848ebbbb73cbf6ac9d59d715aec58")
    callee = Address("0x000d3f6e432d6891a965fc56d39e729652a0762a")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=30000000,
    )

    pre[callee] = Account(
        balance=23,
        nonce=0,
        code=(
            Op.SSTORE(key=0x1, value=Op.CALLER)
            + Op.SSTORE(key=0x2, value=Op.CALLVALUE)
            + Op.STOP
        ),
    )
    # Source: LLL
    # {  [[ 0 ]] (DELEGATECALL 500000 <contract:0x945304eb96065b2a98b57a48a06ae28d285a71b5> 0 64 0 2 ) }  # noqa: E501
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.SSTORE(
                key=0x0,
                value=Op.DELEGATECALL(
                    gas=0x7A120,
                    address=0xD3F6E432D6891A965FC56D39E729652A0762A,
                    args_offset=0x0,
                    args_size=0x40,
                    ret_offset=0x0,
                    ret_size=0x2,
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
                Op.SSTORE(key=0x1, value=Op.CALLER)
                + Op.SSTORE(key=0x2, value=Op.CALLVALUE)
                + Op.STOP
            ),
        ),
        contract: Account(
            storage={
                0: 1,
                1: 0xEBAF50DEBF10E08302FE4280C32DF010463CA297,
            },
            code=(
                Op.SSTORE(
                    key=0x0,
                    value=Op.DELEGATECALL(
                        gas=0x7A120,
                        address=0xD3F6E432D6891A965FC56D39E729652A0762A,
                        args_offset=0x0,
                        args_size=0x40,
                        ret_offset=0x0,
                        ret_size=0x2,
                    ),
                )
                + Op.STOP
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
