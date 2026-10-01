"""
EIP-8250: Keyed Nonces for Frame Transactions.

Replace the single sender nonce of an EIP-8141 frame transaction with a
set of nonce keys sharing one sequence number: key zero aliases the
legacy account nonce, every other key selects an independent sequence
kept in the `NONCE_MANAGER` system contract's storage.

https://eips.ethereum.org/EIPS/eip-8250
"""

from dataclasses import replace
from typing import FrozenSet, Mapping, Sequence

from ethereum_rlp import rlp
from ethereum_types.numeric import U64, U256

from execution_testing.base_types import Address

from ....base_fork import BaseFork
from ....gas_costs import GasCosts
from ..amsterdam.eip_8037 import STATE_BYTES_PER_STORAGE_SET

NONCE_MANAGER_ADDRESS = 0x0000000000000000000000000000000000008250
NONCE_MANAGER_BYTECODE = bytes.fromhex("60006000fd")
NONCE_MANAGER_NONCE = 1


class EIP8250(BaseFork):
    """EIP-8250 class."""

    @classmethod
    def gas_costs(cls) -> GasCosts:
        """
        Add the keyed nonce first-use state gas: one EIP-8037 storage set
        per domain a payment approval uses for the first time.
        """
        return replace(
            super(EIP8250, cls).gas_costs(),
            KEYED_NONCE_FIRST_USE=(
                STATE_BYTES_PER_STORAGE_SET * cls.cost_per_state_byte()
            ),
        )

    @classmethod
    def keyed_nonce_calldata(
        cls, nonce_keys: Sequence[int], nonce_seq: int
    ) -> bytes:
        """
        Return the nonce field encodings priced as transaction data: the
        RLP of the key list followed by the RLP of the sequence.
        """
        keys = tuple(U256(key) for key in nonce_keys)
        return bytes(rlp.encode(keys) + rlp.encode(U64(nonce_seq)))

    @classmethod
    def pre_allocation(cls) -> Mapping:
        """Pre-allocate the nonce manager system contract."""
        return {
            NONCE_MANAGER_ADDRESS: {
                "nonce": NONCE_MANAGER_NONCE,
                "code": NONCE_MANAGER_BYTECODE,
            }
        } | super(EIP8250, cls).pre_allocation()  # type: ignore

    @classmethod
    def activation_code_installs(cls) -> Mapping:
        """
        Initialize the nonce manager when the fork activates.

        The install writes the runtime code and raises the nonce to one,
        keeping a higher existing nonce and the balance; blockchain tests
        get the account from this hook at the fork block, so a fixture
        crossing the boundary exercises the initialization itself.
        """
        return {
            NONCE_MANAGER_ADDRESS: {
                "code": NONCE_MANAGER_BYTECODE,
                "nonce": NONCE_MANAGER_NONCE,
            },
        } | super(EIP8250, cls).activation_code_installs()  # type: ignore

    @classmethod
    def recorded_activation_installs(cls) -> FrozenSet[Address]:
        """
        Record the nonce manager's initialization in the fork block's
        block access list, at block access index 0.
        """
        parent = super(EIP8250, cls)
        inherited = parent.recorded_activation_installs()  # type: ignore
        return frozenset({Address(NONCE_MANAGER_ADDRESS)}) | inherited
