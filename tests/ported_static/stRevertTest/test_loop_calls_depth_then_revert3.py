"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRevertTest/LoopCallsDepthThenRevert3Filler.json
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
    [
        "tests/static/state_tests/stRevertTest/LoopCallsDepthThenRevert3Filler.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.valid_until("Prague")
@pytest.mark.pre_alloc_mutable
def test_loop_calls_depth_then_revert3(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xa000000000000000000000000000000000000000")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[contract] = Account(
        balance=10,
        nonce=0,
        code=bytes.fromhex(
            "6103fe60005414603f576001600054016000556000600060006000600073a00000000000"  # noqa: E501
            "00000000000000000000000000005af15061041a600054106053575b66600060006002f0"  # noqa: E501
            "600052600760196003f0505b"
        ),
    )
    pre[sender] = Account(balance=0x13426172C74D822B878FE800000000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=9214364837600034817,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            storage={0: 1022},
            code=bytes.fromhex(
                "6103fe60005414603f576001600054016000556000600060006000600073a0000000000000000000000000000000000000005af15061041a600054106053575b66600060006002f0600052600760196003f0505b"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
