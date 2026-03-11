"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stSystemOperationsTest
callcodeToNameRegistratorZeroMemExpanionFiller.json
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
        "tests/static/state_tests/stSystemOperationsTest/callcodeToNameRegistratorZeroMemExpanionFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit, expected_post",
    [
        (
            50000,
            {
                Address("0x15eb18969e0925c8e4a76fd7cbce36a2b056b27e"): Account(
                    code=Op.JUMPI(
                        pc=0x9,
                        condition=Op.ISZERO(
                            Op.SLOAD(key=Op.CALLDATALOAD(offset=0x0))
                        ),
                    )
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(
                        key=Op.CALLDATALOAD(offset=0x0),
                        value=Op.CALLDATALOAD(offset=0x20),
                    )
                ),
                Address("0x82f454dea4d0958bced42315a0e580848b2c440c"): Account(
                    code=Op.MSTORE(
                        offset=0x0,
                        value=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                    )
                    + Op.MSTORE(
                        offset=0x20,
                        value=0xAAFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFAA,  # noqa: E501
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.CALLCODE(
                            gas=0x1388,
                            address=0x15EB18969E0925C8E4A76FD7CBCE36A2B056B27E,
                            value=0x17,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.STOP
                ),
            },
        ),
        (
            1000000,
            {
                Address("0x15eb18969e0925c8e4a76fd7cbce36a2b056b27e"): Account(
                    code=Op.JUMPI(
                        pc=0x9,
                        condition=Op.ISZERO(
                            Op.SLOAD(key=Op.CALLDATALOAD(offset=0x0))
                        ),
                    )
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.SSTORE(
                        key=Op.CALLDATALOAD(offset=0x0),
                        value=Op.CALLDATALOAD(offset=0x20),
                    )
                ),
                Address("0x82f454dea4d0958bced42315a0e580848b2c440c"): Account(
                    storage={0: 1},
                    code=Op.MSTORE(
                        offset=0x0,
                        value=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                    )
                    + Op.MSTORE(
                        offset=0x20,
                        value=0xAAFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFAA,  # noqa: E501
                    )
                    + Op.SSTORE(
                        key=0x0,
                        value=Op.CALLCODE(
                            gas=0x1388,
                            address=0x15EB18969E0925C8E4A76FD7CBCE36A2B056B27E,
                            value=0x17,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.STOP,
                ),
            },
        ),
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_callcode_to_name_registrator_zero_mem_expanion(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0x82f454dea4d0958bced42315a0e580848b2c440c")
    callee = Address("0x15eb18969e0925c8e4a76fd7cbce36a2b056b27e")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    # Source: raw bytecode
    pre[callee] = Account(
        balance=23,
        nonce=0,
        code=(
            Op.JUMPI(
                pc=0x9,
                condition=Op.ISZERO(Op.SLOAD(key=Op.CALLDATALOAD(offset=0x0))),
            )
            + Op.STOP
            + Op.JUMPDEST
            + Op.SSTORE(
                key=Op.CALLDATALOAD(offset=0x0),
                value=Op.CALLDATALOAD(offset=0x20),
            )
        ),
    )
    # Source: LLL
    # { (MSTORE 0 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) (MSTORE 32 0xaaffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffaa ) [[ 0 ]] (CALLCODE 5000 <contract:0x945304eb96065b2a98b57a48a06ae28d285a71b5> 23 0 0 0 0) }  # noqa: E501
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.MSTORE(
                offset=0x0,
                value=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
            )
            + Op.MSTORE(
                offset=0x20,
                value=0xAAFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFAA,  # noqa: E501
            )
            + Op.SSTORE(
                key=0x0,
                value=Op.CALLCODE(
                    gas=0x1388,
                    address=0x15EB18969E0925C8E4A76FD7CBCE36A2B056B27E,
                    value=0x17,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.STOP
        ),
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xe04d1ac7ddda0c98397d56a0b501e960d4cd325a39286919ac23c1a07009a869"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=100000,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
