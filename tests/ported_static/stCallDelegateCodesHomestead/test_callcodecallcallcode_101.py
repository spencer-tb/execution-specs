"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stCallDelegateCodesHomestead
callcodecallcallcode_101Filler.json
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
        "tests/static/state_tests/stCallDelegateCodesHomestead/callcodecallcallcode_101Filler.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_callcodecallcallcode_101(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0xd26e26d5a4796d450bfa296d70c05f02dbc1a4b9")
    callee = Address("0x063f88dcf511e5686bc6b446d10538e665bf81a8")
    callee_1 = Address("0x181b4ed322e192361633cc3c0a418f259ab0cf4b")
    callee_2 = Address("0xae5f44e50ecbf16179774393c643204383fde833")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=30000000,
    )

    pre[callee] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "6040600060406000600173ae5f44e50ecbf16179774393c643204383fde833620493e0f1"  # noqa: E501
            "6001553360055500"
        ),
    )
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "600160035533600455346007553061014a553261014c55366101505538610152553a6101"  # noqa: E501
            "545500"
        ),
    )
    pre[callee_2] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "604060006040600073181b4ed322e192361633cc3c0a418f259ab0cf4b6203d090f46002"  # noqa: E501
            "553360065500"
        ),
    )
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "604060006040600073063f88dcf511e5686bc6b446d10538e665bf81a862055730f46000"  # noqa: E501
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
                "6040600060406000600173ae5f44e50ecbf16179774393c643204383fde833620493e0f16001553360055500"  # noqa: E501
            ),
        ),
        callee_1: Account(
            code=bytes.fromhex(
                "600160035533600455346007553061014a553261014c55366101505538610152553a6101545500"  # noqa: E501
            ),
        ),
        callee_2: Account(
            storage={
                2: 1,
                3: 1,
                4: 0xD26E26D5A4796D450BFA296D70C05F02DBC1A4B9,
                6: 0xD26E26D5A4796D450BFA296D70C05F02DBC1A4B9,
                7: 1,
                330: 0xAE5F44E50ECBF16179774393C643204383FDE833,
                332: 0xEBAF50DEBF10E08302FE4280C32DF010463CA297,
                336: 64,
                338: 39,
                340: 10,
            },
            code=bytes.fromhex(
                "604060006040600073181b4ed322e192361633cc3c0a418f259ab0cf4b6203d090f46002553360065500"  # noqa: E501
            ),
        ),
        contract: Account(
            storage={
                0: 1,
                1: 1,
                5: 0xEBAF50DEBF10E08302FE4280C32DF010463CA297,
            },
            code=bytes.fromhex(
                "604060006040600073063f88dcf511e5686bc6b446d10538e665bf81a862055730f460005500"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
