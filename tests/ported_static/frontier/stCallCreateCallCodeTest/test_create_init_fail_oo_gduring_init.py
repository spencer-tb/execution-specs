"""
Create fails because init code has OOG.

Ported from:
state_tests/stCallCreateCallCodeTest/createInitFail_OOGduringInitFiller.json

@manually-enhanced: Do not overwrite. Per-era post: the CREATE leaves
zero gas, so its one-byte init code OOGs on every fork. Pre-EIP-150
SELFDESTRUCT is free and the frame still affords it, paying the whole
balance to the zero-address beneficiary; from EIP-150 on its 5000-gas
price OOGs the frame and the transaction reverts.
"""

import pytest
from execution_testing import (
    EOA,
    Account,
    Address,
    Alloc,
    Bytes,
    Environment,
    Fork,
    StateTestFiller,
    Transaction,
)
from execution_testing.forks import TangerineWhistle
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"

CONTRACT_BALANCE = 0xDE0B6B3A7640000
TX_VALUE = 0x186A0


@pytest.mark.ported_from(
    [
        "state_tests/stCallCreateCallCodeTest/createInitFail_OOGduringInitFiller.json"  # noqa: E501
    ],
)
@pytest.mark.valid_from("Frontier")
@pytest.mark.pre_alloc_mutable
def test_create_init_fail_oo_gduring_init(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """Create fails because init code has OOG."""
    coinbase = Address(0x2ADC25665018AA1FE0E6BC666DAC8FC2697FF9BA)
    contract_0 = Address(0x095E7BAEA6A6C7C4C2DFEB977EFAC326AF552D87)
    sender = EOA(
        key=0x45A915E4D060149EB4365960E6A7A45F334393093061116B197E3240065FF2D8
    )

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000,
    )

    pre[sender] = Account(balance=0xDE0B6B3A7640000)
    # Source: lll
    # {(MSTORE8 0 0x5a ) (SELFDESTRUCT (CREATE 1 0 1)) }
    contract_0 = pre.deploy_contract(  # noqa: F841
        code=Op.MSTORE8(offset=0x0, value=0x5A)
        + Op.SELFDESTRUCT(address=Op.CREATE(value=0x1, offset=0x0, size=0x1))
        + Op.STOP,
        balance=CONTRACT_BALANCE,
        nonce=0,
        address=Address(0x095E7BAEA6A6C7C4C2DFEB977EFAC326AF552D87),  # noqa: E501
    )

    tx = Transaction(
        protected=fork.supports_protected_txs(),
        sender=sender,
        to=contract_0,
        data=Bytes(""),
        gas_limit=53021,
        value=TX_VALUE,
    )

    zero_address = Address(0x0000000000000000000000000000000000000000)
    beneficiary: Account | None
    contract_0_account: Account | None
    if fork >= TangerineWhistle:
        # EIP-150's 5000-gas SELFDESTRUCT price OOGs the frame: the
        # transaction reverts and the beneficiary is never paid.
        beneficiary = Account.NONEXISTENT
        contract_0_account = Account(balance=CONTRACT_BALANCE)
    else:
        # SELFDESTRUCT is free: the contract self-destructs, paying
        # its balance plus the transaction value to the zero address.
        beneficiary = Account(balance=CONTRACT_BALANCE + TX_VALUE)
        contract_0_account = Account.NONEXISTENT
    post = {
        zero_address: beneficiary,
        contract_0: contract_0_account,
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
