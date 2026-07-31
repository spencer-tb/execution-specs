"""
Verify mass creation of max-codesize contracts: a delegatecalled creator
commits its creations to the caller, a called creator either reverts them
all on a final INVALID or keeps them, and a self-destruct sweep removes a
prefix of the created contracts.

Ported from:
state_tests/stCreateTest/CreateOOGafterMaxCodesizeFiller.yml

@manually-enhanced: Do not overwrite. The expect table was folded into a
post derived from the per-case creation counts. The compiled-Yul bytecode
(pc-sensitive, with embedded 0xC0DE* addresses) is kept verbatim, and the
4-gigagas budget keeps the test capped at Prague: EIP-7825 cannot fit
hundreds of max-codesize deposits in one transaction.
"""

import pytest
from execution_testing import (
    Account,
    Address,
    Alloc,
    Bytes,
    Environment,
    Hash,
    StateTestFiller,
    Transaction,
    compute_create_address,
)
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"

# Deployed size of every created contract, fixed by the init-code template
# contract's RETURN(0, 0x6000); the clones store their CODESIZE when run.
DEPLOYED_SIZE = 0x6000
TX_GAS_LIMIT = 2**32


@pytest.mark.ported_from(
    ["state_tests/stCreateTest/CreateOOGafterMaxCodesizeFiller.yml"],
)
@pytest.mark.valid_from("Cancun")
@pytest.mark.valid_until("Prague")
@pytest.mark.slow
@pytest.mark.parametrize(
    "delegate_count, subcall_count, subcall_oog, selfdestruct_count",
    [
        pytest.param(
            0x0,
            0xA,
            True,
            0x0,
            id="LowContractCount_NoDelegateCreate_CallCreateOOG",
        ),
        pytest.param(
            0xA,
            0xA,
            True,
            0x0,
            id="LowContractCount_DelegateCreate_CallCreateOOG",
        ),
        pytest.param(
            0xA,
            0xA,
            False,
            0xE,
            id="LowContractCount_DelegateCreate_CallCreate_SelfDestruct",
        ),
        pytest.param(
            0x0,
            0xFA,
            True,
            0x0,
            id="HighContractCount_NoDelegateCreate_CallCreateOOG",
        ),
        pytest.param(
            0xFA,
            0xFA,
            True,
            0x0,
            id="HighContractCount_DelegateCreate_CallCreateOOG",
        ),
        pytest.param(
            0xFA,
            0xFA,
            False,
            0x1EE,
            id="HighContractCount_DelegateCreate_CallCreate_SelfDestruct",
        ),
    ],
)
@pytest.mark.pre_alloc_mutable
def test_create_oo_gafter_max_codesize(
    state_test: StateTestFiller,
    pre: Alloc,
    delegate_count: int,
    subcall_count: int,
    subcall_oog: bool,
    selfdestruct_count: int,
) -> None:
    """Create max-codesize contracts by delegate, call, and sweep paths."""
    coinbase = Address(0x2ADC25665018AA1FE0E6BC666DAC8FC2697FF9BA)
    contract_0 = Address(0x00000000000000000000000000000000000C0DE0)
    contract_1 = Address(0x00000000000000000000000000000000000C0DE1)
    contract_2 = Address(0x00000000000000000000000000000000000C0DEB)
    contract_3 = Address(0x00000000000000000000000000000000000C0DEA)
    sender = pre.fund_eoa(amount=0xBA1A9CE0BA1A9CE)

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=TX_GAS_LIMIT,
    )

    # Source: yul
    # berlin
    # {
    #   // If calldata > 0, self-destruct, otherwise
    #   sstore(0, codesize())
    #   if gt(calldatasize(), 0) {
    #     selfdestruct(0)
    #   }
    # }
    contract_0 = pre.deploy_contract(  # noqa: F841
        code=Op.SSTORE(key=0x0, value=Op.CODESIZE)
        + Op.JUMPI(pc=0xC, condition=Op.GT(Op.CALLDATASIZE, 0x0))
        + Op.STOP
        + Op.JUMPDEST
        + Op.SELFDESTRUCT(address=0x0),
        nonce=0,
        address=Address(0x00000000000000000000000000000000000C0DE0),  # noqa: E501
    )
    # Source: yul
    # berlin
    # {
    #   // Init code that uses max codesize and can be called to selfdestruct
    #   let code_addr := 0x00000000000000000000000000000000000c0de0
    #   extcodecopy(code_addr, 0, 0, extcodesize(code_addr))
    #   return(0, 0x6000)
    # }
    contract_1 = pre.deploy_contract(  # noqa: F841
        code=Op.PUSH3[0xC0DE0]
        + Op.PUSH1[0x0]
        + Op.DUP1
        + Op.EXTCODESIZE(address=Op.DUP3)
        + Op.SWAP3
        + Op.EXTCODECOPY
        + Op.RETURN(offset=0x0, size=0x6000),
        nonce=0,
        address=Address(0x00000000000000000000000000000000000C0DE1),  # noqa: E501
    )
    # Source: yul
    # berlin
    # {
    #   sstore (1, 1)
    #   let contract_count := calldataload(0)
    #   let should_oog := calldataload(32)
    #
    #   // get the init code that returns max codesize from another contract
    #   let initcode_addr := 0x00000000000000000000000000000000000c0de1
    #   let initcode_size := extcodesize(initcode_addr)
    #   extcodecopy(initcode_addr, 0, 0, initcode_size)
    #
    #   // create contracts with max codesize in loop
    #   for { let i := 0 } lt(i, contract_count) { i := add(i, 1) }
    #   {
    #       let address_created := create(0, 0, initcode_size)
    #       mstore( add(initcode_size, mul(i, 32)), address_created )
    #   }
    #   if gt(should_oog, 0) {
    #     invalid()
    #   }
    #   return(initcode_size, mul(contract_count, 32))
    # }
    contract_2 = pre.deploy_contract(  # noqa: F841
        code=Op.SSTORE(key=Op.DUP1, value=0x1)
        + Op.PUSH1[0x0]
        + Op.CALLDATALOAD(offset=Op.DUP1)
        + Op.CALLDATALOAD(offset=0x20)
        + Op.PUSH3[0xC0DE1]
        + Op.DUP4
        + Op.EXTCODESIZE(address=Op.DUP2)
        + Op.SWAP5
        + Op.DUP6
        + Op.SWAP3
        + Op.EXTCODECOPY
        + Op.PUSH1[0x0]
        + Op.JUMPDEST
        + Op.JUMPI(pc=0x2D, condition=Op.LT(Op.DUP2, Op.DUP3))
        + Op.POP
        + Op.PUSH1[0x0]
        + Op.JUMPI(pc=0x2B, condition=Op.LT)
        + Op.PUSH1[0x20]
        + Op.MUL
        + Op.SWAP1
        + Op.RETURN
        + Op.JUMPDEST
        + Op.INVALID
        + Op.JUMPDEST
        + Op.PUSH1[0x1]
        + Op.SWAP1
        + Op.MSTORE(
            offset=Op.ADD(Op.DUP7, Op.MUL(Op.DUP3, 0x20)),
            value=Op.CREATE(value=Op.DUP1, offset=0x0, size=Op.DUP5),
        )
        + Op.ADD
        + Op.JUMP(pc=0x18),
        nonce=1,
        address=Address(0x00000000000000000000000000000000000C0DEB),  # noqa: E501
    )
    # Source: yul
    # berlin
    # {
    #
    #   // Get the amount of contracts to create on this level
    #   let delegate_contract_count := calldataload(4)
    #
    #   // Get the amount of contracts to create on the sub level call
    #   let subcall_contract_count := calldataload(36)
    #
    #   // Get whether the subcall should oog
    #   let subcall_oog := calldataload(68)
    #
    #   // Get count of contracts to call to self-destruct
    #   let selfdestruct_count := calldataload(100)
    #
    #   // Delegate call for contract creation
    #   mstore(0, delegate_contract_count)
    #   mstore(32, 0)
    #   let returnStart := 64
    #   let returnLength := mul(delegate_contract_count, 32)
    #   let retcode := delegatecall(div(gas(), 2), 0x00000000000000000000000000000000000c0deb, 0, 64, returnStart, returnLength)  # noqa: E501
    #
    #   if eq(retcode, 0) {
    #     // We oog'd, fail test
    #     revert(0, 0)
    #   }
    #
    #   // Call for OOG contract creation
    #   mstore(0, subcall_contract_count)
    #   mstore(32, subcall_oog)
    # ... (31 more lines)
    contract_3 = pre.deploy_contract(  # noqa: F841
        code=Op.CALLDATALOAD(offset=0x4)
        + Op.CALLDATALOAD(offset=0x24)
        + Op.CALLDATALOAD(offset=0x44)
        + Op.SWAP1
        + Op.CALLDATALOAD(offset=0x64)
        + Op.SWAP3
        + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.MSTORE(offset=0x20, value=0x0)
        + Op.PUSH1[0x0]
        + Op.PUSH1[0x40]
        + Op.MUL(Op.DUP4, 0x20)
        + Op.SWAP1
        + Op.PUSH1[0x40]
        + Op.DUP4
        + Op.PUSH3[0xC0DEB]
        + Op.JUMPI(
            pc=0xBF, condition=Op.EQ(Op.DELEGATECALL, Op.DIV(Op.GAS, 0x2))
        )
        + Op.MSTORE(offset=0x0, value=Op.DUP2)
        + Op.MSTORE(offset=0x20, value=Op.DUP3)
        + Op.PUSH1[0x0]
        + Op.ADD(0x40, Op.MUL(Op.DUP3, 0x20))
        + Op.MUL(Op.DUP5, 0x20)
        + Op.SWAP1
        + Op.PUSH1[0x40]
        + Op.DUP4
        + Op.DUP1
        + Op.PUSH3[0xC0DEB]
        + Op.JUMPI(pc=0xBA, condition=Op.EQ(Op.CALL, Op.DIV(Op.GAS, 0x2)))
        + Op.JUMPDEST
        + Op.PUSH1[0x0]
        + Op.DUP2
        + Op.SWAP4
        + Op.JUMPI(pc=0xB1, condition=Op.EQ)
        + Op.JUMPDEST
        + Op.POP * 2
        + Op.PUSH1[0x0]
        + Op.JUMPDEST
        + Op.JUMPI(pc=0x94, condition=Op.LT(Op.DUP2, Op.DUP2))
        + Op.DUP3
        + Op.PUSH1[0x0]
        + Op.JUMPDEST
        + Op.JUMPI(pc=0x77, condition=Op.LT(Op.DUP2, Op.DUP2))
        + Op.STOP
        + Op.JUMPDEST
        + Op.DUP1
        + Op.PUSH1[0x0]
        + Op.DUP1
        + Op.PUSH1[0x1]
        + Op.DUP2
        + Op.DUP1
        + Op.PUSH1[0x20]
        + Op.DUP4
        + Op.SWAP8
        + Op.MLOAD(offset=Op.ADD(0x40, Op.MUL))
        + Op.SUB(Op.GAS, 0x3E8)
        + Op.POP(Op.CALL)
        + Op.ADD
        + Op.JUMP(pc=0x6F)
        + Op.JUMPDEST
        + Op.DUP1
        + Op.PUSH1[0x0]
        + Op.DUP1 * 4
        + Op.PUSH1[0x20]
        + Op.PUSH1[0x1]
        + Op.SWAP8
        + Op.MLOAD(offset=Op.ADD(0x40, Op.MUL))
        + Op.SUB(Op.GAS, 0x3E8)
        + Op.POP(Op.CALL)
        + Op.ADD
        + Op.JUMP(pc=0x65)
        + Op.JUMPDEST
        + Op.ADD
        + Op.SWAP1
        + Op.POP
        + Op.CODESIZE
        + Op.DUP1
        + Op.JUMP(pc=0x60)
        + Op.JUMPDEST
        + Op.JUMPI(pc=0x57, condition=Op.DUP3)
        + Op.JUMPDEST
        + Op.REVERT(offset=Op.DUP1, size=0x0),
        nonce=1,
    )

    data = (
        Bytes("a6f227c0")
        + Hash(delegate_count)
        + Hash(subcall_count)
        + Hash(1 if subcall_oog else 0)
        + Hash(selfdestruct_count)
    )

    tx = Transaction(
        sender=sender,
        to=contract_3,
        data=data,
        gas_limit=TX_GAS_LIMIT,
    )

    # The delegatecalled creator commits its work to the top contract: its
    # marker store lands in contract_3's storage and its creations consume
    # contract_3's nonces. The called creator keeps its work only when it
    # does not end on INVALID.
    post: dict = {
        contract_3: Account(storage={1: 1}, nonce=1 + delegate_count),
        contract_2: (
            Account(storage={}, nonce=1)
            if subcall_oog
            else Account(storage={1: 1}, nonce=1 + subcall_count)
        ),
    }
    # The self-destruct sweep removes the delegate-created contracts
    # first, then a prefix of the call-created ones.
    destroyed_subcall = selfdestruct_count - delegate_count
    if delegate_count:
        for nonce in {1, delegate_count}:
            post[compute_create_address(address=contract_3, nonce=nonce)] = (
                Account.NONEXISTENT
                if selfdestruct_count
                else Account(storage={0: DEPLOYED_SIZE})
            )
    if subcall_oog:
        # Every call-created contract was reverted by the INVALID.
        for nonce in {1, subcall_count}:
            post[compute_create_address(address=contract_2, nonce=nonce)] = (
                Account.NONEXISTENT
            )
    else:
        for nonce in {1, destroyed_subcall}:
            post[compute_create_address(address=contract_2, nonce=nonce)] = (
                Account.NONEXISTENT
            )
        for nonce in range(destroyed_subcall + 1, subcall_count + 1):
            post[compute_create_address(address=contract_2, nonce=nonce)] = (
                Account(storage={0: DEPLOYED_SIZE})
            )

    state_test(env=env, pre=pre, post=post, tx=tx)
