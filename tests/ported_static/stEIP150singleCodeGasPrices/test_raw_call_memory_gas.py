"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stEIP150singleCodeGasPrices
RawCallMemoryGasFiller.json
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
        "tests/static/state_tests/stEIP150singleCodeGasPrices/RawCallMemoryGasFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_raw_call_memory_gas(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xfaa10b404ab607779993c016cd5da73ae1f29d7e")
    contract = Address("0x590b5b415a9a5f546bdb1a7781b31b91c53902ed")
    callee = Address("0xe497cd0909c3691e0b6d2a42e26f36696fc27ba5")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.MSTORE(offset=0x0, value=Op.GAS)
            + Op.POP(
                Op.CALL(
                    gas=0x7530,
                    address=0xE497CD0909C3691E0B6D2A42E26F36696FC27BA5,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x1F40,
                    ret_offset=0x0,
                    ret_size=0x1F40,
                ),
            )
            + Op.SSTORE(key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS))
            + Op.STOP
        ),
    )
    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=Op.SSTORE(key=0x2, value=Op.GAS) + Op.STOP,
    )
    pre[sender] = Account(balance=0xE8D4A51000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x4f31b3206fbf0e0e598b9b1a7d8ac86302a0ff1d8930738f1bebae9b67173e52"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=500000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            storage={1: 25608},
            code=(
                Op.MSTORE(offset=0x0, value=Op.GAS)
                + Op.POP(
                    Op.CALL(
                        gas=0x7530,
                        address=0xE497CD0909C3691E0B6D2A42E26F36696FC27BA5,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x1F40,
                        ret_offset=0x0,
                        ret_size=0x1F40,
                    ),
                )
                + Op.SSTORE(
                    key=0x1, value=Op.SUB(Op.MLOAD(offset=0x0), Op.GAS)
                )
                + Op.STOP
            ),
        ),
        callee: Account(
            storage={2: 29998},
            code=Op.SSTORE(key=0x2, value=Op.GAS) + Op.STOP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
