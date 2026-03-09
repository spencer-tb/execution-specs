"""
create2SmartInitCode. create2 works different each time you call it.

Ported from:
tests/static/state_tests/stCreate2/create2SmartInitCodeFiller.json
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
    ["tests/static/state_tests/stCreate2/create2SmartInitCodeFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        (
            "0000000000000000000000000f572e5295c57f15886f9b263e2f6d2d6c7b5ec6",
            {
                Address("0x0f572e5295c57f15886f9b263e2f6d2d6c7b5ec6"): Account(
                    storage={1: 0xF6510583D425CFCF94B99F8B073B44F60D1912B},
                    code=bytes.fromhex(
                        "7a600060015414601157600a6000f3601a565b60016001556001ff5b6000526000601b60056001f56001556000601b60056001f560025500"  # noqa: E501
                    ),
                ),
                Address("0x1f572e5295c57f15886f9b263e2f6d2d6c7b5ec6"): Account(
                    code=bytes.fromhex(
                        "7c600060015414601157600a6000f3601c565b6001600155600a6000f35b6000526000601d60036001f56001556000601b60056001f560025500"  # noqa: E501
                    )
                ),
                Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(
                    code=bytes.fromhex("600060006000600060006000355af100")
                ),
            },
        ),
        (
            "0000000000000000000000001f572e5295c57f15886f9b263e2f6d2d6c7b5ec6",
            {
                Address("0x0f572e5295c57f15886f9b263e2f6d2d6c7b5ec6"): Account(
                    code=bytes.fromhex(
                        "7a600060015414601157600a6000f3601a565b60016001556001ff5b6000526000601b60056001f56001556000601b60056001f560025500"  # noqa: E501
                    )
                ),
                Address("0x1f572e5295c57f15886f9b263e2f6d2d6c7b5ec6"): Account(
                    storage={1: 0xD27E800C69122409AC5609FE4DF903745F3988A0},
                    code=bytes.fromhex(
                        "7c600060015414601157600a6000f3601c565b6001600155600a6000f35b6000526000601d60036001f56001556000601b60056001f560025500"  # noqa: E501
                    ),
                ),
                Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(
                    code=bytes.fromhex("600060006000600060006000355af100")
                ),
                Address("0xd27e800c69122409ac5609fe4df903745f3988a0"): Account(
                    storage={1: 1}, code=bytes.fromhex("00000000000000000000")
                ),
            },
        ),
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_create2_smart_init_code(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Create2SmartInitCode. create2 works different each time you call it."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    callee = Address("0x0f572e5295c57f15886f9b263e2f6d2d6c7b5ec6")
    callee_1 = Address("0x1f572e5295c57f15886f9b263e2f6d2d6c7b5ec6")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=47244640256,
    )

    pre[callee] = Account(
        balance=100,
        nonce=0,
        code=bytes.fromhex(
            "7a600060015414601157600a6000f3601a565b60016001556001ff5b6000526000601b60"  # noqa: E501
            "056001f56001556000601b60056001f560025500"
        ),
    )
    pre[callee_1] = Account(
        balance=100,
        nonce=0,
        code=bytes.fromhex(
            "7c600060015414601157600a6000f3601c565b6001600155600a6000f35b600052600060"  # noqa: E501
            "1d60036001f56001556000601b60056001f560025500"
        ),
    )
    pre[sender] = Account(balance=0x6400000000, nonce=0)
    pre[contract] = Account(
        balance=0x6400000000,
        nonce=0,
        code=bytes.fromhex("600060006000600060006000355af100"),
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
        nonce=0,
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
