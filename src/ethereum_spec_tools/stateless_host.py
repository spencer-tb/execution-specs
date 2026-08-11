"""
Fork generic host side drivers for stateless validation.

Building an execution witness and packaging a stateless input is the
same procedure for every fork: collect what the tracker recorded,
traverse the pre state tries, assemble the payload from the fork's own
types and serialize through the fork's codec. This module implements
that procedure once. The fork supplies its shapes and codecs through
[`ForkLoad`], so the payload field list is introspected from the fork's
own `ExecutionPayload` dataclass rather than enumerated here.

[`ForkLoad`]: ref:ethereum_spec_tools.evm_tools.loaders.fork_loader.ForkLoad
"""

import dataclasses
from typing import Any, Dict, List, Optional, Set, Tuple

from ethereum_rlp import rlp
from ethereum_types.bytes import Bytes, Bytes32
from ethereum_types.numeric import U64, U256, Uint

from ethereum.crypto.hash import Hash32, keccak256
from ethereum.exceptions import InvalidSignatureError
from ethereum.incremental_mpt import (
    IncrementalMPT,
    build_mpt,
    mpt_get,
    mpt_root,
    mpt_set,
)
from ethereum.merkle_patricia_trie import EMPTY_TRIE_ROOT, Trie
from ethereum.state import Account, Address, PreState, Root

from .evm_tools.loaders.fork_loader import ForkLoad

# Engine API names differ from the spec's header field names by a fixed
# set of renames, stable since the merge.
_PAYLOAD_FIELD_SOURCES = {
    "fee_recipient": "coinbase",
    "receipts_root": "receipt_root",
    "logs_bloom": "bloom",
}


def serialize_stateless_input(load: ForkLoad, stateless_input: Any) -> Bytes:
    """Serialize a stateless input to schema prefixed SSZ bytes."""
    ssz = load.stateless_ssz_module
    ssz_obj = ssz.stateless_input_to_ssz(stateless_input)
    return Bytes(
        bytes(ssz.STATELESS_INPUT_SCHEMA_ID_BYTES)
        + bytes(ssz_obj.encode_bytes())
    )


def deserialize_stateless_output(load: ForkLoad, data: Bytes) -> Any:
    """Deserialize a stateless validation result from SSZ bytes."""
    ssz = load.stateless_ssz_module
    ssz_obj = ssz.SSZStatelessValidationResult.decode_bytes(data)
    return ssz.ssz_to_validation_result(ssz_obj)


def build_stateless_input(
    load: ForkLoad,
    block: Any,
    *,
    execution_witness: Any,
    execution_requests: Any,
    block_access_list: Any,
    chain_id: U64,
) -> Any:
    """
    Build a stateless input from a completed block.

    Extract the header, transactions and withdrawals from the block,
    compute the block hash, collect versioned hashes and package
    everything into the fork's stateless input. The payload fields are
    introspected from the fork's `ExecutionPayload` dataclass, so a fork
    that adds or removes header fields needs no change here.
    """
    transactions = load.transactions_module
    header = block.header
    block_hash = Hash32(keccak256(rlp.encode(header)))

    # Encode transactions to bytes, recover public keys, and collect
    # versioned hashes.
    tx_bytes_list: List[Bytes] = []
    public_keys: List[Bytes] = []
    versioned_hashes: List[Any] = []
    for tx in block.transactions:
        if isinstance(tx, transactions.LegacyTransaction):
            tx_bytes_list.append(Bytes(rlp.encode(tx)))
            tx_obj = tx
        else:
            tx_bytes_list.append(Bytes(tx))
            # A typed tx may be malformed (pre-execution-rejected by
            # t8n but still committed to by the block's transactions
            # trie).
            try:
                tx_obj = transactions.decode_transaction(tx)
            except Exception:
                continue
        try:
            public_keys.append(
                transactions.recover_transaction_public_key(chain_id, tx_obj)
            )
        except InvalidSignatureError:
            # Rejected transactions remain in invalid payloads passed to
            # the guest, but cannot provide a recoverable public key.
            continue
        if hasattr(tx_obj, "blob_versioned_hashes"):
            versioned_hashes.extend(tx_obj.blob_versioned_hashes)

    payload_type = load.execution_payload_type
    computed = {
        "block_hash": block_hash,
        "transactions": tuple(tx_bytes_list),
        "withdrawals": block.withdrawals,
        "block_access_list": Bytes(rlp.encode(block_access_list)),
    }
    payload_kwargs = {}
    for field in dataclasses.fields(payload_type):
        if field.name in computed:
            payload_kwargs[field.name] = computed[field.name]
        else:
            source = _PAYLOAD_FIELD_SOURCES.get(field.name, field.name)
            payload_kwargs[field.name] = getattr(header, source)
    payload = payload_type(**payload_kwargs)

    new_payload = load.new_payload_request_type(
        execution_payload=payload,
        versioned_hashes=tuple(versioned_hashes),
        parent_beacon_block_root=header.parent_beacon_block_root,
        execution_requests=execution_requests,
    )

    return load.stateless_input_type(
        new_payload_request=new_payload,
        witness=execution_witness,
        chain_id=chain_id,
        public_keys=tuple(public_keys),
    )


