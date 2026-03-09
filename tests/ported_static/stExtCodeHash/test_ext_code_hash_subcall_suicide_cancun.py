"""
transaction to B | B call to A | A delegatecall/callcode to C (C has...

Ported from:
tests/static/state_tests/stExtCodeHash
extCodeHashSubcallSuicideCancunFiller.yml
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
        "tests/static/state_tests/stExtCodeHash/extCodeHashSubcallSuicideCancunFiller.yml",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_ext_code_hash_subcall_suicide_cancun(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Transaction to B | B call to A | A delegatecall/callcode to C (C..."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xb000000000000000000000000000000000000000")
    callee = Address("0xa000000000000000000000000000000000000000")
    callee_1 = Address("0xd000000000000000000000000000000000000000")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[callee] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "60206000600060006000733e180b1862f9d158abb5e519a6d8605540c2368262055730f2"  # noqa: E501
            "00"
        ),
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "60498061010c6000396000670de0b6b3a7640000f05073a0000000000000000000000000"  # noqa: E501
            "000000000000003f60015573a0000000000000000000000000000000000000003b600255"  # noqa: E501
            "60206000600073a0000000000000000000000000000000000000003c6000516003556020"  # noqa: E501
            "600060006000600073a00000000000000000000000000000000000000062055730f15073"  # noqa: E501
            "a0000000000000000000000000000000000000003f60045573a000000000000000000000"  # noqa: E501
            "0000000000000000003b60055560206000600073a0000000000000000000000000000000"  # noqa: E501
            "000000003c6000516006556020600060006000600073a000000000000000000000000000"  # noqa: E501
            "00000000000062055730f160075500fe6000600060006000600073d00000000000000000"  # noqa: E501
            "0000000000000000000000620186a0f15060178060326000396000f300fe73a94f5374fc"  # noqa: E501
            "e5edbc8e2a8697c15331677e6ebf0bff00"
        ),
    )
    pre[callee_1] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex("600160015500"),
    )

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=500000,
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = {
        Address("0x3e180b1862f9d158abb5e519a6d8605540c23682"): Account(
            code=bytes.fromhex(
                "73a94f5374fce5edbc8e2a8697c15331677e6ebf0bff00"
            ),
        ),
        callee: Account(
            code=bytes.fromhex(
                "60206000600060006000733e180b1862f9d158abb5e519a6d8605540c2368262055730f200"  # noqa: E501
            ),
        ),
        contract: Account(
            storage={
                1: 0x807D478BD0D0173122F5531D4C43781631444232A0816DD35578747C7D67AF0D,  # noqa: E501
                2: 37,
                3: 0x60206000600060006000733E180B1862F9D158ABB5E519A6D8605540C2368262,  # noqa: E501
                4: 0x807D478BD0D0173122F5531D4C43781631444232A0816DD35578747C7D67AF0D,  # noqa: E501
                5: 37,
                6: 0x60206000600060006000733E180B1862F9D158ABB5E519A6D8605540C2368262,  # noqa: E501
                7: 1,
            },
            code=bytes.fromhex(
                "60498061010c6000396000670de0b6b3a7640000f05073a0000000000000000000000000000000000000003f60015573a0000000000000000000000000000000000000003b60025560206000600073a0000000000000000000000000000000000000003c6000516003556020600060006000600073a00000000000000000000000000000000000000062055730f15073a0000000000000000000000000000000000000003f60045573a0000000000000000000000000000000000000003b60055560206000600073a0000000000000000000000000000000000000003c6000516006556020600060006000600073a00000000000000000000000000000000000000062055730f160075500fe6000600060006000600073d000000000000000000000000000000000000000620186a0f15060178060326000396000f300fe73a94f5374fce5edbc8e2a8697c15331677e6ebf0bff00"  # noqa: E501
            ),
        ),
        callee_1: Account(storage={1: 1}, code=bytes.fromhex("600160015500")),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
