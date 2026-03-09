"""
call -> call -> callcode - > code, params check.

Ported from:
tests/static/state_tests/stCallCodes/callcallcallcode_001Filler.json
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
    ["tests/static/state_tests/stCallCodes/callcallcallcode_001Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_callcallcallcode_001(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Call -> call -> callcode - > code, params check."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0xeb09ff15547417853f6f4b240b8804769c37b0f1")
    callee = Address("0x0ffffaeb931552e5f094ca96a70be612da56b887")
    callee_1 = Address("0x7e63847aad8ca50fb7c04777dce6871a6bf8de0c")
    callee_2 = Address("0x9073671d2bfb351331716fd279282eacf50824ad")

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
            "60406000604060006003737e63847aad8ca50fb7c04777dce6871a6bf8de0c6203d090f2"  # noqa: E501
            "60025500"
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
            "60406000604060006002730ffffaeb931552e5f094ca96a70be612da56b887620493e0f1"  # noqa: E501
            "60015500"
        ),
    )
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "60406000604060006001739073671d2bfb351331716fd279282eacf50824ad62055730f1"  # noqa: E501
            "60005500"
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
                2: 1,
                3: 1,
                4: 0xFFFFAEB931552E5F094CA96A70BE612DA56B887,
                7: 3,
                330: 0xFFFFAEB931552E5F094CA96A70BE612DA56B887,
                332: 0xEBAF50DEBF10E08302FE4280C32DF010463CA297,
                336: 64,
                338: 39,
                340: 10,
            },
            code=bytes.fromhex(
                "60406000604060006003737e63847aad8ca50fb7c04777dce6871a6bf8de0c6203d090f260025500"  # noqa: E501
            ),
        ),
        callee_1: Account(
            code=bytes.fromhex(
                "600160035533600455346007553061014a553261014c55366101505538610152553a6101545500"  # noqa: E501
            ),
        ),
        callee_2: Account(
            storage={1: 1},
            code=bytes.fromhex(
                "60406000604060006002730ffffaeb931552e5f094ca96a70be612da56b887620493e0f160015500"  # noqa: E501
            ),
        ),
        contract: Account(
            storage={0: 1},
            code=bytes.fromhex(
                "60406000604060006001739073671d2bfb351331716fd279282eacf50824ad62055730f160005500"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
