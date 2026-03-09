"""
CreateMessageReverted for CREATE2

Ported from:
tests/static/state_tests/stCreate2/CreateMessageRevertedFiller.json
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
    ["tests/static/state_tests/stCreate2/CreateMessageRevertedFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit, expected_post",
    [
        (80000, {Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(code=Op.MSTORE(offset=0x0, value=0x600c600055600d600155) + Op.CREATE2(value=0x0, offset=0x16, size=0xa, salt=0x0) + Op.STOP)}),
        (150000, {Address("0x244fe9a7867edcc140245e775071fbfe6ebedbae"): Account(storage={0: 12, 1: 13}), Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(code=Op.MSTORE(offset=0x0, value=0x600c600055600d600155) + Op.CREATE2(value=0x0, offset=0x16, size=0xa, salt=0x0) + Op.STOP)}),
    ],
    ids=['case0', 'case1'],
)
@pytest.mark.pre_alloc_mutable
def test_create_message_reverted(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
    expected_post: dict,
) -> None:
    """CreateMessageReverted for CREATE2."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000000000,
    )

    pre[sender] = Account(balance=0x2dc6c0, nonce=0)
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.MSTORE(offset=0x0, value=0x600c600055600d600155)
        + Op.CREATE2(value=0x0, offset=0x16, size=0xa, salt=0x0) + Op.STOP
    ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=b"",
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=100,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
