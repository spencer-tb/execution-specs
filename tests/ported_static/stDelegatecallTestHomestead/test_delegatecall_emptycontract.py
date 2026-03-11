"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stDelegatecallTestHomestead
delegatecallEmptycontractFiller.json
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
        "tests/static/state_tests/stDelegatecallTestHomestead/delegatecallEmptycontractFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_delegatecall_emptycontract(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x739cba7753b12ea8d3a364e609b7a5cec9c4c320")
    contract = Address("0x4a88cf3b3f1dabdd27e62fcb5df86d7d685e0044")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    # Source: LLL
    # { [[ 0 ]] (DELEGATECALL 50000 0x945304eb96065b2a98b57a48a06ae28d285a71b5 0 64 0 64 )}  # noqa: E501
    pre[contract] = Account(
        balance=1000,
        nonce=0,
        code=(
            Op.SSTORE(
                key=0x0,
                value=Op.DELEGATECALL(
                    gas=0xC350,
                    address=0x945304EB96065B2A98B57A48A06AE28D285A71B5,
                    args_offset=0x0,
                    args_size=0x40,
                    ret_offset=0x0,
                    ret_size=0x40,
                ),
            )
            + Op.STOP
        ),
    )
    pre[sender] = Account(balance=0x10C8E0, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x11489f9b076d3f3185ebe5c6e2dbedbe9e283a6ce75895780134252b3dd5dbcc"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=105044,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            storage={0: 1},
            code=(
                Op.SSTORE(
                    key=0x0,
                    value=Op.DELEGATECALL(
                        gas=0xC350,
                        address=0x945304EB96065B2A98B57A48A06AE28D285A71B5,
                        args_offset=0x0,
                        args_size=0x40,
                        ret_offset=0x0,
                        ret_size=0x40,
                    ),
                )
                + Op.STOP
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
