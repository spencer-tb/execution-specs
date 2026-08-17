"""Shared scaffold for making the EIP-8279 floor observable."""

from execution_testing import Fork

from .spec import Spec

COLD_SLOT = 0xBA1
STORAGE_KEY_FLOOR = Spec.BYTES_PER_STORAGE_KEY * Spec.FLOOR_PER_BYTE
STORAGE_VALUE_FLOOR = Spec.BYTES_PER_STORAGE_VALUE * Spec.FLOOR_PER_BYTE
ADDRESS_FLOOR = Spec.BYTES_PER_ADDRESS * Spec.FLOOR_PER_BYTE


def scaffold_data(fork: Fork, execution_headroom: int) -> bytes:
    """
    Return nonzero calldata whose EIP-7623 floor exceeds the intrinsic
    cost by at least `execution_headroom`, so the floor binds for any
    test body spending less than the headroom in execution gas.

    The intrinsic cost must be sampled in its pre-execution-deduction
    mode: the default mode already includes the floor, which the floor
    can then never exceed.
    """
    data_floor = fork.transaction_data_floor_cost_calculator()
    intrinsic = fork.transaction_intrinsic_cost_calculator()

    def floor_gap(size: int) -> int:
        data = b"\x01" * size
        return data_floor(data=data) - intrinsic(
            calldata=data, return_cost_deducted_prior_execution=True
        )

    gap_per_byte = floor_gap(1024) - floor_gap(1023)
    assert gap_per_byte > 0, "calldata floor cannot outgrow intrinsic cost"
    deficit = execution_headroom - floor_gap(1024)
    size = max(1, 1024 + -(-deficit // gap_per_byte))
    assert size <= 2**20, "scaffold data unreasonably large"
    assert floor_gap(size) >= execution_headroom
    return b"\x01" * size
