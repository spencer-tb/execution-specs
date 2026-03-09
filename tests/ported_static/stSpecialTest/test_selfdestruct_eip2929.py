"""
Martin: @tkstanczak requested a state-test regarding selfdestructs in...

Ported from:
tests/static/state_tests/stSpecialTest/selfdestructEIP2929Filler.json
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
    ["tests/static/state_tests/stSpecialTest/selfdestructEIP2929Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_selfdestruct_eip2929(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Martin: @tkstanczak requested a state-test regarding..."""
    coinbase = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    sender = Address("0x2e3d0156d2b99a6eacba540c55f423c8f5a33143")
    contract = Address("0xb686be1a7a0f441fae9583884043ac034fe82089")
    callee = Address("0x7704d8a022a1ba8f3539fc82c7d7fb065abc0df3")
    callee_1 = Address("0x9ecbdbdbd8448cdd955755cdd81d6918e436f68a")
    callee_2 = Address("0xd2e5c26a2f035a63d0859e255621ed1e57148085")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10944489199640098,
    )

    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)
    pre[callee] = Account(balance=0, nonce=1)
    pre[callee_1] = Account(balance=0, nonce=1)
    pre[contract] = Account(
        balance=1,
        nonce=1,
        code=bytes.fromhex(
            "6000600060006000600060cc6000f1506000600060006000600060dd6000f15060006000"  # noqa: E501
            "60006000600060036000f15060aa6000526000600060206000600061dead5af15060aa60"  # noqa: E501
            "00526000600060206000600061dead5af15060bb6000526000600060206000600061dead"  # noqa: E501
            "5af15060bb6000526000600060206000600061dead5af15060cc60005260006000602060"  # noqa: E501
            "00600061dead5af15060cc6000526000600060206000600061dead5af15060dd60005260"  # noqa: E501
            "00600060206000600061dead5af15060dd6000526000600060206000600061dead5af150"  # noqa: E501
            "60016000526000600060206000600061dead5af150600160005260006000602060006000"  # noqa: E501
            "61dead5af15060026000526000600060206000600061dead5af150600260005260006000"  # noqa: E501
            "60206000600061dead5af15060036000526000600060206000600061dead5af150600160"  # noqa: E501
            "0155"
        ),
    )
    pre[callee_2] = Account(
        balance=1,
        nonce=1,
        code=bytes.fromhex(
            "60003574ffffffffffffffffffffffffffffffffffffffffff16ff"
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xb1f4cbc3a50042184425a6f9e996d0910f7ba879457ce5dac5c71e498ad3c005"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=8000000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            storage={1: 1},
            code=bytes.fromhex(
                "6000600060006000600060cc6000f1506000600060006000600060dd6000f1506000600060006000600060036000f15060aa6000526000600060206000600061dead5af15060aa6000526000600060206000600061dead5af15060bb6000526000600060206000600061dead5af15060bb6000526000600060206000600061dead5af15060cc6000526000600060206000600061dead5af15060cc6000526000600060206000600061dead5af15060dd6000526000600060206000600061dead5af15060dd6000526000600060206000600061dead5af15060016000526000600060206000600061dead5af15060016000526000600060206000600061dead5af15060026000526000600060206000600061dead5af15060026000526000600060206000600061dead5af15060036000526000600060206000600061dead5af1506001600155"  # noqa: E501
            ),
        ),
        callee_2: Account(
            code=bytes.fromhex(
                "60003574ffffffffffffffffffffffffffffffffffffffffff16ff"
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
