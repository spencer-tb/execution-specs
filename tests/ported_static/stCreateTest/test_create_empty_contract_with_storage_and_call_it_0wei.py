"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stCreateTest
CREATE_EmptyContractWithStorageAndCallIt_0weiFiller.json
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
        "tests/static/state_tests/stCreateTest/CREATE_EmptyContractWithStorageAndCallIt_0weiFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_create_empty_contract_with_storage_and_call_it_0wei(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    callee = Address("0xc94f5374fce5edbc8e2a8697c15331677e6ebf0b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[sender] = Account(balance=0xE8D4A51000, nonce=0)
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "5a6000557f600c6000556000600060006000600073c94f5374fce5edbc8e2a8697c15331"  # noqa: E501
            "676000527f7e6ebf0b61ea60f10000000000000000000000000000000000000000000000"  # noqa: E501
            "00602052604060006000f06001555a6002556000600060006000600060015461ea60f160"  # noqa: E501
            "03555a60645500"
        ),
    )
    pre[callee] = Account(
        balance=0xE8D4A51000,
        nonce=0,
        code=bytes.fromhex("600c60015500"),
    )

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=600000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            storage={
                0: 0x8D5B6,
                1: 0xF1ECF98489FA9ED60A664FC4998DB699CFA39D40,
                2: 0x6F4F0,
                3: 1,
                100: 0x64763,
            },
            code=bytes.fromhex(
                "5a6000557f600c6000556000600060006000600073c94f5374fce5edbc8e2a8697c15331676000527f7e6ebf0b61ea60f1000000000000000000000000000000000000000000000000602052604060006000f06001555a6002556000600060006000600060015461ea60f16003555a60645500"  # noqa: E501
            ),
        ),
        callee: Account(storage={1: 12}, code=bytes.fromhex("600c60015500")),
        Address("0xf1ecf98489fa9ed60a664fc4998db699cfa39d40"): Account(
            storage={0: 12},
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
