"""
callcode -> callcode -> callcode -> code oog

Ported from:
tests/static/state_tests/stCallCodes/callcodecallcodecallcode_111_OOGEFiller.json
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
    ["tests/static/state_tests/stCallCodes/callcodecallcodecallcode_111_OOGEFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_callcodecallcodecallcode_111_ooge(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """callcode -> callcode -> callcode -> code oog."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0x9e57433afaff8a546fbc43cf0330afb6561dc550")
    callee = Address("0x1dd747f92062bb53bb8e867ec2902792435f1748")
    callee_1 = Address("0x6322dc554acdcada01cbf7ac6a163d207c34ded2")
    callee_2 = Address("0x913cf7a18f61bab7bccf5607dfa9b730c5976000")

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
        code=Op.SSTORE(key=0x3, value=0x1) + Op.SHA3(offset=0x0, size=0x2fffff) + Op.STOP,
    )
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.SSTORE(key=0x2, value=Op.CALLCODE(gas=0x61a80, address=0x1dd747f92062bb53bb8e867ec2902792435f1748, value=0x0, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40))
        + Op.SSTORE(key=0xb, value=0x1) + Op.STOP
    ),
    )
    pre[callee_2] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.SSTORE(key=0x1, value=Op.CALLCODE(gas=0x927c0, address=0x6322dc554acdcada01cbf7ac6a163d207c34ded2, value=0x0, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40))
        + Op.STOP
    ),
    )
    pre[contract] = Account(
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=(
        Op.SSTORE(key=0x0, value=Op.CALLCODE(gas=0xc3500, address=0x913cf7a18f61bab7bccf5607dfa9b730c5976000, value=0x0, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40))
        + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0xde0b6b3a7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xe04d1ac7ddda0c98397d56a0b501e960d4cd325a39286919ac23c1a07009a869"
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
            code=Op.SSTORE(key=0x3, value=0x1) + Op.SHA3(offset=0x0, size=0x2fffff) + Op.STOP,
        ),
        callee_1: Account(
            code=Op.SSTORE(key=0x2, value=Op.CALLCODE(gas=0x61a80, address=0x1dd747f92062bb53bb8e867ec2902792435f1748, value=0x0, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40)) + Op.SSTORE(key=0xb, value=0x1) + Op.STOP,
        ),
        callee_2: Account(
            code=Op.SSTORE(key=0x1, value=Op.CALLCODE(gas=0x927c0, address=0x6322dc554acdcada01cbf7ac6a163d207c34ded2, value=0x0, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40)) + Op.STOP,
        ),
        contract: Account(
            storage={0: 1, 1: 1, 11: 1},
            code=Op.SSTORE(key=0x0, value=Op.CALLCODE(gas=0xc3500, address=0x913cf7a18f61bab7bccf5607dfa9b730c5976000, value=0x0, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40)) + Op.STOP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
