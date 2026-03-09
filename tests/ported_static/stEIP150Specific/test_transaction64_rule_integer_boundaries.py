"""
Danno Ferrin danno.ferrin@gmail.com.

Ported from:
tests/static/state_tests/stEIP150Specific
Transaction64Rule_integerBoundariesFiller.yml
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
        "tests/static/state_tests/stEIP150Specific/Transaction64Rule_integerBoundariesFiller.yml",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        (
            "000000000000000000000000000000007fffffffffffffffffffffffffffffff",
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("600060ff00")
                ),
                Address("0x000000000000000000000000000000000000c0de"): Account(
                    storage={0: 1, 1: 1, 2: 1, 3: 1},
                    code=bytes.fromhex(
                        "5a602060008181611000813583838080808686f150865a10835583838080808686f250865a10600155838381818585f450865a10600255fa505a1060035500"  # noqa: E501
                    ),
                ),
            },
        ),
        (
            "0000000000000000000000000000000000000000000000000000000000007fff",
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("600060ff00")
                ),
                Address("0x000000000000000000000000000000000000c0de"): Account(
                    storage={0: 1, 1: 1, 2: 1, 3: 1},
                    code=bytes.fromhex(
                        "5a602060008181611000813583838080808686f150865a10835583838080808686f250865a10600155838381818585f450865a10600255fa505a1060035500"  # noqa: E501
                    ),
                ),
            },
        ),
        (
            "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("600060ff00")
                ),
                Address("0x000000000000000000000000000000000000c0de"): Account(
                    storage={0: 1, 1: 1, 2: 1, 3: 1},
                    code=bytes.fromhex(
                        "5a602060008181611000813583838080808686f150865a10835583838080808686f250865a10600155838381818585f450865a10600255fa505a1060035500"  # noqa: E501
                    ),
                ),
            },
        ),
        (
            "000000000000000000000000000000000000000000000000000000007fffffff",
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("600060ff00")
                ),
                Address("0x000000000000000000000000000000000000c0de"): Account(
                    storage={0: 1, 1: 1, 2: 1, 3: 1},
                    code=bytes.fromhex(
                        "5a602060008181611000813583838080808686f150865a10835583838080808686f250865a10600155838381818585f450865a10600255fa505a1060035500"  # noqa: E501
                    ),
                ),
            },
        ),
        (
            "0000000000000000000000000000000000000000000000007fffffffffffffff",
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("600060ff00")
                ),
                Address("0x000000000000000000000000000000000000c0de"): Account(
                    storage={0: 1, 1: 1, 2: 1, 3: 1},
                    code=bytes.fromhex(
                        "5a602060008181611000813583838080808686f150865a10835583838080808686f250865a10600155838381818585f450865a10600255fa505a1060035500"  # noqa: E501
                    ),
                ),
            },
        ),
        (
            "000000000000000000000000000000000000000000000000000000000000007f",
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("600060ff00")
                ),
                Address("0x000000000000000000000000000000000000c0de"): Account(
                    storage={0: 1, 1: 1, 2: 1, 3: 1},
                    code=bytes.fromhex(
                        "5a602060008181611000813583838080808686f150865a10835583838080808686f250865a10600155838381818585f450865a10600255fa505a1060035500"  # noqa: E501
                    ),
                ),
            },
        ),
        (
            "000000000000000000000000000000008fffffffffffffffffffffffffffffff",
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("600060ff00")
                ),
                Address("0x000000000000000000000000000000000000c0de"): Account(
                    storage={0: 1, 1: 1, 2: 1, 3: 1},
                    code=bytes.fromhex(
                        "5a602060008181611000813583838080808686f150865a10835583838080808686f250865a10600155838381818585f450865a10600255fa505a1060035500"  # noqa: E501
                    ),
                ),
            },
        ),
        (
            "0000000000000000000000000000000000000000000000000000000000008fff",
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("600060ff00")
                ),
                Address("0x000000000000000000000000000000000000c0de"): Account(
                    storage={0: 1, 1: 1, 2: 1, 3: 1},
                    code=bytes.fromhex(
                        "5a602060008181611000813583838080808686f150865a10835583838080808686f250865a10600155838381818585f450865a10600255fa505a1060035500"  # noqa: E501
                    ),
                ),
            },
        ),
        (
            "8fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("600060ff00")
                ),
                Address("0x000000000000000000000000000000000000c0de"): Account(
                    storage={0: 1, 1: 1, 2: 1, 3: 1},
                    code=bytes.fromhex(
                        "5a602060008181611000813583838080808686f150865a10835583838080808686f250865a10600155838381818585f450865a10600255fa505a1060035500"  # noqa: E501
                    ),
                ),
            },
        ),
        (
            "000000000000000000000000000000000000000000000000000000008fffffff",
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("600060ff00")
                ),
                Address("0x000000000000000000000000000000000000c0de"): Account(
                    storage={0: 1, 1: 1, 2: 1, 3: 1},
                    code=bytes.fromhex(
                        "5a602060008181611000813583838080808686f150865a10835583838080808686f250865a10600155838381818585f450865a10600255fa505a1060035500"  # noqa: E501
                    ),
                ),
            },
        ),
        (
            "0000000000000000000000000000000000000000000000008fffffffffffffff",
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("600060ff00")
                ),
                Address("0x000000000000000000000000000000000000c0de"): Account(
                    storage={0: 1, 1: 1, 2: 1, 3: 1},
                    code=bytes.fromhex(
                        "5a602060008181611000813583838080808686f150865a10835583838080808686f250865a10600155838381818585f450865a10600255fa505a1060035500"  # noqa: E501
                    ),
                ),
            },
        ),
        (
            "000000000000000000000000000000000000000000000000000000000000008f",
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex("600060ff00")
                ),
                Address("0x000000000000000000000000000000000000c0de"): Account(
                    storage={0: 1, 1: 1, 2: 1, 3: 1},
                    code=bytes.fromhex(
                        "5a602060008181611000813583838080808686f150865a10835583838080808686f250865a10600155838381818585f450865a10600255fa505a1060035500"  # noqa: E501
                    ),
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
def test_transaction64_rule_integer_boundaries(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Danno Ferrin danno.ferrin@gmail.com."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x000000000000000000000000000000000000c0de")
    callee = Address("0x0000000000000000000000000000000000001000")

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
        nonce=0,
        code=bytes.fromhex("600060ff00"),
    )
    pre[contract] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex(
            "5a602060008181611000813583838080808686f150865a10835583838080808686f25086"  # noqa: E501
            "5a10600155838381818585f450865a10600255fa505a1060035500"
        ),
    )
    pre[sender] = Account(balance=0x10000000000000000, nonce=0)

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=tx_data,
        gas_limit=800000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
