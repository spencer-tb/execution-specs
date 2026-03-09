"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stCallDelegateCodesHomestead
callcodecallcall_100Filler.json
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
        "tests/static/state_tests/stCallDelegateCodesHomestead/callcodecallcall_100Filler.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_callcodecallcall_100(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0xd26e26d5a4796d450bfa296d70c05f02dbc1a4b9")
    callee = Address("0x181b4ed322e192361633cc3c0a418f259ab0cf4b")
    callee_1 = Address("0x3c83297c6dcbc0520cd68714f85dc444469fb287")
    callee_2 = Address("0x5f6eacde5a1e97f48c5db4ee84fdf614f9dd9756")

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
            "600160035533600455346007553061014a553261014c55366101505538610152553a6101"  # noqa: E501
            "545500"
        ),
    )
    pre[callee_1] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "60406000604060006001735f6eacde5a1e97f48c5db4ee84fdf614f9dd9756620493e0f1"  # noqa: E501
            "6001553360055500"
        ),
    )
    pre[callee_2] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "6040600060406000600273181b4ed322e192361633cc3c0a418f259ab0cf4b6203d090f1"  # noqa: E501
            "60025500"
        ),
    )
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "6040600060406000733c83297c6dcbc0520cd68714f85dc444469fb28762055730f46000"  # noqa: E501
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
            storage={
                3: 1,
                4: 0x5F6EACDE5A1E97F48C5DB4EE84FDF614F9DD9756,
                7: 2,
                330: 0x181B4ED322E192361633CC3C0A418F259AB0CF4B,
                332: 0xEBAF50DEBF10E08302FE4280C32DF010463CA297,
                336: 64,
                338: 39,
                340: 10,
            },
            code=bytes.fromhex(
                "600160035533600455346007553061014a553261014c55366101505538610152553a6101545500"  # noqa: E501
            ),
        ),
        callee_1: Account(
            code=bytes.fromhex(
                "60406000604060006001735f6eacde5a1e97f48c5db4ee84fdf614f9dd9756620493e0f16001553360055500"  # noqa: E501
            ),
        ),
        callee_2: Account(
            storage={2: 1},
            code=bytes.fromhex(
                "6040600060406000600273181b4ed322e192361633cc3c0a418f259ab0cf4b6203d090f160025500"  # noqa: E501
            ),
        ),
        contract: Account(
            storage={
                0: 1,
                1: 1,
                5: 0xEBAF50DEBF10E08302FE4280C32DF010463CA297,
            },
            code=bytes.fromhex(
                "6040600060406000733c83297c6dcbc0520cd68714f85dc444469fb28762055730f460005500"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
