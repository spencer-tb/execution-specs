"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stCallDelegateCodesCallCodeHomestead
callcallcodecall_010Filler.json
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
        "tests/static/state_tests/stCallDelegateCodesCallCodeHomestead/callcallcodecall_010Filler.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_callcallcodecall_010(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0xdb43306b16c521b9cc3667fbe7d1b697bb1f9605")
    callee = Address("0x8738ab5302009e8bad163c8a9e91e72926b09d34")
    callee_1 = Address("0xb8601b04bfd9eb63bc6ff0263567113d4cb874e4")
    callee_2 = Address("0xfed08e44ae95ece264bc94a1fc45af8bc4ef4f1d")

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
        code=(
            Op.SSTORE(
                key=0x2,
                value=Op.CALLCODE(
                    gas=0x3D090,
                    address=0xB8601B04BFD9EB63BC6FF0263567113D4CB874E4,
                    value=0x2,
                    args_offset=0x0,
                    args_size=0x40,
                    ret_offset=0x0,
                    ret_size=0x40,
                ),
            )
            + Op.SSTORE(key=0x5, value=Op.CALLER)
            + Op.STOP
        ),
    )
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(key=0x3, value=0x1)
            + Op.SSTORE(key=0x4, value=Op.CALLER)
            + Op.SSTORE(key=0x6, value=Op.CALLVALUE)
            + Op.SSTORE(key=0x14A, value=Op.ADDRESS)
            + Op.SSTORE(key=0x14C, value=Op.ORIGIN)
            + Op.SSTORE(key=0x150, value=Op.CALLDATASIZE)
            + Op.SSTORE(key=0x152, value=Op.CODESIZE)
            + Op.SSTORE(key=0x154, value=Op.GASPRICE)
            + Op.STOP
        ),
    )
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.SSTORE(
                key=0x0,
                value=Op.CALLCODE(
                    gas=0x55730,
                    address=0xFED08E44AE95ECE264BC94A1FC45AF8BC4EF4F1D,
                    value=0x1,
                    args_offset=0x0,
                    args_size=0x40,
                    ret_offset=0x0,
                    ret_size=0x40,
                ),
            )
            + Op.STOP
        ),
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)
    pre[callee_2] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.SSTORE(
                key=0x1,
                value=Op.DELEGATECALL(
                    gas=0x493E0,
                    address=0x8738AB5302009E8BAD163C8A9E91E72926B09D34,
                    args_offset=0x0,
                    args_size=0x40,
                    ret_offset=0x0,
                    ret_size=0x40,
                ),
            )
            + Op.STOP
        ),
    )

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
            code=(
                Op.SSTORE(
                    key=0x2,
                    value=Op.CALLCODE(
                        gas=0x3D090,
                        address=0xB8601B04BFD9EB63BC6FF0263567113D4CB874E4,
                        value=0x2,
                        args_offset=0x0,
                        args_size=0x40,
                        ret_offset=0x0,
                        ret_size=0x40,
                    ),
                )
                + Op.SSTORE(key=0x5, value=Op.CALLER)
                + Op.STOP
            ),
        ),
        callee_1: Account(
            code=(
                Op.SSTORE(key=0x3, value=0x1)
                + Op.SSTORE(key=0x4, value=Op.CALLER)
                + Op.SSTORE(key=0x6, value=Op.CALLVALUE)
                + Op.SSTORE(key=0x14A, value=Op.ADDRESS)
                + Op.SSTORE(key=0x14C, value=Op.ORIGIN)
                + Op.SSTORE(key=0x150, value=Op.CALLDATASIZE)
                + Op.SSTORE(key=0x152, value=Op.CODESIZE)
                + Op.SSTORE(key=0x154, value=Op.GASPRICE)
                + Op.STOP
            ),
        ),
        contract: Account(
            storage={
                0: 1,
                1: 1,
                2: 1,
                3: 1,
                4: 0xDB43306B16C521B9CC3667FBE7D1B697BB1F9605,
                5: 0xDB43306B16C521B9CC3667FBE7D1B697BB1F9605,
                6: 2,
                330: 0xDB43306B16C521B9CC3667FBE7D1B697BB1F9605,
                332: 0xEBAF50DEBF10E08302FE4280C32DF010463CA297,
                336: 64,
                338: 39,
                340: 10,
            },
            code=(
                Op.SSTORE(
                    key=0x0,
                    value=Op.CALLCODE(
                        gas=0x55730,
                        address=0xFED08E44AE95ECE264BC94A1FC45AF8BC4EF4F1D,
                        value=0x1,
                        args_offset=0x0,
                        args_size=0x40,
                        ret_offset=0x0,
                        ret_size=0x40,
                    ),
                )
                + Op.STOP
            ),
        ),
        callee_2: Account(
            code=(
                Op.SSTORE(
                    key=0x1,
                    value=Op.DELEGATECALL(
                        gas=0x493E0,
                        address=0x8738AB5302009E8BAD163C8A9E91E72926B09D34,
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