def _build_pre_state_storage_mpts(
    pre_state_storages_data: Dict[Address, Trie[Bytes32, U256]],
) -> Dict[Address, IncrementalMPT[Bytes32, U256]]:
    """Build incremental storage MPTs from pre-state flat storage data."""
    incr_storage_mpts: Dict[Address, IncrementalMPT[Bytes32, U256]] = {}
    for address, data in pre_state_storages_data.items():
        incr_storage_mpts[address] = build_mpt(
            data._data, secured=True, default=U256(0)
        )
    return incr_storage_mpts


def _build_pre_state_account_mpt(
    pre_state_accounts_data: Trie[Address, Optional[Account]],
    incr_storage_mpts: Dict[Address, IncrementalMPT[Bytes32, U256]],
) -> IncrementalMPT[Address, Optional[Account]]:
    """Build the incremental account MPT from pre-state flat account data."""

    def get_pre_storage_root(address: Address) -> Root:
        if address in incr_storage_mpts:
            return mpt_root(incr_storage_mpts[address])
        return EMPTY_TRIE_ROOT

    return build_mpt(
        pre_state_accounts_data._data,
        secured=True,
        default=None,
        get_storage_root=get_pre_storage_root,
    )


def _collect_storage_accesses(
    block_state: Any,
) -> Dict[Address, Set[Bytes32]]:
    """
    Collect all storage keys that must be traversed on pre-state tries.

    Includes both reads and writes so all needed pre-state nodes are
    captured before in-place mutation.
    """
    all_storage_accesses: Dict[Address, Set[Bytes32]] = {}
    for address, key in block_state.storage_reads:
        all_storage_accesses.setdefault(address, set()).add(key)
    for address, slots in block_state.storage_writes.items():
        all_storage_accesses.setdefault(address, set()).update(slots)
    return all_storage_accesses


def _capture_pre_state_storage_nodes(
    incr_storage_mpts: Dict[Address, IncrementalMPT[Bytes32, U256]],
    all_storage_accesses: Dict[Address, Set[Bytes32]],
) -> None:
    """Traverse pre-state storage tries to record witness nodes."""
    for address, keys in all_storage_accesses.items():
        if address not in incr_storage_mpts:
            continue
        for key in keys:
            mpt_get(incr_storage_mpts[address], key)


def _apply_storage_writes(
    incr_storage_mpts: Dict[Address, IncrementalMPT[Bytes32, U256]],
    storage_writes: Dict[Address, Dict[Bytes32, U256]],
) -> None:
    """Apply block storage writes to incremental storage MPTs."""
    for address, dirty_keys in storage_writes.items():
        if address not in incr_storage_mpts:
            # New storage created during block.
            incr_storage_mpts[address] = build_mpt(
                {}, secured=True, default=U256(0)
            )

        # Two passes: insert/update first, deletions second.
        for key, value in dirty_keys.items():
            if value != 0:
                mpt_set(incr_storage_mpts[address], key, value)
        for key, value in dirty_keys.items():
            if value == 0:
                mpt_set(incr_storage_mpts[address], key, value)


def _get_all_dirty_accounts(block_state: Any) -> Set[Address]:
    """Return addresses whose account leaf may change in the state trie."""
    return set(block_state.account_writes.keys()) | set(
        block_state.storage_writes.keys()
    )


def _capture_pre_state_account_nodes(
    incr_account_mpt: IncrementalMPT[Address, Optional[Account]],
    account_reads: Set[Address],
    all_dirty_accounts: Set[Address],
) -> None:
    """Traverse pre-state account trie to record witness nodes."""
    for address in account_reads | all_dirty_accounts:
        mpt_get(incr_account_mpt, address)


def _apply_account_writes(
    incr_account_mpt: IncrementalMPT[Address, Optional[Account]],
    incr_storage_mpts: Dict[Address, IncrementalMPT[Bytes32, U256]],
    block_state: Any,
    all_dirty_accounts: Set[Address],
) -> None:
    """Apply final account values and post-storage roots to account trie."""
    for address in all_dirty_accounts:
        if address in block_state.account_writes:
            account = block_state.account_writes[address]
        else:
            account = block_state.pre_state.get_account_optional(address)

        if address in incr_storage_mpts:
            addr_storage_root = mpt_root(incr_storage_mpts[address])
        else:
            addr_storage_root = EMPTY_TRIE_ROOT

        def get_storage_root_fn(
            _: Address, sr: Root = addr_storage_root
        ) -> Root:
            return sr

        mpt_set(
            incr_account_mpt,
            address,
            account,
            get_storage_root=get_storage_root_fn,
        )


