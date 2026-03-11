"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stEIP150Specific/SuicideToExistingContractFiller.json
"""

import pytest
from execution_testing import (
    Account,
    Address,
    Alloc,
    EOA,
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
        "tests/static/state_tests/stEIP150Specific/SuicideToExistingContractFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_suicide_to_existing_contract(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = EOA(
        key=0x4F31B3206FBF0E0E598B9B1A7D8AC86302A0FF1D8930738F1BEBAE9B67173E52
    )
    contract = Address("0xe110d543aadc3060d6b9e80d3e16be7a828128ec")
    callee = Address("0x79968a94dbedb20475585e9dd4dae6333add4c01")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SELFDESTRUCT(address=0xE110D543AADC3060D6B9E80D3E16BE7A828128EC)
            + Op.STOP
        ),
    )
    # Source: LLL
    # { [0] (GAS) (CALL 60000 <contract:0x1000000000000000000000000000000000000118> 0 0 0 0 0) [[1]] (SUB @0 (GAS)) }  # noqa: E501
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.MSTORE(offset=0x0, value=Op.GAS)
            + Op.POP(
                Op.CALL(
                    gas=0xEA60,
                    address=0x79968A94DBEDB20475585E9DD4DAE6333ADD4C01,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.SSTORE(key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS))
            + Op.STOP
        ),
    )
    pre[sender] = Account(balance=0xE8D4A51000, nonce=0)

    tx = Transaction(
        sender=sender,
        to=contract,
        data=b"",
        gas_limit=600000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        callee: Account(
            code=(
                Op.SELFDESTRUCT(
                    address=0xE110D543AADC3060D6B9E80D3E16BE7A828128EC,
                )
                + Op.STOP
            ),
        ),
        contract: Account(
            storage={1: 7637},
            code=(
                Op.MSTORE(offset=0x0, value=Op.GAS)
                + Op.POP(
                    Op.CALL(
                        gas=0xEA60,
                        address=0x79968A94DBEDB20475585E9DD4DAE6333ADD4C01,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    ),
                )
                + Op.SSTORE(
                    key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                )
                + Op.STOP
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
