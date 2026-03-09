"""
Check that create2 does not fill returndata buffer with its return opcode.

Ported from:
tests/static/state_tests/stCreate2/returndatacopy_following_createFiller.json
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
        "tests/static/state_tests/stCreate2/returndatacopy_following_createFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex",
    [
        "0000000000000000000000000f572e5295c57f15886f9b263e2f6d2d6c7b5ec6",
        "0000000000000000000000001f572e5295c57f15886f9b263e2f6d2d6c7b5ec6",
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_returndatacopy_following_create(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
) -> None:
    """Check that create2 does not fill returndata buffer with its..."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x1aabbccdd5c57f15886f9b263e2f6d2d6c7b5ec6")
    callee = Address("0x0f572e5295c57f15886f9b263e2f6d2d6c7b5ec6")
    callee_1 = Address("0x1f572e5295c57f15886f9b263e2f6d2d6c7b5ec6")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=47244640256,
    )

    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "6000602880601f60003960006000f5506020600060003e60005160005500fe7d11112222"  # noqa: E501
            "3333444455556666777788889999aaaabbbbccccddddeeeeffff60005260206000f300"  # noqa: E501
        ),
        storage={0x0: 0x1},
    )
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("600060006000600060006000355af100"),
    )
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "6000600280601f60003960006000f5506020600060003e60005160005500fe0000"  # noqa: E501
        ),
        storage={0x0: 0x1},
    )
    pre[sender] = Account(balance=0x6400000000, nonce=0)

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=tx_data,
        gas_limit=100000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        callee: Account(
            storage={0: 1},
            code=bytes.fromhex(
                "6000602880601f60003960006000f5506020600060003e60005160005500fe7d111122223333444455556666777788889999aaaabbbbccccddddeeeeffff60005260206000f300"  # noqa: E501
            ),
        ),
        contract: Account(
            code=bytes.fromhex("600060006000600060006000355af100"),
        ),
        callee_1: Account(
            storage={0: 1},
            code=bytes.fromhex(
                "6000600280601f60003960006000f5506020600060003e60005160005500fe0000"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
