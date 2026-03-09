"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stEIP158Specific/CALL_OneVCallSuicide2Filler.json
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
        "tests/static/state_tests/stEIP158Specific/CALL_OneVCallSuicide2Filler.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_call_one_v_call_suicide2(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xfaa10b404ab607779993c016cd5da73ae1f29d7e")
    contract = Address("0xea04224539257fbe043981aa6058fbc1d5e21b1a")
    callee = Address("0x99378e0db04e57ae174ad69770e1b7a0aa805930")
    callee_1 = Address("0xeb201d2887816e041f6e807e804f64f3a7a226fe")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("73eb201d2887816e041f6e807e804f64f3a7a226feff00"),
    )
    pre[contract] = Account(
        balance=100,
        nonce=0,
        code=bytes.fromhex(
            "5a600052600060006000600060017399378e0db04e57ae174ad69770e1b7a0aa80593061"  # noqa: E501
            "ea60f1505a6000510360645500"
        ),
    )
    pre[callee_1] = Account(balance=0, nonce=1)
    pre[sender] = Account(balance=0xE8D4A51000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x4f31b3206fbf0e0e598b9b1a7d8ac86302a0ff1d8930738f1bebae9b67173e52"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=600000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        callee: Account(
            code=bytes.fromhex(
                "73eb201d2887816e041f6e807e804f64f3a7a226feff00"
            ),
        ),
        contract: Account(
            storage={100: 16937},
            code=bytes.fromhex(
                "5a600052600060006000600060017399378e0db04e57ae174ad69770e1b7a0aa80593061ea60f1505a6000510360645500"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
