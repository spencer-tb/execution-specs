"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stSpecialTest/failed_tx_xcf416c53_ParisFiller.json
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
        "tests/static/state_tests/stSpecialTest/failed_tx_xcf416c53_ParisFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_failed_tx_xcf416c53_paris(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x68795c4aa09d6f4ed3e5deddf8c2ad3049a601da")
    sender = Address("0xadd22153059388891d82c6c8e08d80845352bbb0")
    contract = Address("0x7e6e9b4ca1b88937abeaec23bc4b6986caf05188")
    callee = Address("0x76fae819612a29489a1a43208613d8f8557b8898")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=200000000,
    )

    pre[callee] = Account(balance=10, nonce=0)
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "7c0100000000000000000000000000000000000000000000000000000000600035046397"  # noqa: E501
            "dd3054811415610065576004356040526024356060526040516060515b80821215610062"  # noqa: E501
            "5760006000600060006000866000f150600182019150610040565b50505b50"
        ),
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=1)

    tx = Transaction(
        secret_key=Hash(
            "0x0ff8d58222f34f6890ddaa468c023b77d6691ed7d3c4dcddae38336212faf54b"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex(
            "97dd30540000000000000000000000000000000000000000000000000000000000000000"  # noqa: E501
            "00000000000000000000000000000000000000000000000000000000000002bc"
        ),
        gas_limit=16300000,
        gas_price=10,
        nonce=1,
        value=0,
    )

    post = {
        contract: Account(
            code=bytes.fromhex(
                "7c0100000000000000000000000000000000000000000000000000000000600035046397dd3054811415610065576004356040526024356060526040516060515b808212156100625760006000600060006000866000f150600182019150610040565b50505b50"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
