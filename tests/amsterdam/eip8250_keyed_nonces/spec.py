"""Defines EIP-8250 specification constants and types."""

from dataclasses import dataclass
from typing import Sequence

from execution_testing import Address, keccak256


@dataclass(frozen=True)
class ReferenceSpec:
    """Defines the reference spec version and git path."""

    git_path: str
    version: str


ref_spec_8250 = ReferenceSpec(
    "EIPS/eip-8250.md", "c9d962f194b9b167e045b3b68a7a292cdc4cec7f"
)


@dataclass(frozen=True)
class Spec:
    """
    Parameters from the EIP-8250 specification as defined at
    https://eips.ethereum.org/EIPS/eip-8250.
    """

    NONCE_MANAGER = Address(0x8250)
    NONCE_MANAGER_CODE = bytes.fromhex("60006000fd")
    MAX_NONCE_KEYS = 16
    MAX_NONCE_SEQ = 2**64 - 1

    # TXPARAM selectors added by this EIP; 0x0F stays undefined.
    TXPARAM_LEGACY_NONCE = 0x0C
    TXPARAM_NONCE_KEY_COUNT = 0x0D
    TXPARAM_NONCE_KEYS_HASH = 0x0E
    TXPARAM_NONCE_KEY_0 = 0x10


def keyed_nonce_slot(sender: Address, nonce_key: int) -> int:
    """
    Derive the `NONCE_MANAGER` storage slot holding the sequence of
    `nonce_key` for `sender`.
    """
    padded_sender = bytes(12) + bytes(sender)
    key_bytes = nonce_key.to_bytes(32, "big")
    return int.from_bytes(keccak256(padded_sender + key_bytes), "big")


def nonce_keys_hash(nonce_keys: Sequence[int]) -> int:
    """
    Hash the selected key set canonically: the key count followed by
    each key, all as 32-byte big-endian words.
    """
    encoded = len(nonce_keys).to_bytes(32, "big")
    for key in nonce_keys:
        encoded += key.to_bytes(32, "big")
    return int.from_bytes(keccak256(encoded), "big")
