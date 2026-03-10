"""
Call RETURNDATASIZE and RETURNDATACOPY after CREATE2 deploy a contract....

Ported from:
tests/static/state_tests/stCreate2
Create2OOGafterInitCodeReturndata2Filler.json
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
        "tests/static/state_tests/stCreate2/Create2OOGafterInitCodeReturndata2Filler.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit, expected_post",
    [
        (
            54000,
            {
                Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(
                    storage={1: 2},
                    code=Op.MSTORE(
                        offset=0x0, value=0x6460016001556000526005601BF3
                    )
                    + Op.POP(
                        Op.CREATE2(value=0x0, offset=0x12, size=0xE, salt=0x0)
                    )
                    + Op.SSTORE(key=0x1, value=Op.RETURNDATASIZE)
                    + Op.RETURNDATACOPY(dest_offset=0x0, offset=0x0, size=0x0)
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                )
            },
        ),
        (
            95000,
            {
                Address("0x6878b140f875209c82ab4d5f083b55947299ef6b"): Account(
                    code=Op.SSTORE(key=0x1, value=0x1)
                ),
                Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(
                    storage={2: 0x6460016001556000526005601BF3},
                    code=Op.MSTORE(
                        offset=0x0, value=0x6460016001556000526005601BF3
                    )
                    + Op.POP(
                        Op.CREATE2(value=0x0, offset=0x12, size=0xE, salt=0x0)
                    )
                    + Op.SSTORE(key=0x1, value=Op.RETURNDATASIZE)
                    + Op.RETURNDATACOPY(dest_offset=0x0, offset=0x0, size=0x0)
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
            },
        ),
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_create2_oo_gafter_init_code_returndata2(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
    expected_post: dict,
) -> None:
    """Call RETURNDATASIZE and RETURNDATACOPY after CREATE2 deploy a..."""
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

    pre[sender] = Account(balance=0xE8D4A51000, nonce=0)
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.MSTORE(offset=0x0, value=0x6460016001556000526005601BF3)
            + Op.POP(Op.CREATE2(value=0x0, offset=0x12, size=0xE, salt=0x0))
            + Op.SSTORE(key=0x1, value=Op.RETURNDATASIZE)
            + Op.RETURNDATACOPY(dest_offset=0x0, offset=0x0, size=0x0)
            + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
            + Op.STOP
        ),
        storage={0x1: 0x2},
    )

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
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
