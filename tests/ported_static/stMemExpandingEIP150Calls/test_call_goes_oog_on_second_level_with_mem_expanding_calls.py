"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stMemExpandingEIP150Calls
CallGoesOOGOnSecondLevelWithMemExpandingCallsFiller.json
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
        "tests/static/state_tests/stMemExpandingEIP150Calls/CallGoesOOGOnSecondLevelWithMemExpandingCallsFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_call_goes_oog_on_second_level_with_mem_expanding_calls(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = EOA(
        key=0x8D19F2B0D2F5689C1771FBCA70476CA6E877A81EE15C3733DE87FAE38E5ABCEF
    )
    contract = Address("0xaf229807016a538dfcdab92a53337de38178d40f")
    callee = Address("0x2ef686162bebf2542147767d5be471976860cceb")
    callee_1 = Address("0xa27e20572430916b3d6772b27329cc460224904d")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    # Source: raw bytecode
    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(key=0x8, value=Op.GAS)
            + Op.POP(Op.CREATE(value=0x0, offset=0x0, size=0x0))
            + Op.POP(Op.CREATE(value=0x0, offset=0x0, size=0x0))
            + Op.SSTORE(key=0x9, value=Op.GAS)
            + Op.SSTORE(key=0xA, value=Op.GAS)
        ),
    )
    pre[sender] = Account(balance=0xE8D4A51000, nonce=0)
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(key=0x8, value=Op.GAS)
            + Op.SSTORE(
                key=0x9,
                value=Op.CALL(
                    gas=0x927C0,
                    address=0x2EF686162BEBF2542147767D5BE471976860CCEB,
                    value=0x0,
                    args_offset=0xFF,
                    args_size=0xFF,
                    ret_offset=0xFF,
                    ret_size=0xFF,
                ),
            )
        ),
    )
    # Source: raw bytecode
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(key=0x8, value=Op.GAS)
            + Op.SSTORE(
                key=0x9,
                value=Op.CALL(
                    gas=0x927C0,
                    address=0xA27E20572430916B3D6772B27329CC460224904D,
                    value=0x0,
                    args_offset=0xFF,
                    args_size=0xFF,
                    ret_offset=0xFF,
                    ret_size=0xFF,
                ),
            )
        ),
    )

    tx = Transaction(
        sender=sender,
        to=contract,
        data=b"",
        gas_limit=220000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        callee: Account(
            code=(
                Op.SSTORE(key=0x8, value=Op.GAS)
                + Op.POP(Op.CREATE(value=0x0, offset=0x0, size=0x0))
                + Op.POP(Op.CREATE(value=0x0, offset=0x0, size=0x0))
                + Op.SSTORE(key=0x9, value=Op.GAS)
                + Op.SSTORE(key=0xA, value=Op.GAS)
            ),
        ),
        callee_1: Account(
            code=(
                Op.SSTORE(key=0x8, value=Op.GAS)
                + Op.SSTORE(
                    key=0x9,
                    value=Op.CALL(
                        gas=0x927C0,
                        address=0x2EF686162BEBF2542147767D5BE471976860CCEB,
                        value=0x0,
                        args_offset=0xFF,
                        args_size=0xFF,
                        ret_offset=0xFF,
                        ret_size=0xFF,
                    ),
                )
            ),
        ),
        contract: Account(
            storage={8: 0x30956},
            code=(
                Op.SSTORE(key=0x8, value=Op.GAS)
                + Op.SSTORE(
                    key=0x9,
                    value=Op.CALL(
                        gas=0x927C0,
                        address=0xA27E20572430916B3D6772B27329CC460224904D,
                        value=0x0,
                        args_offset=0xFF,
                        args_size=0xFF,
                        ret_offset=0xFF,
                        ret_size=0xFF,
                    ),
                )
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
