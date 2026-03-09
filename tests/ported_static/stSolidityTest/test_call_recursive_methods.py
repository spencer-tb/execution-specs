"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stSolidityTest/CallRecursiveMethodsFiller.json
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
        "tests/static/state_tests/stSolidityTest/CallRecursiveMethodsFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_call_recursive_methods(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0xeb201d2887816e041f6e807e804f64f3a7a226fe")
    sender = Address("0x73c241c3bc4fdf83b6ff3ae73735fddf7c9d711d")
    contract = Address("0xc7c7851c7f3291bed1039bb4ffa166c290a605a9")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000,
    )

    pre[sender] = Account(balance=0x12A05F200, nonce=0)
    pre[contract] = Account(
        balance=0x186A0,
        nonce=0,
        code=bytes.fromhex(
            "7c0100000000000000000000000000000000000000000000000000000000600035046329"  # noqa: E501
            "6df0df811460415780634893d88a14604d578063981a316514605957005b60476065565b"  # noqa: E501
            "60006000f35b6053607a565b60006000f35b605f6072565b60006000f35b5b6001156070"  # noqa: E501
            "576066565b565b6078607a565b565b60806072565b56"
        ),
    )
    pre[coinbase] = Account(balance=0, nonce=1)

    tx = Transaction(
        secret_key=Hash(
            "0xa9ae12cb2700c0214f86b9796881bc03a1fd5605d0e76d2da2ca592e62d53e52"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex("981a3165"),
        gas_limit=60000,
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = {
        contract: Account(
            code=bytes.fromhex(
                "7c01000000000000000000000000000000000000000000000000000000006000350463296df0df811460415780634893d88a14604d578063981a316514605957005b60476065565b60006000f35b6053607a565b60006000f35b605f6072565b60006000f35b5b6001156070576066565b565b6078607a565b565b60806072565b56"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
