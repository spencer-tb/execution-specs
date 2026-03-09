"""
Test ported from static filler.

Ported from:
tests/static/state_tests/Shanghai/stEIP3860_limitmeterinitcode
create2InitCodeSizeLimitFiller.yml
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
        "tests/static/state_tests/Shanghai/stEIP3860_limitmeterinitcode/create2InitCodeSizeLimitFiller.yml",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        (
            "000000000000000000000000000000000000000000000000000000000000c001",
            {
                Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(
                    storage={1: 1},
                    code=bytes.fromhex(
                        "60003560005260008036818073c94f5374fce5edbc8e2a8697c15331677e6ebf0b62989680f16000556001805500"  # noqa: E501
                    ),
                ),
                Address("0xc94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(
                    code=bytes.fromhex(
                        "69600a80600080396000f360b01b60009081523563deadbeef5a91600080f5905a9003600a5560005500"  # noqa: E501
                    )
                ),
            },
        ),
        (
            "000000000000000000000000000000000000000000000000000000000000c000",
            {
                Address("0x9e7a3337d18c31fe4c1fe51ab2da6cfd3629923d"): Account(
                    code=bytes.fromhex("600a80600080396000f3")
                ),
                Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(
                    storage={0: 1, 1: 1},
                    code=bytes.fromhex(
                        "60003560005260008036818073c94f5374fce5edbc8e2a8697c15331677e6ebf0b62989680f16000556001805500"  # noqa: E501
                    ),
                ),
                Address("0xc94f5374fce5edbc8e2a8697c15331677e6ebf0b"): Account(
                    storage={
                        0: 0x9E7A3337D18C31FE4C1FE51AB2DA6CFD3629923D,
                        10: 55539,
                    },
                    code=bytes.fromhex(
                        "69600a80600080396000f360b01b60009081523563deadbeef5a91600080f5905a9003600a5560005500"  # noqa: E501
                    ),
                ),
            },
        ),
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_create2_init_code_size_limit(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    callee = Address("0xc94f5374fce5edbc8e2a8697c15331677e6ebf0b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=20000000,
    )

    pre[sender] = Account(balance=0xBEBC200, nonce=0)
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "60003560005260008036818073c94f5374fce5edbc8e2a8697c15331677e6ebf0b629896"  # noqa: E501
            "80f16000556001805500"
        ),
    )
    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "69600a80600080396000f360b01b60009081523563deadbeef5a91600080f5905a900360"  # noqa: E501
            "0a5560005500"
        ),
    )

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=tx_data,
        gas_limit=15000000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
