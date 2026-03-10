"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stDelegatecallTestHomestead
deleagateCallAfterValueTransferFiller.json
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
        "tests/static/state_tests/stDelegatecallTestHomestead/deleagateCallAfterValueTransferFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_deleagate_call_after_value_transfer(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x6fda566d1950d7e0a4dac1de87109b2ca7d12da4")
    contract = Address("0xdd657898b318b3d967472eaa82bb75c4141b6735")
    callee = Address("0x0346aa231cb52f55ddf201dc19ca469cc73e6495")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=Op.CALLVALUE)
            + Op.SSTORE(key=0x1, value=Op.CALLER)
            + Op.SSTORE(key=0x2, value=Op.CALLDATALOAD(offset=0x0))
            + Op.STOP
        ),
    )
    pre[sender] = Account(balance=0x2386F26FC10000, nonce=0)
    pre[contract] = Account(
        balance=0x10C8E0,
        nonce=0,
        code=(
            Op.MSTORE(offset=0x0, value=0x1)
            + Op.DELEGATECALL(
                gas=0x186A0,
                address=0x346AA231CB52F55DDF201DC19CA469CC73E6495,
                args_offset=0x0,
                args_size=0x40,
                ret_offset=0x0,
                ret_size=0x40,
            )
            + Op.STOP
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0x3722faab4d25b944622d559ea4bcf38b4bcf3caf07a6d2c6fd99321c1a66c974"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=453081,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        callee: Account(
            code=(
                Op.SSTORE(key=0x0, value=Op.CALLVALUE)
                + Op.SSTORE(key=0x1, value=Op.CALLER)
                + Op.SSTORE(key=0x2, value=Op.CALLDATALOAD(offset=0x0))
                + Op.STOP
            ),
        ),
        contract: Account(
            storage={
                1: 0x6FDA566D1950D7E0A4DAC1DE87109B2CA7D12DA4,
                2: 1,
            },
            code=(
                Op.MSTORE(offset=0x0, value=0x1)
                + Op.DELEGATECALL(
                    gas=0x186A0,
                    address=0x346AA231CB52F55DDF201DC19CA469CC73E6495,
                    args_offset=0x0,
                    args_size=0x40,
                    ret_offset=0x0,
                    ret_size=0x40,
                )
                + Op.STOP
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
