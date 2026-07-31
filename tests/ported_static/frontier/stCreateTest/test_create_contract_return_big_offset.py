"""
Test_create_contract_return_big_offset.

Ported from:
state_tests/stCreateTest/CREATE_ContractRETURNBigOffsetFiller.yml

@manually-enhanced: Do not overwrite. Per-era post: below EIP-170's
code-size cap the 64-KiB all-zero return (d0) is a legal, affordable
code deposit, so the creation succeeds and the contract exists with
nonce 0 (pre-EIP-161); the larger returns stay unaffordable to
deposit on every era.
"""

import pytest
from execution_testing import (
    Account,
    Address,
    Alloc,
    Environment,
    StateTestFiller,
    Transaction,
    compute_create_address,
)
from execution_testing.forks import Fork, SpuriousDragon
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


@pytest.mark.ported_from(
    ["state_tests/stCreateTest/CREATE_ContractRETURNBigOffsetFiller.yml"],
)
@pytest.mark.valid_from("Frontier")
@pytest.mark.parametrize(
    "d, g, v",
    [
        pytest.param(
            0,
            0,
            0,
            id="d0",
        ),
        pytest.param(
            1,
            0,
            0,
            id="d1",
        ),
        pytest.param(
            2,
            0,
            0,
            id="d2",
        ),
        pytest.param(
            3,
            0,
            0,
            id="d3",
        ),
    ],
)
def test_create_contract_return_big_offset(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    d: int,
    g: int,
    v: int,
) -> None:
    """Test_create_contract_return_big_offset."""
    coinbase = Address(0x2ADC25665018AA1FE0E6BC666DAC8FC2697FF9BA)
    sender = pre.fund_eoa(amount=0x9184E72A000)

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=89128960,
    )

    tx_data = [
        Op.RETURN(offset=0x74AC2, size=0x10000),
        Op.RETURN(offset=0x74AC2, size=0x51EB8),
        Op.RETURN(offset=0x74AC2, size=0x51EB9),
        Op.RETURN(offset=0x74AC2, size=0xD15BC),
    ]
    tx_gas = [16777216]

    tx = Transaction(
        protected=fork.supports_protected_txs(),
        sender=sender,
        to=None,
        data=tx_data[d],
        gas_limit=tx_gas[g],
    )

    created_account: Account | None = Account.NONEXISTENT
    if d == 0 and fork < SpuriousDragon:
        # Below EIP-170's 24576-byte cap the 64-KiB all-zero return
        # is a legal, affordable code deposit (200 gas per byte), so
        # the creation succeeds; created contracts start at nonce 0
        # before EIP-161.
        created_account = Account(code=b"\x00" * 0x10000, nonce=0)
    post = {
        sender: Account(nonce=1),
        compute_create_address(address=sender, nonce=0): created_account,
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
