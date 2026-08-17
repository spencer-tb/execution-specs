"""Defines EIP-8372 specification constants and types."""

from dataclasses import dataclass


@dataclass(frozen=True)
class ReferenceSpec:
    """Defines the reference spec version and git path."""

    git_path: str
    version: str


ref_spec_8372 = ReferenceSpec(
    "EIPS/eip-8372.md", "4742786332d1c2dfc7d725a95292f8bdf11ff9c7"
)


@dataclass(frozen=True)
class Spec:
    """
    Parameters from the EIP-8372 specification as defined at
    https://eips.ethereum.org/EIPS/eip-8372.

    The prototype uses the Figure-2 contraction calibration: the
    state-byte price and the raw state-gas limit scale halve together,
    preserving the normalized blockspace a state byte occupies.
    """

    COST_PER_STATE_BYTE = 765
    STATE_GAS_LIMIT_SCALE = 50
    STATE_GAS_LIMIT_SCALE_DENOMINATOR = 100
