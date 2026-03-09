"""
callcode happen to a contract that is dynamically created from within the...

Ported from:
tests/static/state_tests/stCallCodes/callcodeDynamicCode2SelfCallFiller.json
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
        "tests/static/state_tests/stCallCodes/callcodeDynamicCode2SelfCallFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        (
            "000000000000000000000000a000000000000000000000000000000000000000",
            {
                Address("0x1000000000000000000000000000000000000000"): Account(
                    code=bytes.fromhex(
                        "604680602760003960006000f0600a5560406000604060006000600a54620186a0f2600b5500fe604060006040600060007313136008b64ff592819b2fa6d43f2835c452020e620186a0f2607a5560128060346000396000f300fe600160005530601455326015553360165500"  # noqa: E501
                    )
                ),
                Address("0x1100000000000000000000000000000000000000"): Account(
                    code=bytes.fromhex(
                        "60006000600060006000600035620c3500f100"
                    )
                ),
                Address("0x7db299e0885c85039f56fa504a13dd8ce8a56aa7"): Account(
                    storage={
                        11: 1,
                        12: 0xA000000000000000000000000000000000000000,
                    }
                ),
                Address("0xa000000000000000000000000000000000000000"): Account(
                    code=bytes.fromhex(
                        "7f604060006040600060007313136008b64ff592819b2fa6d43f2835c452020e626000527f0186a0f2600b5533600c55000000000000000000000000000000000000000000602052604060006001f000"  # noqa: E501
                    )
                ),
            },
        ),
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
                        "604680602760003960006000f0600a5560406000604060006000600a54620186a0f2600b5500fe604060006040600060007313136008b64ff592819b2fa6d43f2835c452020e620186a0f2607a5560128060346000396000f300fe600160005530601455326015553360165500"  # noqa: E501
                    ),
                ),
                Address("0x1100000000000000000000000000000000000000"): Account(
                    code=bytes.fromhex(
                        "60006000600060006000600035620c3500f100"
                    )
                ),
                Address("0x13136008b64ff592819b2fa6d43f2835c452020e"): Account(
                    storage={122: 1},
                    code=bytes.fromhex("600160005530601455326015553360165500"),
                ),
                Address("0xa000000000000000000000000000000000000000"): Account(
                    code=bytes.fromhex(
                        "7f604060006040600060007313136008b64ff592819b2fa6d43f2835c452020e626000527f0186a0f2600b5533600c55000000000000000000000000000000000000000000602052604060006001f000"  # noqa: E501
                    )
                ),
            },
        ),
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_callcode_dynamic_code2_self_call(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Callcode happen to a contract that is dynamically created from..."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x1100000000000000000000000000000000000000")
    callee = Address("0x1000000000000000000000000000000000000000")
    callee_1 = Address("0xa000000000000000000000000000000000000000")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[callee] = Account(
        balance=0x2710,
        nonce=0,
        code=bytes.fromhex(
            "604680602760003960006000f0600a5560406000604060006000600a54620186a0f2600b"  # noqa: E501
            "5500fe604060006040600060007313136008b64ff592819b2fa6d43f2835c452020e6201"  # noqa: E501
            "86a0f2607a5560128060346000396000f300fe6001600055306014553260155533601655"  # noqa: E501
            "00"
        ),
    )
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("60006000600060006000600035620c3500f100"),
    )
    pre[callee_1] = Account(
        balance=0x2710,
        nonce=0,
        code=bytes.fromhex(
            "7f604060006040600060007313136008b64ff592819b2fa6d43f2835c452020e62600052"  # noqa: E501
            "7f0186a0f2600b5533600c55000000000000000000000000000000000000000000602052"  # noqa: E501
            "604060006001f000"
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
        gas_limit=1453081,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
