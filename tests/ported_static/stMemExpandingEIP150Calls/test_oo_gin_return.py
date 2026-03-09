"""
Ori Pomerantz qbzzt1@gmail.com

Ported from:
tests/static/state_tests/stMemExpandingEIP150Calls/OOGinReturnFiller.yml
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
    ["tests/static/state_tests/stMemExpandingEIP150Calls/OOGinReturnFiller.yml"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        ("1a8451e60000000000000000000000009f5c4c430e37b429d18f8aba147e2302af08f2100000000000000000000000000000000000000000000000000000000000000036", {Address("0x9f5c4c430e37b429d18f8aba147e2302af08f210"): Account(code=Op.MSTORE(offset=0x0, value=0xdead60a7) + Op.RETURN(offset=0x0, size=0x100) + Op.STOP), Address("0xcee9f0c6117cc881ad7b4c378c2bebee8fcd04a9"): Account(code=Op.MSTORE(offset=0x0, value=0xdead60a7) + Op.REVERT(offset=0x0, size=0x100) + Op.STOP), Address("0xebd3191dd8150f47e30f87927db4592163ee9224"): Account(storage={0: 0xdead60a7, 1: 0xdead60a7}, code=Op.MSTORE(offset=0x120, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x140, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x0, value=0x60a760a7) + Op.MSTORE(offset=0x100, value=Op.CALL(gas=Op.MLOAD(offset=0x140), address=Op.MLOAD(offset=0x120), value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x100)) + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0)) + Op.JUMPI(pc=0x41, condition=Op.GT(Op.RETURNDATASIZE, 0x0)) + Op.POP(0x0) + Op.JUMP(pc=0x4a) + Op.JUMPDEST + Op.RETURNDATACOPY(dest_offset=0x160, offset=0x0, size=0x20) + Op.JUMPDEST + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x160)) + Op.STOP)}),
        ("1a8451e6000000000000000000000000cee9f0c6117cc881ad7b4c378c2bebee8fcd04a90000000000000000000000000000000000000000000000000000000000000036", {Address("0x9f5c4c430e37b429d18f8aba147e2302af08f210"): Account(code=Op.MSTORE(offset=0x0, value=0xdead60a7) + Op.RETURN(offset=0x0, size=0x100) + Op.STOP), Address("0xcee9f0c6117cc881ad7b4c378c2bebee8fcd04a9"): Account(code=Op.MSTORE(offset=0x0, value=0xdead60a7) + Op.REVERT(offset=0x0, size=0x100) + Op.STOP), Address("0xebd3191dd8150f47e30f87927db4592163ee9224"): Account(storage={0: 0xdead60a7, 1: 0xdead60a7}, code=Op.MSTORE(offset=0x120, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x140, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x0, value=0x60a760a7) + Op.MSTORE(offset=0x100, value=Op.CALL(gas=Op.MLOAD(offset=0x140), address=Op.MLOAD(offset=0x120), value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x100)) + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0)) + Op.JUMPI(pc=0x41, condition=Op.GT(Op.RETURNDATASIZE, 0x0)) + Op.POP(0x0) + Op.JUMP(pc=0x4a) + Op.JUMPDEST + Op.RETURNDATACOPY(dest_offset=0x160, offset=0x0, size=0x20) + Op.JUMPDEST + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x160)) + Op.STOP)}),
        ("1a8451e60000000000000000000000009f5c4c430e37b429d18f8aba147e2302af08f2100000000000000000000000000000000000000000000000000000000000000025", {Address("0x9f5c4c430e37b429d18f8aba147e2302af08f210"): Account(code=Op.MSTORE(offset=0x0, value=0xdead60a7) + Op.RETURN(offset=0x0, size=0x100) + Op.STOP), Address("0xcee9f0c6117cc881ad7b4c378c2bebee8fcd04a9"): Account(code=Op.MSTORE(offset=0x0, value=0xdead60a7) + Op.REVERT(offset=0x0, size=0x100) + Op.STOP), Address("0xebd3191dd8150f47e30f87927db4592163ee9224"): Account(storage={0: 0x60a760a7}, code=Op.MSTORE(offset=0x120, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x140, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x0, value=0x60a760a7) + Op.MSTORE(offset=0x100, value=Op.CALL(gas=Op.MLOAD(offset=0x140), address=Op.MLOAD(offset=0x120), value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x100)) + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0)) + Op.JUMPI(pc=0x41, condition=Op.GT(Op.RETURNDATASIZE, 0x0)) + Op.POP(0x0) + Op.JUMP(pc=0x4a) + Op.JUMPDEST + Op.RETURNDATACOPY(dest_offset=0x160, offset=0x0, size=0x20) + Op.JUMPDEST + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x160)) + Op.STOP)}),
        ("1a8451e6000000000000000000000000cee9f0c6117cc881ad7b4c378c2bebee8fcd04a90000000000000000000000000000000000000000000000000000000000000025", {Address("0x9f5c4c430e37b429d18f8aba147e2302af08f210"): Account(code=Op.MSTORE(offset=0x0, value=0xdead60a7) + Op.RETURN(offset=0x0, size=0x100) + Op.STOP), Address("0xcee9f0c6117cc881ad7b4c378c2bebee8fcd04a9"): Account(code=Op.MSTORE(offset=0x0, value=0xdead60a7) + Op.REVERT(offset=0x0, size=0x100) + Op.STOP), Address("0xebd3191dd8150f47e30f87927db4592163ee9224"): Account(storage={0: 0x60a760a7}, code=Op.MSTORE(offset=0x120, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x140, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x0, value=0x60a760a7) + Op.MSTORE(offset=0x100, value=Op.CALL(gas=Op.MLOAD(offset=0x140), address=Op.MLOAD(offset=0x120), value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x100)) + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0)) + Op.JUMPI(pc=0x41, condition=Op.GT(Op.RETURNDATASIZE, 0x0)) + Op.POP(0x0) + Op.JUMP(pc=0x4a) + Op.JUMPDEST + Op.RETURNDATACOPY(dest_offset=0x160, offset=0x0, size=0x20) + Op.JUMPDEST + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x160)) + Op.STOP)}),
        ("1a8451e60000000000000000000000009f5c4c430e37b429d18f8aba147e2302af08f2100000000000000000000000000000000000000000000000000000000000000010", {Address("0x9f5c4c430e37b429d18f8aba147e2302af08f210"): Account(code=Op.MSTORE(offset=0x0, value=0xdead60a7) + Op.RETURN(offset=0x0, size=0x100) + Op.STOP), Address("0xcee9f0c6117cc881ad7b4c378c2bebee8fcd04a9"): Account(code=Op.MSTORE(offset=0x0, value=0xdead60a7) + Op.REVERT(offset=0x0, size=0x100) + Op.STOP), Address("0xebd3191dd8150f47e30f87927db4592163ee9224"): Account(storage={0: 0x60a760a7}, code=Op.MSTORE(offset=0x120, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x140, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x0, value=0x60a760a7) + Op.MSTORE(offset=0x100, value=Op.CALL(gas=Op.MLOAD(offset=0x140), address=Op.MLOAD(offset=0x120), value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x100)) + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0)) + Op.JUMPI(pc=0x41, condition=Op.GT(Op.RETURNDATASIZE, 0x0)) + Op.POP(0x0) + Op.JUMP(pc=0x4a) + Op.JUMPDEST + Op.RETURNDATACOPY(dest_offset=0x160, offset=0x0, size=0x20) + Op.JUMPDEST + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x160)) + Op.STOP)}),
        ("1a8451e6000000000000000000000000cee9f0c6117cc881ad7b4c378c2bebee8fcd04a90000000000000000000000000000000000000000000000000000000000000010", {Address("0x9f5c4c430e37b429d18f8aba147e2302af08f210"): Account(code=Op.MSTORE(offset=0x0, value=0xdead60a7) + Op.RETURN(offset=0x0, size=0x100) + Op.STOP), Address("0xcee9f0c6117cc881ad7b4c378c2bebee8fcd04a9"): Account(code=Op.MSTORE(offset=0x0, value=0xdead60a7) + Op.REVERT(offset=0x0, size=0x100) + Op.STOP), Address("0xebd3191dd8150f47e30f87927db4592163ee9224"): Account(storage={0: 0x60a760a7}, code=Op.MSTORE(offset=0x120, value=Op.CALLDATALOAD(offset=0x4)) + Op.MSTORE(offset=0x140, value=Op.CALLDATALOAD(offset=0x24)) + Op.MSTORE(offset=0x0, value=0x60a760a7) + Op.MSTORE(offset=0x100, value=Op.CALL(gas=Op.MLOAD(offset=0x140), address=Op.MLOAD(offset=0x120), value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x100)) + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0)) + Op.JUMPI(pc=0x41, condition=Op.GT(Op.RETURNDATASIZE, 0x0)) + Op.POP(0x0) + Op.JUMP(pc=0x4a) + Op.JUMPDEST + Op.RETURNDATACOPY(dest_offset=0x160, offset=0x0, size=0x20) + Op.JUMPDEST + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x160)) + Op.STOP)}),
    ],
    ids=['case0', 'case1', 'case2', 'case3', 'case4', 'case5'],
)
@pytest.mark.pre_alloc_mutable
def test_oo_gin_return(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Ori Pomerantz qbzzt1@gmail.com."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x56724d001b4f2a2888a81971a64aad37cd43f881")
    contract = Address("0xebd3191dd8150f47e30f87927db4592163ee9224")
    callee = Address("0x9f5c4c430e37b429d18f8aba147e2302af08f210")
    callee_1 = Address("0xcee9f0c6117cc881ad7b4c378c2bebee8fcd04a9")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=4294967296,
    )

    pre[sender] = Account(balance=0xba1a9ce0ba1a9ce, nonce=0)
    pre[callee] = Account(
        balance=0xba1a9ce0ba1a9ce,
        nonce=0,
        code=(
        Op.MSTORE(offset=0x0, value=0xdead60a7) + Op.RETURN(offset=0x0, size=0x100)
        + Op.STOP
    ),
    )
    pre[callee_1] = Account(
        balance=0xba1a9ce0ba1a9ce,
        nonce=0,
        code=(
        Op.MSTORE(offset=0x0, value=0xdead60a7) + Op.REVERT(offset=0x0, size=0x100)
        + Op.STOP
    ),
    )
    pre[contract] = Account(
        balance=0xba1a9ce0ba1a9ce,
        nonce=0,
        code=(
        Op.MSTORE(offset=0x120, value=Op.CALLDATALOAD(offset=0x4))
        + Op.MSTORE(offset=0x140, value=Op.CALLDATALOAD(offset=0x24))
        + Op.MSTORE(offset=0x0, value=0x60a760a7)
        + Op.MSTORE(offset=0x100, value=Op.CALL(gas=Op.MLOAD(offset=0x140), address=Op.MLOAD(offset=0x120), value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x100))
        + Op.SSTORE(key=0x0, value=Op.MLOAD(offset=0x0))
        + Op.JUMPI(pc=0x41, condition=Op.GT(Op.RETURNDATASIZE, 0x0)) + Op.POP(0x0)
        + Op.JUMP(pc=0x4a) + Op.JUMPDEST
        + Op.RETURNDATACOPY(dest_offset=0x160, offset=0x0, size=0x20) + Op.JUMPDEST
        + Op.SSTORE(key=0x1, value=Op.MLOAD(offset=0x160)) + Op.STOP
    ),
    )

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x40ac0fc28c27e961ee46ec43355a094de205856edbd4654cf2577c2608d4ec1e"
        ),
        to=contract,
        data=tx_data,
        gas_limit=9437184,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
