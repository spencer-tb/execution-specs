"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stMemoryStressTest/MLOAD_BoundsFiller.json
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
    ["tests/static/state_tests/stMemoryStressTest/MLOAD_BoundsFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit, expected_post",
    [
        (
            150000,
            {
                Address("0x8b0647e983082e6923f7b20e38972690fce91e9b"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.MLOAD(offset=0xFFFFFFFF)
                    + Op.STOP
                )
            },
        ),
        (
            16777216,
            {
                Address("0x8b0647e983082e6923f7b20e38972690fce91e9b"): Account(
                    code=Op.POP(Op.MLOAD(offset=0x0))
                    + Op.MLOAD(offset=0xFFFFFFFF)
                    + Op.STOP
                )
            },
        ),
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_mload_bounds(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xd468b4c11201f7d9c35fe33e663dba4f904e4748")
    contract = Address("0x8b0647e983082e6923f7b20e38972690fce91e9b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.POP(Op.MLOAD(offset=0x0))
            + Op.MLOAD(offset=0xFFFFFFFF)
            + Op.STOP
        ),
    )
    pre[sender] = Account(balance=0x7FFFFFFFFFFFFFFFFFF, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xfe5be118ad5955e30e0ffc4e1f1bbdcaa7f5a67cb1426c4ac19e32c80eccdc06"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
