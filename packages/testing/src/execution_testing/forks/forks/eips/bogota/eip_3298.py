"""
EIP-3298: Removal of refunds.

https://eips.ethereum.org/EIPS/eip-3298
"""

from dataclasses import replace

from execution_testing.vm import OpcodeBase

from ....base_fork import BaseFork
from ....gas_costs import GasCosts


class EIP3298(BaseFork):
    """EIP-3298 class."""

    @classmethod
    def gas_costs(cls) -> GasCosts:
        """The storage-clearing refund leaves the gas schedule."""
        return replace(
            super(EIP3298, cls).gas_costs(),
            REFUND_STORAGE_CLEAR=0,
        )

    @classmethod
    def max_refund_quotient(cls) -> int:
        """
        EIP-3298 removes the EIP-3529 refund cap.

        A quotient of one leaves ``min(refund, gas_used // quotient)``
        equal to the full refund, since a refund never exceeds the gas
        charged in the same transaction.
        """
        return 1

    @classmethod
    def _calculate_sstore_refund(
        cls, opcode: OpcodeBase, gas_costs: GasCosts
    ) -> int:
        """
        Calculate the execution SSTORE gas refund.

        Only the net-metered STORAGE_WRITE reversal survives EIP-3298:
        the storage-clearing refund and its restoration reversal are
        removed with the constant.
        """
        metadata = opcode.metadata

        original_value = metadata["original_value"]
        current_value = metadata["current_value"]
        if current_value is None:
            current_value = original_value
        new_value = metadata["new_value"]

        refund = 0
        if current_value != new_value and original_value == new_value:
            # Refund the STORAGE_WRITE charged on the first-time
            # change earlier in the transaction.
            refund += (
                gas_costs.COLD_STORAGE_WRITE - gas_costs.COLD_STORAGE_ACCESS
            )

        return refund
