"""
Tests for [EIP-7666: EVM-ify the identity precompile](https://eips.ethereum.org/EIPS/eip-7666).

The identity precompile is retired: seven bytes of EVM code at its
address return the calldata unchanged, observable as ordinary code and
charged ordinary EVM gas.
"""

import pytest
from execution_testing import (
    AccessList,
    Account,
    Alloc,
    Bytes,
    CodeGasMeasure,
    Fork,
    Op,
    StateTestFiller,
    Storage,
    Transaction,
    keccak256,
)

from .spec import Spec, ref_spec_7666

REFERENCE_SPEC_GIT_PATH = ref_spec_7666.git_path
REFERENCE_SPEC_VERSION = ref_spec_7666.version

pytestmark = pytest.mark.valid_from("EIP7666")

IDENTITY = int.from_bytes(Spec.IDENTITY_PRECOMPILE_ADDRESS, "big")


def identity_runtime_gas(fork: Fork, size: int) -> int:
    """Return the exact gas used by the EIP-7666 replacement bytecode."""
    return (
        2 * Op.CALLDATASIZE.gas_cost(fork)
        + 3 * Op.PUSH0.gas_cost(fork)
        + Op.CALLDATACOPY(
            data_size=size,
            old_memory_size=0,
            new_memory_size=size,
        ).gas_cost(fork)
        + Op.RETURN(
            old_memory_size=size,
            new_memory_size=size,
        ).gas_cost(fork)
    )


