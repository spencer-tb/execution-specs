"""
Call RETURNDATASIZE and RETURNDATACOPY after CREATE2 deploy a contract. correct returndata copy.

Ported from:
tests/static/state_tests/stCreate2/Create2OOGafterInitCodeReturndata2Filler.json

contract code:
    push14 0x6460016001556000526005601bf3
    push1 0x00
    mstore
    push1 0x00
    push1 0x0e
    push1 0x12
    push1 0x00
    create2
    pop
    returndatasize
    push1 0x01
    sstore
    push1 0x00
    push1 0x00
    push1 0x00
    returndatacopy
    push1 0x00
    mload
    push1 0x02
    sstore
    ... (1 more instructions)
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
    ["tests/static/state_tests/stCreate2/Create2OOGafterInitCodeReturndata2Filler.json"],
)
@pytest.mark.valid_from("Cancun")
@pytest.mark.parametrize(
    "tx_gas_limit, expected_post",
    [
    pytest.param(
        54000,
        {Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(storage={1: 2, 2: 0}), Address("0xf1ecf98489fa9ed60a664fc4998db699cfa39d40"): Account.NONEXISTENT},
        id="case0",
    ),
    pytest.param(
        95000,
        {Address("0x6878b140f875209c82ab4d5f083b55947299ef6b"): Account(code=Op.PUSH1[0x1] + Op.PUSH1[0x1] + Op.SSTORE), Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(storage={1: 0, 2: 0x6460016001556000526005601bf3})},
        id="case1",
    ),
    ],
)
@pytest.mark.pre_alloc_mutable
def test_create2_oo_gafter_init_code_returndata2(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
    expected_post: dict,
) -> None:
    """Call RETURNDATASIZE and RETURNDATACOPY after CREATE2 deploy a contract. correct returndata copy.."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[sender] = Account(balance=0xe8d4a51000, nonce=0)
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.PUSH14[0x6460016001556000526005601bf3] + Op.PUSH1[0x0] + Op.MSTORE
        + Op.PUSH1[0x0] + Op.PUSH1[0xe] + Op.PUSH1[0x12] + Op.PUSH1[0x0] + Op.CREATE2
        + Op.POP + Op.RETURNDATASIZE + Op.PUSH1[0x1] + Op.SSTORE + Op.PUSH1[0x0]
        + Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.RETURNDATACOPY + Op.PUSH1[0x0] + Op.MLOAD
        + Op.PUSH1[0x2] + Op.SSTORE + Op.STOP
    ),
        storage={0x1: 0x2},
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
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
