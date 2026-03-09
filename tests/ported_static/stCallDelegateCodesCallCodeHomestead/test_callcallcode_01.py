"""
Ported from:
tests/static/state_tests/stCallDelegateCodesCallCodeHomestead/callcallcode_01Filler.json
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
    ["tests/static/state_tests/stCallDelegateCodesCallCodeHomestead/callcallcode_01Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_callcallcode_01(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0xdb43306b16c521b9cc3667fbe7d1b697bb1f9605")
    callee = Address("0x1ccccf19d84280c8a0e94209761296dabd87b3c9")
    callee_1 = Address("0xd42cd48f1d9a88f4b75bfb5e46e754c1128bd7fb")

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
        Op.SSTORE(key=0x1, value=Op.DELEGATECALL(gas=0x3d090, address=0xd42cd48f1d9a88f4b75bfb5e46e754c1128bd7fb, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40))
        + Op.STOP
    ),
    )
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.SSTORE(key=0x2, value=0x1) + Op.SSTORE(key=0x4, value=Op.CALLER)
        + Op.SSTORE(key=0x5, value=Op.CALLVALUE)
        + Op.SSTORE(key=0xe6, value=Op.ADDRESS) + Op.SSTORE(key=0xe8, value=Op.ORIGIN)
        + Op.SSTORE(key=0xec, value=Op.CALLDATASIZE)
        + Op.SSTORE(key=0xee, value=Op.CODESIZE)
        + Op.SSTORE(key=0xf0, value=Op.GASPRICE) + Op.STOP
    ),
    )
    pre[contract] = Account(
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=(
        Op.SSTORE(key=0x0, value=Op.CALLCODE(gas=0x55730, address=0x1ccccf19d84280c8a0e94209761296dabd87b3c9, value=0x1, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40))
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
            code=Op.SSTORE(key=0x1, value=Op.DELEGATECALL(gas=0x3d090, address=0xd42cd48f1d9a88f4b75bfb5e46e754c1128bd7fb, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40)) + Op.STOP,
        ),
        callee_1: Account(
            code=Op.SSTORE(key=0x2, value=0x1) + Op.SSTORE(key=0x4, value=Op.CALLER) + Op.SSTORE(key=0x5, value=Op.CALLVALUE) + Op.SSTORE(key=0xe6, value=Op.ADDRESS) + Op.SSTORE(key=0xe8, value=Op.ORIGIN) + Op.SSTORE(key=0xec, value=Op.CALLDATASIZE) + Op.SSTORE(key=0xee, value=Op.CODESIZE) + Op.SSTORE(key=0xf0, value=Op.GASPRICE) + Op.STOP,
        ),
        contract: Account(
            storage={0: 1, 1: 1, 2: 1, 4: 0xdb43306b16c521b9cc3667fbe7d1b697bb1f9605, 5: 1, 230: 0xdb43306b16c521b9cc3667fbe7d1b697bb1f9605, 232: 0xebaf50debf10e08302fe4280c32df010463ca297, 236: 64, 238: 34, 240: 10},
            code=Op.SSTORE(key=0x0, value=Op.CALLCODE(gas=0x55730, address=0x1ccccf19d84280c8a0e94209761296dabd87b3c9, value=0x1, args_offset=0x0, args_size=0x40, ret_offset=0x0, ret_size=0x40)) + Op.STOP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
