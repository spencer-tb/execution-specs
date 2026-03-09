"""
Ported from:
tests/static/state_tests/stPreCompiledContracts2/CallSha256_3_prefix0Filler.json
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
    ["tests/static/state_tests/stPreCompiledContracts2/CallSha256_3_prefix0Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_call_sha256_3_prefix0(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0x5d4b89a232555bc139aa244672611edf28d276c7")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[contract] = Account(
        balance=0x1312d00,
        nonce=0,
        code=(
        Op.MSTORE(offset=0x0, value=0xf34578907f)
        + Op.SSTORE(key=0x2, value=Op.CALL(gas=0x1f4, address=0x2, value=0x0, args_offset=0x0, args_size=0x25, ret_offset=0x0, ret_size=0x20))
        + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0)) + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0xde0b6b3a7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xe04d1ac7ddda0c98397d56a0b501e960d4cd325a39286919ac23c1a07009a869"
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
            storage={0: 0x7392925565d67be8e9620aacbcfaecd8cb6ec58d709d25da9eccf1d08a41ce35, 2: 1},
            code=Op.MSTORE(offset=0x0, value=0xf34578907f) + Op.SSTORE(key=0x2, value=Op.CALL(gas=0x1f4, address=0x2, value=0x0, args_offset=0x0, args_size=0x25, ret_offset=0x0, ret_size=0x20)) + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0)) + Op.STOP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
