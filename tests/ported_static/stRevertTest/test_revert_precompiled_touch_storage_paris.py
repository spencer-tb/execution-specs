"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRevertTest
RevertPrecompiledTouch_storage_ParisFiller.json
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
        "tests/static/state_tests/stRevertTest/RevertPrecompiledTouch_storage_ParisFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex",
    [
        "00000000000000000000000087aaeb9e422487283b0b008ef445e32acb9dd1ae",
        "00000000000000000000000031f52a66cf9d94c60f089a2ca9c4e784261c57fa",
        "000000000000000000000000de1200b7ecaea2d15b57d0f331ad5ade8e924255",
        "00000000000000000000000010ef6d6218ada53728683cec4d5160c8c72159bd",
    ],
    ids=["case0", "case1", "case2", "case3"],
)
@pytest.mark.pre_alloc_mutable
def test_revert_precompiled_touch_storage_paris(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x68795c4aa09d6f4ed3e5deddf8c2ad3049a601da")
    sender = Address("0xadd22153059388891d82c6c8e08d80845352bbb0")
    contract = Address("0xe7c596de24ccc387daa5c017066aeb25ea8d2f3f")
    callee = Address("0x0dc4b229346287fe9fa441960081a9886b71c42d")
    callee_1 = Address("0x10ef6d6218ada53728683cec4d5160c8c72159bd")
    callee_2 = Address("0x31f52a66cf9d94c60f089a2ca9c4e784261c57fa")
    callee_3 = Address("0x3a3eee808c401a574f92824dc64d89edb05fafe4")
    callee_4 = Address("0x46ac2e7e1550d911e5a72fbc51c15ca817dbb1d5")
    callee_5 = Address("0x4757608f18b70777ae788dd4056eeed52f7aa68f")
    callee_6 = Address("0x6d15138ce372d9b89ee38fc3973b715477426f11")
    callee_7 = Address("0x87aaeb9e422487283b0b008ef445e32acb9dd1ae")
    callee_8 = Address("0x9deb46a3b3e955bd56ecc4072da4b42bd9b5db2c")
    callee_9 = Address("0xa8fd4cb9c2c538ed7ff94c3b711b2e08a08c7fb8")
    callee_10 = Address("0xda7f8add6896b7e58f28331a97b315dde5fb8cd1")
    callee_11 = Address("0xde1200b7ecaea2d15b57d0f331ad5ade8e924255")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=4012015,
    )

    pre[callee] = Account(balance=10, nonce=0, storage={0x0: 0x1})
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "6000600060006000600161c350fa506000600060006000600261c350fa50600060006000"  # noqa: E501
            "6000600361c350fa506000600060006000600461c350fa506000600060006000600561c3"  # noqa: E501
            "50fa506000600060006000600661c350fa506000600060006000600761c350fa50600060"  # noqa: E501
            "0060006000600861c350fa505a6001555a6002555a60035500"
        ),
    )
    pre[callee_2] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "6000600060006000600161c350f4506000600060006000600261c350f450600060006000"  # noqa: E501
            "6000600361c350f4506000600060006000600461c350f4506000600060006000600561c3"  # noqa: E501
            "50f4506000600060006000600661c350f4506000600060006000600761c350f450600060"  # noqa: E501
            "0060006000600861c350f4505a6001555a6002555a60035500"
        ),
    )
    pre[callee_3] = Account(balance=10, nonce=0, storage={0x0: 0x1})
    pre[callee_4] = Account(balance=10, nonce=0, storage={0x0: 0x1})
    pre[callee_5] = Account(balance=10, nonce=0, storage={0x0: 0x1})
    pre[callee_6] = Account(balance=10, nonce=0, storage={0x0: 0x1})
    pre[callee_7] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "60006000600060006000600161c350f15060006000600060006000600261c350f1506000"  # noqa: E501
            "6000600060006000600361c350f15060006000600060006000600461c350f15060006000"  # noqa: E501
            "600060006000600561c350f15060006000600060006000600661c350f150600060006000"  # noqa: E501
            "60006000600761c350f15060006000600060006000600861c350f1505a6001555a600255"  # noqa: E501
            "5a60035500"
        ),
    )
    pre[callee_8] = Account(balance=10, nonce=0, storage={0x0: 0x1})
    pre[callee_9] = Account(balance=10, nonce=0, storage={0x0: 0x1})
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=1)
    pre[callee_10] = Account(balance=10, nonce=0, storage={0x0: 0x1})
    pre[callee_11] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "60006000600060006000600161c350f25060006000600060006000600261c350f2506000"  # noqa: E501
            "6000600060006000600361c350f25060006000600060006000600461c350f25060006000"  # noqa: E501
            "600060006000600561c350f25060006000600060006000600661c350f250600060006000"  # noqa: E501
            "60006000600761c350f25060006000600060006000600861c350f2505a6001555a600255"  # noqa: E501
            "5a60035500"
        ),
    )
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("600060006000600060006000355af200"),
    )

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x0ff8d58222f34f6890ddaa468c023b77d6691ed7d3c4dcddae38336212faf54b"  # noqa: E501
        ),
        to=contract,
        data=tx_data,
        gas_limit=100000,
        gas_price=10,
        nonce=1,
        value=0,
    )

    post = {
        callee: Account(storage={0: 1}),
        callee_1: Account(
            code=bytes.fromhex(
                "6000600060006000600161c350fa506000600060006000600261c350fa506000600060006000600361c350fa506000600060006000600461c350fa506000600060006000600561c350fa506000600060006000600661c350fa506000600060006000600761c350fa506000600060006000600861c350fa505a6001555a6002555a60035500"  # noqa: E501
            ),
        ),
        callee_2: Account(
            code=bytes.fromhex(
                "6000600060006000600161c350f4506000600060006000600261c350f4506000600060006000600361c350f4506000600060006000600461c350f4506000600060006000600561c350f4506000600060006000600661c350f4506000600060006000600761c350f4506000600060006000600861c350f4505a6001555a6002555a60035500"  # noqa: E501
            ),
        ),
        callee_3: Account(storage={0: 1}),
        callee_4: Account(storage={0: 1}),
        callee_5: Account(storage={0: 1}),
        callee_6: Account(storage={0: 1}),
        callee_7: Account(
            code=bytes.fromhex(
                "60006000600060006000600161c350f15060006000600060006000600261c350f15060006000600060006000600361c350f15060006000600060006000600461c350f15060006000600060006000600561c350f15060006000600060006000600661c350f15060006000600060006000600761c350f15060006000600060006000600861c350f1505a6001555a6002555a60035500"  # noqa: E501
            ),
        ),
        callee_8: Account(storage={0: 1}),
        callee_9: Account(storage={0: 1}),
        callee_10: Account(storage={0: 1}),
        callee_11: Account(
            code=bytes.fromhex(
                "60006000600060006000600161c350f25060006000600060006000600261c350f25060006000600060006000600361c350f25060006000600060006000600461c350f25060006000600060006000600561c350f25060006000600060006000600661c350f25060006000600060006000600761c350f25060006000600060006000600861c350f2505a6001555a6002555a60035500"  # noqa: E501
            ),
        ),
        contract: Account(
            code=bytes.fromhex("600060006000600060006000355af200"),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
