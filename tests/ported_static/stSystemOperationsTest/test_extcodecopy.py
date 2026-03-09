"""
God knows what is happening in this test.

Ported from:
tests/static/state_tests/stSystemOperationsTest/extcodecopyFiller.json
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
    ["tests/static/state_tests/stSystemOperationsTest/extcodecopyFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_extcodecopy(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """God knows what is happening in this test."""
    coinbase = Address("0x4401fcaf7d64d53fb1cfc5c9045c32aa919a8c82")
    sender = Address("0x6a3c158cfb89cd1c76fe54bc718c35f90ffe95ca")
    contract = Address("0x0614253558ab9d138504425f7c247229db2c5baf")
    callee = Address("0x5b400827141a956ceb3e889ad3e1707aee1a575c")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1478962728,
    )

    pre[contract] = Account(
        balance=0x5C81EB0,
        nonce=254,
        code=bytes.fromhex(
            "7f15688566a82f5f946c68028bf626b349e495daa43e33529a76437ac416cd1b7d6e7dae"  # noqa: E501
            "7454bb193b1c28e64a6a935bc373cea0c5cc171fa61277e5604a3bc8aef4de3d38820658"  # noqa: E501
            "600b80797ada6e82e95f6520383f95f5c7dae56b4dc13b6f22ecabfce07c3cff51"  # noqa: E501
        ),
    )
    pre[callee] = Account(
        balance=0x4D6769F8,
        nonce=221,
        code=bytes.fromhex(
            "5a60106017601160116018601c600f601b601d5f60026013600f601a8d5a5b7679177b5d"  # noqa: E501
            "d41a23db52998c4dcd14e88390dcc9f3ed5783601660145f6013600d601f60016011600e"  # noqa: E501
            "600c600d601f60138c7a58f20fd882eb51408a52e569ce80e93270ab53ae9de3fec5498a"  # noqa: E501
            "5c72ce1fcd11bb1553736959df779a616b738c1f407c12459490afe302da311a673488d0"  # noqa: E501
            "9e71041d0761dee4829e3c38e0b1b1787810f2e11e2289983c1ab47cf5ebd38c12f17192"  # noqa: E501
            "32b5f3a7b27a9ea8858a071c4169392ec725646311235cbd9534e5d7cd8cb5e2287738a4"  # noqa: E501
            "3f803384f4e62fe6629ea2e609a71759edab5c3a58b87e94c95f710aa6059b0663c9f374"  # noqa: E501
            "ce6ea0a000c5d594c41252d4a74d64896a987cc57c24df2ce8ffb85adcc27dce2d19f700"  # noqa: E501
            "6fbc1c5a7b79a319418fd6c27ddebcf170192262d82c1053333f6115c8b258b81e2e84d7"  # noqa: E501
            "23c98dbd4535de7f922723a15827bbcfd07f9e2c5027c7736ed68c61b332059d7ec1bae1"  # noqa: E501
            "c1fd41a361d35b996d9740a588b6abf3293236afb927717328c014846148ce67eaf2b33d"  # noqa: E501
            "90672366dafeaae0714eb39e7fd5076a831d8eb4a3546288a3e1a0087aebe80b6bbfa404"  # noqa: E501
            "1330b05d094a697236fe7654d8a7ce630f83a832620125d781666e898f7fdcfd0031"  # noqa: E501
        ),
    )
    pre[sender] = Account(balance=0x4F6CA7B90CEB5FD4, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x7446b5f5f4c3994ba600da46b6ca0e5dbd71bce76740b040ba716507ecb75bb9"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex(
            "6e27b0577f2549e5fa01e3db96e7b03a62e489115538620295677faf15040c1c1796bad1"  # noqa: E501
            "30e2462a8b8d6bbe0fa35bf12087047ef4ff4e66df8772196b4401998ff7f4219c013a0d"  # noqa: E501
            "927b22d8d3fdf625809abb182507d180e687b666f4f1e4f3b8172e87760f436c701264b8"  # noqa: E501
            "9739f3d7c50ec524f16b1a4f91397b760a5209b9b7710544694ecf2729643b3ca545c7"  # noqa: E501
        ),
        gas_limit=100000,
        gas_price=483694712,
        nonce=0,
        value=614700887,
    )

    post = {
        contract: Account(
            code=bytes.fromhex(
                "7f15688566a82f5f946c68028bf626b349e495daa43e33529a76437ac416cd1b7d6e7dae7454bb193b1c28e64a6a935bc373cea0c5cc171fa61277e5604a3bc8aef4de3d38820658600b80797ada6e82e95f6520383f95f5c7dae56b4dc13b6f22ecabfce07c3cff51"  # noqa: E501
            ),
        ),
        callee: Account(
            code=bytes.fromhex(
                "5a60106017601160116018601c600f601b601d5f60026013600f601a8d5a5b7679177b5dd41a23db52998c4dcd14e88390dcc9f3ed5783601660145f6013600d601f60016011600e600c600d601f60138c7a58f20fd882eb51408a52e569ce80e93270ab53ae9de3fec5498a5c72ce1fcd11bb1553736959df779a616b738c1f407c12459490afe302da311a673488d09e71041d0761dee4829e3c38e0b1b1787810f2e11e2289983c1ab47cf5ebd38c12f1719232b5f3a7b27a9ea8858a071c4169392ec725646311235cbd9534e5d7cd8cb5e2287738a43f803384f4e62fe6629ea2e609a71759edab5c3a58b87e94c95f710aa6059b0663c9f374ce6ea0a000c5d594c41252d4a74d64896a987cc57c24df2ce8ffb85adcc27dce2d19f7006fbc1c5a7b79a319418fd6c27ddebcf170192262d82c1053333f6115c8b258b81e2e84d723c98dbd4535de7f922723a15827bbcfd07f9e2c5027c7736ed68c61b332059d7ec1bae1c1fd41a361d35b996d9740a588b6abf3293236afb927717328c014846148ce67eaf2b33d90672366dafeaae0714eb39e7fd5076a831d8eb4a3546288a3e1a0087aebe80b6bbfa4041330b05d094a697236fe7654d8a7ce630f83a832620125d781666e898f7fdcfd0031"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
