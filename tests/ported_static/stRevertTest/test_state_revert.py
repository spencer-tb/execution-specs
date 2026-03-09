"""
Ori Pomerantz qbzzt1@gmail.com

Ported from:
tests/static/state_tests/stRevertTest/stateRevertFiller.yml
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
    ["tests/static/state_tests/stRevertTest/stateRevertFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        ("693c61390000000000000000000000000000000000000000000000000000000000000003", {Address("0x16d83da4c22c26f92c5a8d4cedf367e171f60977"): Account(code=Op.SSTORE(key=0x1, value=0x1001) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.JUMPDEST + Op.JUMPI(pc=0x2b, condition=Op.ISZERO(0x1)) + Op.POP(Op.SHA3(offset=0x0, size=0x1000000)) + Op.JUMP(pc=0x18) + Op.JUMPDEST + Op.STOP), Address("0x1985064d96baaf3305fee248de22965fbf7fbab6"): Account(code=bytes.fromhex("610103600155600060006000600061dead6175305a03f450ba")), Address("0x3559afe49654b532b7e67e6acd87deb8c569e7ad"): Account(storage={0: 24743}, code=Op.SSTORE(key=0x0, value=0x60a7) + Op.DELEGATECALL(gas=Op.GAS, address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)), args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0) + Op.STOP), Address("0x4edc28ff01c9f8731ede6d0fd953da91f749a659"): Account(code=Op.SSTORE(key=0x2, value=0x60a7) + Op.STOP), Address("0x71a06d553f1ac38b5e568ce5a1b5df253ad08d73"): Account(code=Op.SSTORE(key=0x1, value=0x1000) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.REVERT(offset=0x0, size=0x10) + Op.STOP), Address("0xbf0fc73e06f3b2eca8cb8094bdb81d4d2aa2f9b0"): Account(code=Op.SSTORE(key=0x1, value=0x105) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.ADD(Op.ADD, Op.ADD)), Address("0xdd77382f06bfeea4258e6f7bffc6d9d31b885815"): Account(code=Op.SSTORE(key=0x1, value=0x104) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.JUMP(pc=0x0)), Address("0xe08a8de27b3798640d504f1431a360f276b9f2ae"): Account(code=Op.SSTORE(key=0x1, value=0x106) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.JUMPDEST + Op.PC + Op.JUMP(pc=Op.SUB(Op.PC, 0x4))), Address("0xebe3a4514feca3eb2819bf83ebd926c5e4143739"): Account(code=Op.SSTORE(key=0x1, value=0x1002) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SHA3(offset=0x0, size=Op.SUB(0x0, 0x1)) + Op.STOP)}),
        ("693c61390000000000000000000000000000000000000000000000000000000000000004", {Address("0x16d83da4c22c26f92c5a8d4cedf367e171f60977"): Account(code=Op.SSTORE(key=0x1, value=0x1001) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.JUMPDEST + Op.JUMPI(pc=0x2b, condition=Op.ISZERO(0x1)) + Op.POP(Op.SHA3(offset=0x0, size=0x1000000)) + Op.JUMP(pc=0x18) + Op.JUMPDEST + Op.STOP), Address("0x1985064d96baaf3305fee248de22965fbf7fbab6"): Account(code=bytes.fromhex("610103600155600060006000600061dead6175305a03f450ba")), Address("0x3559afe49654b532b7e67e6acd87deb8c569e7ad"): Account(storage={0: 24743}, code=Op.SSTORE(key=0x0, value=0x60a7) + Op.DELEGATECALL(gas=Op.GAS, address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)), args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0) + Op.STOP), Address("0x4edc28ff01c9f8731ede6d0fd953da91f749a659"): Account(code=Op.SSTORE(key=0x2, value=0x60a7) + Op.STOP), Address("0x71a06d553f1ac38b5e568ce5a1b5df253ad08d73"): Account(code=Op.SSTORE(key=0x1, value=0x1000) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.REVERT(offset=0x0, size=0x10) + Op.STOP), Address("0xbf0fc73e06f3b2eca8cb8094bdb81d4d2aa2f9b0"): Account(code=Op.SSTORE(key=0x1, value=0x105) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.ADD(Op.ADD, Op.ADD)), Address("0xdd77382f06bfeea4258e6f7bffc6d9d31b885815"): Account(code=Op.SSTORE(key=0x1, value=0x104) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.JUMP(pc=0x0)), Address("0xe08a8de27b3798640d504f1431a360f276b9f2ae"): Account(code=Op.SSTORE(key=0x1, value=0x106) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.JUMPDEST + Op.PC + Op.JUMP(pc=Op.SUB(Op.PC, 0x4))), Address("0xebe3a4514feca3eb2819bf83ebd926c5e4143739"): Account(code=Op.SSTORE(key=0x1, value=0x1002) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SHA3(offset=0x0, size=Op.SUB(0x0, 0x1)) + Op.STOP)}),
        ("693c61390000000000000000000000000000000000000000000000000000000000000001", {Address("0x16d83da4c22c26f92c5a8d4cedf367e171f60977"): Account(code=Op.SSTORE(key=0x1, value=0x1001) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.JUMPDEST + Op.JUMPI(pc=0x2b, condition=Op.ISZERO(0x1)) + Op.POP(Op.SHA3(offset=0x0, size=0x1000000)) + Op.JUMP(pc=0x18) + Op.JUMPDEST + Op.STOP), Address("0x1985064d96baaf3305fee248de22965fbf7fbab6"): Account(code=bytes.fromhex("610103600155600060006000600061dead6175305a03f450ba")), Address("0x3559afe49654b532b7e67e6acd87deb8c569e7ad"): Account(storage={0: 24743}, code=Op.SSTORE(key=0x0, value=0x60a7) + Op.DELEGATECALL(gas=Op.GAS, address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)), args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0) + Op.STOP), Address("0x4edc28ff01c9f8731ede6d0fd953da91f749a659"): Account(code=Op.SSTORE(key=0x2, value=0x60a7) + Op.STOP), Address("0x71a06d553f1ac38b5e568ce5a1b5df253ad08d73"): Account(code=Op.SSTORE(key=0x1, value=0x1000) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.REVERT(offset=0x0, size=0x10) + Op.STOP), Address("0xbf0fc73e06f3b2eca8cb8094bdb81d4d2aa2f9b0"): Account(code=Op.SSTORE(key=0x1, value=0x105) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.ADD(Op.ADD, Op.ADD)), Address("0xdd77382f06bfeea4258e6f7bffc6d9d31b885815"): Account(code=Op.SSTORE(key=0x1, value=0x104) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.JUMP(pc=0x0)), Address("0xe08a8de27b3798640d504f1431a360f276b9f2ae"): Account(code=Op.SSTORE(key=0x1, value=0x106) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.JUMPDEST + Op.PC + Op.JUMP(pc=Op.SUB(Op.PC, 0x4))), Address("0xebe3a4514feca3eb2819bf83ebd926c5e4143739"): Account(code=Op.SSTORE(key=0x1, value=0x1002) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SHA3(offset=0x0, size=Op.SUB(0x0, 0x1)) + Op.STOP)}),
        ("693c61390000000000000000000000000000000000000000000000000000000000000000", {Address("0x16d83da4c22c26f92c5a8d4cedf367e171f60977"): Account(code=Op.SSTORE(key=0x1, value=0x1001) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.JUMPDEST + Op.JUMPI(pc=0x2b, condition=Op.ISZERO(0x1)) + Op.POP(Op.SHA3(offset=0x0, size=0x1000000)) + Op.JUMP(pc=0x18) + Op.JUMPDEST + Op.STOP), Address("0x1985064d96baaf3305fee248de22965fbf7fbab6"): Account(code=bytes.fromhex("610103600155600060006000600061dead6175305a03f450ba")), Address("0x3559afe49654b532b7e67e6acd87deb8c569e7ad"): Account(storage={0: 24743}, code=Op.SSTORE(key=0x0, value=0x60a7) + Op.DELEGATECALL(gas=Op.GAS, address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)), args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0) + Op.STOP), Address("0x4edc28ff01c9f8731ede6d0fd953da91f749a659"): Account(code=Op.SSTORE(key=0x2, value=0x60a7) + Op.STOP), Address("0x71a06d553f1ac38b5e568ce5a1b5df253ad08d73"): Account(code=Op.SSTORE(key=0x1, value=0x1000) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.REVERT(offset=0x0, size=0x10) + Op.STOP), Address("0xbf0fc73e06f3b2eca8cb8094bdb81d4d2aa2f9b0"): Account(code=Op.SSTORE(key=0x1, value=0x105) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.ADD(Op.ADD, Op.ADD)), Address("0xdd77382f06bfeea4258e6f7bffc6d9d31b885815"): Account(code=Op.SSTORE(key=0x1, value=0x104) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.JUMP(pc=0x0)), Address("0xe08a8de27b3798640d504f1431a360f276b9f2ae"): Account(code=Op.SSTORE(key=0x1, value=0x106) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.JUMPDEST + Op.PC + Op.JUMP(pc=Op.SUB(Op.PC, 0x4))), Address("0xebe3a4514feca3eb2819bf83ebd926c5e4143739"): Account(code=Op.SSTORE(key=0x1, value=0x1002) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SHA3(offset=0x0, size=Op.SUB(0x0, 0x1)) + Op.STOP)}),
        ("693c61390000000000000000000000000000000000000000000000000000000000000006", {Address("0x16d83da4c22c26f92c5a8d4cedf367e171f60977"): Account(code=Op.SSTORE(key=0x1, value=0x1001) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.JUMPDEST + Op.JUMPI(pc=0x2b, condition=Op.ISZERO(0x1)) + Op.POP(Op.SHA3(offset=0x0, size=0x1000000)) + Op.JUMP(pc=0x18) + Op.JUMPDEST + Op.STOP), Address("0x1985064d96baaf3305fee248de22965fbf7fbab6"): Account(code=bytes.fromhex("610103600155600060006000600061dead6175305a03f450ba")), Address("0x3559afe49654b532b7e67e6acd87deb8c569e7ad"): Account(storage={0: 24743}, code=Op.SSTORE(key=0x0, value=0x60a7) + Op.DELEGATECALL(gas=Op.GAS, address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)), args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0) + Op.STOP), Address("0x4edc28ff01c9f8731ede6d0fd953da91f749a659"): Account(code=Op.SSTORE(key=0x2, value=0x60a7) + Op.STOP), Address("0x71a06d553f1ac38b5e568ce5a1b5df253ad08d73"): Account(code=Op.SSTORE(key=0x1, value=0x1000) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.REVERT(offset=0x0, size=0x10) + Op.STOP), Address("0xbf0fc73e06f3b2eca8cb8094bdb81d4d2aa2f9b0"): Account(code=Op.SSTORE(key=0x1, value=0x105) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.ADD(Op.ADD, Op.ADD)), Address("0xdd77382f06bfeea4258e6f7bffc6d9d31b885815"): Account(code=Op.SSTORE(key=0x1, value=0x104) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.JUMP(pc=0x0)), Address("0xe08a8de27b3798640d504f1431a360f276b9f2ae"): Account(code=Op.SSTORE(key=0x1, value=0x106) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.JUMPDEST + Op.PC + Op.JUMP(pc=Op.SUB(Op.PC, 0x4))), Address("0xebe3a4514feca3eb2819bf83ebd926c5e4143739"): Account(code=Op.SSTORE(key=0x1, value=0x1002) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SHA3(offset=0x0, size=Op.SUB(0x0, 0x1)) + Op.STOP)}),
        ("693c61390000000000000000000000000000000000000000000000000000000000000005", {Address("0x16d83da4c22c26f92c5a8d4cedf367e171f60977"): Account(code=Op.SSTORE(key=0x1, value=0x1001) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.JUMPDEST + Op.JUMPI(pc=0x2b, condition=Op.ISZERO(0x1)) + Op.POP(Op.SHA3(offset=0x0, size=0x1000000)) + Op.JUMP(pc=0x18) + Op.JUMPDEST + Op.STOP), Address("0x1985064d96baaf3305fee248de22965fbf7fbab6"): Account(code=bytes.fromhex("610103600155600060006000600061dead6175305a03f450ba")), Address("0x3559afe49654b532b7e67e6acd87deb8c569e7ad"): Account(storage={0: 24743}, code=Op.SSTORE(key=0x0, value=0x60a7) + Op.DELEGATECALL(gas=Op.GAS, address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)), args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0) + Op.STOP), Address("0x4edc28ff01c9f8731ede6d0fd953da91f749a659"): Account(code=Op.SSTORE(key=0x2, value=0x60a7) + Op.STOP), Address("0x71a06d553f1ac38b5e568ce5a1b5df253ad08d73"): Account(code=Op.SSTORE(key=0x1, value=0x1000) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.REVERT(offset=0x0, size=0x10) + Op.STOP), Address("0xbf0fc73e06f3b2eca8cb8094bdb81d4d2aa2f9b0"): Account(code=Op.SSTORE(key=0x1, value=0x105) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.ADD(Op.ADD, Op.ADD)), Address("0xdd77382f06bfeea4258e6f7bffc6d9d31b885815"): Account(code=Op.SSTORE(key=0x1, value=0x104) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.JUMP(pc=0x0)), Address("0xe08a8de27b3798640d504f1431a360f276b9f2ae"): Account(code=Op.SSTORE(key=0x1, value=0x106) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.JUMPDEST + Op.PC + Op.JUMP(pc=Op.SUB(Op.PC, 0x4))), Address("0xebe3a4514feca3eb2819bf83ebd926c5e4143739"): Account(code=Op.SSTORE(key=0x1, value=0x1002) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SHA3(offset=0x0, size=Op.SUB(0x0, 0x1)) + Op.STOP)}),
        ("693c61390000000000000000000000000000000000000000000000000000000000000002", {Address("0x16d83da4c22c26f92c5a8d4cedf367e171f60977"): Account(code=Op.SSTORE(key=0x1, value=0x1001) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.JUMPDEST + Op.JUMPI(pc=0x2b, condition=Op.ISZERO(0x1)) + Op.POP(Op.SHA3(offset=0x0, size=0x1000000)) + Op.JUMP(pc=0x18) + Op.JUMPDEST + Op.STOP), Address("0x1985064d96baaf3305fee248de22965fbf7fbab6"): Account(code=bytes.fromhex("610103600155600060006000600061dead6175305a03f450ba")), Address("0x3559afe49654b532b7e67e6acd87deb8c569e7ad"): Account(storage={0: 24743}, code=Op.SSTORE(key=0x0, value=0x60a7) + Op.DELEGATECALL(gas=Op.GAS, address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)), args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0) + Op.STOP), Address("0x4edc28ff01c9f8731ede6d0fd953da91f749a659"): Account(code=Op.SSTORE(key=0x2, value=0x60a7) + Op.STOP), Address("0x71a06d553f1ac38b5e568ce5a1b5df253ad08d73"): Account(code=Op.SSTORE(key=0x1, value=0x1000) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.REVERT(offset=0x0, size=0x10) + Op.STOP), Address("0xbf0fc73e06f3b2eca8cb8094bdb81d4d2aa2f9b0"): Account(code=Op.SSTORE(key=0x1, value=0x105) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.ADD(Op.ADD, Op.ADD)), Address("0xdd77382f06bfeea4258e6f7bffc6d9d31b885815"): Account(code=Op.SSTORE(key=0x1, value=0x104) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.JUMP(pc=0x0)), Address("0xe08a8de27b3798640d504f1431a360f276b9f2ae"): Account(code=Op.SSTORE(key=0x1, value=0x106) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.JUMPDEST + Op.PC + Op.JUMP(pc=Op.SUB(Op.PC, 0x4))), Address("0xebe3a4514feca3eb2819bf83ebd926c5e4143739"): Account(code=Op.SSTORE(key=0x1, value=0x1002) + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SHA3(offset=0x0, size=Op.SUB(0x0, 0x1)) + Op.STOP)}),
    ],
    ids=['case0', 'case1', 'case2', 'case3', 'case4', 'case5', 'case6'],
)
@pytest.mark.pre_alloc_mutable
def test_state_revert(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Ori Pomerantz qbzzt1@gmail.com."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x64a703f9294edbbf778201f3c2a87c7f91be5a8c")
    contract = Address("0x3559afe49654b532b7e67e6acd87deb8c569e7ad")
    callee = Address("0x16d83da4c22c26f92c5a8d4cedf367e171f60977")
    callee_1 = Address("0x1985064d96baaf3305fee248de22965fbf7fbab6")
    callee_2 = Address("0x4edc28ff01c9f8731ede6d0fd953da91f749a659")
    callee_3 = Address("0x71a06d553f1ac38b5e568ce5a1b5df253ad08d73")
    callee_4 = Address("0xbf0fc73e06f3b2eca8cb8094bdb81d4d2aa2f9b0")
    callee_5 = Address("0xdd77382f06bfeea4258e6f7bffc6d9d31b885815")
    callee_6 = Address("0xe08a8de27b3798640d504f1431a360f276b9f2ae")
    callee_7 = Address("0xebe3a4514feca3eb2819bf83ebd926c5e4143739")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000,
    )

    pre[callee] = Account(
        balance=0xba1a9ce0ba1a9ce,
        nonce=0,
        code=(
        Op.SSTORE(key=0x1, value=0x1001)
        + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.JUMPDEST + Op.JUMPI(pc=0x2b, condition=Op.ISZERO(0x1))
        + Op.POP(Op.SHA3(offset=0x0, size=0x1000000)) + Op.JUMP(pc=0x18) + Op.JUMPDEST
        + Op.STOP
    ),
    )
    pre[callee_1] = Account(
        balance=0xba1a9ce0ba1a9ce,
        nonce=0,
        code=bytes.fromhex("610103600155600060006000600061dead6175305a03f450ba"),
    )
    pre[contract] = Account(
        balance=0xba1a9ce0ba1a9ce,
        nonce=0,
        code=(
        Op.SSTORE(key=0x0, value=0x60a7)
        + Op.DELEGATECALL(gas=Op.GAS, address=Op.ADD(0x1000, Op.CALLDATALOAD(offset=0x4)), args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)
        + Op.STOP
    ),
    )
    pre[callee_2] = Account(
        balance=0xba1a9ce0ba1a9ce,
        nonce=0,
        code=Op.SSTORE(key=0x2, value=0x60a7) + Op.STOP,
    )
    pre[sender] = Account(balance=0x100000000000, nonce=0)
    pre[callee_3] = Account(
        balance=0xba1a9ce0ba1a9ce,
        nonce=0,
        code=(
        Op.SSTORE(key=0x1, value=0x1000)
        + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.REVERT(offset=0x0, size=0x10) + Op.STOP
    ),
    )
    pre[callee_4] = Account(
        balance=0xba1a9ce0ba1a9ce,
        nonce=0,
        code=(
        Op.SSTORE(key=0x1, value=0x105)
        + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.ADD(Op.ADD, Op.ADD)
    ),
    )
    pre[callee_5] = Account(
        balance=0xba1a9ce0ba1a9ce,
        nonce=0,
        code=(
        Op.SSTORE(key=0x1, value=0x104)
        + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.JUMP(pc=0x0)
    ),
    )
    pre[callee_6] = Account(
        balance=0xba1a9ce0ba1a9ce,
        nonce=0,
        code=(
        Op.SSTORE(key=0x1, value=0x106)
        + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.JUMPDEST + Op.PC + Op.JUMP(pc=Op.SUB(Op.PC, 0x4))
    ),
    )
    pre[callee_7] = Account(
        balance=0xba1a9ce0ba1a9ce,
        nonce=0,
        code=(
        Op.SSTORE(key=0x1, value=0x1002)
        + Op.POP(Op.DELEGATECALL(gas=Op.SUB(Op.GAS, 0x7530), address=0xdead, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.SHA3(offset=0x0, size=Op.SUB(0x0, 0x1)) + Op.STOP
    ),
    )

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0xa62d63f95900b04ccd3fee13360de78966f24695945e8b2c09e646352bc5af94"
        ),
        to=contract,
        data=tx_data,
        gas_limit=16777216,
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
