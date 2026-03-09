"""
callcode to a contract that is being created in the same transaction.

Ported from:
tests/static/state_tests/stCallCodes/callcodeDynamicCodeFiller.json
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
    ["tests/static/state_tests/stCallCodes/callcodeDynamicCodeFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        (
            "0000000000000000000000001000000000000000000000000000000000000000",
            {
                Address("0x1000000000000000000000000000000000000000"): Account(
                    storage={
                        0: 1,
                        10: 0x13136008B64FF592819B2FA6D43F2835C452020E,
                        11: 1,
                        20: 0x1000000000000000000000000000000000000000,
                        21: 0xA94F5374FCE5EDBC8E2A8697C15331677E6EBF0B,
                        22: 0x1000000000000000000000000000000000000000,
                    },
                    code=bytes.fromhex(
                        "601f80602760003960006000f0600a5560406000604060006000600a54620186a0f2600b5500fe601280600d6000396000f300fe600160005530601455326015553360165500"  # noqa: E501
                    ),
                ),
                Address("0x1100000000000000000000000000000000000000"): Account(
                    code=bytes.fromhex(
                        "60006000600060006000600035620c3500f100"
                    )
                ),
                Address("0x13136008b64ff592819b2fa6d43f2835c452020e"): Account(
                    code=bytes.fromhex("600160005530601455326015553360165500")
                ),
                Address("0x2000000000000000000000000000000000000000"): Account(
                    code=bytes.fromhex(
                        "6000601f80602960003960006000f5600a5560406000604060006000600a54620186a0f2600b5500fe601280600d6000396000f300fe600160005530601455326015553360165500"  # noqa: E501
                    )
                ),
                Address("0x3000000000000000000000000000000000000000"): Account(
                    code=bytes.fromhex(
                        "604680600f60003960006000f000fe601f80602760003960006000f0600a5560406000604060006000600a54620186a0f2600b5500fe601280600d6000396000f300fe600160005530601455326015553360165500"  # noqa: E501
                    )
                ),
                Address("0x4000000000000000000000000000000000000000"): Account(
                    code=bytes.fromhex(
                        "604880600f60003960006000f000fe6000601f80602960003960006000f5600a5560406000604060006000600a54620186a0f2600b5500fe601280600d6000396000f300fe600160005530601455326015553360165500"  # noqa: E501
                    )
                ),
            },
        ),
        (
            "0000000000000000000000002000000000000000000000000000000000000000",
            {
                Address("0x1000000000000000000000000000000000000000"): Account(
                    code=bytes.fromhex(
                        "601f80602760003960006000f0600a5560406000604060006000600a54620186a0f2600b5500fe601280600d6000396000f300fe600160005530601455326015553360165500"  # noqa: E501
                    )
                ),
                Address("0x1100000000000000000000000000000000000000"): Account(
                    code=bytes.fromhex(
                        "60006000600060006000600035620c3500f100"
                    )
                ),
                Address("0x2000000000000000000000000000000000000000"): Account(
                    storage={
                        0: 1,
                        10: 0x2D39FAD743351D4CF3F4717907D3DDA5E0A689A7,
                        11: 1,
                        20: 0x2000000000000000000000000000000000000000,
                        21: 0xA94F5374FCE5EDBC8E2A8697C15331677E6EBF0B,
                        22: 0x2000000000000000000000000000000000000000,
                    },
                    code=bytes.fromhex(
                        "6000601f80602960003960006000f5600a5560406000604060006000600a54620186a0f2600b5500fe601280600d6000396000f300fe600160005530601455326015553360165500"  # noqa: E501
                    ),
                ),
                Address("0x2d39fad743351d4cf3f4717907d3dda5e0a689a7"): Account(
                    code=bytes.fromhex("600160005530601455326015553360165500")
                ),
                Address("0x3000000000000000000000000000000000000000"): Account(
                    code=bytes.fromhex(
                        "604680600f60003960006000f000fe601f80602760003960006000f0600a5560406000604060006000600a54620186a0f2600b5500fe601280600d6000396000f300fe600160005530601455326015553360165500"  # noqa: E501
                    )
                ),
                Address("0x4000000000000000000000000000000000000000"): Account(
                    code=bytes.fromhex(
                        "604880600f60003960006000f000fe6000601f80602960003960006000f5600a5560406000604060006000600a54620186a0f2600b5500fe601280600d6000396000f300fe600160005530601455326015553360165500"  # noqa: E501
                    )
                ),
            },
        ),
        (
            "0000000000000000000000003000000000000000000000000000000000000000",
            {
                Address("0x1000000000000000000000000000000000000000"): Account(
                    code=bytes.fromhex(
                        "601f80602760003960006000f0600a5560406000604060006000600a54620186a0f2600b5500fe601280600d6000396000f300fe600160005530601455326015553360165500"  # noqa: E501
                    )
                ),
                Address("0x1100000000000000000000000000000000000000"): Account(
                    code=bytes.fromhex(
                        "60006000600060006000600035620c3500f100"
                    )
                ),
                Address("0x2000000000000000000000000000000000000000"): Account(
                    code=bytes.fromhex(
                        "6000601f80602960003960006000f5600a5560406000604060006000600a54620186a0f2600b5500fe601280600d6000396000f300fe600160005530601455326015553360165500"  # noqa: E501
                    )
                ),
                Address("0x3000000000000000000000000000000000000000"): Account(
                    code=bytes.fromhex(
                        "604680600f60003960006000f000fe601f80602760003960006000f0600a5560406000604060006000600a54620186a0f2600b5500fe601280600d6000396000f300fe600160005530601455326015553360165500"  # noqa: E501
                    )
                ),
                Address("0x4000000000000000000000000000000000000000"): Account(
                    code=bytes.fromhex(
                        "604880600f60003960006000f000fe6000601f80602960003960006000f5600a5560406000604060006000600a54620186a0f2600b5500fe601280600d6000396000f300fe600160005530601455326015553360165500"  # noqa: E501
                    )
                ),
                Address("0x4b86c4ed99b87f0f396bc0c76885453c343916ed"): Account(
                    storage={
                        0: 1,
                        10: 0xBF1676BE6038AB86D66E00824C2E3577858040F6,
                        11: 1,
                        20: 0x4B86C4ED99B87F0F396BC0C76885453C343916ED,
                        21: 0xA94F5374FCE5EDBC8E2A8697C15331677E6EBF0B,
                        22: 0x4B86C4ED99B87F0F396BC0C76885453C343916ED,
                    }
                ),
                Address("0xbf1676be6038ab86d66e00824c2e3577858040f6"): Account(
                    code=bytes.fromhex("600160005530601455326015553360165500")
                ),
            },
        ),
        (
            "0000000000000000000000004000000000000000000000000000000000000000",
            {
                Address("0x0f2d6bf688fae45da62ab2dd4f36945bc924cc61"): Account(
                    code=bytes.fromhex("600160005530601455326015553360165500")
                ),
                Address("0x1000000000000000000000000000000000000000"): Account(
                    code=bytes.fromhex(
                        "601f80602760003960006000f0600a5560406000604060006000600a54620186a0f2600b5500fe601280600d6000396000f300fe600160005530601455326015553360165500"  # noqa: E501
                    )
                ),
                Address("0x1100000000000000000000000000000000000000"): Account(
                    code=bytes.fromhex(
                        "60006000600060006000600035620c3500f100"
                    )
                ),
                Address("0x2000000000000000000000000000000000000000"): Account(
                    code=bytes.fromhex(
                        "6000601f80602960003960006000f5600a5560406000604060006000600a54620186a0f2600b5500fe601280600d6000396000f300fe600160005530601455326015553360165500"  # noqa: E501
                    )
                ),
                Address("0x3000000000000000000000000000000000000000"): Account(
                    code=bytes.fromhex(
                        "604680600f60003960006000f000fe601f80602760003960006000f0600a5560406000604060006000600a54620186a0f2600b5500fe601280600d6000396000f300fe600160005530601455326015553360165500"  # noqa: E501
                    )
                ),
                Address("0x4000000000000000000000000000000000000000"): Account(
                    code=bytes.fromhex(
                        "604880600f60003960006000f000fe6000601f80602960003960006000f5600a5560406000604060006000600a54620186a0f2600b5500fe601280600d6000396000f300fe600160005530601455326015553360165500"  # noqa: E501
                    )
                ),
                Address("0xa51c188504a60578914fcae68f7a1f0dcbb856a9"): Account(
                    storage={
                        0: 1,
                        10: 0xF2D6BF688FAE45DA62AB2DD4F36945BC924CC61,
                        11: 1,
                        20: 0xA51C188504A60578914FCAE68F7A1F0DCBB856A9,
                        21: 0xA94F5374FCE5EDBC8E2A8697C15331677E6EBF0B,
                        22: 0xA51C188504A60578914FCAE68F7A1F0DCBB856A9,
                    }
                ),
            },
        ),
    ],
    ids=["case0", "case1", "case2", "case3"],
)
@pytest.mark.pre_alloc_mutable
def test_callcode_dynamic_code(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Callcode to a contract that is being created in the same transaction."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x1100000000000000000000000000000000000000")
    callee = Address("0x1000000000000000000000000000000000000000")
    callee_1 = Address("0x2000000000000000000000000000000000000000")
    callee_2 = Address("0x3000000000000000000000000000000000000000")
    callee_3 = Address("0x4000000000000000000000000000000000000000")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    pre[callee] = Account(
        balance=0x2710,
        nonce=0,
        code=bytes.fromhex(
            "601f80602760003960006000f0600a5560406000604060006000600a54620186a0f2600b"  # noqa: E501
            "5500fe601280600d6000396000f300fe600160005530601455326015553360165500"  # noqa: E501
        ),
    )
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("60006000600060006000600035620c3500f100"),
    )
    pre[callee_1] = Account(
        balance=1000,
        nonce=0,
        code=bytes.fromhex(
            "6000601f80602960003960006000f5600a5560406000604060006000600a54620186a0f2"  # noqa: E501
            "600b5500fe601280600d6000396000f300fe600160005530601455326015553360165500"  # noqa: E501
        ),
    )
    pre[callee_2] = Account(
        balance=0x2710,
        nonce=0,
        code=bytes.fromhex(
            "604680600f60003960006000f000fe601f80602760003960006000f0600a556040600060"  # noqa: E501
            "4060006000600a54620186a0f2600b5500fe601280600d6000396000f300fe6001600055"  # noqa: E501
            "30601455326015553360165500"
        ),
    )
    pre[callee_3] = Account(
        balance=0x2710,
        nonce=0,
        code=bytes.fromhex(
            "604880600f60003960006000f000fe6000601f80602960003960006000f5600a55604060"  # noqa: E501
            "00604060006000600a54620186a0f2600b5500fe601280600d6000396000f300fe600160"  # noqa: E501
            "005530601455326015553360165500"
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
