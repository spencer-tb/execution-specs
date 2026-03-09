"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRefundTest/refund_multimpleSuicideFiller.json
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
        "tests/static/state_tests/stRefundTest/refund_multimpleSuicideFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_refund_multimple_suicide(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0xeb201d2887816e041f6e807e804f64f3a7a226fe")
    sender = Address("0x2f8048c9a8457f574cd0c45ee76b2fcfdf464e8b")
    contract = Address("0x8b9574e5049501f581886404adf7037002276e78")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    pre[sender] = Account(balance=0x623A7C0, nonce=0)
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "606060405260e060020a600035046309e587a58114610031578063c04062261461004d57"  # noqa: E501
            "8063dd4f1f2a1461005a575b005b61002f3373ffffffffffffffffffffffffffffffffff"  # noqa: E501
            "ffffff16ff5b6100f5600061010961005e565b61002f5b60003090508073ffffffffffff"  # noqa: E501
            "ffffffffffffffffffffffffffff166309e587a56040518160e060020a02815260040180"  # noqa: E501
            "90506000604051808303816000876161da5a03f1156100025750604080517f09e587a500"  # noqa: E501
            "000000000000000000000000000000000000000000000000000000815290516004828101"  # noqa: E501
            "926000929190829003018183876161da5a03f1156100025750505050565b604080519115"  # noqa: E501
            "158252519081900360200190f35b5060019056"
        ),
    )
    pre[coinbase] = Account(balance=0, nonce=1)

    tx = Transaction(
        secret_key=Hash(
            "0xc69694690a07d1418b0aadfd424a00ea9f25d84b94fecef12943de9cd38ede14"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex("c0406226"),
        gas_limit=300000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            code=bytes.fromhex(
                "606060405260e060020a600035046309e587a58114610031578063c04062261461004d578063dd4f1f2a1461005a575b005b61002f3373ffffffffffffffffffffffffffffffffffffffff16ff5b6100f5600061010961005e565b61002f5b60003090508073ffffffffffffffffffffffffffffffffffffffff166309e587a56040518160e060020a0281526004018090506000604051808303816000876161da5a03f1156100025750604080517f09e587a500000000000000000000000000000000000000000000000000000000815290516004828101926000929190829003018183876161da5a03f1156100025750505050565b604080519115158252519081900360200190f35b5060019056"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
