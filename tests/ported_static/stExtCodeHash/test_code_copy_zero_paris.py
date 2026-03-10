"""
https://github.com/ethereum/tests/issues/493,  CODECOPY and EXTCODECOPY...

Ported from:
tests/static/state_tests/stExtCodeHash/codeCopyZero_ParisFiller.yml
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
    ["tests/static/state_tests/stExtCodeHash/codeCopyZero_ParisFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_code_copy_zero_paris(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Https://github.com/ethereum/tests/issues/493,  CODECOPY and..."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xa000000000000000000000000000000000000000")
    callee = Address("0xa100000000000000000000000000000000000000")
    callee_1 = Address("0xa200000000000000000000000000000000000000")
    callee_2 = Address("0xa300000000000000000000000000000000000000")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.EXTCODECOPY(
                address=0xA222000000000000000000000000000000000000,
                dest_offset=0x0,
                offset=0x0,
                size=0x20,
            )
            + Op.SSTORE(key=0x10, value=Op.MLOAD(offset=0x0))
            + Op.SSTORE(
                key=0x11,
                value=Op.EXTCODESIZE(
                    address=0xA222000000000000000000000000000000000000,
                ),
            )
            + Op.SSTORE(
                key=0x12,
                value=Op.EXTCODEHASH(
                    address=0xA222000000000000000000000000000000000000,
                ),
            )
            + Op.SSTORE(
                key=0x13,
                value=Op.CALLCODE(
                    gas=0xC350,
                    address=0xA222000000000000000000000000000000000000,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.EXTCODECOPY(
                address=0xA200000000000000000000000000000000000000,
                dest_offset=0x0,
                offset=0x0,
                size=0x20,
            )
            + Op.SSTORE(key=0x20, value=Op.MLOAD(offset=0x0))
            + Op.SSTORE(
                key=0x21,
                value=Op.EXTCODESIZE(
                    address=0xA200000000000000000000000000000000000000,
                ),
            )
            + Op.SSTORE(
                key=0x22,
                value=Op.EXTCODEHASH(
                    address=0xA200000000000000000000000000000000000000,
                ),
            )
            + Op.SSTORE(
                key=0x23,
                value=Op.CALLCODE(
                    gas=0xC350,
                    address=0xA200000000000000000000000000000000000000,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.EXTCODECOPY(
                address=0xA300000000000000000000000000000000000000,
                dest_offset=0x0,
                offset=0x0,
                size=0x20,
            )
            + Op.SSTORE(key=0x30, value=Op.MLOAD(offset=0x0))
            + Op.SSTORE(
                key=0x31,
                value=Op.EXTCODESIZE(
                    address=0xA300000000000000000000000000000000000000,
                ),
            )
            + Op.SSTORE(
                key=0x32,
                value=Op.EXTCODEHASH(
                    address=0xA300000000000000000000000000000000000000,
                ),
            )
            + Op.SSTORE(
                key=0x33,
                value=Op.CALLCODE(
                    gas=0xC350,
                    address=0xA300000000000000000000000000000000000000,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.POP(
                Op.CALL(
                    gas=0x86470,
                    address=0xA100000000000000000000000000000000000000,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x20,
                ),
            )
            + Op.SSTORE(key=0x40, value=Op.MLOAD(offset=0x0))
            + Op.STOP
        ),
    )
    pre[callee] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=(
            Op.PUSH1[0x0]
            + Op.PUSH1[0x39]
            + Op.CODECOPY(dest_offset=0x0, offset=0x1A, size=Op.DUP1)
            + Op.PUSH1[0x0]
            + Op.PUSH1[0x0]
            + Op.MSTORE(offset=0x0, value=Op.CREATE2)
            + Op.RETURN(offset=0x0, size=0x20)
            + Op.STOP
            + Op.STOP
            + Op.INVALID
            + Op.CODECOPY(dest_offset=0x0, offset=0x0, size=0x20)
            + Op.SSTORE(key=0x50, value=Op.MLOAD(offset=0x0))
            + Op.SSTORE(key=0x51, value=Op.EXTCODESIZE(address=Op.ADDRESS))
            + Op.SSTORE(key=0x52, value=Op.EXTCODEHASH(address=Op.ADDRESS))
            + Op.SSTORE(
                key=0x53,
                value=Op.EXTCODESIZE(
                    address=Op.CALLCODE(
                        gas=0xC350,
                        address=Op.ADDRESS,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    ),
                ),
            )
            + Op.EXTCODECOPY(
                address=Op.ADDRESS,
                dest_offset=0x0,
                offset=0x0,
                size=0x20,
            )
            + Op.SSTORE(key=0x54, value=Op.MLOAD(offset=0x0))
            + Op.STOP
        ),
    )
    pre[callee_1] = Account(balance=0xDE0B6B3A7640000, nonce=0)
    pre[callee_2] = Account(balance=10, nonce=0)
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=1400000,
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = {
        Address("0x64bc50092fd622c9cc47d658b99c1af75aaa3d68"): Account(
            storage={
                80: 0x60206000600039600051605055303B605155303F605255600060006000600060,  # noqa: E501
                82: 0xC5D2460186F7233C927E7DB2DCC703C0E500B653CA82273B7BFAD8045D85A470,  # noqa: E501
            },
        ),
        contract: Account(
            storage={
                19: 1,
                34: 0xC5D2460186F7233C927E7DB2DCC703C0E500B653CA82273B7BFAD8045D85A470,  # noqa: E501
                35: 1,
                50: 0xC5D2460186F7233C927E7DB2DCC703C0E500B653CA82273B7BFAD8045D85A470,  # noqa: E501
                51: 1,
                64: 0x64BC50092FD622C9CC47D658B99C1AF75AAA3D68,
            },
            code=(
                Op.EXTCODECOPY(
                    address=0xA222000000000000000000000000000000000000,
                    dest_offset=0x0,
                    offset=0x0,
                    size=0x20,
                )
                + Op.SSTORE(key=0x10, value=Op.MLOAD(offset=0x0))
                + Op.SSTORE(
                    key=0x11,
                    value=Op.EXTCODESIZE(
                        address=0xA222000000000000000000000000000000000000,
                    ),
                )
                + Op.SSTORE(
                    key=0x12,
                    value=Op.EXTCODEHASH(
                        address=0xA222000000000000000000000000000000000000,
                    ),
                )
                + Op.SSTORE(
                    key=0x13,
                    value=Op.CALLCODE(
                        gas=0xC350,
                        address=0xA222000000000000000000000000000000000000,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    ),
                )
                + Op.EXTCODECOPY(
                    address=0xA200000000000000000000000000000000000000,
                    dest_offset=0x0,
                    offset=0x0,
                    size=0x20,
                )
                + Op.SSTORE(key=0x20, value=Op.MLOAD(offset=0x0))
                + Op.SSTORE(
                    key=0x21,
                    value=Op.EXTCODESIZE(
                        address=0xA200000000000000000000000000000000000000,
                    ),
                )
                + Op.SSTORE(
                    key=0x22,
                    value=Op.EXTCODEHASH(
                        address=0xA200000000000000000000000000000000000000,
                    ),
                )
                + Op.SSTORE(
                    key=0x23,
                    value=Op.CALLCODE(
                        gas=0xC350,
                        address=0xA200000000000000000000000000000000000000,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    ),
                )
                + Op.EXTCODECOPY(
                    address=0xA300000000000000000000000000000000000000,
                    dest_offset=0x0,
                    offset=0x0,
                    size=0x20,
                )
                + Op.SSTORE(key=0x30, value=Op.MLOAD(offset=0x0))
                + Op.SSTORE(
                    key=0x31,
                    value=Op.EXTCODESIZE(
                        address=0xA300000000000000000000000000000000000000,
                    ),
                )
                + Op.SSTORE(
                    key=0x32,
                    value=Op.EXTCODEHASH(
                        address=0xA300000000000000000000000000000000000000,
                    ),
                )
                + Op.SSTORE(
                    key=0x33,
                    value=Op.CALLCODE(
                        gas=0xC350,
                        address=0xA300000000000000000000000000000000000000,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    ),
                )
                + Op.POP(
                    Op.CALL(
                        gas=0x86470,
                        address=0xA100000000000000000000000000000000000000,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x20,
                    ),
                )
                + Op.SSTORE(key=0x40, value=Op.MLOAD(offset=0x0))
                + Op.STOP
            ),
        ),
        callee: Account(
            code=(
                Op.PUSH1[0x0]
                + Op.PUSH1[0x39]
                + Op.CODECOPY(dest_offset=0x0, offset=0x1A, size=Op.DUP1)
                + Op.PUSH1[0x0]
                + Op.PUSH1[0x0]
                + Op.MSTORE(offset=0x0, value=Op.CREATE2)
                + Op.RETURN(offset=0x0, size=0x20)
                + Op.STOP
                + Op.STOP
                + Op.INVALID
                + Op.CODECOPY(dest_offset=0x0, offset=0x0, size=0x20)
                + Op.SSTORE(key=0x50, value=Op.MLOAD(offset=0x0))
                + Op.SSTORE(key=0x51, value=Op.EXTCODESIZE(address=Op.ADDRESS))
                + Op.SSTORE(key=0x52, value=Op.EXTCODEHASH(address=Op.ADDRESS))
                + Op.SSTORE(
                    key=0x53,
                    value=Op.EXTCODESIZE(
                        address=Op.CALLCODE(
                            gas=0xC350,
                            address=Op.ADDRESS,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    ),
                )
                + Op.EXTCODECOPY(
                    address=Op.ADDRESS,
                    dest_offset=0x0,
                    offset=0x0,
                    size=0x20,
                )
                + Op.SSTORE(key=0x54, value=Op.MLOAD(offset=0x0))
                + Op.STOP
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
