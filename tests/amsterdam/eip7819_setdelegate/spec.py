"""Reference spec for [EIP-7819](https://eips.ethereum.org/EIPS/eip-7819)."""

from dataclasses import dataclass
from typing import ClassVar

from execution_testing import Address, Bytes


@dataclass(frozen=True)
class ReferenceSpec:
    """Reference specification."""

    git_path: str
    version: str


ref_spec_7819 = ReferenceSpec(
    git_path="EIPS/eip-7819.md",
    version="d420fc4b289e298682006b2ea09355065cf50f99",
)


@dataclass(frozen=True)
class Spec:
    """Constants from the EIP."""

    DESIGNATOR: ClassVar[bytes] = b"\xef\x01\x00"

    @staticmethod
    def delegation_designation(address: Address) -> Bytes:
        """Return the delegation designation for the given address."""
        return Bytes(Spec.DESIGNATOR + bytes(address))
