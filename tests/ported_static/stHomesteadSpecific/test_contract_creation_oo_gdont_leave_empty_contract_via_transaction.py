"""
Ported from:
tests/static/state_tests/stHomesteadSpecific/contractCreationOOGdontLeaveEmptyContractViaTransactionFiller.json
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
    ["tests/static/state_tests/stHomesteadSpecific/contractCreationOOGdontLeaveEmptyContractViaTransactionFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_contract_creation_oo_gdont_leave_empty_contract_via_transaction(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x1000000000000000000000000000000000000001")
    callee_1 = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    pre[contract] = Account(balance=0, nonce=0, code=Op.SSTORE(key=0x1, value=0x1) + Op.STOP)
    pre[sender] = Account(balance=0x10c8e0, nonce=0)
    pre[callee_1] = Account(
        balance=0x186a0,
        nonce=0,
        code=(
        Op.CALL(gas=0xc350, address=0x1000000000000000000000000000000000000001, value=0x0, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40)
        + Op.STOP
    ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=None,
        data=bytes.fromhex("6040600060406000600073100000000000000000000000000000000000000161c350f1"),
        gas_limit=96000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(storage={1: 1}, code=Op.SSTORE(key=0x1, value=0x1) + Op.STOP),
        callee_1: Account(
            code=Op.CALL(gas=0xc350, address=0x1000000000000000000000000000000000000001, value=0x0, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40) + Op.STOP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
