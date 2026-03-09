"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stLogTests/log4_logMemsizeTooHighFiller.json
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

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


@pytest.mark.ported_from(
    ["tests/static/state_tests/stLogTests/log4_logMemsizeTooHighFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_log4_log_memsize_too_high(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0x1e5597b6168fe79952cb2de7af91c3449bc95bd4")
    callee = Address("0x59e2f8fdf907d6e627fcafd97606824ce1fe1e2a")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "600060006000600060177359e2f8fdf907d6e627fcafd97606824ce1fe1e2a6103e8f160"  # noqa: E501
            "005500"
        ),
    )
    pre[callee] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "7faabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd600052"  # noqa: E501
            "60006000600060007fffffffffffffffffffffffffffffffffffffffffffffffffffffff"  # noqa: E501
            "ffffffffff6001a400"
        ),
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xe04d1ac7ddda0c98397d56a0b501e960d4cd325a39286919ac23c1a07009a869"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=210000,
        gas_price=10,
        nonce=0,
        value=100000,
    )

    post = {
        contract: Account(
            code=bytes.fromhex(
                "600060006000600060177359e2f8fdf907d6e627fcafd97606824ce1fe1e2a6103e8f160005500"  # noqa: E501
            ),
        ),
        callee: Account(
            code=bytes.fromhex(
                "7faabbffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdd60005260006000600060007fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff6001a400"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
