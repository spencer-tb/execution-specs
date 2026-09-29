"""Exercise EIP-8272 activation directly, outside fixture code installs."""

import pytest
from ethereum_types.bytes import Bytes32
from ethereum_types.numeric import U64, U256, Uint

from ethereum.crypto.hash import keccak256
from ethereum.exceptions import InvalidBlock
from ethereum.forks.amsterdam.fork import BlockChain, apply_fork
from ethereum.forks.amsterdam.recent_roots import (
    RECENT_ROOT_ADDRESS,
    RECENT_ROOT_CODE,
    recent_root_entry_hash,
    recent_root_source_id,
    recent_root_storage_key,
)
from ethereum.state import EMPTY_CODE_HASH, Account
from ethereum.state_mpt import (
    State,
    set_account,
    set_storage,
    state_root,
    store_code,
)

from ..amsterdam.eip8272_recent_roots.contract import recent_root_code
from ..amsterdam.eip8272_recent_roots.spec import Spec


@pytest.mark.parametrize("nonce", [None, 0, 1, 7])
def test_recent_root_activation(nonce: int | None) -> None:
    """Preserve balances and higher nonces while installing the candidate."""
    state = State()
    if nonce is not None:
        set_account(
            state,
            RECENT_ROOT_ADDRESS,
            Account(Uint(nonce), U256(42), EMPTY_CODE_HASH),
        )
    chain = BlockChain(blocks=[], state=state, chain_id=U64(1))
    assert apply_fork(chain) is chain
    assert state.get_account_optional(RECENT_ROOT_ADDRESS) == Account(
        Uint(max(nonce or 0, 1)),
        U256(0 if nonce is None else 42),
        keccak256(RECENT_ROOT_CODE),
    )
    assert state.get_code(keccak256(RECENT_ROOT_CODE)) == bytes(
        recent_root_code()
    )


@pytest.mark.parametrize(
    "code,storage", [(True, False), (False, True), (True, True)]
)
def test_recent_root_activation_rejects_occupied_address(
    code: bool, storage: bool
) -> None:
    """Reject occupied parent state before modifying either predeploy."""
    state = State()
    set_account(
        state,
        RECENT_ROOT_ADDRESS,
        Account(
            Uint(7),
            U256(42),
            store_code(state, b"\x00") if code else EMPTY_CODE_HASH,
        ),
    )
    if storage:
        set_storage(state, RECENT_ROOT_ADDRESS, Bytes32(b"\x11" * 32), U256(1))
    before = state_root(state)
    with pytest.raises(
        InvalidBlock, match="recent root address already holds"
    ):
        apply_fork(BlockChain(blocks=[], state=state, chain_id=U64(1)))
    assert state_root(state) == before


def test_recent_root_activation_after_storage_cleared() -> None:
    """Accept an account whose last nonzero storage slot was cleared."""
    state = State()
    set_account(
        state, RECENT_ROOT_ADDRESS, Account(Uint(7), U256(42), EMPTY_CODE_HASH)
    )
    key = Bytes32(b"\x11" * 32)
    set_storage(state, RECENT_ROOT_ADDRESS, key, U256(1))
    set_storage(state, RECENT_ROOT_ADDRESS, key, U256(0))
    apply_fork(BlockChain(blocks=[], state=state, chain_id=U64(1)))
    assert state.get_storage(RECENT_ROOT_ADDRESS, key) == 0


def test_recent_root_spec_vector() -> None:
    """Pin the spec helpers and runtime to the EIP vector and candidate."""
    source = recent_root_source_id(
        type(RECENT_ROOT_ADDRESS)(Spec.VECTOR_SOURCE_ADDRESS),
        Bytes32(Spec.VECTOR_SALT),
    )
    assert source == Spec.VECTOR_SOURCE_ID
    assert (
        recent_root_entry_hash(
            source, U64(Spec.VECTOR_SLOT), Bytes32(Spec.VECTOR_ROOT)
        )
        == Spec.VECTOR_ENTRY_HASH
    )
    assert recent_root_storage_key(source, U64(Spec.VECTOR_SLOT)) == (
        Spec.VECTOR_STORAGE_KEY
    )
    assert (
        RECENT_ROOT_CODE == Spec.RECENT_ROOT_CODE == bytes(recent_root_code())
    )
    assert keccak256(RECENT_ROOT_CODE).hex() == (
        "92581be6144206cc1ba9f655324d74f0a49f20661ff2d31975aefb2449884342"
    )
