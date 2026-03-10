"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stNonZeroCallsTest
NonZeroValue_CALLCODE_ToNonNonZeroBalanceFiller.json
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
        "tests/static/state_tests/stNonZeroCallsTest/NonZeroValue_CALLCODE_ToNonNonZeroBalanceFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_non_zero_value_callcode_to_non_non_zero_balance(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xfaa10b404ab607779993c016cd5da73ae1f29d7e")
    contract = Address("0x082a0810da3f7a5b41a2d8291511fe800d7a021c")
    callee = Address("0x9089da66e8bbc08846842a301905501bc8525dc4")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.MSTORE(offset=0x0, value=Op.GAS)
            + Op.SSTORE(
                key=0x1,
                value=Op.CALLCODE(
                    gas=0xEA60,
                    address=0x9089DA66E8BBC08846842A301905501BC8525DC4,
                    value=0x1,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.SSTORE(key=0x64, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS))
            + Op.STOP
        ),
    )
    pre[callee] = Account(balance=100, nonce=0)
    pre[sender] = Account(balance=0xE8D4A51000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x4f31b3206fbf0e0e598b9b1a7d8ac86302a0ff1d8930738f1bebae9b67173e52"  # noqa: E501
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
            storage={100: 11535},
            code=(
                Op.MSTORE(offset=0x0, value=Op.GAS)
                + Op.SSTORE(
                    key=0x1,
                    value=Op.CALLCODE(
                        gas=0xEA60,
                        address=0x9089DA66E8BBC08846842A301905501BC8525DC4,
                        value=0x1,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    ),
                )
                + Op.SSTORE(
                    key=0x64, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                )
                + Op.STOP
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
