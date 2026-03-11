"""
Test ported from static filler.

Ported from:
tests/static/state_tests/Shanghai/stEIP3651_warmcoinbase
coinbaseWarmAccountCallGasFailFiller.yml
"""

import pytest
from execution_testing import (
    Account,
    Address,
    Alloc,
    EOA,
    Environment,
    Hash,
    StateTestFiller,
    Transaction,
)
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


@pytest.mark.ported_from(
    [
        "tests/static/state_tests/Shanghai/stEIP3651_warmcoinbase/coinbaseWarmAccountCallGasFailFiller.yml",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        (
            "693c61390000000000000000000000008ddf5d9a5251c41efd2949f53db0a464116c7c6e",  # noqa: E501
            {
                Address("0x0a92fc97bb4c47b3d5e9e96fbb1c3fc2f07dba81"): Account(
                    storage={0: 1},
                    code=Op.PUSH1[0x0]
                    + Op.DUP1
                    + Op.DUP1
                    + Op.DUP1
                    + Op.DUP1
                    + Op.CALLDATALOAD(offset=0x4)
                    + Op.PUSH1[0x64]
                    + Op.DUP2
                    + Op.JUMPI(
                        pc=0x88,
                        condition=Op.EQ(
                            0x8DDF5D9A5251C41EFD2949F53DB0A464116C7C6E, Op.DUP1
                        ),
                    )
                    + Op.JUMPI(
                        pc=0x88,
                        condition=Op.EQ(
                            0x498516B6B2F25CB6A8E011A7C37A617B77E7D500, Op.DUP1
                        ),
                    )
                    + Op.JUMPI(
                        pc=0x80,
                        condition=Op.EQ(
                            0x8873820BB96DAA39DB93AE64A9D6397E4C6A48D7, Op.DUP1
                        ),
                    )
                    + Op.PUSH20[0x303B6790D019874A107418EB549E4E7766A64728]
                    + Op.JUMPI(pc=0x79, condition=Op.EQ)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=Op.CALL)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.PUSH1[0x18]
                    + Op.ADD
                    + Op.JUMP(pc=0x73)
                    + Op.JUMPDEST
                    + Op.POP
                    + Op.PUSH1[0x18]
                    + Op.ADD
                    + Op.JUMP(pc=0x73)
                    + Op.JUMPDEST
                    + Op.POP
                    + Op.PUSH1[0x1B]
                    + Op.ADD
                    + Op.JUMP(pc=0x73),
                ),
                Address("0x303b6790d019874a107418eb549e4e7766a64728"): Account(
                    code=Op.STATICCALL(
                        gas=Op.DUP2,
                        address=Op.COINBASE,
                        args_offset=Op.DUP1,
                        args_size=Op.DUP1,
                        ret_offset=Op.DUP1,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x498516b6b2f25cb6a8e011a7c37a617b77e7d500"): Account(
                    code=Op.CALLCODE(
                        gas=Op.DUP2,
                        address=Op.COINBASE,
                        value=Op.DUP1,
                        args_offset=Op.DUP1,
                        args_size=Op.DUP1,
                        ret_offset=Op.DUP1,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x8873820bb96daa39db93ae64a9d6397e4c6a48d7"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.DUP2,
                        address=Op.COINBASE,
                        args_offset=Op.DUP1,
                        args_size=Op.DUP1,
                        ret_offset=Op.DUP1,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x8ddf5d9a5251c41efd2949f53db0a464116c7c6e"): Account(
                    code=Op.CALL(
                        gas=Op.DUP2,
                        address=Op.COINBASE,
                        value=Op.DUP1,
                        args_offset=Op.DUP1,
                        args_size=Op.DUP1,
                        ret_offset=Op.DUP1,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
            },
        ),
        (
            "693c6139000000000000000000000000498516b6b2f25cb6a8e011a7c37a617b77e7d500",  # noqa: E501
            {
                Address("0x0a92fc97bb4c47b3d5e9e96fbb1c3fc2f07dba81"): Account(
                    storage={0: 1},
                    code=Op.PUSH1[0x0]
                    + Op.DUP1
                    + Op.DUP1
                    + Op.DUP1
                    + Op.DUP1
                    + Op.CALLDATALOAD(offset=0x4)
                    + Op.PUSH1[0x64]
                    + Op.DUP2
                    + Op.JUMPI(
                        pc=0x88,
                        condition=Op.EQ(
                            0x8DDF5D9A5251C41EFD2949F53DB0A464116C7C6E, Op.DUP1
                        ),
                    )
                    + Op.JUMPI(
                        pc=0x88,
                        condition=Op.EQ(
                            0x498516B6B2F25CB6A8E011A7C37A617B77E7D500, Op.DUP1
                        ),
                    )
                    + Op.JUMPI(
                        pc=0x80,
                        condition=Op.EQ(
                            0x8873820BB96DAA39DB93AE64A9D6397E4C6A48D7, Op.DUP1
                        ),
                    )
                    + Op.PUSH20[0x303B6790D019874A107418EB549E4E7766A64728]
                    + Op.JUMPI(pc=0x79, condition=Op.EQ)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=Op.CALL)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.PUSH1[0x18]
                    + Op.ADD
                    + Op.JUMP(pc=0x73)
                    + Op.JUMPDEST
                    + Op.POP
                    + Op.PUSH1[0x18]
                    + Op.ADD
                    + Op.JUMP(pc=0x73)
                    + Op.JUMPDEST
                    + Op.POP
                    + Op.PUSH1[0x1B]
                    + Op.ADD
                    + Op.JUMP(pc=0x73),
                ),
                Address("0x303b6790d019874a107418eb549e4e7766a64728"): Account(
                    code=Op.STATICCALL(
                        gas=Op.DUP2,
                        address=Op.COINBASE,
                        args_offset=Op.DUP1,
                        args_size=Op.DUP1,
                        ret_offset=Op.DUP1,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x498516b6b2f25cb6a8e011a7c37a617b77e7d500"): Account(
                    code=Op.CALLCODE(
                        gas=Op.DUP2,
                        address=Op.COINBASE,
                        value=Op.DUP1,
                        args_offset=Op.DUP1,
                        args_size=Op.DUP1,
                        ret_offset=Op.DUP1,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x8873820bb96daa39db93ae64a9d6397e4c6a48d7"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.DUP2,
                        address=Op.COINBASE,
                        args_offset=Op.DUP1,
                        args_size=Op.DUP1,
                        ret_offset=Op.DUP1,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x8ddf5d9a5251c41efd2949f53db0a464116c7c6e"): Account(
                    code=Op.CALL(
                        gas=Op.DUP2,
                        address=Op.COINBASE,
                        value=Op.DUP1,
                        args_offset=Op.DUP1,
                        args_size=Op.DUP1,
                        ret_offset=Op.DUP1,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
            },
        ),
        (
            "693c61390000000000000000000000008873820bb96daa39db93ae64a9d6397e4c6a48d7",  # noqa: E501
            {
                Address("0x0a92fc97bb4c47b3d5e9e96fbb1c3fc2f07dba81"): Account(
                    storage={0: 1},
                    code=Op.PUSH1[0x0]
                    + Op.DUP1
                    + Op.DUP1
                    + Op.DUP1
                    + Op.DUP1
                    + Op.CALLDATALOAD(offset=0x4)
                    + Op.PUSH1[0x64]
                    + Op.DUP2
                    + Op.JUMPI(
                        pc=0x88,
                        condition=Op.EQ(
                            0x8DDF5D9A5251C41EFD2949F53DB0A464116C7C6E, Op.DUP1
                        ),
                    )
                    + Op.JUMPI(
                        pc=0x88,
                        condition=Op.EQ(
                            0x498516B6B2F25CB6A8E011A7C37A617B77E7D500, Op.DUP1
                        ),
                    )
                    + Op.JUMPI(
                        pc=0x80,
                        condition=Op.EQ(
                            0x8873820BB96DAA39DB93AE64A9D6397E4C6A48D7, Op.DUP1
                        ),
                    )
                    + Op.PUSH20[0x303B6790D019874A107418EB549E4E7766A64728]
                    + Op.JUMPI(pc=0x79, condition=Op.EQ)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=Op.CALL)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.PUSH1[0x18]
                    + Op.ADD
                    + Op.JUMP(pc=0x73)
                    + Op.JUMPDEST
                    + Op.POP
                    + Op.PUSH1[0x18]
                    + Op.ADD
                    + Op.JUMP(pc=0x73)
                    + Op.JUMPDEST
                    + Op.POP
                    + Op.PUSH1[0x1B]
                    + Op.ADD
                    + Op.JUMP(pc=0x73),
                ),
                Address("0x303b6790d019874a107418eb549e4e7766a64728"): Account(
                    code=Op.STATICCALL(
                        gas=Op.DUP2,
                        address=Op.COINBASE,
                        args_offset=Op.DUP1,
                        args_size=Op.DUP1,
                        ret_offset=Op.DUP1,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x498516b6b2f25cb6a8e011a7c37a617b77e7d500"): Account(
                    code=Op.CALLCODE(
                        gas=Op.DUP2,
                        address=Op.COINBASE,
                        value=Op.DUP1,
                        args_offset=Op.DUP1,
                        args_size=Op.DUP1,
                        ret_offset=Op.DUP1,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x8873820bb96daa39db93ae64a9d6397e4c6a48d7"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.DUP2,
                        address=Op.COINBASE,
                        args_offset=Op.DUP1,
                        args_size=Op.DUP1,
                        ret_offset=Op.DUP1,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x8ddf5d9a5251c41efd2949f53db0a464116c7c6e"): Account(
                    code=Op.CALL(
                        gas=Op.DUP2,
                        address=Op.COINBASE,
                        value=Op.DUP1,
                        args_offset=Op.DUP1,
                        args_size=Op.DUP1,
                        ret_offset=Op.DUP1,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
            },
        ),
        (
            "693c6139000000000000000000000000303b6790d019874a107418eb549e4e7766a64728",  # noqa: E501
            {
                Address("0x0a92fc97bb4c47b3d5e9e96fbb1c3fc2f07dba81"): Account(
                    storage={0: 1},
                    code=Op.PUSH1[0x0]
                    + Op.DUP1
                    + Op.DUP1
                    + Op.DUP1
                    + Op.DUP1
                    + Op.CALLDATALOAD(offset=0x4)
                    + Op.PUSH1[0x64]
                    + Op.DUP2
                    + Op.JUMPI(
                        pc=0x88,
                        condition=Op.EQ(
                            0x8DDF5D9A5251C41EFD2949F53DB0A464116C7C6E, Op.DUP1
                        ),
                    )
                    + Op.JUMPI(
                        pc=0x88,
                        condition=Op.EQ(
                            0x498516B6B2F25CB6A8E011A7C37A617B77E7D500, Op.DUP1
                        ),
                    )
                    + Op.JUMPI(
                        pc=0x80,
                        condition=Op.EQ(
                            0x8873820BB96DAA39DB93AE64A9D6397E4C6A48D7, Op.DUP1
                        ),
                    )
                    + Op.PUSH20[0x303B6790D019874A107418EB549E4E7766A64728]
                    + Op.JUMPI(pc=0x79, condition=Op.EQ)
                    + Op.JUMPDEST
                    + Op.SSTORE(key=0x0, value=Op.CALL)
                    + Op.STOP
                    + Op.JUMPDEST
                    + Op.PUSH1[0x18]
                    + Op.ADD
                    + Op.JUMP(pc=0x73)
                    + Op.JUMPDEST
                    + Op.POP
                    + Op.PUSH1[0x18]
                    + Op.ADD
                    + Op.JUMP(pc=0x73)
                    + Op.JUMPDEST
                    + Op.POP
                    + Op.PUSH1[0x1B]
                    + Op.ADD
                    + Op.JUMP(pc=0x73),
                ),
                Address("0x303b6790d019874a107418eb549e4e7766a64728"): Account(
                    code=Op.STATICCALL(
                        gas=Op.DUP2,
                        address=Op.COINBASE,
                        args_offset=Op.DUP1,
                        args_size=Op.DUP1,
                        ret_offset=Op.DUP1,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x498516b6b2f25cb6a8e011a7c37a617b77e7d500"): Account(
                    code=Op.CALLCODE(
                        gas=Op.DUP2,
                        address=Op.COINBASE,
                        value=Op.DUP1,
                        args_offset=Op.DUP1,
                        args_size=Op.DUP1,
                        ret_offset=Op.DUP1,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x8873820bb96daa39db93ae64a9d6397e4c6a48d7"): Account(
                    code=Op.DELEGATECALL(
                        gas=Op.DUP2,
                        address=Op.COINBASE,
                        args_offset=Op.DUP1,
                        args_size=Op.DUP1,
                        ret_offset=Op.DUP1,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
                Address("0x8ddf5d9a5251c41efd2949f53db0a464116c7c6e"): Account(
                    code=Op.CALL(
                        gas=Op.DUP2,
                        address=Op.COINBASE,
                        value=Op.DUP1,
                        args_offset=Op.DUP1,
                        args_size=Op.DUP1,
                        ret_offset=Op.DUP1,
                        ret_size=0x0,
                    )
                    + Op.STOP
                ),
            },
        ),
    ],
    ids=["case0", "case1", "case2", "case3"],
)
@pytest.mark.pre_alloc_mutable
def test_coinbase_warm_account_call_gas_fail(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x50228c44ed92561d94511e8518a75aa463bd444b")
    sender = EOA(
        key=0x48DC5A9F099CAAAA557742CA3A990A94BE45B9969126A1BC74E5E8BE5A2B5B47
    )
    contract = Address("0x0a92fc97bb4c47b3d5e9e96fbb1c3fc2f07dba81")
    callee = Address("0x303b6790d019874a107418eb549e4e7766a64728")
    callee_1 = Address("0x498516b6b2f25cb6a8e011a7c37a617b77e7d500")
    callee_2 = Address("0x8873820bb96daa39db93ae64a9d6397e4c6a48d7")
    callee_3 = Address("0x8ddf5d9a5251c41efd2949f53db0a464116c7c6e")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000,
    )

    # Source: Yul
    # {
    #    // Depending on the called contract here, the subcall will perform
    #    // another call/delegatecall/staticcall/callcode that will only succeed  # noqa: E501
    #    // if coinbase is considered warm by default (post-Shanghai).
    #    let calladdr := calldataload(4)
    #
    #    let callgas := 100
    #    switch calladdr
    #    case <contract:0x0000000000000000000000000000000000001000> {
    #      // Extra: COINBASE + 6xPUSH1 + DUP6 + 2xPOP
    #      callgas := add(callgas, 27)
    #    }
    #    case <contract:0x0000000000000000000000000000000000002000> {
    #      // Extra: COINBASE + 6xPUSH1 + DUP6 + 2xPOP
    #      callgas := add(callgas, 27)
    #    }
    #    case <contract:0x0000000000000000000000000000000000003000> {
    #      // Extra: COINBASE + 5xPUSH1 + DUP6 + 2xPOP
    #      callgas := add(callgas, 24)
    #    }
    #    case <contract:0x0000000000000000000000000000000000004000> {
    #      // Extra: COINBASE + 5xPUSH1 + DUP6 + 2xPOP
    #      callgas := add(callgas, 24)
    #    }
    #    // Call and save result
    #    sstore(0, call(callgas, calladdr, 0, 0, 0, 0, 0))
    #
    # }
    pre[contract] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=(
            Op.PUSH1[0x0]
            + Op.DUP1
            + Op.DUP1
            + Op.DUP1
            + Op.DUP1
            + Op.CALLDATALOAD(offset=0x4)
            + Op.PUSH1[0x64]
            + Op.DUP2
            + Op.JUMPI(
                pc=0x88,
                condition=Op.EQ(
                    0x8DDF5D9A5251C41EFD2949F53DB0A464116C7C6E,
                    Op.DUP1,
                ),
            )
            + Op.JUMPI(
                pc=0x88,
                condition=Op.EQ(
                    0x498516B6B2F25CB6A8E011A7C37A617B77E7D500,
                    Op.DUP1,
                ),
            )
            + Op.JUMPI(
                pc=0x80,
                condition=Op.EQ(
                    0x8873820BB96DAA39DB93AE64A9D6397E4C6A48D7,
                    Op.DUP1,
                ),
            )
            + Op.PUSH20[0x303B6790D019874A107418EB549E4E7766A64728]
            + Op.JUMPI(pc=0x79, condition=Op.EQ)
            + Op.JUMPDEST
            + Op.SSTORE(key=0x0, value=Op.CALL)
            + Op.STOP
            + Op.JUMPDEST
            + Op.PUSH1[0x18]
            + Op.ADD
            + Op.JUMP(pc=0x73)
            + Op.JUMPDEST
            + Op.POP
            + Op.PUSH1[0x18]
            + Op.ADD
            + Op.JUMP(pc=0x73)
            + Op.JUMPDEST
            + Op.POP
            + Op.PUSH1[0x1B]
            + Op.ADD
            + Op.JUMP(pc=0x73)
        ),
    )
    pre[callee] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=(
            Op.STATICCALL(
                gas=Op.DUP2,
                address=Op.COINBASE,
                args_offset=Op.DUP1,
                args_size=Op.DUP1,
                ret_offset=Op.DUP1,
                ret_size=0x0,
            )
            + Op.STOP
        ),
    )
    pre[sender] = Account(balance=0xBA1A9CE0BA1A9CE, nonce=1)
    pre[callee_1] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=(
            Op.CALLCODE(
                gas=Op.DUP2,
                address=Op.COINBASE,
                value=Op.DUP1,
                args_offset=Op.DUP1,
                args_size=Op.DUP1,
                ret_offset=Op.DUP1,
                ret_size=0x0,
            )
            + Op.STOP
        ),
    )
    pre[coinbase] = Account(balance=0xBA1A9CE0BA1A9CE, nonce=1)
    pre[callee_2] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=(
            Op.DELEGATECALL(
                gas=Op.DUP2,
                address=Op.COINBASE,
                args_offset=Op.DUP1,
                args_size=Op.DUP1,
                ret_offset=Op.DUP1,
                ret_size=0x0,
            )
            + Op.STOP
        ),
    )
    pre[callee_3] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=1,
        code=(
            Op.CALL(
                gas=Op.DUP2,
                address=Op.COINBASE,
                value=Op.DUP1,
                args_offset=Op.DUP1,
                args_size=Op.DUP1,
                ret_offset=Op.DUP1,
                ret_size=0x0,
            )
            + Op.STOP
        ),
    )

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        sender=sender,
        to=contract,
        data=tx_data,
        gas_limit=80000,
        gas_price=10,
        nonce=1,
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
