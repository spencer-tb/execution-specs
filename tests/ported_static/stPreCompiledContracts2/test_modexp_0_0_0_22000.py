"""
Puts the base 0, exponent 0 and modulus 0 into the MODEXP precompile, saves the hash of the result. Gives the execution 22000 gas

Ported from:
tests/static/state_tests/stPreCompiledContracts2/modexp_0_0_0_22000Filler.json
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
    ["tests/static/state_tests/stPreCompiledContracts2/modexp_0_0_0_22000Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit",
    [
        48136,
        90000,
        110000,
        200000,
    ],
    ids=['case0', 'case1', 'case2', 'case3'],
)
@pytest.mark.pre_alloc_mutable
def test_modexp_0_0_0_22000(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
) -> None:
    """Puts the base 0, exponent 0 and modulus 0 into the MODEXP precompile, saves the hash of the result. Gives the execution 22000 gas."""
    coinbase = Address("0x3535353535353535353535353535353535353535")
    sender = Address("0x82a978b3f5962a5b0957d9ee9eef472ee55b42f1")
    contract = Address("0xc305c901078781c232a2a521c2af7980f8385ee9")
    callee = Address("0x0000000000000000000000000000000000000001")
    callee_1 = Address("0x0000000000000000000000000000000000000002")
    callee_2 = Address("0x0000000000000000000000000000000000000003")
    callee_3 = Address("0x0000000000000000000000000000000000000004")
    callee_4 = Address("0x0000000000000000000000000000000000000005")
    callee_5 = Address("0x0000000000000000000000000000000000000006")
    callee_6 = Address("0x0000000000000000000000000000000000000007")
    callee_7 = Address("0x0000000000000000000000000000000000000008")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000,
    )

    pre[callee] = Account(balance=1, nonce=0)
    pre[callee_1] = Account(balance=1, nonce=0)
    pre[callee_2] = Account(balance=1, nonce=0)
    pre[callee_3] = Account(balance=1, nonce=0)
    pre[callee_4] = Account(balance=1, nonce=0)
    pre[callee_5] = Account(balance=1, nonce=0)
    pre[callee_6] = Account(balance=1, nonce=0)
    pre[callee_7] = Account(balance=1, nonce=0)
    pre[coinbase] = Account(balance=0x201ee, nonce=0)
    pre[sender] = Account(balance=0xde0b6b3a761fe12, nonce=1)
    pre[contract] = Account(
        balance=0,
        nonce=1,
        code=(
        Op.MSTORE(offset=0x1c, value=Op.CALLDATALOAD(offset=0x0))
        + Op.MSTORE(offset=0x20, value=0x10000000000000000000000000000000000000000)
        + Op.MSTORE(offset=0x40, value=0xffffffffffffffffffffffffffffffff)
        + Op.MSTORE(offset=0x60, value=0xffffffffffffffffffffffffffffffff00000000000000000000000000000001)
        + Op.MSTORE(offset=0x80, value=0x2540be3fffffffffffffffffffffffffdabf41c00)
        + Op.MSTORE(offset=0xa0, value=0xfffffffffffffffffffffffdabf41c00000000000000000000000002540be400)
        + Op.JUMPI(pc=0x12b, condition=Op.ISZERO(Op.EQ(Op.MLOAD(offset=0x0), 0x30c8d1da)))
        + Op.JUMPI(pc=Op.PC, condition=Op.ISZERO(Op.ISZERO(Op.GT(Op.CALLDATALOAD(offset=Op.ADD(0x4, Op.CALLDATALOAD(offset=0x4))), 0x84))))
        + Op.CALLDATACOPY(dest_offset=0x140, offset=Op.ADD(0x4, Op.CALLDATALOAD(offset=0x4)), size=Op.ADD(0x20, Op.CALLDATALOAD(offset=Op.ADD(0x4, Op.CALLDATALOAD(offset=0x4)))))
        + Op.JUMPI(pc=Op.PC, condition=Op.ISZERO(Op.CALL(gas=0x5f5e0ff, address=0x5, value=0x0, args_offset=0x160, args_size=Op.MLOAD(offset=0x140), ret_offset=0x240, ret_size=0x1)))
        + Op.MSTORE(offset=0x220, value=0x1) + Op.PUSH2[0x220] + Op.PUSH1[0x21]
        + Op.POP(Op.CALL(gas=0x15, address=0x4, value=0x0, args_offset=Op.DUP5, args_size=Op.DUP3, ret_offset=0x280, ret_size=Op.DUP1))
        + Op.POP + Op.POP + Op.PUSH2[0x280]
        + Op.SHA3(offset=Op.ADD(Op.DUP3, 0x20), size=Op.MLOAD(offset=Op.DUP1))
        + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.SSTORE + Op.PUSH2[0x280]
        + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x20), value=0x20)
        + Op.ADD(Op.MLOAD(offset=Op.DUP2), 0x40)
        + Op.SUB(Op.ADD(Op.DUP3, 0x1f), Op.MOD(Op.SUB(Op.DUP3, 0x1), 0x20)) + Op.SWAP1
        + Op.POP + Op.SUB(Op.DUP3, 0x20) + Op.RETURN + Op.POP + Op.STOP + Op.JUMPDEST
    ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0x044852b2a670ade5407e78fb2863c51de9fcb96542a07186fe3aeda6bb8a116d"
        ),
        to=contract,
        data=bytes.fromhex("30c8d1da00000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000060000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"),
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=1,
        value=0,
    )

    post = {
        contract: Account(
            storage={0: 0xbc36789e7a1e281436464229828f817d6612f7b477d66591ff96a9e064bcc98a},
            code=Op.MSTORE(offset=0x1c, value=Op.CALLDATALOAD(offset=0x0)) + Op.MSTORE(offset=0x20, value=0x10000000000000000000000000000000000000000) + Op.MSTORE(offset=0x40, value=0xffffffffffffffffffffffffffffffff) + Op.MSTORE(offset=0x60, value=0xffffffffffffffffffffffffffffffff00000000000000000000000000000001) + Op.MSTORE(offset=0x80, value=0x2540be3fffffffffffffffffffffffffdabf41c00) + Op.MSTORE(offset=0xa0, value=0xfffffffffffffffffffffffdabf41c00000000000000000000000002540be400) + Op.JUMPI(pc=0x12b, condition=Op.ISZERO(Op.EQ(Op.MLOAD(offset=0x0), 0x30c8d1da))) + Op.JUMPI(pc=Op.PC, condition=Op.ISZERO(Op.ISZERO(Op.GT(Op.CALLDATALOAD(offset=Op.ADD(0x4, Op.CALLDATALOAD(offset=0x4))), 0x84)))) + Op.CALLDATACOPY(dest_offset=0x140, offset=Op.ADD(0x4, Op.CALLDATALOAD(offset=0x4)), size=Op.ADD(0x20, Op.CALLDATALOAD(offset=Op.ADD(0x4, Op.CALLDATALOAD(offset=0x4))))) + Op.JUMPI(pc=Op.PC, condition=Op.ISZERO(Op.CALL(gas=0x5f5e0ff, address=0x5, value=0x0, args_offset=0x160, args_size=Op.MLOAD(offset=0x140), ret_offset=0x240, ret_size=0x1))) + Op.MSTORE(offset=0x220, value=0x1) + Op.PUSH2[0x220] + Op.PUSH1[0x21] + Op.POP(Op.CALL(gas=0x15, address=0x4, value=0x0, args_offset=Op.DUP5, args_size=Op.DUP3, ret_offset=0x280, ret_size=Op.DUP1)) + Op.POP + Op.POP + Op.PUSH2[0x280] + Op.SHA3(offset=Op.ADD(Op.DUP3, 0x20), size=Op.MLOAD(offset=Op.DUP1)) + Op.SWAP1 + Op.POP + Op.PUSH1[0x0] + Op.SSTORE + Op.PUSH2[0x280] + Op.MSTORE(offset=Op.SUB(Op.DUP3, 0x20), value=0x20) + Op.ADD(Op.MLOAD(offset=Op.DUP2), 0x40) + Op.SUB(Op.ADD(Op.DUP3, 0x1f), Op.MOD(Op.SUB(Op.DUP3, 0x1), 0x20)) + Op.SWAP1 + Op.POP + Op.SUB(Op.DUP3, 0x20) + Op.RETURN + Op.POP + Op.STOP + Op.JUMPDEST,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
