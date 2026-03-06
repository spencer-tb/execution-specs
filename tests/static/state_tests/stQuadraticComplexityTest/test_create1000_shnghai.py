"""
Ported from:
tests/static/state_tests/stQuadraticComplexityTest/Create1000ShnghaiFiller.json

contract code:
    jumpdest
    push2 0x03e8
    push1 0x80
    mload
    lt
    iszero
    push1 0x22
    jumpi
    push1 0x0a
    push1 0x00
    push1 0x01
    create
    push1 0x00
    sstore
    push1 0x01
    push1 0x80
    mload
    add
    push1 0x80
    mstore
    ... (8 more instructions)
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
    ["tests/static/state_tests/stQuadraticComplexityTest/Create1000ShnghaiFiller.json"],
)
@pytest.mark.valid_from("Cancun")
@pytest.mark.valid_until("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit, expected_post",
    [
    pytest.param(
        150000,
        {Address("0x010d8b0816e30ff51ba07678c64b272cdeddb807"): Account.NONEXISTENT, Address("0x014830fe159f418212e5c39b4b2e2ddc7b295395"): Account.NONEXISTENT, Address("0x0c6a8f1bf692cb9e4f9d9c5a2785d58edfd42457"): Account.NONEXISTENT, Address("0x198d23bedd1a9fdbd4adb5760930f6877f5d142f"): Account.NONEXISTENT, Address("0x266c09580d28c1c576e5c6b9adc926be1fecffb1"): Account.NONEXISTENT, Address("0xbbbf5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(storage={0: 0, 1: 0}, nonce=0), Address("0xe5dc2e5b40069a91f688e56ea8d12149c5480b42"): Account.NONEXISTENT, Address("0xfdbd2625737df76e194c99994be160c5f8248dad"): Account.NONEXISTENT, Address("0xfff043abcbf2b0972c1dca19b2ba3cd682f10e90"): Account.NONEXISTENT},
        id="case0",
    ),
    pytest.param(
        250000000,
        {Address("0x010d8b0816e30ff51ba07678c64b272cdeddb807"): Account(storage={}, nonce=1, balance=1, code=b""), Address("0x014830fe159f418212e5c39b4b2e2ddc7b295395"): Account(storage={}, nonce=1, balance=1, code=b""), Address("0x0443d33cbefcfb9dedd1885b4c58b06cb1bb0c09"): Account(storage={}, nonce=1, balance=1, code=b""), Address("0x0c6a8f1bf692cb9e4f9d9c5a2785d58edfd42457"): Account(storage={}, nonce=1, balance=1, code=b""), Address("0x198d23bedd1a9fdbd4adb5760930f6877f5d142f"): Account(storage={}, nonce=1, balance=1, code=b""), Address("0x266c09580d28c1c576e5c6b9adc926be1fecffb1"): Account(storage={}, nonce=1, balance=1, code=b""), Address("0x38382e1ec7bf834f328feb3170293b1ae558aed0"): Account(storage={}, nonce=1, balance=1, code=b""), Address("0x49198360b42d89332f8cc121182e071493045c40"): Account(storage={}, nonce=1, balance=1, code=b""), Address("0x69eada7f1d77ff9bf9c789d44990f9141e39d71f"): Account(storage={}, nonce=1, balance=1, code=b""), Address("0x901cc1c13f30eb2fc6de17ba1867dcc8c1561d46"): Account(storage={}, nonce=1, balance=1, code=b""), Address("0xbbbf5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(storage={0: 0x7981fa24b134deb51d71d250d7b0d9e33c8c5457, 1: 1000}, nonce=1000, balance=0xffffffffffc21), Address("0xcb78de6453fe67ac38868ac60825f0288e509167"): Account(storage={}, nonce=1, balance=1, code=b""), Address("0xde8ae395bafe56c8968a2cec0567ec2562598189"): Account(storage={}, nonce=1, balance=1, code=b""), Address("0xe5dc2e5b40069a91f688e56ea8d12149c5480b42"): Account(storage={}, nonce=1, balance=1, code=b""), Address("0xfdbd2625737df76e194c99994be160c5f8248dad"): Account(storage={}, nonce=1, balance=1, code=b""), Address("0xfff043abcbf2b0972c1dca19b2ba3cd682f10e90"): Account(storage={}, nonce=1, balance=1, code=b"")},
        id="case1",
    ),
    ],
)
@pytest.mark.pre_alloc_mutable
def test_create1000_shnghai(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xbbbf5374fce5edbc8e2a8697c15331677e6ebf0b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=8600000000,
    )

    pre[sender] = Account(balance=0xffffffffffffffffffffffffffffffff, nonce=0)
    pre[contract] = Account(
        balance=0xfffffffffffff,
        nonce=0,
        code=(
        Op.JUMPDEST + Op.PUSH2[0x3e8] + Op.PUSH1[0x80] + Op.MLOAD + Op.LT
        + Op.ISZERO + Op.PUSH1[0x22] + Op.JUMPI + Op.PUSH1[0xa] + Op.PUSH1[0x0]
        + Op.PUSH1[0x1] + Op.CREATE + Op.PUSH1[0x0] + Op.SSTORE + Op.PUSH1[0x1]
        + Op.PUSH1[0x80] + Op.MLOAD + Op.ADD + Op.PUSH1[0x80] + Op.MSTORE
        + Op.PUSH1[0x0] + Op.JUMP + Op.JUMPDEST + Op.PUSH1[0x80] + Op.MLOAD
        + Op.PUSH1[0x1] + Op.SSTORE + Op.STOP
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
        value=10,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
