"""
Ported from:
tests/static/state_tests/stMemExpandingEIP150Calls/CallGoesOOGOnSecondLevel2WithMemExpandingCallsFiller.json
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
    ["tests/static/state_tests/stMemExpandingEIP150Calls/CallGoesOOGOnSecondLevel2WithMemExpandingCallsFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_call_goes_oog_on_second_level2_with_mem_expanding_calls(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xadc699577c950fccb53e02805bf25c44939cda20")
    contract = Address("0x0700bb425d7d4c412ac658014015bd6c98652dc4")
    callee = Address("0x96983de02bfbcb5d0f4e0ee98fdde6d6f0c75fe0")
    callee_1 = Address("0xc10a98222464b07008ceb5a0ec44ed49920addda")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000,
    )

    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.SSTORE(key=0x8, value=Op.GAS)
        + Op.SSTORE(key=0x9, value=Op.CALL(gas=0x927c0, address=0xc10a98222464b07008ceb5a0ec44ed49920addda, value=0x0, args_offset=0xff, args_size=0xff, ret_offset=0xff, ret_size=0xff))
    ),
    )
    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.SSTORE(key=0x8, value=Op.GAS) + Op.SSTORE(key=0x9, value=Op.GAS)
        + Op.SSTORE(key=0xa, value=Op.GAS)
    ),
    )
    pre[sender] = Account(balance=0xe8d4a510000, nonce=0)
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.SSTORE(key=0x8, value=Op.GAS)
        + Op.SSTORE(key=0x9, value=Op.CALL(gas=0x927c0, address=0x96983de02bfbcb5d0f4e0ee98fdde6d6f0c75fe0, value=0x0, args_offset=0xff, args_size=0xff, ret_offset=0xff, ret_size=0xff))
    ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0x0b51075bb33d347a23b516e327e1b71c54f63faa192d1d94b62c76e0c26cf98a"
        ),
        to=contract,
        data=b"",
        gas_limit=160000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            code=Op.SSTORE(key=0x8, value=Op.GAS) + Op.SSTORE(key=0x9, value=Op.CALL(gas=0x927c0, address=0xc10a98222464b07008ceb5a0ec44ed49920addda, value=0x0, args_offset=0xff, args_size=0xff, ret_offset=0xff, ret_size=0xff)),
        ),
        callee: Account(
            code=Op.SSTORE(key=0x8, value=Op.GAS) + Op.SSTORE(key=0x9, value=Op.GAS) + Op.SSTORE(key=0xa, value=Op.GAS),
        ),
        callee_1: Account(
            code=Op.SSTORE(key=0x8, value=Op.GAS) + Op.SSTORE(key=0x9, value=Op.CALL(gas=0x927c0, address=0x96983de02bfbcb5d0f4e0ee98fdde6d6f0c75fe0, value=0x0, args_offset=0xff, args_size=0xff, ret_offset=0xff, ret_size=0xff)),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
