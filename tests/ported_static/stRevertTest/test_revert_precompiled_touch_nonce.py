"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRevertTest/RevertPrecompiledTouch_nonceFiller.json
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
        "tests/static/state_tests/stRevertTest/RevertPrecompiledTouch_nonceFiller.json",  # noqa: E501
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
def test_revert_precompiled_touch_nonce(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x68795c4aa09d6f4ed3e5deddf8c2ad3049a601da")
    sender = Address("0xadd22153059388891d82c6c8e08d80845352bbb0")
    contract = Address("0xe7c596de24ccc387daa5c017066aeb25ea8d2f3f")
    callee = Address("0x05a4faf1ede8e96aae92ae51915074e42787f868")
    callee_1 = Address("0x10ef6d6218ada53728683cec4d5160c8c72159bd")
    callee_2 = Address("0x31f52a66cf9d94c60f089a2ca9c4e784261c57fa")
    callee_3 = Address("0x4ba6259bb96e9d7822a5fb3a1f8037bc68a08d43")
    callee_4 = Address("0x6a22458e937f487e2daffa193b9c5fb610dc4789")
    callee_5 = Address("0x87aaeb9e422487283b0b008ef445e32acb9dd1ae")
    callee_6 = Address("0x8d1d883976df004b96c383782a828dc5bc82ef9d")
    callee_7 = Address("0xb478e245708be95c33c6c35dea161c0429d02dd2")
    callee_8 = Address("0xbeb47e021a70649b079c4bdf150108c0d8c6accb")
    callee_9 = Address("0xde1200b7ecaea2d15b57d0f331ad5ade8e924255")
    callee_10 = Address("0xeb201d2887816e041f6e807e804f64f3a7a226fe")
    callee_11 = Address("0xf8f0aec70f4bbdadce829783a0afff43f384c640")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=4012015,
    )

    pre[callee] = Account(balance=0, nonce=1)
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
    pre[callee_3] = Account(balance=0, nonce=1)
    pre[callee_4] = Account(balance=0, nonce=1)
    pre[callee_5] = Account(
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
    pre[callee_6] = Account(balance=0, nonce=1)
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=1)
    pre[callee_7] = Account(balance=0, nonce=1)
    pre[callee_8] = Account(balance=0, nonce=1)
    pre[callee_9] = Account(
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
    pre[callee_10] = Account(balance=0, nonce=1)
    pre[callee_11] = Account(balance=0, nonce=1)

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
        callee_5: Account(
            code=bytes.fromhex(
                "60006000600060006000600161c350f15060006000600060006000600261c350f15060006000600060006000600361c350f15060006000600060006000600461c350f15060006000600060006000600561c350f15060006000600060006000600661c350f15060006000600060006000600761c350f15060006000600060006000600861c350f1505a6001555a6002555a60035500"  # noqa: E501
            ),
        ),
        callee_9: Account(
            code=bytes.fromhex(
                "60006000600060006000600161c350f25060006000600060006000600261c350f25060006000600060006000600361c350f25060006000600060006000600461c350f25060006000600060006000600561c350f25060006000600060006000600661c350f25060006000600060006000600761c350f25060006000600060006000600861c350f2505a6001555a6002555a60035500"  # noqa: E501
            ),
        ),
        contract: Account(
            code=bytes.fromhex("600060006000600060006000355af200"),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
