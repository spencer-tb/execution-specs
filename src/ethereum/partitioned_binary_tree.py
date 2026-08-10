"""
The [EIP-8297] Partitioned Binary Tree: a single authenticated
key/value tree holding all of Ethereum state.

The raw tree is a compressed binary radix trie mapping
variable-length keys to 32-byte values, committing to its entire
contents with one root hash. Keys are consumed bit by bit, most
significant bit first, and must be prefix-free; see [`Key`]. The
mapping of keys to values is exposed through [`BinaryTrie`], and the
[`root`] function reduces a tree to its 32-byte commitment. The hash
function follows the EIP's reference implementation (BLAKE3).

The rest of the module defines the _embedding_: how accounts,
storage slots, and code chunks are assigned keys and packed into
values, merging the account and storage tries of the Merkle-Patricia
design into this one tree. State is written through
[`embed_account`] and [`embed_storage_slot`] and removed through
[`remove_account`], [`remove_storage_slot`][rss], and
[`remove_code_chunks`], all built on the raw tree operations.

The first byte of every key is a **zone** identifier labeling the
category of state the key holds: account headers live in
[`ACCOUNT_ZONE`], content-addressed code in [`CODE_ZONE`], and
overflow storage in [`STORAGE_ZONE`]. Keys are variable length, but
every key of a zone has the same length, keeping keys prefix-free as
the tree requires.

A key's **stem** is every byte except its final sub-index byte. Keys
sharing a stem form one group of up to [`STEM_SUBTREE_WIDTH`]
co-located values, all reachable through the same branch of the
tree. This keeps data that is accessed together cheap to prove: an
account's header stem holds its basic data, its code hash or its
delegation, and its first storage slots, so one proof path covers
them all.

Code is not keyed by account at all: every chunk lives in
[`CODE_ZONE`], content-addressed by code hash, so contracts with
identical bytecode share their chunk leaves. Overflow storage and
code are co-located at coarser granularity: aligned groups of up to
[`STEM_SUBTREE_WIDTH`] consecutive slots or chunks share a stem, so
neighboring values are still proved through one shared path rather
than one path each.

[EIP-8297]: https://eips.ethereum.org/EIPS/eip-8297
[`Key`]: ref:ethereum.partitioned_binary_tree.Key
[`BinaryTrie`]: ref:ethereum.partitioned_binary_tree.BinaryTrie
[`root`]: ref:ethereum.partitioned_binary_tree.root
[`ACCOUNT_ZONE`]: ref:ethereum.partitioned_binary_tree.ACCOUNT_ZONE
[`CODE_ZONE`]: ref:ethereum.partitioned_binary_tree.CODE_ZONE
[`STORAGE_ZONE`]: ref:ethereum.partitioned_binary_tree.STORAGE_ZONE
[`STEM_SUBTREE_WIDTH`]: ref:ethereum.partitioned_binary_tree.STEM_SUBTREE_WIDTH
[`embed_account`]: ref:ethereum.partitioned_binary_tree.embed_account
[`embed_storage_slot`]: ref:ethereum.partitioned_binary_tree.embed_storage_slot
[`remove_account`]: ref:ethereum.partitioned_binary_tree.remove_account
[rss]: ref:ethereum.partitioned_binary_tree.remove_storage_slot
[`remove_code_chunks`]: ref:ethereum.partitioned_binary_tree.remove_code_chunks
"""

import copy
from dataclasses import dataclass, field
from typing import Dict, List, Mapping, Optional, Union, final

from blake3 import blake3
from ethereum_types.bytes import Bytes, Bytes20, Bytes32
from ethereum_types.frozen import slotted_freezable
from ethereum_types.numeric import U8, U32, U64, U256, Uint

from ethereum.crypto.hash import Hash32, keccak256
from ethereum.exceptions import BalanceOverflowError
from ethereum.utils.byte import left_pad_zero_bytes, right_pad_zero_bytes

EMPTY_TRIE_ROOT = Hash32(b"\x00" * 32)
"""
Root hash of an empty binary tree, defined as 32 zero bytes.

This is a sentinel value rather than a hash output: no input is
expected to hash to all zeroes, so it cannot collide with the
commitment of a non-empty tree.
"""


def blake3_hash(data: Bytes) -> Hash32:
    """
    Hash `data` with the tree's hash function.
    """
    return Hash32(blake3(data).digest())


def bytes_to_bit_list(data: Bytes) -> Bytes:
    """
    Expand each input byte into eight bits, most significant bit first.
    """
    return Bytes(
        bytearray(
            (byte >> (7 - offset)) & 1 for byte in data for offset in range(8)
        )
    )


Key = Bytes
"""
A tree key is any non-empty byte string, consumed bit by bit, MSB first.

Keys must be **prefix-free**, so no key may be a prefix of another. A
key is its path and a [`LeafNode`] ends a path, so a longer key
could never pass through the position a shorter key terminates at.

[`LeafNode`]: ref:ethereum.partitioned_binary_tree.LeafNode
"""

