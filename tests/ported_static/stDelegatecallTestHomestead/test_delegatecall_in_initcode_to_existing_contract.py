"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stDelegatecallTestHomestead
delegatecallInInitcodeToExistingContractFiller.json
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
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


@pytest.mark.ported_from(
    [
        "tests/static/state_tests/stDelegatecallTestHomestead/delegatecallInInitcodeToExistingContractFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_delegatecall_in_initcode_to_existing_contract(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x1000000000000000000000000000000000000000")
    callee = Address("0x1000000000000000000000000000000000000001")
    callee_1 = Address("0x945304eb96065b2a98b57a48a06ae28d285a71b5")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    # Source: LLL
    # { (MSTORE 0 0x604060006040600073945304eb96065b2a98b57a48a06ae28d285a71b5620186) (MSTORE 32 0xa0f4600055336001550000000000000000000000000000000000000000000000) (CREATE 1 0 64) }  # noqa: E501
    pre[contract] = Account(
        balance=0x2710,
        nonce=0,
        code=(
            Op.MSTORE(
                offset=0x0,
                value=0x604060006040600073945304EB96065B2A98B57A48A06AE28D285A71B5620186,  # noqa: E501
            )
            + Op.MSTORE(
                offset=0x20,
                value=0xA0F4600055336001550000000000000000000000000000000000000000000000,  # noqa: E501
            )
            + Op.CREATE(value=0x1, offset=0x0, size=0x40)
            + Op.STOP
        ),
    )
    # Source: LLL
    # { (MSTORE 0 0x6001600055) (CREATE 1 27 5) }
    pre[callee] = Account(
        balance=1000,
        nonce=0,
        code=(
            Op.MSTORE(offset=0x0, value=0x6001600055)
            + Op.CREATE(value=0x1, offset=0x1B, size=0x5)
            + Op.STOP
        ),
    )
    # Source: LLL
    # { (SSTORE 2 1) [[ 11 ]] (CALLER) }
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(key=0x2, value=0x1)
            + Op.SSTORE(key=0xB, value=Op.CALLER)
            + Op.STOP
        ),
    )
    pre[sender] = Account(balance=0x2386F26FC10000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=453081,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            code=(
                Op.MSTORE(
                    offset=0x0,
                    value=0x604060006040600073945304EB96065B2A98B57A48A06AE28D285A71B5620186,  # noqa: E501
                )
                + Op.MSTORE(
                    offset=0x20,
                    value=0xA0F4600055336001550000000000000000000000000000000000000000000000,  # noqa: E501
                )
                + Op.CREATE(value=0x1, offset=0x0, size=0x40)
                + Op.STOP
            ),
        ),
        callee: Account(
            code=(
                Op.MSTORE(offset=0x0, value=0x6001600055)
                + Op.CREATE(value=0x1, offset=0x1B, size=0x5)
                + Op.STOP
            ),
        ),
        Address("0x13136008b64ff592819b2fa6d43f2835c452020e"): Account(
            storage={
                0: 1,
                1: 0x1000000000000000000000000000000000000000,
                2: 1,
                11: 0x1000000000000000000000000000000000000000,
            },
        ),
        callee_1: Account(
            code=(
                Op.SSTORE(key=0x2, value=0x1)
                + Op.SSTORE(key=0xB, value=Op.CALLER)
                + Op.STOP
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
