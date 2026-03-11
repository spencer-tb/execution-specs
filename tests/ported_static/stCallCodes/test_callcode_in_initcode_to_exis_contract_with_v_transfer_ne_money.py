"""
callcode inside create/create2 contract init to existing contract. callcode...

Ported from:
tests/static/state_tests/stCallCodes
callcodeInInitcodeToExisContractWithVTransferNEMoneyFiller.json
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
        "tests/static/state_tests/stCallCodes/callcodeInInitcodeToExisContractWithVTransferNEMoneyFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        (
            "0000000000000000000000001000000000000000000000000000000000000000",
            {
                Address("0x1000000000000000000000000000000000000000"): Account(
                    code=Op.PUSH1[0x28]
                    + Op.CODECOPY(dest_offset=0x0, offset=0xF, size=Op.DUP1)
                    + Op.PUSH1[0x0]
                    + Op.PUSH1[0x0]
                    + Op.CREATE
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(
                        key=0x1,
                        value=Op.CALLCODE(
                            gas=0x7A120,
                            address=0x1000000000000000000000000000000000000001,
                            value=0x1,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x1000000000000000000000000000000000000001"): Account(
                    code=Op.SSTORE(key=0x2, value=0x1) + Op.STOP
                ),
                Address("0x1100000000000000000000000000000000000000"): Account(
                    code=Op.CALL(
                        gas=0x493E0,
                        address=Op.CALLDATALOAD(offset=0x0),
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x2000000000000000000000000000000000000000"): Account(
                    code=Op.PUSH1[0x0]
                    + Op.PUSH1[0x28]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x11, size=Op.DUP1)
                    + Op.PUSH1[0x0]
                    + Op.PUSH1[0x0]
                    + Op.CREATE2
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(
                        key=0x1,
                        value=Op.CALLCODE(
                            gas=0x7A120,
                            address=0x1000000000000000000000000000000000000001,
                            value=0x1,
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
            "0000000000000000000000002000000000000000000000000000000000000000",
            {
                Address("0x1000000000000000000000000000000000000000"): Account(
                    code=Op.PUSH1[0x28]
                    + Op.CODECOPY(dest_offset=0x0, offset=0xF, size=Op.DUP1)
                    + Op.PUSH1[0x0]
                    + Op.PUSH1[0x0]
                    + Op.CREATE
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(
                        key=0x1,
                        value=Op.CALLCODE(
                            gas=0x7A120,
                            address=0x1000000000000000000000000000000000000001,
                            value=0x1,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x1000000000000000000000000000000000000001"): Account(
                    code=Op.SSTORE(key=0x2, value=0x1) + Op.STOP
                ),
                Address("0x1100000000000000000000000000000000000000"): Account(
                    code=Op.CALL(
                        gas=0x493E0,
                        address=Op.CALLDATALOAD(offset=0x0),
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x2000000000000000000000000000000000000000"): Account(
                    code=Op.PUSH1[0x0]
                    + Op.PUSH1[0x28]
                    + Op.CODECOPY(dest_offset=0x0, offset=0x11, size=Op.DUP1)
                    + Op.PUSH1[0x0]
                    + Op.PUSH1[0x0]
                    + Op.CREATE2
                    + Op.STOP
                    + Op.INVALID
                    + Op.SSTORE(
                        key=0x1,
                        value=Op.CALLCODE(
                            gas=0x7A120,
                            address=0x1000000000000000000000000000000000000001,
                            value=0x1,
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
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_callcode_in_initcode_to_exis_contract_with_v_transfer_ne_money(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Callcode inside create/create2 contract init to existing..."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x1100000000000000000000000000000000000000")
    callee = Address("0x1000000000000000000000000000000000000000")
    callee_1 = Address("0x1000000000000000000000000000000000000001")
    callee_2 = Address("0x2000000000000000000000000000000000000000")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    # Source: LLL
    # {(seq (CREATE 0 0 (lll (seq  [[1]] (CALLCODE 500000 0x1000000000000000000000000000000000000001 1 0 0 0 0)) 0)   )           )}  # noqa: E501
    pre[callee] = Account(
        balance=0x2710,
        nonce=0,
        code=(
            Op.PUSH1[0x28]
            + Op.CODECOPY(dest_offset=0x0, offset=0xF, size=Op.DUP1)
            + Op.PUSH1[0x0]
            + Op.PUSH1[0x0]
            + Op.CREATE
            + Op.STOP
            + Op.INVALID
            + Op.SSTORE(
                key=0x1,
                value=Op.CALLCODE(
                    gas=0x7A120,
                    address=0x1000000000000000000000000000000000000001,
                    value=0x1,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.STOP
        ),
    )
    # Source: LLL
    # { (SSTORE 2 1) }
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=Op.SSTORE(key=0x2, value=0x1) + Op.STOP,
    )
    # Source: LLL
    # { (CALL 300000 (CALLDATALOAD 0) 0 0 0 0 0) }
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.CALL(
                gas=0x493E0,
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
    # {(seq (CREATE2 0 0 (lll (seq  [[1]] (CALLCODE 500000 0x1000000000000000000000000000000000000001 1 0 0 0 0)) 0)   0)           )}  # noqa: E501
    pre[callee_2] = Account(
        balance=0x2710,
        nonce=0,
        code=(
            Op.PUSH1[0x0]
            + Op.PUSH1[0x28]
            + Op.CODECOPY(dest_offset=0x0, offset=0x11, size=Op.DUP1)
            + Op.PUSH1[0x0]
            + Op.PUSH1[0x0]
            + Op.CREATE2
            + Op.STOP
            + Op.INVALID
            + Op.SSTORE(
                key=0x1,
                value=Op.CALLCODE(
                    gas=0x7A120,
                    address=0x1000000000000000000000000000000000000001,
                    value=0x1,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.STOP
        ),
    )
    pre[sender] = Account(balance=0x2386F26FC10000, nonce=0)

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=tx_data,
        gas_limit=1000000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