MAX_KEY_LENGTH = Uint(8192)
"""
Longest key the tree accepts, in bytes.

The bound is derived from the prefix encoding algorithm: a branch prefix can
approach the full bit length of the keys sharing it, and
[`encode_bit_prefix`] stores the bit count in two bytes, so keys
longer than this could produce a prefix the encoding cannot
represent. That bound is the worst case and longer keys often
encode fine, but enforcing it on every key in [`trie_set`] keeps
the limit a stated contract instead of a data-dependent failure
during merkleization.

[`encode_bit_prefix`]: ref:ethereum.partitioned_binary_tree.encode_bit_prefix
[`trie_set`]: ref:ethereum.partitioned_binary_tree.trie_set
"""

LEAF_NODE_TAG = Bytes(b"\x00")
"""
First byte of every [`LeafNode`] hash preimage.

This is needed so that two different nodes can never share a
preimage (since their first byte will always differ).

See [`merkleize`] for usage.

[`LeafNode`]: ref:ethereum.partitioned_binary_tree.LeafNode
[`merkleize`]: ref:ethereum.partitioned_binary_tree.merkleize
"""

BRANCH_NODE_TAG = Bytes(b"\x01")
"""
First byte of every [`BranchNode`] hash preimage.

[`BranchNode`]: ref:ethereum.partitioned_binary_tree.BranchNode
"""


@final
@slotted_freezable
@dataclass
class LeafNode:
    """
    Terminal node holding a single key's value.

    Note: the complete key is committed, not just the bits below the
    leaf's position, so a leaf's meaning never depends on the path
    taken to reach it.
    """

    key: Key
    """
    The complete key whose value this leaf holds.
    """

    value: Bytes32
    """
    The 32-byte value stored under [`key`].

    [`key`]: ref:ethereum.partitioned_binary_tree.LeafNode.key
    """


@final
@slotted_freezable
@dataclass
class BranchNode:
    """
    Binary branch splitting on a single bit, carrying the run of bits
    every key below it shares beyond the bits consumed above it.

    This inlines the Merkle Patricia Trie's extension-node concept
    into the branch itself.
    """

    prefix: Bytes
    """
    The compressed run of bits shared by every key below this branch,
    one bit per byte, in consumption order.
    This is empty when the keys diverge immediately.

    Like the MPT, the run is relative: it holds only the bits between the
    parent's split point and this branch's split bit, never the path
    from the root, which is reconstructed by the walk down.
    """

    left: "BinaryNode"
    """
    Subtree of keys whose bit after [`prefix`] is `0`.

    [`prefix`]: ref:ethereum.partitioned_binary_tree.BranchNode.prefix
    """

    right: "BinaryNode"
    """
    Subtree of keys whose bit after [`prefix`] is `1`.

    [`prefix`]: ref:ethereum.partitioned_binary_tree.BranchNode.prefix
    """


BinaryNode = Union[BranchNode, LeafNode]
"""
Either of the node types making up a non-empty binary tree.
"""


@final
@dataclass
class BinaryTrie:
    """
    Mapping of variable-length keys to 32-byte values with a single
    root hash that cryptographically commits to the mapping.

    Only the key/value pairs are stored; [`root`] rebuilds the node
    structure and rehashes it from scratch on every call, which makes
    the canonical compressed form automatic rather than a rule the
    caller must maintain.

    A production client would instead keep the tree's nodes in
    memory between calls and recompute only the hashes along the
    path to a changed key; this reference implementation rebuilds
    everything each time for readability.

    [`root`]: ref:ethereum.partitioned_binary_tree.root
    """

    _data: Dict[Key, Bytes32] = field(default_factory=dict)


def copy_trie(trie: BinaryTrie) -> BinaryTrie:
    """
    Create a copy of `trie`.

    Keys and values are immutable, so the contents are shared between
    the original and the copy.
    """
    return BinaryTrie(copy.copy(trie._data))


def trie_set(trie: BinaryTrie, key: Key, value: Optional[Bytes32]) -> None:
    """
    Insert or update `key` in `trie` with the given `value`; setting
    `None` removes the key, and removing an absent key does nothing.

    `None` can mark absence because it lies outside the value space:
    every 32-byte value, including all zeroes, is a legitimate leaf,
    so no stored value could play the role the Merkle Patricia
    Trie's default value does. The same convention marks deleted
    accounts in [`BlockDiff`], and mirrors [`trie_get`], which
    returns `None` for absent keys.

    Since [`root`] rebuilds the node structure from the surviving
    entries, a removal needs no node surgery here: branches held
    open by the removed key simply never form, and the trie commits
    as if the key had never been inserted.

    The caller must keep keys prefix-free; see [`Key`].

    [`Key`]: ref:ethereum.partitioned_binary_tree.Key
    [`root`]: ref:ethereum.partitioned_binary_tree.root
    [`BlockDiff`]: ref:ethereum.state.BlockDiff
    """
    assert (
        len(key) >= 1
    )  # Reject the empty key since it is a prefix of every other key
    assert Uint(len(key)) <= MAX_KEY_LENGTH
    if value is None:
        trie._data.pop(key, None)
        return
    # `Bytes32` already rejects other lengths; asserted anyway, as in
    # `root`, to keep the EIP's explicit validation visible.
    assert len(value) == 32
    trie._data[key] = value


def trie_get(trie: BinaryTrie, key: Key) -> Optional[Bytes32]:
    """
    Look up `key` in `trie`, returning `None` if absent.
    """
    return trie._data.get(key)


