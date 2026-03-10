"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stMemExpandingEIP150Calls
CreateAndGasInsideCreateWithMemExpandingCallsFiller.json
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
        "tests/static/state_tests/stMemExpandingEIP150Calls/CreateAndGasInsideCreateWithMemExpandingCallsFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_create_and_gas_inside_create_with_mem_expanding_calls(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[sender] = Account(balance=0xE8D4A51000, nonce=0)
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(key=0xA, value=Op.GAS)
            + Op.MSTORE(offset=0x0, value=0x5A60FD55)
            + Op.SSTORE(
                key=0xB, value=Op.CREATE(value=0x0, offset=0x1C, size=0x4)
            )
            + Op.SSTORE(key=0x9, value=Op.GAS)
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
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
            storage={
                9: 0x75596,
                10: 0x8D5B6,
                11: 0xF1ECF98489FA9ED60A664FC4998DB699CFA39D40,
            },
            code=(
                Op.SSTORE(key=0xA, value=Op.GAS)
                + Op.MSTORE(offset=0x0, value=0x5A60FD55)
                + Op.SSTORE(
                    key=0xB,
                    value=Op.CREATE(value=0x0, offset=0x1C, size=0x4),
                )
                + Op.SSTORE(key=0x9, value=Op.GAS)
            ),
        ),
        Address("0xf1ecf98489fa9ed60a664fc4998db699cfa39d40"): Account(
            storage={253: 0x7E23D},
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
