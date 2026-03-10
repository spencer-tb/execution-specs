"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stPreCompiledContracts2/CALLCODEEcrecover1Filler.json
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
        "tests/static/state_tests/stPreCompiledContracts2/CALLCODEEcrecover1Filler.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_callcode_ecrecover1(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0xc305c830833ccb72817f7b8b8d9c6d5645fc9e5f")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[contract] = Account(
        balance=0x1312D00,
        nonce=0,
        code=(
            Op.MSTORE(
                offset=0x0,
                value=0x18C547E4F7B0F325AD1E56F57E26C745B09A3E503D86E00E5255FF7F715D3D1C,  # noqa: E501
            )
            + Op.MSTORE(offset=0x20, value=0x1)
            + Op.MSTORE(
                offset=0x40,
                value=0x73B1693892219D736CABA55BDB67216E485557EA6B6AF75F37096C9AA6A5A75F,  # noqa: E501
            )
            + Op.MSTORE(
                offset=0x60,
                value=0xEEB940B1D03B21E36B0E47E79769F095FE2AB855BD91E3A38756B7D75A9C4549,  # noqa: E501
            )
            + Op.SSTORE(
                key=0x2,
                value=Op.CALLCODE(
                    gas=0x186A0,
                    address=0x1,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x80,
                    ret_offset=0x80,
                    ret_size=0x20,
                ),
            )
            + Op.SSTORE(
                key=0x0,
                value=Op.MOD(Op.MLOAD(offset=0x80), Op.EXP(0x2, 0xA0)),
            )
            + Op.SSTORE(key=0x1, value=Op.EQ(Op.ORIGIN, Op.SLOAD(key=0x0)))
            + Op.STOP
        ),
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xe04d1ac7ddda0c98397d56a0b501e960d4cd325a39286919ac23c1a07009a869"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=365224,
        gas_price=10,
        nonce=0,
        value=100000,
    )

    post = {
        contract: Account(
            storage={2: 1},
            code=(
                Op.MSTORE(
                    offset=0x0,
                    value=0x18C547E4F7B0F325AD1E56F57E26C745B09A3E503D86E00E5255FF7F715D3D1C,  # noqa: E501
                )
                + Op.MSTORE(offset=0x20, value=0x1)
                + Op.MSTORE(
                    offset=0x40,
                    value=0x73B1693892219D736CABA55BDB67216E485557EA6B6AF75F37096C9AA6A5A75F,  # noqa: E501
                )
                + Op.MSTORE(
                    offset=0x60,
                    value=0xEEB940B1D03B21E36B0E47E79769F095FE2AB855BD91E3A38756B7D75A9C4549,  # noqa: E501
                )
                + Op.SSTORE(
                    key=0x2,
                    value=Op.CALLCODE(
                        gas=0x186A0,
                        address=0x1,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x80,
                        ret_offset=0x80,
                        ret_size=0x20,
                    ),
                )
                + Op.SSTORE(
                    key=0x0,
                    value=Op.MOD(Op.MLOAD(offset=0x80), Op.EXP(0x2, 0xA0)),
                )
                + Op.SSTORE(key=0x1, value=Op.EQ(Op.ORIGIN, Op.SLOAD(key=0x0)))
                + Op.STOP
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
