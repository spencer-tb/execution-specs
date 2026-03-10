"""
Ori Pomerantz qbzzt1@gmail.com.

Ported from:
tests/static/state_tests/stEIP150singleCodeGasPrices/gasCostReturnFiller.yml
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
        "tests/static/state_tests/stEIP150singleCodeGasPrices/gasCostReturnFiller.yml",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_gas_cost_return(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Ori Pomerantz qbzzt1@gmail.com."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x56724d001b4f2a2888a81971a64aad37cd43f881")
    contract = Address("0x155665fb22995bb5b9dc1d8d9d57a00ac64dc1e0")
    callee = Address("0x35cd99e56b0f9ac243172a86bef4d042dfdbc166")
    callee_1 = Address("0xeb0e68b88a12fc84ad4a1eeb07b289638c4d9f3c")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000,
    )

    pre[contract] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=(
            Op.MSTORE(offset=0x0, value=0x60A7)
            + Op.MSTORE(offset=0x20, value=0x60A7)
            + Op.MSTORE(offset=0x40, value=0x60A7)
            + Op.MSTORE(offset=0x0, value=Op.GAS)
            + Op.POP(
                Op.CALL(
                    gas=0x10000,
                    address=0x1000,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.MSTORE(
                offset=0x20, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
            )
            + Op.MSTORE(offset=0x0, value=Op.GAS)
            + Op.POP(
                Op.CALL(
                    gas=0x10000,
                    address=0x2000,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.MSTORE(
                offset=0x40, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
            )
            + Op.SSTORE(
                key=0x0,
                value=Op.SUB(Op.MLOAD(offset=0x20), Op.MLOAD(offset=0x40)),
            )
            + Op.STOP
        ),
        storage={0x0: 0x60A7},
    )
    pre[callee] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=Op.RETURN(offset=0xFF, size=0x0),
    )
    pre[sender] = Account(balance=0xBA1A9CE0BA1A9CE, nonce=0)
    pre[callee_1] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=Op.PUSH1[0x0] + Op.PUSH1[0xFF] + Op.STOP,
    )

    tx = Transaction(
        secret_key=Hash(
            "0x40ac0fc28c27e961ee46ec43355a094de205856edbd4654cf2577c2608d4ec1e"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex("00"),
        gas_limit=16777216,
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = {
        contract: Account(
            code=(
                Op.MSTORE(offset=0x0, value=0x60A7)
                + Op.MSTORE(offset=0x20, value=0x60A7)
                + Op.MSTORE(offset=0x40, value=0x60A7)
                + Op.MSTORE(offset=0x0, value=Op.GAS)
                + Op.POP(
                    Op.CALL(
                        gas=0x10000,
                        address=0x1000,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    ),
                )
                + Op.MSTORE(
                    offset=0x20,
                    value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS),
                )
                + Op.MSTORE(offset=0x0, value=Op.GAS)
                + Op.POP(
                    Op.CALL(
                        gas=0x10000,
                        address=0x2000,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    ),
                )
                + Op.MSTORE(
                    offset=0x40,
                    value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS),
                )
                + Op.SSTORE(
                    key=0x0,
                    value=Op.SUB(Op.MLOAD(offset=0x20), Op.MLOAD(offset=0x40)),
                )
                + Op.STOP
            ),
        ),
        callee: Account(code=Op.RETURN(offset=0xFF, size=0x0)),
        callee_1: Account(code=Op.PUSH1[0x0] + Op.PUSH1[0xFF] + Op.STOP),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
