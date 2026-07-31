"""
Test_delegatecall_in_initcode_to_existing_contract_oog.

Ported from:
state_tests/stDelegatecallTestHomestead/delegatecallInInitcodeToExistingContractOOGFiller.json

@manually-enhanced: Do not overwrite. Per-era post: the init code asks
for a fixed 100000 gas in its DELEGATECALL. From EIP-150 on the ask is
capped to the available gas and the creation completes; on Homestead
the over-ask is an exception, the init frame dies, and the creation
fails with the endowment staying at the creator.
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
    compute_create_address,
)
from execution_testing.forks import Amsterdam, TangerineWhistle
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


@pytest.mark.ported_from(
    [
        "state_tests/stDelegatecallTestHomestead/delegatecallInInitcodeToExistingContractOOGFiller.json"  # noqa: E501
    ],
)
@pytest.mark.valid_from("Homestead")
@pytest.mark.pre_alloc_mutable
def test_delegatecall_in_initcode_to_existing_contract_oog(
    state_test: StateTestFiller,
    fork: Fork,
    pre: Alloc,
) -> None:
    """Test_delegatecall_in_initcode_to_existing_contract_oog."""
    coinbase = Address(0x2ADC25665018AA1FE0E6BC666DAC8FC2697FF9BA)
    contract_0 = Address(0x1000000000000000000000000000000000000000)
    contract_1 = Address(0x945304EB96065B2A98B57A48A06AE28D285A71B5)
    sender = EOA(
        key=0x45A915E4D060149EB4365960E6A7A45F334393093061116B197E3240065FF2D8
    )

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=3000000 if fork >= Amsterdam else 1000000,
    )

    pre[sender] = Account(balance=0x2386F26FC10000)
    # Source: lll
    # { (MSTORE 0 0x604060006040600073945304eb96065b2a98b57a48a06ae28d285a71b5620186) (MSTORE 32 0xa0f4600a5533600b550000000000000000000000000000000000000000000000) (CREATE 5 0 64) }  # noqa: E501
    contract_0 = pre.deploy_contract(  # noqa: F841
        code=Op.MSTORE(
            offset=0x0,
            value=0x604060006040600073945304EB96065B2A98B57A48A06AE28D285A71B5620186,  # noqa: E501
        )
        + Op.MSTORE(
            offset=0x20,
            value=0xA0F4600A5533600B550000000000000000000000000000000000000000000000,  # noqa: E501
        )
        + Op.CREATE(value=0x5, offset=0x0, size=0x40)
        + Op.STOP,
        balance=10000,
        nonce=0,
        address=Address(0x1000000000000000000000000000000000000000),  # noqa: E501
    )
    # Source: lll
    # { (SSTORE 2 1) }
    contract_1 = pre.deploy_contract(  # noqa: F841
        code=Op.SSTORE(key=0x2, value=0x1) + Op.STOP,
        nonce=0,
        address=Address(0x945304EB96065B2A98B57A48A06AE28D285A71B5),  # noqa: E501
    )

    tx = Transaction(
        protected=fork.supports_protected_txs(),
        sender=sender,
        to=contract_0,
        data=Bytes(""),
        gas_limit=2153096 if fork >= Amsterdam else 153096,
    )

    created = compute_create_address(address=contract_0, nonce=0)
    if fork >= TangerineWhistle:
        # EIP-150 caps the 100000-gas ask to the available gas, so
        # the creation completes and keeps the 5-wei endowment.
        created_account: Account | None = Account(balance=5)
        creator_balance = 10000 - 5
    else:
        # Pre-EIP-150 asking for more gas than the frame holds is an
        # exception: the init frame dies, the creation fails, and the
        # endowment stays with the creator.
        created_account = Account.NONEXISTENT
        creator_balance = 10000
    post = {
        created: created_account,
        contract_0: Account(balance=creator_balance, nonce=1),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
