"""
Deploy legacy contract normally

Ported from:
tests/static/state_tests/stCallCreateCallCodeTest/createJS_NoCollisionFiller.json
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
    ["tests/static/state_tests/stCallCreateCallCodeTest/createJS_NoCollisionFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_create_js_no_collision(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Deploy legacy contract normally."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    pre[sender] = Account(balance=0x9184e72a000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=None,
        data=bytes.fromhex(
            "60406103ca60043960045160245133600081905550600060048190555081600181905550"
            "8060028190555042600581905550336003819055505050610381806100496000396000f3"
            "0060003560e060020a9004806343d726d61461004257806391b7f5ed14610050578063d6"
            "86f9ee14610061578063f5bade661461006f578063fcfff16f1461008057005b61004a61"
            "01de565b60006000f35b61005b6004356100bf565b60006000f35b610069610304565b60"
            "006000f35b61007a60043561008e565b60006000f35b6100886100f0565b60006000f35b"
            "600054600160a060020a031633600160a060020a031614156100af576100b4565b6100bc"
            "565b806001819055505b50565b600054600160a060020a031633600160a060020a031614"
            "156100e0576100e5565b6100ed565b806002819055505b50565b600054600160a060020a"
            "031633600160a060020a031614806101255750600354600160a060020a031633600160a0"
            "60020a0316145b61012e57610161565b60016004819055507f59ebeb90bc63057b651567"
            "3c3ecf9438e5058bca0f92585014eced636878c9a560006000a16101dc565b6004546001"
            "1480610173575060015434105b6101b85760016004819055507f59ebeb90bc63057b6515"
            "673c3ecf9438e5058bca0f92585014eced636878c9a560006000a1426005819055503360"
            "03819055506101db565b33600160a060020a03166000346000600060006000848787f161"
            "01d757005b5050505b5b565b60006004546000146101ef576101f4565b610301565b6000"
            "54600160a060020a031633600160a060020a031614801561022c5750600054600160a060"
            "020a0316600354600160a060020a0316145b61023557610242565b600060048190555061"
            "0301565b600354600160a060020a031633600160a060020a03161461026257610300565b"
            "600554420360025402905060015481116102c757600354600160a060020a031660008260"
            "0154036000600060006000848787f161029b57005b505050600054600160a060020a0316"
            "6000826000600060006000848787f16102bf57005b5050506102ee565b600054600160a0"
            "60020a031660006001546000600060006000848787f16102ea57005b5050505b60006004"
            "819055506000546003819055505b5b50565b6000600054600160a060020a031633600160"
            "a060020a031614156103275761032c565b61037e565b6005544203600254029050600154"
            "81116103455761037d565b600054600160a060020a031660006001546000600060006000"
            "848787f161036857005b50505060006004819055506000546003819055505b5b50560000"
            "000000000000000000000000000000000000000000000000000000000042000000000000"
            "0000000000000000000000000000000000000000000000000023"
        ),
        gas_limit=600000,
        gas_price=10,
        nonce=0,
        value=100000,
    )

    post = {
        Address("0x6295ee1b4f6dd65047762f924ecd367c17eabf8f"): Account(
            storage={0: 0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b, 1: 66, 2: 35, 3: 0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b, 5: 1000},
            code=Op.CALLDATALOAD(offset=0x0) + Op.EXP(0x2, 0xe0) + Op.SWAP1 + Op.DIV + Op.JUMPI(pc=Op.PUSH2[0x42], condition=Op.EQ(0x43d726d6, Op.DUP1)) + Op.JUMPI(pc=Op.PUSH2[0x50], condition=Op.EQ(0x91b7f5ed, Op.DUP1)) + Op.JUMPI(pc=Op.PUSH2[0x61], condition=Op.EQ(0xd686f9ee, Op.DUP1)) + Op.JUMPI(pc=Op.PUSH2[0x6f], condition=Op.EQ(0xf5bade66, Op.DUP1)) + Op.JUMPI(pc=Op.PUSH2[0x80], condition=Op.EQ(0xfcfff16f, Op.DUP1)) + Op.STOP + Op.JUMPDEST + Op.PUSH2[0x4a] + Op.JUMP(pc=0x1de) + Op.JUMPDEST + Op.RETURN(offset=0x0, size=0x0) + Op.JUMPDEST + Op.PUSH2[0x5b] + Op.CALLDATALOAD(offset=0x4) + Op.JUMP(pc=Op.PUSH2[0xbf]) + Op.JUMPDEST + Op.RETURN(offset=0x0, size=0x0) + Op.JUMPDEST + Op.PUSH2[0x69] + Op.JUMP(pc=0x304) + Op.JUMPDEST + Op.RETURN(offset=0x0, size=0x0) + Op.JUMPDEST + Op.PUSH2[0x7a] + Op.CALLDATALOAD(offset=0x4) + Op.JUMP(pc=Op.PUSH2[0x8e]) + Op.JUMPDEST + Op.RETURN(offset=0x0, size=0x0) + Op.JUMPDEST + Op.PUSH2[0x88] + Op.JUMP(pc=Op.PUSH2[0xf0]) + Op.JUMPDEST + Op.RETURN(offset=0x0, size=0x0) + Op.JUMPDEST + Op.JUMPI(pc=Op.PUSH2[0xaf], condition=Op.ISZERO(Op.EQ(Op.AND(Op.SUB(Op.EXP(0x2, 0xa0), 0x1), Op.CALLER), Op.AND(Op.SUB(Op.EXP(0x2, 0xa0), 0x1), Op.SLOAD(key=0x0))))) + Op.JUMP(pc=Op.PUSH2[0xb4]) + Op.JUMPDEST + Op.JUMP(pc=Op.PUSH2[0xbc]) + Op.JUMPDEST + Op.DUP1 + Op.PUSH1[0x1] + Op.DUP2 + Op.SWAP1 + Op.SSTORE + Op.POP + Op.JUMPDEST + Op.POP + Op.JUMP + Op.JUMPDEST + Op.JUMPI(pc=Op.PUSH2[0xe0], condition=Op.ISZERO(Op.EQ(Op.AND(Op.SUB(Op.EXP(0x2, 0xa0), 0x1), Op.CALLER), Op.AND(Op.SUB(Op.EXP(0x2, 0xa0), 0x1), Op.SLOAD(key=0x0))))) + Op.JUMP(pc=Op.PUSH2[0xe5]) + Op.JUMPDEST + Op.JUMP(pc=Op.PUSH2[0xed]) + Op.JUMPDEST + Op.DUP1 + Op.PUSH1[0x2] + Op.DUP2 + Op.SWAP1 + Op.SSTORE + Op.POP + Op.JUMPDEST + Op.POP + Op.JUMP + Op.JUMPDEST + Op.EQ(Op.AND(Op.SUB(Op.EXP(0x2, 0xa0), 0x1), Op.CALLER), Op.AND(Op.SUB(Op.EXP(0x2, 0xa0), 0x1), Op.SLOAD(key=0x0))) + Op.JUMPI(pc=0x125, condition=Op.DUP1) + Op.POP + Op.EQ(Op.AND(Op.SUB(Op.EXP(0x2, 0xa0), 0x1), Op.CALLER), Op.AND(Op.SUB(Op.EXP(0x2, 0xa0), 0x1), Op.SLOAD(key=0x3))) + Op.JUMPDEST + Op.PUSH2[0x12e] + Op.JUMPI + Op.JUMP(pc=0x161) + Op.JUMPDEST + Op.PUSH1[0x1] + Op.PUSH1[0x4] + Op.DUP2 + Op.SWAP1 + Op.SSTORE + Op.POP + Op.LOG1(offset=0x0, size=0x0, topic_1=0x59ebeb90bc63057b6515673c3ecf9438e5058bca0f92585014eced636878c9a5) + Op.JUMP(pc=0x1dc) + Op.JUMPDEST + Op.EQ(0x1, Op.SLOAD(key=0x4)) + Op.JUMPI(pc=0x173, condition=Op.DUP1) + Op.POP + Op.LT(Op.CALLVALUE, Op.SLOAD(key=0x1)) + Op.JUMPDEST + Op.PUSH2[0x1b8] + Op.JUMPI + Op.PUSH1[0x1] + Op.PUSH1[0x4] + Op.DUP2 + Op.SWAP1 + Op.SSTORE + Op.POP + Op.LOG1(offset=0x0, size=0x0, topic_1=0x59ebeb90bc63057b6515673c3ecf9438e5058bca0f92585014eced636878c9a5) + Op.TIMESTAMP + Op.PUSH1[0x5] + Op.DUP2 + Op.SWAP1 + Op.SSTORE + Op.POP + Op.CALLER + Op.PUSH1[0x3] + Op.DUP2 + Op.SWAP1 + Op.SSTORE + Op.POP + Op.JUMP(pc=0x1db) + Op.JUMPDEST + Op.AND(Op.SUB(Op.EXP(0x2, 0xa0), 0x1), Op.CALLER) + Op.PUSH1[0x0] + Op.CALLVALUE + Op.JUMPI(pc=0x1d7, condition=Op.CALL(gas=Op.DUP8, address=Op.DUP8, value=Op.DUP5, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.STOP + Op.JUMPDEST + Op.POP + Op.POP + Op.POP + Op.JUMPDEST + Op.JUMPDEST + Op.JUMP + Op.JUMPDEST + Op.PUSH1[0x0] + Op.JUMPI(pc=0x1ef, condition=Op.EQ(0x0, Op.SLOAD(key=0x4))) + Op.JUMP(pc=0x1f4) + Op.JUMPDEST + Op.JUMP(pc=0x301) + Op.JUMPDEST + Op.EQ(Op.AND(Op.SUB(Op.EXP(0x2, 0xa0), 0x1), Op.CALLER), Op.AND(Op.SUB(Op.EXP(0x2, 0xa0), 0x1), Op.SLOAD(key=0x0))) + Op.JUMPI(pc=0x22c, condition=Op.ISZERO(Op.DUP1)) + Op.POP + Op.EQ(Op.AND(Op.SUB(Op.EXP(0x2, 0xa0), 0x1), Op.SLOAD(key=0x3)), Op.AND(Op.SUB(Op.EXP(0x2, 0xa0), 0x1), Op.SLOAD(key=0x0))) + Op.JUMPDEST + Op.PUSH2[0x235] + Op.JUMPI + Op.JUMP(pc=0x242) + Op.JUMPDEST + Op.PUSH1[0x0] + Op.PUSH1[0x4] + Op.DUP2 + Op.SWAP1 + Op.SSTORE + Op.POP + Op.JUMP(pc=0x301) + Op.JUMPDEST + Op.JUMPI(pc=0x262, condition=Op.EQ(Op.AND(Op.SUB(Op.EXP(0x2, 0xa0), 0x1), Op.CALLER), Op.AND(Op.SUB(Op.EXP(0x2, 0xa0), 0x1), Op.SLOAD(key=0x3)))) + Op.JUMP(pc=0x300) + Op.JUMPDEST + Op.MUL(Op.SLOAD(key=0x2), Op.SUB(Op.TIMESTAMP, Op.SLOAD(key=0x5))) + Op.SWAP1 + Op.POP + Op.JUMPI(pc=0x2c7, condition=Op.GT(Op.DUP2, Op.SLOAD(key=0x1))) + Op.AND(Op.SUB(Op.EXP(0x2, 0xa0), 0x1), Op.SLOAD(key=0x3)) + Op.PUSH1[0x0] + Op.SUB(Op.SLOAD(key=0x1), Op.DUP3) + Op.JUMPI(pc=0x29b, condition=Op.CALL(gas=Op.DUP8, address=Op.DUP8, value=Op.DUP5, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.STOP + Op.JUMPDEST + Op.POP + Op.POP + Op.POP + Op.AND(Op.SUB(Op.EXP(0x2, 0xa0), 0x1), Op.SLOAD(key=0x0)) + Op.PUSH1[0x0] + Op.DUP3 + Op.JUMPI(pc=0x2bf, condition=Op.CALL(gas=Op.DUP8, address=Op.DUP8, value=Op.DUP5, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.STOP + Op.JUMPDEST + Op.POP + Op.POP + Op.POP + Op.JUMP(pc=0x2ee) + Op.JUMPDEST + Op.AND(Op.SUB(Op.EXP(0x2, 0xa0), 0x1), Op.SLOAD(key=0x0)) + Op.PUSH1[0x0] + Op.SLOAD(key=0x1) + Op.JUMPI(pc=0x2ea, condition=Op.CALL(gas=Op.DUP8, address=Op.DUP8, value=Op.DUP5, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.STOP + Op.JUMPDEST + Op.POP + Op.POP + Op.POP + Op.JUMPDEST + Op.PUSH1[0x0] + Op.PUSH1[0x4] + Op.DUP2 + Op.SWAP1 + Op.SSTORE + Op.POP + Op.SLOAD(key=0x0) + Op.PUSH1[0x3] + Op.DUP2 + Op.SWAP1 + Op.SSTORE + Op.POP + Op.JUMPDEST + Op.JUMPDEST + Op.POP + Op.JUMP + Op.JUMPDEST + Op.PUSH1[0x0] + Op.JUMPI(pc=0x327, condition=Op.ISZERO(Op.EQ(Op.AND(Op.SUB(Op.EXP(0x2, 0xa0), 0x1), Op.CALLER), Op.AND(Op.SUB(Op.EXP(0x2, 0xa0), 0x1), Op.SLOAD(key=0x0))))) + Op.JUMP(pc=0x32c) + Op.JUMPDEST + Op.JUMP(pc=0x37e) + Op.JUMPDEST + Op.MUL(Op.SLOAD(key=0x2), Op.SUB(Op.TIMESTAMP, Op.SLOAD(key=0x5))) + Op.SWAP1 + Op.POP + Op.JUMPI(pc=0x345, condition=Op.GT(Op.DUP2, Op.SLOAD(key=0x1))) + Op.JUMP(pc=0x37d) + Op.JUMPDEST + Op.AND(Op.SUB(Op.EXP(0x2, 0xa0), 0x1), Op.SLOAD(key=0x0)) + Op.PUSH1[0x0] + Op.SLOAD(key=0x1) + Op.JUMPI(pc=0x368, condition=Op.CALL(gas=Op.DUP8, address=Op.DUP8, value=Op.DUP5, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.STOP + Op.JUMPDEST + Op.POP + Op.POP + Op.POP + Op.PUSH1[0x0] + Op.PUSH1[0x4] + Op.DUP2 + Op.SWAP1 + Op.SSTORE + Op.POP + Op.SLOAD(key=0x0) + Op.PUSH1[0x3] + Op.DUP2 + Op.SWAP1 + Op.SSTORE + Op.POP + Op.JUMPDEST + Op.JUMPDEST + Op.POP + Op.JUMP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
