"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stReturnDataTest
returndatasize_initial_zero_readFiller.json
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
        "tests/static/state_tests/stReturnDataTest/returndatasize_initial_zero_readFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        (
            "",
            {
                Address("0x537cd1744af41c3a74d5aa5ae93958d1160ca98f"): Account(
                    code=Op.RETURNDATACOPY(
                        dest_offset=0x0, offset=0x0, size=0x0
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                )
            },
        ),
        (
            "992919aa",
            {
                Address("0x537cd1744af41c3a74d5aa5ae93958d1160ca98f"): Account(
                    code=Op.RETURNDATACOPY(
                        dest_offset=0x0, offset=0x0, size=0x0
                    )
                    + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                )
            },
        ),
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_returndatasize_initial_zero_read(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xc102734f6a1e4747310179c0a0fc16e674aa901d")
    contract = Address("0x537cd1744af41c3a74d5aa5ae93958d1160ca98f")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=111669149696,
    )

    # Source: LLL
    # { (RETURNDATACOPY 0 0 0) (SSTORE 0 (MLOAD 0)) }
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.RETURNDATACOPY(dest_offset=0x0, offset=0x0, size=0x0)
            + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
            + Op.STOP
        ),
        storage={0x0: 0x1},
    )
    pre[sender] = Account(balance=0x6400000000, nonce=0)

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x834185262e53584684bf2b72c64e510013c235d0f45e462db65900455df45a35"  # noqa: E501
        ),
        to=contract,
        data=tx_data,
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
