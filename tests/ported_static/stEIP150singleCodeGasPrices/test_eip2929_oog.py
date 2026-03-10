"""
Ori Pomerantz qbzzt1@gmail.com.

Ported from:
tests/static/state_tests/stEIP150singleCodeGasPrices/eip2929OOGFiller.yml
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
        "tests/static/state_tests/stEIP150singleCodeGasPrices/eip2929OOGFiller.yml",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        (
            "1a8451e600000000000000000000000000000000000000000000000000000000000010fa00000000000000000000000000000000000000000000000000000000000006d6",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001031"): Account(
                    code=Op.BALANCE(address=0xACC7) + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000103b"): Account(
                    code=Op.EXTCODESIZE(address=0x1031) + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000103c"): Account(
                    code=Op.EXTCODECOPY(
                        address=0x1031, dest_offset=0x0, offset=0x0, size=0x20
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000103f"): Account(
                    code=Op.EXTCODEHASH(address=0x1031) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001054"): Account(
                    code=Op.SLOAD(key=0x0) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001055"): Account(
                    code=Op.SSTORE(key=0x0, value=0x60A7) + Op.STOP
                ),
                Address("0x00000000000000000000000000000000000010f1"): Account(
                    code=Op.CALL(
                        gas=0x6A5,
                        address=0xACC7,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000000010f2"): Account(
                    code=Op.CALLCODE(
                        gas=0x6A5,
                        address=0xACC7,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000000010f4"): Account(
                    code=Op.DELEGATECALL(
                        gas=0x6A5,
                        address=0xACC7,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000000010fa"): Account(
                    code=Op.STATICCALL(
                        gas=0x6A5,
                        address=0xACC7,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000acc7"): Account(
                    code=Op.RETURN(offset=0x0, size=0x0) + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.CALL(
                            gas=Op.CALLDATALOAD(offset=0x24),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
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
            "1a8451e6000000000000000000000000000000000000000000000000000000000000105500000000000000000000000000000000000000000000000000000000000055f0",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001031"): Account(
                    code=Op.BALANCE(address=0xACC7) + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000103b"): Account(
                    code=Op.EXTCODESIZE(address=0x1031) + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000103c"): Account(
                    code=Op.EXTCODECOPY(
                        address=0x1031, dest_offset=0x0, offset=0x0, size=0x20
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000103f"): Account(
                    code=Op.EXTCODEHASH(address=0x1031) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001054"): Account(
                    code=Op.SLOAD(key=0x0) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001055"): Account(
                    code=Op.SSTORE(key=0x0, value=0x60A7) + Op.STOP
                ),
                Address("0x00000000000000000000000000000000000010f1"): Account(
                    code=Op.CALL(
                        gas=0x6A5,
                        address=0xACC7,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000000010f2"): Account(
                    code=Op.CALLCODE(
                        gas=0x6A5,
                        address=0xACC7,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000000010f4"): Account(
                    code=Op.DELEGATECALL(
                        gas=0x6A5,
                        address=0xACC7,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000000010fa"): Account(
                    code=Op.STATICCALL(
                        gas=0x6A5,
                        address=0xACC7,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000acc7"): Account(
                    code=Op.RETURN(offset=0x0, size=0x0) + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.CALL(
                            gas=Op.CALLDATALOAD(offset=0x24),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
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
            "1a8451e6000000000000000000000000000000000000000000000000000000000000103100000000000000000000000000000000000000000000000000000000000007d0",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001031"): Account(
                    code=Op.BALANCE(address=0xACC7) + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000103b"): Account(
                    code=Op.EXTCODESIZE(address=0x1031) + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000103c"): Account(
                    code=Op.EXTCODECOPY(
                        address=0x1031, dest_offset=0x0, offset=0x0, size=0x20
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000103f"): Account(
                    code=Op.EXTCODEHASH(address=0x1031) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001054"): Account(
                    code=Op.SLOAD(key=0x0) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001055"): Account(
                    code=Op.SSTORE(key=0x0, value=0x60A7) + Op.STOP
                ),
                Address("0x00000000000000000000000000000000000010f1"): Account(
                    code=Op.CALL(
                        gas=0x6A5,
                        address=0xACC7,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000000010f2"): Account(
                    code=Op.CALLCODE(
                        gas=0x6A5,
                        address=0xACC7,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000000010f4"): Account(
                    code=Op.DELEGATECALL(
                        gas=0x6A5,
                        address=0xACC7,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000000010fa"): Account(
                    code=Op.STATICCALL(
                        gas=0x6A5,
                        address=0xACC7,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000acc7"): Account(
                    code=Op.RETURN(offset=0x0, size=0x0) + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.CALL(
                            gas=Op.CALLDATALOAD(offset=0x24),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
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
            "1a8451e6000000000000000000000000000000000000000000000000000000000000103b00000000000000000000000000000000000000000000000000000000000009c4",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001031"): Account(
                    code=Op.BALANCE(address=0xACC7) + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000103b"): Account(
                    code=Op.EXTCODESIZE(address=0x1031) + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000103c"): Account(
                    code=Op.EXTCODECOPY(
                        address=0x1031, dest_offset=0x0, offset=0x0, size=0x20
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000103f"): Account(
                    code=Op.EXTCODEHASH(address=0x1031) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001054"): Account(
                    code=Op.SLOAD(key=0x0) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001055"): Account(
                    code=Op.SSTORE(key=0x0, value=0x60A7) + Op.STOP
                ),
                Address("0x00000000000000000000000000000000000010f1"): Account(
                    code=Op.CALL(
                        gas=0x6A5,
                        address=0xACC7,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000000010f2"): Account(
                    code=Op.CALLCODE(
                        gas=0x6A5,
                        address=0xACC7,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000000010f4"): Account(
                    code=Op.DELEGATECALL(
                        gas=0x6A5,
                        address=0xACC7,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000000010fa"): Account(
                    code=Op.STATICCALL(
                        gas=0x6A5,
                        address=0xACC7,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000acc7"): Account(
                    code=Op.RETURN(offset=0x0, size=0x0) + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.CALL(
                            gas=Op.CALLDATALOAD(offset=0x24),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
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
            "1a8451e6000000000000000000000000000000000000000000000000000000000000103c00000000000000000000000000000000000000000000000000000000000009c4",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001031"): Account(
                    code=Op.BALANCE(address=0xACC7) + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000103b"): Account(
                    code=Op.EXTCODESIZE(address=0x1031) + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000103c"): Account(
                    code=Op.EXTCODECOPY(
                        address=0x1031, dest_offset=0x0, offset=0x0, size=0x20
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000103f"): Account(
                    code=Op.EXTCODEHASH(address=0x1031) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001054"): Account(
                    code=Op.SLOAD(key=0x0) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001055"): Account(
                    code=Op.SSTORE(key=0x0, value=0x60A7) + Op.STOP
                ),
                Address("0x00000000000000000000000000000000000010f1"): Account(
                    code=Op.CALL(
                        gas=0x6A5,
                        address=0xACC7,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000000010f2"): Account(
                    code=Op.CALLCODE(
                        gas=0x6A5,
                        address=0xACC7,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000000010f4"): Account(
                    code=Op.DELEGATECALL(
                        gas=0x6A5,
                        address=0xACC7,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000000010fa"): Account(
                    code=Op.STATICCALL(
                        gas=0x6A5,
                        address=0xACC7,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000acc7"): Account(
                    code=Op.RETURN(offset=0x0, size=0x0) + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.CALL(
                            gas=Op.CALLDATALOAD(offset=0x24),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
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
            "1a8451e6000000000000000000000000000000000000000000000000000000000000103f00000000000000000000000000000000000000000000000000000000000009c4",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001031"): Account(
                    code=Op.BALANCE(address=0xACC7) + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000103b"): Account(
                    code=Op.EXTCODESIZE(address=0x1031) + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000103c"): Account(
                    code=Op.EXTCODECOPY(
                        address=0x1031, dest_offset=0x0, offset=0x0, size=0x20
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000103f"): Account(
                    code=Op.EXTCODEHASH(address=0x1031) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001054"): Account(
                    code=Op.SLOAD(key=0x0) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001055"): Account(
                    code=Op.SSTORE(key=0x0, value=0x60A7) + Op.STOP
                ),
                Address("0x00000000000000000000000000000000000010f1"): Account(
                    code=Op.CALL(
                        gas=0x6A5,
                        address=0xACC7,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000000010f2"): Account(
                    code=Op.CALLCODE(
                        gas=0x6A5,
                        address=0xACC7,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000000010f4"): Account(
                    code=Op.DELEGATECALL(
                        gas=0x6A5,
                        address=0xACC7,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000000010fa"): Account(
                    code=Op.STATICCALL(
                        gas=0x6A5,
                        address=0xACC7,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000acc7"): Account(
                    code=Op.RETURN(offset=0x0, size=0x0) + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.CALL(
                            gas=Op.CALLDATALOAD(offset=0x24),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
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
            "1a8451e600000000000000000000000000000000000000000000000000000000000010f100000000000000000000000000000000000000000000000000000000000006d6",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001031"): Account(
                    code=Op.BALANCE(address=0xACC7) + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000103b"): Account(
                    code=Op.EXTCODESIZE(address=0x1031) + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000103c"): Account(
                    code=Op.EXTCODECOPY(
                        address=0x1031, dest_offset=0x0, offset=0x0, size=0x20
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000103f"): Account(
                    code=Op.EXTCODEHASH(address=0x1031) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001054"): Account(
                    code=Op.SLOAD(key=0x0) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001055"): Account(
                    code=Op.SSTORE(key=0x0, value=0x60A7) + Op.STOP
                ),
                Address("0x00000000000000000000000000000000000010f1"): Account(
                    code=Op.CALL(
                        gas=0x6A5,
                        address=0xACC7,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000000010f2"): Account(
                    code=Op.CALLCODE(
                        gas=0x6A5,
                        address=0xACC7,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000000010f4"): Account(
                    code=Op.DELEGATECALL(
                        gas=0x6A5,
                        address=0xACC7,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000000010fa"): Account(
                    code=Op.STATICCALL(
                        gas=0x6A5,
                        address=0xACC7,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000acc7"): Account(
                    code=Op.RETURN(offset=0x0, size=0x0) + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.CALL(
                            gas=Op.CALLDATALOAD(offset=0x24),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
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
            "1a8451e600000000000000000000000000000000000000000000000000000000000010f200000000000000000000000000000000000000000000000000000000000006d6",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001031"): Account(
                    code=Op.BALANCE(address=0xACC7) + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000103b"): Account(
                    code=Op.EXTCODESIZE(address=0x1031) + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000103c"): Account(
                    code=Op.EXTCODECOPY(
                        address=0x1031, dest_offset=0x0, offset=0x0, size=0x20
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000103f"): Account(
                    code=Op.EXTCODEHASH(address=0x1031) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001054"): Account(
                    code=Op.SLOAD(key=0x0) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001055"): Account(
                    code=Op.SSTORE(key=0x0, value=0x60A7) + Op.STOP
                ),
                Address("0x00000000000000000000000000000000000010f1"): Account(
                    code=Op.CALL(
                        gas=0x6A5,
                        address=0xACC7,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000000010f2"): Account(
                    code=Op.CALLCODE(
                        gas=0x6A5,
                        address=0xACC7,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000000010f4"): Account(
                    code=Op.DELEGATECALL(
                        gas=0x6A5,
                        address=0xACC7,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000000010fa"): Account(
                    code=Op.STATICCALL(
                        gas=0x6A5,
                        address=0xACC7,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000acc7"): Account(
                    code=Op.RETURN(offset=0x0, size=0x0) + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.CALL(
                            gas=Op.CALLDATALOAD(offset=0x24),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
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
            "1a8451e600000000000000000000000000000000000000000000000000000000000010f400000000000000000000000000000000000000000000000000000000000006d6",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001031"): Account(
                    code=Op.BALANCE(address=0xACC7) + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000103b"): Account(
                    code=Op.EXTCODESIZE(address=0x1031) + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000103c"): Account(
                    code=Op.EXTCODECOPY(
                        address=0x1031, dest_offset=0x0, offset=0x0, size=0x20
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000103f"): Account(
                    code=Op.EXTCODEHASH(address=0x1031) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001054"): Account(
                    code=Op.SLOAD(key=0x0) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001055"): Account(
                    code=Op.SSTORE(key=0x0, value=0x60A7) + Op.STOP
                ),
                Address("0x00000000000000000000000000000000000010f1"): Account(
                    code=Op.CALL(
                        gas=0x6A5,
                        address=0xACC7,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000000010f2"): Account(
                    code=Op.CALLCODE(
                        gas=0x6A5,
                        address=0xACC7,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000000010f4"): Account(
                    code=Op.DELEGATECALL(
                        gas=0x6A5,
                        address=0xACC7,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000000010fa"): Account(
                    code=Op.STATICCALL(
                        gas=0x6A5,
                        address=0xACC7,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000acc7"): Account(
                    code=Op.RETURN(offset=0x0, size=0x0) + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.CALL(
                            gas=Op.CALLDATALOAD(offset=0x24),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
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
            "1a8451e6000000000000000000000000000000000000000000000000000000000000105400000000000000000000000000000000000000000000000000000000000007d0",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001031"): Account(
                    code=Op.BALANCE(address=0xACC7) + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000103b"): Account(
                    code=Op.EXTCODESIZE(address=0x1031) + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000103c"): Account(
                    code=Op.EXTCODECOPY(
                        address=0x1031, dest_offset=0x0, offset=0x0, size=0x20
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000103f"): Account(
                    code=Op.EXTCODEHASH(address=0x1031) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001054"): Account(
                    code=Op.SLOAD(key=0x0) + Op.STOP
                ),
                Address("0x0000000000000000000000000000000000001055"): Account(
                    code=Op.SSTORE(key=0x0, value=0x60A7) + Op.STOP
                ),
                Address("0x00000000000000000000000000000000000010f1"): Account(
                    code=Op.CALL(
                        gas=0x6A5,
                        address=0xACC7,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000000010f2"): Account(
                    code=Op.CALLCODE(
                        gas=0x6A5,
                        address=0xACC7,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000000010f4"): Account(
                    code=Op.DELEGATECALL(
                        gas=0x6A5,
                        address=0xACC7,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x00000000000000000000000000000000000010fa"): Account(
                    code=Op.STATICCALL(
                        gas=0x6A5,
                        address=0xACC7,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x000000000000000000000000000000000000acc7"): Account(
                    code=Op.RETURN(offset=0x0, size=0x0) + Op.STOP
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=Op.SSTORE(
                        key=0x0,
                        value=Op.CALL(
                            gas=Op.CALLDATALOAD(offset=0x24),
                            address=Op.CALLDATALOAD(offset=0x4),
                            value=0x0,
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
    ids=[
        "case0",
        "case1",
        "case2",
        "case3",
        "case4",
        "case5",
        "case6",
        "case7",
        "case8",
        "case9",
    ],
)
@pytest.mark.pre_alloc_mutable
def test_eip2929_oog(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Ori Pomerantz qbzzt1@gmail.com."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xcccccccccccccccccccccccccccccccccccccccc")
    callee = Address("0x0000000000000000000000000000000000001031")
    callee_1 = Address("0x000000000000000000000000000000000000103b")
    callee_2 = Address("0x000000000000000000000000000000000000103c")
    callee_3 = Address("0x000000000000000000000000000000000000103f")
    callee_4 = Address("0x0000000000000000000000000000000000001054")
    callee_5 = Address("0x0000000000000000000000000000000000001055")
    callee_6 = Address("0x00000000000000000000000000000000000010f1")
    callee_7 = Address("0x00000000000000000000000000000000000010f2")
    callee_8 = Address("0x00000000000000000000000000000000000010f4")
    callee_9 = Address("0x00000000000000000000000000000000000010fa")
    callee_10 = Address("0x000000000000000000000000000000000000acc7")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000,
    )

    pre[callee] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=Op.BALANCE(address=0xACC7) + Op.STOP,
    )
    pre[callee_1] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=Op.EXTCODESIZE(address=0x1031) + Op.STOP,
    )
    pre[callee_2] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=(
            Op.EXTCODECOPY(
                address=0x1031,
                dest_offset=0x0,
                offset=0x0,
                size=0x20,
            )
            + Op.STOP
        ),
    )
    pre[callee_3] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=Op.EXTCODEHASH(address=0x1031) + Op.STOP,
    )
    pre[callee_4] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=Op.SLOAD(key=0x0) + Op.STOP,
    )
    pre[callee_5] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=Op.SSTORE(key=0x0, value=0x60A7) + Op.STOP,
    )
    pre[callee_6] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=(
            Op.CALL(
                gas=0x6A5,
                address=0xACC7,
                value=0x0,
                args_offset=0x0,
                args_size=0x0,
                ret_offset=0x0,
                ret_size=0x0,
            )
            + Op.STOP
        ),
    )
    pre[callee_7] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=(
            Op.CALLCODE(
                gas=0x6A5,
                address=0xACC7,
                value=0x0,
                args_offset=0x0,
                args_size=0x0,
                ret_offset=0x0,
                ret_size=0x0,
            )
            + Op.STOP
        ),
    )
    pre[callee_8] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=(
            Op.DELEGATECALL(
                gas=0x6A5,
                address=0xACC7,
                args_offset=0x0,
                args_size=0x0,
                ret_offset=0x0,
                ret_size=0x0,
            )
            + Op.STOP
        ),
    )
    pre[callee_9] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=(
            Op.STATICCALL(
                gas=0x6A5,
                address=0xACC7,
                args_offset=0x0,
                args_size=0x0,
                ret_offset=0x0,
                ret_size=0x0,
            )
            + Op.STOP
        ),
    )
    pre[callee_10] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=Op.RETURN(offset=0x0, size=0x0) + Op.STOP,
    )
    pre[sender] = Account(balance=0xBA1A9CE0BA1A9CE, nonce=1)
    pre[contract] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=(
            Op.SSTORE(
                key=0x0,
                value=Op.CALL(
                    gas=Op.CALLDATALOAD(offset=0x24),
                    address=Op.CALLDATALOAD(offset=0x4),
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.STOP
        ),
        storage={0x0: 0x60A7},
    )

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=tx_data,
        gas_limit=16777216,
        gas_price=10,
        nonce=1,
        value=1,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
