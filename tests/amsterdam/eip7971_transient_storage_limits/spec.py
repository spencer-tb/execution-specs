"""Defines the EIP-7971 reference specification."""

from dataclasses import dataclass


@dataclass(frozen=True)
class ReferenceSpec:
    """Defines the reference spec version and git path."""

    git_path: str
    version: str


ref_spec_7971 = ReferenceSpec(
    "EIPS/eip-7971.md", "de83a8d1bcdf89a5780076290b1d9a0799f2faec"
)


@dataclass(frozen=True)
class Spec:
    """Parameters defined by EIP-7971."""

    GAS_TLOAD = 5
    GAS_TSTORE = 12
    GAS_TSTORE_ALLOCATE = 24
    MAX_TRANSIENT_SLOTS = 131072
