"""
Tests for [EIP-8200: EVMification](https://eips.ethereum.org/EIPS/eip-8200).

The RIPEMD-160, MODEXP, and BLAKE2f precompiles are retired: EVM
bytecode with equivalent functionality lives at their addresses, is
observable as ordinary code, and is charged ordinary EVM gas.
"""

import pytest
from execution_testing import (
    Account,
    Alloc,
    Bytecode,
    Fork,
    Op,
    StateTestFiller,
    Storage,
    Transaction,
    keccak256,
)

from ...istanbul.eip152_blake2.common import Blake2bInput
from .spec import Spec, ref_spec_8200

REFERENCE_SPEC_GIT_PATH = ref_spec_8200.git_path
REFERENCE_SPEC_VERSION = ref_spec_8200.version

pytestmark = pytest.mark.valid_from("EIP8200")


def call_and_store_word(
    storage: Storage, address: int, args_size: int, expected_word: int
) -> Bytecode:
    """
    Call `address` with the calldata already in memory, then store the
    call's success flag and the first word of its returndata.
    """
    return (
        Op.SSTORE(
            storage.store_next(1),
            Op.CALL(address=address, args_size=args_size),
        )
        + Op.RETURNDATACOPY(0x100, 0, 0x20)
        + Op.SSTORE(storage.store_next(expected_word), Op.MLOAD(0x100))
    )


def test_replacement_code_observable(
    state_test: StateTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    The retired addresses hold ordinary code: sized and hashed like any
    contract, where a precompile account exposes none.
    """
    allocation = fork.pre_allocation_blockchain()
    storage = Storage()
    code = Bytecode()
    for address in (
        Spec.RIPEMD160_ADDRESS,
        Spec.MODEXP_ADDRESS,
        Spec.BLAKE2F_ADDRESS,
    ):
        deployed = bytes(allocation[int.from_bytes(address, "big")]["code"])
        code += Op.SSTORE(
            storage.store_next(len(deployed)), Op.EXTCODESIZE(address)
        )
        code += Op.SSTORE(
            storage.store_next(keccak256(deployed)), Op.EXTCODEHASH(address)
        )
    contract = pre.deploy_contract(code=code)
    tx = Transaction(sender=pre.fund_eoa(), to=contract)
    state_test(pre=pre, tx=tx, post={contract: Account(storage=storage)})


def test_ripemd160_equivalence(
    state_test: StateTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    The replacement at `0x03` hashes like the precompile it retires:
    the digest of `b"abc"` right-aligned in one word.
    """
    storage = Storage()
    contract = pre.deploy_contract(
        code=Op.MSTORE(0, int.from_bytes(b"abc".ljust(32, b"\x00"), "big"))
        + call_and_store_word(
            storage,
            int.from_bytes(Spec.RIPEMD160_ADDRESS, "big"),
            3,
            Spec.RIPEMD160_OF_ABC,
        )
    )
    tx = Transaction(sender=pre.fund_eoa(), to=contract)
    state_test(pre=pre, tx=tx, post={contract: Account(storage=storage)})


def test_modexp_equivalence(
    state_test: StateTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    The replacement at `0x05` exponentiates like the precompile it
    retires: `3**5 mod 7` with one-byte operands.
    """
    storage = Storage()
    calldata = (
        (1).to_bytes(32, "big")
        + (1).to_bytes(32, "big")
        + (1).to_bytes(32, "big")
        + b"\x03\x05\x07"
    )
    contract = pre.deploy_contract(
        code=Op.CALLDATACOPY(0, 0, Op.CALLDATASIZE)
        + Op.SSTORE(
            storage.store_next(1),
            Op.CALL(
                address=int.from_bytes(Spec.MODEXP_ADDRESS, "big"),
                args_size=Op.CALLDATASIZE,
            ),
        )
        + Op.RETURNDATACOPY(0x100, 0, Op.RETURNDATASIZE)
        # A one-byte modulus yields a one-byte result: 243 mod 7.
        + Op.SSTORE(storage.store_next(5), Op.SHR(248, Op.MLOAD(0x100)))
    )
    tx = Transaction(sender=pre.fund_eoa(), to=contract, data=calldata)
    state_test(pre=pre, tx=tx, post={contract: Account(storage=storage)})


def test_blake2f_equivalence(
    state_test: StateTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    The replacement at `0x09` compresses like the precompile it
    retires, on the EIP-152 specification vector.
    """
    calldata = bytes(Blake2bInput())
    expected_first_word = int.from_bytes(
        bytes.fromhex(
            "ba80a53f981c4d0d6a2797b69f12f6e94c212f14685ac4b74b12bb6fdbffa2d1"
        ),
        "big",
    )
    storage = Storage()
    contract = pre.deploy_contract(
        code=Op.CALLDATACOPY(0, 0, Op.CALLDATASIZE)
        + call_and_store_word(
            storage,
            int.from_bytes(Spec.BLAKE2F_ADDRESS, "big"),
            len(calldata),
            expected_first_word,
        )
    )
    tx = Transaction(sender=pre.fund_eoa(), to=contract, data=calldata)
    state_test(pre=pre, tx=tx, post={contract: Account(storage=storage)})
