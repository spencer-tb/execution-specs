"""
EIP-7686: Linear EVM Memory Limits.

https://eips.ethereum.org/EIPS/eip-7686
"""

from ....base_fork import BaseFork, MemoryExpansionGasCalculator
from ...helpers import ceiling_division


class EIP7686(BaseFork):
    """EIP-7686 class."""

    @classmethod
    def memory_expansion_gas_calculator(cls) -> MemoryExpansionGasCalculator:
        """
        Return callable that calculates the gas cost of memory expansion
        for the fork.

        EIP-7686 removes the quadratic term: the cost is
        MEMORY_PER_WORD per newly allocated word.
        """
        gas_costs = cls.gas_costs()

        def fn(*, new_bytes: int, previous_bytes: int = 0) -> int:
            if new_bytes <= previous_bytes:
                return 0
            new_words = ceiling_division(new_bytes, 32)
            previous_words = ceiling_division(previous_bytes, 32)
            return gas_costs.MEMORY_PER_WORD * (new_words - previous_words)

        return fn

    @classmethod
    def memory_grant_floor(cls, memory_byte_size: int) -> int:
        """
        Return the minimum gas grant a frame needs to expand its memory
        to the given size.

        EIP-7686 caps a frame's memory at one byte per gas of its
        grant. Memory grows in whole words, so the floor is the size
        rounded up to a word boundary.
        """
        return ceiling_division(memory_byte_size, 32) * 32