def _collect_accessed_nodes(
    incr_account_mpt: IncrementalMPT[Address, Optional[Account]],
    incr_storage_mpts: Dict[Address, IncrementalMPT[Bytes32, U256]],
) -> Dict[Bytes, Bytes]:
    """Merge accessed trie nodes from account and storage witnesses."""
    accessed_nodes = dict(incr_account_mpt.witness.accessed_nodes)
    for mpt in incr_storage_mpts.values():
        accessed_nodes.update(mpt.witness.accessed_nodes)
    return accessed_nodes


def build_execution_witness(
    load: ForkLoad,
    block_state: Any,
    expected_post_state_root: Root,
    pre_state_accounts_data: Trie[Address, Optional[Account]],
    pre_state_storages_data: Dict[Address, Trie[Bytes32, U256]],
    blockchain_headers: Optional[List[Bytes]] = None,
) -> Any:
    """
    Build the execution witness from block state and pre-state trie data.

    Sort state and codes in lexicographic ascending order, headers by
    block number ascending. What counts as an access is defined by the
    fork's recording hooks, this function only collects what the tracker
    recorded.
    """
    ancestor_headers = get_witness_ancestors(
        blockchain_headers if blockchain_headers is not None else [],
        block_state.oldest_ancestor_offset,
    )
    codes = get_witness_codes(block_state.code_reads, block_state.pre_state)

    # Build account and storage IncrementalMPTs from pre-state flat data.
    incr_storage_mpts = _build_pre_state_storage_mpts(pre_state_storages_data)
    incr_account_mpt = _build_pre_state_account_mpt(
        pre_state_accounts_data, incr_storage_mpts
    )

    # 1. Traverse all accessed and dirty storage keys on the pre-state
    # MPTs to capture pre-state trie nodes in the witness. This must
    # happen before any writes since writes mutate the tree in-place.
    all_storage_accesses = _collect_storage_accesses(block_state)
    _capture_pre_state_storage_nodes(incr_storage_mpts, all_storage_accesses)

    # 2. Apply dirty storage to storages (writes)
    _apply_storage_writes(incr_storage_mpts, block_state.storage_writes)

    # Accounts are "dirty" if:
    # - Account fields changed (nonce/balance/code)
    # - Storage changed (storage root changed)
    all_dirty_accounts = _get_all_dirty_accounts(block_state)

    # 3. Traverse all accessed and dirty accounts on the pre-state MPT
    # to capture pre-state trie nodes before writes mutate the tree.
    _capture_pre_state_account_nodes(
        incr_account_mpt,
        block_state.account_reads,
        all_dirty_accounts,
    )

    # 4. Apply dirty accounts
    _apply_account_writes(
        incr_account_mpt,
        incr_storage_mpts,
        block_state,
        all_dirty_accounts,
    )

    # Safety check: the post-state root implied by the witness
    # construction must match the canonical state-root calculation.
    assert mpt_root(incr_account_mpt) == expected_post_state_root

    # Collect witness from all MPTs
    accessed_nodes = _collect_accessed_nodes(
        incr_account_mpt, incr_storage_mpts
    )

    return load.execution_witness_type(
        state=tuple(sorted(accessed_nodes.values())),
        codes=tuple(codes),
        headers=tuple(ancestor_headers),
    )


def get_witness_codes(
    code_reads: Set[Tuple[Address, Hash32]],
    pre_state: PreState,
) -> List[Bytes]:
    """
    Collect bytecodes from the pre-state for all code reads during
    execution.

    Include a code hash only when the same address already had that code
    in the pre-state. This avoids accidentally including bytecode created
    during the current block when the same hash already exists elsewhere.
    """
    witness_code_hashes: Set[Hash32] = set()
    for address, code_hash in code_reads:
        pre_account = pre_state.get_account_optional(address)
        if pre_account is None or pre_account.code_hash != code_hash:
            continue
        witness_code_hashes.add(code_hash)

    codes: List[Bytes] = []
    for code_hash in witness_code_hashes:
        try:
            codes.append(pre_state.get_code(code_hash))
        except KeyError:
            pass
    return sorted(codes)


def get_witness_ancestors(
    block_headers: List[Bytes],
    oldest_ancestor_offset: Optional[Uint],
) -> List[Bytes]:
    """
    Collect RLP encoded ancestor headers from ``oldest_ancestor_offset``
    blocks back onward.
    """
    if oldest_ancestor_offset is None:
        return []
    return list(block_headers[-int(oldest_ancestor_offset) :])
