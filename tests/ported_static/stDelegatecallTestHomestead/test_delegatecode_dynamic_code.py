"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stDelegatecallTestHomestead
delegatecodeDynamicCodeFiller.json
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
        "tests/static/state_tests/stDelegatecallTestHomestead/delegatecodeDynamicCodeFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_delegatecode_dynamic_code(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x1000000000000000000000000000000000000000")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    pre[contract] = Account(
        balance=0x2710,
        nonce=0,
        code=bytes.fromhex(
            "7f716860016000553360145560005260096017f36000526012600e6001f0600a55600052"  # noqa: E501
            "7f604060006040600073ffe4ebd2a68c02d9dcb0a17283d13346beb2d8b6620186602052"  # noqa: E501
            "7fa0f4600b55000000000000000000000000000000000000000000000000000000604052"  # noqa: E501
            "606060006001f000"
        ),
    )
    pre[sender] = Account(balance=0x2386F26FC10000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=453081,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            code=bytes.fromhex(
                "7f716860016000553360145560005260096017f36000526012600e6001f0600a556000527f604060006040600073ffe4ebd2a68c02d9dcb0a17283d13346beb2d8b66201866020527fa0f4600b55000000000000000000000000000000000000000000000000000000604052606060006001f000"  # noqa: E501
            ),
        ),
        Address("0x13136008b64ff592819b2fa6d43f2835c452020e"): Account(
            storage={
                10: 0x568A95F77B047BECE6AA68843D2019332C46A585,
                11: 1,
            },
        ),
        Address("0x568a95f77b047bece6aa68843d2019332c46a585"): Account(
            code=bytes.fromhex("600160005533601455"),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
