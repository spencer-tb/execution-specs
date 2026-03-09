"""
EXTCODEHASH/EXTCODESIZE of an account created then deleted in a CALL,...

Ported from:
tests/static/state_tests/stExtCodeHash
extCodeHashCreatedAndDeletedAccountRecheckInOuterCallFiller.json
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
        "tests/static/state_tests/stExtCodeHash/extCodeHashCreatedAndDeletedAccountRecheckInOuterCallFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_ext_code_hash_created_and_deleted_account_recheck_in_outer_call(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """EXTCODEHASH/EXTCODESIZE of an account created then deleted in a..."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xdeadbeef00000000000000000000000000000001")
    callee = Address("0xdeadbeef00000000000000000000000000000000")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)
    pre[callee] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "6010601180604460803960806000f56000526000513f6000556000513b60015560006000"  # noqa: E501
            "60006000600060005162010000f1506000513f6002556000513b6003550000fe60048060"  # noqa: E501
            "0d6000396000f300fe6000ff00"
        ),
    )
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=0,
        code=bytes.fromhex(
            "6000600060006000600073deadbeef0000000000000000000000000000000062020000f1"  # noqa: E501
            "5073123f4c415171383dcf6f3ac6c3b70fe321e11b5e3f60005573123f4c415171383dcf"  # noqa: E501
            "6f3ac6c3b70fe321e11b5e3b6001550000"
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=400000,
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = {
        callee: Account(
            storage={
                0: 0x73C5F15B1290FD9E66722596C2FA1E1C9341F7ACB185530DCE0BF0E0FEC7DFC6,  # noqa: E501
                1: 4,
                2: 0x73C5F15B1290FD9E66722596C2FA1E1C9341F7ACB185530DCE0BF0E0FEC7DFC6,  # noqa: E501
                3: 4,
            },
            code=bytes.fromhex(
                "6010601180604460803960806000f56000526000513f6000556000513b6001556000600060006000600060005162010000f1506000513f6002556000513b6003550000fe600480600d6000396000f300fe6000ff00"  # noqa: E501
            ),
        ),
        contract: Account(
            storage={
                0: 0x73C5F15B1290FD9E66722596C2FA1E1C9341F7ACB185530DCE0BF0E0FEC7DFC6,  # noqa: E501
                1: 4,
            },
            code=bytes.fromhex(
                "6000600060006000600073deadbeef0000000000000000000000000000000062020000f15073123f4c415171383dcf6f3ac6c3b70fe321e11b5e3f60005573123f4c415171383dcf6f3ac6c3b70fe321e11b5e3b6001550000"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
