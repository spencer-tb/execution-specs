"""
Ported from:
tests/static/state_tests/stMemExpandingEIP150Calls/CallGoesOOGOnSecondLevelWithMemExpandingCallsFiller.json
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
    ["tests/static/state_tests/stMemExpandingEIP150Calls/CallGoesOOGOnSecondLevelWithMemExpandingCallsFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_call_goes_oog_on_second_level_with_mem_expanding_calls(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x823066fb511f07f5e49cbd8ca9874e4bc6ee9e65")
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

    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.SSTORE(key=0x8, value=Op.GAS)
        + Op.POP(Op.CREATE(value=0x0, offset=0x0, size=0x0))
        + Op.POP(Op.CREATE(value=0x0, offset=0x0, size=0x0))
        + Op.SSTORE(key=0x9, value=Op.GAS) + Op.SSTORE(key=0xa, value=Op.GAS)
    ),
    )
    pre[sender] = Account(balance=0xe8d4a51000, nonce=0)
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.SSTORE(key=0x8, value=Op.GAS)
        + Op.SSTORE(key=0x9, value=Op.CALL(gas=0x927c0, address=0x2ef686162bebf2542147767d5be471976860cceb, value=0x0, args_offset=0xff, args_size=0xff, ret_offset=0xff, ret_size=0xff))
    ),
    )
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.SSTORE(key=0x8, value=Op.GAS)
        + Op.SSTORE(key=0x9, value=Op.CALL(gas=0x927c0, address=0xa27e20572430916b3d6772b27329cc460224904d, value=0x0, args_offset=0xff, args_size=0xff, ret_offset=0xff, ret_size=0xff))
    ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0x8d19f2b0d2f5689c1771fbca70476ca6e877a81ee15c3733de87fae38e5abcef"
        ),
        to=contract,
        data=b"",
        gas_limit=220000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        callee: Account(
            code=Op.SSTORE(key=0x8, value=Op.GAS) + Op.POP(Op.CREATE(value=0x0, offset=0x0, size=0x0)) + Op.POP(Op.CREATE(value=0x0, offset=0x0, size=0x0)) + Op.SSTORE(key=0x9, value=Op.GAS) + Op.SSTORE(key=0xa, value=Op.GAS),
        ),
        callee_1: Account(
            code=Op.SSTORE(key=0x8, value=Op.GAS) + Op.SSTORE(key=0x9, value=Op.CALL(gas=0x927c0, address=0x2ef686162bebf2542147767d5be471976860cceb, value=0x0, args_offset=0xff, args_size=0xff, ret_offset=0xff, ret_size=0xff)),
        ),
        contract: Account(
            storage={8: 0x30956},
            code=Op.SSTORE(key=0x8, value=Op.GAS) + Op.SSTORE(key=0x9, value=Op.CALL(gas=0x927c0, address=0xa27e20572430916b3d6772b27329cc460224904d, value=0x0, args_offset=0xff, args_size=0xff, ret_offset=0xff, ret_size=0xff)),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
