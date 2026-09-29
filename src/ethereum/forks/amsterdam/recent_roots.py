"""
The recent root contract introduced by [EIP-8272], which lets frame
transactions verify recent application roots.

A frame transaction verifies recent application roots by
running an ordinary [`VERIFY`][v] frame against
[`RECENT_ROOT_ADDRESS`][rra]; root sources publish roots by calling the
same contract. The contract is installed when the fork activates (see
[`apply_fork`][af]); nothing else in the state transition changes.

[EIP-8272]: https://eips.ethereum.org/EIPS/eip-8272
[v]: ref:ethereum.forks.amsterdam.transactions.frame_transaction.FrameMode.VERIFY
[rra]: ref:ethereum.forks.amsterdam.recent_roots.RECENT_ROOT_ADDRESS
[af]: ref:ethereum.forks.amsterdam.fork.apply_fork
"""  # noqa: E501

from typing import Final

from ethereum_types.bytes import Bytes, Bytes32
from ethereum_types.numeric import U64, Uint

from ethereum.crypto.hash import Hash32, keccak256

from .fork_types import Address

RECENT_ROOT_ADDRESS: Final[Address] = Address(
    bytes.fromhex("0000000000000000000000000000000000008272")
)
"""
Address of the recent root contract.

Calls with 64 bytes of calldata publish a root for the caller's source;
calls with one to [`MAX_RECENT_ROOT_REFERENCES`][mrr] tuples of
[`RECENT_ROOT_TUPLE_BYTES`][rtb] bytes each check those references. A
[`VERIFY`][v] frame targeting this address is a _recent root verifier
frame_; if the contract reverts, the frame fails and the transaction is
invalid, as for any [`VERIFY`][v] frame.

[mrr]: ref:ethereum.forks.amsterdam.recent_roots.MAX_RECENT_ROOT_REFERENCES
[rtb]: ref:ethereum.forks.amsterdam.recent_roots.RECENT_ROOT_TUPLE_BYTES
[v]: ref:ethereum.forks.amsterdam.transactions.frame_transaction.FrameMode.VERIFY
"""  # noqa: E501

RECENT_ROOT_NONCE: Final[Uint] = Uint(1)
"""
Nonce the recent root contract is given at activation; a higher existing
nonce is kept.
"""

RECENT_ROOT_LENGTH: Final[Uint] = Uint(8192)
"""
Number of ring buffer entries a root source keeps: the root written in
slot `S` occupies index `S mod RECENT_ROOT_LENGTH`.
"""

RECENT_ROOT_USABLE_WINDOW: Final[Uint] = Uint(8191)
"""
Maximum age, in slots, of a referenceable root. The current slot itself is
never referenceable, so the window is one less than the buffer length.
"""

MAX_RECENT_ROOT_REFERENCES: Final[Uint] = Uint(16)
"""Maximum number of tuples in one validation call."""

RECENT_ROOT_TUPLE_BYTES: Final[Uint] = Uint(72)
"""
Length of a validation tuple: a 32-byte source identifier, an 8-byte
big-endian slot and a 32-byte root.
"""

RECENT_ROOT_WRITE_BYTES: Final[Uint] = Uint(64)
"""Length of a write call's calldata: a 32-byte salt and a 32-byte root."""

RECENT_ROOT_ENTRY_DOMAIN: Final[Hash32] = keccak256(b"RECENT_ROOT_ENTRY")
"""Domain separator of the committed entry hash."""

RECENT_ROOT_STORAGE_DOMAIN: Final[Hash32] = keccak256(b"RECENT_ROOT_STORAGE")
"""Domain separator of the storage key derivation."""

