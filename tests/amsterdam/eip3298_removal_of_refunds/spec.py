"""Defines EIP-3298 specification constants and types."""

from dataclasses import dataclass


@dataclass(frozen=True)
class ReferenceSpec:
    """Defines the reference spec version and git path."""

    git_path: str
    version: str


ref_spec_3298 = ReferenceSpec(
    "EIPS/eip-3298.md", "548ebfb1e987ddb8dc260324e02ee9ec643525a1"
)
