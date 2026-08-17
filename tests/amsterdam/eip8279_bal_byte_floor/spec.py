"""Reference spec for [EIP-8279](https://eips.ethereum.org/EIPS/eip-8279)."""

from dataclasses import dataclass


@dataclass(frozen=True)
class ReferenceSpec:
    """Reference specification."""

    git_path: str
    version: str


ref_spec_8279 = ReferenceSpec(
    git_path="EIPS/eip-8279.md",
    version="4484909deb60e8266152f4b6eed2d79990af072b",
)


@dataclass(frozen=True)
class Spec:
    """
    Constants from the EIP-8279 specification.

    The floor charges a fixed price per byte the transaction adds to
    the block access list; each access kind contributes the encoded
    size of the value it publishes.
    """

    FLOOR_PER_BYTE = 64
    BYTES_PER_ADDRESS = 20
    BYTES_PER_STORAGE_KEY = 32
    BYTES_PER_STORAGE_VALUE = 32
    BYTES_PER_BALANCE = 32
    BYTES_PER_NONCE = 8
    DELEGATION_CODE_BYTES = 23
    AUTHORIZATION_SEED_BYTES = (
        BYTES_PER_ADDRESS + DELEGATION_CODE_BYTES + BYTES_PER_NONCE
    )
