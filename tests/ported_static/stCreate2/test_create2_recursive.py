"""
Create2 inside Create2 inside Create2....

Ported from:
tests/static/state_tests/stCreate2/Create2RecursiveFiller.json
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
    ["tests/static/state_tests/stCreate2/Create2RecursiveFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.valid_until("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit, expected_post",
    [
        (
            9151314442816847871,
            {
                Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(
                    code=Op.MSTORE(
                        offset=0x0,
                        value=0x606460006000396103E85A10601B576000606460006000F5601D565B5A5B,  # noqa: E501
                    )
                    + Op.CREATE2(value=0x0, offset=0x2, size=0x1E, salt=0x0)
                    + Op.STOP
                )
            },
        ),
        (
            20070000000000,
            {
                Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(
                    code=Op.MSTORE(
                        offset=0x0,
                        value=0x606460006000396103E85A10601B576000606460006000F5601D565B5A5B,  # noqa: E501
                    )
                    + Op.CREATE2(value=0x0, offset=0x2, size=0x1E, salt=0x0)
                    + Op.STOP
                )
            },
        ),
        (
            20080000000000,
            {
                Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(
                    code=Op.MSTORE(
                        offset=0x0,
                        value=0x606460006000396103E85A10601B576000606460006000F5601D565B5A5B,  # noqa: E501
                    )
                    + Op.CREATE2(value=0x0, offset=0x2, size=0x1E, salt=0x0)
                    + Op.STOP
                )
            },
        ),
    ],
    ids=["case0", "case1", "case2"],
)
@pytest.mark.pre_alloc_mutable
def test_create2_recursive(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
    expected_post: dict,
) -> None:
    """Create2 inside Create2 inside Create2...."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[sender] = Account(
        balance=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
        nonce=0,
    )
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.MSTORE(
                offset=0x0,
                value=0x606460006000396103E85A10601B576000606460006000F5601D565B5A5B,  # noqa: E501
            )
            + Op.CREATE2(value=0x0, offset=0x2, size=0x1E, salt=0x0)
            + Op.STOP
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
