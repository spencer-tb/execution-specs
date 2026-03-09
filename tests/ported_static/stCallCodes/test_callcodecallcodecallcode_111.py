"""
CALLCODE -> CALLCODE -> CALLCODE -> code check parameter opcodes

Ported from:
tests/static/state_tests/stCallCodes/callcodecallcodecallcode_111Filler.json
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
    ["tests/static/state_tests/stCallCodes/callcodecallcodecallcode_111Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_callcodecallcodecallcode_111(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """CALLCODE -> CALLCODE -> CALLCODE -> code check parameter opcodes."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0xdb43306b16c521b9cc3667fbe7d1b697bb1f9605")
    callee = Address("0x0ffffaeb931552e5f094ca96a70be612da56b887")
    callee_1 = Address("0x4c0de71b93de6b7055a3686e4bf93add02b39ed8")
    callee_2 = Address("0x7e63847aad8ca50fb7c04777dce6871a6bf8de0c")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=30000000,
    )

    pre[callee] = Account(
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=(
        Op.SSTORE(key=0x2, value=Op.CALLCODE(gas=0x3d090, address=0x7e63847aad8ca50fb7c04777dce6871a6bf8de0c, value=0x3, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40))
        + Op.STOP
    ),
    )
    pre[callee_1] = Account(
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=(
        Op.SSTORE(key=0x1, value=Op.CALLCODE(gas=0x493e0, address=0xffffaeb931552e5f094ca96a70be612da56b887, value=0x2, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40))
        + Op.STOP
    ),
    )
    pre[callee_2] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.SSTORE(key=0x3, value=0x1) + Op.SSTORE(key=0x4, value=Op.CALLER)
        + Op.SSTORE(key=0x7, value=Op.CALLVALUE)
        + Op.SSTORE(key=0x14a, value=Op.ADDRESS)
        + Op.SSTORE(key=0x14c, value=Op.ORIGIN)
        + Op.SSTORE(key=0x150, value=Op.CALLDATASIZE)
        + Op.SSTORE(key=0x152, value=Op.CODESIZE)
        + Op.SSTORE(key=0x154, value=Op.GASPRICE) + Op.STOP
    ),
    )
    pre[contract] = Account(
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=(
        Op.SSTORE(key=0x0, value=Op.CALLCODE(gas=0x55730, address=0x4c0de71b93de6b7055a3686e4bf93add02b39ed8, value=0x1, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40))
        + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0xde0b6b3a7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xe04d1ac7ddda0c98397d56a0b501e960d4cd325a39286919ac23c1a07009a869"
        ),
        to=contract,
        data=b"",
        gas_limit=3000000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        callee: Account(
            code=Op.SSTORE(key=0x2, value=Op.CALLCODE(gas=0x3d090, address=0x7e63847aad8ca50fb7c04777dce6871a6bf8de0c, value=0x3, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40)) + Op.STOP,
        ),
        callee_1: Account(
            code=Op.SSTORE(key=0x1, value=Op.CALLCODE(gas=0x493e0, address=0xffffaeb931552e5f094ca96a70be612da56b887, value=0x2, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40)) + Op.STOP,
        ),
        callee_2: Account(
            code=Op.SSTORE(key=0x3, value=0x1) + Op.SSTORE(key=0x4, value=Op.CALLER) + Op.SSTORE(key=0x7, value=Op.CALLVALUE) + Op.SSTORE(key=0x14a, value=Op.ADDRESS) + Op.SSTORE(key=0x14c, value=Op.ORIGIN) + Op.SSTORE(key=0x150, value=Op.CALLDATASIZE) + Op.SSTORE(key=0x152, value=Op.CODESIZE) + Op.SSTORE(key=0x154, value=Op.GASPRICE) + Op.STOP,
        ),
        contract: Account(
            storage={0: 1, 1: 1, 2: 1, 3: 1, 4: 0xdb43306b16c521b9cc3667fbe7d1b697bb1f9605, 7: 3, 330: 0xdb43306b16c521b9cc3667fbe7d1b697bb1f9605, 332: 0xebaf50debf10e08302fe4280c32df010463ca297, 336: 64, 338: 39, 340: 10},
            code=Op.SSTORE(key=0x0, value=Op.CALLCODE(gas=0x55730, address=0x4c0de71b93de6b7055a3686e4bf93add02b39ed8, value=0x1, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40)) + Op.STOP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
