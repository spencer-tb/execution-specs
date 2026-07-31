"""
Test_delegatecode_dynamic_code.

Ported from:
state_tests/stDelegatecallTestHomestead/delegatecodeDynamicCodeFiller.json

@manually-enhanced: Do not overwrite. Per-era post: EIP-161 starts
created contracts at nonce 1, steering the init code's inner CREATE.
Pre-SpuriousDragon it lands exactly on the DELEGATECALL target, whose
freshly deposited code then runs in the creating frame's context; from
SpuriousDragon on the target stays code-less and the call is a no-op.
The mirror address is pinned nonexistent and the dynamically created
contract's code/balance are asserted on every era.
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
from execution_testing.forks import SpuriousDragon
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


@pytest.mark.ported_from(
    [
        "state_tests/stDelegatecallTestHomestead/delegatecodeDynamicCodeFiller.json"  # noqa: E501
    ],
)
@pytest.mark.valid_from("Homestead")
@pytest.mark.pre_alloc_mutable
def test_delegatecode_dynamic_code(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """Test_delegatecode_dynamic_code."""
    coinbase = Address(0x2ADC25665018AA1FE0E6BC666DAC8FC2697FF9BA)
    contract_0 = Address(0x1000000000000000000000000000000000000000)
    sender = EOA(
        key=0x45A915E4D060149EB4365960E6A7A45F334393093061116B197E3240065FF2D8
    )

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    pre[sender] = Account(balance=0x2386F26FC10000)
    # Source: lll
    # { (MSTORE 0 0x716860016000553360145560005260096017f36000526012600e6001f0600a55) (MSTORE 32 0x604060006040600073ffe4ebd2a68c02d9dcb0a17283d13346beb2d8b6620186) (MSTORE 64 0xa0f4600b55000000000000000000000000000000000000000000000000000000) (CREATE 1 0 96) }  # noqa: E501
    contract_0 = pre.deploy_contract(  # noqa: F841
        code=Op.MSTORE(
            offset=0x0,
            value=0x716860016000553360145560005260096017F36000526012600E6001F0600A55,  # noqa: E501
        )
        + Op.MSTORE(
            offset=0x20,
            value=0x604060006040600073FFE4EBD2A68C02D9DCB0A17283D13346BEB2D8B6620186,  # noqa: E501
        )
        + Op.MSTORE(
            offset=0x40,
            value=0xA0F4600B55000000000000000000000000000000000000000000000000000000,  # noqa: E501
        )
        + Op.CREATE(value=0x1, offset=0x0, size=0x60)
        + Op.STOP,
        balance=10000,
        nonce=0,
        address=Address(0x1000000000000000000000000000000000000000),  # noqa: E501
    )

    tx = Transaction(
        protected=fork.supports_protected_txs(),
        sender=sender,
        to=contract_0,
        data=Bytes(""),
    )

    child = compute_create_address(address=contract_0, nonce=0)
    # EIP-161 starts created contracts at nonce 1, steering the inner
    # CREATE's address: pre-SpuriousDragon it lands exactly on the
    # init code's hardcoded DELEGATECALL target.
    grandchild_nonce = 1 if fork >= SpuriousDragon else 0
    grandchild = compute_create_address(address=child, nonce=grandchild_nonce)
    mirror = compute_create_address(address=child, nonce=1 - grandchild_nonce)

    if fork >= SpuriousDragon:
        # The delegate target holds no code: the call succeeds as a
        # no-op and the delegate-written slots stay zero.
        child_storage = {0: 0, 10: grandchild, 11: 1, 20: 0}
    else:
        # The freshly deposited code at the delegate target runs in
        # the child's context with the child's caller preserved.
        child_storage = {0: 1, 10: grandchild, 11: 1, 20: contract_0}

    post = {
        mirror: Account.NONEXISTENT,
        child: Account(storage=child_storage, balance=0),
        grandchild: Account(
            balance=1,
            nonce=grandchild_nonce,
            code=bytes.fromhex("600160005533601455"),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
