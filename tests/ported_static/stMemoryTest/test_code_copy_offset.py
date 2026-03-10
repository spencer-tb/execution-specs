"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stMemoryTest/codeCopyOffsetFiller.json
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
    ["tests/static/state_tests/stMemoryTest/codeCopyOffsetFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_code_copy_offset(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x2e3d0156d2b99a6eacba540c55f423c8f5a33143")
    contract = Address("0xaf89a7504341a87e1cfdffd483a00a4688469b3d")
    callee = Address("0x27d16e1d3cc862149f1e7162e612635fcaef9ff4")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    pre[callee] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=1,
        code=(
            Op.MSTORE(
                offset=0x0,
                value=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
            )
            + Op.CODECOPY(dest_offset=0x0, offset=0xFFFF, size=0x10)
            + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
            + Op.STOP
        ),
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=1,
        code=(
            Op.MSTORE(offset=0x0, value=0x123456789ABCDEF)
            + Op.CALL(
                gas=0xFFFF,
                address=0x27D16E1D3CC862149F1E7162E612635FCAEF9FF4,
                value=Op.DUP1,
                args_offset=Op.DUP2,
                args_size=0xF,
                ret_offset=Op.DUP1,
                ret_size=0x0,
            )
            + Op.STOP
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xb1f4cbc3a50042184425a6f9e996d0910f7ba879457ce5dac5c71e498ad3c005"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=400000,
        gas_price=10,
        nonce=0,
        value=100000,
    )

    post = {
        callee: Account(
            storage={0: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF},
            code=(
                Op.MSTORE(
                    offset=0x0,
                    value=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                )
                + Op.CODECOPY(dest_offset=0x0, offset=0xFFFF, size=0x10)
                + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                + Op.STOP
            ),
        ),
        contract: Account(
            code=(
                Op.MSTORE(offset=0x0, value=0x123456789ABCDEF)
                + Op.CALL(
                    gas=0xFFFF,
                    address=0x27D16E1D3CC862149F1E7162E612635FCAEF9FF4,
                    value=Op.DUP1,
                    args_offset=Op.DUP2,
                    args_size=0xF,
                    ret_offset=Op.DUP1,
                    ret_size=0x0,
                )
                + Op.STOP
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
