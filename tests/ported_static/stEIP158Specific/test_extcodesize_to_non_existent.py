"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stEIP158Specific/EXTCODESIZE_toNonExistentFiller.json
"""

import pytest
from execution_testing import (
    Account,
    Address,
    Alloc,
    EOA,
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
        "tests/static/state_tests/stEIP158Specific/EXTCODESIZE_toNonExistentFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_extcodesize_to_non_existent(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = EOA(
        key=0x45A915E4D060149EB4365960E6A7A45F334393093061116B197E3240065FF2D8
    )
    contract = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[sender] = Account(balance=0xE8D4A51000, nonce=0)
    # Source: LLL
    # { [0](GAS) [[1]] (EXTCODESIZE 0xc94f5374fce5edbc8e2a8697c15331677e6ebf0b) [[100]] (SUB @0 (GAS)) }  # noqa: E501
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.MSTORE(offset=0x0, value=Op.GAS)
            + Op.SSTORE(
                key=0x1,
                value=Op.EXTCODESIZE(
                    address=0xC94F5374FCE5EDBC8E2A8697C15331677E6EBF0B,
                ),
            )
            + Op.SSTORE(key=0x64, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS))
            + Op.STOP
        ),
    )

    tx = Transaction(
        sender=sender,
        to=contract,
        data=b"",
        gas_limit=600000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            storage={100: 4817},
            code=(
                Op.MSTORE(offset=0x0, value=Op.GAS)
                + Op.SSTORE(
                    key=0x1,
                    value=Op.EXTCODESIZE(
                        address=0xC94F5374FCE5EDBC8E2A8697C15331677E6EBF0B,
                    ),
                )
                + Op.SSTORE(
                    key=0x64, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                )
                + Op.STOP
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
