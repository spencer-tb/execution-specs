"""
check output memory after callcode.

Ported from:
tests/static/state_tests/stCallCreateCallCodeTest/callcodeOutput2Filler.json
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
        "tests/static/state_tests/stCallCreateCallCodeTest/callcodeOutput2Filler.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_callcode_output2(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Check output memory after callcode."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x2e3d0156d2b99a6eacba540c55f423c8f5a33143")
    contract = Address("0xe6470a86a9862d2ce7db006ee9c99092cd5e71bb")
    callee = Address("0xbcc1197ccd23a97607f2f96d031f3432e0d16a02")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)
    pre[callee] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=Op.SSTORE(key=0x0, value=Op.ADD(0x1, 0x1)),
    )
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.MSTORE(
                offset=0x0,
                value=0x5E20A0453CECD065EA59C37AC63E079EE08998B6045136A8CE6635C7912EC0B6,  # noqa: E501
            )
            + Op.POP(
                Op.CALLCODE(
                    gas=0xC350,
                    address=0xBCC1197CCD23A97607F2F96D031F3432E0D16A02,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x20,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
            + Op.STOP
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xb1f4cbc3a50042184425a6f9e996d0910f7ba879457ce5dac5c71e498ad3c005"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=1000000,
        gas_price=10,
        nonce=0,
        value=100000,
    )

    post = {
        callee: Account(code=Op.SSTORE(key=0x0, value=Op.ADD(0x1, 0x1))),
        contract: Account(
            storage={
                0: 0x5E20A0453CECD065EA59C37AC63E079EE08998B6045136A8CE6635C7912EC0B6,  # noqa: E501
            },
            code=(
                Op.MSTORE(
                    offset=0x0,
                    value=0x5E20A0453CECD065EA59C37AC63E079EE08998B6045136A8CE6635C7912EC0B6,  # noqa: E501
                )
                + Op.POP(
                    Op.CALLCODE(
                        gas=0xC350,
                        address=0xBCC1197CCD23A97607F2F96D031F3432E0D16A02,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x20,
                        ret_offset=0x0,
                        ret_size=0x0,
                    ),
                )
                + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                + Op.STOP
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