def test_replacement_code_observable(
    state_test: StateTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    The retired address holds exactly the specified seven bytes of
    code, sized and hashed like any contract.
    """
    storage = Storage()
    contract = pre.deploy_contract(
        code=Op.SSTORE(
            storage.store_next(len(Spec.EVM_CODE)), Op.EXTCODESIZE(IDENTITY)
        )
        + Op.SSTORE(
            storage.store_next(keccak256(Spec.EVM_CODE)),
            Op.EXTCODEHASH(IDENTITY),
        )
    )
    tx = Transaction(sender=pre.fund_eoa(), to=contract)
    state_test(pre=pre, tx=tx, post={contract: Account(storage=storage)})


@pytest.mark.parametrize(
    "size",
    [
        pytest.param(0, id="empty"),
        pytest.param(1, id="single_byte"),
        pytest.param(32, id="one_word"),
        pytest.param(33, id="word_plus_one"),
        pytest.param(96, id="three_words"),
    ],
)
def test_identity_equivalence(
    state_test: StateTestFiller, pre: Alloc, fork: Fork, size: int
) -> None:
    """
    The replacement returns its calldata unchanged: the returndata size
    matches the input size and the round-tripped bytes are identical.
    """
    data = Bytes(bytes(range(1, size + 1)) if size else b"")
    storage = Storage()
    code = (
        Op.CALLDATACOPY(0, 0, Op.CALLDATASIZE)
        + Op.SSTORE(
            storage.store_next(1),
            Op.CALL(address=IDENTITY, args_size=Op.CALLDATASIZE),
        )
        + Op.SSTORE(storage.store_next(size), Op.RETURNDATASIZE)
    )
    if size:
        code += Op.RETURNDATACOPY(0x100, 0, Op.RETURNDATASIZE)
        first_word = int.from_bytes(bytes(data[:32]).ljust(32, b"\x00"), "big")
        code += Op.SSTORE(storage.store_next(first_word), Op.MLOAD(0x100))
        last_offset = 0x100 + size - 32 if size >= 32 else 0x100
        last_word = int.from_bytes(
            bytes(data[-32:]).ljust(32, b"\x00")
            if size < 32
            else bytes(data[size - 32 : size]),
            "big",
        )
        code += Op.SSTORE(storage.store_next(last_word), Op.MLOAD(last_offset))
    contract = pre.deploy_contract(code=code)
    tx = Transaction(sender=pre.fund_eoa(), to=contract, data=data)
    state_test(pre=pre, tx=tx, post={contract: Account(storage=storage)})


@pytest.mark.parametrize("warm", [False, True], ids=["cold", "warm"])
@pytest.mark.with_all_call_opcodes()
def test_retired_identity_address_access_cost(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    call_opcode: Op,
    warm: bool,
) -> None:
    """
    Address ``0x04`` is no longer implicitly warm as a precompile.

    Its first access is cold unless the transaction access list warms it.
    This is consensus-observable independently of the replacement code's
    execution, so the call forwards zero gas and only its access cost is
    measured.
    """
    measured_code = call_opcode(gas=0, address=IDENTITY)
    cold_call = call_opcode(address_warm=False)
    measure_contract = pre.deploy_contract(
        code=CodeGasMeasure(
            code=measured_code,
            overhead_cost=(
                measured_code.gas_cost(fork) - cold_call.gas_cost(fork)
            ),
            extra_stack_items=1,
        )
    )
    tx = Transaction(
        sender=pre.fund_eoa(),
        to=measure_contract,
        access_list=[
            AccessList(
                address=Spec.IDENTITY_PRECOMPILE_ADDRESS,
                storage_keys=[],
            )
        ]
        if warm
        else None,
    )
    expected_gas = call_opcode(address_warm=warm).gas_cost(fork)
    state_test(
        pre=pre,
        tx=tx,
        post={measure_contract: Account(storage={0: expected_gas})},
    )


@pytest.mark.parametrize(
    "size",
    [
        pytest.param(0, id="empty"),
        pytest.param(1, id="single_byte"),
        pytest.param(32, id="one_word"),
        pytest.param(33, id="word_plus_one"),
        pytest.param(96, id="three_words"),
    ],
)
@pytest.mark.parametrize(
    "gas_delta,expected_success",
    [
        pytest.param(-1, 0, id="one_short"),
        pytest.param(0, 1, id="exact"),
    ],
)
def test_replacement_code_exact_gas_boundary(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    size: int,
    gas_delta: int,
    expected_success: int,
) -> None:
    """The replacement succeeds with exactly its runtime gas, not one less."""
    forwarded_gas = identity_runtime_gas(fork, size) + gas_delta
    caller = pre.deploy_contract(
        code=Op.CALLDATACOPY(0, 0, size)
        + Op.SSTORE(
            0,
            Op.CALL(
                gas=forwarded_gas,
                address=IDENTITY,
                args_offset=0,
                args_size=size,
            ),
        )
    )
    tx = Transaction(
        sender=pre.fund_eoa(),
        to=caller,
        data=bytes(range(1, size + 1)),
    )
    state_test(
        pre=pre,
        tx=tx,
        post={caller: Account(storage={0: expected_success})},
    )


def test_identity_via_eip7702_delegation(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """
    A delegation to ``0x04`` executes the replacement as ordinary code.

    EIP-7702 disables precompile dispatch for delegated calls. Retiring the
    identity precompile therefore makes its state code reachable in this
    context, and the call must still round-trip its input.
    """
    data = Bytes(bytes(range(1, 34)))
    delegated_eoa = pre.fund_eoa(
        amount=0,
        delegation=Spec.IDENTITY_PRECOMPILE_ADDRESS,
    )
    caller = pre.deploy_contract(
        code=Op.CALLDATACOPY(0, 0, Op.CALLDATASIZE)
        + Op.SSTORE(
            0,
            Op.CALL(
                address=delegated_eoa,
                args_size=Op.CALLDATASIZE,
            ),
        )
        + Op.RETURNDATACOPY(0x100, 0, Op.RETURNDATASIZE)
        + Op.SSTORE(1, Op.RETURNDATASIZE)
        + Op.SSTORE(2, Op.MLOAD(0x100))
        + Op.SSTORE(3, Op.MLOAD(0x101))
    )
    tx = Transaction(sender=pre.fund_eoa(), to=caller, data=data)
    state_test(
        pre=pre,
        tx=tx,
        post={
            caller: Account(
                storage={
                    0: 1,
                    1: len(data),
                    2: int.from_bytes(bytes(data[:32]), "big"),
                    3: int.from_bytes(bytes(data[1:33]), "big"),
                }
            )
        },
    )
