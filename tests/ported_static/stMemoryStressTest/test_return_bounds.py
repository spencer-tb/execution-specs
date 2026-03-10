"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stMemoryStressTest/RETURN_BoundsFiller.json
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
    ["tests/static/state_tests/stMemoryStressTest/RETURN_BoundsFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit, expected_post",
    [
        (
            150000,
            {
                Address("0x07084994c5891b1467d74bedb0477da4909e4c0e"): Account(
                    code=Op.RETURN(offset=0xFFFFFFF, size=0xFFFFFFF) + Op.STOP
                ),
                Address("0x0b09ca4308585f026b8d02be147fea0739ec463a"): Account(
                    code=Op.RETURN(offset=0x0, size=0xFFFFFFFFFFFFFFFF)
                    + Op.STOP
                ),
                Address("0x2548bda95a3831abcd613f4d24e4634615a71cca"): Account(
                    code=Op.RETURN(
                        offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                        size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                    )
                    + Op.STOP
                ),
                Address("0x28463490948d21efc49949b4d394989bf52c57f1"): Account(
                    code=Op.RETURN(
                        offset=0x0,
                        size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                    )
                    + Op.STOP
                ),
                Address("0x2ceb88d6c420e5c65593d9ebed9a25600ab9e113"): Account(
                    code=Op.RETURN(offset=0x0, size=0xFFFFFFFF) + Op.STOP
                ),
                Address("0x416408c1d7fda274ddeb45ffe4817068808121ca"): Account(
                    code=Op.RETURN(
                        offset=0xFFFFFFFFFFFFFFFF, size=0xFFFFFFFFFFFFFFFF
                    )
                    + Op.STOP
                ),
                Address("0x4912bc7b66a3bf27adfa54ab049e90e8c9c4dc63"): Account(
                    code=Op.RETURN(
                        offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                        size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x5efbf04d8e1cc5b6b3719b16b5744a09bacfc18b"): Account(
                    code=Op.RETURN(offset=0x0, size=0x0) + Op.STOP
                ),
                Address("0x7266f1c07958d55ce36de0592604f1a915bdf1c2"): Account(
                    code=Op.RETURN(offset=0x0, size=0xFFFFFFF) + Op.STOP
                ),
                Address("0x76006c948f3a0529479c6d18a6f95908426e8092"): Account(
                    code=Op.RETURN(
                        offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                        size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                    )
                    + Op.STOP
                ),
                Address("0x7a4461ac9f9cd13f40f9514a7c60e23a71c1dff3"): Account(
                    code=Op.RETURN(
                        offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFF, size=0x0
                    )
                    + Op.STOP
                ),
                Address("0x7bbcf24c83493c4e733cb54079b51873d3211ad2"): Account(
                    code=Op.RETURN(offset=0xFFFFFFFFFFFFFFFF, size=0x0)
                    + Op.STOP
                ),
                Address("0xad7754a8a56cc5ad4e319fa94194e435628dee67"): Account(
                    code=Op.RETURN(offset=0xFFFFFFFF, size=0xFFFFFFFF)
                    + Op.STOP
                ),
                Address("0xc7aa750fe05c7e38475a49fe98a301024d0c1d54"): Account(
                    code=Op.RETURN(offset=0xFFFFFFF, size=0x0) + Op.STOP
                ),
                Address("0xd66a0237ee5d25106fc05bc767734bddba1fab35"): Account(
                    code=Op.SSTORE(
                        key=0x1,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x5EFBF04D8E1CC5B6B3719B16B5744A09BACFC18B,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0x2,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0xC7AA750FE05C7E38475A49FE98A301024D0C1D54,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0x3,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0xFF6B6D23BE161344E86EB7B174ACEDD4B1DC6DC7,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0x4,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x7BBCF24C83493C4E733CB54079B51873D3211AD2,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0x5,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x7A4461AC9F9CD13F40F9514A7C60E23A71C1DFF3,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0x6,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0x7,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0x8,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0x9,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0xA,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0xB,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0xC,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0xD,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0xE,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0xF,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0x10,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.STOP
                ),
                Address("0xf519de4dcb9aaa53f8f0db9b18c715c928caade8"): Account(
                    code=Op.RETURN(
                        offset=0x0, size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFF
                    )
                    + Op.STOP
                ),
                Address("0xff6b6d23be161344e86eb7b174acedd4b1dc6dc7"): Account(
                    code=Op.RETURN(offset=0xFFFFFFFF, size=0x0) + Op.STOP
                ),
            },
        ),
        (
            500000,
            {
                Address("0x07084994c5891b1467d74bedb0477da4909e4c0e"): Account(
                    code=Op.RETURN(offset=0xFFFFFFF, size=0xFFFFFFF) + Op.STOP
                ),
                Address("0x0b09ca4308585f026b8d02be147fea0739ec463a"): Account(
                    code=Op.RETURN(offset=0x0, size=0xFFFFFFFFFFFFFFFF)
                    + Op.STOP
                ),
                Address("0x2548bda95a3831abcd613f4d24e4634615a71cca"): Account(
                    code=Op.RETURN(
                        offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                        size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                    )
                    + Op.STOP
                ),
                Address("0x28463490948d21efc49949b4d394989bf52c57f1"): Account(
                    code=Op.RETURN(
                        offset=0x0,
                        size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                    )
                    + Op.STOP
                ),
                Address("0x2ceb88d6c420e5c65593d9ebed9a25600ab9e113"): Account(
                    code=Op.RETURN(offset=0x0, size=0xFFFFFFFF) + Op.STOP
                ),
                Address("0x416408c1d7fda274ddeb45ffe4817068808121ca"): Account(
                    code=Op.RETURN(
                        offset=0xFFFFFFFFFFFFFFFF, size=0xFFFFFFFFFFFFFFFF
                    )
                    + Op.STOP
                ),
                Address("0x4912bc7b66a3bf27adfa54ab049e90e8c9c4dc63"): Account(
                    code=Op.RETURN(
                        offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                        size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x5efbf04d8e1cc5b6b3719b16b5744a09bacfc18b"): Account(
                    code=Op.RETURN(offset=0x0, size=0x0) + Op.STOP
                ),
                Address("0x7266f1c07958d55ce36de0592604f1a915bdf1c2"): Account(
                    code=Op.RETURN(offset=0x0, size=0xFFFFFFF) + Op.STOP
                ),
                Address("0x76006c948f3a0529479c6d18a6f95908426e8092"): Account(
                    code=Op.RETURN(
                        offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                        size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                    )
                    + Op.STOP
                ),
                Address("0x7a4461ac9f9cd13f40f9514a7c60e23a71c1dff3"): Account(
                    code=Op.RETURN(
                        offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFF, size=0x0
                    )
                    + Op.STOP
                ),
                Address("0x7bbcf24c83493c4e733cb54079b51873d3211ad2"): Account(
                    code=Op.RETURN(offset=0xFFFFFFFFFFFFFFFF, size=0x0)
                    + Op.STOP
                ),
                Address("0xad7754a8a56cc5ad4e319fa94194e435628dee67"): Account(
                    code=Op.RETURN(offset=0xFFFFFFFF, size=0xFFFFFFFF)
                    + Op.STOP
                ),
                Address("0xc7aa750fe05c7e38475a49fe98a301024d0c1d54"): Account(
                    code=Op.RETURN(offset=0xFFFFFFF, size=0x0) + Op.STOP
                ),
                Address("0xd66a0237ee5d25106fc05bc767734bddba1fab35"): Account(
                    storage={
                        1: 1,
                        2: 1,
                        3: 1,
                        4: 1,
                        5: 1,
                        6: 1,
                        7: 1,
                        8: 1,
                        9: 1,
                        10: 1,
                        11: 1,
                        12: 1,
                        13: 1,
                        14: 1,
                        15: 1,
                        16: 1,
                    },
                    code=Op.SSTORE(
                        key=0x1,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x5EFBF04D8E1CC5B6B3719B16B5744A09BACFC18B,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0x2,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0xC7AA750FE05C7E38475A49FE98A301024D0C1D54,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0x3,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0xFF6B6D23BE161344E86EB7B174ACEDD4B1DC6DC7,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0x4,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x7BBCF24C83493C4E733CB54079B51873D3211AD2,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0x5,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x7A4461AC9F9CD13F40F9514A7C60E23A71C1DFF3,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0x6,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0x7,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0x8,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0x9,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0xA,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0xB,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0xC,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0xD,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0xE,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0xF,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0x10,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.STOP,
                ),
                Address("0xf519de4dcb9aaa53f8f0db9b18c715c928caade8"): Account(
                    code=Op.RETURN(
                        offset=0x0, size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFF
                    )
                    + Op.STOP
                ),
                Address("0xff6b6d23be161344e86eb7b174acedd4b1dc6dc7"): Account(
                    code=Op.RETURN(offset=0xFFFFFFFF, size=0x0) + Op.STOP
                ),
            },
        ),
        (
            15000000,
            {
                Address("0x07084994c5891b1467d74bedb0477da4909e4c0e"): Account(
                    code=Op.RETURN(offset=0xFFFFFFF, size=0xFFFFFFF) + Op.STOP
                ),
                Address("0x0b09ca4308585f026b8d02be147fea0739ec463a"): Account(
                    code=Op.RETURN(offset=0x0, size=0xFFFFFFFFFFFFFFFF)
                    + Op.STOP
                ),
                Address("0x2548bda95a3831abcd613f4d24e4634615a71cca"): Account(
                    code=Op.RETURN(
                        offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                        size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                    )
                    + Op.STOP
                ),
                Address("0x28463490948d21efc49949b4d394989bf52c57f1"): Account(
                    code=Op.RETURN(
                        offset=0x0,
                        size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                    )
                    + Op.STOP
                ),
                Address("0x2ceb88d6c420e5c65593d9ebed9a25600ab9e113"): Account(
                    code=Op.RETURN(offset=0x0, size=0xFFFFFFFF) + Op.STOP
                ),
                Address("0x416408c1d7fda274ddeb45ffe4817068808121ca"): Account(
                    code=Op.RETURN(
                        offset=0xFFFFFFFFFFFFFFFF, size=0xFFFFFFFFFFFFFFFF
                    )
                    + Op.STOP
                ),
                Address("0x4912bc7b66a3bf27adfa54ab049e90e8c9c4dc63"): Account(
                    code=Op.RETURN(
                        offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                        size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x5efbf04d8e1cc5b6b3719b16b5744a09bacfc18b"): Account(
                    code=Op.RETURN(offset=0x0, size=0x0) + Op.STOP
                ),
                Address("0x7266f1c07958d55ce36de0592604f1a915bdf1c2"): Account(
                    code=Op.RETURN(offset=0x0, size=0xFFFFFFF) + Op.STOP
                ),
                Address("0x76006c948f3a0529479c6d18a6f95908426e8092"): Account(
                    code=Op.RETURN(
                        offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                        size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                    )
                    + Op.STOP
                ),
                Address("0x7a4461ac9f9cd13f40f9514a7c60e23a71c1dff3"): Account(
                    code=Op.RETURN(
                        offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFF, size=0x0
                    )
                    + Op.STOP
                ),
                Address("0x7bbcf24c83493c4e733cb54079b51873d3211ad2"): Account(
                    code=Op.RETURN(offset=0xFFFFFFFFFFFFFFFF, size=0x0)
                    + Op.STOP
                ),
                Address("0xad7754a8a56cc5ad4e319fa94194e435628dee67"): Account(
                    code=Op.RETURN(offset=0xFFFFFFFF, size=0xFFFFFFFF)
                    + Op.STOP
                ),
                Address("0xc7aa750fe05c7e38475a49fe98a301024d0c1d54"): Account(
                    code=Op.RETURN(offset=0xFFFFFFF, size=0x0) + Op.STOP
                ),
                Address("0xd66a0237ee5d25106fc05bc767734bddba1fab35"): Account(
                    storage={
                        1: 1,
                        2: 1,
                        3: 1,
                        4: 1,
                        5: 1,
                        6: 1,
                        7: 1,
                        8: 1,
                        9: 1,
                        10: 1,
                        11: 1,
                        12: 1,
                        13: 1,
                        14: 1,
                        15: 1,
                        16: 1,
                    },
                    code=Op.SSTORE(
                        key=0x1,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x5EFBF04D8E1CC5B6B3719B16B5744A09BACFC18B,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0x2,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0xC7AA750FE05C7E38475A49FE98A301024D0C1D54,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0x3,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0xFF6B6D23BE161344E86EB7B174ACEDD4B1DC6DC7,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0x4,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x7BBCF24C83493C4E733CB54079B51873D3211AD2,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0x5,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x7A4461AC9F9CD13F40F9514A7C60E23A71C1DFF3,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0x6,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0x7,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0x8,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0x9,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0xA,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0xB,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0xC,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0xD,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0xE,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0xF,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0x10,
                        value=Op.CALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.STOP,
                ),
                Address("0xf519de4dcb9aaa53f8f0db9b18c715c928caade8"): Account(
                    code=Op.RETURN(
                        offset=0x0, size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFF
                    )
                    + Op.STOP
                ),
                Address("0xff6b6d23be161344e86eb7b174acedd4b1dc6dc7"): Account(
                    code=Op.RETURN(offset=0xFFFFFFFF, size=0x0) + Op.STOP
                ),
            },
        ),
    ],
    ids=["case0", "case1", "case2"],
)
@pytest.mark.pre_alloc_mutable
def test_return_bounds(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa99635038e8d9ab237a31179dd5c9087713f723a")
    contract = Address("0xd66a0237ee5d25106fc05bc767734bddba1fab35")
    callee = Address("0x07084994c5891b1467d74bedb0477da4909e4c0e")
    callee_1 = Address("0x0b09ca4308585f026b8d02be147fea0739ec463a")
    callee_2 = Address("0x2548bda95a3831abcd613f4d24e4634615a71cca")
    callee_3 = Address("0x28463490948d21efc49949b4d394989bf52c57f1")
    callee_4 = Address("0x2ceb88d6c420e5c65593d9ebed9a25600ab9e113")
    callee_5 = Address("0x416408c1d7fda274ddeb45ffe4817068808121ca")
    callee_6 = Address("0x4912bc7b66a3bf27adfa54ab049e90e8c9c4dc63")
    callee_7 = Address("0x5efbf04d8e1cc5b6b3719b16b5744a09bacfc18b")
    callee_8 = Address("0x7266f1c07958d55ce36de0592604f1a915bdf1c2")
    callee_9 = Address("0x76006c948f3a0529479c6d18a6f95908426e8092")
    callee_10 = Address("0x7a4461ac9f9cd13f40f9514a7c60e23a71c1dff3")
    callee_11 = Address("0x7bbcf24c83493c4e733cb54079b51873d3211ad2")
    callee_12 = Address("0xad7754a8a56cc5ad4e319fa94194e435628dee67")
    callee_13 = Address("0xc7aa750fe05c7e38475a49fe98a301024d0c1d54")
    callee_14 = Address("0xf519de4dcb9aaa53f8f0db9b18c715c928caade8")
    callee_15 = Address("0xff6b6d23be161344e86eb7b174acedd4b1dc6dc7")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=Op.RETURN(offset=0xFFFFFFF, size=0xFFFFFFF) + Op.STOP,
    )
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=Op.RETURN(offset=0x0, size=0xFFFFFFFFFFFFFFFF) + Op.STOP,
    )
    pre[callee_2] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.RETURN(
                offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFF,
            )
            + Op.STOP
        ),
    )
    pre[callee_3] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.RETURN(
                offset=0x0,
                size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
            )
            + Op.STOP
        ),
    )
    pre[callee_4] = Account(
        balance=0,
        nonce=0,
        code=Op.RETURN(offset=0x0, size=0xFFFFFFFF) + Op.STOP,
    )
    pre[callee_5] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.RETURN(offset=0xFFFFFFFFFFFFFFFF, size=0xFFFFFFFFFFFFFFFF)
            + Op.STOP
        ),
    )
    pre[callee_6] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.RETURN(
                offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                size=0x0,
            )
            + Op.STOP
        ),
    )
    pre[callee_7] = Account(
        balance=0,
        nonce=0,
        code=Op.RETURN(offset=0x0, size=0x0) + Op.STOP,
    )
    pre[callee_8] = Account(
        balance=0,
        nonce=0,
        code=Op.RETURN(offset=0x0, size=0xFFFFFFF) + Op.STOP,
    )
    pre[callee_9] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.RETURN(
                offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
            )
            + Op.STOP
        ),
    )
    pre[callee_10] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.RETURN(offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFF, size=0x0) + Op.STOP
        ),
    )
    pre[callee_11] = Account(
        balance=0,
        nonce=0,
        code=Op.RETURN(offset=0xFFFFFFFFFFFFFFFF, size=0x0) + Op.STOP,
    )
    pre[sender] = Account(
        balance=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
        nonce=0,
    )
    pre[callee_12] = Account(
        balance=0,
        nonce=0,
        code=Op.RETURN(offset=0xFFFFFFFF, size=0xFFFFFFFF) + Op.STOP,
    )
    pre[callee_13] = Account(
        balance=0,
        nonce=0,
        code=Op.RETURN(offset=0xFFFFFFF, size=0x0) + Op.STOP,
    )
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(
                key=0x1,
                value=Op.CALL(
                    gas=0x7FFFFFFFFFFFFFF,
                    address=0x5EFBF04D8E1CC5B6B3719B16B5744A09BACFC18B,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.SSTORE(
                key=0x2,
                value=Op.CALL(
                    gas=0x7FFFFFFFFFFFFFF,
                    address=0xC7AA750FE05C7E38475A49FE98A301024D0C1D54,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.SSTORE(
                key=0x3,
                value=Op.CALL(
                    gas=0x7FFFFFFFFFFFFFF,
                    address=0xFF6B6D23BE161344E86EB7B174ACEDD4B1DC6DC7,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.SSTORE(
                key=0x4,
                value=Op.CALL(
                    gas=0x7FFFFFFFFFFFFFF,
                    address=0x7BBCF24C83493C4E733CB54079B51873D3211AD2,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.SSTORE(
                key=0x5,
                value=Op.CALL(
                    gas=0x7FFFFFFFFFFFFFF,
                    address=0x7A4461AC9F9CD13F40F9514A7C60E23A71C1DFF3,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.SSTORE(
                key=0x6,
                value=Op.CALL(
                    gas=0x7FFFFFFFFFFFFFF,
                    address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.SSTORE(
                key=0x7,
                value=Op.CALL(
                    gas=0x7FFFFFFFFFFFFFF,
                    address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.SSTORE(
                key=0x8,
                value=Op.CALL(
                    gas=0x7FFFFFFFFFFFFFF,
                    address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.SSTORE(
                key=0x9,
                value=Op.CALL(
                    gas=0x7FFFFFFFFFFFFFF,
                    address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.SSTORE(
                key=0xA,
                value=Op.CALL(
                    gas=0x7FFFFFFFFFFFFFF,
                    address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.SSTORE(
                key=0xB,
                value=Op.CALL(
                    gas=0x7FFFFFFFFFFFFFF,
                    address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.SSTORE(
                key=0xC,
                value=Op.CALL(
                    gas=0x7FFFFFFFFFFFFFF,
                    address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.SSTORE(
                key=0xD,
                value=Op.CALL(
                    gas=0x7FFFFFFFFFFFFFF,
                    address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.SSTORE(
                key=0xE,
                value=Op.CALL(
                    gas=0x7FFFFFFFFFFFFFF,
                    address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.SSTORE(
                key=0xF,
                value=Op.CALL(
                    gas=0x7FFFFFFFFFFFFFF,
                    address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.SSTORE(
                key=0x10,
                value=Op.CALL(
                    gas=0x7FFFFFFFFFFFFFF,
                    address=0x4912BC7B66A3BF27ADFA54AB049E90E8C9C4DC63,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.STOP
        ),
    )
    pre[callee_14] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.RETURN(offset=0x0, size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFF) + Op.STOP
        ),
    )
    pre[callee_15] = Account(
        balance=0,
        nonce=0,
        code=Op.RETURN(offset=0xFFFFFFFF, size=0x0) + Op.STOP,
    )

    tx = Transaction(
        secret_key=Hash(
            "0x50eadfb1030587ab3a993a6ecc073041fc3b45e119daa31a13d78c7e209631a5"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
