"""
Ported from:
tests/static/state_tests/stZeroCallsRevert/ZeroValue_SUICIDE_ToNonZeroBalance_OOGRevertFiller.json
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
    ["tests/static/state_tests/stZeroCallsRevert/ZeroValue_SUICIDE_ToNonZeroBalance_OOGRevertFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_zero_value_suicide_to_non_zero_balance_oog_revert(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xfaa10b404ab607779993c016cd5da73ae1f29d7e")
    contract = Address("0xa2e25f47a24c66cfef22d3304777a22d6dd7ad4a")
    callee = Address("0x888748026558f849c1b2433ea5e1daf1444dfc60")
    callee_1 = Address("0x9089da66e8bbc08846842a301905501bc8525dc4")

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
        code=Op.SELFDESTRUCT(address=0x9089da66e8bbc08846842a301905501bc8525dc4) + Op.STOP,
    )
    pre[callee_1] = Account(balance=100, nonce=0)
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.POP(Op.CALL(gas=0xc350, address=0x888748026558f849c1b2433ea5e1daf1444dfc60, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.SSTORE(key=0x2, value=0xc) + Op.SSTORE(key=0x3, value=0xc)
        + Op.SSTORE(key=0x4, value=0xc) + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0xe8d4a51000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x4f31b3206fbf0e0e598b9b1a7d8ac86302a0ff1d8930738f1bebae9b67173e52"
        ),
        to=contract,
        data=b"",
        gas_limit=75000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        callee: Account(
            code=Op.SELFDESTRUCT(address=0x9089da66e8bbc08846842a301905501bc8525dc4) + Op.STOP,
        ),
        contract: Account(
            code=Op.POP(Op.CALL(gas=0xc350, address=0x888748026558f849c1b2433ea5e1daf1444dfc60, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x2, value=0xc) + Op.SSTORE(key=0x3, value=0xc) + Op.SSTORE(key=0x4, value=0xc) + Op.STOP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
