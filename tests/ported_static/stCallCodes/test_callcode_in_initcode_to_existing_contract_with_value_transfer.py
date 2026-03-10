"""
callcode inside create/create2 contract init to existing contract.

Ported from:
tests/static/state_tests/stCallCodes
callcodeInInitcodeToExistingContractWithValueTransferFiller.json
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
        "tests/static/state_tests/stCallCodes/callcodeInInitcodeToExistingContractWithValueTransferFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_callcode_in_initcode_to_existing_contract_with_value_transfer(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Callcode inside create/create2 contract init to existing contract."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x1000000000000000000000000000000000000000")
    callee = Address("0x945304eb96065b2a98b57a48a06ae28d285a71b5")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    pre[contract] = Account(
        balance=0x2710,
        nonce=0,
        code=(
            Op.MSTORE(
                offset=0x0,
                value=0x6040600060406000600573945304EB96065B2A98B57A48A06AE28D285A71B562,  # noqa: E501
            )
            + Op.MSTORE(
                offset=0x20,
                value=0x186A0F260005500000000000000000000000000000000000000000000000000,  # noqa: E501
            )
            + Op.CREATE(value=0x5, offset=0x0, size=0x40)
            + Op.STOP
        ),
    )
    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=Op.SSTORE(key=0x2, value=0x1) + Op.STOP,
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
                    value=0x6040600060406000600573945304EB96065B2A98B57A48A06AE28D285A71B562,  # noqa: E501
                )
                + Op.MSTORE(
                    offset=0x20,
                    value=0x186A0F260005500000000000000000000000000000000000000000000000000,  # noqa: E501
                )
                + Op.CREATE(value=0x5, offset=0x0, size=0x40)
                + Op.STOP
            ),
        ),
        Address("0x13136008b64ff592819b2fa6d43f2835c452020e"): Account(
            storage={0: 1, 2: 1},
        ),
        callee: Account(code=Op.SSTORE(key=0x2, value=0x1) + Op.STOP),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
