"""
EIP-7819: SETDELEGATE instruction.

https://eips.ethereum.org/EIPS/eip-7819
"""

from typing import Callable, Dict, List

from execution_testing.vm import OpcodeBase, Opcodes

from ....base_fork import BaseFork
from ....gas_costs import GasCosts


class EIP7819(BaseFork):
    """EIP-7819 class."""

    @classmethod
    def opcode_gas_map(
        cls,
    ) -> Dict[OpcodeBase, int | Callable[[OpcodeBase], int]]:
        """Add the SETDELEGATE execution gas cost."""
        gas_costs = cls.gas_costs()
        base_map = super(EIP7819, cls).opcode_gas_map()
        return {
            **base_map,
            Opcodes.SETDELEGATE: lambda op: cls._calculate_setdelegate_gas(
                op, gas_costs
            ),
        }

    @classmethod
    def opcode_state_map(
        cls,
    ) -> Dict[OpcodeBase, int | Callable[[OpcodeBase], int]]:
        """Add the SETDELEGATE state gas cost."""
        gas_costs = cls.gas_costs()
        base_map = super(EIP7819, cls).opcode_state_map()
        return {
            **base_map,
            Opcodes.SETDELEGATE: (
                lambda op: cls._calculate_setdelegate_state_gas(op, gas_costs)
            ),
        }

    @classmethod
    def opcode_state_refund_map(
        cls,
    ) -> Dict[OpcodeBase, int | Callable[[OpcodeBase], int]]:
        """Add the SETDELEGATE designation state-gas refill."""
        gas_costs = cls.gas_costs()
        base_map = super(EIP7819, cls).opcode_state_refund_map()
        return {
            **base_map,
            Opcodes.SETDELEGATE: (
                lambda op: gas_costs.AUTH_BASE
                if op.metadata["designation_cleared"]
                else 0
            ),
        }

    @classmethod
    def _calculate_setdelegate_gas(
        cls, opcode: OpcodeBase, gas_costs: GasCosts
    ) -> int:
        """
        Calculate the SETDELEGATE execution gas cost: the access cost
        of the written address plus `ACCOUNT_WRITE`.
        """
        metadata = opcode.metadata
        if metadata["address_warm"]:
            gas_cost = gas_costs.WARM_ACCESS
        else:
            gas_cost = gas_costs.COLD_ACCOUNT_ACCESS
        return gas_cost + gas_costs.ACCOUNT_WRITE

    @classmethod
    def _calculate_setdelegate_state_gas(
        cls, opcode: OpcodeBase, gas_costs: GasCosts
    ) -> int:
        """
        Calculate the SETDELEGATE state gas cost: `NEW_ACCOUNT` when
        the account leaf does not exist yet and `AUTH_BASE` when a
        net-new designation is written.
        """
        metadata = opcode.metadata
        state_gas = 0
        if metadata["account_new"]:
            state_gas += gas_costs.NEW_ACCOUNT
        if metadata["designation_new"]:
            state_gas += gas_costs.AUTH_BASE
        return state_gas

    @classmethod
    def valid_opcodes(cls) -> List[Opcodes]:
        """Add SETDELEGATE to valid opcodes."""
        return [
            Opcodes.SETDELEGATE,
        ] + super(EIP7819, cls).valid_opcodes()
