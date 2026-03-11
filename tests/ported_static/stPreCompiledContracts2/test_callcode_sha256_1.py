"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stPreCompiledContracts2/CALLCODESha256_1Filler.json
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
        "tests/static/state_tests/stPreCompiledContracts2/CALLCODESha256_1Filler.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_callcode_sha256_1(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0xc4009bc3b312ce413bfb8734800aa7b54261856d")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    # Source: LLL
    # { [[ 2 ]] (CALLCODE 500 2 0 0 0 0 32) [[ 0 ]] (MLOAD 0)}
    pre[contract] = Account(
        balance=0x1312D00,
        nonce=0,
        code=(
            Op.SSTORE(
                key=0x2,
                value=Op.CALLCODE(
                    gas=0x1F4,
                    address=0x2,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x20,
                ),
            )
            + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
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
        gas_limit=365224,
        gas_price=10,
        nonce=0,
        value=100000,
    )

    post = {
        contract: Account(
            storage={
                0: 0xE3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855,  # noqa: E501
                2: 1,
            },
            code=(
                Op.SSTORE(
                    key=0x2,
                    value=Op.CALLCODE(
                        gas=0x1F4,
                        address=0x2,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    ),
                )
                + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                + Op.STOP
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
