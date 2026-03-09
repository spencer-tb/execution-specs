"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stEIP150Specific
SuicideToNotExistingContractFiller.json
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
        "tests/static/state_tests/stEIP150Specific/SuicideToNotExistingContractFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_suicide_to_not_existing_contract(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xfaa10b404ab607779993c016cd5da73ae1f29d7e")
    contract = Address("0xbabae893bee69e2141e0e92f2251664ac445ea2a")
    callee = Address("0x09d6d7885d3d58a49c8352635776c205f722501c")

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
        code=bytes.fromhex("732000000000000000000000000000000000000115ff00"),
    )
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "5a600052600060006000600060007309d6d7885d3d58a49c8352635776c205f722501c61"  # noqa: E501
            "ea60f1505a6000510360015500"
        ),
    )
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
                "732000000000000000000000000000000000000115ff00"
            ),
        ),
        contract: Account(
            storage={1: 10237},
            code=bytes.fromhex(
                "5a600052600060006000600060007309d6d7885d3d58a49c8352635776c205f722501c61ea60f1505a6000510360015500"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
