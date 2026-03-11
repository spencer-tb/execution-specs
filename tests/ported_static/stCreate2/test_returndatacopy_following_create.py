"""
Check that create2 does not fill returndata buffer with its return opcode.

Ported from:
tests/static/state_tests/stCreate2/returndatacopy_following_createFiller.json
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
    [
        "tests/static/state_tests/stCreate2/returndatacopy_following_createFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex",
    [
        "0000000000000000000000000f572e5295c57f15886f9b263e2f6d2d6c7b5ec6",
        "0000000000000000000000001f572e5295c57f15886f9b263e2f6d2d6c7b5ec6",
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_returndatacopy_following_create(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
) -> None:
    """Check that create2 does not fill returndata buffer with its..."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x1aabbccdd5c57f15886f9b263e2f6d2d6c7b5ec6")
    callee = Address("0x0f572e5295c57f15886f9b263e2f6d2d6c7b5ec6")
    callee_1 = Address("0x1f572e5295c57f15886f9b263e2f6d2d6c7b5ec6")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=47244640256,
    )

    # Source: LLL
    # { (CREATE2 0 0 (lll (seq (MSTORE 0 0x0000111122223333444455556666777788889999aaaabbbbccccddddeeeeffff) (RETURN 0 32)) 0) 0) (RETURNDATACOPY 0 0 32) (SSTORE 0 (MLOAD 0)) }  # noqa: E501
    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.PUSH1[0x0]
            + Op.PUSH1[0x28]
            + Op.CODECOPY(dest_offset=0x0, offset=0x1F, size=Op.DUP1)
            + Op.PUSH1[0x0]
            + Op.PUSH1[0x0]
            + Op.POP(Op.CREATE2)
            + Op.RETURNDATACOPY(dest_offset=0x0, offset=0x0, size=0x20)
            + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
            + Op.STOP
            + Op.INVALID
            + Op.MSTORE(
                offset=0x0,
                value=0x111122223333444455556666777788889999AAAABBBBCCCCDDDDEEEEFFFF,  # noqa: E501
            )
            + Op.RETURN(offset=0x0, size=0x20)
            + Op.STOP
        ),
        storage={0x0: 0x1},
    )
    # Source: LLL
    # { (CALL (GAS) (CALLDATALOAD 0) 0 0 0 0 0) }
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.CALL(
                gas=Op.GAS,
                address=Op.CALLDATALOAD(offset=0x0),
                value=0x0,
                args_offset=0x0,
                args_size=0x0,
                ret_offset=0x0,
                ret_size=0x0,
            )
            + Op.STOP
        ),
    )
    # Source: LLL
    # { (seq (create2 0 0 (lll (STOP) 0) 0) (RETURNDATACOPY 0 0 32) (SSTORE 0 (MLOAD 0)) )}  # noqa: E501
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.PUSH1[0x0]
            + Op.PUSH1[0x2]
            + Op.CODECOPY(dest_offset=0x0, offset=0x1F, size=Op.DUP1)
            + Op.PUSH1[0x0]
            + Op.PUSH1[0x0]
            + Op.POP(Op.CREATE2)
            + Op.RETURNDATACOPY(dest_offset=0x0, offset=0x0, size=0x20)
            + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
            + Op.STOP
            + Op.INVALID
            + Op.STOP
            + Op.STOP
        ),
        storage={0x0: 0x1},
    )
    pre[sender] = Account(balance=0x6400000000, nonce=0)

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=tx_data,
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        callee: Account(
            storage={0: 1},
            code=(
                Op.PUSH1[0x0]
                + Op.PUSH1[0x28]
                + Op.CODECOPY(dest_offset=0x0, offset=0x1F, size=Op.DUP1)
                + Op.PUSH1[0x0]
                + Op.PUSH1[0x0]
                + Op.POP(Op.CREATE2)
                + Op.RETURNDATACOPY(dest_offset=0x0, offset=0x0, size=0x20)
                + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                + Op.STOP
                + Op.INVALID
                + Op.MSTORE(
                    offset=0x0,
                    value=0x111122223333444455556666777788889999AAAABBBBCCCCDDDDEEEEFFFF,  # noqa: E501
                )
                + Op.RETURN(offset=0x0, size=0x20)
                + Op.STOP
            ),
        ),
        contract: Account(
            code=(
                Op.CALL(
                    gas=Op.GAS,
                    address=Op.CALLDATALOAD(offset=0x0),
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                )
                + Op.STOP
            ),
        ),
        callee_1: Account(
            storage={0: 1},
            code=(
                Op.PUSH1[0x0]
                + Op.PUSH1[0x2]
                + Op.CODECOPY(dest_offset=0x0, offset=0x1F, size=Op.DUP1)
                + Op.PUSH1[0x0]
                + Op.PUSH1[0x0]
                + Op.POP(Op.CREATE2)
                + Op.RETURNDATACOPY(dest_offset=0x0, offset=0x0, size=0x20)
                + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
                + Op.STOP
                + Op.INVALID
                + Op.STOP
                + Op.STOP
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
