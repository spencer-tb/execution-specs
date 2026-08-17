"""
EIP-8372: Normalized state gas limit.

https://eips.ethereum.org/EIPS/eip-8372
"""

from ....base_fork import BaseFork


class EIP8372(BaseFork):
    """EIP-8372 class."""

    STATE_GAS_LIMIT_SCALE = 50
    STATE_GAS_LIMIT_SCALE_DENOMINATOR = 100

    @classmethod
    def cost_per_state_byte(cls) -> int:
        """Recalibrated state-byte price, scaled with the limit."""
        return 765

    @classmethod
    def block_state_gas_limit(cls, block_gas_limit: int) -> int:
        """Scale the raw state-gas limit to its calibrated share."""
        return (
            block_gas_limit
            * cls.STATE_GAS_LIMIT_SCALE
            // cls.STATE_GAS_LIMIT_SCALE_DENOMINATOR
        )

    @classmethod
    def normalized_block_state_gas(cls, state_gas_used: int) -> int:
        """Undo the limit scaling on the block gas axis."""
        return (
            state_gas_used
            * cls.STATE_GAS_LIMIT_SCALE_DENOMINATOR
            // cls.STATE_GAS_LIMIT_SCALE
        )
