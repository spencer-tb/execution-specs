"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stCreateTest/CreateOOGFromCallRefundsFiller.yml
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

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


@pytest.mark.ported_from(
    [
        "tests/static/state_tests/stCreateTest/CreateOOGFromCallRefundsFiller.yml",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000006a",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000001a"): Account(
                    code=bytes.fromhex("60016000818155808255f3")
                ),
                Address("0x000000000000000000000000000000000000001b"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000001c"): Account(
                    code=bytes.fromhex("600160008181559055fe")
                ),
                Address("0x000000000000000000000000000000000000002a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000003a"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af460016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003b"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af46113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af450fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000004a"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af260016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000004b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af26113886000f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000004c"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af250fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000005a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000006a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000007a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082558190620c0de1803b91829181903c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007c"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556000620c0de181813b9283923c600080f050fe"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082557f6001600055600060005560016000f3000000000000000000000000000000000081528190600f90818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c6000818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000600155600080620c0de181813b9283923c8180f550fe"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000c0de0"): Account(
                    storage={1: 1},
                    code=bytes.fromhex(
                        "60ff60005260206000a060fa60206000a160fb60fa60206000a260fc60fb60fa60206000a360fd60fc60fb60fa60206000a400"  # noqa: E501
                    ),
                ),
                Address("0x00000000000000000000000000000000000c0de1"): Account(
                    code=bytes.fromhex("6000808055600190f3")
                ),
                Address("0x00000000000000000000000000000000000c0dea"): Account(
                    storage={1: 1}, code=bytes.fromhex("600060015500")
                ),
                Address("0x00000000000000000000000000000000000c0ded"): Account(
                    storage={1: 1}, code=bytes.fromhex("32ff")
                ),
                Address("0x4501f8fa1e67827ebfb1f6d5510c606871c5a599"): Account(
                    storage={0: 1}, code=bytes.fromhex("00")
                ),
                Address("0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"): Account(
                    code=bytes.fromhex(
                        "60008060043581813b9283923c8180f014601557005bfe"
                    )
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000006c",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000001a"): Account(
                    code=bytes.fromhex("60016000818155808255f3")
                ),
                Address("0x000000000000000000000000000000000000001b"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000001c"): Account(
                    code=bytes.fromhex("600160008181559055fe")
                ),
                Address("0x000000000000000000000000000000000000002a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000003a"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af460016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003b"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af46113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af450fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000004a"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af260016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000004b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af26113886000f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000004c"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af250fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000005a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000006a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000007a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082558190620c0de1803b91829181903c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007c"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556000620c0de181813b9283923c600080f050fe"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082557f6001600055600060005560016000f3000000000000000000000000000000000081528190600f90818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c6000818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000600155600080620c0de181813b9283923c8180f550fe"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000c0de0"): Account(
                    storage={1: 1},
                    code=bytes.fromhex(
                        "60ff60005260206000a060fa60206000a160fb60fa60206000a260fc60fb60fa60206000a360fd60fc60fb60fa60206000a400"  # noqa: E501
                    ),
                ),
                Address("0x00000000000000000000000000000000000c0de1"): Account(
                    code=bytes.fromhex("6000808055600190f3")
                ),
                Address("0x00000000000000000000000000000000000c0dea"): Account(
                    storage={1: 1}, code=bytes.fromhex("600060015500")
                ),
                Address("0x00000000000000000000000000000000000c0ded"): Account(
                    storage={1: 1}, code=bytes.fromhex("32ff")
                ),
                Address("0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"): Account(
                    code=bytes.fromhex(
                        "60008060043581813b9283923c8180f014601557005bfe"
                    )
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000006b",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000001a"): Account(
                    code=bytes.fromhex("60016000818155808255f3")
                ),
                Address("0x000000000000000000000000000000000000001b"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000001c"): Account(
                    code=bytes.fromhex("600160008181559055fe")
                ),
                Address("0x000000000000000000000000000000000000002a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000003a"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af460016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003b"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af46113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af450fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000004a"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af260016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000004b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af26113886000f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000004c"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af250fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000005a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000006a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000007a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082558190620c0de1803b91829181903c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007c"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556000620c0de181813b9283923c600080f050fe"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082557f6001600055600060005560016000f3000000000000000000000000000000000081528190600f90818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c6000818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000600155600080620c0de181813b9283923c8180f550fe"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000c0de0"): Account(
                    storage={1: 1},
                    code=bytes.fromhex(
                        "60ff60005260206000a060fa60206000a160fb60fa60206000a260fc60fb60fa60206000a360fd60fc60fb60fa60206000a400"  # noqa: E501
                    ),
                ),
                Address("0x00000000000000000000000000000000000c0de1"): Account(
                    code=bytes.fromhex("6000808055600190f3")
                ),
                Address("0x00000000000000000000000000000000000c0dea"): Account(
                    storage={1: 1}, code=bytes.fromhex("600060015500")
                ),
                Address("0x00000000000000000000000000000000000c0ded"): Account(
                    storage={1: 1}, code=bytes.fromhex("32ff")
                ),
                Address("0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"): Account(
                    code=bytes.fromhex(
                        "60008060043581813b9283923c8180f014601557005bfe"
                    )
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000008a",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000001a"): Account(
                    code=bytes.fromhex("60016000818155808255f3")
                ),
                Address("0x000000000000000000000000000000000000001b"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000001c"): Account(
                    code=bytes.fromhex("600160008181559055fe")
                ),
                Address("0x000000000000000000000000000000000000002a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000003a"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af460016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003b"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af46113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af450fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000004a"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af260016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000004b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af26113886000f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000004c"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af250fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000005a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000006a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000007a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082558190620c0de1803b91829181903c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007c"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556000620c0de181813b9283923c600080f050fe"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082557f6001600055600060005560016000f3000000000000000000000000000000000081528190600f90818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c6000818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000600155600080620c0de181813b9283923c8180f550fe"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000c0de0"): Account(
                    storage={1: 1},
                    code=bytes.fromhex(
                        "60ff60005260206000a060fa60206000a160fb60fa60206000a260fc60fb60fa60206000a360fd60fc60fb60fa60206000a400"  # noqa: E501
                    ),
                ),
                Address("0x00000000000000000000000000000000000c0de1"): Account(
                    code=bytes.fromhex("6000808055600190f3")
                ),
                Address("0x00000000000000000000000000000000000c0dea"): Account(
                    storage={1: 1}, code=bytes.fromhex("600060015500")
                ),
                Address("0x00000000000000000000000000000000000c0ded"): Account(
                    storage={1: 1}, code=bytes.fromhex("32ff")
                ),
                Address("0x06019547b6e360abdafeade158a9667cc6106c17"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0x4501f8fa1e67827ebfb1f6d5510c606871c5a599"): Account(
                    storage={0: 1}, code=bytes.fromhex("00")
                ),
                Address("0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"): Account(
                    code=bytes.fromhex(
                        "60008060043581813b9283923c8180f014601557005bfe"
                    )
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000008c",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000001a"): Account(
                    code=bytes.fromhex("60016000818155808255f3")
                ),
                Address("0x000000000000000000000000000000000000001b"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000001c"): Account(
                    code=bytes.fromhex("600160008181559055fe")
                ),
                Address("0x000000000000000000000000000000000000002a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000003a"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af460016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003b"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af46113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af450fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000004a"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af260016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000004b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af26113886000f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000004c"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af250fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000005a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000006a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000007a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082558190620c0de1803b91829181903c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007c"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556000620c0de181813b9283923c600080f050fe"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082557f6001600055600060005560016000f3000000000000000000000000000000000081528190600f90818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c6000818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000600155600080620c0de181813b9283923c8180f550fe"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000c0de0"): Account(
                    storage={1: 1},
                    code=bytes.fromhex(
                        "60ff60005260206000a060fa60206000a160fb60fa60206000a260fc60fb60fa60206000a360fd60fc60fb60fa60206000a400"  # noqa: E501
                    ),
                ),
                Address("0x00000000000000000000000000000000000c0de1"): Account(
                    code=bytes.fromhex("6000808055600190f3")
                ),
                Address("0x00000000000000000000000000000000000c0dea"): Account(
                    storage={1: 1}, code=bytes.fromhex("600060015500")
                ),
                Address("0x00000000000000000000000000000000000c0ded"): Account(
                    storage={1: 1}, code=bytes.fromhex("32ff")
                ),
                Address("0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"): Account(
                    code=bytes.fromhex(
                        "60008060043581813b9283923c8180f014601557005bfe"
                    )
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000008b",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000001a"): Account(
                    code=bytes.fromhex("60016000818155808255f3")
                ),
                Address("0x000000000000000000000000000000000000001b"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000001c"): Account(
                    code=bytes.fromhex("600160008181559055fe")
                ),
                Address("0x000000000000000000000000000000000000002a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000003a"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af460016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003b"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af46113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af450fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000004a"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af260016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000004b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af26113886000f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000004c"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af250fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000005a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000006a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000007a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082558190620c0de1803b91829181903c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007c"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556000620c0de181813b9283923c600080f050fe"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082557f6001600055600060005560016000f3000000000000000000000000000000000081528190600f90818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c6000818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000600155600080620c0de181813b9283923c8180f550fe"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000c0de0"): Account(
                    storage={1: 1},
                    code=bytes.fromhex(
                        "60ff60005260206000a060fa60206000a160fb60fa60206000a260fc60fb60fa60206000a360fd60fc60fb60fa60206000a400"  # noqa: E501
                    ),
                ),
                Address("0x00000000000000000000000000000000000c0de1"): Account(
                    code=bytes.fromhex("6000808055600190f3")
                ),
                Address("0x00000000000000000000000000000000000c0dea"): Account(
                    storage={1: 1}, code=bytes.fromhex("600060015500")
                ),
                Address("0x00000000000000000000000000000000000c0ded"): Account(
                    storage={1: 1}, code=bytes.fromhex("32ff")
                ),
                Address("0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"): Account(
                    code=bytes.fromhex(
                        "60008060043581813b9283923c8180f014601557005bfe"
                    )
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000007a",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000001a"): Account(
                    code=bytes.fromhex("60016000818155808255f3")
                ),
                Address("0x000000000000000000000000000000000000001b"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000001c"): Account(
                    code=bytes.fromhex("600160008181559055fe")
                ),
                Address("0x000000000000000000000000000000000000002a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000003a"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af460016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003b"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af46113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af450fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000004a"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af260016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000004b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af26113886000f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000004c"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af250fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000005a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000006a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000007a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082558190620c0de1803b91829181903c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007c"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556000620c0de181813b9283923c600080f050fe"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082557f6001600055600060005560016000f3000000000000000000000000000000000081528190600f90818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c6000818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000600155600080620c0de181813b9283923c8180f550fe"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000c0de0"): Account(
                    storage={1: 1},
                    code=bytes.fromhex(
                        "60ff60005260206000a060fa60206000a160fb60fa60206000a260fc60fb60fa60206000a360fd60fc60fb60fa60206000a400"  # noqa: E501
                    ),
                ),
                Address("0x00000000000000000000000000000000000c0de1"): Account(
                    code=bytes.fromhex("6000808055600190f3")
                ),
                Address("0x00000000000000000000000000000000000c0dea"): Account(
                    storage={1: 1}, code=bytes.fromhex("600060015500")
                ),
                Address("0x00000000000000000000000000000000000c0ded"): Account(
                    storage={1: 1}, code=bytes.fromhex("32ff")
                ),
                Address("0x4501f8fa1e67827ebfb1f6d5510c606871c5a599"): Account(
                    storage={0: 1}, code=bytes.fromhex("00")
                ),
                Address("0x522c2e1c5da65010908ef9929e327fe8b6cc86da"): Account(
                    code=bytes.fromhex("00")
                ),
                Address("0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"): Account(
                    code=bytes.fromhex(
                        "60008060043581813b9283923c8180f014601557005bfe"
                    )
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000007c",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000001a"): Account(
                    code=bytes.fromhex("60016000818155808255f3")
                ),
                Address("0x000000000000000000000000000000000000001b"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000001c"): Account(
                    code=bytes.fromhex("600160008181559055fe")
                ),
                Address("0x000000000000000000000000000000000000002a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000003a"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af460016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003b"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af46113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af450fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000004a"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af260016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000004b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af26113886000f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000004c"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af250fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000005a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000006a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000007a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082558190620c0de1803b91829181903c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007c"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556000620c0de181813b9283923c600080f050fe"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082557f6001600055600060005560016000f3000000000000000000000000000000000081528190600f90818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c6000818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000600155600080620c0de181813b9283923c8180f550fe"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000c0de0"): Account(
                    storage={1: 1},
                    code=bytes.fromhex(
                        "60ff60005260206000a060fa60206000a160fb60fa60206000a260fc60fb60fa60206000a360fd60fc60fb60fa60206000a400"  # noqa: E501
                    ),
                ),
                Address("0x00000000000000000000000000000000000c0de1"): Account(
                    code=bytes.fromhex("6000808055600190f3")
                ),
                Address("0x00000000000000000000000000000000000c0dea"): Account(
                    storage={1: 1}, code=bytes.fromhex("600060015500")
                ),
                Address("0x00000000000000000000000000000000000c0ded"): Account(
                    storage={1: 1}, code=bytes.fromhex("32ff")
                ),
                Address("0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"): Account(
                    code=bytes.fromhex(
                        "60008060043581813b9283923c8180f014601557005bfe"
                    )
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000007b",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000001a"): Account(
                    code=bytes.fromhex("60016000818155808255f3")
                ),
                Address("0x000000000000000000000000000000000000001b"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000001c"): Account(
                    code=bytes.fromhex("600160008181559055fe")
                ),
                Address("0x000000000000000000000000000000000000002a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000003a"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af460016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003b"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af46113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af450fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000004a"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af260016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000004b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af26113886000f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000004c"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af250fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000005a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000006a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000007a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082558190620c0de1803b91829181903c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007c"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556000620c0de181813b9283923c600080f050fe"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082557f6001600055600060005560016000f3000000000000000000000000000000000081528190600f90818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c6000818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000600155600080620c0de181813b9283923c8180f550fe"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000c0de0"): Account(
                    storage={1: 1},
                    code=bytes.fromhex(
                        "60ff60005260206000a060fa60206000a160fb60fa60206000a260fc60fb60fa60206000a360fd60fc60fb60fa60206000a400"  # noqa: E501
                    ),
                ),
                Address("0x00000000000000000000000000000000000c0de1"): Account(
                    code=bytes.fromhex("6000808055600190f3")
                ),
                Address("0x00000000000000000000000000000000000c0dea"): Account(
                    storage={1: 1}, code=bytes.fromhex("600060015500")
                ),
                Address("0x00000000000000000000000000000000000c0ded"): Account(
                    storage={1: 1}, code=bytes.fromhex("32ff")
                ),
                Address("0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"): Account(
                    code=bytes.fromhex(
                        "60008060043581813b9283923c8180f014601557005bfe"
                    )
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000002a",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000001a"): Account(
                    code=bytes.fromhex("60016000818155808255f3")
                ),
                Address("0x000000000000000000000000000000000000001b"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000001c"): Account(
                    code=bytes.fromhex("600160008181559055fe")
                ),
                Address("0x000000000000000000000000000000000000002a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000003a"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af460016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003b"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af46113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af450fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000004a"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af260016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000004b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af26113886000f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000004c"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af250fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000005a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000006a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000007a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082558190620c0de1803b91829181903c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007c"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556000620c0de181813b9283923c600080f050fe"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082557f6001600055600060005560016000f3000000000000000000000000000000000081528190600f90818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c6000818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000600155600080620c0de181813b9283923c8180f550fe"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000c0de0"): Account(
                    storage={1: 1},
                    code=bytes.fromhex(
                        "60ff60005260206000a060fa60206000a160fb60fa60206000a260fc60fb60fa60206000a360fd60fc60fb60fa60206000a400"  # noqa: E501
                    ),
                ),
                Address("0x00000000000000000000000000000000000c0de1"): Account(
                    code=bytes.fromhex("6000808055600190f3")
                ),
                Address("0x00000000000000000000000000000000000c0dea"): Account(
                    code=bytes.fromhex("600060015500")
                ),
                Address("0x00000000000000000000000000000000000c0ded"): Account(
                    storage={1: 1}, code=bytes.fromhex("32ff")
                ),
                Address("0x4501f8fa1e67827ebfb1f6d5510c606871c5a599"): Account(
                    storage={0: 1}, code=bytes.fromhex("00")
                ),
                Address("0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"): Account(
                    code=bytes.fromhex(
                        "60008060043581813b9283923c8180f014601557005bfe"
                    )
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000003a",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000001a"): Account(
                    code=bytes.fromhex("60016000818155808255f3")
                ),
                Address("0x000000000000000000000000000000000000001b"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000001c"): Account(
                    code=bytes.fromhex("600160008181559055fe")
                ),
                Address("0x000000000000000000000000000000000000002a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000003a"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af460016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003b"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af46113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af450fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000004a"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af260016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000004b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af26113886000f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000004c"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af250fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000005a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000006a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000007a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082558190620c0de1803b91829181903c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007c"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556000620c0de181813b9283923c600080f050fe"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082557f6001600055600060005560016000f3000000000000000000000000000000000081528190600f90818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c6000818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000600155600080620c0de181813b9283923c8180f550fe"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000c0de0"): Account(
                    storage={1: 1},
                    code=bytes.fromhex(
                        "60ff60005260206000a060fa60206000a160fb60fa60206000a260fc60fb60fa60206000a360fd60fc60fb60fa60206000a400"  # noqa: E501
                    ),
                ),
                Address("0x00000000000000000000000000000000000c0de1"): Account(
                    code=bytes.fromhex("6000808055600190f3")
                ),
                Address("0x00000000000000000000000000000000000c0dea"): Account(
                    storage={1: 1}, code=bytes.fromhex("600060015500")
                ),
                Address("0x00000000000000000000000000000000000c0ded"): Account(
                    storage={1: 1}, code=bytes.fromhex("32ff")
                ),
                Address("0x4501f8fa1e67827ebfb1f6d5510c606871c5a599"): Account(
                    storage={0: 1}, code=bytes.fromhex("00")
                ),
                Address("0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"): Account(
                    code=bytes.fromhex(
                        "60008060043581813b9283923c8180f014601557005bfe"
                    )
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000004a",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000001a"): Account(
                    code=bytes.fromhex("60016000818155808255f3")
                ),
                Address("0x000000000000000000000000000000000000001b"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000001c"): Account(
                    code=bytes.fromhex("600160008181559055fe")
                ),
                Address("0x000000000000000000000000000000000000002a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000003a"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af460016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003b"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af46113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af450fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000004a"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af260016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000004b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af26113886000f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000004c"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af250fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000005a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000006a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000007a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082558190620c0de1803b91829181903c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007c"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556000620c0de181813b9283923c600080f050fe"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082557f6001600055600060005560016000f3000000000000000000000000000000000081528190600f90818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c6000818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000600155600080620c0de181813b9283923c8180f550fe"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000c0de0"): Account(
                    storage={1: 1},
                    code=bytes.fromhex(
                        "60ff60005260206000a060fa60206000a160fb60fa60206000a260fc60fb60fa60206000a360fd60fc60fb60fa60206000a400"  # noqa: E501
                    ),
                ),
                Address("0x00000000000000000000000000000000000c0de1"): Account(
                    code=bytes.fromhex("6000808055600190f3")
                ),
                Address("0x00000000000000000000000000000000000c0dea"): Account(
                    storage={1: 1}, code=bytes.fromhex("600060015500")
                ),
                Address("0x00000000000000000000000000000000000c0ded"): Account(
                    storage={1: 1}, code=bytes.fromhex("32ff")
                ),
                Address("0x4501f8fa1e67827ebfb1f6d5510c606871c5a599"): Account(
                    storage={0: 1}, code=bytes.fromhex("00")
                ),
                Address("0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"): Account(
                    code=bytes.fromhex(
                        "60008060043581813b9283923c8180f014601557005bfe"
                    )
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000001a",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000001a"): Account(
                    code=bytes.fromhex("60016000818155808255f3")
                ),
                Address("0x000000000000000000000000000000000000001b"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000001c"): Account(
                    code=bytes.fromhex("600160008181559055fe")
                ),
                Address("0x000000000000000000000000000000000000002a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000003a"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af460016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003b"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af46113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af450fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000004a"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af260016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000004b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af26113886000f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000004c"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af250fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000005a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000006a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000007a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082558190620c0de1803b91829181903c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007c"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556000620c0de181813b9283923c600080f050fe"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082557f6001600055600060005560016000f3000000000000000000000000000000000081528190600f90818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c6000818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000600155600080620c0de181813b9283923c8180f550fe"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000c0de0"): Account(
                    storage={1: 1},
                    code=bytes.fromhex(
                        "60ff60005260206000a060fa60206000a160fb60fa60206000a260fc60fb60fa60206000a360fd60fc60fb60fa60206000a400"  # noqa: E501
                    ),
                ),
                Address("0x00000000000000000000000000000000000c0de1"): Account(
                    code=bytes.fromhex("6000808055600190f3")
                ),
                Address("0x00000000000000000000000000000000000c0dea"): Account(
                    storage={1: 1}, code=bytes.fromhex("600060015500")
                ),
                Address("0x00000000000000000000000000000000000c0ded"): Account(
                    storage={1: 1}, code=bytes.fromhex("32ff")
                ),
                Address("0x4501f8fa1e67827ebfb1f6d5510c606871c5a599"): Account(
                    storage={0: 1}, code=bytes.fromhex("00")
                ),
                Address("0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"): Account(
                    code=bytes.fromhex(
                        "60008060043581813b9283923c8180f014601557005bfe"
                    )
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000001c",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000001a"): Account(
                    code=bytes.fromhex("60016000818155808255f3")
                ),
                Address("0x000000000000000000000000000000000000001b"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000001c"): Account(
                    code=bytes.fromhex("600160008181559055fe")
                ),
                Address("0x000000000000000000000000000000000000002a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000003a"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af460016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003b"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af46113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af450fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000004a"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af260016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000004b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af26113886000f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000004c"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af250fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000005a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000006a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000007a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082558190620c0de1803b91829181903c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007c"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556000620c0de181813b9283923c600080f050fe"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082557f6001600055600060005560016000f3000000000000000000000000000000000081528190600f90818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c6000818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000600155600080620c0de181813b9283923c8180f550fe"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000c0de0"): Account(
                    storage={1: 1},
                    code=bytes.fromhex(
                        "60ff60005260206000a060fa60206000a160fb60fa60206000a260fc60fb60fa60206000a360fd60fc60fb60fa60206000a400"  # noqa: E501
                    ),
                ),
                Address("0x00000000000000000000000000000000000c0de1"): Account(
                    code=bytes.fromhex("6000808055600190f3")
                ),
                Address("0x00000000000000000000000000000000000c0dea"): Account(
                    storage={1: 1}, code=bytes.fromhex("600060015500")
                ),
                Address("0x00000000000000000000000000000000000c0ded"): Account(
                    storage={1: 1}, code=bytes.fromhex("32ff")
                ),
                Address("0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"): Account(
                    code=bytes.fromhex(
                        "60008060043581813b9283923c8180f014601557005bfe"
                    )
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000002b",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000001a"): Account(
                    code=bytes.fromhex("60016000818155808255f3")
                ),
                Address("0x000000000000000000000000000000000000001b"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000001c"): Account(
                    code=bytes.fromhex("600160008181559055fe")
                ),
                Address("0x000000000000000000000000000000000000002a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000003a"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af460016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003b"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af46113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af450fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000004a"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af260016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000004b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af26113886000f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000004c"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af250fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000005a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000006a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000007a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082558190620c0de1803b91829181903c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007c"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556000620c0de181813b9283923c600080f050fe"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082557f6001600055600060005560016000f3000000000000000000000000000000000081528190600f90818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c6000818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000600155600080620c0de181813b9283923c8180f550fe"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000c0de0"): Account(
                    storage={1: 1},
                    code=bytes.fromhex(
                        "60ff60005260206000a060fa60206000a160fb60fa60206000a260fc60fb60fa60206000a360fd60fc60fb60fa60206000a400"  # noqa: E501
                    ),
                ),
                Address("0x00000000000000000000000000000000000c0de1"): Account(
                    code=bytes.fromhex("6000808055600190f3")
                ),
                Address("0x00000000000000000000000000000000000c0dea"): Account(
                    storage={1: 1}, code=bytes.fromhex("600060015500")
                ),
                Address("0x00000000000000000000000000000000000c0ded"): Account(
                    storage={1: 1}, code=bytes.fromhex("32ff")
                ),
                Address("0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"): Account(
                    code=bytes.fromhex(
                        "60008060043581813b9283923c8180f014601557005bfe"
                    )
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000002c",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000001a"): Account(
                    code=bytes.fromhex("60016000818155808255f3")
                ),
                Address("0x000000000000000000000000000000000000001b"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000001c"): Account(
                    code=bytes.fromhex("600160008181559055fe")
                ),
                Address("0x000000000000000000000000000000000000002a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000003a"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af460016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003b"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af46113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af450fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000004a"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af260016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000004b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af26113886000f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000004c"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af250fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000005a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000006a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000007a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082558190620c0de1803b91829181903c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007c"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556000620c0de181813b9283923c600080f050fe"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082557f6001600055600060005560016000f3000000000000000000000000000000000081528190600f90818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c6000818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000600155600080620c0de181813b9283923c8180f550fe"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000c0de0"): Account(
                    storage={1: 1},
                    code=bytes.fromhex(
                        "60ff60005260206000a060fa60206000a160fb60fa60206000a260fc60fb60fa60206000a360fd60fc60fb60fa60206000a400"  # noqa: E501
                    ),
                ),
                Address("0x00000000000000000000000000000000000c0de1"): Account(
                    code=bytes.fromhex("6000808055600190f3")
                ),
                Address("0x00000000000000000000000000000000000c0dea"): Account(
                    storage={1: 1}, code=bytes.fromhex("600060015500")
                ),
                Address("0x00000000000000000000000000000000000c0ded"): Account(
                    storage={1: 1}, code=bytes.fromhex("32ff")
                ),
                Address("0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"): Account(
                    code=bytes.fromhex(
                        "60008060043581813b9283923c8180f014601557005bfe"
                    )
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000003b",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000001a"): Account(
                    code=bytes.fromhex("60016000818155808255f3")
                ),
                Address("0x000000000000000000000000000000000000001b"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000001c"): Account(
                    code=bytes.fromhex("600160008181559055fe")
                ),
                Address("0x000000000000000000000000000000000000002a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000003a"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af460016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003b"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af46113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af450fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000004a"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af260016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000004b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af26113886000f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000004c"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af250fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000005a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000006a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000007a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082558190620c0de1803b91829181903c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007c"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556000620c0de181813b9283923c600080f050fe"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082557f6001600055600060005560016000f3000000000000000000000000000000000081528190600f90818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c6000818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000600155600080620c0de181813b9283923c8180f550fe"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000c0de0"): Account(
                    storage={1: 1},
                    code=bytes.fromhex(
                        "60ff60005260206000a060fa60206000a160fb60fa60206000a260fc60fb60fa60206000a360fd60fc60fb60fa60206000a400"  # noqa: E501
                    ),
                ),
                Address("0x00000000000000000000000000000000000c0de1"): Account(
                    code=bytes.fromhex("6000808055600190f3")
                ),
                Address("0x00000000000000000000000000000000000c0dea"): Account(
                    storage={1: 1}, code=bytes.fromhex("600060015500")
                ),
                Address("0x00000000000000000000000000000000000c0ded"): Account(
                    storage={1: 1}, code=bytes.fromhex("32ff")
                ),
                Address("0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"): Account(
                    code=bytes.fromhex(
                        "60008060043581813b9283923c8180f014601557005bfe"
                    )
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000003c",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000001a"): Account(
                    code=bytes.fromhex("60016000818155808255f3")
                ),
                Address("0x000000000000000000000000000000000000001b"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000001c"): Account(
                    code=bytes.fromhex("600160008181559055fe")
                ),
                Address("0x000000000000000000000000000000000000002a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000003a"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af460016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003b"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af46113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af450fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000004a"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af260016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000004b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af26113886000f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000004c"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af250fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000005a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000006a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000007a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082558190620c0de1803b91829181903c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007c"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556000620c0de181813b9283923c600080f050fe"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082557f6001600055600060005560016000f3000000000000000000000000000000000081528190600f90818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c6000818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000600155600080620c0de181813b9283923c8180f550fe"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000c0de0"): Account(
                    storage={1: 1},
                    code=bytes.fromhex(
                        "60ff60005260206000a060fa60206000a160fb60fa60206000a260fc60fb60fa60206000a360fd60fc60fb60fa60206000a400"  # noqa: E501
                    ),
                ),
                Address("0x00000000000000000000000000000000000c0de1"): Account(
                    code=bytes.fromhex("6000808055600190f3")
                ),
                Address("0x00000000000000000000000000000000000c0dea"): Account(
                    storage={1: 1}, code=bytes.fromhex("600060015500")
                ),
                Address("0x00000000000000000000000000000000000c0ded"): Account(
                    storage={1: 1}, code=bytes.fromhex("32ff")
                ),
                Address("0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"): Account(
                    code=bytes.fromhex(
                        "60008060043581813b9283923c8180f014601557005bfe"
                    )
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000004b",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000001a"): Account(
                    code=bytes.fromhex("60016000818155808255f3")
                ),
                Address("0x000000000000000000000000000000000000001b"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000001c"): Account(
                    code=bytes.fromhex("600160008181559055fe")
                ),
                Address("0x000000000000000000000000000000000000002a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000003a"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af460016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003b"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af46113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af450fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000004a"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af260016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000004b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af26113886000f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000004c"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af250fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000005a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000006a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000007a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082558190620c0de1803b91829181903c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007c"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556000620c0de181813b9283923c600080f050fe"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082557f6001600055600060005560016000f3000000000000000000000000000000000081528190600f90818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c6000818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000600155600080620c0de181813b9283923c8180f550fe"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000c0de0"): Account(
                    storage={1: 1},
                    code=bytes.fromhex(
                        "60ff60005260206000a060fa60206000a160fb60fa60206000a260fc60fb60fa60206000a360fd60fc60fb60fa60206000a400"  # noqa: E501
                    ),
                ),
                Address("0x00000000000000000000000000000000000c0de1"): Account(
                    code=bytes.fromhex("6000808055600190f3")
                ),
                Address("0x00000000000000000000000000000000000c0dea"): Account(
                    storage={1: 1}, code=bytes.fromhex("600060015500")
                ),
                Address("0x00000000000000000000000000000000000c0ded"): Account(
                    storage={1: 1}, code=bytes.fromhex("32ff")
                ),
                Address("0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"): Account(
                    code=bytes.fromhex(
                        "60008060043581813b9283923c8180f014601557005bfe"
                    )
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000004c",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000001a"): Account(
                    code=bytes.fromhex("60016000818155808255f3")
                ),
                Address("0x000000000000000000000000000000000000001b"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000001c"): Account(
                    code=bytes.fromhex("600160008181559055fe")
                ),
                Address("0x000000000000000000000000000000000000002a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000003a"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af460016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003b"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af46113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af450fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000004a"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af260016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000004b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af26113886000f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000004c"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af250fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000005a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000006a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000007a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082558190620c0de1803b91829181903c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007c"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556000620c0de181813b9283923c600080f050fe"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082557f6001600055600060005560016000f3000000000000000000000000000000000081528190600f90818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c6000818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000600155600080620c0de181813b9283923c8180f550fe"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000c0de0"): Account(
                    storage={1: 1},
                    code=bytes.fromhex(
                        "60ff60005260206000a060fa60206000a160fb60fa60206000a260fc60fb60fa60206000a360fd60fc60fb60fa60206000a400"  # noqa: E501
                    ),
                ),
                Address("0x00000000000000000000000000000000000c0de1"): Account(
                    code=bytes.fromhex("6000808055600190f3")
                ),
                Address("0x00000000000000000000000000000000000c0dea"): Account(
                    storage={1: 1}, code=bytes.fromhex("600060015500")
                ),
                Address("0x00000000000000000000000000000000000c0ded"): Account(
                    storage={1: 1}, code=bytes.fromhex("32ff")
                ),
                Address("0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"): Account(
                    code=bytes.fromhex(
                        "60008060043581813b9283923c8180f014601557005bfe"
                    )
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000001b",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000001a"): Account(
                    code=bytes.fromhex("60016000818155808255f3")
                ),
                Address("0x000000000000000000000000000000000000001b"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000001c"): Account(
                    code=bytes.fromhex("600160008181559055fe")
                ),
                Address("0x000000000000000000000000000000000000002a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000003a"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af460016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003b"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af46113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af450fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000004a"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af260016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000004b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af26113886000f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000004c"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af250fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000005a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000006a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000007a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082558190620c0de1803b91829181903c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007c"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556000620c0de181813b9283923c600080f050fe"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082557f6001600055600060005560016000f3000000000000000000000000000000000081528190600f90818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c6000818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000600155600080620c0de181813b9283923c8180f550fe"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000c0de0"): Account(
                    storage={1: 1},
                    code=bytes.fromhex(
                        "60ff60005260206000a060fa60206000a160fb60fa60206000a260fc60fb60fa60206000a360fd60fc60fb60fa60206000a400"  # noqa: E501
                    ),
                ),
                Address("0x00000000000000000000000000000000000c0de1"): Account(
                    code=bytes.fromhex("6000808055600190f3")
                ),
                Address("0x00000000000000000000000000000000000c0dea"): Account(
                    storage={1: 1}, code=bytes.fromhex("600060015500")
                ),
                Address("0x00000000000000000000000000000000000c0ded"): Account(
                    storage={1: 1}, code=bytes.fromhex("32ff")
                ),
                Address("0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"): Account(
                    code=bytes.fromhex(
                        "60008060043581813b9283923c8180f014601557005bfe"
                    )
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000005a",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000001a"): Account(
                    code=bytes.fromhex("60016000818155808255f3")
                ),
                Address("0x000000000000000000000000000000000000001b"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000001c"): Account(
                    code=bytes.fromhex("600160008181559055fe")
                ),
                Address("0x000000000000000000000000000000000000002a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000003a"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af460016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003b"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af46113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af450fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000004a"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af260016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000004b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af26113886000f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000004c"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af250fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000005a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000006a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000007a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082558190620c0de1803b91829181903c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007c"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556000620c0de181813b9283923c600080f050fe"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082557f6001600055600060005560016000f3000000000000000000000000000000000081528190600f90818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c6000818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000600155600080620c0de181813b9283923c8180f550fe"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000c0de0"): Account(
                    storage={1: 1},
                    code=bytes.fromhex(
                        "60ff60005260206000a060fa60206000a160fb60fa60206000a260fc60fb60fa60206000a360fd60fc60fb60fa60206000a400"  # noqa: E501
                    ),
                ),
                Address("0x00000000000000000000000000000000000c0de1"): Account(
                    code=bytes.fromhex("6000808055600190f3")
                ),
                Address("0x00000000000000000000000000000000000c0dea"): Account(
                    storage={1: 1}, code=bytes.fromhex("600060015500")
                ),
                Address("0x00000000000000000000000000000000000c0ded"): Account(
                    storage={1: 1}, code=bytes.fromhex("32ff")
                ),
                Address("0x4501f8fa1e67827ebfb1f6d5510c606871c5a599"): Account(
                    storage={0: 1}, code=bytes.fromhex("00")
                ),
                Address("0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"): Account(
                    code=bytes.fromhex(
                        "60008060043581813b9283923c8180f014601557005bfe"
                    )
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000005c",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000001a"): Account(
                    code=bytes.fromhex("60016000818155808255f3")
                ),
                Address("0x000000000000000000000000000000000000001b"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000001c"): Account(
                    code=bytes.fromhex("600160008181559055fe")
                ),
                Address("0x000000000000000000000000000000000000002a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000003a"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af460016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003b"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af46113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af450fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000004a"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af260016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000004b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af26113886000f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000004c"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af250fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000005a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000006a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000007a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082558190620c0de1803b91829181903c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007c"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556000620c0de181813b9283923c600080f050fe"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082557f6001600055600060005560016000f3000000000000000000000000000000000081528190600f90818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c6000818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000600155600080620c0de181813b9283923c8180f550fe"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000c0de0"): Account(
                    storage={1: 1},
                    code=bytes.fromhex(
                        "60ff60005260206000a060fa60206000a160fb60fa60206000a260fc60fb60fa60206000a360fd60fc60fb60fa60206000a400"  # noqa: E501
                    ),
                ),
                Address("0x00000000000000000000000000000000000c0de1"): Account(
                    code=bytes.fromhex("6000808055600190f3")
                ),
                Address("0x00000000000000000000000000000000000c0dea"): Account(
                    storage={1: 1}, code=bytes.fromhex("600060015500")
                ),
                Address("0x00000000000000000000000000000000000c0ded"): Account(
                    storage={1: 1}, code=bytes.fromhex("32ff")
                ),
                Address("0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"): Account(
                    code=bytes.fromhex(
                        "60008060043581813b9283923c8180f014601557005bfe"
                    )
                ),
            },
        ),
        (
            "693c6139000000000000000000000000000000000000000000000000000000000000005b",  # noqa: E501
            {
                Address("0x000000000000000000000000000000000000001a"): Account(
                    code=bytes.fromhex("60016000818155808255f3")
                ),
                Address("0x000000000000000000000000000000000000001b"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000001c"): Account(
                    code=bytes.fromhex("600160008181559055fe")
                ),
                Address("0x000000000000000000000000000000000000002a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000002c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0dea5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000003a"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af460016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003b"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af46113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000003c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000808080620c0dea5af450fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000004a"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af260016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000004b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af26113886000f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000004c"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600080808080620c0dea5af250fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000005a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000005c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0ded5af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000006a"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af160016000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006b"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af16113886000f3"
                    )
                ),
                Address("0x000000000000000000000000000000000000006c"): Account(
                    code=bytes.fromhex(
                        "6001600055600080808080620c0de05af150fe"
                    )
                ),
                Address("0x000000000000000000000000000000000000007a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082558190620c0de1803b91829181903c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c80600080f05001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000007c"): Account(
                    code=bytes.fromhex(
                        "60016000556001805560006001556000620c0de181813b9283923c600080f050fe"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008a"): Account(
                    code=bytes.fromhex(
                        "600160008181558082557f6001600055600060005560016000f3000000000000000000000000000000000081528190600f90818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008b"): Account(
                    code=bytes.fromhex(
                        "600160005560018055600060015561138860016000620c0de181813b9283923c6000818180f55001f3"  # noqa: E501
                    )
                ),
                Address("0x000000000000000000000000000000000000008c"): Account(
                    code=bytes.fromhex(
                        "6001600055600180556000600155600080620c0de181813b9283923c8180f550fe"  # noqa: E501
                    )
                ),
                Address("0x00000000000000000000000000000000000c0de0"): Account(
                    storage={1: 1},
                    code=bytes.fromhex(
                        "60ff60005260206000a060fa60206000a160fb60fa60206000a260fc60fb60fa60206000a360fd60fc60fb60fa60206000a400"  # noqa: E501
                    ),
                ),
                Address("0x00000000000000000000000000000000000c0de1"): Account(
                    code=bytes.fromhex("6000808055600190f3")
                ),
                Address("0x00000000000000000000000000000000000c0dea"): Account(
                    storage={1: 1}, code=bytes.fromhex("600060015500")
                ),
                Address("0x00000000000000000000000000000000000c0ded"): Account(
                    storage={1: 1}, code=bytes.fromhex("32ff")
                ),
                Address("0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"): Account(
                    code=bytes.fromhex(
                        "60008060043581813b9283923c8180f014601557005bfe"
                    )
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
        "case12",
        "case13",
        "case14",
        "case15",
        "case16",
        "case17",
        "case18",
        "case19",
        "case20",
        "case21",
        "case22",
        "case23",
    ],
)
@pytest.mark.pre_alloc_mutable
def test_create_oog_from_call_refunds(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    callee = Address("0x000000000000000000000000000000000000001a")
    callee_1 = Address("0x000000000000000000000000000000000000001b")
    callee_2 = Address("0x000000000000000000000000000000000000001c")
    callee_3 = Address("0x000000000000000000000000000000000000002a")
    callee_4 = Address("0x000000000000000000000000000000000000002b")
    callee_5 = Address("0x000000000000000000000000000000000000002c")
    callee_6 = Address("0x000000000000000000000000000000000000003a")
    callee_7 = Address("0x000000000000000000000000000000000000003b")
    callee_8 = Address("0x000000000000000000000000000000000000003c")
    callee_9 = Address("0x000000000000000000000000000000000000004a")
    callee_10 = Address("0x000000000000000000000000000000000000004b")
    callee_11 = Address("0x000000000000000000000000000000000000004c")
    callee_12 = Address("0x000000000000000000000000000000000000005a")
    callee_13 = Address("0x000000000000000000000000000000000000005b")
    callee_14 = Address("0x000000000000000000000000000000000000005c")
    callee_15 = Address("0x000000000000000000000000000000000000006a")
    callee_16 = Address("0x000000000000000000000000000000000000006b")
    callee_17 = Address("0x000000000000000000000000000000000000006c")
    callee_18 = Address("0x000000000000000000000000000000000000007a")
    callee_19 = Address("0x000000000000000000000000000000000000007b")
    callee_20 = Address("0x000000000000000000000000000000000000007c")
    callee_21 = Address("0x000000000000000000000000000000000000008a")
    callee_22 = Address("0x000000000000000000000000000000000000008b")
    callee_23 = Address("0x000000000000000000000000000000000000008c")
    callee_24 = Address("0x00000000000000000000000000000000000c0de0")
    callee_25 = Address("0x00000000000000000000000000000000000c0de1")
    callee_26 = Address("0x00000000000000000000000000000000000c0dea")
    callee_27 = Address("0x00000000000000000000000000000000000c0ded")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=4294967296,
    )

    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("60016000818155808255f3"),
    )
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("60016000556001805560006001556113886000f3"),
    )
    pre[callee_2] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("600160008181559055fe"),
    )
    pre[callee_3] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("6001600055600080808080620c0dea5af160016000f3"),
    )
    pre[callee_4] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("6001600055600080808080620c0dea5af16113886000f3"),
    )
    pre[callee_5] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("6001600055600080808080620c0dea5af150fe"),
    )
    pre[callee_6] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "6001600055600180556000808080620c0dea5af460016000f3"
        ),
    )
    pre[callee_7] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "6001600055600180556000808080620c0dea5af46113886000f3"
        ),
    )
    pre[callee_8] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("6001600055600180556000808080620c0dea5af450fe"),
    )
    pre[callee_9] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "600160005560018055600080808080620c0dea5af260016000f3"
        ),
    )
    pre[callee_10] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "600160005560018055600080808080620c0dea5af26113886000f3"
        ),
    )
    pre[callee_11] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("600160005560018055600080808080620c0dea5af250fe"),
    )
    pre[callee_12] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("6001600055600080808080620c0ded5af160016000f3"),
    )
    pre[callee_13] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("6001600055600080808080620c0ded5af16113886000f3"),
    )
    pre[callee_14] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("6001600055600080808080620c0ded5af150fe"),
    )
    pre[callee_15] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("6001600055600080808080620c0de05af160016000f3"),
    )
    pre[callee_16] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("6001600055600080808080620c0de05af16113886000f3"),
    )
    pre[callee_17] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("6001600055600080808080620c0de05af150fe"),
    )
    pre[callee_18] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "600160008181558082558190620c0de1803b91829181903c80600080f05001f3"
        ),
    )
    pre[callee_19] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "600160005560018055600060015561138860016000620c0de181813b9283923c80600080"  # noqa: E501
            "f05001f3"
        ),
    )
    pre[callee_20] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "60016000556001805560006001556000620c0de181813b9283923c600080f050fe"  # noqa: E501
        ),
    )
    pre[callee_21] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "600160008181558082557f6001600055600060005560016000f300000000000000000000"  # noqa: E501
            "0000000000000081528190600f90818180f55001f3"
        ),
    )
    pre[callee_22] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "600160005560018055600060015561138860016000620c0de181813b9283923c60008181"  # noqa: E501
            "80f55001f3"
        ),
    )
    pre[callee_23] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "6001600055600180556000600155600080620c0de181813b9283923c8180f550fe"  # noqa: E501
        ),
    )
    pre[callee_24] = Account(
        balance=0,
        nonce=1,
        code=bytes.fromhex(
            "60ff60005260206000a060fa60206000a160fb60fa60206000a260fc60fb60fa60206000"  # noqa: E501
            "a360fd60fc60fb60fa60206000a400"
        ),
        storage={0x1: 0x1},
    )
    pre[callee_25] = Account(
        balance=0,
        nonce=1,
        code=bytes.fromhex("6000808055600190f3"),
    )
    pre[callee_26] = Account(
        balance=0,
        nonce=1,
        code=bytes.fromhex("600060015500"),
        storage={0x1: 0x1},
    )
    pre[callee_27] = Account(
        balance=0,
        nonce=1,
        code=bytes.fromhex("32ff"),
        storage={0x1: 0x1},
    )
    pre[sender] = Account(balance=0x3D0900, nonce=1)
    pre[contract] = Account(
        balance=0,
        nonce=1,
        code=bytes.fromhex("60008060043581813b9283923c8180f014601557005bfe"),
    )

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=tx_data,
        gas_limit=400000,
        gas_price=10,
        nonce=1,
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
