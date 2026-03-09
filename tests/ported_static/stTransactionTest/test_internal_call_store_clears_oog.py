"""
Ported from:
tests/static/state_tests/stTransactionTest/InternalCallStoreClearsOOGFiller.json
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
    ["tests/static/state_tests/stTransactionTest/InternalCallStoreClearsOOGFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_internal_call_store_clears_oog(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    sender = Address("0xc4a2ca1058df329e5da4755f9921ddaf05cbaa06")
    contract = Address("0x30bfe899ef735d5aaca102952664a74b1de046af")
    callee = Address("0xd61e0564fab2b0da5136f75db579b663bd9f2bd8")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    pre[contract] = Account(
        balance=10,
        nonce=0,
        code=(
        Op.CALL(gas=0x9c40, address=0xd61e0564fab2b0da5136f75db579b663bd9f2bd8, value=0x1, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)
        + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0x3b9aca00, nonce=0)
    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.SSTORE(key=0x0, value=0x0) + Op.SSTORE(key=0x1, value=0x0)
        + Op.SSTORE(key=0x2, value=0x0) + Op.SSTORE(key=0x3, value=0x0)
        + Op.SSTORE(key=0x4, value=0x0) + Op.SSTORE(key=0x5, value=0x0)
        + Op.SSTORE(key=0x6, value=0x0) + Op.SSTORE(key=0x7, value=0x0)
        + Op.SSTORE(key=0x8, value=0x0) + Op.SSTORE(key=0x9, value=0x0) + Op.STOP
    ),
        storage={0x0: 0xc, 0x1: 0xc, 0x2: 0xc, 0x3: 0xc, 0x4: 0xc, 0x5: 0xc, 0x6: 0xc, 0x7: 0xc, 0x8: 0xc, 0x9: 0xc},
    )

    tx = Transaction(
        secret_key=Hash(
            "0xf79127a3004abde26a4cbd80c428cb10f829fa11b54d36e7b326f4f4a5927acf"
        ),
        to=contract,
        data=b"",
        gas_limit=160000,
        gas_price=10,
        nonce=0,
        value=10,
    )

    post = {
        contract: Account(
            code=Op.CALL(gas=0x9c40, address=0xd61e0564fab2b0da5136f75db579b663bd9f2bd8, value=0x1, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0) + Op.STOP,
        ),
        callee: Account(
            storage={0: 12, 1: 12, 2: 12, 3: 12, 4: 12, 5: 12, 6: 12, 7: 12, 8: 12, 9: 12},
            code=Op.SSTORE(key=0x0, value=0x0) + Op.SSTORE(key=0x1, value=0x0) + Op.SSTORE(key=0x2, value=0x0) + Op.SSTORE(key=0x3, value=0x0) + Op.SSTORE(key=0x4, value=0x0) + Op.SSTORE(key=0x5, value=0x0) + Op.SSTORE(key=0x6, value=0x0) + Op.SSTORE(key=0x7, value=0x0) + Op.SSTORE(key=0x8, value=0x0) + Op.SSTORE(key=0x9, value=0x0) + Op.STOP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
