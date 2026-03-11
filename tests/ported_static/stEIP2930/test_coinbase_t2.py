"""
Ori Pomerantz qbzzt1@gmail.com.

Ported from:
tests/static/state_tests/stEIP2930/coinbaseT2Filler.yml
"""

import pytest
from execution_testing import (
    AccessList,
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
    ["tests/static/state_tests/stEIP2930/coinbaseT2Filler.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_access_list",
    [
        [
            AccessList(
                address=Address("0x7704d8a022a1ba8f3539fc82c7d7fb065abc0df3"),
                storage_keys=[],
            )
        ],
        [
            AccessList(
                address=Address("0x000000000000000000000000000000000000ba5a"),
                storage_keys=[],
            )
        ],
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_coinbase_t2(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_access_list: list | None,
) -> None:
    """Ori Pomerantz qbzzt1@gmail.com."""
    coinbase = Address("0x7704d8a022a1ba8f3539fc82c7d7fb065abc0df3")
    sender = Address("0x8dab845a8398167a1c204f0e79540d619be8b473")
    contract = Address("0x30873f83c35401e315e6e5994c012f1ee8119585")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=100,
        gas_limit=71794957647893862,
    )

    # Source: Yul
    # {
    #   mstore(0, gas())
    #   pop(call(gas(), <eoa:0x000000000000000000000000000000000000ba5e>, 1000000, 0, 0, 0, 0))  # noqa: E501
    #   mstore(0x20, gas())
    #
    #   // The 24 is the cost of twi gas(), seven pushes(), a pop(), and an mstore()  # noqa: E501
    #   sstore(0, sub(sub(mload(0), mload(0x20)),33))
    # }
    pre[contract] = Account(
        balance=0xDE0B6B3A7640000,
        nonce=1,
        code=(
            Op.MSTORE(offset=0x0, value=Op.GAS)
            + Op.POP(
                Op.CALL(
                    gas=Op.GAS,
                    address=0x7704D8A022A1BA8F3539FC82C7D7FB065ABC0DF3,
                    value=0xF4240,
                    args_offset=Op.DUP1,
                    args_size=Op.DUP1,
                    ret_offset=Op.DUP1,
                    ret_size=0x0,
                ),
            )
            + Op.MSTORE(offset=0x20, value=Op.GAS)
            + Op.SSTORE(
                key=0x0,
                value=Op.SUB(
                    Op.SUB(Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)),
                    0x21,
                ),
            )
            + Op.STOP
        ),
    )
    pre[coinbase] = Account(balance=0, nonce=1)
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=1)

    tx = Transaction(
        secret_key=Hash(
            "0xde0c95357363da5c1c5a73bd7c2781ca5c9fecc1014103b5e1d1e990ae8208ec"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex(
            "693c61390000000000000000000000000000000000000000000000000000000000000000"  # noqa: E501
        ),
        gas_limit=16777216,
        max_fee_per_gas=10000,
        max_priority_fee_per_gas=100,
        nonce=1,
        value=0,
        access_list=tx_access_list,
    )

    post = {
        contract: Account(
            storage={0: 6800},
            code=(
                Op.MSTORE(offset=0x0, value=Op.GAS)
                + Op.POP(
                    Op.CALL(
                        gas=Op.GAS,
                        address=0x7704D8A022A1BA8F3539FC82C7D7FB065ABC0DF3,
                        value=0xF4240,
                        args_offset=Op.DUP1,
                        args_size=Op.DUP1,
                        ret_offset=Op.DUP1,
                        ret_size=0x0,
                    ),
                )
                + Op.MSTORE(offset=0x20, value=Op.GAS)
                + Op.SSTORE(
                    key=0x0,
                    value=Op.SUB(
                        Op.SUB(Op.MLOAD(offset=0x0), Op.MLOAD(offset=0x20)),
                        0x21,
                    ),
                )
                + Op.STOP
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
