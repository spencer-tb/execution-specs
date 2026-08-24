"""
Tests for [EIP-7819: SETDELEGATE instruction](https://eips.ethereum.org/EIPS/eip-7819).

SETDELEGATE writes an EIP-7702 delegation designation at an address
derived from the executing account and a salt. A zero target clears the
designation instead. The written account's nonce is raised to one so it
can never return to an empty state.
"""

import pytest
from execution_testing import (
    Account,
    Address,
    Alloc,
    BalAccountExpectation,
    BalCodeChange,
    BalNonceChange,
    Block,
    BlockAccessListExpectation,
    BlockchainTestFiller,
    Op,
    StateTestFiller,
    Storage,
    Transaction,
    compute_create_address,
    compute_setdelegate_address,
)
from execution_testing.checklists import EIPChecklist

from .spec import Spec, ref_spec_7819

REFERENCE_SPEC_GIT_PATH = ref_spec_7819.git_path
REFERENCE_SPEC_VERSION = ref_spec_7819.version

pytestmark = pytest.mark.valid_from("EIP7819")

SALT = 0xC0FFEE
CANARY = 0xC0DE


@EIPChecklist.Opcode.Test.ContractCreation.Address()
@pytest.mark.pre_alloc_mutable
@pytest.mark.parametrize(
    "location_pre",
    [
        pytest.param("nonexistent", id="nonexistent"),
        pytest.param("funded_eoa", id="funded_eoa"),
        pytest.param("existing_designation", id="existing_designation"),
    ],
)
def test_designation_write(
    state_test: StateTestFiller,
    pre: Alloc,
    location_pre: str,
) -> None:
    """
    Write a designation and verify the derived address, its code, its
    nonce, and the location pushed onto the stack.
    """
    target = pre.fund_eoa(amount=0)
    factory = pre.deploy_contract(
        code=Op.SSTORE(0, Op.SETDELEGATE(SALT, target)),
    )
    location = compute_setdelegate_address(factory, SALT)

    expected_nonce = 1
    if location_pre == "funded_eoa":
        pre.fund_address(location, 1)
    elif location_pre == "existing_designation":
        old_target = pre.fund_eoa(amount=0)
        pre.deploy_contract(
            code=Spec.delegation_designation(old_target),
            address=location,
            nonce=7,
        )
        expected_nonce = 7

    tx = Transaction(to=factory, sender=pre.fund_eoa())

    post = {
        factory: Account(storage={0: location}),
        location: Account(
            code=Spec.delegation_designation(target),
            nonce=expected_nonce,
        ),
    }
    state_test(pre=pre, post=post, tx=tx)


@pytest.mark.pre_alloc_mutable
@pytest.mark.parametrize(
    "location_pre",
    [
        pytest.param("nonexistent", id="nonexistent"),
        pytest.param("existing_designation", id="existing_designation"),
        pytest.param("set_same_tx", id="set_same_tx"),
    ],
)
def test_clear_designation(
    state_test: StateTestFiller,
    pre: Alloc,
    location_pre: str,
) -> None:
    """
    A zero target clears the designation but the account persists with
    a nonce of at least one, so it never returns to an empty state.
    """
    code = Op.POP(Op.SETDELEGATE(SALT, 0))
    if location_pre == "set_same_tx":
        target = pre.fund_eoa(amount=0)
        code = Op.POP(Op.SETDELEGATE(SALT, target)) + code
    factory = pre.deploy_contract(code=code)
    location = compute_setdelegate_address(factory, SALT)

    expected_nonce = 1
    if location_pre == "existing_designation":
        old_target = pre.fund_eoa(amount=0)
        pre.deploy_contract(
            code=Spec.delegation_designation(old_target),
            address=location,
            nonce=3,
        )
        expected_nonce = 3

    tx = Transaction(to=factory, sender=pre.fund_eoa())

    post = {
        location: Account(code=b"", nonce=expected_nonce),
    }
    state_test(pre=pre, post=post, tx=tx)


