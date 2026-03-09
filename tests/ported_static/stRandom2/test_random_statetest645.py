"""
Geth Failed this test on Frontier and Homestead.

Ported from:
tests/static/state_tests/stRandom2/randomStatetest645Filler.json
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
    ["tests/static/state_tests/stRandom2/randomStatetest645Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_value, expected_post",
    [
        (
            4074160023,
            {
                Address("0x322c72dedad1a81092ab9ba908fbec8779ce1c32"): Account(
                    code=bytes.fromhex(
                        "58679b8e24022d8c28f3620b55a06384bc2f83136515b61916f0f579ea3e9d28799d45aa77bf1fc1a84edf0193dea2d610209eaaf9c814"  # noqa: E501
                    )
                ),
                Address("0xaa0103980a7c3113d3a8f81478b0281492eb3d38"): Account(
                    code=bytes.fromhex(
                        "63cbb01282621d72de5268022948f746c938a0cb7c01ef17f23ed237d9f3262c4eb1b95112820595b127c516074df06223db7e0c396eb18074f148d96fd766dda35b6cc250661b5f83f0ed625ba68a5ff49aa1"  # noqa: E501
                    )
                ),
            },
        ),
        (
            0,
            {
                Address("0x322c72dedad1a81092ab9ba908fbec8779ce1c32"): Account(
                    code=bytes.fromhex(
                        "58679b8e24022d8c28f3620b55a06384bc2f83136515b61916f0f579ea3e9d28799d45aa77bf1fc1a84edf0193dea2d610209eaaf9c814"  # noqa: E501
                    )
                ),
                Address("0xaa0103980a7c3113d3a8f81478b0281492eb3d38"): Account(
                    code=bytes.fromhex(
                        "63cbb01282621d72de5268022948f746c938a0cb7c01ef17f23ed237d9f3262c4eb1b95112820595b127c516074df06223db7e0c396eb18074f148d96fd766dda35b6cc250661b5f83f0ed625ba68a5ff49aa1"  # noqa: E501
                    )
                ),
            },
        ),
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_random_statetest645(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_value: int,
    expected_post: dict,
) -> None:
    """Geth Failed this test on Frontier and Homestead."""
    coinbase = Address("0xaa0103980a7c3113d3a8f81478b0281492eb3d38")
    sender = Address("0xf2a0abc1a62216629b2c1aad302408e8e6054a61")
    contract = Address("0x0000000000000000000000000000000000000003")
    callee = Address("0x322c72dedad1a81092ab9ba908fbec8779ce1c32")
    callee_1 = Address("0x9e9c03f8f885c32813db5207fd04870f08327f30")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=13175566155172316,
    )

    pre[callee] = Account(
        balance=0xBCBAF5A33577F162,
        nonce=29,
        code=bytes.fromhex(
            "58679b8e24022d8c28f3620b55a06384bc2f83136515b61916f0f579ea3e9d28799d45aa"  # noqa: E501
            "77bf1fc1a84edf0193dea2d610209eaaf9c814"
        ),
    )
    pre[callee_1] = Account(balance=0xB3508C0F8A22F8A1, nonce=28)
    pre[coinbase] = Account(
        balance=0x2BE1CFD5D6D6B0B7,
        nonce=175,
        code=bytes.fromhex(
            "63cbb01282621d72de5268022948f746c938a0cb7c01ef17f23ed237d9f3262c4eb1b951"  # noqa: E501
            "12820595b127c516074df06223db7e0c396eb18074f148d96fd766dda35b6cc250661b5f"  # noqa: E501
            "83f0ed625ba68a5ff49aa1"
        ),
    )
    pre[sender] = Account(balance=0x6F1F70FEA641F30A, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x0e5fb93861a38e5458e9d2ff0203d01d1d8167fa9c0db762cc5ca50eb43b3376"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex(
            "326e3696ffc10e3e95c67d29784a35ba967d416feb1e1712098bcbb4d20454c1681694f5"  # noqa: E501
            "1d8591ff7b80f0e4da50c89a0a777fa7666abccfbd600e213bd71da4925c2a2115799e9c"  # noqa: E501
            "3bb1622f075452"
        ),
        gas_limit=26970,
        gas_price=10,
        nonce=0,
        value=tx_value,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
