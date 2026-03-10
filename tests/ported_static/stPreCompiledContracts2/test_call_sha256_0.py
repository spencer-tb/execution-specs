"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stPreCompiledContracts2/CallSha256_0Filler.json
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
        "tests/static/state_tests/stPreCompiledContracts2/CallSha256_0Filler.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_call_sha256_0(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0xdcddac785b7920159cf9aa510ecd630640710567")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[contract] = Account(
        balance=0x1312D00,
        nonce=0,
        code=(
            Op.MSTORE(offset=0x0, value=0x1)
            + Op.CALL(
                gas=0xFF,
                address=0x2,
                value=0x0,
                args_offset=0x0,
                args_size=0x20,
                ret_offset=0x0,
                ret_size=0x20,
            )
            + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
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
                0: 0xEC4916DD28FC4C10D78E287CA5D9CC51EE1AE73CBFDE08C6B37324CBFAAC8BC5,  # noqa: E501
            },
            code=(
                Op.MSTORE(offset=0x0, value=0x1)
                + Op.CALL(
                    gas=0xFF,
                    address=0x2,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x20,
                    ret_offset=0x0,
                    ret_size=0x20,
                )
                + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
