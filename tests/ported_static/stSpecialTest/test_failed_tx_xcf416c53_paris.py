"""
Ported from:
tests/static/state_tests/stSpecialTest/failed_tx_xcf416c53_ParisFiller.json
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
    ["tests/static/state_tests/stSpecialTest/failed_tx_xcf416c53_ParisFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_failed_tx_xcf416c53_paris(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x68795c4aa09d6f4ed3e5deddf8c2ad3049a601da")
    sender = Address("0xadd22153059388891d82c6c8e08d80845352bbb0")
    contract = Address("0x7e6e9b4ca1b88937abeaec23bc4b6986caf05188")
    callee = Address("0x76fae819612a29489a1a43208613d8f8557b8898")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=200000000,
    )

    pre[callee] = Account(balance=10, nonce=0)
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
        Op.DIV(Op.CALLDATALOAD(offset=0x0), 0x100000000000000000000000000000000000000000000000000000000)
        + Op.JUMPI(pc=Op.PUSH2[0x65], condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x97dd3054)))
        + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MLOAD(offset=0x40) + Op.MLOAD(offset=0x60) + Op.JUMPDEST
        + Op.JUMPI(pc=Op.PUSH2[0x62], condition=Op.ISZERO(Op.SLT(Op.DUP3, Op.DUP1)))
        + Op.POP(Op.CALL(gas=0x0, address=Op.DUP7, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.ADD(Op.DUP3, 0x1) + Op.SWAP2 + Op.POP + Op.JUMP(pc=Op.PUSH2[0x40])
        + Op.JUMPDEST + Op.POP + Op.POP + Op.JUMPDEST + Op.POP
    ),
    )
    pre[sender] = Account(balance=0xde0b6b3a7640000, nonce=1)

    tx = Transaction(
        secret_key=Hash(
            "0x0ff8d58222f34f6890ddaa468c023b77d6691ed7d3c4dcddae38336212faf54b"
        ),
        to=contract,
        data=bytes.fromhex(
            "97dd30540000000000000000000000000000000000000000000000000000000000000000"
            "00000000000000000000000000000000000000000000000000000000000002bc"
        ),
        gas_limit=16300000,
        gas_price=10,
        nonce=1,
        value=0,
    )

    post = {
        contract: Account(
            code=Op.DIV(Op.CALLDATALOAD(offset=0x0), 0x100000000000000000000000000000000000000000000000000000000) + Op.JUMPI(pc=Op.PUSH2[0x65], condition=Op.ISZERO(Op.EQ(Op.DUP2, 0x97dd3054))) + Op.MSTORE(offset=0x40, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x60, value=Op.CALLDATALOAD(offset=0x24)) + Op.MLOAD(offset=0x40) + Op.MLOAD(offset=0x60) + Op.JUMPDEST + Op.JUMPI(pc=Op.PUSH2[0x62], condition=Op.ISZERO(Op.SLT(Op.DUP3, Op.DUP1))) + Op.POP(Op.CALL(gas=0x0, address=Op.DUP7, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.ADD(Op.DUP3, 0x1) + Op.SWAP2 + Op.POP + Op.JUMP(pc=Op.PUSH2[0x40]) + Op.JUMPDEST + Op.POP + Op.POP + Op.JUMPDEST + Op.POP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
