"""
EIP-8250: Keyed Nonces for Frame Transactions.

https://eips.ethereum.org/EIPS/eip-8250
"""

from dataclasses import replace
from typing import Mapping, Sequence

import ethereum_rlp as eth_rlp
from ethereum_types.numeric import U64, U256

from ....base_fork import BaseFork
from ....gas_costs import GasCosts

NONCE_MANAGER_ADDRESS = 0x0000000000000000000000000000000000008250
NONCE_MANAGER_BYTECODE = bytes.fromhex("60006000fd")


class EIP8250(BaseFork):
    """EIP-8250 class."""

    @classmethod
    def gas_costs(cls) -> GasCosts:
        """Add the keyed-nonce first-use surcharge."""
        return replace(
            super(EIP8250, cls).gas_costs(),
            KEYED_NONCE_FIRST_USE=20_000,
        )

    @classmethod
    def pre_allocation(cls) -> Mapping:
        """Pre-allocate the nonce manager system contract."""
        return {
            NONCE_MANAGER_ADDRESS: {
                # EIP-8250 initializes the account with nonce 1 at
                # activation; its storage starts empty.
                "nonce": 1,
                "code": NONCE_MANAGER_BYTECODE,
            }
        } | super(EIP8250, cls).pre_allocation()  # type: ignore

    @classmethod
    def pre_allocation_blockchain(cls) -> Mapping:
        """Pre-allocate the nonce manager system contract."""
        return {
            NONCE_MANAGER_ADDRESS: {
                # EIP-8250 initializes the account with nonce 1 at
                # activation; its storage starts empty.
                "nonce": 1,
                "code": NONCE_MANAGER_BYTECODE,
            }
        } | super(EIP8250, cls).pre_allocation_blockchain()  # type: ignore

    @classmethod
    def keyed_nonce_calldata(
        cls, nonce_keys: Sequence[int], nonce_seq: int
    ) -> bytes:
        """
        Return the nonce encodings priced as transaction data: the RLP
        of the key list followed by the RLP of the sequence.
        """
        keys = tuple(U256(key) for key in nonce_keys)
        return bytes(
            eth_rlp.rlp.encode(keys) + eth_rlp.rlp.encode(U64(nonce_seq))
        )
