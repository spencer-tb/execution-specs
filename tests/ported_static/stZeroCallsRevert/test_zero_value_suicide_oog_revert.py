"""
Ported from:
tests/static/state_tests/stZeroCallsRevert/ZeroValue_SUICIDE_OOGRevertFiller.json
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
    ["tests/static/state_tests/stZeroCallsRevert/ZeroValue_SUICIDE_OOGRevertFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_zero_value_suicide_oog_revert(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xfaa10b404ab607779993c016cd5da73ae1f29d7e")
    contract = Address("0x3f9709b08071257d9b49276abf1787b5bdccf0c4")
    callee = Address("0xda2eb5512889130c4af686a291b08665b889cb22")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.POP(Op.CALL(gas=0x9c40, address=0xda2eb5512889130c4af686a291b08665b889cb22, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.SSTORE(key=0x2, value=0xc) + Op.SSTORE(key=0x3, value=0xc)
        + Op.SSTORE(key=0x4, value=0xc) + Op.SSTORE(key=0x64, value=Op.GAS) + Op.STOP
    ),
    )
    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=Op.SELFDESTRUCT(address=0xda2eb5512889130c4af686a291b08665b889cb22) + Op.STOP,
    )
    pre[sender] = Account(balance=0xe8d4a51000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x4f31b3206fbf0e0e598b9b1a7d8ac86302a0ff1d8930738f1bebae9b67173e52"
        ),
        to=contract,
        data=b"",
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            code=Op.POP(Op.CALL(gas=0x9c40, address=0xda2eb5512889130c4af686a291b08665b889cb22, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x2, value=0xc) + Op.SSTORE(key=0x3, value=0xc) + Op.SSTORE(key=0x4, value=0xc) + Op.SSTORE(key=0x64, value=Op.GAS) + Op.STOP,
        ),
        callee: Account(
            code=Op.SELFDESTRUCT(address=0xda2eb5512889130c4af686a291b08665b889cb22) + Op.STOP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