@pytest.mark.parametrize(
    "target_word,expected_target_bytes",
    [
        pytest.param(
            (0xBADC0FFEE << 160) | 0x1122334455667788990011223344556677889900,
            bytes.fromhex("1122334455667788990011223344556677889900"),
            id="oversized_word_trimmed",
        ),
        pytest.param(
            0x1234,
            (0x1234).to_bytes(20, "big"),
            id="small_word_left_padded",
        ),
    ],
)
def test_target_word_masking(
    state_test: StateTestFiller,
    pre: Alloc,
    target_word: int,
    expected_target_bytes: bytes,
) -> None:
    """
    The target stack word is masked to its 20 low-order bytes, so the
    written designation is always exactly 23 bytes.
    """
    factory = pre.deploy_contract(
        code=Op.POP(Op.SETDELEGATE(SALT, target_word)),
    )
    location = compute_setdelegate_address(factory, SALT)

    tx = Transaction(to=factory, sender=pre.fund_eoa())

    post = {
        location: Account(
            code=Spec.DESIGNATOR + expected_target_bytes,
            nonce=1,
        ),
    }
    state_test(pre=pre, post=post, tx=tx)


@pytest.mark.pre_alloc_mutable
def test_address_derivation_vector(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """
    Pin the address preimage and top-first stack order with a fixed
    vector that is independent of the test framework's address helper.
    """
    factory_address = Address(0x1000000000000000000000000000000000000001)
    target = Address(0x2000000000000000000000000000000000000002)
    factory = pre.deploy_contract(
        code=Op.POP(Op.SETDELEGATE(0, target)),
        address=factory_address,
    )
    assert factory == factory_address

    # keccak256(0xef0100 ++ factory_address ++ bytes32(0))[12:]
    expected_location = Address(0xF0A2CC0F12106E99C59353031A1C5AB3C82B165C)
    tx = Transaction(to=factory, sender=pre.fund_eoa())

    post = {
        expected_location: Account(
            code=Spec.delegation_designation(target),
            nonce=1,
        ),
    }
    state_test(pre=pre, post=post, tx=tx)


@EIPChecklist.Opcode.Test.ContractCreation.Failure.Collision()
@pytest.mark.pre_alloc_mutable
@pytest.mark.parametrize(
    "collision_code",
    [
        pytest.param(bytes(Op.STOP), id="plain_code"),
        pytest.param(b"\xef\x01", id="truncated_marker"),
        pytest.param(b"\xef\x01\x01" + b"\x11" * 20, id="wrong_marker"),
        pytest.param(b"\xef\x01\x00" + b"\x11" * 19, id="short_designation"),
        pytest.param(b"\xef\x01\x00" + b"\x11" * 21, id="long_designation"),
    ],
)
def test_collision_with_non_designation_code(
    state_test: StateTestFiller,
    pre: Alloc,
    collision_code: bytes,
) -> None:
    """
    Non-empty code at the derived address that is not a designation
    exceptionally halts the frame and consumes its gas.
    """
    target = pre.fund_eoa(amount=0)
    factory = pre.deploy_contract(
        code=Op.POP(Op.SETDELEGATE(SALT, target)) + Op.SSTORE(0, CANARY),
    )
    location = compute_setdelegate_address(factory, SALT)
    pre.deploy_contract(code=collision_code, address=location, nonce=5)

    caller_storage = Storage()
    caller = pre.deploy_contract(
        code=Op.SSTORE(
            caller_storage.store_next(0, "call_success"),
            Op.CALL(address=factory),
        ),
    )

    tx = Transaction(to=caller, sender=pre.fund_eoa())

    post = {
        caller: Account(storage=caller_storage),
        factory: Account(storage={0: 0}),
        location: Account(code=collision_code, nonce=5),
    }
    state_test(pre=pre, post=post, tx=tx)


@EIPChecklist.Opcode.Test.ExecutionContext.Staticcall.BanCheck()
@EIPChecklist.Opcode.Test.ExecutionContext.Staticcall.BanNoModification()
def test_static_context(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """
    SETDELEGATE in a static frame exceptionally halts and writes no
    designation.
    """
    target = pre.fund_eoa(amount=0)
    factory = pre.deploy_contract(
        code=Op.POP(Op.SETDELEGATE(SALT, target)),
    )
    location = compute_setdelegate_address(factory, SALT)

    caller_storage = Storage()
    caller = pre.deploy_contract(
        code=Op.SSTORE(
            caller_storage.store_next(0, "staticcall_success"),
            Op.STATICCALL(address=factory),
        ),
    )

    tx = Transaction(to=caller, sender=pre.fund_eoa())

    post = {
        caller: Account(storage=caller_storage),
        location: Account.NONEXISTENT,
    }
    state_test(pre=pre, post=post, tx=tx)


@EIPChecklist.Opcode.Test.ExecutionContext.Call()
@EIPChecklist.Opcode.Test.ExecutionContext.Callcode()
@EIPChecklist.Opcode.Test.ExecutionContext.Delegatecall()
@pytest.mark.parametrize(
    "call_opcode",
    [
        pytest.param(Op.CALL, id="call"),
        pytest.param(Op.CALLCODE, id="callcode"),
        pytest.param(Op.DELEGATECALL, id="delegatecall"),
    ],
)
def test_derivation_address_by_call_context(
    state_test: StateTestFiller,
    pre: Alloc,
    call_opcode: Op,
) -> None:
    """
    The derivation address is the executing account: the callee under
    CALL and the caller under DELEGATECALL and CALLCODE.
    """
    target = pre.fund_eoa(amount=0)
    writer = pre.deploy_contract(
        code=Op.POP(Op.SETDELEGATE(SALT, target)),
    )
    caller = pre.deploy_contract(
        code=Op.POP(call_opcode(address=writer)),
    )

    deriving_account = writer if call_opcode == Op.CALL else caller
    location = compute_setdelegate_address(deriving_account, SALT)
    other_location = compute_setdelegate_address(
        caller if call_opcode == Op.CALL else writer, SALT
    )

    tx = Transaction(to=caller, sender=pre.fund_eoa())

    post = {
        location: Account(code=Spec.delegation_designation(target), nonce=1),
        other_location: Account.NONEXISTENT,
    }
    state_test(pre=pre, post=post, tx=tx)


@EIPChecklist.Opcode.Test.ExecutionContext.Initcode.Behavior.Opcode()
def test_derivation_address_in_initcode(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """
    SETDELEGATE in initcode derives the written address from the
    contract under construction.
    """
    target = pre.fund_eoa(amount=0)
    initcode = Op.POP(Op.SETDELEGATE(SALT, target)) + Op.STOP
    factory = pre.deploy_contract(
        code=Op.CALLDATACOPY(0, 0, Op.CALLDATASIZE)
        + Op.POP(Op.CREATE(0, 0, Op.CALLDATASIZE)),
    )
    created = compute_create_address(address=factory, nonce=1)
    location = compute_setdelegate_address(created, SALT)

    tx = Transaction(to=factory, data=initcode, sender=pre.fund_eoa())

    post = {
        created: Account(code=b"", nonce=1),
        location: Account(code=Spec.delegation_designation(target), nonce=1),
    }
    state_test(pre=pre, post=post, tx=tx)


def test_delegation_effective_immediately(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """
    A call to the written address right after SETDELEGATE executes the
    delegated code in the delegating account's context.
    """
    target = pre.deploy_contract(code=Op.SSTORE(0, CANARY))
    factory = pre.deploy_contract(
        code=Op.POP(Op.CALL(address=Op.SETDELEGATE(SALT, target))),
    )
    location = compute_setdelegate_address(factory, SALT)

    tx = Transaction(to=factory, sender=pre.fund_eoa())

    post = {
        location: Account(
            code=Spec.delegation_designation(target),
            nonce=1,
            storage={0: CANARY},
        ),
        target: Account(storage={}),
    }
    state_test(pre=pre, post=post, tx=tx)


def test_selfdestruct_does_not_delete_designation(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """
    A designation account created this transaction survives executing
    SELFDESTRUCT through its delegation: the balance is swept but the
    account is not deleted.
    """
    beneficiary = pre.fund_eoa(amount=1)
    target = pre.deploy_contract(code=Op.SELFDESTRUCT(beneficiary))
    balance = 0x1234
    factory = pre.deploy_contract(
        code=Op.POP(
            Op.CALL(
                address=Op.SETDELEGATE(SALT, target),
                value=balance,
            )
        ),
        balance=balance,
    )
    location = compute_setdelegate_address(factory, SALT)

    tx = Transaction(to=factory, sender=pre.fund_eoa())

    post = {
        location: Account(
            code=Spec.delegation_designation(target),
            nonce=1,
            balance=0,
        ),
        beneficiary: Account(balance=1 + balance),
    }
    state_test(pre=pre, post=post, tx=tx)


@pytest.mark.parametrize(
    "special_target",
    [
        pytest.param("precompile", id="precompile"),
        pytest.param("designation", id="chained_designation"),
    ],
)
def test_delegation_to_special_targets(
    state_test: StateTestFiller,
    pre: Alloc,
    special_target: str,
) -> None:
    """
    Designations written by SETDELEGATE behave like EIP-7702 ones for
    special targets: a precompile target executes as empty code and a
    designation chain is not followed.
    """
    storage = Storage()
    if special_target == "precompile":
        # The identity precompile is used as the specimen because its
        # body would observably echo the call data if it executed.
        target = Address(0x04)
        expected_call_success = 1
    else:
        chain_end = pre.deploy_contract(code=Op.SSTORE(0, CANARY))
        target = pre.deploy_contract(
            code=Spec.delegation_designation(chain_end),
            nonce=1,
        )
        # Executing the raw designation bytes hits the invalid 0xEF
        # opcode, so the call fails without following the chain.
        expected_call_success = 0

    factory = pre.deploy_contract(
        code=Op.MSTORE(0, CANARY)
        + Op.SSTORE(
            storage.store_next(expected_call_success, "call_success"),
            Op.CALL(
                address=Op.SETDELEGATE(SALT, target),
                args_offset=0,
                args_size=32,
                ret_offset=32,
                ret_size=32,
            ),
        )
        + Op.SSTORE(
            storage.store_next(0, "returndata_size"), Op.RETURNDATASIZE
        ),
    )
    location = compute_setdelegate_address(factory, SALT)

    tx = Transaction(to=factory, sender=pre.fund_eoa())

    post = {
        factory: Account(storage=storage),
        location: Account(
            code=Spec.delegation_designation(target),
            nonce=1,
        ),
    }
    state_test(pre=pre, post=post, tx=tx)


@EIPChecklist.Opcode.Test.StackUnderflow()
def test_stack_underflow(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """
    SETDELEGATE with fewer than two stack items exceptionally halts.
    """
    factory = pre.deploy_contract(code=Op.PUSH1(1) + Op.SETDELEGATE)

    caller_storage = Storage()
    caller = pre.deploy_contract(
        code=Op.SSTORE(
            caller_storage.store_next(0, "call_success"),
            Op.CALL(address=factory),
        ),
    )

    tx = Transaction(to=caller, sender=pre.fund_eoa())

    post = {caller: Account(storage=caller_storage)}
    state_test(pre=pre, post=post, tx=tx)


def test_block_access_list(
    blockchain_test: BlockchainTestFiller,
    pre: Alloc,
) -> None:
    """
    The designation write is recorded in the block access list as a
    code change and a nonce change on the written account.
    """
    target = pre.fund_eoa(amount=0)
    factory = pre.deploy_contract(
        code=Op.POP(Op.SETDELEGATE(SALT, target)),
    )
    location = compute_setdelegate_address(factory, SALT)

    tx = Transaction(to=factory, sender=pre.fund_eoa())

    block = Block(
        txs=[tx],
        expected_block_access_list=BlockAccessListExpectation(
            account_expectations={
                location: BalAccountExpectation(
                    nonce_changes=[
                        BalNonceChange(block_access_index=1, post_nonce=1)
                    ],
                    code_changes=[
                        BalCodeChange(
                            block_access_index=1,
                            new_code=Spec.delegation_designation(target),
                        )
                    ],
                ),
            }
        ),
    )

    post = {
        location: Account(code=Spec.delegation_designation(target), nonce=1),
    }
    blockchain_test(pre=pre, blocks=[block], post=post)
