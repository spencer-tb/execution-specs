"""
callcode inside create/create2 contract init to existing contract. callcode...

Ported from:
tests/static/state_tests/stCallCodes
callcodeInInitcodeToExisContractWithVTransferNEMoneyFiller.json
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
        "tests/static/state_tests/stCallCodes/callcodeInInitcodeToExisContractWithVTransferNEMoneyFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        (
            "0000000000000000000000001000000000000000000000000000000000000000",
            {
                Address("0x1000000000000000000000000000000000000000"): Account(
                    code=bytes.fromhex(
                        "602880600f60003960006000f000fe600060006000600060017310000000000000000000000000000000000000016207a120f260015500"  # noqa: E501
                    )
                ),
                Address("0x1000000000000000000000000000000000000001"): Account(
                    code=bytes.fromhex("600160025500")
                ),
                Address("0x1100000000000000000000000000000000000000"): Account(
                    code=bytes.fromhex(
                        "60006000600060006000600035620493e0f100"
                    )
                ),
                Address("0x2000000000000000000000000000000000000000"): Account(
                    code=bytes.fromhex(
                        "6000602880601160003960006000f500fe600060006000600060017310000000000000000000000000000000000000016207a120f260015500"  # noqa: E501
                    )
                ),
            },
        ),
        (
            "0000000000000000000000002000000000000000000000000000000000000000",
            {
                Address("0x1000000000000000000000000000000000000000"): Account(
                    code=bytes.fromhex(
                        "602880600f60003960006000f000fe600060006000600060017310000000000000000000000000000000000000016207a120f260015500"  # noqa: E501
                    )
                ),
                Address("0x1000000000000000000000000000000000000001"): Account(
                    code=bytes.fromhex("600160025500")
                ),
                Address("0x1100000000000000000000000000000000000000"): Account(
                    code=bytes.fromhex(
                        "60006000600060006000600035620493e0f100"
                    )
                ),
                Address("0x2000000000000000000000000000000000000000"): Account(
                    code=bytes.fromhex(
                        "6000602880601160003960006000f500fe600060006000600060017310000000000000000000000000000000000000016207a120f260015500"  # noqa: E501
                    )
                ),
            },
        ),
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_callcode_in_initcode_to_exis_contract_with_v_transfer_ne_money(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Callcode inside create/create2 contract init to existing..."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x1100000000000000000000000000000000000000")
    callee = Address("0x1000000000000000000000000000000000000000")
    callee_1 = Address("0x1000000000000000000000000000000000000001")
    callee_2 = Address("0x2000000000000000000000000000000000000000")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    pre[callee] = Account(
        balance=0x2710,
        nonce=0,
        code=bytes.fromhex(
            "602880600f60003960006000f000fe600060006000600060017310000000000000000000"  # noqa: E501
            "000000000000000000016207a120f260015500"
        ),
    )
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("600160025500"),
    )
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("60006000600060006000600035620493e0f100"),
    )
    pre[callee_2] = Account(
        balance=0x2710,
        nonce=0,
        code=bytes.fromhex(
            "6000602880601160003960006000f500fe60006000600060006001731000000000000000"  # noqa: E501
            "0000000000000000000000016207a120f260015500"
        ),
    )
    pre[sender] = Account(balance=0x2386F26FC10000, nonce=0)

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=tx_data,
        gas_limit=1000000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
