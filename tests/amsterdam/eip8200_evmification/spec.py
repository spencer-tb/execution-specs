"""Defines EIP-8200 specification constants and types."""

from dataclasses import dataclass

from execution_testing import Address


@dataclass(frozen=True)
class ReferenceSpec:
    """Defines the reference spec version and git path."""

    git_path: str
    version: str


ref_spec_8200 = ReferenceSpec(
    "EIPS/eip-8200.md", "4453c19567bd461d27ec555aa6f91e6423b4613e"
)


@dataclass(frozen=True)
class Spec:
    """
    Parameters from the EIP-8200 specification as defined at
    https://eips.ethereum.org/EIPS/eip-8200.

    The deployed bytecode is not yet specified by the EIP; the
    prototype pins the runtime code compiled from eth-act/evmification
    at `a6da8572` and carried in the framework's fork pre-allocation.
    """

    RIPEMD160_ADDRESS = Address(0x03)
    MODEXP_ADDRESS = Address(0x05)
    BLAKE2F_ADDRESS = Address(0x09)

    RIPEMD160_OF_ABC = 0x8EB208F7E05D987A9B044A8E98C6B087F15A0BFC
    """RIPEMD-160 digest of `b"abc"`, right-aligned in a 32-byte word."""
