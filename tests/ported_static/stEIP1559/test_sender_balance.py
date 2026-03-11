"""
The execution records the EIP-1559 transaction origin balance to make sure...

properly computed based on the effective gas price (not the maximum gas price
as in
the transaction validity check).

Ported from:
tests/static/state_tests/stEIP1559/senderBalanceFiller.yml
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
    ["tests/static/state_tests/stEIP1559/senderBalanceFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_sender_balance(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """The execution records the EIP-1559 transaction origin balance to..."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = EOA(
        key=0xE04D1AC7DDDA0C98397D56A0B501E960D4CD325A39286919AC23C1A07009A869
    )
    contract = Address("0x420132f96200ba8e5c98298a85633c35c4f052ef")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=11,
        gas_limit=30000000,
    )

    # Source: Yul
    # {
    #   sstore(0, balance(caller()))
    # }
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=Op.SSTORE(key=0x0, value=Op.BALANCE(address=Op.CALLER)) + Op.STOP,
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)

    tx = Transaction(
        sender=sender,
        to=contract,
        data=b"",
        gas_limit=60000,
        max_fee_per_gas=1000,
        max_priority_fee_per_gas=100,
        nonce=0,
        value=0,
        access_list=[],
    )

    post = {
        contract: Account(
            storage={0: 0xDE0B6B3A6FE6060},
            code=(
                Op.SSTORE(key=0x0, value=Op.BALANCE(address=Op.CALLER))
                + Op.STOP
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
