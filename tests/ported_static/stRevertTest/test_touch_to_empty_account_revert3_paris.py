"""
Ported from:
tests/static/state_tests/stRevertTest/TouchToEmptyAccountRevert3_ParisFiller.json
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
    ["tests/static/state_tests/stRevertTest/TouchToEmptyAccountRevert3_ParisFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_touch_to_empty_account_revert3_paris(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xfaa10b404ab607779993c016cd5da73ae1f29d7e")
    contract = Address("0xcd48e0c45933cfa7aa1345807cf2d6b02875f627")
    callee = Address("0x2620916b2f3d6b185f4d9dd1ecee4a1f665d5c36")
    callee_1 = Address("0x28207e524ccb9dbc79bb3044819acd87d630f27a")
    callee_2 = Address("0x51cd6399de7e11930d3aa146d45a2e327b5894b9")
    callee_3 = Address("0x76fae819612a29489a1a43208613d8f8557b8898")

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
        Op.SSTORE(key=0x2, value=Op.CALL(gas=0x186a0, address=0x28207e524ccb9dbc79bb3044819acd87d630f27a, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.SHA3(offset=0x0, size=0x2fffff) + Op.STOP
    ),
    )
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=Op.SELFDESTRUCT(address=0x76fae819612a29489a1a43208613d8f8557b8898) + Op.STOP,
    )
    pre[callee_2] = Account(
        balance=0,
        nonce=0,
        code=Op.SELFDESTRUCT(address=0x76fae819612a29489a1a43208613d8f8557b8898) + Op.STOP,
    )
    pre[callee_3] = Account(balance=10, nonce=0)
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.SSTORE(key=0x0, value=Op.CALL(gas=0x1fbd0, address=0x51cd6399de7e11930d3aa146d45a2e327b5894b9, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.SSTORE(key=0x1, value=Op.CALL(gas=0x1fbd0, address=0x2620916b2f3d6b185f4d9dd1ecee4a1f665d5c36, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0xe8d4a51000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x4f31b3206fbf0e0e598b9b1a7d8ac86302a0ff1d8930738f1bebae9b67173e52"
        ),
        to=contract,
        data=b"",
        gas_limit=200000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        callee: Account(
            code=Op.SSTORE(key=0x2, value=Op.CALL(gas=0x186a0, address=0x28207e524ccb9dbc79bb3044819acd87d630f27a, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SHA3(offset=0x0, size=0x2fffff) + Op.STOP,
        ),
        callee_1: Account(
            code=Op.SELFDESTRUCT(address=0x76fae819612a29489a1a43208613d8f8557b8898) + Op.STOP,
        ),
        callee_2: Account(
            code=Op.SELFDESTRUCT(address=0x76fae819612a29489a1a43208613d8f8557b8898) + Op.STOP,
        ),
        contract: Account(
            storage={0: 1},
            code=Op.SSTORE(key=0x0, value=Op.CALL(gas=0x1fbd0, address=0x51cd6399de7e11930d3aa146d45a2e327b5894b9, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x1, value=Op.CALL(gas=0x1fbd0, address=0x2620916b2f3d6b185f4d9dd1ecee4a1f665d5c36, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.STOP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
