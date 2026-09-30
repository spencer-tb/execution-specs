"""Exercise EIP-8250 activation directly, outside fixture code installs."""

import pytest
from ethereum_types.bytes import Bytes, Bytes32
from ethereum_types.numeric import U64, U256, Uint

from ethereum.crypto.hash import keccak256
from ethereum.exceptions import InvalidBlock
from ethereum.forks.amsterdam.fork import BlockChain, apply_fork
from ethereum.forks.amsterdam.transactions.frame_transaction import (
    EXPIRY_VERIFIER,
    EXPIRY_VERIFIER_CODE,
    NONCE_MANAGER,
    NONCE_MANAGER_CODE,
)
from ethereum.merkle_patricia_trie import EMPTY_TRIE_ROOT
from ethereum.state import EMPTY_CODE_HASH, Account
from ethereum.state_mpt import (
    State,
    set_account,
    set_storage,
    state_root,
    storage_root,
    store_code,
)

from ..amsterdam.eip8250_keyed_nonces.spec import Spec


@pytest.mark.parametrize(
    "nonce,balance",
    [
        pytest.param(None, None, id="absent"),
        pytest.param(0, 42, id="balance_only"),
        pytest.param(7, 42, id="nonce_above_one"),
    ],
)
def test_nonce_manager_activation(
    nonce: int | None, balance: int | None
) -> None:
    """Install the code, raise the nonce to one and keep the balance."""
    state = State()
    if nonce is not None and balance is not None:
        set_account(
            state,
            NONCE_MANAGER,
            Account(Uint(nonce), U256(balance), EMPTY_CODE_HASH),
        )
    chain = BlockChain(blocks=[], state=state, chain_id=U64(1))
    assert apply_fork(chain) is chain
    assert state.get_account_optional(NONCE_MANAGER) == Account(
        Uint(max(nonce or 0, Spec.NONCE_MANAGER_NONCE)),
        U256(balance or 0),
        keccak256(NONCE_MANAGER_CODE),
    )
    assert state.get_code(keccak256(NONCE_MANAGER_CODE)) == (
        Spec.NONCE_MANAGER_CODE
    )
    assert storage_root(state, NONCE_MANAGER) == EMPTY_TRIE_ROOT


@pytest.mark.parametrize(
    "code,storage",
    [
        pytest.param(NONCE_MANAGER_CODE, False, id="nonce_manager_code"),
        pytest.param(Bytes(b"\x00"), False, id="foreign_code"),
        pytest.param(None, True, id="storage_without_code"),
        pytest.param(Bytes(b"\x00"), True, id="foreign_code_and_storage"),
    ],
)
def test_nonce_manager_activation_rejects_occupied_address(
    code: Bytes | None, storage: bool
) -> None:
    """Reject occupied parent state before modifying either predeploy."""
    state = State()
    set_account(
        state,
        NONCE_MANAGER,
        Account(
            Uint(7),
            U256(42),
            EMPTY_CODE_HASH if code is None else store_code(state, code),
        ),
    )
    if storage:
        set_storage(state, NONCE_MANAGER, Bytes32(b"\x11" * 32), U256(1))
    nonce_manager = state.get_account_optional(NONCE_MANAGER)
    before = state_root(state)
    with pytest.raises(
        InvalidBlock, match="nonce manager address already holds"
    ):
        apply_fork(BlockChain(blocks=[], state=state, chain_id=U64(1)))
    assert state_root(state) == before
    assert state.get_account_optional(NONCE_MANAGER) == nonce_manager
    assert state.get_account_optional(EXPIRY_VERIFIER) is None


def test_nonce_manager_activation_after_storage_cleared() -> None:
    """Accept an account whose last nonzero storage slot was cleared."""
    state = State()
    set_account(
        state, NONCE_MANAGER, Account(Uint(7), U256(42), EMPTY_CODE_HASH)
    )
    key = Bytes32(b"\x11" * 32)
    set_storage(state, NONCE_MANAGER, key, U256(1))
    set_storage(state, NONCE_MANAGER, key, U256(0))
    apply_fork(BlockChain(blocks=[], state=state, chain_id=U64(1)))
    assert state.get_account_optional(NONCE_MANAGER) == Account(
        Uint(7), U256(42), keccak256(NONCE_MANAGER_CODE)
    )
    assert state.get_storage(NONCE_MANAGER, key) == 0
    expiry_verifier = state.get_account_optional(EXPIRY_VERIFIER)
    assert expiry_verifier is not None
    assert expiry_verifier.code_hash == keccak256(EXPIRY_VERIFIER_CODE)
