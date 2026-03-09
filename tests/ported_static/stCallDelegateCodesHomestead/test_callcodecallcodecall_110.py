"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stCallDelegateCodesHomestead
callcodecallcodecall_110Filler.json
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
        "tests/static/state_tests/stCallDelegateCodesHomestead/callcodecallcodecall_110Filler.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_callcodecallcodecall_110(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0xd26e26d5a4796d450bfa296d70c05f02dbc1a4b9")
    callee = Address("0x669e33b1aa30351139b73c3942acde1b09e75bcd")
    callee_1 = Address("0x78b5bd809b0b6fe0b8e371f286d7aa6a3b930718")
    callee_2 = Address("0x7e63847aad8ca50fb7c04777dce6871a6bf8de0c")

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
            "60406000604060007378b5bd809b0b6fe0b8e371f286d7aa6a3b930718620493e0f46001"  # noqa: E501
            "553360055500"
        ),
    )
    pre[callee_1] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "60406000604060006001737e63847aad8ca50fb7c04777dce6871a6bf8de0c6203d090f1"  # noqa: E501
            "6002553360065500"
        ),
    )
    pre[callee_2] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "600160035533600455346007553061014a553261014c55366101505538610152553a6101"  # noqa: E501
            "545500"
        ),
    )
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "604060006040600073669e33b1aa30351139b73c3942acde1b09e75bcd62055730f46000"  # noqa: E501
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
                "60406000604060007378b5bd809b0b6fe0b8e371f286d7aa6a3b930718620493e0f46001553360055500"  # noqa: E501
            ),
        ),
        callee_1: Account(
            code=bytes.fromhex(
                "60406000604060006001737e63847aad8ca50fb7c04777dce6871a6bf8de0c6203d090f16002553360065500"  # noqa: E501
            ),
        ),
        callee_2: Account(
            storage={
                3: 1,
                4: 0xD26E26D5A4796D450BFA296D70C05F02DBC1A4B9,
                7: 1,
                330: 0x7E63847AAD8CA50FB7C04777DCE6871A6BF8DE0C,
                332: 0xEBAF50DEBF10E08302FE4280C32DF010463CA297,
                336: 64,
                338: 39,
                340: 10,
            },
            code=bytes.fromhex(
                "600160035533600455346007553061014a553261014c55366101505538610152553a6101545500"  # noqa: E501
            ),
        ),
        contract: Account(
            storage={
                0: 1,
                1: 1,
                2: 1,
                5: 0xEBAF50DEBF10E08302FE4280C32DF010463CA297,
                6: 0xEBAF50DEBF10E08302FE4280C32DF010463CA297,
            },
            code=bytes.fromhex(
                "604060006040600073669e33b1aa30351139b73c3942acde1b09e75bcd62055730f460005500"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
