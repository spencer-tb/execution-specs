"""
Ori Pomerantz qbzzt1@gmail.com.

Ported from:
tests/static/state_tests/VMTests/vmIOandFlowOperations/msizeFiller.yml
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
    ["tests/static/state_tests/VMTests/vmIOandFlowOperations/msizeFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.valid_until("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000004",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.MSTORE(offset=0x0, value=0xFF)
                    + Op.SSTORE(key=0x0, value=Op.MSIZE)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.MSTORE(offset=0x0, value=0xFFFFFFFFFF)
                    + Op.SSTORE(key=0x0, value=Op.MSIZE)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.MSTORE(offset=0x0, value=0xFFFFFFFFFF)
                    + Op.MSTORE(offset=0x20, value=0xEEEE)
                    + Op.SSTORE(key=0x0, value=Op.MSIZE)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.MSTORE(offset=0x0, value=0xFFFFFFFFFF)
                    + Op.MSTORE(offset=0x5A, value=0xEEEE)
                    + Op.SSTORE(key=0x0, value=Op.MSIZE)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.MSTORE8(offset=0x1F, value=0x1)
                    + Op.SSTORE(key=0x0, value=Op.MSIZE)
                    + Op.MSTORE8(offset=0x20, value=0x1)
                    + Op.SSTORE(key=0x1, value=Op.MSIZE)
                    + Op.MSTORE8(offset=0x20, value=0x0)
                    + Op.SSTORE(key=0x2, value=Op.MSIZE)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.MSTORE8(offset=0xB00000, value=0x1)
                    + Op.SSTORE(key=0x0, value=Op.MSIZE)
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 32, 1: 64, 2: 64},
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP,
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000005",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.MSTORE(offset=0x0, value=0xFF)
                    + Op.SSTORE(key=0x0, value=Op.MSIZE)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.MSTORE(offset=0x0, value=0xFFFFFFFFFF)
                    + Op.SSTORE(key=0x0, value=Op.MSIZE)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.MSTORE(offset=0x0, value=0xFFFFFFFFFF)
                    + Op.MSTORE(offset=0x20, value=0xEEEE)
                    + Op.SSTORE(key=0x0, value=Op.MSIZE)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.MSTORE(offset=0x0, value=0xFFFFFFFFFF)
                    + Op.MSTORE(offset=0x5A, value=0xEEEE)
                    + Op.SSTORE(key=0x0, value=Op.MSIZE)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.MSTORE8(offset=0x1F, value=0x1)
                    + Op.SSTORE(key=0x0, value=Op.MSIZE)
                    + Op.MSTORE8(offset=0x20, value=0x1)
                    + Op.SSTORE(key=0x1, value=Op.MSIZE)
                    + Op.MSTORE8(offset=0x20, value=0x0)
                    + Op.SSTORE(key=0x2, value=Op.MSIZE)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.MSTORE8(offset=0xB00000, value=0x1)
                    + Op.SSTORE(key=0x0, value=Op.MSIZE)
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 0xB00020},
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP,
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000000",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.MSTORE(offset=0x0, value=0xFF)
                    + Op.SSTORE(key=0x0, value=Op.MSIZE)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.MSTORE(offset=0x0, value=0xFFFFFFFFFF)
                    + Op.SSTORE(key=0x0, value=Op.MSIZE)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.MSTORE(offset=0x0, value=0xFFFFFFFFFF)
                    + Op.MSTORE(offset=0x20, value=0xEEEE)
                    + Op.SSTORE(key=0x0, value=Op.MSIZE)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.MSTORE(offset=0x0, value=0xFFFFFFFFFF)
                    + Op.MSTORE(offset=0x5A, value=0xEEEE)
                    + Op.SSTORE(key=0x0, value=Op.MSIZE)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.MSTORE8(offset=0x1F, value=0x1)
                    + Op.SSTORE(key=0x0, value=Op.MSIZE)
                    + Op.MSTORE8(offset=0x20, value=0x1)
                    + Op.SSTORE(key=0x1, value=Op.MSIZE)
                    + Op.MSTORE8(offset=0x20, value=0x0)
                    + Op.SSTORE(key=0x2, value=Op.MSIZE)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.MSTORE8(offset=0xB00000, value=0x1)
                    + Op.SSTORE(key=0x0, value=Op.MSIZE)
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 32},
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP,
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000001",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.MSTORE(offset=0x0, value=0xFF)
                    + Op.SSTORE(key=0x0, value=Op.MSIZE)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.MSTORE(offset=0x0, value=0xFFFFFFFFFF)
                    + Op.SSTORE(key=0x0, value=Op.MSIZE)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.MSTORE(offset=0x0, value=0xFFFFFFFFFF)
                    + Op.MSTORE(offset=0x20, value=0xEEEE)
                    + Op.SSTORE(key=0x0, value=Op.MSIZE)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.MSTORE(offset=0x0, value=0xFFFFFFFFFF)
                    + Op.MSTORE(offset=0x5A, value=0xEEEE)
                    + Op.SSTORE(key=0x0, value=Op.MSIZE)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.MSTORE8(offset=0x1F, value=0x1)
                    + Op.SSTORE(key=0x0, value=Op.MSIZE)
                    + Op.MSTORE8(offset=0x20, value=0x1)
                    + Op.SSTORE(key=0x1, value=Op.MSIZE)
                    + Op.MSTORE8(offset=0x20, value=0x0)
                    + Op.SSTORE(key=0x2, value=Op.MSIZE)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.MSTORE8(offset=0xB00000, value=0x1)
                    + Op.SSTORE(key=0x0, value=Op.MSIZE)
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 32},
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP,
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000002",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.MSTORE(offset=0x0, value=0xFF)
                    + Op.SSTORE(key=0x0, value=Op.MSIZE)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.MSTORE(offset=0x0, value=0xFFFFFFFFFF)
                    + Op.SSTORE(key=0x0, value=Op.MSIZE)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.MSTORE(offset=0x0, value=0xFFFFFFFFFF)
                    + Op.MSTORE(offset=0x20, value=0xEEEE)
                    + Op.SSTORE(key=0x0, value=Op.MSIZE)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.MSTORE(offset=0x0, value=0xFFFFFFFFFF)
                    + Op.MSTORE(offset=0x5A, value=0xEEEE)
                    + Op.SSTORE(key=0x0, value=Op.MSIZE)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.MSTORE8(offset=0x1F, value=0x1)
                    + Op.SSTORE(key=0x0, value=Op.MSIZE)
                    + Op.MSTORE8(offset=0x20, value=0x1)
                    + Op.SSTORE(key=0x1, value=Op.MSIZE)
                    + Op.MSTORE8(offset=0x20, value=0x0)
                    + Op.SSTORE(key=0x2, value=Op.MSIZE)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.MSTORE8(offset=0xB00000, value=0x1)
                    + Op.SSTORE(key=0x0, value=Op.MSIZE)
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 64},
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP,
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000003",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=Op.MSTORE(offset=0x0, value=0xFF)
                    + Op.SSTORE(key=0x0, value=Op.MSIZE)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=Op.MSTORE(offset=0x0, value=0xFFFFFFFFFF)
                    + Op.SSTORE(key=0x0, value=Op.MSIZE)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=Op.MSTORE(offset=0x0, value=0xFFFFFFFFFF)
                    + Op.MSTORE(offset=0x20, value=0xEEEE)
                    + Op.SSTORE(key=0x0, value=Op.MSIZE)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=Op.MSTORE(offset=0x0, value=0xFFFFFFFFFF)
                    + Op.MSTORE(offset=0x5A, value=0xEEEE)
                    + Op.SSTORE(key=0x0, value=Op.MSIZE)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=Op.MSTORE8(offset=0x1F, value=0x1)
                    + Op.SSTORE(key=0x0, value=Op.MSIZE)
                    + Op.MSTORE8(offset=0x20, value=0x1)
                    + Op.SSTORE(key=0x1, value=Op.MSIZE)
                    + Op.MSTORE8(offset=0x20, value=0x0)
                    + Op.SSTORE(key=0x2, value=Op.MSIZE)
                    + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001005"): Account(
                    code=Op.MSTORE8(offset=0xB00000, value=0x1)
                    + Op.SSTORE(key=0x0, value=Op.MSIZE)
                    + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={0: 128},
                    code=Op.DELEGATECALL(
                        gas=Op.GAS,
                        address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP,
                ),
            },
        ),
    ],
    ids=["case0", "case1", "case2", "case3", "case4", "case5"],
)
@pytest.mark.pre_alloc_mutable
def test_msize(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Ori Pomerantz qbzzt1@gmail.com."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xcccccccccccccccccccccccccccccccccccccccc")
    callee = Address("0x0000000000000000000000000000000000001000")
    callee_1 = Address("0x0000000000000000000000000000000000001001")
    callee_2 = Address("0x0000000000000000000000000000000000001002")
    callee_3 = Address("0x0000000000000000000000000000000000001003")
    callee_4 = Address("0x0000000000000000000000000000000000001004")
    callee_5 = Address("0x0000000000000000000000000000000000001005")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=4294967296,
    )

    pre[callee] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.MSTORE(offset=0x0, value=0xFF)
            + Op.SSTORE(key=0x0, value=Op.MSIZE)
            + Op.STOP
        ),
    )
    pre[callee_1] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.MSTORE(offset=0x0, value=0xFFFFFFFFFF)
            + Op.SSTORE(key=0x0, value=Op.MSIZE)
            + Op.STOP
        ),
    )
    pre[callee_2] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.MSTORE(offset=0x0, value=0xFFFFFFFFFF)
            + Op.MSTORE(offset=0x20, value=0xEEEE)
            + Op.SSTORE(key=0x0, value=Op.MSIZE)
            + Op.STOP
        ),
    )
    pre[callee_3] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.MSTORE(offset=0x0, value=0xFFFFFFFFFF)
            + Op.MSTORE(offset=0x5A, value=0xEEEE)
            + Op.SSTORE(key=0x0, value=Op.MSIZE)
            + Op.STOP
        ),
    )
    pre[callee_4] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.MSTORE8(offset=0x1F, value=0x1)
            + Op.SSTORE(key=0x0, value=Op.MSIZE)
            + Op.MSTORE8(offset=0x20, value=0x1)
            + Op.SSTORE(key=0x1, value=Op.MSIZE)
            + Op.MSTORE8(offset=0x20, value=0x0)
            + Op.SSTORE(key=0x2, value=Op.MSIZE)
            + Op.STOP
        ),
    )
    pre[callee_5] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.MSTORE8(offset=0xB00000, value=0x1)
            + Op.SSTORE(key=0x0, value=Op.MSIZE)
            + Op.STOP
        ),
    )
    pre[sender] = Account(balance=0x100000000000, nonce=0)
    pre[contract] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.DELEGATECALL(
                gas=Op.GAS,
                address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)),
                args_offset=0x0,
                args_size=0x0,
                ret_offset=0x0,
                ret_size=0x0,
            )
            + Op.STOP
        ),
    )

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=tx_data,
        gas_limit=268435456,
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
