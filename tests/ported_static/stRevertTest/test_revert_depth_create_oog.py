"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRevertTest/RevertDepthCreateOOGFiller.json
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
    ["tests/static/state_tests/stRevertTest/RevertDepthCreateOOGFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, tx_gas_limit, tx_value, expected_post",
    [
        (
            "000000000000000000000000000000000000000000000000000000000000ea60",
            110000,
            1,
            {
                Address("0xa000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x0, value=0x1)
                    + Op.SSTORE(
                        key=0x1,
                        value=Op.CALL(
                            gas=Op.CALLDATALOAD(offset=0x0),
                            address=0xB000000000000000000000000000000000000000,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(key=0x4, value=0xC)
                    + Op.STOP
                ),
                Address("0xb000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x2, value=0x8)
                    + Op.POP(Op.CREATE(value=0x0, offset=0x0, size=0x0))
                    + Op.SSTORE(key=0x3, value=0xC)
                    + Op.STOP
                ),
            },
        ),
        (
            "000000000000000000000000000000000000000000000000000000000000ea60",
            110000,
            0,
            {
                Address("0xa000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x0, value=0x1)
                    + Op.SSTORE(
                        key=0x1,
                        value=Op.CALL(
                            gas=Op.CALLDATALOAD(offset=0x0),
                            address=0xB000000000000000000000000000000000000000,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(key=0x4, value=0xC)
                    + Op.STOP
                ),
                Address("0xb000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x2, value=0x8)
                    + Op.POP(Op.CREATE(value=0x0, offset=0x0, size=0x0))
                    + Op.SSTORE(key=0x3, value=0xC)
                    + Op.STOP
                ),
            },
        ),
        (
            "000000000000000000000000000000000000000000000000000000000000ea60",
            180000,
            1,
            {
                Address("0xa000000000000000000000000000000000000000"): Account(
                    storage={0: 1, 4: 12},
                    code=Op.SSTORE(key=0x0, value=0x1)
                    + Op.SSTORE(
                        key=0x1,
                        value=Op.CALL(
                            gas=Op.CALLDATALOAD(offset=0x0),
                            address=0xB000000000000000000000000000000000000000,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(key=0x4, value=0xC)
                    + Op.STOP,
                ),
                Address("0xb000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x2, value=0x8)
                    + Op.POP(Op.CREATE(value=0x0, offset=0x0, size=0x0))
                    + Op.SSTORE(key=0x3, value=0xC)
                    + Op.STOP
                ),
            },
        ),
        (
            "000000000000000000000000000000000000000000000000000000000000ea60",
            180000,
            0,
            {
                Address("0xa000000000000000000000000000000000000000"): Account(
                    storage={0: 1, 4: 12},
                    code=Op.SSTORE(key=0x0, value=0x1)
                    + Op.SSTORE(
                        key=0x1,
                        value=Op.CALL(
                            gas=Op.CALLDATALOAD(offset=0x0),
                            address=0xB000000000000000000000000000000000000000,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(key=0x4, value=0xC)
                    + Op.STOP,
                ),
                Address("0xb000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x2, value=0x8)
                    + Op.POP(Op.CREATE(value=0x0, offset=0x0, size=0x0))
                    + Op.SSTORE(key=0x3, value=0xC)
                    + Op.STOP
                ),
            },
        ),
        (
            "000000000000000000000000000000000000000000000000000000000001ea60",
            110000,
            1,
            {
                Address("0xa000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x0, value=0x1)
                    + Op.SSTORE(
                        key=0x1,
                        value=Op.CALL(
                            gas=Op.CALLDATALOAD(offset=0x0),
                            address=0xB000000000000000000000000000000000000000,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(key=0x4, value=0xC)
                    + Op.STOP
                ),
                Address("0xb000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x2, value=0x8)
                    + Op.POP(Op.CREATE(value=0x0, offset=0x0, size=0x0))
                    + Op.SSTORE(key=0x3, value=0xC)
                    + Op.STOP
                ),
            },
        ),
        (
            "000000000000000000000000000000000000000000000000000000000001ea60",
            110000,
            0,
            {
                Address("0xa000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x0, value=0x1)
                    + Op.SSTORE(
                        key=0x1,
                        value=Op.CALL(
                            gas=Op.CALLDATALOAD(offset=0x0),
                            address=0xB000000000000000000000000000000000000000,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(key=0x4, value=0xC)
                    + Op.STOP
                ),
                Address("0xb000000000000000000000000000000000000000"): Account(
                    code=Op.SSTORE(key=0x2, value=0x8)
                    + Op.POP(Op.CREATE(value=0x0, offset=0x0, size=0x0))
                    + Op.SSTORE(key=0x3, value=0xC)
                    + Op.STOP
                ),
            },
        ),
        (
            "000000000000000000000000000000000000000000000000000000000001ea60",
            180000,
            1,
            {
                Address("0xa000000000000000000000000000000000000000"): Account(
                    storage={0: 1, 1: 1, 4: 12},
                    code=Op.SSTORE(key=0x0, value=0x1)
                    + Op.SSTORE(
                        key=0x1,
                        value=Op.CALL(
                            gas=Op.CALLDATALOAD(offset=0x0),
                            address=0xB000000000000000000000000000000000000000,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(key=0x4, value=0xC)
                    + Op.STOP,
                ),
                Address("0xb000000000000000000000000000000000000000"): Account(
                    storage={2: 8, 3: 12},
                    code=Op.SSTORE(key=0x2, value=0x8)
                    + Op.POP(Op.CREATE(value=0x0, offset=0x0, size=0x0))
                    + Op.SSTORE(key=0x3, value=0xC)
                    + Op.STOP,
                ),
            },
        ),
        (
            "000000000000000000000000000000000000000000000000000000000001ea60",
            180000,
            0,
            {
                Address("0xa000000000000000000000000000000000000000"): Account(
                    storage={0: 1, 1: 1, 4: 12},
                    code=Op.SSTORE(key=0x0, value=0x1)
                    + Op.SSTORE(
                        key=0x1,
                        value=Op.CALL(
                            gas=Op.CALLDATALOAD(offset=0x0),
                            address=0xB000000000000000000000000000000000000000,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(key=0x4, value=0xC)
                    + Op.STOP,
                ),
                Address("0xb000000000000000000000000000000000000000"): Account(
                    storage={2: 8, 3: 12},
                    code=Op.SSTORE(key=0x2, value=0x8)
                    + Op.POP(Op.CREATE(value=0x0, offset=0x0, size=0x0))
                    + Op.SSTORE(key=0x3, value=0xC)
                    + Op.STOP,
                ),
            },
        ),
    ],
    ids=[
        "case0",
        "case1",
        "case2",
        "case3",
        "case4",
        "case5",
        "case6",
        "case7",
    ],
)
@pytest.mark.pre_alloc_mutable
def test_revert_depth_create_oog(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    tx_gas_limit: int,
    tx_value: int,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xa000000000000000000000000000000000000000")
    callee = Address("0xb000000000000000000000000000000000000000")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[contract] = Account(
        balance=5,
        nonce=54,
        code=(
            Op.SSTORE(key=0x0, value=0x1)
            + Op.SSTORE(
                key=0x1,
                value=Op.CALL(
                    gas=Op.CALLDATALOAD(offset=0x0),
                    address=0xB000000000000000000000000000000000000000,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.SSTORE(key=0x4, value=0xC)
            + Op.STOP
        ),
    )
    pre[sender] = Account(balance=0xE8D4A51000, nonce=0)
    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(key=0x2, value=0x8)
            + Op.POP(Op.CREATE(value=0x0, offset=0x0, size=0x0))
            + Op.SSTORE(key=0x3, value=0xC)
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
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=tx_value,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
