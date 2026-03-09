"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stMemoryStressTest/DUP_BoundsFiller.json
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
    ["tests/static/state_tests/stMemoryStressTest/DUP_BoundsFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit",
    [
        150000,
        1000000,
        16777216,
    ],
    ids=["case0", "case1", "case2"],
)
@pytest.mark.pre_alloc_mutable
def test_dup_bounds(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xf2f6c03017e58b15115443223a6a0f8a4363b5c1")
    contract = Address("0xe860bd7bf0474923e526cbe86fa5b5f76aee36ed")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "600080505063ffffffff80505067ffffffffffffffff8050506fffffffffffffffffffff"  # noqa: E501
            "ffffffffffff8050507fffffffffffffffffffffffffffffffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffff805050600060008150505063ffffffff63ffffffff8150505067ffffffff"  # noqa: E501
            "ffffffff67ffffffffffffffff815050506fffffffffffffffffffffffffffffffff6fff"  # noqa: E501
            "ffffffffffffffffffffffffffffff815050507fffffffffffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffff81505050600060006000825050505063ffffffff63ffff"  # noqa: E501
            "ffff63ffffffff825050505067ffffffffffffffff67ffffffffffffffff67ffffffffff"  # noqa: E501
            "ffffff82505050506fffffffffffffffffffffffffffffffff6fffffffffffffffffffff"  # noqa: E501
            "ffffffffffff6fffffffffffffffffffffffffffffffff82505050507fffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffff8250505050600060006000600083505050"  # noqa: E501
            "505063ffffffff63ffffffff63ffffffff63ffffffff83505050505067ffffffffffffff"  # noqa: E501
            "ff67ffffffffffffffff67ffffffffffffffff67ffffffffffffffff8350505050506fff"  # noqa: E501
            "ffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffff"  # noqa: E501
            "ffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff835050505050"  # noqa: E501
            "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffffffffffffff835050505050600060006000"  # noqa: E501
            "600060008450505050505063ffffffff63ffffffff63ffffffff63ffffffff63ffffffff"  # noqa: E501
            "8450505050505067ffffffffffffffff67ffffffffffffffff67ffffffffffffffff67ff"  # noqa: E501
            "ffffffffffffff67ffffffffffffffff845050505050506fffffffffffffffffffffffff"  # noqa: E501
            "ffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffff"  # noqa: E501
            "ffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff"  # noqa: E501
            "845050505050507fffffffffffffffffffffffffffffffffffffffffffffffffffffffff"  # noqa: E501
            "ffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"  # noqa: E501
            "ff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffffffffffffffffffffff8450505050505060"  # noqa: E501
            "0060006000600060006000855050505050505063ffffffff63ffffffff63ffffffff63ff"  # noqa: E501
            "ffffff63ffffffff63ffffffff855050505050505067ffffffffffffffff67ffffffffff"  # noqa: E501
            "ffffff67ffffffffffffffff67ffffffffffffffff67ffffffffffffffff67ffffffffff"  # noqa: E501
            "ffffff85505050505050506fffffffffffffffffffffffffffffffff6fffffffffffffff"  # noqa: E501
            "ffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffff"  # noqa: E501
            "ffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffff"  # noqa: E501
            "ffffffffff85505050505050507fffffffffffffffffffffffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffff"  # noqa: E501
            "ffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"  # noqa: E501
            "ff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8550505050"  # noqa: E501
            "505050600060006000600060006000600086505050505050505063ffffffff63ffffffff"  # noqa: E501
            "63ffffffff63ffffffff63ffffffff63ffffffff63ffffffff86505050505050505067ff"  # noqa: E501
            "ffffffffffffff67ffffffffffffffff67ffffffffffffffff67ffffffffffffffff67ff"  # noqa: E501
            "ffffffffffffff67ffffffffffffffff67ffffffffffffffff8650505050505050506fff"  # noqa: E501
            "ffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffff"  # noqa: E501
            "ffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffff"  # noqa: E501
            "ffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffff"  # noqa: E501
            "ffffffffffffffffff8650505050505050507fffffffffffffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"  # noqa: E501
            "ffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"  # noqa: E501
            "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff865050"  # noqa: E501
            "505050505050600060006000600060006000600060008750505050505050505063ffffff"  # noqa: E501
            "ff63ffffffff63ffffffff63ffffffff63ffffffff63ffffffff63ffffffff63ffffffff"  # noqa: E501
            "8750505050505050505067ffffffffffffffff67ffffffffffffffff67ffffffffffffff"  # noqa: E501
            "ff67ffffffffffffffff67ffffffffffffffff67ffffffffffffffff67ffffffffffffff"  # noqa: E501
            "ff67ffffffffffffffff875050505050505050506fffffffffffffffffffffffffffffff"  # noqa: E501
            "ff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6f"  # noqa: E501
            "ffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffff"  # noqa: E501
            "ffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffff"  # noqa: E501
            "ffffffffffffffffffffffff875050505050505050507fffffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffff"  # noqa: E501
            "ffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffff"  # noqa: E501
            "ffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"  # noqa: E501
            "ff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff87"  # noqa: E501
        ),
    )
    pre[sender] = Account(balance=0x7FFFFFFFFFFFFFFF, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x31b5af02b012484ae954b3a43943242ede546a2e76fc0a6acc17435107c385eb"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = {
        contract: Account(
            code=bytes.fromhex(
                "600080505063ffffffff80505067ffffffffffffffff8050506fffffffffffffffffffffffffffffffff8050507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff805050600060008150505063ffffffff63ffffffff8150505067ffffffffffffffff67ffffffffffffffff815050506fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff815050507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff81505050600060006000825050505063ffffffff63ffffffff63ffffffff825050505067ffffffffffffffff67ffffffffffffffff67ffffffffffffffff82505050506fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff82505050507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8250505050600060006000600083505050505063ffffffff63ffffffff63ffffffff63ffffffff83505050505067ffffffffffffffff67ffffffffffffffff67ffffffffffffffff67ffffffffffffffff8350505050506fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff8350505050507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff835050505050600060006000600060008450505050505063ffffffff63ffffffff63ffffffff63ffffffff63ffffffff8450505050505067ffffffffffffffff67ffffffffffffffff67ffffffffffffffff67ffffffffffffffff67ffffffffffffffff845050505050506fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff845050505050507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff84505050505050600060006000600060006000855050505050505063ffffffff63ffffffff63ffffffff63ffffffff63ffffffff63ffffffff855050505050505067ffffffffffffffff67ffffffffffffffff67ffffffffffffffff67ffffffffffffffff67ffffffffffffffff67ffffffffffffffff85505050505050506fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff85505050505050507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8550505050505050600060006000600060006000600086505050505050505063ffffffff63ffffffff63ffffffff63ffffffff63ffffffff63ffffffff63ffffffff86505050505050505067ffffffffffffffff67ffffffffffffffff67ffffffffffffffff67ffffffffffffffff67ffffffffffffffff67ffffffffffffffff67ffffffffffffffff8650505050505050506fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff8650505050505050507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff865050505050505050600060006000600060006000600060008750505050505050505063ffffffff63ffffffff63ffffffff63ffffffff63ffffffff63ffffffff63ffffffff63ffffffff8750505050505050505067ffffffffffffffff67ffffffffffffffff67ffffffffffffffff67ffffffffffffffff67ffffffffffffffff67ffffffffffffffff67ffffffffffffffff67ffffffffffffffff875050505050505050506fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffff875050505050505050507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff87"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