def remove_subtree(trie: BinaryTrie, prefix: Bytes) -> None:
    """
    Remove every key of `trie` beginning with `prefix`; a prefix
    matching nothing does nothing.

    Keys are consumed most significant bit first, so the keys sharing
    a `prefix` are exactly the keys of one subtree, and this removes
    that subtree whole. Callers reach for it when the set of keys to
    remove is known by where it sits in the tree rather than by
    enumeration; see [`remove_account`], which drops an account's
    unbounded storage without being told which slots it holds.

    A production client would unlink the subtree's node from its
    parent and be done, which is why this is a tree operation and not
    a loop of removals; the scan here follows [`BinaryTrie`] storing
    only key/value pairs.

    [`remove_account`]: ref:ethereum.partitioned_binary_tree.remove_account
    [`BinaryTrie`]: ref:ethereum.partitioned_binary_tree.BinaryTrie
    """
    for key in [key for key in trie._data if key.startswith(prefix)]:
        del trie._data[key]


def encode_bit_prefix(prefix: Bytes) -> Bytes:
    """
    Encode a branch prefix: a two-byte big-endian bit
    count followed by the bits packed most significant bit first,
    zero padded to a byte boundary.

    The explicit bit count keeps the encoding injective. Without it, two
    prefixes differing only by trailing zero bits would pack to the
    same bytes and two different trees could share a root.

    Two bytes are enough because a prefix cannot outgrow the bit length
    of the keys sharing it, and [`trie_set`] bounds every key at
    [`MAX_KEY_LENGTH`].

    [`trie_set`]: ref:ethereum.partitioned_binary_tree.trie_set
    [`MAX_KEY_LENGTH`]: ref:ethereum.partitioned_binary_tree.MAX_KEY_LENGTH
    """
    assert len(prefix) < 2**16
    packed = bytearray((len(prefix) + 7) // 8)
    for bit_index, bit in enumerate(prefix):
        packed[bit_index // 8] |= bit << (7 - bit_index % 8)
    return Bytes(len(prefix).to_bytes(2, "big") + bytes(packed))


def merkleize(node: BinaryNode) -> Hash32:
    """
    Compute the hash committing to `node` and everything below it.
    """
    if isinstance(node, LeafNode):
        return blake3_hash(LEAF_NODE_TAG + node.key + node.value)
    return blake3_hash(
        BRANCH_NODE_TAG
        + encode_bit_prefix(node.prefix)
        + merkleize(node.left)
        + merkleize(node.right)
    )


def binarize(entries: Mapping[Key, Bytes32], depth: Uint) -> BinaryNode:
    """
    Build the canonical node structure for `entries`, whose keys all
    share their first `depth` bits. `entries` must not be empty.

    A single entry becomes a [`LeafNode`] immediately. Multiple
    entries become a [`BranchNode`] carrying the run of bits they
    share beyond `depth` and splitting on the first bit where they
    differ.

    [`LeafNode`]: ref:ethereum.partitioned_binary_tree.LeafNode
    [`BranchNode`]: ref:ethereum.partitioned_binary_tree.BranchNode
    """
    assert len(entries) > 0
    if len(entries) == 1:
        ((key, value),) = entries.items()
        return LeafNode(key, value)

    bit_lists = {key: bytes_to_bit_list(key) for key in entries}

    split = depth
    while True:
        # A key running out of bits while still grouped with others
        # would be a prefix of theirs; see `Key`.
        for bit_list in bit_lists.values():
            assert split < Uint(len(bit_list))
        distinct_bits_at_split = {
            bit_list[split] for bit_list in bit_lists.values()
        }
        if len(distinct_bits_at_split) > 1:
            break
        split += Uint(1)

    left = {
        key: value
        for key, value in entries.items()
        if bit_lists[key][split] == 0
    }
    right = {
        key: value
        for key, value in entries.items()
        if bit_lists[key][split] == 1
    }
    shared_bits = next(iter(bit_lists.values()))
    return BranchNode(
        Bytes(shared_bits[depth:split]),
        binarize(left, split + Uint(1)),
        binarize(right, split + Uint(1)),
    )


def root(trie: BinaryTrie) -> Hash32:
    """
    Compute the root hash of `trie`.

    An empty trie commits to [`EMPTY_TRIE_ROOT`]; any other trie
    commits to the hash of its canonical node structure.

    Every entry is validated before hashing, as in the EIP's
    `state_root`: computing the root rejects out-of-range keys and
    values that are not 32 bytes, even though [`trie_set`] already
    enforced both at write time. Prefix-freeness is enforced during
    the walk itself, in [`binarize`].

    [`EMPTY_TRIE_ROOT`]: ref:ethereum.partitioned_binary_tree.EMPTY_TRIE_ROOT
    [`trie_set`]: ref:ethereum.partitioned_binary_tree.trie_set
    [`binarize`]: ref:ethereum.partitioned_binary_tree.binarize
    """
    for key, value in trie._data.items():
        assert len(key) >= 1
        assert Uint(len(key)) <= MAX_KEY_LENGTH
        assert len(value) == 32
    if len(trie._data) == 0:
        return EMPTY_TRIE_ROOT
    return merkleize(binarize(trie._data, Uint(0)))


Zone = U8
"""
One-byte identifier labeling the category of state a key holds,
prepended as the first byte of every key.

Zones are the partitions of the Partitioned Binary Tree: because the
tree consumes key bits most significant first, every zone owns its
own region of the key space.
Defined zones are [`ACCOUNT_ZONE`], [`CODE_ZONE`], and
[`STORAGE_ZONE`]; the remaining values are reserved for future
state categories.

[`ACCOUNT_ZONE`]: ref:ethereum.partitioned_binary_tree.ACCOUNT_ZONE
[`CODE_ZONE`]: ref:ethereum.partitioned_binary_tree.CODE_ZONE
[`STORAGE_ZONE`]: ref:ethereum.partitioned_binary_tree.STORAGE_ZONE
"""

Address32 = Bytes32
"""
32-byte address used to key the tree.

Legacy 20-byte addresses are converted by [`address20_to_address32`].

[`address20_to_address32`]: ref:ethereum.partitioned_binary_tree.address20_to_address32
"""  # noqa: E501

BASIC_DATA_LEAF_KEY = Uint(0)
"""
Sub-index of the account header leaf packing version, code size,
nonce, and balance.
"""

BASIC_DATA_VERSION = Uint(0)
"""
Version of the basic data leaf layout, packed as the leaf's first
byte by [`encode_basic_data`]. A future change to the layout bumps
the version so readers can tell the encodings apart.

[`encode_basic_data`]: ref:ethereum.partitioned_binary_tree.encode_basic_data
"""

CODE_HASH_LEAF_KEY = Uint(1)
"""
Sub-index of the account header leaf holding the code hash.

An account that is delegated holds no such leaf; its code is its
delegation indicator, kept at [`DELEGATION_LEAF_KEY`] instead. Every
account that exists holds exactly one of the two.

[`DELEGATION_LEAF_KEY`]: ref:ethereum.partitioned_binary_tree.DELEGATION_LEAF_KEY
"""  # noqa: E501

DELEGATION_LEAF_KEY = Uint(2)
"""
Sub-index of the account header leaf holding a delegation indicator.

The leaf determines both the code and its hash: a code read takes
the leading `code_size` bytes of the value, and `EXTCODEHASH` hashes
them. Holding it in the header rather than as content-addressed code
keeps the indicator private to one account, so replacing or clearing
a delegation touches no leaf another account shares; see
[`embed_account`].

[`embed_account`]: ref:ethereum.partitioned_binary_tree.embed_account
"""

DELEGATION_MARKER = Bytes(b"\xef\x01\x00")
"""
Leading bytes marking an account's code as a delegation indicator.

Defined here rather than imported so this module stays independent
of any fork, as [`EMPTY_CODE_HASH`] is.

[`EMPTY_CODE_HASH`]: ref:ethereum.partitioned_binary_tree.EMPTY_CODE_HASH
"""

DELEGATION_CODE_LENGTH = Uint(23)
"""
Length of a delegation indicator: the marker and a 20-byte address.
"""

EMPTY_CODE_HASH = keccak256(b"")
"""
Code hash for accounts without code.

The code hash leaf is written on account creation, EOAs included,
and holds the Keccak hash of empty bytecode: `EXTCODEHASH` of a
codeless account, existing or newly created, must keep returning
this value.

`code_hash` is an EVM-observable value stored in a leaf, not a tree
commitment, so it stays Keccak even though the tree hashes with
[`blake3_hash`].

[`blake3_hash`]: ref:ethereum.partitioned_binary_tree.blake3_hash
"""

HEADER_STORAGE_OFFSET = Uint(64)
"""
Sub-index of storage slot `0` within the account header stem. Slots
`0` through `63` live in the header.
"""

HEADER_STORAGE_SLOTS = Uint(64)
"""
Number of storage slots co-located in the account header stem:
slots `0` through `HEADER_STORAGE_SLOTS - 1` live there, at
sub-indices counted from [`HEADER_STORAGE_OFFSET`], and every later
slot lives in [`STORAGE_ZONE`]; see
[`get_tree_key_for_storage_slot`].

[`HEADER_STORAGE_OFFSET`]: ref:ethereum.partitioned_binary_tree.HEADER_STORAGE_OFFSET
[`STORAGE_ZONE`]: ref:ethereum.partitioned_binary_tree.STORAGE_ZONE
[`get_tree_key_for_storage_slot`]: ref:ethereum.partitioned_binary_tree.get_tree_key_for_storage_slot
"""  # noqa: E501

STEM_SUBTREE_WIDTH = Uint(256)
"""
Maximum number of values grouped under a single stem: the size of
the sub-index byte's space.

The EIP requires `HEADER_STORAGE_OFFSET + HEADER_STORAGE_SLOTS <=
STEM_SUBTREE_WIDTH` as an invariant; the header storage sweep and
the storage key split assume it.
"""

ACCOUNT_ZONE = Zone(0)
"""
Zone byte of account header stems.
"""

CODE_ZONE = Zone(1)
"""
Zone byte of content-addressed code stems.

Code chunk keys derive from the code hash rather than from any
account, so contracts with identical bytecode share their chunk
leaves; see [`get_tree_key_for_code_chunk`].

[`get_tree_key_for_code_chunk`]: ref:ethereum.partitioned_binary_tree.get_tree_key_for_code_chunk
"""  # noqa: E501

STORAGE_ZONE = Zone(255)
"""
Zone byte of overflow storage stems.

Storage sits at the far end of the zone byte, leaving zones `2`
through `254` reserved for future state categories.

Note: Because keys are variable length, a zone's one-byte label
says nothing about its capacity so every zone's key space is
unbounded behind its prefix.
"""

ACCOUNT_KEY_LENGTH = Uint(34)
"""
Length of every account zone key: the zone byte, a full address
digest, and the sub-index byte.
"""

CODE_KEY_LENGTH = Uint(34)
"""
Length of every code zone key: the zone byte, a full digest of the
code hash and group index, and the sub-index byte.
"""

STORAGE_KEY_LENGTH = Uint(66)
"""
Length of every storage zone key: the zone byte, two full digests
binding the account and its group index, and the sub-index byte.
"""

PUSH_OFFSET = Uint(95)
"""
Opcode value one below `PUSH1`, so `PUSH_OFFSET + n` is the opcode
pushing `n` bytes.
"""

PUSH1 = PUSH_OFFSET + Uint(1)
"""
Opcode of the smallest push instruction.
"""

PUSH32 = PUSH_OFFSET + Uint(32)
"""
Opcode of the largest push instruction.
"""


def address20_to_address32(address: Bytes20) -> Address32:
    """
    Convert a legacy 20-byte address by prepending 12 zero bytes.

    The embedding keys the tree by 32-byte addresses so that a future
    address-space extension needs no re-keying.
    """
    return Address32(left_pad_zero_bytes(address, 32))


def key_hash(data: Bytes) -> Hash32:
    """
    Hash `data` for use in tree key derivation.

    Key derivation reuses [`blake3_hash`], the tree's merkleization
    hash.

    [`blake3_hash`]: ref:ethereum.partitioned_binary_tree.blake3_hash
    """
    return blake3_hash(data)


def get_tree_key(zone: Zone, tree_position: Bytes, sub_index: U8) -> Key:
    """
    Build a key from its three parts: the `zone` byte, the
    hash-derived `tree_position`, and the final `sub_index` byte.
    """
    return Key(bytes([int(zone)]) + tree_position + bytes([int(sub_index)]))


def get_tree_key_for_header(address: Address32, sub_index: Uint) -> Key:
    """
    Compute the key of the account header leaf at `sub_index`.

    The header stem is in [`ACCOUNT_ZONE`] and is keyed by the address
    alone, so each account has exactly one header stem. The header is
    not one key: it is up to [`STEM_SUBTREE_WIDTH`] separate leaves
    sharing that stem, and `sub_index` selects which one; basic
    data, code hash, delegation, or an early storage slot. The
    embedding derives no header key outside those sub-indices, so
    the rest of the stem's space is unallocated and reserved for
    future header fields.

    [`ACCOUNT_ZONE`]: ref:ethereum.partitioned_binary_tree.ACCOUNT_ZONE
    [`STEM_SUBTREE_WIDTH`]: ref:ethereum.partitioned_binary_tree.STEM_SUBTREE_WIDTH
    """  # noqa: E501
    key = get_tree_key(ACCOUNT_ZONE, key_hash(address), U8(sub_index))
    assert len(key) == int(ACCOUNT_KEY_LENGTH)
    return key


def account_header_stem(address: Address32) -> Bytes:
    """
    Compute the stem shared by every leaf of an account's header:
    its basic data, its code hash or its delegation, and its first
    storage slots.

    Every key under this prefix belongs to `address` and no key of
    `address`'s header sits outside it, so the prefix is the account
    header as one addressable region; see [`remove_account`].

    [`remove_account`]: ref:ethereum.partitioned_binary_tree.remove_account
    """
    return Bytes(bytes([int(ACCOUNT_ZONE)]) + key_hash(address))


def account_storage_prefix(address: Address32) -> Bytes:
    """
    Compute the prefix covering every overflow storage leaf of an
    account, across all of its storage groups.

    Unlike [`account_header_stem`] this spans many stems: it is the
    outer digest of [`storage_tree_position`], deliberately shared by
    an account's whole overflow storage so that storage forms one
    contiguous key range rather than locations scattered across the
    tree.

    The range is unbounded, since an account may hold slots at any
    of `2**256` positions, so it can only be addressed as a prefix,
    never enumerated key by key.

    [`account_header_stem`]: ref:ethereum.partitioned_binary_tree.account_header_stem
    [`storage_tree_position`]: ref:ethereum.partitioned_binary_tree.storage_tree_position
    """  # noqa: E501
    return Bytes(bytes([int(STORAGE_ZONE)]) + key_hash(address))


def get_tree_key_for_basic_data(address: Address32) -> Key:
    """
    Compute the key of the account's basic data leaf.
    """
    return get_tree_key_for_header(address, BASIC_DATA_LEAF_KEY)


def get_tree_key_for_code_hash(address: Address32) -> Key:
    """
    Compute the key of the account's code hash leaf.
    """
    return get_tree_key_for_header(address, CODE_HASH_LEAF_KEY)


def get_tree_key_for_delegation(address: Address32) -> Key:
    """
    Compute the key of the account's delegation leaf.
    """
    return get_tree_key_for_header(address, DELEGATION_LEAF_KEY)


def is_delegation(code: Bytes) -> bool:
    """
    Check whether `code` is a delegation indicator.

    Deployed code may not begin with the marker's first byte, so an
    account holds an indicator only by delegating; the classification
    is a function of the code alone, never of its hash, which an
    attacker could otherwise grind to have a contract read as
    delegated.
    """
    return (
        Uint(len(code)) == DELEGATION_CODE_LENGTH
        and code[: len(DELEGATION_MARKER)] == DELEGATION_MARKER
    )


def encode_delegation(code: Bytes) -> Bytes32:
    """
    Pack a delegation indicator into the 32-byte value stored at
    [`DELEGATION_LEAF_KEY`].

    The indicator occupies the leading bytes and the remainder is
    zero. This is not the chunk encoding: a chunk reserves its first
    byte for a push-data count, which an indicator, never being
    executed as code, does not carry.

    [`DELEGATION_LEAF_KEY`]: ref:ethereum.partitioned_binary_tree.DELEGATION_LEAF_KEY
    """  # noqa: E501
    return Bytes32(right_pad_zero_bytes(code, 32))


def storage_tree_position(address: Address32, tree_index: U256) -> Bytes:
    """
    Build the hash-derived position of an account's overflow storage
    group at `tree_index`.

    The position carries two full digests:

    - `key_hash(address)` gathers all of an account's overflow
      storage under one subtree, which future expiry and sync
      schemes could use as their unit of work: a contract's whole
      storage is one contiguous key range that can be expired or
      served as a single subtree, rather than locations scattered
      across the whole tree.
    - `key_hash(address ‖ tree_index)` spreads the account's groups
      within that subtree.

    Both digests depend on the address, so storage keys that an
    attacker grinds to sit close together under one contract cannot
    be reused against a different contract.

    `key_hash(address)` is the same digest [`get_tree_key_for_header`]
    uses for the account's header stem; the two never collide because
    they sit in different zones, differing in the key's first byte.

    [`get_tree_key_for_header`]: ref:ethereum.partitioned_binary_tree.get_tree_key_for_header
    """  # noqa: E501
    prefix = key_hash(address)
    suffix = key_hash(address + tree_index.to_be_bytes32())
    return Bytes(prefix + suffix)


def get_tree_key_for_storage_slot(
    address: Address32, storage_key: U256
) -> Key:
    """
    Compute the key of a storage slot.

    The first [`HEADER_STORAGE_SLOTS`] slots live in the account
    header stem, co-located with the account's basic data; all other
    slots live in the storage zone.

    This leaves group `0` (`tree_index == 0`) short; its
    storage-zone leaves are only sub-indices `64`-`255`, 192 slots
    rather than the full 256 every later group has.

    [`HEADER_STORAGE_SLOTS`]: ref:ethereum.partitioned_binary_tree.HEADER_STORAGE_SLOTS
    """  # noqa: E501
    if storage_key < U256(HEADER_STORAGE_SLOTS):
        return get_tree_key_for_header(
            address, HEADER_STORAGE_OFFSET + Uint(storage_key)
        )
    tree_index = storage_key // U256(STEM_SUBTREE_WIDTH)
    sub_index = storage_key % U256(STEM_SUBTREE_WIDTH)
    key = get_tree_key(
        STORAGE_ZONE,
        storage_tree_position(address, tree_index),
        U8(sub_index),
    )
    assert len(key) == int(STORAGE_KEY_LENGTH)
    return key


def get_tree_key_for_code_chunk(code_hash: Hash32, chunk_id: Uint) -> Key:
    """
    Compute the key of a code chunk, which lives in [`CODE_ZONE`].

    No address takes part: the key is content-addressed by
    `code_hash`, so every account running the same bytecode shares
    the leaf. That sharing is why chunks outlive the accounts
    referencing them; see [`remove_code_chunks`].

    An aligned range of [`STEM_SUBTREE_WIDTH`] chunks sharing one
    `tree_index` is a **code group**: its chunks share a stem and
    differ only in the sub-index byte.

    [`CODE_ZONE`]: ref:ethereum.partitioned_binary_tree.CODE_ZONE
    [`STEM_SUBTREE_WIDTH`]: ref:ethereum.partitioned_binary_tree.STEM_SUBTREE_WIDTH
    [`remove_code_chunks`]: ref:ethereum.partitioned_binary_tree.remove_code_chunks
    """  # noqa: E501
    tree_index = chunk_id // STEM_SUBTREE_WIDTH
    sub_index = chunk_id % STEM_SUBTREE_WIDTH
    key = get_tree_key(
        CODE_ZONE,
        key_hash(code_hash + tree_index.to_be_bytes32()),
        U8(sub_index),
    )
    assert len(key) == int(CODE_KEY_LENGTH)
    return key


def chunkify_code(code: Bytes) -> List[Bytes32]:
    """
    Split `code` into the 32-byte chunks stored in the tree.

    Chunk `i` holds the `i`-th 31-byte slice of the code in bytes `1`
    through `31`, preceded by one byte counting how many of the
    slice's leading bytes are data of a push instruction that began in
    an earlier chunk.

    The count lets a chunk be interpreted without
    its predecessors and is capped at `31`, the chunk payload size.
    """
    if len(code) % 31 != 0:
        pad_amount = 31 - (len(code) % 31)
        code = Bytes(right_pad_zero_bytes(code, len(code) + pad_amount))

    # Number of push-data bytes remaining at each position, counting
    # the position itself; `0` marks executable bytes. The extra 32
    # entries let the largest push record data past the end of the
    # code.
    remaining_push_data = [0] * (len(code) + 32)
    position = 0
    while position < len(code):
        opcode = Uint(code[position])
        if PUSH1 <= opcode <= PUSH32:
            push_data_bytes = int(opcode - PUSH_OFFSET)
        else:
            push_data_bytes = 0
        position += 1
        for offset in range(push_data_bytes):
            remaining_push_data[position + offset] = push_data_bytes - offset
        position += push_data_bytes

    return [
        Bytes32(
            bytes([min(remaining_push_data[start], 31)])
            + code[start : start + 31]
        )
        for start in range(0, len(code), 31)
    ]


def encode_basic_data(code_size: U32, nonce: U64, balance: U256) -> Bytes32:
    """
    Pack an account's basic data into the 32-byte value stored at
    [`BASIC_DATA_LEAF_KEY`].

    The fields are packed big-endian, consistent with every other
    encoding in the embedding:

    - one version byte, currently zero
    - three reserved zero bytes
    - four bytes of code size
    - eight bytes of nonce
    - sixteen bytes of balance

    The code size and nonce parameters are typed at their field
    widths; the nonce cannot exceed eight bytes by [EIP-2681].
    Balances are protocol-level `U256` values, so the parameter
    keeps that type; a balance too large for the sixteen-byte
    field cannot be committed and raises [`BalanceOverflowError`],
    invalidating the block whose state would hold it.

    The four-byte `code_size` at offset four matches EIP-8297; it is
    one byte wider than EIP-7864's three-byte field at offset five,
    from which this layout descends.

    [`BASIC_DATA_LEAF_KEY`]: ref:ethereum.partitioned_binary_tree.BASIC_DATA_LEAF_KEY
    [`BalanceOverflowError`]: ref:ethereum.exceptions.BalanceOverflowError
    [EIP-2681]: https://eips.ethereum.org/EIPS/eip-2681
    """  # noqa: E501
    if balance >= U256(2) ** U256(128):  # U128 doesn't exist
        raise BalanceOverflowError(
            f"balance {balance} does not fit the sixteen-byte "
            f"basic data balance field"
        )
    return Bytes32(
        bytes([int(BASIC_DATA_VERSION)])
        # Reserved bytes: headroom for future header fields.
        + b"\x00" * 3
        + code_size.to_be_bytes4()
        + nonce.to_be_bytes8()
        + int(balance).to_bytes(16, "big")
    )


ZERO_VALUE = Bytes32(b"\x00" * 32)
"""
The value that [`state_write`] resolves to a deletion rather
than an insertion.

[`state_write`]: ref:ethereum.partitioned_binary_tree.state_write
"""


def state_write(trie: BinaryTrie, key: Key, value: Bytes32) -> None:
    """
    Write `value` at `key`, resolving 32 zero bytes to a deletion
    rather than an insertion.

    The tree itself has no value meaning absence: every 32-byte
    value is storable, and only a key's presence distinguishes it
    from an absent one. Collapsing zero onto absence is the state
    model's choice, made here so that state written through this
    module cannot commit to a zero-valued leaf, and so an absent key
    and a zero one are the same state with the same root.

    Reads recover the collapsed value: an absent key reads back as
    the zero it stood for, whether that is an empty storage slot or
    a code chunk of 31 zero bytes.
    """
    trie_set(trie, key, None if value == ZERO_VALUE else value)


def embed_account(
    trie: BinaryTrie,
    address32: Address32,
    nonce: U64,
    balance: U256,
    code_hash: Hash32,
    code: Bytes,
) -> None:
    """
    Write an account's leaves into `trie`: packed basic data, then
    either a delegation leaf or a code hash leaf and one leaf per
    chunk of `code`.

    Being delegated and holding contract code are exclusive, so an
    account holds exactly one of the two leaves and the other is
    removed here. Writing over an existing account updates its leaves
    in place and is told nothing of what the account was before, so
    both removals are unconditional: an account that has just
    delegated still carries the code hash leaf it held a moment ago,
    and one that has just cleared its delegation still carries the
    delegation leaf.

    Chunk leaves are content-addressed, so accounts sharing bytecode
    write the same leaves with the same values, and a re-embedding
    is idempotent. Leaves of a previous, different code are not
    touched here: content addressing keeps them out of this code's
    key set, and reclaiming them is a reference check against the
    resulting state; see [`remove_code_chunks`].

    Every leaf goes through [`state_write`], so any of them encoding
    to 32 zero bytes is left absent and reads back as the zero it
    stood for. Two cases reach that:

    - A chunk of 31 zero bytes, as in a run of `STOP` or a
      zero-filled data region. Chunk presence therefore does not
      delimit the code; its length is `code_size`.
    - The basic data of an account with zero nonce, zero balance and
      no code, since the version byte and the reserved bytes are
      zero too. Such an account is still distinguished from an
      absent one by the one header leaf it always holds.

    [`remove_code_chunks`]: ref:ethereum.partitioned_binary_tree.remove_code_chunks
    [`state_write`]: ref:ethereum.partitioned_binary_tree.state_write
    """  # noqa: E501
    state_write(
        trie,
        get_tree_key_for_basic_data(address32),
        encode_basic_data(
            code_size=U32(len(code)),
            nonce=nonce,
            balance=balance,
        ),
    )
    if is_delegation(code):
        state_write(
            trie,
            get_tree_key_for_delegation(address32),
            encode_delegation(code),
        )
        trie_set(trie, get_tree_key_for_code_hash(address32), None)
        return

    trie_set(trie, get_tree_key_for_delegation(address32), None)
    state_write(
        trie,
        get_tree_key_for_code_hash(address32),
        Bytes32(code_hash),
    )
    for chunk_id, chunk in enumerate(chunkify_code(code)):
        state_write(
            trie,
            get_tree_key_for_code_chunk(code_hash, Uint(chunk_id)),
            chunk,
        )


def embed_storage_slot(
    trie: BinaryTrie,
    address32: Address32,
    storage_key: U256,
    value: Bytes32,
) -> None:
    """
    Write one storage slot's leaf into `trie`, in the account header
    stem or the account's overflow storage subtree as the slot
    number dictates.

    Writing zero removes the slot's leaf, per [`state_write`], so a
    slot cleared to zero is indistinguishable from one never
    written.

    [`state_write`]: ref:ethereum.partitioned_binary_tree.state_write
    """
    state_write(
        trie, get_tree_key_for_storage_slot(address32, storage_key), value
    )


def remove_account(trie: BinaryTrie, address32: Address32) -> None:
    """
    Remove an account from `trie` entirely: its basic data, its code
    hash or delegation, and every storage slot it holds.

    An account owns exactly two regions of the key space, both fixed
    by its address: its [`account_header_stem`] and its
    [`account_storage_prefix`]. Removing an account is removing those
    two subtrees, so what has to go is read off the address rather
    than out of a list of the account's slots, which the caller may
    not have, and which for storage is unbounded anyway.

    Code chunks are the one thing an account holds that it does not
    own: they live in [`CODE_ZONE`], content-addressed, and are
    shared with every other account running the same bytecode, so
    they outlive the account that referenced them and are not removed
    here. Dropping them takes a reference check against the resulting
    state; see [`remove_code_chunks`].

    Removing an absent account does nothing.

    [`account_header_stem`]: ref:ethereum.partitioned_binary_tree.account_header_stem
    [`account_storage_prefix`]: ref:ethereum.partitioned_binary_tree.account_storage_prefix
    [`CODE_ZONE`]: ref:ethereum.partitioned_binary_tree.CODE_ZONE
    [`remove_code_chunks`]: ref:ethereum.partitioned_binary_tree.remove_code_chunks
    """  # noqa: E501
    remove_subtree(trie, account_header_stem(address32))
    remove_subtree(trie, account_storage_prefix(address32))


def remove_code_chunks(
    trie: BinaryTrie, code_hash: Hash32, code: Bytes
) -> None:
    """
    Remove the [`CODE_ZONE`] leaves of `code` from `trie`.

    These leaves are content-addressed, so they belong to the
    bytecode rather than to any account holding it. They may be
    removed only once no account in the resulting state has
    `code_hash`, which the caller establishes; removing them while an
    account still runs that code would take its bytecode with it.

    The sweep covers every chunk of `code` without consulting the
    tree: chunks encoding to 32 zero bytes were never in it (see
    [`state_write`]) and removing an absent chunk does nothing.

    [`CODE_ZONE`]: ref:ethereum.partitioned_binary_tree.CODE_ZONE
    [`state_write`]: ref:ethereum.partitioned_binary_tree.state_write
    """  # noqa: E501
    for chunk_id in range(len(chunkify_code(code))):
        trie_set(
            trie,
            get_tree_key_for_code_chunk(code_hash, Uint(chunk_id)),
            None,
        )


def remove_all_storage(trie: BinaryTrie, address32: Address32) -> None:
    """
    Remove every storage slot leaf of an account from `trie`, leaving
    the account itself and its code in place.

    An account's storage straddles the two regions its address fixes:
    the header slots sit in the header stem beside the basic data
    and the code hash or delegation that must survive, so the header
    is swept one slot sub-index at a time, while the overflow
    storage subtree goes whole. As in [`remove_account`], no list of
    the account's slots is needed.

    [`remove_account`]: ref:ethereum.partitioned_binary_tree.remove_account
    """
    for sub_index in range(
        HEADER_STORAGE_OFFSET, HEADER_STORAGE_OFFSET + HEADER_STORAGE_SLOTS
    ):
        trie_set(
            trie, get_tree_key_for_header(address32, Uint(sub_index)), None
        )
    remove_subtree(trie, account_storage_prefix(address32))


def remove_storage_slot(
    trie: BinaryTrie, address32: Address32, storage_key: U256
) -> None:
    """
    Remove one storage slot's leaf from `trie`; removing an absent
    slot does nothing.
    """
    trie_set(trie, get_tree_key_for_storage_slot(address32, storage_key), None)
