"""
EIP-8115: Batch priority fees at end of block.

https://eips.ethereum.org/EIPS/eip-8115
"""

from ....base_fork import BaseFork


class EIP8115(BaseFork):
    """EIP-8115 class."""

    @classmethod
    def batched_priority_fees(cls) -> bool:
        """
        Priority fees are summed and credited to the fee recipient once
        at the end of the block.
        """
        return True
