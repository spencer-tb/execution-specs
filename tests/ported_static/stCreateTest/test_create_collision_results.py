"""
Ori Pomerantz qbzzt1@gmail.com.

Ported from:
tests/static/state_tests/stCreateTest/CreateCollisionResultsFiller.yml
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
    ["tests/static/state_tests/stCreateTest/CreateCollisionResultsFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        (
            "01",
            {
                Address("0x40f1299359ea754ac29eb2662a1900752bf8275f"): Account(
                    storage={0: 29}, code=bytes.fromhex("601d60005500")
                ),
                Address("0x8af6a7af30d840ba137e8f3f34d54cfb8beba6e2"): Account(
                    storage={0: 29}, code=bytes.fromhex("601d60005500")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={
                        32: 89,
                        33: 143,
                        34: 200,
                        48: 6,
                        49: 0x601D600055000000000000000000000000000000000000000000000000000000,  # noqa: E501
                        50: 6,
                        51: 0x601D600055000000000000000000000000000000000000000000000000000000,  # noqa: E501
                    },
                    code=bytes.fromhex(
                        "60f860020a6000350461010052601580610158610300396105405260068061016d61020039610520526001610100511461004957615a17610540516103006000f561060052610058565b610540516103006000f0610600525b586020553d6010556106005160115560006000600060006000738af6a7af30d840ba137e8f3f34d54cfb8beba6e261fffff16106405258602155600161064051036012553d601355600060006000600060007340f1299359ea754ac29eb2662a1900752bf8275f61fffff16106405258602255600161064051036014553d601555738af6a7af30d840ba137e8f3f34d54cfb8beba6e23b6030556030546000610660738af6a7af30d840ba137e8f3f34d54cfb8beba6e23c610660516031557340f1299359ea754ac29eb2662a1900752bf8275f3b60325560325460006106607340f1299359ea754ac29eb2662a1900752bf8275f3c6106605160335500fe600680600f61020039610200f300fe60ff6000550060ff60005500"  # noqa: E501
                    ),
                ),
            },
        ),
        (
            "02",
            {
                Address("0x40f1299359ea754ac29eb2662a1900752bf8275f"): Account(
                    storage={0: 29}, code=bytes.fromhex("601d60005500")
                ),
                Address("0x8af6a7af30d840ba137e8f3f34d54cfb8beba6e2"): Account(
                    storage={0: 29}, code=bytes.fromhex("601d60005500")
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={
                        32: 89,
                        33: 143,
                        34: 200,
                        48: 6,
                        49: 0x601D600055000000000000000000000000000000000000000000000000000000,  # noqa: E501
                        50: 6,
                        51: 0x601D600055000000000000000000000000000000000000000000000000000000,  # noqa: E501
                    },
                    code=bytes.fromhex(
                        "60f860020a6000350461010052601580610158610300396105405260068061016d61020039610520526001610100511461004957615a17610540516103006000f561060052610058565b610540516103006000f0610600525b586020553d6010556106005160115560006000600060006000738af6a7af30d840ba137e8f3f34d54cfb8beba6e261fffff16106405258602155600161064051036012553d601355600060006000600060007340f1299359ea754ac29eb2662a1900752bf8275f61fffff16106405258602255600161064051036014553d601555738af6a7af30d840ba137e8f3f34d54cfb8beba6e23b6030556030546000610660738af6a7af30d840ba137e8f3f34d54cfb8beba6e23c610660516031557340f1299359ea754ac29eb2662a1900752bf8275f3b60325560325460006106607340f1299359ea754ac29eb2662a1900752bf8275f3c6106605160335500fe600680600f61020039610200f300fe60ff6000550060ff60005500"  # noqa: E501
                    ),
                ),
            },
        ),
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_create_collision_results(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Ori Pomerantz qbzzt1@gmail.com."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xcccccccccccccccccccccccccccccccccccccccc")
    callee = Address("0x40f1299359ea754ac29eb2662a1900752bf8275f")
    callee_1 = Address("0x8af6a7af30d840ba137e8f3f34d54cfb8beba6e2")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=4294967296,
    )

    pre[callee] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("601d60005500"),
        storage={0x0: 0x60A7},
    )
    pre[callee_1] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("601d60005500"),
        storage={0x0: 0x60A7},
    )
    pre[sender] = Account(balance=0xBA1A9CE0BA1A9CE, nonce=0)
    pre[contract] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex(
            "60f860020a6000350461010052601580610158610300396105405260068061016d610200"  # noqa: E501
            "39610520526001610100511461004957615a17610540516103006000f561060052610058"  # noqa: E501
            "565b610540516103006000f0610600525b586020553d6010556106005160115560006000"  # noqa: E501
            "600060006000738af6a7af30d840ba137e8f3f34d54cfb8beba6e261fffff16106405258"  # noqa: E501
            "602155600161064051036012553d601355600060006000600060007340f1299359ea754a"  # noqa: E501
            "c29eb2662a1900752bf8275f61fffff16106405258602255600161064051036014553d60"  # noqa: E501
            "1555738af6a7af30d840ba137e8f3f34d54cfb8beba6e23b603055603054600061066073"  # noqa: E501
            "8af6a7af30d840ba137e8f3f34d54cfb8beba6e23c610660516031557340f1299359ea75"  # noqa: E501
            "4ac29eb2662a1900752bf8275f3b60325560325460006106607340f1299359ea754ac29e"  # noqa: E501
            "b2662a1900752bf8275f3c6106605160335500fe600680600f61020039610200f300fe60"  # noqa: E501
            "ff6000550060ff60005500"
        ),
        storage={
            0x10: 0x60A7,
            0x11: 0x60A7,
            0x12: 0x60A7,
            0x13: 0x60A7,
            0x14: 0x60A7,
            0x15: 0x60A7,
            0x20: 0x60A7,
            0x21: 0x60A7,
            0x22: 0x60A7,
        },
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
        nonce=0,
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
