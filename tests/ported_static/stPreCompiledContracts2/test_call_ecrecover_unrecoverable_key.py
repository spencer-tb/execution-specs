"""
CALL to ECREC precompile with input that has a valid signature structure but that does not recover a valid key. Specifies a 32 byte output range in memory. ECREC should return an empty response and the 32 byte output range should be left unchanged.

Ported from:
tests/static/state_tests/stPreCompiledContracts2/CallEcrecoverUnrecoverableKeyFiller.json
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
    ["tests/static/state_tests/stPreCompiledContracts2/CallEcrecoverUnrecoverableKeyFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_call_ecrecover_unrecoverable_key(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """CALL to ECREC precompile with input that has a valid signature structure but that does not recover a valid key. Specifies a 32 byte output range in memory. ECREC should return an empty response and the 32 byte output range should be left unchanged.."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0x85c44d846ed50ac9e384c1b575fd96f3edf5751f")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[contract] = Account(
        balance=0x1312d00,
        nonce=0,
        code=(
        Op.MSTORE(offset=0x0, value=0xa8b53bdf3306a35a7103ab5504a0c9b492295564b6202b1942a84ef300107281)
        + Op.MSTORE(offset=0x20, value=0x1b)
        + Op.MSTORE(offset=0x40, value=0x3078356531653033663533636531386237373263636230303933666637316633)
        + Op.MSTORE(offset=0x60, value=0x6635336635633735623734646362333161383561613862383839326234653862)
        + Op.MSTORE(offset=0x80, value=0x1122334455667788991011121314151617181920212223242526272829303132)
        + Op.POP(Op.CALL(gas=0x493e0, address=0x1, value=0x0, args_offset=0x0, args_size=0x80, ret_offset=0x80, ret_size=0x20))
        + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x80)) + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0xde0b6b3a7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xe04d1ac7ddda0c98397d56a0b501e960d4cd325a39286919ac23c1a07009a869"
        ),
        to=contract,
        data=b"",
        gas_limit=3652240,
        gas_price=10,
        nonce=0,
        value=100000,
    )

    post = {
        contract: Account(
            storage={0: 0x1122334455667788991011121314151617181920212223242526272829303132},
            code=Op.MSTORE(offset=0x0, value=0xa8b53bdf3306a35a7103ab5504a0c9b492295564b6202b1942a84ef300107281) + Op.MSTORE(offset=0x20, value=0x1b) + Op.MSTORE(offset=0x40, value=0x3078356531653033663533636531386237373263636230303933666637316633) + Op.MSTORE(offset=0x60, value=0x6635336635633735623734646362333161383561613862383839326234653862) + Op.MSTORE(offset=0x80, value=0x1122334455667788991011121314151617181920212223242526272829303132) + Op.POP(Op.CALL(gas=0x493e0, address=0x1, value=0x0, args_offset=0x0, args_size=0x80, ret_offset=0x80, ret_size=0x20)) + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x80)) + Op.STOP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
