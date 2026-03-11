"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stBugs/staticcall_createfailsFiller.json
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
    ["tests/static/state_tests/stBugs/staticcall_createfailsFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex",
    [
        "000000000000000000000000c94f5374fce5edbc8e2a8697c15331677e6ebf0b",
        "000000000000000000000000d94f5374fce5edbc8e2a8697c15331677e6ebf0b",
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_staticcall_createfails(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x1000000000000000000000000000000000000000")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    callee = Address("0xc94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    callee_1 = Address("0xd94f5374fce5edbc8e2a8697c15331677e6ebf0b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=23826461031063688,
    )

    pre[sender] = Account(balance=0x38BEEC8FEECA2598, nonce=0)
    # Source: LLL
    # { [[1]] (STATICCALL 70000 (CALLDATALOAD 0) 0 0 0 0) }
    pre[contract] = Account(
        balance=0,
        nonce=63,
        code=(
            Op.SSTORE(
                key=0x1,
                value=Op.STATICCALL(
                    gas=0x11170,
                    address=Op.CALLDATALOAD(offset=0x0),
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.STOP
        ),
        storage={0x1: 0x1},
    )
    # Source: LLL
    # { (MSTORE 1 1) [[2]] (CREATE 1 1 1) }
    pre[callee] = Account(
        balance=0,
        nonce=63,
        code=(
            Op.MSTORE(offset=0x1, value=0x1)
            + Op.SSTORE(
                key=0x2, value=Op.CREATE(value=0x1, offset=0x1, size=0x1)
            )
            + Op.STOP
        ),
    )
    # Source: raw bytecode
    pre[callee_1] = Account(
        balance=0,
        nonce=63,
        code=Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.CREATE,
    )

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=tx_data,
        gas_limit=120000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            code=(
                Op.SSTORE(
                    key=0x1,
                    value=Op.STATICCALL(
                        gas=0x11170,
                        address=Op.CALLDATALOAD(offset=0x0),
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    ),
                )
                + Op.STOP
            ),
        ),
        callee: Account(
            code=(
                Op.MSTORE(offset=0x1, value=0x1)
                + Op.SSTORE(
                    key=0x2,
                    value=Op.CREATE(value=0x1, offset=0x1, size=0x1),
                )
                + Op.STOP
            ),
        ),
        callee_1: Account(code=Op.PUSH1[0x0] + Op.PUSH1[0x0] + Op.CREATE),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
