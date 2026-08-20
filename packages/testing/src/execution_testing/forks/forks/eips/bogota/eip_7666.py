"""
EIP-7666: EVM-ify the identity precompile.

https://eips.ethereum.org/EIPS/eip-7666
"""

from typing import List, Mapping

from .....base_types import Address
from ....base_fork import BaseFork

IDENTITY_ADDRESS = 0x04
IDENTITY_EVM_CODE = bytes.fromhex("365f5f37365ff3")


class EIP7666(BaseFork):
    """EIP-7666 class."""

    @classmethod
    def precompiles(cls) -> List[Address]:
        """The identity address is no longer a precompile."""
        return [
            address
            for address in super(EIP7666, cls).precompiles()
            if address != Address(IDENTITY_ADDRESS)
        ]

    @classmethod
    def pre_allocation(cls) -> Mapping:
        """Pre-allocate the EVM identity code at the retired address."""
        return {
            IDENTITY_ADDRESS: {"nonce": 0, "code": IDENTITY_EVM_CODE}
        } | super(EIP7666, cls).pre_allocation()  # type: ignore

    @classmethod
    def pre_allocation_blockchain(cls) -> Mapping:
        """Pre-allocate the EVM identity code at the retired address."""
        return {
            IDENTITY_ADDRESS: {"nonce": 0, "code": IDENTITY_EVM_CODE}
        } | super(EIP7666, cls).pre_allocation_blockchain()  # type: ignore
