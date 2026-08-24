"""Reference spec for [EIP-8115](https://eips.ethereum.org/EIPS/eip-8115)."""

from dataclasses import dataclass


@dataclass(frozen=True)
class ReferenceSpec:
    """Reference specification."""

    git_path: str
    version: str


ref_spec_8115 = ReferenceSpec(
    git_path="EIPS/eip-8115.md",
    version="5682596cab5f27a5809a2e5d87f8508b7220f1ad",
)
