"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRevertTest/RevertOpcodeReturnFiller.json
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
    ["tests/static/state_tests/stRevertTest/RevertOpcodeReturnFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, tx_gas_limit, expected_post",
    [
        (
            "0000000000000000000000001963fd2c717f5b4b9fa3d6baf38d66241e1ec005",
            800000,
            {
                Address("0x1963fd2c717f5b4b9fa3d6baf38d66241e1ec005"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x1fc98371f1a058f1a6042e30a141aa8bb67dd1bc"): Account(
                    storage={2: 0x726576657274206D657373616765},
                    code=Op.SSTORE(
                        key=0x1,
                        value=Op.CALL(
                            gas=0x249F0,
                            address=Op.CALLDATALOAD(offset=0x0),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x50eaca0a040ac6242d0c01cc1ff82f5b95cc10e4"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(
                        offset=0x0, size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
                    )
                    + Op.STOP
                ),
                Address("0x745e52346d8549444323699e9fc383ae89bdd24f"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x0, size=0x0)
                    + Op.STOP
                ),
                Address("0x858f82bbfd84fc9eb91291458511df77311dbd0d"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(
                        offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFF, size=0x0
                    )
                    + Op.STOP
                ),
                Address("0xe5b2dfe7f932f2d5eaa7c8fb2e1e9a8b6a846fd7"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x1, size=0x0)
                    + Op.STOP
                ),
                Address("0xf933d2374d5875de033a8ed9d9c1ce5dea25c78b"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x100, size=0x0)
                    + Op.STOP
                ),
            },
        ),
        (
            "0000000000000000000000001963fd2c717f5b4b9fa3d6baf38d66241e1ec005",
            80000,
            {
                Address("0x1963fd2c717f5b4b9fa3d6baf38d66241e1ec005"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x1fc98371f1a058f1a6042e30a141aa8bb67dd1bc"): Account(
                    storage={2: 0x726576657274206D657373616765},
                    code=Op.SSTORE(
                        key=0x1,
                        value=Op.CALL(
                            gas=0x249F0,
                            address=Op.CALLDATALOAD(offset=0x0),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP,
                ),
                Address("0x50eaca0a040ac6242d0c01cc1ff82f5b95cc10e4"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(
                        offset=0x0, size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
                    )
                    + Op.STOP
                ),
                Address("0x745e52346d8549444323699e9fc383ae89bdd24f"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x0, size=0x0)
                    + Op.STOP
                ),
                Address("0x858f82bbfd84fc9eb91291458511df77311dbd0d"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(
                        offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFF, size=0x0
                    )
                    + Op.STOP
                ),
                Address("0xe5b2dfe7f932f2d5eaa7c8fb2e1e9a8b6a846fd7"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x1, size=0x0)
                    + Op.STOP
                ),
                Address("0xf933d2374d5875de033a8ed9d9c1ce5dea25c78b"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x100, size=0x0)
                    + Op.STOP
                ),
            },
        ),
        (
            "000000000000000000000000745e52346d8549444323699e9fc383ae89bdd24f",
            800000,
            {
                Address("0x1963fd2c717f5b4b9fa3d6baf38d66241e1ec005"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x1fc98371f1a058f1a6042e30a141aa8bb67dd1bc"): Account(
                    code=Op.SSTORE(
                        key=0x1,
                        value=Op.CALL(
                            gas=0x249F0,
                            address=Op.CALLDATALOAD(offset=0x0),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x50eaca0a040ac6242d0c01cc1ff82f5b95cc10e4"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(
                        offset=0x0, size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
                    )
                    + Op.STOP
                ),
                Address("0x745e52346d8549444323699e9fc383ae89bdd24f"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x0, size=0x0)
                    + Op.STOP
                ),
                Address("0x858f82bbfd84fc9eb91291458511df77311dbd0d"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(
                        offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFF, size=0x0
                    )
                    + Op.STOP
                ),
                Address("0xe5b2dfe7f932f2d5eaa7c8fb2e1e9a8b6a846fd7"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x1, size=0x0)
                    + Op.STOP
                ),
                Address("0xf933d2374d5875de033a8ed9d9c1ce5dea25c78b"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x100, size=0x0)
                    + Op.STOP
                ),
            },
        ),
        (
            "000000000000000000000000745e52346d8549444323699e9fc383ae89bdd24f",
            80000,
            {
                Address("0x1963fd2c717f5b4b9fa3d6baf38d66241e1ec005"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x1fc98371f1a058f1a6042e30a141aa8bb67dd1bc"): Account(
                    code=Op.SSTORE(
                        key=0x1,
                        value=Op.CALL(
                            gas=0x249F0,
                            address=Op.CALLDATALOAD(offset=0x0),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x50eaca0a040ac6242d0c01cc1ff82f5b95cc10e4"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(
                        offset=0x0, size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
                    )
                    + Op.STOP
                ),
                Address("0x745e52346d8549444323699e9fc383ae89bdd24f"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x0, size=0x0)
                    + Op.STOP
                ),
                Address("0x858f82bbfd84fc9eb91291458511df77311dbd0d"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(
                        offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFF, size=0x0
                    )
                    + Op.STOP
                ),
                Address("0xe5b2dfe7f932f2d5eaa7c8fb2e1e9a8b6a846fd7"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x1, size=0x0)
                    + Op.STOP
                ),
                Address("0xf933d2374d5875de033a8ed9d9c1ce5dea25c78b"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x100, size=0x0)
                    + Op.STOP
                ),
            },
        ),
        (
            "00000000000000000000000050eaca0a040ac6242d0c01cc1ff82f5b95cc10e4",
            800000,
            {
                Address("0x1963fd2c717f5b4b9fa3d6baf38d66241e1ec005"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x1fc98371f1a058f1a6042e30a141aa8bb67dd1bc"): Account(
                    code=Op.SSTORE(
                        key=0x1,
                        value=Op.CALL(
                            gas=0x249F0,
                            address=Op.CALLDATALOAD(offset=0x0),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x50eaca0a040ac6242d0c01cc1ff82f5b95cc10e4"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(
                        offset=0x0, size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
                    )
                    + Op.STOP
                ),
                Address("0x745e52346d8549444323699e9fc383ae89bdd24f"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x0, size=0x0)
                    + Op.STOP
                ),
                Address("0x858f82bbfd84fc9eb91291458511df77311dbd0d"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(
                        offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFF, size=0x0
                    )
                    + Op.STOP
                ),
                Address("0xe5b2dfe7f932f2d5eaa7c8fb2e1e9a8b6a846fd7"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x1, size=0x0)
                    + Op.STOP
                ),
                Address("0xf933d2374d5875de033a8ed9d9c1ce5dea25c78b"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x100, size=0x0)
                    + Op.STOP
                ),
            },
        ),
        (
            "00000000000000000000000050eaca0a040ac6242d0c01cc1ff82f5b95cc10e4",
            80000,
            {
                Address("0x1963fd2c717f5b4b9fa3d6baf38d66241e1ec005"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x1fc98371f1a058f1a6042e30a141aa8bb67dd1bc"): Account(
                    code=Op.SSTORE(
                        key=0x1,
                        value=Op.CALL(
                            gas=0x249F0,
                            address=Op.CALLDATALOAD(offset=0x0),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x50eaca0a040ac6242d0c01cc1ff82f5b95cc10e4"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(
                        offset=0x0, size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
                    )
                    + Op.STOP
                ),
                Address("0x745e52346d8549444323699e9fc383ae89bdd24f"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x0, size=0x0)
                    + Op.STOP
                ),
                Address("0x858f82bbfd84fc9eb91291458511df77311dbd0d"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(
                        offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFF, size=0x0
                    )
                    + Op.STOP
                ),
                Address("0xe5b2dfe7f932f2d5eaa7c8fb2e1e9a8b6a846fd7"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x1, size=0x0)
                    + Op.STOP
                ),
                Address("0xf933d2374d5875de033a8ed9d9c1ce5dea25c78b"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x100, size=0x0)
                    + Op.STOP
                ),
            },
        ),
        (
            "000000000000000000000000f933d2374d5875de033a8ed9d9c1ce5dea25c78b",
            800000,
            {
                Address("0x1963fd2c717f5b4b9fa3d6baf38d66241e1ec005"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x1fc98371f1a058f1a6042e30a141aa8bb67dd1bc"): Account(
                    code=Op.SSTORE(
                        key=0x1,
                        value=Op.CALL(
                            gas=0x249F0,
                            address=Op.CALLDATALOAD(offset=0x0),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x50eaca0a040ac6242d0c01cc1ff82f5b95cc10e4"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(
                        offset=0x0, size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
                    )
                    + Op.STOP
                ),
                Address("0x745e52346d8549444323699e9fc383ae89bdd24f"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x0, size=0x0)
                    + Op.STOP
                ),
                Address("0x858f82bbfd84fc9eb91291458511df77311dbd0d"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(
                        offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFF, size=0x0
                    )
                    + Op.STOP
                ),
                Address("0xe5b2dfe7f932f2d5eaa7c8fb2e1e9a8b6a846fd7"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x1, size=0x0)
                    + Op.STOP
                ),
                Address("0xf933d2374d5875de033a8ed9d9c1ce5dea25c78b"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x100, size=0x0)
                    + Op.STOP
                ),
            },
        ),
        (
            "000000000000000000000000f933d2374d5875de033a8ed9d9c1ce5dea25c78b",
            80000,
            {
                Address("0x1963fd2c717f5b4b9fa3d6baf38d66241e1ec005"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x1fc98371f1a058f1a6042e30a141aa8bb67dd1bc"): Account(
                    code=Op.SSTORE(
                        key=0x1,
                        value=Op.CALL(
                            gas=0x249F0,
                            address=Op.CALLDATALOAD(offset=0x0),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x50eaca0a040ac6242d0c01cc1ff82f5b95cc10e4"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(
                        offset=0x0, size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
                    )
                    + Op.STOP
                ),
                Address("0x745e52346d8549444323699e9fc383ae89bdd24f"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x0, size=0x0)
                    + Op.STOP
                ),
                Address("0x858f82bbfd84fc9eb91291458511df77311dbd0d"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(
                        offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFF, size=0x0
                    )
                    + Op.STOP
                ),
                Address("0xe5b2dfe7f932f2d5eaa7c8fb2e1e9a8b6a846fd7"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x1, size=0x0)
                    + Op.STOP
                ),
                Address("0xf933d2374d5875de033a8ed9d9c1ce5dea25c78b"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x100, size=0x0)
                    + Op.STOP
                ),
            },
        ),
        (
            "000000000000000000000000e5b2dfe7f932f2d5eaa7c8fb2e1e9a8b6a846fd7",
            800000,
            {
                Address("0x1963fd2c717f5b4b9fa3d6baf38d66241e1ec005"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x1fc98371f1a058f1a6042e30a141aa8bb67dd1bc"): Account(
                    code=Op.SSTORE(
                        key=0x1,
                        value=Op.CALL(
                            gas=0x249F0,
                            address=Op.CALLDATALOAD(offset=0x0),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x50eaca0a040ac6242d0c01cc1ff82f5b95cc10e4"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(
                        offset=0x0, size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
                    )
                    + Op.STOP
                ),
                Address("0x745e52346d8549444323699e9fc383ae89bdd24f"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x0, size=0x0)
                    + Op.STOP
                ),
                Address("0x858f82bbfd84fc9eb91291458511df77311dbd0d"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(
                        offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFF, size=0x0
                    )
                    + Op.STOP
                ),
                Address("0xe5b2dfe7f932f2d5eaa7c8fb2e1e9a8b6a846fd7"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x1, size=0x0)
                    + Op.STOP
                ),
                Address("0xf933d2374d5875de033a8ed9d9c1ce5dea25c78b"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x100, size=0x0)
                    + Op.STOP
                ),
            },
        ),
        (
            "000000000000000000000000e5b2dfe7f932f2d5eaa7c8fb2e1e9a8b6a846fd7",
            80000,
            {
                Address("0x1963fd2c717f5b4b9fa3d6baf38d66241e1ec005"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x1fc98371f1a058f1a6042e30a141aa8bb67dd1bc"): Account(
                    code=Op.SSTORE(
                        key=0x1,
                        value=Op.CALL(
                            gas=0x249F0,
                            address=Op.CALLDATALOAD(offset=0x0),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x50eaca0a040ac6242d0c01cc1ff82f5b95cc10e4"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(
                        offset=0x0, size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
                    )
                    + Op.STOP
                ),
                Address("0x745e52346d8549444323699e9fc383ae89bdd24f"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x0, size=0x0)
                    + Op.STOP
                ),
                Address("0x858f82bbfd84fc9eb91291458511df77311dbd0d"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(
                        offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFF, size=0x0
                    )
                    + Op.STOP
                ),
                Address("0xe5b2dfe7f932f2d5eaa7c8fb2e1e9a8b6a846fd7"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x1, size=0x0)
                    + Op.STOP
                ),
                Address("0xf933d2374d5875de033a8ed9d9c1ce5dea25c78b"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x100, size=0x0)
                    + Op.STOP
                ),
            },
        ),
        (
            "000000000000000000000000858f82bbfd84fc9eb91291458511df77311dbd0d",
            800000,
            {
                Address("0x1963fd2c717f5b4b9fa3d6baf38d66241e1ec005"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x1fc98371f1a058f1a6042e30a141aa8bb67dd1bc"): Account(
                    code=Op.SSTORE(
                        key=0x1,
                        value=Op.CALL(
                            gas=0x249F0,
                            address=Op.CALLDATALOAD(offset=0x0),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x50eaca0a040ac6242d0c01cc1ff82f5b95cc10e4"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(
                        offset=0x0, size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
                    )
                    + Op.STOP
                ),
                Address("0x745e52346d8549444323699e9fc383ae89bdd24f"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x0, size=0x0)
                    + Op.STOP
                ),
                Address("0x858f82bbfd84fc9eb91291458511df77311dbd0d"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(
                        offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFF, size=0x0
                    )
                    + Op.STOP
                ),
                Address("0xe5b2dfe7f932f2d5eaa7c8fb2e1e9a8b6a846fd7"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x1, size=0x0)
                    + Op.STOP
                ),
                Address("0xf933d2374d5875de033a8ed9d9c1ce5dea25c78b"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x100, size=0x0)
                    + Op.STOP
                ),
            },
        ),
        (
            "000000000000000000000000858f82bbfd84fc9eb91291458511df77311dbd0d",
            80000,
            {
                Address("0x1963fd2c717f5b4b9fa3d6baf38d66241e1ec005"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x0, size=0x20)
                    + Op.STOP
                ),
                Address("0x1fc98371f1a058f1a6042e30a141aa8bb67dd1bc"): Account(
                    code=Op.SSTORE(
                        key=0x1,
                        value=Op.CALL(
                            gas=0x249F0,
                            address=Op.CALLDATALOAD(offset=0x0),
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x20,
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
                    + Op.STOP
                ),
                Address("0x50eaca0a040ac6242d0c01cc1ff82f5b95cc10e4"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(
                        offset=0x0, size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
                    )
                    + Op.STOP
                ),
                Address("0x745e52346d8549444323699e9fc383ae89bdd24f"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x0, size=0x0)
                    + Op.STOP
                ),
                Address("0x858f82bbfd84fc9eb91291458511df77311dbd0d"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(
                        offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFF, size=0x0
                    )
                    + Op.STOP
                ),
                Address("0xe5b2dfe7f932f2d5eaa7c8fb2e1e9a8b6a846fd7"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x1, size=0x0)
                    + Op.STOP
                ),
                Address("0xf933d2374d5875de033a8ed9d9c1ce5dea25c78b"): Account(
                    code=Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
                    + Op.MSTORE(
                        offset=0x0, value=0x726576657274206D657373616765
                    )
                    + Op.REVERT(offset=0x100, size=0x0)
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
        "case10",
        "case11",
    ],
)
@pytest.mark.pre_alloc_mutable
def test_revert_opcode_return(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    tx_gas_limit: int,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xfaa10b404ab607779993c016cd5da73ae1f29d7e")
    contract = Address("0x1fc98371f1a058f1a6042e30a141aa8bb67dd1bc")
    callee = Address("0x1963fd2c717f5b4b9fa3d6baf38d66241e1ec005")
    callee_1 = Address("0x50eaca0a040ac6242d0c01cc1ff82f5b95cc10e4")
    callee_2 = Address("0x745e52346d8549444323699e9fc383ae89bdd24f")
    callee_3 = Address("0x858f82bbfd84fc9eb91291458511df77311dbd0d")
    callee_4 = Address("0xe5b2dfe7f932f2d5eaa7c8fb2e1e9a8b6a846fd7")
    callee_5 = Address("0xf933d2374d5875de033a8ed9d9c1ce5dea25c78b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
            + Op.MSTORE(offset=0x0, value=0x726576657274206D657373616765)
            + Op.REVERT(offset=0x0, size=0x20)
            + Op.STOP
        ),
    )
    # Source: LLL
    # { [[1]](CALL 150000 (CALLDATALOAD 0) 0 0 0 0 32) [[2]] (MLOAD 0) }
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(
                key=0x1,
                value=Op.CALL(
                    gas=0x249F0,
                    address=Op.CALLDATALOAD(offset=0x0),
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x20,
                ),
            )
            + Op.SSTORE(key=0x2, value=Op.MLOAD(offset=0x0))
            + Op.STOP
        ),
    )
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
            + Op.MSTORE(offset=0x0, value=0x726576657274206D657373616765)
            + Op.REVERT(offset=0x0, size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFF)
            + Op.STOP
        ),
    )
    pre[callee_2] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
            + Op.MSTORE(offset=0x0, value=0x726576657274206D657373616765)
            + Op.REVERT(offset=0x0, size=0x0)
            + Op.STOP
        ),
    )
    pre[callee_3] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
            + Op.MSTORE(offset=0x0, value=0x726576657274206D657373616765)
            + Op.REVERT(offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFF, size=0x0)
            + Op.STOP
        ),
    )
    pre[callee_4] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
            + Op.MSTORE(offset=0x0, value=0x726576657274206D657373616765)
            + Op.REVERT(offset=0x1, size=0x0)
            + Op.STOP
        ),
    )
    pre[callee_5] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=0x72657665727465642064617461)
            + Op.MSTORE(offset=0x0, value=0x726576657274206D657373616765)
            + Op.REVERT(offset=0x100, size=0x0)
            + Op.STOP
        ),
    )
    pre[sender] = Account(balance=0xE8D4A51000, nonce=0)

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x4f31b3206fbf0e0e598b9b1a7d8ac86302a0ff1d8930738f1bebae9b67173e52"  # noqa: E501
        ),
        to=contract,
        data=tx_data,
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
