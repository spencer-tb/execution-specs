"""
Tests for [EIP-7666: EVM-ify the identity precompile](https://eips.ethereum.org/EIPS/eip-7666).
"""

# TODO: Re-derive the tests parked with `valid_before("EIP7666")`
#  once the EIP settles: the ported modexp harnesses use the identity
#  precompile as a memory-copy primitive and need an MCOPY-based
#  rewrite; the 2929/static-call/spam cases pin identity-as-precompile
#  warmth or nonexistence. The marker itself enumerates the worklist.
