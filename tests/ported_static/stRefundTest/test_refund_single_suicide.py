"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRefundTest/refund_singleSuicideFiller.json
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
    ["tests/static/state_tests/stRefundTest/refund_singleSuicideFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_refund_single_suicide(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0xeb201d2887816e041f6e807e804f64f3a7a226fe")
    sender = Address("0xdf2e264abeec114532b73774cfa1994aed66a9f6")
    contract = Address("0xfc2c9403120f755b844fd30d99c231483e701631")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    pre[sender] = Account(balance=0x1C9C380, nonce=0)
    pre[coinbase] = Account(balance=0, nonce=1)
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "606060405260e060020a600035046309e587a58114602e5780632e4699ed146049578063"  # noqa: E501
            "c040622614609b575b005b602c3373ffffffffffffffffffffffffffffffffffffffff16"  # noqa: E501
            "ff5b602c5b60003090508073ffffffffffffffffffffffffffffffffffffffff166309e5"  # noqa: E501
            "87a56040518160e060020a0281526004018090506000604051808303816000876161da5a"  # noqa: E501
            "03f11560025750505050565b60a5600060b9604c565b6040805191151582525190819003"  # noqa: E501
            "60200190f35b5060019056"
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0x2b75d0c814eb07c075fccbdd9a036faf651d9c46d7477d6c4f30772cfca90d38"  # noqa: E501
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
                "606060405260e060020a600035046309e587a58114602e5780632e4699ed146049578063c040622614609b575b005b602c3373ffffffffffffffffffffffffffffffffffffffff16ff5b602c5b60003090508073ffffffffffffffffffffffffffffffffffffffff166309e587a56040518160e060020a0281526004018090506000604051808303816000876161da5a03f11560025750505050565b60a5600060b9604c565b604080519115158252519081900360200190f35b5060019056"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
