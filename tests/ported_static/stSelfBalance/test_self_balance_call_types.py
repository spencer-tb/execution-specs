"""
SELFBALANCE tests inside CALL, DELEGATECALL, and CALLCODE.

Ported from:
tests/static/state_tests/stSelfBalance/selfBalanceCallTypesFiller.json
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
    ["tests/static/state_tests/stSelfBalance/selfBalanceCallTypesFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        (
            "0000000000000000000000000000000000000000000000000000000000000001",
            {
                Address("0x76bac61ee2056f42f6cc29f5400adae3e5705237"): Account(
                    storage={33: 4352}, code=bytes.fromhex("4760215500")
                ),
                Address("0x84bf87fbef135afea15330fdf5847eb504cff901"): Account(
                    storage={
                        0: 0xA590BBF1B07B00FED987724E1DB1BF206C2BC37C,
                        1: 0x76BAC61EE2056F42F6CC29F5400ADAE3E5705237,
                        2: 0x8537CE29429EA557E3903C255EE6554DD8D21D26,
                        3: 0xE1CE93B3251FB38AE74D41AF9F865978C572CF63,
                    },
                    code=bytes.fromhex(
                        "60006080525b608051541560755760003560011415602c57600060006000600060006080515460155a03f1505b6000356002141560495760006000600060006080515460155a03f4505b60003560031415606857600060006000600060006080515460155a03f2505b6001608051016080526005565b00"  # noqa: E501
                    ),
                ),
                Address("0x8537ce29429ea557e3903c255ee6554dd8d21d26"): Account(
                    storage={49: 5},
                    code=bytes.fromhex("5a475a905090036002900360315500"),
                ),
                Address("0xa590bbf1b07b00fed987724e1db1bf206c2bc37c"): Account(
                    storage={17: 1}, code=bytes.fromhex("3031471460115500")
                ),
                Address("0xe1ce93b3251fb38ae74d41af9f865978c572cf63"): Account(
                    storage={65: 4864, 66: 4863, 67: 1},
                    code=bytes.fromhex(
                        "47806041556000600060006000600160006000f1504780604255900360435500"  # noqa: E501
                    ),
                ),
            },
        ),
        (
            "0000000000000000000000000000000000000000000000000000000000000002",
            {
                Address("0x76bac61ee2056f42f6cc29f5400adae3e5705237"): Account(
                    code=bytes.fromhex("4760215500")
                ),
                Address("0x84bf87fbef135afea15330fdf5847eb504cff901"): Account(
                    storage={
                        0: 0xA590BBF1B07B00FED987724E1DB1BF206C2BC37C,
                        1: 0x76BAC61EE2056F42F6CC29F5400ADAE3E5705237,
                        2: 0x8537CE29429EA557E3903C255EE6554DD8D21D26,
                        3: 0xE1CE93B3251FB38AE74D41AF9F865978C572CF63,
                        17: 1,
                        33: 8192,
                        49: 5,
                        65: 8192,
                        66: 8191,
                        67: 1,
                    },
                    code=bytes.fromhex(
                        "60006080525b608051541560755760003560011415602c57600060006000600060006080515460155a03f1505b6000356002141560495760006000600060006080515460155a03f4505b60003560031415606857600060006000600060006080515460155a03f2505b6001608051016080526005565b00"  # noqa: E501
                    ),
                ),
                Address("0x8537ce29429ea557e3903c255ee6554dd8d21d26"): Account(
                    code=bytes.fromhex("5a475a905090036002900360315500")
                ),
                Address("0xa590bbf1b07b00fed987724e1db1bf206c2bc37c"): Account(
                    code=bytes.fromhex("3031471460115500")
                ),
                Address("0xe1ce93b3251fb38ae74d41af9f865978c572cf63"): Account(
                    code=bytes.fromhex(
                        "47806041556000600060006000600160006000f1504780604255900360435500"  # noqa: E501
                    )
                ),
            },
        ),
        (
            "0000000000000000000000000000000000000000000000000000000000000003",
            {
                Address("0x76bac61ee2056f42f6cc29f5400adae3e5705237"): Account(
                    code=bytes.fromhex("4760215500")
                ),
                Address("0x84bf87fbef135afea15330fdf5847eb504cff901"): Account(
                    storage={
                        0: 0xA590BBF1B07B00FED987724E1DB1BF206C2BC37C,
                        1: 0x76BAC61EE2056F42F6CC29F5400ADAE3E5705237,
                        2: 0x8537CE29429EA557E3903C255EE6554DD8D21D26,
                        3: 0xE1CE93B3251FB38AE74D41AF9F865978C572CF63,
                        17: 1,
                        33: 8192,
                        49: 5,
                        65: 8192,
                        66: 8191,
                        67: 1,
                    },
                    code=bytes.fromhex(
                        "60006080525b608051541560755760003560011415602c57600060006000600060006080515460155a03f1505b6000356002141560495760006000600060006080515460155a03f4505b60003560031415606857600060006000600060006080515460155a03f2505b6001608051016080526005565b00"  # noqa: E501
                    ),
                ),
                Address("0x8537ce29429ea557e3903c255ee6554dd8d21d26"): Account(
                    code=bytes.fromhex("5a475a905090036002900360315500")
                ),
                Address("0xa590bbf1b07b00fed987724e1db1bf206c2bc37c"): Account(
                    code=bytes.fromhex("3031471460115500")
                ),
                Address("0xe1ce93b3251fb38ae74d41af9f865978c572cf63"): Account(
                    code=bytes.fromhex(
                        "47806041556000600060006000600160006000f1504780604255900360435500"  # noqa: E501
                    )
                ),
            },
        ),
    ],
    ids=["case0", "case1", "case2"],
)
@pytest.mark.pre_alloc_mutable
def test_self_balance_call_types(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """SELFBALANCE tests inside CALL, DELEGATECALL, and CALLCODE."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xd187b36e8532efd7f15218fb1781d79330c0cda2")
    contract = Address("0x84bf87fbef135afea15330fdf5847eb504cff901")
    callee = Address("0x76bac61ee2056f42f6cc29f5400adae3e5705237")
    callee_1 = Address("0x8537ce29429ea557e3903c255ee6554dd8d21d26")
    callee_2 = Address("0xa590bbf1b07b00fed987724e1db1bf206c2bc37c")
    callee_3 = Address("0xe1ce93b3251fb38ae74d41af9f865978c572cf63")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000000,
    )

    pre[callee] = Account(
        balance=4352,
        nonce=0,
        code=bytes.fromhex("4760215500"),
    )
    pre[contract] = Account(
        balance=8192,
        nonce=0,
        code=bytes.fromhex(
            "60006080525b608051541560755760003560011415602c57600060006000600060006080"  # noqa: E501
            "515460155a03f1505b6000356002141560495760006000600060006080515460155a03f4"  # noqa: E501
            "505b60003560031415606857600060006000600060006080515460155a03f2505b600160"  # noqa: E501
            "8051016080526005565b00"
        ),
        storage={
            0x0: 0xA590BBF1B07B00FED987724E1DB1BF206C2BC37C,
            0x1: 0x76BAC61EE2056F42F6CC29F5400ADAE3E5705237,
            0x2: 0x8537CE29429EA557E3903C255EE6554DD8D21D26,
            0x3: 0xE1CE93B3251FB38AE74D41AF9F865978C572CF63,
        },
    )
    pre[callee_1] = Account(
        balance=4608,
        nonce=0,
        code=bytes.fromhex("5a475a905090036002900360315500"),
    )
    pre[callee_2] = Account(
        balance=4096,
        nonce=0,
        code=bytes.fromhex("3031471460115500"),
    )
    pre[sender] = Account(balance=0x3635C9ADC5DEA00000, nonce=0)
    pre[callee_3] = Account(
        balance=4864,
        nonce=0,
        code=bytes.fromhex(
            "47806041556000600060006000600160006000f1504780604255900360435500"
        ),
    )

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x897b12d02d588d8a4fe16ff831cbd4459c6f62f8c845b0ccdd31caf068c84a26"  # noqa: E501
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
