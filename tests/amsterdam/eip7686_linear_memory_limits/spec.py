"""Defines EIP-7686 specification constants and functions."""

from dataclasses import dataclass


@dataclass(frozen=True)
class ReferenceSpec:
    """Defines the reference spec version and git path."""

    git_path: str
    version: str


ref_spec_7686 = ReferenceSpec(
    "EIPS/eip-7686.md", "1d2e1c18f7cdecc8fa35a74a0040c61ed326a9c1"
)


@dataclass(frozen=True)
class Spec:
    """
    Parameters from the EIP.

    A frame's memory is hard-capped at one byte per gas of its initial
    execution-gas grant, and a sub-call leaves the caller at least the
    larger of one 64th of its remaining gas and one gas per byte of
    its memory.
    """

    GAS_RETAINED_DIVISOR = 64

    @staticmethod
    def max_call_gas(gas: int, memory_byte_size: int) -> int:
        """
        Return the maximum gas a sub-call may receive.

        Mirrors the EIP's `max_call_gas`, clamped at zero for callers
        whose memory already exceeds their remaining gas.
        """
        withheld = max(gas // Spec.GAS_RETAINED_DIVISOR, memory_byte_size)
        return max(gas - withheld, 0)

    @staticmethod
    def memory_limit(gas_grant: int) -> int:
        """Return a frame's hard memory limit: one byte per gas."""
        return gas_grant
