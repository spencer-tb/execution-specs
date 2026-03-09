"""
A single contract can execute SELFDESTRUCT multiple times using by being...

multiple times. The second and later SELFDESTRUCTs have little effect but can
touch some new beneficiary addresses.

Ported from:
tests/static/state_tests/stSystemOperationsTest
doubleSelfdestructTouch_ParisFiller.yml
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
        "tests/static/state_tests/stSystemOperationsTest/doubleSelfdestructTouch_ParisFiller.yml",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_value, expected_post",
    [
        (
            0,
            {
                Address("0x29e4504a3d2a0e0ae0ebbbefedd4570639b3ebee"): Account(
                    storage={
                        0: 2,
                        1: 0x68FA59E127B7526718EB0A4E113DF5793628CB91,
                        2: 0x76FAE819612A29489A1A43208613D8F8557B8898,
                    },
                    code=bytes.fromhex("6001600054018060005554ff"),
                ),
                Address("0x8ec7465877d3957084dc907c0f6d8f2911a17a52"): Account(
                    code=bytes.fromhex(
                        "6000808080348060011c9082808080857329e4504a3d2a0e0ae0ebbbefedd4570639b3ebee62011170f150037329e4504a3d2a0e0ae0ebbbefedd4570639b3ebee62011170f100"  # noqa: E501
                    )
                ),
            },
        ),
        (
            1,
            {
                Address("0x29e4504a3d2a0e0ae0ebbbefedd4570639b3ebee"): Account(
                    storage={
                        0: 2,
                        1: 0x68FA59E127B7526718EB0A4E113DF5793628CB91,
                        2: 0x76FAE819612A29489A1A43208613D8F8557B8898,
                    },
                    code=bytes.fromhex("6001600054018060005554ff"),
                ),
                Address("0x8ec7465877d3957084dc907c0f6d8f2911a17a52"): Account(
                    code=bytes.fromhex(
                        "6000808080348060011c9082808080857329e4504a3d2a0e0ae0ebbbefedd4570639b3ebee62011170f150037329e4504a3d2a0e0ae0ebbbefedd4570639b3ebee62011170f100"  # noqa: E501
                    )
                ),
            },
        ),
        (
            2,
            {
                Address("0x29e4504a3d2a0e0ae0ebbbefedd4570639b3ebee"): Account(
                    storage={
                        0: 2,
                        1: 0x68FA59E127B7526718EB0A4E113DF5793628CB91,
                        2: 0x76FAE819612A29489A1A43208613D8F8557B8898,
                    },
                    code=bytes.fromhex("6001600054018060005554ff"),
                ),
                Address("0x8ec7465877d3957084dc907c0f6d8f2911a17a52"): Account(
                    code=bytes.fromhex(
                        "6000808080348060011c9082808080857329e4504a3d2a0e0ae0ebbbefedd4570639b3ebee62011170f150037329e4504a3d2a0e0ae0ebbbefedd4570639b3ebee62011170f100"  # noqa: E501
                    )
                ),
            },
        ),
    ],
    ids=["case0", "case1", "case2"],
)
@pytest.mark.pre_alloc_mutable
def test_double_selfdestruct_touch_paris(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_value: int,
    expected_post: dict,
) -> None:
    """A single contract can execute SELFDESTRUCT multiple times using..."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x3a164fee089b5ce1f6f7071e90f56caeb7f19b1d")
    contract = Address("0x8ec7465877d3957084dc907c0f6d8f2911a17a52")
    callee = Address("0x29e4504a3d2a0e0ae0ebbbefedd4570639b3ebee")
    callee_1 = Address("0x68fa59e127b7526718eb0a4e113df5793628cb91")
    callee_2 = Address("0x76fae819612a29489a1a43208613d8f8557b8898")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=999,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=30000000,
    )

    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("6001600054018060005554ff"),
        storage={
            0x0: 0x0,
            0x1: 0x68FA59E127B7526718EB0A4E113DF5793628CB91,
            0x2: 0x76FAE819612A29489A1A43208613D8F8557B8898,
        },
    )
    pre[sender] = Account(balance=0x5F5E102, nonce=0)
    pre[callee_1] = Account(balance=10, nonce=0)
    pre[callee_2] = Account(balance=10, nonce=0)
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "6000808080348060011c9082808080857329e4504a3d2a0e0ae0ebbbefedd4570639b3eb"  # noqa: E501
            "ee62011170f150037329e4504a3d2a0e0ae0ebbbefedd4570639b3ebee62011170f100"  # noqa: E501
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xe92c121432830128ca66d3d8c4e6d8d96cc4befa7c612d28415082eb3c8339c5"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=10000000,
        gas_price=10,
        nonce=0,
        value=tx_value,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
