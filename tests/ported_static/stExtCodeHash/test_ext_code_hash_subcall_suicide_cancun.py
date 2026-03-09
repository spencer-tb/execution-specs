"""
transaction to B | B call to A | A delegatecall/callcode to C (C has selfdestruct) | A selfdestructed. returned to B. now we could check extcodehash of A (in account B code)

Ported from:
tests/static/state_tests/stExtCodeHash/extCodeHashSubcallSuicideCancunFiller.yml
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
    ["tests/static/state_tests/stExtCodeHash/extCodeHashSubcallSuicideCancunFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_ext_code_hash_subcall_suicide_cancun(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """transaction to B | B call to A | A delegatecall/callcode to C (C has selfdestruct) | A selfdestructed. returned to B. now we could check extcodehash of A (in account B code)."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xb000000000000000000000000000000000000000")
    callee = Address("0xa000000000000000000000000000000000000000")
    callee_1 = Address("0xd000000000000000000000000000000000000000")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[callee] = Account(
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=(
        Op.CALLCODE(gas=0x55730, address=0x3e180b1862f9d158abb5e519a6d8605540c23682, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x20)
        + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0xde0b6b3a7640000, nonce=0)
    pre[contract] = Account(
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=(
        Op.PUSH1[0x49] + Op.CODECOPY(dest_offset=0x0, offset=0x10c, size=Op.DUP1)
        + Op.PUSH1[0x0] + Op.PUSH8[0xde0b6b3a7640000] + Op.POP(Op.CREATE)
        + Op.SSTORE(key=0x1, value=Op.EXTCODEHASH(address=0xa000000000000000000000000000000000000000))
        + Op.SSTORE(key=0x2, value=Op.EXTCODESIZE(address=0xa000000000000000000000000000000000000000))
        + Op.EXTCODECOPY(address=0xa000000000000000000000000000000000000000, dest_offset=0x0, offset=0x0, size=0x20)
        + Op.SSTORE(key=0x3, value=Op.MLOAD(offset=0x0))
        + Op.POP(Op.CALL(gas=0x55730, address=0xa000000000000000000000000000000000000000, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x20))
        + Op.SSTORE(key=0x4, value=Op.EXTCODEHASH(address=0xa000000000000000000000000000000000000000))
        + Op.SSTORE(key=0x5, value=Op.EXTCODESIZE(address=0xa000000000000000000000000000000000000000))
        + Op.EXTCODECOPY(address=0xa000000000000000000000000000000000000000, dest_offset=0x0, offset=0x0, size=0x20)
        + Op.SSTORE(key=0x6, value=Op.MLOAD(offset=0x0))
        + Op.SSTORE(key=0x7, value=Op.CALL(gas=0x55730, address=0xa000000000000000000000000000000000000000, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x20))
        + Op.STOP + Op.INVALID
        + Op.POP(Op.CALL(gas=0x186a0, address=0xd000000000000000000000000000000000000000, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.PUSH1[0x17] + Op.CODECOPY(dest_offset=0x0, offset=0x32, size=Op.DUP1)
        + Op.PUSH1[0x0] + Op.RETURN + Op.STOP + Op.INVALID
        + Op.SELFDESTRUCT(address=0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b)
        + Op.STOP
    ),
    )
    pre[callee_1] = Account(
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=Op.SSTORE(key=0x1, value=0x1) + Op.STOP,
    )

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=b"",
        gas_limit=500000,
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = {
        Address("0x3e180b1862f9d158abb5e519a6d8605540c23682"): Account(
            code=Op.SELFDESTRUCT(address=0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b) + Op.STOP,
        ),
        callee: Account(
            code=Op.CALLCODE(gas=0x55730, address=0x3e180b1862f9d158abb5e519a6d8605540c23682, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x20) + Op.STOP,
        ),
        contract: Account(
            storage={1: 0x807d478bd0d0173122f5531d4c43781631444232a0816dd35578747c7d67af0d, 2: 37, 3: 0x60206000600060006000733e180b1862f9d158abb5e519a6d8605540c2368262, 4: 0x807d478bd0d0173122f5531d4c43781631444232a0816dd35578747c7d67af0d, 5: 37, 6: 0x60206000600060006000733e180b1862f9d158abb5e519a6d8605540c2368262, 7: 1},
            code=Op.PUSH1[0x49] + Op.CODECOPY(dest_offset=0x0, offset=0x10c, size=Op.DUP1) + Op.PUSH1[0x0] + Op.PUSH8[0xde0b6b3a7640000] + Op.POP(Op.CREATE) + Op.SSTORE(key=0x1, value=Op.EXTCODEHASH(address=0xa000000000000000000000000000000000000000)) + Op.SSTORE(key=0x2, value=Op.EXTCODESIZE(address=0xa000000000000000000000000000000000000000)) + Op.EXTCODECOPY(address=0xa000000000000000000000000000000000000000, dest_offset=0x0, offset=0x0, size=0x20) + Op.SSTORE(key=0x3, value=Op.MLOAD(offset=0x0)) + Op.POP(Op.CALL(gas=0x55730, address=0xa000000000000000000000000000000000000000, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x20)) + Op.SSTORE(key=0x4, value=Op.EXTCODEHASH(address=0xa000000000000000000000000000000000000000)) + Op.SSTORE(key=0x5, value=Op.EXTCODESIZE(address=0xa000000000000000000000000000000000000000)) + Op.EXTCODECOPY(address=0xa000000000000000000000000000000000000000, dest_offset=0x0, offset=0x0, size=0x20) + Op.SSTORE(key=0x6, value=Op.MLOAD(offset=0x0)) + Op.SSTORE(key=0x7, value=Op.CALL(gas=0x55730, address=0xa000000000000000000000000000000000000000, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x20)) + Op.STOP + Op.INVALID + Op.POP(Op.CALL(gas=0x186a0, address=0xd000000000000000000000000000000000000000, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.PUSH1[0x17] + Op.CODECOPY(dest_offset=0x0, offset=0x32, size=Op.DUP1) + Op.PUSH1[0x0] + Op.RETURN + Op.STOP + Op.INVALID + Op.SELFDESTRUCT(address=0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b) + Op.STOP,
        ),
        callee_1: Account(storage={1: 1}, code=Op.SSTORE(key=0x1, value=0x1) + Op.STOP),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
