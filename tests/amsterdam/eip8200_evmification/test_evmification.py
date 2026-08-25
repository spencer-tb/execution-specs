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


def test_modexp_legacy_minimum_gas_no_longer_sufficient(
    state_test: StateTestFiller, pre: Alloc
) -> None:
    """
    Pin a compatibility boundary caused by ordinary EVM pricing.

    The one-byte ``3**5 mod 7`` input costs the retired MODEXP
    precompile's 500-gas minimum, but the candidate replacement needs
    more: a call forwarding 500 gas fails while a generously funded
    call succeeds and returns the equivalent result.
    """
    calldata = (
        (1).to_bytes(32, "big")
        + (1).to_bytes(32, "big")
        + (1).to_bytes(32, "big")
        + b"\x03\x05\x07"
    )
    target = int.from_bytes(Spec.MODEXP_ADDRESS, "big")
    storage = Storage()
    contract = pre.deploy_contract(
        code=Op.CALLDATACOPY(0, 0, Op.CALLDATASIZE)
        + Op.SSTORE(
            storage.store_next(0),
            Op.CALL(gas=500, address=target, args_size=Op.CALLDATASIZE),
        )
        + Op.SSTORE(
            storage.store_next(1),
            Op.CALL(gas=100_000, address=target, args_size=Op.CALLDATASIZE),
        )
        + Op.RETURNDATACOPY(0x100, 0, Op.RETURNDATASIZE)
        + Op.SSTORE(storage.store_next(5), Op.SHR(248, Op.MLOAD(0x100)))
    )
    tx = Transaction(
        sender=pre.fund_eoa(), to=contract, data=calldata, gas_limit=1_000_000
    )
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


@pytest.mark.parametrize(
    "retired_address",
    [
        pytest.param(Spec.RIPEMD160_ADDRESS, id="ripemd160"),
        pytest.param(Spec.MODEXP_ADDRESS, id="modexp"),
        pytest.param(Spec.BLAKE2F_ADDRESS, id="blake2f"),
    ],
)
def test_retired_addresses_not_prewarm(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    retired_address: bytes,
) -> None:
    """
    The retired addresses leave the precompile warm set: the first call
    in a transaction pays the cold account access surcharge that the
    precompile never paid.
    """
    gas_costs = fork.gas_costs()
    surcharge = gas_costs.COLD_ACCOUNT_ACCESS - gas_costs.WARM_ACCESS
    target = int.from_bytes(retired_address, "big")
    storage = Storage()
    measure = Bytecode()
    for slot in (0x00, 0x20, 0x40):
        measure += Op.MSTORE(slot, Op.GAS)
        measure += Op.POP(Op.CALL(gas=100_000, address=target, args_size=0))
    contract = pre.deploy_contract(
        code=Op.MSTORE(0x40, 0)
        + measure
        + Op.SSTORE(
            storage.store_next(surcharge),
            Op.SUB(
                Op.SUB(Op.MLOAD(0x00), Op.MLOAD(0x20)),
                Op.SUB(Op.MLOAD(0x20), Op.MLOAD(0x40)),
            ),
        )
    )
    tx = Transaction(sender=pre.fund_eoa(), to=contract, gas_limit=1_000_000)
    state_test(pre=pre, tx=tx, post={contract: Account(storage=storage)})


def test_blake2f_invalid_length_returndata(
    state_test: StateTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    Pin the candidate bytecode's invalid input handling at `0x09`.

    The replacement rejects a truncated input like the precompile it
    retires, but reverts with an `Error(string)` payload where the
    precompile returned empty revert data. This pins candidate
    artifact behavior that diverges from the EIP's equivalence claim
    and must flip when the bytecode is fixed.
    """
    calldata = bytes(Blake2bInput())[:-1]
    storage = Storage()
    contract = pre.deploy_contract(
        code=Op.CALLDATACOPY(0, 0, Op.CALLDATASIZE)
        + Op.SSTORE(
            storage.store_next(0),
            Op.CALL(
                gas=100_000,
                address=int.from_bytes(Spec.BLAKE2F_ADDRESS, "big"),
                args_size=Op.CALLDATASIZE,
            ),
        )
        # 4 selector + 32 offset + 32 length + 32 padded message bytes.
        + Op.SSTORE(storage.store_next(100), Op.RETURNDATASIZE)
        + Op.RETURNDATACOPY(0x100, 0, 4)
        + Op.SSTORE(
            storage.store_next(0x08C379A0), Op.SHR(224, Op.MLOAD(0x100))
        )
    )
    tx = Transaction(
        sender=pre.fund_eoa(), to=contract, data=calldata, gas_limit=1_000_000
    )
    state_test(pre=pre, tx=tx, post={contract: Account(storage=storage)})


def test_blake2f_invalid_flag_accepted(
    state_test: StateTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    Pin the candidate bytecode's final block flag handling at `0x09`.

    EIP-152 requires rejecting any flag other than 0 or 1, and the
    retired precompile did. The candidate bytecode accepts `f = 2`.
    This pins the consensus divergence in the candidate artifact and
    must flip to a rejection when the bytecode is fixed.
    """
    calldata = bytes(Blake2bInput(f=2))
    # The candidate treats any nonzero flag as final: the output is
    # the valid final block digest of the EIP-152 vector.
    final_digest_first_word = int.from_bytes(
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
            final_digest_first_word,
        )
    )
    tx = Transaction(
        sender=pre.fund_eoa(), to=contract, data=calldata, gas_limit=1_000_000
    )
    state_test(pre=pre, tx=tx, post={contract: Account(storage=storage)})
