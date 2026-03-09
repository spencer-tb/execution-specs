"""
Ori Pomerantz   qbzzt1@gmail.com

Ported from:
tests/static/state_tests/stRandom/randomStatetest384Filler.yml
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
    ["tests/static/state_tests/stRandom/randomStatetest384Filler.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_random_statetest384(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Ori Pomerantz   qbzzt1@gmail.com."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x2462945f21bb3b46ed8b2a975227d838bd1c8038")
    contract = Address("0x14ceed78f6e86eead0a39e3f5c3481c7c233e8ea")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=71794957647893862,
    )

    pre[contract] = Account(
        balance=0xde0b6b3a7640000,
        nonce=1,
        code=(
        Op.EXTCODESIZE(address=0x6675a4758d443dbff535f034a4eda729a6ffc1e59f674e0c55)
        + Op.PUSH6[0x5d7974272ac7] + Op.AND(0xffff, 0x18ce2014249172572ed5eac0b9d2e4)
        + Op.SWAP1 + Op.LOG0(offset=Op.AND, size=0xffff) + Op.CALLER + Op.GT
        + Op.BASEFEE
        + Op.EXTCODESIZE(address=Op.EQ(0x513376bc288aa1fdb973c149cd, Op.DELEGATECALL(gas=Op.GAS, address=0x4d84673d975d1811374a239ef14ee26532d643cc4dd6e9115e28815562c2eb94, args_offset=0xad13, args_size=0xa9bb, ret_offset=0x9fe1, ret_size=0xc0cd)))
        + Op.PUSH25[0x89cc6512f8d604e5d0656c17f2d45b916df6816a1999719f2b]
        + Op.JUMPI(pc=Op.ADD(0x8, Op.PC), condition=Op.AND(0x1, 0xd521394f07100138b341f1debc06c3fb3cbc))
        + Op.POP(0xcb) + Op.JUMPDEST
        + Op.PUSH19[0x27e1dc4c54400e52ab133f162c6df107151d11] + Op.GASLIMIT + Op.SWAP4
        + Op.SWAP5 + Op.GASLIMIT + Op.DUP1
        + Op.PUSH31[0x5153417e8ff00d138f0dffc0cd79ced2ececd6f0dce826302e4129cb6c37ab]
        + Op.NUMBER + Op.COINBASE + Op.JUMPDEST
        + Op.AND(0xffff, Op.DELEGATECALL(gas=Op.GAS, address=0xa5d352916626fe6be4aa6ef0e7634db7909fd79752e5bcb504b358d36af70849, args_offset=0xc30, args_size=0x52a9, ret_offset=0x73ce, ret_size=0x45c1))
        + Op.SWAP1 + Op.PUSH2[0xffff] + Op.AND + Op.LOG2
        + Op.MLOAD(offset=Op.AND(0xffff, 0xe900f727806828f5ee6088ebf8))
        + Op.PUSH17[0x15c1269fa9f5387ab7387a81f51905640] + Op.SWAP9 + Op.PUSH1[0x1f]
        + Op.SWAP5 + Op.PUSH18[0xb46eb2f2d66ee0b4c6845455e9c5eeff0218]
        + Op.SMOD(0x66120b1a7a97c93a6a04bd493f4a, 0xbae1d66f6cb6213c6ce69859f1046ae4cb5e5b743ab7)
        + Op.SWAP7 + Op.RETURNDATASIZE + Op.SIGNEXTEND
        + Op.PUSH10[0x471b70dec306fa6142ce] + Op.SWAP13
        + Op.MOD(Op.SDIV(0xa04ea7e0bd9d9cda29962b, Op.BLOCKHASH(block_number=Op.SUB(Op.NUMBER, Op.AND))), 0xff)
        + Op.PUSH19[0x46ce83ab26762d5e2cfb614aa2394ad1d70ea9] + Op.CODESIZE + Op.DUP6
        + Op.PUSH12[0x938d5c3ff280bf7efda95e66] + Op.DUP11
        + Op.PUSH17[0x149afa7a18bf9c2d796de03773e0d35c9a]
        + Op.NOT(0x8e0e968ba16f3ad59d6442ddbdb9e537908db1f791bb3f17b33a1433340107)
        + Op.PUSH2[0xa168] + Op.SWAP13
        + Op.PUSH28[0x413ed4a9b16e7d66a17b07730188a08fa9e6148100f0311ea269ecc5]
        + Op.DUP9 + Op.PUSH1[0x7d]
        + Op.PUSH32[0xcbfff9f42e22612e938809af2674b0cedc8548f47ee642097c0c4abc9bf7c76b]
        + Op.SWAP7 + Op.PUSH25[0x996410d0bf28e5e3e1b35b37ffce70e346e013d5345494d476]
        + Op.SWAP1 + Op.CALLER + Op.TIMESTAMP
        + Op.DELEGATECALL(gas=Op.GAS, address=0x1396b439a0049676213fd1ff8b75232dbd2117c0c5dcc184d76e2534ea9628ac, args_offset=0xf195, args_size=0x74fd, ret_offset=0xabae, ret_size=0x7717)
        + Op.DUP7 + Op.GASPRICE + Op.SWAP8 + Op.PUSH2[0xffff] + Op.AND + Op.SWAP1
        + Op.LOG0(offset=Op.AND, size=0xffff)
        + Op.MSTORE8(offset=Op.AND(0xffff, Op.EQ), value=0x486085a7047bd1acab7c048c2ae5a07a9e25934021cfaf0651efbd393b7214)
        + Op.PUSH2[0xffff] + Op.AND + Op.SWAP1 + Op.PUSH2[0xffff] + Op.AND + Op.LOG1
        + Op.EQ(Op.DIV(Op.ADDRESS, Op.DUP7), 0x84ed962562151d0b903fb2) + Op.DIV
        + Op.PUSH20[0x380357280d5dbc434298ac45559fc2855c0d2a04] + Op.GAS
        + Op.PUSH7[0xaf59655ed483a0]
        + Op.SHL(0x5f1536b1893659fbb9ffa023722beb2f24b5693be6b572737fed, Op.BLOCKHASH(block_number=Op.SUB(Op.NUMBER, Op.AND(0xff, Op.BALANCE(address=Op.PC)))))
        + Op.SWAP14 + Op.EXP + Op.PUSH5[0x6f7a2658b5] + Op.DUP12 + Op.JUMPDEST
        + Op.COINBASE + Op.PUSH19[0x20e684f471111724a4f72553b4fdc9593ae22c] + Op.SWAP7
        + Op.SWAP6 + Op.SWAP10
        + Op.CALL(gas=Op.GAS, address=0x39dbe091b64b8be6a557a93bf2c25dd042e8c8fea4db3bd8ee5be3eabde2835e, value=0x8fe0, args_offset=0xf3f6, args_size=0x1991, ret_offset=0x5ad4, ret_size=0xa631)
        + Op.SSTORE(key=0x0, value=Op.SDIV) + Op.PUSH1[0x1] + Op.SSTORE
        + Op.PUSH1[0x2] + Op.SSTORE + Op.PUSH1[0x3] + Op.SSTORE + Op.PUSH1[0x4]
        + Op.SSTORE + Op.PUSH1[0x5] + Op.SSTORE + Op.PUSH1[0x6] + Op.SSTORE
        + Op.PUSH1[0x7] + Op.SSTORE + Op.PUSH1[0x8] + Op.SSTORE + Op.PUSH1[0x9]
        + Op.SSTORE + Op.PUSH1[0xa] + Op.SSTORE + Op.PUSH1[0xb] + Op.SSTORE
        + Op.PUSH1[0xc] + Op.SSTORE + Op.PUSH1[0xd] + Op.SSTORE + Op.PUSH1[0xe]
        + Op.SSTORE + Op.PUSH1[0xf] + Op.SSTORE + Op.PUSH1[0x10] + Op.SSTORE
        + Op.PUSH1[0x11] + Op.SSTORE + Op.PUSH1[0x12] + Op.SSTORE + Op.PUSH1[0x13]
        + Op.SSTORE + Op.PUSH1[0x14] + Op.SSTORE + Op.PUSH1[0x15] + Op.SSTORE
        + Op.PUSH1[0x16] + Op.SSTORE + Op.PUSH1[0x17] + Op.SSTORE + Op.PUSH1[0x18]
        + Op.SSTORE + Op.PUSH1[0x19] + Op.SSTORE + Op.PUSH1[0x1a] + Op.SSTORE
        + Op.PUSH1[0x1b] + Op.SSTORE + Op.PUSH1[0x1c] + Op.SSTORE + Op.PUSH1[0x1d]
        + Op.SSTORE + Op.PUSH1[0x1e] + Op.SSTORE
        + Op.RETURN(offset=0xc065, size=0x2739)
    ),
    )
    pre[sender] = Account(balance=0x3635c9adc5dea00000, nonce=1)

    tx = Transaction(
        secret_key=Hash(
            "0x04dc42d61413d4ded993826ac4d6ed7a4a970c60335d2b285c60a4274e792ff1"
        ),
        to=contract,
        data=b"",
        gas_limit=16777216,
        gas_price=100,
        nonce=1,
        value=0,
    )

    post = {
        contract: Account(
            storage={1: 0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba, 2: 0x938d5c3ff280bf7efda95e66, 3: 0x6f7a2658b5, 4: 0x9582ced6097ae8d75cb9cac205753dd88202d5d36541f1b1bb9c1446739e0d01, 5: 0xf400ca, 7: 0x20e684f471111724a4f72553b4fdc9593ae22c, 8: 100, 9: 0x413ed4a9b16e7d66a17b07730188a08fa9e6148100f0311ea269ecc5, 10: 0x380357280d5dbc434298ac45559fc2855c0d2a04, 11: 0xff71f169745e90c52a629bbd2242461ac86f724e086e44c0e84cc5ebcccbfef8, 12: 0x149afa7a18bf9c2d796de03773e0d35c9a, 13: 0xcbfff9f42e22612e938809af2674b0cedc8548f47ee642097c0c4abc9bf7c76b, 14: 0x938d5c3ff280bf7efda95e66, 15: 10, 16: 996, 19: 0xb46eb2f2d66ee0b4c6845455e9c5eeff0218, 20: 1, 21: 10, 23: 41320, 24: 0xff112233445566, 25: 0x66120b1a7a97c93a6a04bd493f4a, 26: 0x27e1dc4c54400e52ab133f162c6df107151d11, 27: 0x89cc6512f8d604e5d0656c17f2d45b916df6816a1999719f2b, 29: 0xff112233445566, 30: 0x471b70dec306fa6142ce},
            code=Op.EXTCODESIZE(address=0x6675a4758d443dbff535f034a4eda729a6ffc1e59f674e0c55) + Op.PUSH6[0x5d7974272ac7] + Op.AND(0xffff, 0x18ce2014249172572ed5eac0b9d2e4) + Op.SWAP1 + Op.LOG0(offset=Op.AND, size=0xffff) + Op.CALLER + Op.GT + Op.BASEFEE + Op.EXTCODESIZE(address=Op.EQ(0x513376bc288aa1fdb973c149cd, Op.DELEGATECALL(gas=Op.GAS, address=0x4d84673d975d1811374a239ef14ee26532d643cc4dd6e9115e28815562c2eb94, args_offset=0xad13, args_size=0xa9bb, ret_offset=0x9fe1, ret_size=0xc0cd))) + Op.PUSH25[0x89cc6512f8d604e5d0656c17f2d45b916df6816a1999719f2b] + Op.JUMPI(pc=Op.ADD(0x8, Op.PC), condition=Op.AND(0x1, 0xd521394f07100138b341f1debc06c3fb3cbc)) + Op.POP(0xcb) + Op.JUMPDEST + Op.PUSH19[0x27e1dc4c54400e52ab133f162c6df107151d11] + Op.GASLIMIT + Op.SWAP4 + Op.SWAP5 + Op.GASLIMIT + Op.DUP1 + Op.PUSH31[0x5153417e8ff00d138f0dffc0cd79ced2ececd6f0dce826302e4129cb6c37ab] + Op.NUMBER + Op.COINBASE + Op.JUMPDEST + Op.AND(0xffff, Op.DELEGATECALL(gas=Op.GAS, address=0xa5d352916626fe6be4aa6ef0e7634db7909fd79752e5bcb504b358d36af70849, args_offset=0xc30, args_size=0x52a9, ret_offset=0x73ce, ret_size=0x45c1)) + Op.SWAP1 + Op.PUSH2[0xffff] + Op.AND + Op.LOG2 + Op.MLOAD(offset=Op.AND(0xffff, 0xe900f727806828f5ee6088ebf8)) + Op.PUSH17[0x15c1269fa9f5387ab7387a81f51905640] + Op.SWAP9 + Op.PUSH1[0x1f] + Op.SWAP5 + Op.PUSH18[0xb46eb2f2d66ee0b4c6845455e9c5eeff0218] + Op.SMOD(0x66120b1a7a97c93a6a04bd493f4a, 0xbae1d66f6cb6213c6ce69859f1046ae4cb5e5b743ab7) + Op.SWAP7 + Op.RETURNDATASIZE + Op.SIGNEXTEND + Op.PUSH10[0x471b70dec306fa6142ce] + Op.SWAP13 + Op.MOD(Op.SDIV(0xa04ea7e0bd9d9cda29962b, Op.BLOCKHASH(block_number=Op.SUB(Op.NUMBER, Op.AND))), 0xff) + Op.PUSH19[0x46ce83ab26762d5e2cfb614aa2394ad1d70ea9] + Op.CODESIZE + Op.DUP6 + Op.PUSH12[0x938d5c3ff280bf7efda95e66] + Op.DUP11 + Op.PUSH17[0x149afa7a18bf9c2d796de03773e0d35c9a] + Op.NOT(0x8e0e968ba16f3ad59d6442ddbdb9e537908db1f791bb3f17b33a1433340107) + Op.PUSH2[0xa168] + Op.SWAP13 + Op.PUSH28[0x413ed4a9b16e7d66a17b07730188a08fa9e6148100f0311ea269ecc5] + Op.DUP9 + Op.PUSH1[0x7d] + Op.PUSH32[0xcbfff9f42e22612e938809af2674b0cedc8548f47ee642097c0c4abc9bf7c76b] + Op.SWAP7 + Op.PUSH25[0x996410d0bf28e5e3e1b35b37ffce70e346e013d5345494d476] + Op.SWAP1 + Op.CALLER + Op.TIMESTAMP + Op.DELEGATECALL(gas=Op.GAS, address=0x1396b439a0049676213fd1ff8b75232dbd2117c0c5dcc184d76e2534ea9628ac, args_offset=0xf195, args_size=0x74fd, ret_offset=0xabae, ret_size=0x7717) + Op.DUP7 + Op.GASPRICE + Op.SWAP8 + Op.PUSH2[0xffff] + Op.AND + Op.SWAP1 + Op.LOG0(offset=Op.AND, size=0xffff) + Op.MSTORE8(offset=Op.AND(0xffff, Op.EQ), value=0x486085a7047bd1acab7c048c2ae5a07a9e25934021cfaf0651efbd393b7214) + Op.PUSH2[0xffff] + Op.AND + Op.SWAP1 + Op.PUSH2[0xffff] + Op.AND + Op.LOG1 + Op.EQ(Op.DIV(Op.ADDRESS, Op.DUP7), 0x84ed962562151d0b903fb2) + Op.DIV + Op.PUSH20[0x380357280d5dbc434298ac45559fc2855c0d2a04] + Op.GAS + Op.PUSH7[0xaf59655ed483a0] + Op.SHL(0x5f1536b1893659fbb9ffa023722beb2f24b5693be6b572737fed, Op.BLOCKHASH(block_number=Op.SUB(Op.NUMBER, Op.AND(0xff, Op.BALANCE(address=Op.PC))))) + Op.SWAP14 + Op.EXP + Op.PUSH5[0x6f7a2658b5] + Op.DUP12 + Op.JUMPDEST + Op.COINBASE + Op.PUSH19[0x20e684f471111724a4f72553b4fdc9593ae22c] + Op.SWAP7 + Op.SWAP6 + Op.SWAP10 + Op.CALL(gas=Op.GAS, address=0x39dbe091b64b8be6a557a93bf2c25dd042e8c8fea4db3bd8ee5be3eabde2835e, value=0x8fe0, args_offset=0xf3f6, args_size=0x1991, ret_offset=0x5ad4, ret_size=0xa631) + Op.SSTORE(key=0x0, value=Op.SDIV) + Op.PUSH1[0x1] + Op.SSTORE + Op.PUSH1[0x2] + Op.SSTORE + Op.PUSH1[0x3] + Op.SSTORE + Op.PUSH1[0x4] + Op.SSTORE + Op.PUSH1[0x5] + Op.SSTORE + Op.PUSH1[0x6] + Op.SSTORE + Op.PUSH1[0x7] + Op.SSTORE + Op.PUSH1[0x8] + Op.SSTORE + Op.PUSH1[0x9] + Op.SSTORE + Op.PUSH1[0xa] + Op.SSTORE + Op.PUSH1[0xb] + Op.SSTORE + Op.PUSH1[0xc] + Op.SSTORE + Op.PUSH1[0xd] + Op.SSTORE + Op.PUSH1[0xe] + Op.SSTORE + Op.PUSH1[0xf] + Op.SSTORE + Op.PUSH1[0x10] + Op.SSTORE + Op.PUSH1[0x11] + Op.SSTORE + Op.PUSH1[0x12] + Op.SSTORE + Op.PUSH1[0x13] + Op.SSTORE + Op.PUSH1[0x14] + Op.SSTORE + Op.PUSH1[0x15] + Op.SSTORE + Op.PUSH1[0x16] + Op.SSTORE + Op.PUSH1[0x17] + Op.SSTORE + Op.PUSH1[0x18] + Op.SSTORE + Op.PUSH1[0x19] + Op.SSTORE + Op.PUSH1[0x1a] + Op.SSTORE + Op.PUSH1[0x1b] + Op.SSTORE + Op.PUSH1[0x1c] + Op.SSTORE + Op.PUSH1[0x1d] + Op.SSTORE + Op.PUSH1[0x1e] + Op.SSTORE + Op.RETURN(offset=0xc065, size=0x2739),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
