"""
EIP-7971: Hard Limits for Transient Storage.

Decrease costs for TLOAD and TSTORE with a transaction-global limit on
unique transient storage slots.

https://eips.ethereum.org/EIPS/eip-7971
"""

from dataclasses import replace
from typing import Callable, Dict

from execution_testing.vm import OpcodeBase, Opcodes

from ....base_fork import BaseFork
from ....gas_costs import GasCosts


class EIP7971(BaseFork):
    """EIP-7971 class."""

    @classmethod
    def gas_costs(cls) -> GasCosts:
        """
        Reprice transient storage with constant costs decoupled from
        warm access, plus an allocation cost for the first write to a
        slot in a transaction.
        """
        return replace(
            super(EIP7971, cls).gas_costs(),
            OPCODE_TLOAD=5,
            OPCODE_TSTORE=12,
            OPCODE_TSTORE_ALLOCATE=24,
        )

    @classmethod
    def opcode_gas_map(
        cls,
    ) -> Dict[OpcodeBase, int | Callable[[OpcodeBase], int]]:
        """Price TSTORE by the slot's allocation state."""
        gas_costs = cls.gas_costs()
        base_map = super(EIP7971, cls).opcode_gas_map()

        def tstore_cost(opcode: OpcodeBase) -> int:
            if opcode.metadata["slot_allocated"]:
                return gas_costs.OPCODE_TSTORE
            return gas_costs.OPCODE_TSTORE + gas_costs.OPCODE_TSTORE_ALLOCATE

        return {**base_map, Opcodes.TSTORE: tstore_cost}

    @classmethod
    def max_transient_storage_slots(cls) -> int | None:
        """Bound the unique transient slots written per transaction."""
        return 131072
