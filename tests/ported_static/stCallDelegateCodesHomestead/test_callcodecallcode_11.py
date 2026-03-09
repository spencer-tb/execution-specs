"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stCallDelegateCodesHomestead
callcodecallcode_11Filler.json
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
        "tests/static/state_tests/stCallDelegateCodesHomestead/callcodecallcode_11Filler.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_callcodecallcode_11(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0xd26e26d5a4796d450bfa296d70c05f02dbc1a4b9")
    callee = Address("0x2b0691cd58a1cf4628d642e9aca9ab04946e3ec9")
    callee_1 = Address("0xcb4336321fac69281bd2902d427f4ef9e8584251")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=30000000,
    )

    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "604060006040600073cb4336321fac69281bd2902d427f4ef9e85842516203d090f46001"  # noqa: E501
            "5500"
        ),
    )
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "600160025533600455346007553060e6553260e8553660ec553860ee553a60f05500"  # noqa: E501
        ),
    )
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "6040600060406000732b0691cd58a1cf4628d642e9aca9ab04946e3ec962055730f46000"  # noqa: E501
            "5500"
        ),
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xe04d1ac7ddda0c98397d56a0b501e960d4cd325a39286919ac23c1a07009a869"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=3000000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        callee: Account(
            code=bytes.fromhex(
                "604060006040600073cb4336321fac69281bd2902d427f4ef9e85842516203d090f460015500"  # noqa: E501
            ),
        ),
        callee_1: Account(
            code=bytes.fromhex(
                "600160025533600455346007553060e6553260e8553660ec553860ee553a60f05500"  # noqa: E501
            ),
        ),
        contract: Account(
            storage={
                0: 1,
                1: 1,
                2: 1,
                4: 0xEBAF50DEBF10E08302FE4280C32DF010463CA297,
                230: 0xD26E26D5A4796D450BFA296D70C05F02DBC1A4B9,
                232: 0xEBAF50DEBF10E08302FE4280C32DF010463CA297,
                236: 64,
                238: 34,
                240: 10,
            },
            code=bytes.fromhex(
                "6040600060406000732b0691cd58a1cf4628d642e9aca9ab04946e3ec962055730f460005500"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