RECENT_ROOT_CODE: Final[Bytes] = Bytes(
    bytes.fromhex(
        "34600858015760095801565b60006000fd5b6040361461010e5801576104"
        "8036116048360617361517600858015760095801565b60006000fd5b6000"
        "6080525b608051356020526020608051013560c01c60a0524b60a0511015"
        "600858015760095801565b60006000fd5b611fff60a0514b031160085801"
        "5760095801565b60006000fd5b7f8f42481679c8e6fefa040974b3c905e0"
        "ce3f2e464ba93acdb074a41181617efc60005260a05160c01b6040526028"
        "608051013560485260686000207fbdc897da2177d260ff5f4be5d4b2aad4"
        "3f89c3347a305b584fa5a2546d053daa60005261200060a0510660c01b60"
        "40526048600020541415600858015760095801565b60006000fd5b604860"
        "805101608052366080511063000000df5803570060855801565b3360601b"
        "60005260003560145260346000206020527f8f42481679c8e6fefa040974"
        "b3c905e0ce3f2e464ba93acdb074a41181617efc6000524b60c01b604052"
        "60203560485260686000207fbdc897da2177d260ff5f4be5d4b2aad43f89"
        "c3347a305b584fa5a2546d053daa6000526120004b0660c01b6040526048"
        "60002055005b"
    )
)
"""
Runtime code of the recent root contract, installed at
[`RECENT_ROOT_ADDRESS`][rra] when the fork activates (see
[`apply_fork`][af]).

[EIP-8272] leaves this code to be determined. This is a candidate
implementing the specified behaviour (keccak256
`0x92581be6144206cc1ba9f655324d74f0a49f20661ff2d31975aefb2449884342`):

* A call carrying value reverts.
* With exactly [`RECENT_ROOT_WRITE_BYTES`][rwb] bytes of calldata, the
  call is a write: with the caller as the source address and calldata
  `0..32` as the salt, it stores
  [`recent_root_entry_hash`][reh] of the current slot and the root in
  calldata `32..64` under the caller's
  [`recent_root_storage_key`][rsk] for that slot, then stops. In a static
  context the store fails, leaving storage unchanged.
* Otherwise the call is a validation: it reverts unless the calldata is
  one to [`MAX_RECENT_ROOT_REFERENCES`][mrr] tuples of
  [`RECENT_ROOT_TUPLE_BYTES`][rtb] bytes, and for each tuple checks that
  its slot is strictly before the current slot, that the root is at most
  [`RECENT_ROOT_USABLE_WINDOW`][ruw] slots old and that the tuple's entry
  hash is stored under its storage key, reverting at the first failure
  and stopping with no return data otherwise.

The current slot is read with `SLOTNUM`. The contract reads no account
other than itself and no storage other than the keys derived from its
calldata.

[EIP-8272]: https://eips.ethereum.org/EIPS/eip-8272
[rra]: ref:ethereum.forks.amsterdam.recent_roots.RECENT_ROOT_ADDRESS
[af]: ref:ethereum.forks.amsterdam.fork.apply_fork
[rwb]: ref:ethereum.forks.amsterdam.recent_roots.RECENT_ROOT_WRITE_BYTES
[reh]: ref:ethereum.forks.amsterdam.recent_roots.recent_root_entry_hash
[rsk]: ref:ethereum.forks.amsterdam.recent_roots.recent_root_storage_key
[mrr]: ref:ethereum.forks.amsterdam.recent_roots.MAX_RECENT_ROOT_REFERENCES
[rtb]: ref:ethereum.forks.amsterdam.recent_roots.RECENT_ROOT_TUPLE_BYTES
[ruw]: ref:ethereum.forks.amsterdam.recent_roots.RECENT_ROOT_USABLE_WINDOW
"""  # noqa: E501


def recent_root_source_id(source_address: Address, salt: Bytes32) -> Hash32:
    """
    Derive the identifier of a root source: the keccak256 of the source
    address followed by the salt.

    A source address may publish under any number of salts; each pair is
    an independent ring buffer of roots.
    """
    return keccak256(source_address + salt)


def recent_root_entry_hash(
    source_id: Hash32, slot: U64, root: Bytes32
) -> Hash32:
    """
    Derive the entry committed for `(source_id, slot, root)`: the keccak256
    of [`RECENT_ROOT_ENTRY_DOMAIN`][red], the source identifier, the slot as
    an eight-byte big-endian integer and the root.

    Committing to the source and the slot keeps a root of another source,
    or a stale occupant of the same ring buffer index, from satisfying a
    reference.

    [red]: ref:ethereum.forks.amsterdam.recent_roots.RECENT_ROOT_ENTRY_DOMAIN
    """  # noqa: E501
    return keccak256(
        RECENT_ROOT_ENTRY_DOMAIN + source_id + slot.to_be_bytes8() + root
    )


def recent_root_storage_key(source_id: Hash32, slot: U64) -> Bytes32:
    """
    Derive the storage key holding the entry of `slot` for a root source:
    the keccak256 of [`RECENT_ROOT_STORAGE_DOMAIN`][rsd], the source
    identifier and the ring buffer index `slot mod RECENT_ROOT_LENGTH` as
    an eight-byte big-endian integer.

    [rsd]: ref:ethereum.forks.amsterdam.recent_roots.RECENT_ROOT_STORAGE_DOMAIN
    """  # noqa: E501
    index = U64(Uint(slot) % RECENT_ROOT_LENGTH)
    return Bytes32(
        keccak256(
            RECENT_ROOT_STORAGE_DOMAIN + source_id + index.to_be_bytes8()
        )
    )
