"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stSystemOperationsTest/ABAcalls1Filler.json
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
    ["tests/static/state_tests/stSystemOperationsTest/ABAcalls1Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.valid_until("Prague")
@pytest.mark.pre_alloc_mutable
def test_ab_acalls1(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0x572a88ed686beb6c9b71dc491ba1e120b327a85f")
    callee = Address("0x6236ea4ea8f3e5263acb65a97abe8683ab54d03a")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000000,
    )

    # Source: LLL
    # {  [[ (PC) ]] (CALL (- (GAS) 100000) <contract:0x945304eb96065b2a98b57a48a06ae28d285a71b5> 24 0 0 0 0) }  # noqa: E501
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.SSTORE(
                key=Op.PC,
                value=Op.CALL(
                    gas=Op.SUB(Op.GAS, 0x186A0),
                    address=0x6236EA4EA8F3E5263ACB65A97ABE8683AB54D03A,
                    value=0x18,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.STOP
        ),
    )
    pre[callee] = Account(
        balance=23,
        nonce=0,
        code=(
            Op.SSTORE(
                key=Op.PC,
                value=Op.ADD(
                    0x1,
                    Op.CALL(
                        gas=Op.SUB(Op.GAS, 0x186A0),
                        address=0x572A88ED686BEB6C9B71DC491BA1E120B327A85F,
                        value=0x17,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    ),
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
        gas_limit=1000000000,
        gas_price=10,
        nonce=0,
        value=100000,
    )

    post = {
        contract: Account(
            storage={38: 1},
            code=(
                Op.SSTORE(
                    key=Op.PC,
                    value=Op.CALL(
                        gas=Op.SUB(Op.GAS, 0x186A0),
                        address=0x6236EA4EA8F3E5263ACB65A97ABE8683AB54D03A,
                        value=0x18,
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
            storage={41: 2},
            code=(
                Op.SSTORE(
                    key=Op.PC,
                    value=Op.ADD(
                        0x1,
                        Op.CALL(
                            gas=Op.SUB(Op.GAS, 0x186A0),
                            address=0x572A88ED686BEB6C9B71DC491BA1E120B327A85F,
                            value=0x17,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    ),
                )
                + Op.STOP
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
