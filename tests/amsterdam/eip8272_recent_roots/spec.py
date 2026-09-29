"""Defines EIP-8272 specification constants and types."""

from dataclasses import dataclass

from execution_testing import Address, keccak256


@dataclass(frozen=True)
class ReferenceSpec:
    """Defines the reference spec version and git path."""

    git_path: str
    version: str


ref_spec_8272 = ReferenceSpec(
    "EIPS/eip-8272.md", "274ce98c57ec285862f4d2ff48cd9f545c385f12"
)


@dataclass(frozen=True)
class Spec:
    """
    Parameters from the EIP-8272 specification as defined at
    https://eips.ethereum.org/EIPS/eip-8272.

    `RECENT_ROOT_CODE` is `TBD` in the EIP; the value here is the
    candidate runtime code this prototype installs, assembled from the
    readable source in `contract.py`.
    """

    RECENT_ROOT_ADDRESS = Address(0x8272)
    RECENT_ROOT_ADDRESS_INT = 0x8272
    RECENT_ROOT_CODE = bytes.fromhex(
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
    RECENT_ROOT_NONCE = 1
    RECENT_ROOT_LENGTH = 8192
    RECENT_ROOT_USABLE_WINDOW = 8191
    MAX_RECENT_ROOT_REFERENCES = 16
    RECENT_ROOT_TUPLE_BYTES = 72
    RECENT_ROOT_WRITE_BYTES = 64
    RECENT_ROOT_ENTRY_DOMAIN = keccak256(b"RECENT_ROOT_ENTRY")
    RECENT_ROOT_STORAGE_DOMAIN = keccak256(b"RECENT_ROOT_STORAGE")

    # Reference vector from the EIP, valid at `current_slot = 2`.
    VECTOR_SOURCE_ADDRESS = Address(0x01)
    VECTOR_SALT = bytes(32)
    VECTOR_SLOT = 1
    VECTOR_ROOT = (2).to_bytes(32, "big")
    VECTOR_CURRENT_SLOT = 2
    VECTOR_SOURCE_ID = bytes.fromhex(
        "b9382d35273c75a50631a3e84d3c75ec9266e2b18c35a627e16cdbf26a18ca85"
    )
    VECTOR_ENTRY_HASH = bytes.fromhex(
        "0a0d1254c851be5a133b4c9a9e300f5602fc0f43dbe65aa6a66930d4ca0a51b8"
    )
    VECTOR_STORAGE_KEY = bytes.fromhex(
        "5f027aa1cbe2df279bf6518edd4b44ea5409fd800189ec35224e10ab05e574c3"
    )


def source_id(source_address: Address, salt: bytes) -> bytes:
    """
    Return the root source identifier: the keccak256 of the 20-byte source
    address followed by the 32-byte salt.
    """
    return bytes(keccak256(bytes(source_address) + bytes(salt)))


def entry_hash(source: bytes, slot: int, root: bytes) -> bytes:
    """
    Return the committed entry for `(source_id, slot, root)`: the keccak256
    of the entry domain, the source identifier, the slot as an eight-byte
    big-endian integer, and the root.
    """
    return bytes(
        keccak256(
            bytes(Spec.RECENT_ROOT_ENTRY_DOMAIN)
            + bytes(source)
            + slot.to_bytes(8, "big")
            + bytes(root)
        )
    )


def storage_key(source: bytes, slot: int) -> int:
    """
    Return the recent root storage key holding the entry of `slot` for a
    source: the keccak256 of the storage domain, the source identifier,
    and the ring buffer index `slot mod RECENT_ROOT_LENGTH` as an
    eight-byte big-endian integer.
    """
    index = slot % Spec.RECENT_ROOT_LENGTH
    return int.from_bytes(
        keccak256(
            bytes(Spec.RECENT_ROOT_STORAGE_DOMAIN)
            + bytes(source)
            + index.to_bytes(8, "big")
        ),
        "big",
    )


def validation_tuple(source: bytes, slot: int, root: bytes) -> bytes:
    """Return the 72-byte validation encoding of `(source_id, slot, root)`."""
    return bytes(source) + slot.to_bytes(8, "big") + bytes(root)


def write_calldata(salt: bytes, root: bytes) -> bytes:
    """Return the 64-byte write encoding of `(salt, root)`."""
    return bytes(salt) + bytes(root)
