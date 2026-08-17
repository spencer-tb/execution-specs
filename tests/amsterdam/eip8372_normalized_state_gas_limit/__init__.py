"""
Tests for [EIP-8372: Normalized state gas limit](https://eips.ethereum.org/EIPS/eip-8372).
"""

# TODO: Re-derive the tests parked with `valid_before("EIP8372")`
#  across the repository once the calibration constants (`CPSB`,
#  `STATE_GAS_LIMIT_SCALE`) are final: header pins move to
#  `fork.normalized_block_state_gas(...)` and state-gas-heavy
#  scenarios resize against `fork.block_state_gas_limit(...)`. The
#  marker itself enumerates the worklist.
