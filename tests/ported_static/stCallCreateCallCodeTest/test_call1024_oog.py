"""
calldepth with oog.

Ported from:
tests/static/state_tests/stCallCreateCallCodeTest/Call1024OOGFiller.json
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
        "tests/static/state_tests/stCallCreateCallCodeTest/Call1024OOGFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit, expected_post",
    [
        (
            13120826,
            {
                Address("0x0878bc1c3d660907b056e31c854a309f7ef1b4c4"): Account(
                    storage={0: 134, 1: 1, 2: 0x20B71},
                    code=bytes.fromhex(
                        "60016000540160005560006000600060006000730878bc1c3d660907b056e31c854a309f7ef1b4c4610401600054046001036127105a0302f16001556103e86000540260010160025500"  # noqa: E501
                    ),
                )
            },
        ),
        (
            9320826,
            {
                Address("0x0878bc1c3d660907b056e31c854a309f7ef1b4c4"): Account(
                    storage={0: 113, 1: 1, 2: 0x1B969},
                    code=bytes.fromhex(
                        "60016000540160005560006000600060006000730878bc1c3d660907b056e31c854a309f7ef1b4c4610401600054046001036127105a0302f16001556103e86000540260010160025500"  # noqa: E501
                    ),
                )
            },
        ),
        (
            15720826,
            {
                Address("0x0878bc1c3d660907b056e31c854a309f7ef1b4c4"): Account(
                    storage={0: 146, 1: 1, 2: 0x23A51},
                    code=bytes.fromhex(
                        "60016000540160005560006000600060006000730878bc1c3d660907b056e31c854a309f7ef1b4c4610401600054046001036127105a0302f16001556103e86000540260010160025500"  # noqa: E501
                    ),
                )
            },
        ),
        (
            11220826,
            {
                Address("0x0878bc1c3d660907b056e31c854a309f7ef1b4c4"): Account(
                    storage={0: 124, 1: 1, 2: 0x1E461},
                    code=bytes.fromhex(
                        "60016000540160005560006000600060006000730878bc1c3d660907b056e31c854a309f7ef1b4c4610401600054046001036127105a0302f16001556103e86000540260010160025500"  # noqa: E501
                    ),
                )
            },
        ),
    ],
    ids=["case0", "case1", "case2", "case3"],
)
@pytest.mark.pre_alloc_mutable
def test_call1024_oog(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
    expected_post: dict,
) -> None:
    """Calldepth with oog."""
    coinbase = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    sender = Address("0x4768b5e50b0ebe91ae38d84a47e3179e615f9c40")
    contract = Address("0x0878bc1c3d660907b056e31c854a309f7ef1b4c4")
    callee = Address("0xd9b97c712ebce43f3c19179bbef44b550f9e8bc0")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[contract] = Account(
        balance=1024,
        nonce=0,
        code=bytes.fromhex(
            "60016000540160005560006000600060006000730878bc1c3d660907b056e31c854a309f"  # noqa: E501
            "7ef1b4c4610401600054046001036127105a0302f16001556103e8600054026001016002"  # noqa: E501
            "5500"
        ),
    )
    pre[sender] = Account(balance=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF, nonce=0)
    pre[callee] = Account(balance=7000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xe7c72b378297589acee4e0ba3272841bcfc5e220f86de253f890274cfee9e474"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=10,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
