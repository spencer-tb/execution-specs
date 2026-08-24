"""
Tests for [EIP-3298: Removal of refunds](https://eips.ethereum.org/EIPS/eip-3298).
"""

# TODO: Re-derive the tests parked with `valid_before("EIP3298")` once
#  the EIP settles: the quotient-cap and clear-refund scenarios have no
#  post-3298 life, but their gas-boundary shapes (cap saturation,
#  floor-vs-refund windows) should be re-expressed against the
#  surviving write reversal. The marker itself enumerates the worklist.
